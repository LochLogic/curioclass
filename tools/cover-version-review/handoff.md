# Cover Version Review: build handoff

## Structure
One offline source, `src.html`, using kit:curio and kit:music-studio.
CSS defines the record-sleeve desk, a responsive difference strip, the transport and each mode's controls.
The script contains the content table, melody, persistence, voice queue, strip, measurement model,
review writer and two gain buses. `window.__tool` exposes state and focused verification hooks.
Controls precede the eight line buttons in DOM tab order. CSS places the strip first on desktop.
At 375 pixels, lyric lines become rows and A/B sit side by side; playback and recording controls stay above them.
Compact measurement windows use a selector to show each complete group of recording choices.
My taste opens as a native closing-card dialog so both sliders and the sentence controls stay visible together.
The Review writer keeps My taste and Copy review next to Add claim, including on phones.

## Tricky parts
- A/B crossfades gain buses over 30 milliseconds. Both buses use a shared beat position, with the audible
  version setting the rate. The switch preserves that beat, not elapsed seconds.
  Active vowel/brass envelopes are retimed to the new version's remaining beat duration when it flips.
- A's last two beats on lines 4 and 7 ease linearly to 80 percent of the listed tempo.
  The clock integrates that curve analytically. Real full plays measured 68.86 and 50.09 seconds.
- The local scheduler uses the page clock and short Web Audio dispatches. MS.parse supplies pitch events;
  MS.pluck supplies guitar and the engine's piano voice supplies Plain tune. Local formant, brass and snare
  implementations are in the source because the shared kit is read-only during this build.
- During music, narration stays silent. Events are deferred to stop. Repeated event instances get unique
  queue keys so a newer claim does not erase an earlier pending claim. Read stops music first.
- Measurements are per line and version. Check covers all recorded fields, including extras, and reveals
  truth only on recorded lines. The count covers tempo, loudness and instrument cells, excluding extras.
- Review evidence accepts matching measurements or checked truth. It does not accept an unchecked guess.
  A Both pin plays A and then B. A named-version pin plays only that version.
- All saves are wrapped localStorage calls. Reset uses a native dialog with a safe initial focus and clears
  every saved field. Clipboard has a plain-text fallback. Nothing is recorded or sent anywhere.

## Spec choices and open questions
- Voice: kept calm-professor / Schedar, as the spec leans. Its use in a different grade's gallery tool does
  not override this explicit selection. No recording was made; the kit uses browser speech until later narration work.
- Engine conflict: followed CODEX-BUILD's ban on kit and docs changes. Implemented the required extra synth
  voices locally, with the shared change request below.
- Historical printing: no authenticated pre-1930 printing was verified. The Archive/Wikimedia item with an
  1848 catalogue date is a Robert A. Hudson modern engraving with Finale PrintMusic 2009 metadata.
  The supplied public-domain melody was implemented with pickups inside each lyric column and durations
  normalized to eight beats. Notes name the consulted score and the Chambers pitch reference.
  Verification against an authenticated printing remains open. Do not treat this as a verified historical transcription.
- A line 8: the table specifies Voice only, while the prose says the second repeat removes guitar.
  Followed the explicit instrument table: Voice only on both passes. The repeated line is audible, but there
  is consequently no guitar removal between its passes. This contradiction remains for the owner/reviewer.
- Slowdown: used the specified gradual easing, rather than holding the final two beats at 80 percent throughout.
  Recomputed duration 68.82 seconds versus the supplied 69.4-second upper estimate, within its one-second tolerance.
- Repeat clips: Play line plays one eight-beat line for short comparison. Play all performs the additional
  repeats, B's intro/outro and tag. Switching from B's non-lyric intro/outro to A starts the selected lyric line,
  since A has no corresponding instrumental section.
- Extra labels abbreviate only in short previews (held, slows, repeat, shout, key up arrow).
  Their title text and the Measure controls keep the full names.
- Added a matching claim-added voice variant for a named-version pin: it says "this version" instead of
  "both versions". STANDARDS requires the spoken line to match the actual playback. Empty pins without
  reliable evidence direct the student to Measure and do not speak the unavailable evidence-chip instruction.
- Check uses a compact two-line result per lane. In short previews, the off badge sits beside the true value
  to preserve legibility. Full windows put the true value beneath the recorded value.

## Art
Eight original generated paintings, all present and used: two venue sleeves and six instrument cutouts.
Full prompts and provenance are in `art/prompts.json`; raw originals are in `art/raw/`.
The images contain no people. No artwork remains to paint.

## Engine changes wanted
- `kit/music-studio.js`, instrument functions / INSTR: add formant ah and oo voices using two bandpass formants,
  filtered sawtooth brass voices and a snare noise envelope. Preserve existing instrument calls.
- `kit/music-studio.js`, play(): expose or accept a per-player gain bus and support a beat-aligned seek / rate
  anchor. The current private bus prevents direct use of MS.play for a 30-millisecond A/B crossfade.
- Update `docs/families/music-studio.md` with those APIs in the same shared change. No shared files were edited here.

## Verification pointers
Evidence, bar copies, screenshots and timeout wrappers are under `_scratch/cover-version-review/`.
`functional.json` records real held taps, comparison cells, pin playback, full durations and reset.
`voice-check.json` records repeat narration. `clipboard-check.json` records the corrected real clipboard check,
including Windows line-ending normalization. `static-check.json` checks all 64 content fields.
The final report records the audit outcome and any remaining limitations. This was Build only, without a commit.

## Audit dispositions
The single full audit completed with 36 leads. Post-audit focused checks cover its confirmed fixes: 44-pixel minimum
widths, explanation-input name, unknown/check lane spacing, 760-pixel instrument layout, the taste dialog, long-word
wrapping and same-mode clicks preserving a welcome already in progress. The compact recorded-state fixture now
opens the measurement selector before choosing loudness. Modal fixtures keep the modal itself in view.
Phone lyric rows intentionally scroll as the spec requires. A music-first tap intentionally suppresses the welcome
so narration cannot overlap music. The full audit was not rerun after the targeted fixes.
