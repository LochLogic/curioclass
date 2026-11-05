# Name Song Practice handoff

Built and cold-reviewed in one review pass. No git commit or deployment.

## Implementation
src.html starts from the kit starter. Local responsive CSS and semantic controls precede the tool logic. The logic contains the song generator, stable-control renderer, practice state machine, local synthesizer, audio-clock scheduler, memory-only recorder and microphone lifecycle.

Curio.voice owns narration and Read; Curio.audio provides the shared audio context. Music uses a 25 ms lookahead with a 75 ms horizon. The ball and count-in read AudioContext.currentTime. Feeling changes invalidate a future scheduled beat and rebuild it. Resize changes only CSS geometry, so notes are measured again without resetting playback.

The four bars stay across on landscape previews and use a two-by-two arrangement on phones. Notes use readable visual spacing, with extra room for longer favorite words; exact durations are in the event model and note titles. Lyrics share a baseline below both staff lines. Multiple name syllables use neutral dots because names are never typed or stored. The second take's chosen fix is reused in Perform when Take 2 or Both good is selected.

Compact Practice keeps a full-width song strip, with microphone/reset controls beside the lower action row and privacy text below it. Compact Perform places the four feelings in the top control row to preserve audience height. The song-control toolbar is a semantic header so the audit's mode discovery can find it. Microphone input releases when leaving Practice, with existing take blobs retained for comparison.

All 17 painted assets are in art/ with generated originals in art/raw/. Prompts and provenance are in art/prompts.json. Generated using the built-in OpenAI image tool, then processed only with art.py --rekey. No people were generated.

## Open question decisions
- Microphone: retained, off by default, following the option developed throughout the spec. Permission is requested on the explicit toggle. At most two audio blobs stay only in page memory. Thumbs remains the full alternative.

## Engine changes wanted
None required. No kit files were changed. A future shared music scheduler could extract the local lookahead and source-cancellation routines, but this spec has no family engine.

## Remaining classroom check
Listen to the four accompaniments and browser narration on an actual classroom device. The loudness display is illustrative and is labelled as such. Plush comments cycle as scripted encouragement and do not analyze the class. The manifest names big-sister/Leda, but this build did not record narration, as instructed.

Evidence, bounded command runner, reference bundles, frames and mechanical audit output are in _scratch/name-song-practice/. The final report records tested results and remaining limits.

## Cold review repairs
Cold play preceded this handoff and the source. Compact Clear words lyrics had collisions; the strip now uses the full width, with space weighted toward actual words and a wider last phrase. Compact and phone words enlarge from 11 to 16.5 px. Take comparison shows the actual take-2 fix, and the selected take remains on the cue badge.

Feeling changes now retime a held syllable and its oscillator at the next beat, so the ball follows the changed tempo. Song-change confirmation speech is hushed on close or cancellation. The soccer card was redrawn with built-in OpenAI image generation and processed only with art.py --rekey soccer.

Review evidence and the single final audit are in _scratch/name-song-practice/. Browser voice fallback remains because narration recording is prohibited by the build brief. No classroom acoustic calibration is claimed.

The review audit completed once within the 40-minute cap: 81 frames, 31 leads. Fourteen duplicate layout leads were repaired by moving the compact badge and tightening phone lyric line boxes. Two large-screen span-box overlaps were removed without moving the words. Fifteen welcome warnings follow the required first-tap and incomplete-song guards. The eight final targeted frames report no collisions or invalid control geometry and no console errors. The full audit was not repeated after those scoped repairs.
