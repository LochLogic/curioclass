# Codex review: name-song-practice

## Played
Cold Grade 1 play preceded the builder report, handoff, notes and source: Make, Hear it, both takes, thumbs, one fix, comparison and Silly performance. Also exercised the projecting-teacher path and a keyboard-only solo path. The cheering plush audience is the strongest moment.

Independently checked all 96 combinations, G4/E4, rhythm totals, tempos and contrast ratios against the spec. The actual note generator agrees. Notes retain the required first three sections and practical home activities. All four standards have student actions.

## Findings fixed
- **Should fix, general, compact Practice:** four-clap Clear words lyrics collided. Kept the strip full width, moved mic/reset beside the lower controls, weighted spacing toward words and widened the last phrase. Compact/phone words grow from 11 to 16.5 px; full-screen enlargement remains 18 to 27 px.
- **Should fix, general, Perform:** changing feeling left a held syllable and its ball on the old tempo. Retimed its remaining sound and event at the next beat. The Happy-to-Sleepy test now ends at the computed 5.84947 s instead of 5.61556 s.
- **Should fix, general, song-change dialog:** confirmation narration could outlive Keep my song, Yes, change it or Escape. Hush on dialog entry/exit, preserving focus without scrolling. Final Escape check cuts the old line and restores the current hint.
- **Should fix, general, audit layout leads:** moved the compact fix badge above the last bar heading and tightened phone lyric line boxes so enlarged words cannot reach the next row headings. Removed excess span width behind two large-screen word-box warnings without moving their text. The responsive badge keeps the fix concise; the chosen comparison card stays selected.
- **Polish, general, flattest moment, Compare:** bare take buttons did not connect reflection to the chosen fix. Added First try and the actual take-2 cue, retained the chosen take on the full-size badge, and made the comparison hint ask students to listen/think about their fix. Updated the matching voice manifest.
- **Polish, general, Make art:** redrew the soccer card with clearer sewn panels, warm paper texture and a rounded silhouette. Preserved the other 16 paintings and the toy-stage payoff.

## Findings left
- **Polish, narration:** browser fallback remains. CODEX-BUILD.md prohibits recording audio; the matching 48-line big-sister manifest is ready for recordings.
- **Nit, graphics:** faint violet fringing remains on parts of the lamb cutout at the largest view. It is subtle at laptop size; left without another art pass.
- No blocker or should-fix remains from this review's findings.

## Flattest moment left
With the microphone off, comparison depends on remembering the class's live singing. The cue now focuses that reflection; optional in-page recording supplies actual playback.

## Graphics
All 17 finished images checked in the scenes and on the Scratch contact sheet. Soccer redrawn with built-in OpenAI image generation, then art.py --rekey soccer. Full prompt, house style and provenance remain in art/prompts.json; raw selection is art/raw/soccer.png. No people or missing art tokens. Cozy stage, eight plush poses and all eight favorites retained. Art: 521.2 KB. Final bundle: 978.2 KB (1,001,708 bytes). Opened both bar tools for comparison; the scene retains its richness.

## Audit
Completed once within the 40-minute cap, exit 0. Evidence: _scratch/name-song-practice/review-audit/audit.md. Opened all 81 audit PNGs directly or on labelled boards.

31 leads answered:
- 14 duplicated reports describe the compact badge and phone lyric/header overlaps in Clear words and Compare. Fixed and re-shot.
- Two large-screen warnings concerned overlapping transparent word boxes; the visible words were separated. Tightened the boxes and re-shot.
- 15 welcome warnings accepted under STANDARDS: the two incomplete mode entries send the class back to Make; Clap, Clear claps, all three shape controls and all eight favorites supply their own current line, so the welcome skips. No late welcome was added.

Opening screens were clean at all eight sizes. Resize stress completed without exceptions or stuck controls. Control/focus checks, Motion off, repeated held clicks and quick taps were clean apart from the explained welcome leads.

After the scoped fixes, eight targeted frames in _scratch/name-song-practice/final-targeted/ show no collisions, controls under 60 px, controls below the fold, or console errors. Phone clear/compare/perform, compact clear/compare, large-screen words, wide comparison and dialog Escape were inspected. The full audit was not repeated, as instructed.

Voice check at a two-second held-tap pace, allowing the final queue to settle:

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Louder! Big voices. | event | 5 | 5 |
| Tap Sing take 2, and try your fix. | how | 1 | 1 |

Read works with Sound off and releases promptly on a mode change. The 48 manifest lines match allLines(). Keyboard-only input reaches Listen with focus intact; grayscale and Motion off retain readable cues and timing. No external asset URLs or song/audio storage were introduced. Wave checks covered immediate hints, stable controls, visible short choice sets, truthful cues, incomplete states, resize, motion and voice; this creative rehearsal has no hidden-answer quiz to give away.

## Left open
No classroom acoustic calibration or live class trial is claimed. Microphone success used a synthetic MediaStream with the real MediaRecorder; denial and missing-device paths were simulated. Two takes replayed. Reset and confirmed song edits erased them; leaving Practice released the stream while retaining the takes for comparison. No song/audio is saved between visits.

The spec's microphone policy question is unchanged. No new modes/topics, commits or shared-kit changes. Repository edits stayed in tools/name-song-practice/ and _scratch/name-song-practice/. Test Chrome/server processes are closed and host.html is removed. One review pass, with the required final audit and only scoped repairs afterward.
