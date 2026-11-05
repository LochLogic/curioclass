# Music History Radio handoff

Offline Grade 9-12 listening instrument. Dial, Mixing desk and six-round Mystery station.
The original eight-phrase Traveler melody runs through twelve arrangements. No commits or shared-file changes.

## Source map

src.html contains responsive scene CSS, station data, compileBar, RadioAudio and application controls.
MS supplies the shared audio context, pitch, plucked instruments and recorder synthesis.
The local conductor supplies variable phrase lengths, drums, synthesized samples, static and room impulses.
Nothing is downloaded. The HTML bundle is generated from source and art tokens.

## Cold-review repairs

- Mixing desk tempo now follows Beat; chant is labeled free rhythm, including Compare.
- Mixed texture and melody-instrument rows describe the selected combination. They no longer promise drums
  or accompaniment that Chant Beat or Harmony has removed. Notation in the desk is labeled as an era reference.
- The conductor commits a new arrangement on the actual phrase boundary instead of 150 ms ahead.
  A request 70 ms before the boundary passed the targeted regression check. Tuning cancels a queued Flip.
- Mystery reveals and the six-choice recap now lead the feature panel. Compact reveals hide secondary notation.
- Postcards preserve their full 4:3 composition. Hip hop was repainted with a woman DJ and a natural community,
  including a wheelchair user. Its prompt is marked people: true. Full prompt and provenance are in prompts.json.
- Diatonic staff spacing, low-C ledger lines, dotted halves, lead-sheet chords and the hip hop drum grid were corrected.
- All fixed Read phrases are in allLines and voice/lines.json. Read starts with the current action hint.
  Browser speech remains the fallback; no narration was recorded.
- Paused hints name Resume. Returning to Dial snaps its needle to the audible station.
- After the single final audit, quick Station taps now preserve the still-valid Power-off welcome.
  A first Compare tap before Power speaks the Power instruction. Both paths were rechecked with held clicks.
- Audit-frame inspection caught overlapping dial years at 1000 pixels. The rail now has a readable minimum
  width at every size; pointer tuning maps to that visible scrolled rail. Compact and phone real drags passed.
- The live counter now says phrase, so organum's fourteen measures are not mislabeled as eight bars.

## Owner decision and cultural check

The owner requested a station outside the European and American line. Javanese gamelan fulfills it.
1889 is an international encounter anchor, not an invention date or a step in a universal progression.
Sundanese and Javanese artists performed at Paris. The original Javanese-inspired model does not reconstruct
the fair's mainly Sundanese repertoire. Equal-tempered pentatonic tuning is explicitly a simplification,
not traditional repertoire or authentic slendro / pelog tuning.

Sources in notes.md include Smithsonian Folkways, Smithsonian NMAA and UNESCO.
The fresh cultural wording and people-art review passed: refine/sensitivity.md.

## Timing and checks

compileBar returns events in seconds. Chant is free length; organum maps the eight melody phrases to
6/6/6/3/6/6/6/3 beats, fourteen 3/4 bars in total. The shared playhead counts melody phrases, not organum measures.
Every station preserves all 24 melody notes. Swing / disco / hip hop loops are 13.6 / 17 / 22.174 seconds.
All twelve loops are under 30 seconds. The spec's chant maximum calculation is wrong: 24 times .9 is 21.6 seconds.
All 1,728 mixes compiled with 232,380 finite events. This does not certify historical timbre by ear.

Controls are created once; render updates their values and labels without replacing focus.
On phones main scrolls above a separate footer. The panel follows the radio, so secondary details require scrolling.
Mystery results live in page memory only. Keyboard instructions are in notes.md.

Scratch contains the cold play, numbers, voice logs, targeted timing checks and review-audit output.
The cold-review report records the final audit outcome. The builder's codex-report.md remains its historical snapshot.
The audit completed with six leads: rapid Station welcome cuts were repaired; action-owned first speech,
Pause cutting its ident, and Reset at its unchanged starting value were examined and explained in the review.
There were no size, state, Motion-off, runtime, focus or resize failures. Only affected frames followed the repairs.

## Engine changes wanted

- kit/music-studio.js, play: explicit audio-clock start and variable-length phrase boundary hooks.
- kit/music-studio.js, instrument buses: a documented custom-voice bus with immediate cancellation and room sends.

No engine changed. The local conductor is retained because those APIs are unavailable.

## Left open

- By-ear listening and historical timbre / balance certification remain unperformed; all Chrome runs are muted.
- The requested recorded news-reader character cannot be guaranteed by browser speech.
- A fixed eight-phrase tune cannot demonstrate the full depth or repertoire of any historical tradition.
  Gamelan in particular is an explicitly simplified comparative arrangement.
