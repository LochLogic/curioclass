# Codex report: feeling-scarf-dance

## Built

Four modes: Build, Watch, Your turn and Share. Five feeling tracks and patterned scarves, five start/end shapes, six middle moves, 4+8+4 engine phrases, live edits, Slow, Mirror, quiet Freeze and audience observations. Uses the kit starter, Curio.voice and Dance engine. Build only, no git commit or polish round. All repository writes are within the tool folder and its Scratch folder.

## Numbers check

Scratch compute_numbers.py recomputed all spec numbers. Sixteen counts / with four-count introduction, seconds: Happy 8.571 / 10.714; Sad 14.545 / 18.182; Calm 13.333 / 16.667; Mad 9.600 / 12.000; Surprised 10.000 / 12.500. Normal runs match the rounded spec values.

Contrast ratios: white/brand 7.155, brand/paper 6.713, ink/paper 15.873, muted/paper 6.428. All match the spec rounding. Twenty-four points have 23 segments, so spacing is 1.1 / 23 = 0.047826 body heights; the spec's 0.046 value assumes 24 links. The implementation preserves the required 24 points and total length. All named shape/gait references resolve in the actual engine.

## Feel check

Best moment: Zap whips the patterned silk across the sky, then Your turn removes the figure so the same scarf is the class's movement cue. The full Happy performance ends in a high held shape with a quiet Freeze.

Two flat moments repaired during this Build: the cloth originally fell below the stage, so it now settles on the painted grass; compact cards originally had tiny figures in large empty boxes, so their figure area grew and their height is capped. Build's middle/end prompts now name the part card to tap. The temporary kit figure remains visibly simpler than the intended painted dancer.

Played all four modes through Build, Watch, Your turn, audience chips and Swap. Five real-time Watch runs and a full Your turn run completed. Compared the Zap frame against Snowy Mail Route in Scratch feel-comparison.png; opened Beat Lab as the second quality bar. The landscape, silk sheen, patterns and physical response carry the finish; the owner's painted figure is the remaining art step. No ten-minute super-tool claim is made.

## Done when

1. PASS: Watch centers the figure and scarf; Your turn hides the figure and leaves a large scarf with readable part word. Inspected 1366x768 and 680x425 frames.
2. PASS: all 750 feeling/start/move/end combinations sampled at all 16 counts, no invalid pose values; five real-time feeling runs ended at count 16 without console errors. Combination sampling is not 750 real-time runs.
3. PASS: six focused motion frames show Float's arc, Swirl's turn, Zap's snap, Melt's low drape, Shiver's flutter and Leap's trailing cloth.
4. PASS: held-click live edits changed Middle to Zap, feeling to Sad and Slow to 46.2 bpm on the next count. The phrase proxy blends edits over 180 ms. Mirror flips immediately; Stop's scarf remained byte-for-byte unchanged after 350 ms.
5. PASS: real-time logs contain only end narration after the music. Read stops an active run before speaking. Sound off/on during a run did not queue a welcome.
6. PASS: both modes use the same phrase and scarf simulation. Your turn hides the figure and retains a 12 percent hand marker. End showed Freeze, a still scarf and no speech for the sampled quiet hold; full-run log started the freeze reminder after three quiet seconds.
7. PASS: chips check/uncheck, five repeated Start chip taps produced five event lines, and Swap clears observations. Other chip lines are also declared event keys.
8. PASS: at two-second held-click pace, the Middle how-to started once across five taps, then was silent as heard. Stale queued copies were dropped.
9. PASS: 28 full size/mode frames plus four 375-pixel iframe frames. Measurements found zero controls below 60 px, zero horizontal overflow and zero below-viewport buttons. Play and Go remain visible. All controls combine an icon/figure/trace with a word.
10. PASS with shared-setting exception: Motion off keeps count timing and a straight scarf (measured horizontal spread zero); no infinite CSS movement. Static bundle scan found no fetch, remote resource, unresolved art or network library. Dance and observations are memory-only; the required shared kit remembers Motion preference.

## Wave lessons

- Hint and voice: PASS. Direct synchronous hint updates; Read uses the current hint; incomplete Watch/Your turn names Build; how-to keys use Curio.voice heard tracking. Music never waits behind a stale line.
- Focus and layout: PASS. Stable outer controls, no focus on load, preventScroll on deliberate focus; keyboard-only Build-to-Watch and Play/Stop ended with focus on Play. Hint space is reserved.
- Sizes: PASS. Every standing size, every mode and a 375-pixel hosted iframe were inspected; all control targets measured at least 60 px.
- No giveaways: PASS, expressive creation has no hidden answer, ranking, score or correct-feeling association.
- Honest numbers: PASS. Counts and tempos use the engine clock; Slow is 70 percent. Number/contrast recomputation is in Scratch.
- Standards: PASS for the teacher-led spec. Building three parts practices DA:Cr2; Your turn performance and audience observation support DA:Pr6; teacher notes invite a lived-experience feeling connection for DA:Cn10.
- Motion off: PASS. One pose per count, straight scarf, same real-time clock; idle drawing and CSS breeze stop.
- Short choices visible: PASS. Only the selected part's complete choice set is shown; no choice scroll panels. The choice menu shows all five or six options.
- Resize mid-animation: PASS. The one full audit reports no exception and no control left disabled after resizing every explicit reached state and changed walked control.
- Deferred welcome: PASS. Multiple modes use the standard welcome mechanism; first action lines supersede stale welcomes, with no welcomeAfter.
- Unknown as unknown: PASS. Incomplete part cards say Choose; Play/Go are disabled and Build is named in the hint. Incomplete performance says Build first and Choose a feeling.
- One look, one meaning: PASS. Pattern and face/word accompany every scarf color; selected cards and running parts have distinct context.
- Badge truth: PASS. Part names and feeling labels update from current state; no score or success badge.
- Reversible hints: PASS. Changes between modes, dialogs, stop and missing choices update Read's current hint.
- No copying-word answer: PASS, no diagnostic quiz or hidden answer exists.

## Audit leads

The one full audit completed within its 40-minute limit and produced 27 leads. All eight base sizes are clean; Motion off is clean; resize stress reports no exceptions or stuck disabled controls. All 47 audit frames were reviewed in twelve contact sheets. The audit was not rerun after the focused repairs below.

- Built-dance stale how-to: intentional. Feeling idea fills the start shape, so the previously queued "Tap a start shape" instruction is obsolete and is dropped. No line is marked heard by hand. Feeling idea as the very first tap now avoids queuing that obsolete instruction at all.
- Live-editor #hint keep region: native modal backdrop intentionally makes the background footer inert. It stays visually legible; the current menu has a clear heading, all options and an in-menu Read control. The added Read control stops music and reads the current choice hint. Focused checks cover 680x425, 1366x768 and a 375-pixel iframe.
- Welcome skips on m-watch and m-turn: intentional while the dance is incomplete. Their Play/Go welcomes would name disabled controls; the available Build control is voiced instead.
- Welcome skips on feelings 0 to 4, Start/Middle/End, shape options 0 to 4 and Feeling idea: intentional first-action behavior. Each tap has its own relevant event or how-to and suppresses the obsolete welcome. End's first instruction was repaired so it always speaks an enabled action.
- The Middle card shifts four option buttons when it replaces five shapes with six moves. That is the intended change of choice set; the part strip, hint and action bar remain stable and nothing rebuilds under the clicked card.
- Four repeated-name leads (Happy, Sad, Calm, Mad): repaired with unique event queue keys. The follow-up tests check all five feeling names, five held taps each at two-second pace, without replacing an earlier same-name event.
- Four quick-mode cuts (Build, Watch, Your turn, Share): repaired. Tapping the current mode no longer hushes its own instruction or restarts a run. Focused quick-tap checks exercise all four.
- Follow-up results: all 25 feeling events spoke, zero event drops; all four quick-mode logs had zero cuts. End-first spoke its enabled instruction and Feeling idea first spoke only its relevant event. Narrow-stage checks sampled 330 frames across six moves with zero scarf-center points outside the stage, with an added inset for the ribbon width. This is a sampled bound check, not exhaustive trajectory proof.
- No runtime, focus-loss or control-jump failure was reported. Sound's cut welcome is the intended Sound-off hush, and Read is allowed to skip the welcome.
- Audit coverage limitation: automatic mode discovery only searches header, whereas this tool has a separate nav. Explicit reached-state checks cover all four modes; the automatic default walk does not exhaustively walk the other three. Manual held-click runs cover their main interactions.

## Frames looked at

Scratch barframes: both quality bars. early-frames: five initial size/layout frames. focused-frames: ten move, editor, calm and audience frames. run-frames: five complete feeling endings. special-frames: seven live-edit, Freeze, Mirror, grayscale, voice, keyboard and combination frames. extra-frames: four keyboard, full Your turn, repeated how-to and Read frames. matrix-frames: all 28 mode/size frames, reviewed in seven contact sheets. phone-frames: four modes in a true 375x812 iframe. final-focused-frames: six compact, incomplete, Sound and Motion-off frames. Audit: 47 frames in twelve contact sheets. Post-audit: menu Read at three sizes, narrow Swirl, and targeted voice repairs; 11 repair frames, three final narrow-stage frames, three menu/narrow frames and one menu frame in a true 375-pixel iframe were inspected.

## Art made

Two images made with the built-in image tool, no people: hilltop (1500x844) and silk (384x384), selected without a redraw. Full prompts and house style are in art/prompts.json, originals in art/raw, processed with art.py --rekey only. Final WebP art is 92,626 bytes (90.5 KiB). Final offline bundle: 399,221 bytes (389.9 KiB), below 2 MB.

## Art still to paint

Eleven people:true manifest entries cover five held shapes and six multi-phase moves. The next painter needs consistent facings, full bodies, pose phases and right-hand registration. createDancerRenderer is the swap boundary. Current kit figure is temporary by owner decision. No people, faces or body parts were generated.

## Engine changes wanted

See handoff.md for the exact dance.md table row, an optional full-height square backdrop without the platform, and optional in-memory-only kit Motion preference. No kit or shared doc was edited.

## Left open

- Painted dancer assets are intentionally deferred to the next painter.
- Forty-four narration lines use browser speech; the requested soft-breath / Enceladus bank is declared, with no recordings made in Build.
- Muted browser checks verify scheduling and state, not headphone timbre or classroom loudness. Calm's soft chime uses the engine's high-register piano.
- The tool-local grass contact constraint and reduced-motion camera adjustment are documented specification interpretations.
- The full audit predates the focused narration, menu Read and narrow-scarf repairs. Those received targeted rechecks; no full post-repair audit or cold review was run.

Final checks: required files present; stage built; tool-owned Chrome and host ports closed; host.html absent. No commit, deployment, shared-file edit or polish round was performed.
