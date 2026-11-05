# Codex review: cartoon-soundtrack-mixer

## Played
Cold Grade 4 solo run before reading builder notes: full silent film, three-way demo, four shaped cues, effects, complete score, live swaps, Class guess/Show and writing; also checked the projected-class flow. The theater and expressive cat are strong. Stopped music edits were the flattest action.
Checked all five catalog standards against composing, personal mood, comparison, written reasons and the silent-film accompaniment activity. Notes retain the required three opening sections and practical home activities.

## Findings fixed
- **Should fix, general, Score it/effects:** dense chips covered one another. Two-lane labels now stay separate with 44 px grab areas; exact onset pins and duration strokes retain the time scale. Labels show start and length. Checked every required size and 16 real drags at 680, 1366 and 375.
- **Should fix, general, effect boundaries:** moving near 24 s permanently shortened sounds, and last-slot collisions could share an onset. Preserve intended length, clip only playback/display, and search for a free quarter-second slot. Rain restores its three-second length after moving back; all 16 boundary onsets are distinct.
- **Should fix, general, effect editing:** drag-release hints retained the old time and Remove could be hidden. Placement, movement and chip dragging open Effects; release names the current time; canceled drags restore the start. Stopped phone selections scroll into view. Final real drag and phone frames confirm this.
- **Should fix, general, Box scene:** the painted background box competed with a different animated box. Repainted the porch without its baked-in box and redrew kitten-peek against the empty box reference. One box now persists through the reveal and pickup.
- **Should fix, general, Home scene:** a flat rectangle covered a cat walking below the cat door. The approach now changes perspective toward the painted opening and clips at its jamb.
- **Should fix, general, voice and hints:** Read during playback named Stop after stopping; later swaps could leave old score-name speech queued or speaking. Read now names a stopped action, new swaps drop stale results, and queued results validate the announced score. Read remains protected. Stop hints name controls in the current mode.
- **Should fix, general, phone privacy:** the saving notice was hidden. It now has a visible footer line; final 375 px checks show it inside the viewport with zero page scrolling.
- **Should fix, general, writing:** the focus ring touched the prompt at 680x425. Textarea focus is now inset; the repaired frame is clear.
- **Polish, general, cue shaping:** replaced the identical beep with a two-note audition using the selected melody, tempo, loudness, instrument and style. Play, Read, mode changes and Sound changes stop the audition.
- **Polish, general, payoff:** completed scores name the student's mood, shaped scenes and effects, with correct singular/plural words. The three-way demo ends on the storm rather than the next scene.

## Findings left
- **Polish, general, dense compact preview:** two 44 px effect lanes leave limited film height at 680x425 and on a phone. Transport and editing remain reachable without page scrolling. Larger classroom views present the cartoon much better.
- No other confirmed blocker or should-fix remains. Perceptual audio review and the spec conflicts below remain unverified or unresolved, rather than being called passes.

## Flattest moment left
The short preview with both effect lanes occupied. Live mood changes and the kitten ending remain the strongest moments; the painted theater, full art set and musical choices were preserved.

## Graphics
Inspected all 16 assets and rendered scenes, plus Beat Lab and Snowy Mail Route frames. Repainted `art/bg-porch.webp` and `art/kitten-peek.webp` using built-in image generation, retained selected originals in `art/raw/`, and processed with `art.py --rekey`. Prompts and provenance are in `art/prompts.json`. No people are present; the spec explicitly calls for an empty piano bench and an animal story. Art: 693.0 KiB. Final offline bundle: 1032.8 KiB.

## Audit
Ran `audit_tool.py` once, last, with a 2400-second limit, Chrome 9931 and host 8735. It finished with 10 leads. Read `_scratch/cartoon-soundtrack-mixer/review-audit/audit.md`; all 61 audit PNGs were inspected, with relevant writing and secret-guess frames also opened at full size.
- Four phone timeline leads are the spec's required 720 px scrolling timeline, rather than sideways page overflow. Final selected-effect checks also keep the selected chip visible.
- Three writing keep-region leads are deliberate modal coverage. Keep regions are now scoped to each state's visible work rather than requiring the stage behind the dialog.
- Two skipped welcomes are Play silent and Hear it three ways, as required by the no-narration-over-cartoon rule.
- The quick Start scoring tap cuts its welcome because the second tap hits Chase and shapes the first cue. A targeted real double tap confirmed that state change, which makes the introductory guidance stale.
- Held controls, repeat clicks, Motion off and resize checks reported no errors, lost focus, repeated how-to lines or controls left disabled.
- The initial dense-effects fixture failed to return its drag points, so its audit pictures were empty. Corrected the manifest and verified the density case separately with 16 real drags at each of 680, 1366 and 375. Do not count that initial audit state as dense coverage.
- Final hint, focus, privacy, duration-label and count repairs were checked only in affected frames after the audit; the full audit was not rerun. Final targeted runs report zero tool errors. Earlier helper-host favicon 404s were outside the bundled tool.

| Voice check | Kind | Expected | Spoken |
|---|---|---:|---:|
| Effects guidance, five requests | how | 1 | 1 |
| Show result, five random rounds | event | 5 | 5 |

Three complete 24-second clock runs at 66, 104 and 152 beats/minute finished at 24. Incoming live-edit/swap notes were scheduled immediately, and the picture clock did not restart. A real effect drag landed at 8.25 s. Sound off/on preserved monotonic time. Writing and clearing survived fresh loads; keyboard, grayscale, reduced motion, blank scores, full effect capacity and all required sizes were checked. Fixed narration matches all ten manifest lines; resource inspection found no external tool requests.

## Left open
- Every Chrome was muted. Synthesized timbre quality, perceptual transitions and physical speaker/display latency were not listened to or measured. No audio was recorded, as required; browser narration remains the fallback for the prepared upbeat-guide/Zephyr manifest.
- Spec conflict: Funny explicitly uses Boing at 7.2 s while Done when 4 generalizes about 7.0 s. Preserved Content: Scary/Sad Thunder is at 7.0 s and all Tiny mews are at 16.0 s.
- Recomputed 24 s, 96 quarter-second slots, 30 px/s phone scale, loop lengths and all nine AA contrast pairs. The spec's 680 px estimate of 27 px/s disagrees with its 62 percent formula, which gives 17.57; the named art list totals 16 rather than 15. Spec was not edited.
- Shared-engine additions remain requested in handoff.md. Tuba, strings and timing workarounds stay tool-local; no kit file changed.
- No git commits. All review writes stayed in the tool and its scratch folder; temporary host.html is absent and no assigned test port remains listening.
