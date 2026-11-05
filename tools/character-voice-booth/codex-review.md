# Codex review: character-voice-booth

## Played
Grade 4 solo and projector paths: cold Booth, no-mic, Plan and Perform before builder notes/source.
Then synthetic MediaStream captures, checked Plan, Compare, Mystery guesses/Reveal, interruption, cancellation and Clear.
The booth and painted props are strong. The original tick-like ghost and small Reveal payoff were the flat spots.
Keyboard-only line/card/four-dial/Perform and Space playback passed; grayscale and Motion off were inspected.

## Findings fixed
- Blocker, general, Plan: grading used the student's baseline speed while the ghost used 2.5 words/s. Both now use 2.5.
- Should fix, general, baseline: a character recorded first was falsely called the usual voice. Chart and speech name the fallback baseline.
- Should fix, general, charts: segmented strokes broke prints into ticks. Continuous paths retain loudness widths and correct dash phase.
- Should fix, general, targets: range inputs were 23/28 px high. All are now 44 px, with compact controls still visible.
- Should fix, general, hints: denied-mic/card selection, completed Reveal and family switches now retain fitting instructions and drop stale speech.
- Should fix, general, keyboard: held R ignores repeat events rather than immediately stopping its own recording.
- Should fix, general, Plan: a planned pitch beyond the chart's measurable range now has an explicit edge warning.
- Should fix, general, graphics: tiny, mixed system emoji became six consistent, shaded SVG feeling expressions.
- Should fix, general, Reveal: six results were clipped at 680x425. The recap now scrolls by keyboard, with total and return action visible.
- Should fix, general, playback: Compare/Mystery animated a hidden Booth strip. The active chart now gets its playhead or Motion-off outline.
- Should fix, general, voice: a welcome could refer to controls behind the line dialog. A once-only dialog instruction speaks there; welcome waits for close.
- Should fix, general, Perform: the listener could see the answer prop. Visible and spoken instructions now tell the listener to look away.
- Polish, general, payoff: Mystery's earned total is prominent on the main stage, including compact layouts; revealed badges/hints are truthful.
- Polish, general, weakest painting: repainted the idle lamp with dark glass, retaining its detailed red case and warm studio lighting.

## Findings left
- Should fix, spec: four internal pauses cannot fit between four words. The existing three-of-four warning stays; see Left open.
- Polish, layout: 375 px keeps actions first and places full plots below the fold. Readable history remains scrollable.

## Flattest moment left
Plan's usual ghost is deliberately a level line. It needs a live performance or measured take to become interesting.

## Graphics
All 12 paintings inspected, including large performance props; one idle-lamp redraw and six code-face redraws.
The imagegen edit used the existing lamp as reference; final prompt is in art/prompts.json and raw output in art/raw/lamp-off.png.
All specified art is present and used. No people assets, missing paintings or stereotypes found.
Art: 310.6 KiB. Final bundle: 512.5 KiB, 524849 bytes. Snowy Mail Route and Beat Lab were viewed as finish bars.

## Audit
One full audit completed in 1588.41 seconds, below 40 minutes: _scratch/character-voice-booth/review-audit/audit.md.
All 85 audit frames were inspected. Default sizes, repeat taps, rapid taps, Motion off and resize stress were clean.
Its 12 mechanical leads were reviewed: two expected modal-hint warnings; three history-scroll warnings;
three phone-plot visibility warnings; three correct first-tap own-line welcome skips; one drawing-animation keep warning.
The shelf recipe now waits 800 ms, beyond the specified 600 ms draw. Settled shelf frames confirm the newest print is visible.
The frames exposed the clipped Reveal recap and dialog narration issue; those and the hidden playback feedback were fixed.
Only affected states were re-shot afterward: recap top/bottom, phone recap, active-chart playback, modal speech and Perform instructions.
Focused drive batches had zero browser console errors. The full audit was not rerun after those scoped fixes.

Five-take narration counts, from review-five-take-voice.json:

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| First-take character instruction | how | 1 | 1 |
| Tap Compare | how | 1 | 1 |
| Baseline result | event | 1 | 1 |
| This take is | event | 4 | 4 |

Pitch/speed result parts each spoke four times. One stale comparison tail was dropped when a newer take arrived.
The line dialog spoke its own instruction, then the welcome after close. All 74 fixed lines match the final voice manifest.
Actual AudioWorklet capture of synthetic 220/330 Hz streams read +7.0 steps, faster delivery and +9.9 dB.
Capture windows had zero spoken narration entries; mic tracks ended; Play switching, mode interruption and count-in cancellation passed.
A deliberately fast baseline still yielded four correct usual-plan matches. Explicit permission denial retained Go to Plan after a card change.
Loudness-only +10 dB passed the fair test; pitch plus loudness failed and named both. Mystery matched 3 of 3 and cleared guesses.
The seventh take preserved the baseline; Clear left no take buffers or chunks. Audio has no authored localStorage path.
Recomputed 7.01955 steps, 7.81818 s longest ghost, 1 s shortest ghost, five speed ratios and all six stated contrast pairs.
Wave lessons checked: current hints/Read, stable focus, visible choices/targets, hidden answers, honest bins, all five theatre standards,
Motion off, resize, truthful badges, reversible hints and no word-copy answer. Notes retain the three required opening sections.

## Left open
The spec requests four between-word pauses on the four-word line. Kept its explicit three-gap limit; changing the line or notch needs a spec decision.
Narration uses browser fallback; recordings remain absent under the brief's no-recording rule. No live classroom/human-voice trial was run.
Embedded microphone permission is controlled by the host page. The denied-mic Plan path works; no shared host template was changed.
No engine changes, git commits, owned Chrome/server processes or tools-folder host.html remain. One review pass only.
