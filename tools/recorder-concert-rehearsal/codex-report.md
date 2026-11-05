# Codex report: recorder-concert-rehearsal

## Built
- Rehearsal and Concert, both fixed melodies, five modeled problems, Solo, Loop bar, Score view and precise note coaching.
- Four animal performers with playing/rest poses, a clipboard checklist, randomized rehearsals and a personal note history.
- Four stage-manners moments, a gated play-along with B/A/G fingerings, live 80/96 tempo and first/final comparisons.
- Offline bundle: 1035.2 KB (1,060,090 bytes). No network resources, microphone, recording or audio storage.
- Required draft, source, notes, 37-line voice manifest, audit states, prompts and handoff supplied. No commits or polish round.
- Chrome used ports 9990 and 9991; host used 8795. All are closed. host.html is removed.

## Numbers check
- Independent calculation: `_scratch/recorder-concert-rehearsal/numbers.json`. No specification-number discrepancies.
- G5 783.9909 Hz, A5 880 Hz, B5 987.7666 Hz; 40 cents factor 1.023373892, sharp B 1010.8546 Hz.
- Clean Hot Cross Buns 10.9091 s, with count 13.6364 s; Lune 20 s, with count 22.5 s; slower Lune 24 s plus 3 s count.
- Late onset 0.15 s = 0.22 beat at 88; rush bar 2.3715 s versus 2.7273 s. Event lists match these values.
- The engine rounds middle C to 261.63. The instrument applies a tiny calibration factor so A5 is exactly 880 Hz.
- Contrast: white/brand 5.92; brand/paper 5.45; ink/paper 14.63; muted/paper 5.89; ink/clipboard 11.30; ink/white 15.90.
- Animal badges: white/Juniper 6.57, white/Otis 5.80, white/Bea 6.15; ink/Finn 8.64. All listed text pairs meet AA.

## Feel check
- Played both scripted routes with held clicks, then manners, play-along, Slower and the first/final comparison.
- Best moment: the earned concert and its personal record, showing the three actual rehearsal notes beside the changed take.
- Flat moment 1: a clean result was buried below note cards. Clean takes now remove that builder and expose Go to the concert.
- Flat moment 2: the score and staff were shrinking into tiny pictures. Score now uses real pixels; staff height is reserved.
  Phones put fingering beside the staff and Slower beside Play. Compact note-building keeps every animal's whole body visible.
- Compared with Snowy Mail Route and opened Beat Lab. `_scratch/recorder-concert-rehearsal/feel-comparison.png` puts the two tools side by side.
  The painted room and detailed cast meet the visual bar. Compact post-take figures are deliberately smaller to keep controls readable.
- Headless tests were muted as required. This is a visual, interaction and synthesis check, not a human headphone assessment.

## Done when
1. PASS: four performers, bars and Play visible at 1366x768, 680x425 and 375 wide, also with Score view. Final repair frames confirm.
2. FAIL verification: all five correct sound changes are scheduled and their score marks are implemented, but subjective audibility needs a headphone check.
3. PASS: six scripted fixes remove exactly one problem. Wrong who, bar and vague notes preserve identical event lists. See logic-results.json.
4. PASS: actual held-click journey cleaned both pieces in four takes. 2,000 random rehearsals had three distinct solvable, sound-affecting problems.
   A later regression check confirms one-note-per-take gating survives a piece switch and releases after a completed take.
5. PASS: Loop response about 1.2 ms, Stop about 0.1 ms; Solo gain routes settle within 110 ms. Score switches immediately.
   Audio trace confirms four pans, exact sounding pitches and halved vibrato. Five-take log contains no narration over music.
6. PASS: wrong manners choices cannot open the gate; all four correct moments are required. Actual play-along and live 80 tempo tested.
7. PASS: Buns first/final played back to back in the full journey. Both Lune buttons select exactly their stored first/last event settings.
8. PASS: five real takes at a held-click, two-second pace gave markHow 1, noteHow 1, toolsHow 1, noChange 4, with no speech/music overlap.
   Fixed events spoke in the full journey. Final fixes also queue their specific fixed line before ready. Quick-tap repairs preserve welcomes.
9. PASS: stored data contains only notes and first/last problem lists. No microphone calls, media recording or stored audio.

## Wave lessons
- Hint and voice: PASS. Immediate tool-owned hints, Read stops music, V.heard guards how lines, stale checks and first-checklist welcome tested.
- Focus and layout: PASS after repairs. Controls remain stable, no focus on load, curtain transition focuses Play, resize preserves guide controls.
- Sizes: FAIL strict no-scroll interpretation. Core scene and transport fit all required sizes; phone note building/history still require page scrolling.
- No giveaways: FAIL for prescribed manners wording. Rehearsal hides problems until Score and rotates cards; manners right choices are often longest.
- Honest numbers: PASS. Tempi, durations, late offset, cents and modeled changes match independent calculations; no performance grade is claimed.
- Standards: PASS. Solo students evaluate takes, give actionable feedback, practice manners, then play, sing or clap their own concert part.
- Motion off: PASS. Audit found no endless animation. Timing remains musical; pose swaps and beat-stepped heads remain.
- Short choices visible: FAIL on phones and the optional unfiltered six-card set at 680. Criterion-filtered compact cards fit and receive real clicks.
- Resize mid-animation: PASS. Audit clean; final phone-to-desktop-to-phone resize retained running playback and restored guide controls.
- Welcome not late: PASS after targeted repairs. Music-start taps skip a stale welcome. Same-mode/reset quick pairs preserve an active generic welcome.
- Unknown shown as unknown: PASS for applicable scope. No culprit highlight or correctness diagnosis appears before listening; checklist marks are the student's.
- One look, one meaning: PASS. Badge shapes/numbers identify players; Solo, loop selection, sounding pose and score marks each have separate meanings.
- Badge says what is true: PASS. Take counts, mode, solo and loop reflect state. Wrong group-target notes avoid claiming an individual already plays correctly.
- Hint changes back: PASS. Mode, piece, concert part, Stop and Read immediately set relevant controls and instructions.
- No answer by copying: PASS for rehearsal. Diagnosis is by sound/score; no descriptive clue repeats the fixing card. Manners wording caveat above remains.

## Audit leads
- Full audit completed once: 55 leads, `_scratch/recorder-concert-rehearsal/audit/audit.md`.
- Every row is dispositioned in `_scratch/recorder-concert-rehearsal/audit-responses.md`.
- Fixed: compact Read width, room-prompt overlaps, curtain focus, tiny fingering label, eight-bar widths, concert label collisions,
  phone guide scrolling, first-checklist welcome and four quick-welcome interruptions. Final held-click checks passed without console errors.
- False leads: the workspace-positioned tray is visibly clickable outside the panel, proven with elementFromPoint and a held click.
  Staff letters outside its viewport are intentional scrolling content. Music-start welcome omissions prevent narration over a take.
- Left open: phone note/history scrolling. Sound-off hush is expected. The full audit was not repeated after repairs, per the once-only rule.
- Mechanical audit reported clean Motion off, action resizing, per-control errors/Enter paths and five-click how-line counts.

## Frames looked at
- Two bar-tool frames, every final WebP at output size, art contact sheet and the side-by-side Feel comparison.
- Early 4, checks 4, logic 1, journey 7, final-size suite 12, target fixes 6, last frames 3, repair frames 8 and lead frames 8.
- Closing live-resize frame, Space keyboard frame and both final count-in frames.
- All 33 audit frames reviewed on nine contact sheets, with close-ups of compact notes, phone manners and concert guides.
- Size suite: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 through the iframe host.
- Grayscale, Motion off, keyboard-only activation, live Score, all concert parts, clean takes and nonempty histories were inspected.
- The only early browser-host resource error was a missing parent favicon. Targeted host runs use an inline icon and report zero errors.
- An early logic-test assertion counted Lune notes incorrectly; the corrected 88-event clean list test passes. This was a test error.

## Art made
- 10 separate built-in imagegen images: music room, school stage, and two poses each for rabbit, owl, badger and fox.
- Final art 694.4 KB. Bundle 1035.2 KB. Prompts and house style are in art/prompts.json, with drawn_by codex.
- Used only art.py --rekey for finishing. Re-keyed with despill and holes to remove edge tint; no images needed a redraw.
- Original full prompts, raw images and generated-image provenance are preserved. No generated people; audience is code silhouettes.

## Art still to paint
None. All ten requested assets are present and placed.

## Engine changes wanted
- kit/music-studio.js, play: stable per-event pan support. Tool-local registered instruments supply stereo panning for now.
- kit/music-studio.js, blow: optional vibrato depth multiplier. Tool-local scoped createGain adapter halves the existing vibrato assignment.
- Fractional semi already works in MS.freq. No shared file was changed. Adapter implementation and risks are documented in handoff.md.

## Left open
- Human headphone review of tone quality and how clearly each fault stands out in the four-player mix.
- Recorded Leda narration is absent because recording was prohibited. Browser speech works; 37 requested how/event strings are prepared.
- Phone note-building/history and optional unfiltered cards at 680 use page scrolling. Core players, bars and Play remain in view.
- Specified manners-choice lengths can cue a guess. The content was kept as supplied rather than inventing replacement choices.
- The vibrato adapter depends on the current MS.blow implementation. A stable engine option is preferable in a later authorized shared-engine change.
- Final repairs received focused checks rather than a second full audit. Cold review is still the next stage; no polish round was started.
