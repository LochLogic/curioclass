# Codex review: parade-and-bedtime-music
## Played
Cold K-2 student and projector walkthrough before reading builder notes/source: all eight full tunes, placement, wrong/right clues, composer, favorite, Somewhere else, both reset choices, and the march-to-bedtime transformation. Rich scenes and the continuous musical transformation are the strengths.

## Findings fixed
- **Blocker, general, src.html / chooseClue:** a dropped wrong-clue question restarted music after Composer's note and canceled the reveal. Every stop/new action now invalidates pending replays; dropped speech cannot replay. Held-click Composer, favorite, Read and mode/reset paths rechecked.
- **Should fix, general, compact clue tray:** inert header made Read, Sound and Motion unavailable. The actual controls now move inside the dialog and its focus loop, returning to the header on close. Checked at 680x425 and 375x812; Read keeps focus through real iframe resizes in both directions.
- **Should fix, general, tune cards:** earned icons collided with Tune labels and conveyed success by color alone. Separate identity/label/badge rows, visible check marks and accessible clue words now preserve the result. All standard sizes inspected.
- **Should fix, general, Somewhere else:** eight marks overflowed and hid the label. A four-column mark grid fits all eight and names its contents for assistive technology.
- **Polish, general, clue result:** a newly earned icon travels from the chosen clue to the card, making the listening result visible. Motion off keeps the checked chip and badge without movement.
- **Polish, general, Composer's note:** the hint stayed on the reveal after the discussion line. It now advances to the discussion prompt, guarded against newer actions.
- **Polish, general, art:** redrew the green-fringed teddy in the same watercolor style; reprocessed teddy and drum with key-tint cleanup.
- **Should fix, general, audit-confirmed card row:** the note's inherited line-height exceeded its reserved row. Explicit line-height 1 removes all 24 repeated note/label overlaps; 1280, 1366 and 1920 widths and a playing note rechecked with zero overlap.

## Findings left
- **Should fix, general, voice:** all 47 fixed lines are present and match runtime, but friendly-dad recordings are absent. Recording is forbidden in this run; browser narration remains.
- **Should fix, general, crossing speech volume:** music ducks by 6 dB, but the shared kit has no narration-volume callback. Exact kit/curio.js change remains in handoff.md; kit edits are out of bounds.
- **Should fix, general, spec conflict:** the required crossing speech can misname the current qualities. At (100,1), p=.278 is Bedtime but 100 bpm is Fast; at (90,10), p=.722 is Parade but 90 bpm is middle. Kept the mandated meter and lines; resolving the wording changes the spec.

## Flattest moment left
Closing the clue tray returns to a still scene grid. The favorite and earned clue badges preserve this class's choices, but the recap is quiet. No additional mode or reward was added.

## Graphics
Six images checked in their final scenes and both cutouts checked separately. Teddy redrawn once with built-in imagegen, magenta keyed, saved as art/teddy.webp; drum rekeyed. Full prompt saved in art/prompts.json. No people images; the spec's empty prepared scenes remain.
Final bundle: 1,297,943 bytes (1,267.5 KiB); six finished images: 589,180 bytes (575.4 KiB).

## Audit
One audit completed normally within its 2400-second limit on Chrome 9961, host 8765. Report: `_scratch/parade-and-bedtime-music/review-audit/audit.md`.
- 45 leads addressed: 24 repeated note/label overlaps fixed; seven reset-overlay flags are intentional covered background; 14 first-tap welcome suppressions match the spec. Tune taps immediately play music; scene/basket/reset taps give their own needed instruction. No late welcome was added.
- All reached states, Motion off, control walks, settled focus, repeated/quick taps and resize stress completed. No tool console/runtime errors or controls left disabled. All 57 audit PNGs viewed in 15 sheets.
- Re-shot only the affected rows and compact-control paths after the audit. Full basket also passed all 24 real held clicks, now recorded explicitly in audit-states.json. The full audit was not rerun after these targeted repairs.
Focused evidence in `_scratch/parade-and-bedtime-music/`: review-sizes, review-phone, review-regressions, review-voice, review-drag and review-audit.
- 80 clue choices agree with independently entered expectations, with the computed Tune 5 correction below.
- Eight exact tune durations, gains and meter examples recomputed. Next brass/percussion events retimed to 110 bpm; dial handler took 0.4 ms and preserved beat position. Mixed extremes both p=0.5.
- Keyboard-only Turn it, whole-pixel jittered drag, Motion off, grayscale and phone iframe checked. Shared compact controls are in view.
- Source/bundle resource scan found no network resources or network APIs. Notes' first three sections are correct. Main contrast ratios: 8.770, 8.106, 15.504, 6.360.
- Module codes match data/modules.csv: expressive clue choices teach MU:Re8, favorite plus spoken reasons teach MU:Re9, and everyday scene placement teaches MU:Cn11. These remain teacher-led K-2 activities.
- Wave checks: next-action hints/Read, stable targets and focus, short choice sets, no hidden composer giveaway, truthful badges, reset/mode persistence, and resize behavior checked. Calm mode preserves playback time.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Yes! It is slow. | event, five held taps at 2 s | 5 | 5 |
| What is the clue? Tap a clue word. | how, five placements | 1 | 1, then 4 silent |
| Sort welcome, first plain tap | welcome | 1 | 1 |
| First Read | read | hint only | hint only |
| First Sound off | control | 0 | 0 |

Read with Sound off worked; Sound on restored the skipped welcome. Rapid stale actions and the settled Composer prompt passed. Chrome was muted, so these are timing/log checks, not a headphone timbre review.

## Left open
- Spec conflict: Tune 5 is 108 bpm, Fast under the stated >=100 rule. Kept the builder's computed Fast answer, as CODEX-BUILD directs, rather than the conflicting table's middle. spec.md untouched.
- Spec conflict: Tune 8's full 16 beats last 13.714 seconds, exceeding the summary's 13-second ceiling. Full melody retained.
- Crossing-line wording and kit speech-volume limits remain as described under Findings left; their exact constraints are recorded in handoff.md.
- Headphone review and friendly-dad recordings remain open. No audio was recorded.
- Temporary host's favicon 404 is outside the offline tool. One post-audit host page also returned 404; one bounded retry served the iframe and passed focus checks. host.html and all Chrome/server processes started here were removed/stopped.
- Process deviation: the first two read commands and one short arithmetic command completed immediately with tool yield limits rather than explicit process-kill timeouts. Subsequent command/check processes had explicit limits.
- No commits or repo changes outside the two authorized folders. One review/fix pass; only targeted checks after repairs.
