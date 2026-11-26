# Parade and Bedtime Music: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: parade-and-bedtime-music

#### Built
- Sort: eight original synthesized tunes, four painted moments, Somewhere else, tap and real drag placement,
  ten clue chips, earned badges, a gentle composer reveal, one class favorite, and confirmed reset.
- Turn it: looping Big Drum March, live Speed and Loudness dials, a spatial street-to-bedroom reveal,
  beat-driven drum and teddy, mood meter, March again, keyboard controls and shared Read / Sound / Motion.
- All requested build files are present. No git commit, branch change or polish round.
- The report was written last to honor the user's explicit stop-on-report instruction.

#### Numbers check
- Independently recomputed in `_scratch/parade-and-bedtime-music/number-check.py`; results in `numbers.json`.
- Tune lengths: 10.909, 12.414, 8.000, 8.571, 6.667, 7.500, 11.429 and 13.714 seconds.
- March at 50 bpm: 19.2 seconds. Gains at levels 1, 5, 9, 10: .080, .195312, .476837, .596046.
  Dynamic span: 17.4438 dB. Start meter .833333; both mixed extremes .5; endpoints 0 and 1.
- All supplied high/low note-attack fractions check out. All supplied contrast ratios check out:
  white/brand 8.770, brand/paper 8.106, ink/paper 15.504, muted/paper 6.360.
- Difference: Tune 5 at 108 bpm is Fast under the stated >=100 rule, despite middle in the supplied table.
  The computation wins, as CODEX-BUILD directs. spec.md is untouched; notes and handoff explain it.
- Difference: Tune 8 exceeds the summary's 13-second ceiling. Its full written 16 beats are retained.

#### Feel check
- Walked the full listening flow: all eight tunes finished, placements were made, clues and a favorite chosen,
  modes switched, the scene changed through both boundaries twice, and Keep it / Start over were exercised.
- Best moment: the same march notes continue while the bedroom enters from the right and the teddy takes over the movement.
- Flattest moment 1: the first mixed scene looked like two ghosted pictures. Replaced full-frame opacity with a spatial reveal.
- Flattest moment 2: a compact clue tray squeezed the painted scenes. It now opens over them with all ten choices together,
  then Scenes returns to the full painted grid. The phone uses the same clear, large-target tray.
- Compared against both bundled reference tools. The side-by-side frame is
  `_scratch/parade-and-bedtime-music/bar-comparison.jpg`; the tool does not look plainer than Snowy Mail Route.
- All Chrome checks were muted as required. Headphone review of the instrument balance is still open.

#### Done when
1. PASS: 1366x768 and 680x425 scene grids and Turn it controls viewed. All visible controls measured at least 60 px.
2. PASS for implementation and timing: all exact melody events, tempos and gains checked; all eight full runs finished.
   Replacement tunes stop the preceding transport. Audible timbre quality remains for headphone review.
3. PASS with the documented Tune 5 correction: all 80 chip choices across the 40 pairs match independent expected results.
4. PASS: real jittered drag and held taps; tempo state updated in .5 ms in the recorded check, preserving beat position.
   The next brass and snare events were scheduled at 110 bpm. Only 100 ms is scheduled ahead; unstarted nodes are canceled.
5. PASS: two stopped-at-boundary trips each into Bedtime and Parade logged four spoken event lines.
   Rapid continued turning correctly expires queued lines after a further dial change.
6. PASS: (140,1) and (50,10) both returned .5 and displayed In between.
7. PASS for queue behavior: Sort starts no narrator line during music; wrong clues speak before replay.
   How lines were spoken once in the multi-action run. FAIL for the exact requested voice: recordings are pending.
8. PASS: any scene and Somewhere else accept every tune. Composer reveal names the intended moment without wrong feedback.
9. PASS: Sound off mutes the music bus and displays its hint while timing continues. Motion off has no prop movement
   or infinite animation, and switches among three scene states. Read follows the kit's explicit speech override.
10. PASS: no external resources or network API calls in the source or bundle. No class work is stored.
    Shared kit Motion preference storage remains, as required by STANDARDS.

#### Wave lessons
- Hint and voice: PASS. Immediate hints name controls, Read uses the current hint, queue validity follows the mode and step.
- Focus and layout: PASS. Outer buttons persist, deliberate focus prevents scrolling, and compact tray focus is contained.
- Sizes: PASS on the full set: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe.
- No giveaways: PASS. Intended moments are hidden until Composer's note. Shape marks convey identity, never an answer.
- Honest numbers: PASS. Original notes and computed values are retained; equal meter weighting is named in its tooltip and notes.
- Standards: PASS for teacher-led scope. Expressive clues, personal preference with a reason, and everyday connections are practiced.
- Motion off: PASS. No infinite CSS animation or JavaScript prop movement; music duration stays unchanged.
- Short choice sets: PASS. All ten clues stay visible together; no short choices hide in a scroll panel.
- Resize mid-animation: PASS. Full audit found no exceptions or controls left disabled after resizing every reached state and walk control.
- Welcome after first action: PASS. Two-mode welcome validity and first-tap suppression use Curio.voice; no welcomeAfter.
- Unknown as unknown: PASS. No intended-moment label appears before reveal; badges appear only after earned clues.
- One look, one meaning: PASS. Consistent tune shape marks, paired clue icons and a single favorite heart.
- Badge says what is true: PASS. Badges are earned from the verified table, including the computed Tune 5 Fast correction.
- Hint changes back: PASS. Mode, stop, reset, close-tray and Read-pause paths update the current action.
- No answer by copied words: PASS. Students hear original music before naming a clue; scene placements have no right/wrong score.

#### Audit leads
- Full audit completed normally, once, using Chrome 9981 and host 8785. Report: `_scratch/parade-and-bedtime-music/audit/audit.md`.
- Sizes, reached states, Motion off, resize stress, console checks, settled focus and five held clicks at a 2 s pace were clean.
- Leads 1 to 8, Tune 1 through Tune 8 welcome not heard: intentional. A first tap plays its tune immediately;
  the specified Sort welcome becomes stale once a card is tapped, and narration must not compete with music.
- Lead 9, Somewhere else welcome not heard: intentional. Its first-tap instruction names the needed tune card and scene,
  so Curio.voice correctly skips the welcome without marking it heard.
- Leads 10 to 13, Bedtime, Parade, Birthday and Rainy day welcome not heard: same required first-tap own-line behavior.
- Lead 14, Start over welcome not heard: the reset question takes precedence on that first action, as specified.
- Leads 15 and 16, quick Sort and Turn it taps cut the welcome: fixed. Re-selecting the current mode now leaves its speech
  and work alone. Targeted held double taps at .7 s confirmed one whole welcome per mode, with no cut entry.
- Two additional build fixes received targeted checks: a placed tune's end reopens its clue tray and names the next action;
  numeric shortcuts retain focus on the replay card, then on a clue when stopped. Read's paused hint follows placement state.
- The full audit was not rerun after these focused fixes. Wide and compact end states and shortcut focus were rechecked.

#### Frames looked at
- Both reference frames, all four quick frames, all 23 full-run frames, three phone frames, the deep-check frame,
  four session frames, all six finished artworks and the bar comparison.
- Full-run frames were viewed in seven labeled contact sheets; phone views, key interactions and session frames
  were also opened at full size. Every claimed generated PNG was viewed.
- Viewed all 41 audit PNGs in 11 labeled contact sheets and the six final targeted frames.

#### Art made
- Six built-in image-tool illustrations, 574.35 KiB total finished art. Bundle: 1,293,095 bytes, about 1,262.79 KiB.
- Four watercolor scenes, one toy drum and one teddy; no generated people. No image needed a redraw.
- Drum and teddy received a second keying pass with despill. The parade background is about 197 KiB,
  above the suggested per-background target, while the total bundle remains well below 2 MB.
- Prompts are in art/prompts.json; original PNGs in art/raw; all generated assets are credited in draft metadata.

#### Art still to paint
- None.

#### Engine changes wanted
- kit/curio.js, voice / speakOne and init: optional speech-volume callback applied to clip volume and utterance volume.
  Crossing narration should track selected music loudness. Current tool ducks the music by 6 dB, but browser speech
  remains at normal speech volume because the public kit API has no volume hook. Full detail is in handoff.md.

#### Left open
- Friendly-dad / Achird recordings: 47 fixed lines are manifested and match runtime allLines, but no audio was recorded,
  as the build instructions require. Browser narration is the current fallback.
- Speech-to-music volume matching needs the kit extension above. Full headphone review remains for cold review.
- Compact tray presentation and the persistent replay row are explicit layout adaptations documented in handoff.md.
- drive.py's iframe host requests favicon.ico and logs a 404 outside the tool. Its top-level host is temporary;
  the bundled tool has a data favicon and no external requests. The audit intentionally filters this known host artifact.
- No audit-confirmed layout or runtime repair remains. The final focused fixes have targeted evidence; a fresh full audit
  and the already planned cold review can independently check the final bundle.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: parade-and-bedtime-music
#### Played
Cold K-2 student and projector walkthrough before reading builder notes/source: all eight full tunes, placement, wrong/right clues, composer, favorite, Somewhere else, both reset choices, and the march-to-bedtime transformation. Rich scenes and the continuous musical transformation are the strengths.

#### Findings fixed
- **Blocker, general, src.html / chooseClue:** a dropped wrong-clue question restarted music after Composer's note and canceled the reveal. Every stop/new action now invalidates pending replays; dropped speech cannot replay. Held-click Composer, favorite, Read and mode/reset paths rechecked.
- **Should fix, general, compact clue tray:** inert header made Read, Sound and Motion unavailable. The actual controls now move inside the dialog and its focus loop, returning to the header on close. Checked at 680x425 and 375x812; Read keeps focus through real iframe resizes in both directions.
- **Should fix, general, tune cards:** earned icons collided with Tune labels and conveyed success by color alone. Separate identity/label/badge rows, visible check marks and accessible clue words now preserve the result. All standard sizes inspected.
- **Should fix, general, Somewhere else:** eight marks overflowed and hid the label. A four-column mark grid fits all eight and names its contents for assistive technology.
- **Polish, general, clue result:** a newly earned icon travels from the chosen clue to the card, making the listening result visible. Motion off keeps the checked chip and badge without movement.
- **Polish, general, Composer's note:** the hint stayed on the reveal after the discussion line. It now advances to the discussion prompt, guarded against newer actions.
- **Polish, general, art:** redrew the green-fringed teddy in the same watercolor style; reprocessed teddy and drum with key-tint cleanup.
- **Should fix, general, audit-confirmed card row:** the note's inherited line-height exceeded its reserved row. Explicit line-height 1 removes all 24 repeated note/label overlaps; 1280, 1366 and 1920 widths and a playing note rechecked with zero overlap.

#### Findings left
- **Should fix, general, voice:** all 47 fixed lines are present and match runtime, but friendly-dad recordings are absent. Recording is forbidden in this run; browser narration remains.
- **Should fix, general, crossing speech volume:** music ducks by 6 dB, but the shared kit has no narration-volume callback. Exact kit/curio.js change remains in handoff.md; kit edits are out of bounds.
- **Should fix, general, spec conflict:** the required crossing speech can misname the current qualities. At (100,1), p=.278 is Bedtime but 100 bpm is Fast; at (90,10), p=.722 is Parade but 90 bpm is middle. Kept the mandated meter and lines; resolving the wording changes the spec.

#### Flattest moment left
Closing the clue tray returns to a still scene grid. The favorite and earned clue badges preserve this class's choices, but the recap is quiet. No additional mode or reward was added.

#### Graphics
Six images checked in their final scenes and both cutouts checked separately. Teddy redrawn once with built-in imagegen, magenta keyed, saved as art/teddy.webp; drum rekeyed. Full prompt saved in art/prompts.json. No people images; the spec's empty prepared scenes remain.
Final bundle: 1,297,943 bytes (1,267.5 KiB); six finished images: 589,180 bytes (575.4 KiB).

#### Audit
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

#### Left open
- Spec conflict: Tune 5 is 108 bpm, Fast under the stated >=100 rule. Kept the builder's computed Fast answer, as CODEX-BUILD directs, rather than the conflicting table's middle. spec.md untouched.
- Spec conflict: Tune 8's full 16 beats last 13.714 seconds, exceeding the summary's 13-second ceiling. Full melody retained.
- Crossing-line wording and kit speech-volume limits remain as described under Findings left; their exact constraints are recorded in handoff.md.
- Headphone review and friendly-dad recordings remain open. No audio was recorded.
- Temporary host's favicon 404 is outside the offline tool. One post-audit host page also returned 404; one bounded retry served the iframe and passed focus checks. host.html and all Chrome/server processes started here were removed/stopped.
- Process deviation: the first two read commands and one short arithmetic command completed immediately with tool yield limits rather than explicit process-kill timeouts. Subsequent command/check processes had explicit limits.
- No commits or repo changes outside the two authorized folders. One review/fix pass; only targeted checks after repairs.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Parade and Bedtime Music handoff

Built November 1, 2026 in S:/CurioClass-codex. Build only, no commit, no polish round.
The report is written last because the user's instruction says to stop when it is written.

#### Structure
src.html starts from the kit starter and uses kit:curio for the shared frame, controls, voice queue and audio context.
CSS lays out at real viewport sizes. The Sort stage has a tune row, four large scenes and a clue tray.
At compact sizes the tray becomes a modal over the scenes, with a focus loop, inert background and a Scenes close control.
At full laptop height the tray is under the grid. Neither form hides any of the ten clue choices in a scroll list.
Native outer buttons stay in place while their badges and labels change. Intentional focus uses preventScroll.

The script holds the eight melodies, the narrative line table, transport and synth, scene rendering, clue actions,
pointer dragging, mode lifecycle, reset and shared control callbacks. __tool exposes state and evidence hooks.
The single offline bundle is parade-and-bedtime-music.html; metadata stays in tool.draft.json with stage built.

#### Audio and narration
All tunes use their exact written notes, tempo, meter and specified gain. Accompaniments are synthesized in code.
The continuous beat clock uses performance time, independent of visual animation and Sound. A 25 ms scheduler
looks ahead 100 ms. Speed changes preserve the current beat, stop all unstarted voices, and reseek the events.
Started notes keep their existing decay; every unplayed note is retimed. Loudness ramps over 50 ms.
Sound off mutes the bus immediately; musical timing and visual beats continue.
Stop, replacement tunes, drag, placement and mode switches cancel the previous transport immediately.

Curio.voice owns narration, once-only how lines, repeatable events, welcome validity and Read.
Sort narration never competes with music: actions stop the tune before their spoken answer, and a wrong clue
waits for its spoken question before replay. Read pauses music before speaking the current instruction or answer.
Turn it crossings may speak while music plays. The music is ducked by 6 dB during queue speech.
A further dial change makes queued crossing lines stale, as specified. Stop at the crossing to hear the whole line.
friendly-dad / Achird is listed in voice/lines.json. No audio was recorded, as required in this Build run.
All fixed lines currently fall back to browser narration; the precise requested friendly-dad timbre is still pending.
Browser speech volume cannot be tied to music gain through the current public kit API; see Engine changes wanted.

#### Art
Six images made with the built-in image tool, one per prompt, in the same watercolor picture-book style.
Prompts and house style are in art/prompts.json; originals are in art/raw. Each was processed with art.py --rekey.
Drum and teddy were rekeyed with despill after viewing their initial green fringes. All six finished images were viewed.
No people, faces of people or body parts were generated. The teddy is a stuffed toy.
Scenes are large images. Turn it uses a spatial mask so the street remains left and bedroom enters from the right.
Motion off switches directly among street, dusk blend and bedroom, with no animated cross-fade, bounce or rock.

#### Specification choices and open questions
The spec has no explicit open-question list. The following conflicting or underspecified details were resolved:
- Tune 5 is Fast at 108 bpm. The table says middle, but the explicit >=100 rule and independent computation say Fast.
  CODEX-BUILD says to trust the computation. notes.md and the report identify the difference; spec.md is untouched.
- Tune 8 plays the full written 16 beats, about 13.714 seconds, beyond the summary's 6 to 13 second range.
- Cold review noted another spec conflict: the equal-weight meter calls (100 bpm, loudness 1) Bedtime (p=.278),
  yet 100 bpm is Fast under the clue rule; its required crossing line says Slow and soft. At (90,10), p=.722 is Parade
  although 90 bpm is middle. The prescribed meter and exact crossing lines were kept; resolving their wording requires a spec decision.
- Piccolo pitches are played exactly as written, G5 through C6; the phrase an octave up describes that written register.
- A tune's listening button stays in the top row while its shape and number sit in the chosen scene's corner.
  This keeps all eight 60-pixel replay targets accessible even when all eight are put in one scene.
- Each selected, placed card exposes its 60-pixel favorite and Composer's note buttons in the tray, rather than
  squeezing eight extra heart buttons into the row. Favorite remains unique and visible on its row card and scene token.
- Compact clue trays overlay the grid instead of sitting below it. This preserves ten 60-pixel choices at 680x425 and 375 wide.
- Somewhere else keeps a tune's shape in its basket. Any moment choice is accepted, with no score or wrong-scene feedback.
- No class work is stored. The shared kit remembers only the Motion preference, which its standing rules require.
- Chrome remains muted during all automated runs. Headphone review of the synthesized instrument balance remains open.

#### Verification pointers
Scratch contains number-check.py and numbers.json, shots in batches of 12, frames, contact sheets, raw logs,
deep-evidence.json for all 80 clue answers and immediate retiming, and session evidence for all eight complete tunes.
Real held taps, a whole-pixel jittered drag, keyboard input, grayscale, Sound off and Motion off were exercised.
The full size run was performed once; later runs target changes and deeper interactions.
The supplied drive.py host requests favicon.ico outside the tool iframe and reports a 404. The offline tool itself
has a data favicon and no network resources. The audit explicitly excludes this host favicon false positive.

The single full audit completed with 16 leads: 14 intentional first-tap welcome suppressions and two cut welcomes
from quick repeats on the current mode. The latter were fixed by leaving an already selected mode alone.
Post-audit fixes also return a finished placed tune to its clue tray, update Read's paused hint, and retain keyboard
focus when a number shortcut closes or reopens the compact tray. These paths received targeted checks, not another full audit.

#### Engine changes wanted
- kit/curio.js, voice / speakOne and init: accept an optional speech-volume callback, sampled when a line starts,
  and apply it to both recorded Audio.volume and SpeechSynthesisUtterance.volume. This tool needs crossing speech
  at the selected music level, with the music itself ducked by 6 dB. Tool code already performs the music ducking.
  Do not change the kit in this build. The browser voice currently uses its normal speech volume.

#### Next review
Cold review should listen to all eight timbres and the soft-to-loud progression, confirm the original melodies,
and review the two compact presentation choices above. Friendly-dad recordings need the owner's later voice pipeline.

#### Cold review repairs, November 4, 2026
- stopMusic increments the action revision. Canceled or stale wrong-clue speech cannot restart music after Composer's note,
  Our favorite, Read, Scenes or Start over. Replays also require a non-dropped voice result.
- Composer's note updates the hint to the discussion prompt after its reveal, guarded by the same action revision.
- Tune cards now reserve separate rows for identity, label and earned clues. Badges no longer collide with Tune labels.
  Earned clue words are included in the accessible name, check marks supplement color, and new badges travel to their card.
- Somewhere else wraps its eight marks in a four-column grid and names its contents for assistive technology.
- The teddy was redrawn with the built-in image tool on magenta to remove its green fringe, then processed with art.py --rekey.
- Reset synchronizes the compact tray's inert state immediately as well as through the existing MutationObserver.
- Compact trays move the actual shared Read, Sound and Motion buttons into the dialog, returning them to the header on close.
  They remain inside the focus loop and reachable while the scene and tune controls are inert.

Audit follow-up: note line-height is explicitly 1 so its box fits the reserved identity row.
The full-basket audit state now lists every real tune, basket and Scenes click rather than direct function calls.
Compact listening controls preserve focus after moving between the dialog and header on resize.

The November 4 cold audit completed once: `_scratch/parade-and-bedtime-music/review-audit/audit.md`, Chrome 9961, host 8765.
Its 45 leads are addressed in codex-review.md: 24 note line-box overlaps repaired, seven expected reset-overlay flags,
and 14 specified first-tap welcome suppressions. All 57 audit frames were viewed. Wide row, playing-note, full-basket
and compact shared-control focus checks passed after the targeted repairs. The full audit was not rerun afterward.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
