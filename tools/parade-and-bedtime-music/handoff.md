# Parade and Bedtime Music handoff

Built November 1, 2026 in S:/CurioClass-codex. Build only, no commit, no polish round.
The report is written last because the user's instruction says to stop when it is written.

## Structure
src.html starts from the kit starter and uses kit:curio for the shared frame, controls, voice queue and audio context.
CSS lays out at real viewport sizes. The Sort stage has a tune row, four large scenes and a clue tray.
At compact sizes the tray becomes a modal over the scenes, with a focus loop, inert background and a Scenes close control.
At full laptop height the tray is under the grid. Neither form hides any of the ten clue choices in a scroll list.
Native outer buttons stay in place while their badges and labels change. Intentional focus uses preventScroll.

The script holds the eight melodies, the narrative line table, transport and synth, scene rendering, clue actions,
pointer dragging, mode lifecycle, reset and shared control callbacks. __tool exposes state and evidence hooks.
The single offline bundle is parade-and-bedtime-music.html; metadata stays in tool.draft.json with stage built.

## Audio and narration
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

## Art
Six images made with the built-in image tool, one per prompt, in the same watercolor picture-book style.
Prompts and house style are in art/prompts.json; originals are in art/raw. Each was processed with art.py --rekey.
Drum and teddy were rekeyed with despill after viewing their initial green fringes. All six finished images were viewed.
No people, faces of people or body parts were generated. The teddy is a stuffed toy.
Scenes are large images. Turn it uses a spatial mask so the street remains left and bedroom enters from the right.
Motion off switches directly among street, dusk blend and bedroom, with no animated cross-fade, bounce or rock.

## Specification choices and open questions
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

## Verification pointers
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

## Engine changes wanted
- kit/curio.js, voice / speakOne and init: accept an optional speech-volume callback, sampled when a line starts,
  and apply it to both recorded Audio.volume and SpeechSynthesisUtterance.volume. This tool needs crossing speech
  at the selected music level, with the music itself ducked by 6 dB. Tool code already performs the music ducking.
  Do not change the kit in this build. The browser voice currently uses its normal speech volume.

## Next review
Cold review should listen to all eight timbres and the soft-to-loud progression, confirm the original melodies,
and review the two compact presentation choices above. Friendly-dad recordings need the owner's later voice pipeline.

## Cold review repairs, November 4, 2026
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
