# Recorder Concert Rehearsal handoff

## Build and layout

`src.html` starts from the kit starter. It contains tool CSS, permanent controls, then content, deterministic take generation,
instrument adapters, rendering, transport, rehearsal rules, concert rules and event bindings. `window.__tool` exposes state,
pure `eventsFor`, pure `applyNote`, random generation, mode switching and voice logs for inspection.

The room uses the painted backgrounds with eight keyed animal pose assets. Name tags use both numbered badge shapes and colors.
The DOM puts the panel before the scene for keyboard access. CSS keeps it on the right on laptops and underneath the stage on phones.
Bar buttons appear above the room visually but follow the players in keyboard order.
At short landscape sizes the note builder uses a tray across the bottom. Score view occupies the lower third of the room;
its SVG is measured in actual pixels rather than shrinking a fixed scene.
On phones in Play with them, the next fingering sits beside the staff and Slower sits beside Play.
After a take, six unfiltered note cards fit a three-column tray. At compact sizes, Piece, New rehearsal and Start over
move beside Score view and Hear everyone so they remain available without hiding any note choices.
Resize restores these controls to the panel while preserving focus. Phone bar strips with eight bars use two rows of four.

## Musical model

`MS.parse` supplies both traditional melodies. Written pitch is converted to key G with a one-octave sounding transposition.
The instrument compensates for the engine's rounded middle-C constant so A is exactly 440 in octave 4 and 880 in octave 5.
Each take produces a stable merged event list with player, bar, original beat and issue annotations.
The rush warps bar 3 and all following onsets, keeping the ending together. The late onset delays only the culprit's first note.
Breath shortens the last note before an internal bar boundary; random breath locations exclude phrase ends.
Random squeaks choose only bars containing G. Identical problem lists produce identical event lists, with no random audio variation.

`applyNote` removes at most one matching problem. Only late accepts Whole piece. Everyone is the culprit only for rush.
Each piece keeps a pending note until its next completed take. A second Give note asks the student to listen first,
including after switching pieces. Giving a note from a scrolled page returns to Play and focuses it without a focus scroll.
The take number increments on Give note. Latest settings are saved after a take finishes, so Then and now uses completed takes.
Start over replaces only the chosen piece's notes and settings. Storage is validated and wrapped in try/catch.

`MS.play` supplies the clock, count-in and live tempo. All player instruments call `MS.blow` through stereo gain routes.
Silent layers remain scheduled so Solo can reveal a held note immediately. A loop tap cuts the old transport and re-anchors
the requested bar with no count-in. Stop fades through the engine. Narration is hushed before music; Read stops music first.

## Voice

The requested bank is big-sister, Leda. No audio was recorded, as required by this build brief.
`Curio.voice` supplies the queue and browser-speech fallback. The tool owns the hint, with Read reading its current text.
How lines use `V.heard` through the helper; fixed, noChange, notThem, ready and manners lines are events.
The mode scope is mode plus piece. Result lines wait until a completed take and expire at the next playback.

## Art

Ten built-in imagegen calls produced ten individual PNG assets, copied to art/raw and processed only with `art.py --rekey <name>`.
Animal assets use a green key and despill. Full prompts and house style are in art/prompts.json; `drawn_by` is codex.
The holes option removes residual green from whiskers and fur. Each asset was inspected on the contact sheet and in the scene.
The art is animals and unoccupied settings. The audience is code silhouettes. No generated people or recorded audio.

## Open questions

The specification lists no open questions for Cory.

## Engine changes wanted

- `kit/music-studio.js`, `play`: support per-event `pan` by routing the event bus through a StereoPannerNode.
  Current tool workaround registers per-player instruments and routes their dry sound through stereo panners.
- `kit/music-studio.js`, `blow`: accept an optional vibrato-depth multiplier, default 1, so a recorder can pass 0.5.
  Current scoped adapter intercepts the second createGain call and halves only that vibrato AudioParam assignment,
  restoring createGain in finally. This relies on the current blow implementation and deserves a stable engine option.
- No fractional pitch change is needed: `MS.freq` already accepts 0.4 semitones.

## Next review

The 2026-11-04 cold review played the whole tool before reading the builder documents. No commit was made.
Use the saved event-list tests and held-click journey to distinguish synthesis inspection from an actual headphone review.
Browser speech quality differs from the specified recorded Leda voice; recording remains owner work.
The cold review repaired phone and compact note-building. All six unfiltered cards, the players, bars and Play fit
without scrolling, including the eight-bar phone Score view. layoutNotes and layoutJoin preserve focus when moving controls.

## Final verification

The audit completed once with 55 leads. Dispositions are in the tool report and scratch/audit-responses.md.
Final repairs received focused held-click, keyboard, phone-guide and live-resize checks, all without console errors.
All test Chrome instances and host servers are closed, and host.html is removed.
Scratch write_tool.py generated the first draft only. The final owning source is src.html; do not rerun that generator.

## Cold review repairs, 2026-11-04

- Concert invitation waits for a completed clean take. endTake consumes the pending result before rendering the invitation.
- Checklist marks are independent; the last-tapped criterion filters cards. Marks reset after each completed take.
- Give note returns focus to Play when the builder closes. The how-to now names an actual checklist control.
- Leaving a tuning moment stops its audio. Failed gated navigation refreshes transport controls.
- The tuning label follows the actual sounding event; the audience quiets visually and the shared bow follows a held pause.
- Otis playing pose was redrawn from his resting pose with built-in imagegen, then finished with art.py --rekey.
  All ten images remain; the layered audience remains code silhouettes. No generated people or recorded audio.
- Audit states now include all six cards and eight-bar phone Score view. Review evidence is under Scratch.

## Cold review final verification

The review audit completed once on 2026-11-04, within its 2400-second limit, with 39 frames and 23 leads.
Ten real layout leads were corrected: three caption/player overlaps, six score-label overlaps, and the phone history keep region.
The remaining leads are three intentional scrolling-staff text groups and ten skipped welcomes on music-start controls.
All controls and Enter paths, repeated/quick clicks, Motion off, and action resizing were mechanically clean.
The audited frames also prompted phone join-choice fitting and scoping audience chatter to manners only.
Compare identifies First/Final in the transport hint and refreshes transport when its piece selector stops playback.
Only five affected frames were re-shot afterward. Targeted checks are clean except the intentional offscreen staff notes;
there was no second full audit. Audit dispositions and final metrics are in Scratch.

Both fresh scripted pieces completed in four actual takes, with no early invitation. Two thousand random rehearsals
had three distinct solvable, sound-changing problems. A five-take held-click run spoke noChange four times and markHow once.
Wrong player/bar/vague event lists, independent marks, voice-manifest equality, storage keys, and rapid Read/mode changes passed.
All test Chrome instances and the host are closed; host.html is absent. No commits or shared-file changes were made.
