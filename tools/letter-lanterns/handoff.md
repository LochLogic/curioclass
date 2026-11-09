# Handoff: Letter Lanterns

## Structure

This fix follows the user's Curiosity instruction over the older lesson-shaped spec and Refine. The village fills the screen, with its own wooden controls and power panel. There is no kit stylesheet, header, welcome gate, quiz, score, mastery rating, earned badge or end screen. The lower-left Manual contains operation, model limits, privacy, discoveries and named sources with licence status.

`src.html` uses the kit only for `Curio.voice`, tones, Motion, Sound and Read. `lesson.json` bundles the supplied names, words, letter geometry and art placement. All 96 existing illustrations remain available through their existing asset map. No new artwork or topic was added. `tool.draft.json` has `curiosity: true`; `plate` is null because neither the spec nor the concept catalogue assigns Letter Lanterns a Curiosity number. The engraved plate therefore omits an invented number.

The three freely selectable views are Lanterns, Street and Wordbook. The tray chooses any enabled letter or any supplied sign, twin pair, vowel pair or banner. Touching a letter lights it; this is an exploration mark, never a measure of knowledge. Settings can hide content, light all, or clear the village. No activity unlocks another.

## Tricky parts

- `wordGlyph` renders a whole word in one SVG with fixed .85 advances, top line 0, midline .5, baseline 1 and descender 1.5. Signs, twins, vowel boards and banners use this layout. `glyph` may still crop a single isolated letter to fit a lantern's painted glass.
- Sound sequences are separate from displayed text. `intro.<letter>`, `short.<vowel>`, `long.<vowel>` and `twinDiff.<pair>` reference reusable `sound.<letter>` or `longSound.<vowel>` pieces. `resolveSequence` substitutes an anchor-word line if an isolated recording is unavailable; a bare consonant or short-vowel letter never falls through to browser TTS as its sound. All fixed narration remains in `voice/lines.json`, equal to `allLines()`.
- The voice manifest selects playful-friend / Laomedeia. No recordings were made. All 31 isolated sound recordings still need Forge production and listening approval. Queue logs prove routing and timing, not acoustic correctness. This remains the substantive limitation of Refine blocker 1.
- Twin windows always begin hidden on entering a pair, including previously opened shops. Both windows are freely revealable. The changed letter gets amber light and flicker; cyan is reserved for keyboard focus.
- The slate retains the reviewed direction, coverage, end and ordered-progress evaluator. It is an optional drawing aid. A matching stroke moves to the next trail; three misses can demonstrate the trail. Next stroke and Back to lantern are always available. No badge, score or required sequence is attached. A free-drawing miss overlays every path of the whole letter.
- Street lanterns have identical 60 by 80 hit boxes. Their string wraps with room reserved above the shops. Compact landscape and phone layouts hide the string and use a hint that does not name it. The 760 by 900 view shows all 26 in three rows.
- Version 2 local saves hold exploratory choices and touched/opened objects. Version 1 saves can retain touched letters and opened shops, with their former ratings discarded. Invalid saves start from the default village.
- Read owns the current hint. Settings Read includes its privacy line. Routine Settings narration is a how line, once per load; privacy stays visible and readable. Taps invalidate stale queued speech and act immediately. Mode changes cancel street reading.

## Inspection and evidence

`window.__tool` exposes state, setMode, render, save, validSave, allLines, vlog, vq, data, assessTrace, resample, currentPath, slatePoint, wordGlyph, selectLetter, section, beginTrace, resolveSequence, sequences, reading and audioReady.

Before evidence, scripts, numerical results and after frames are under `_scratch/letter-lanterns/`. The unmodified source and data are preserved there. The final mechanical audit is `fix-audit/`. Read `polish.md` for item-by-item status and any audit limitations. Do not mistake an old lesson audit state or historical build report for the current interface.

The audit's automatic mode selector only searches headers. This tool has no header, so `audit-states.json` explicitly walks all three views and every material interaction, with real clicks. No shared audit script was changed.

## Sources and rights

The Manual, teacher notes and `tool.draft.json` name the same source families and distinguish original Curio Class material (CC BY 4.0, code MIT) from copyrighted reference works. Reading Rockets, Speech to Print, CCSS, Zaner-Bloser and Learning Without Tears are references; their articles, books and chart images are not bundled. The supplied ten-banner selection is retained without copying a full Dolch or Fry compilation or asserting an open licence for Fry. No external dataset or artwork was downloaded into the product.

## Sensitivity

Fictional village, no human figures, no personal prompts and no microphone. US English anchor words do not model every dialect. No cultural or medical claims were introduced.

## Art still to paint

None. The existing art is retained. Isolated phoneme recording and listening review are separate from art.

## Engine changes wanted

None in the kit. A future audit enhancement could include `nav button[aria-pressed]` in `scripts/audit_tool.py` `MODES_JS`, so Curiosity views are detected without a lesson header. The current explicit audit states cover them.

## Left open

- Produce and listen to the 31 isolated sound clips and the fixed narration in the selected bank voice. No acoustic pass is claimed.
- Assign the Curiosity plate number outside this task; no number was supplied and none was invented.
- The four-question Curiosity test is a judgement, not a mechanical pass. The real sounds must be finished before the authenticity question can receive an unqualified yes.

## Final audit and corrective verification

The full audit completed once with 82 leads. Its frozen input is preserved in Scratch as `audit-input.html` and `audit-input-src.html`, with SHA-256. After that audit, a focused corrective pass fixed the confirmed geometry and source-link targets. The full audit was not repeated. `corrective1/`, `corrective2/`, `final-hints/` and their JSON measurements cover the affected cases; `final-validation.json` records the final bundle hash. The source-link minimum is 60x60, and board lanterns are centered on the actual drawn vowel bounds to within 0.01 px. The final zero-letter hint distinguishes a fresh street from an already-opened shop, and all-hidden content keeps its Settings hint after resize.

Accepted polish 19 remains only partly addressed: height-based sizing is in place, but exact cart-rim seating for every creature is not approved. The 31 isolated recordings remain acoustically open. See `polish.md` for the complete per-item dispositions.
