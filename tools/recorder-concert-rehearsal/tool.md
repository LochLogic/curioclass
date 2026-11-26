# Recorder Concert Rehearsal: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: recorder-concert-rehearsal

#### Built
- Rehearsal and Concert, both fixed melodies, five modeled problems, Solo, Loop bar, Score view and precise note coaching.
- Four animal performers with playing/rest poses, a clipboard checklist, randomized rehearsals and a personal note history.
- Four stage-manners moments, a gated play-along with B/A/G fingerings, live 80/96 tempo and first/final comparisons.
- Offline bundle: 1035.2 KB (1,060,090 bytes). No network resources, microphone, recording or audio storage.
- Required draft, source, notes, 37-line voice manifest, audit states, prompts and handoff supplied. No commits or polish round.
- Chrome used ports 9990 and 9991; host used 8795. All are closed. host.html is removed.

#### Numbers check
- Independent calculation: `_scratch/recorder-concert-rehearsal/numbers.json`. No specification-number discrepancies.
- G5 783.9909 Hz, A5 880 Hz, B5 987.7666 Hz; 40 cents factor 1.023373892, sharp B 1010.8546 Hz.
- Clean Hot Cross Buns 10.9091 s, with count 13.6364 s; Lune 20 s, with count 22.5 s; slower Lune 24 s plus 3 s count.
- Late onset 0.15 s = 0.22 beat at 88; rush bar 2.3715 s versus 2.7273 s. Event lists match these values.
- The engine rounds middle C to 261.63. The instrument applies a tiny calibration factor so A5 is exactly 880 Hz.
- Contrast: white/brand 5.92; brand/paper 5.45; ink/paper 14.63; muted/paper 5.89; ink/clipboard 11.30; ink/white 15.90.
- Animal badges: white/Juniper 6.57, white/Otis 5.80, white/Bea 6.15; ink/Finn 8.64. All listed text pairs meet AA.

#### Feel check
- Played both scripted routes with held clicks, then manners, play-along, Slower and the first/final comparison.
- Best moment: the earned concert and its personal record, showing the three actual rehearsal notes beside the changed take.
- Flat moment 1: a clean result was buried below note cards. Clean takes now remove that builder and expose Go to the concert.
- Flat moment 2: the score and staff were shrinking into tiny pictures. Score now uses real pixels; staff height is reserved.
  Phones put fingering beside the staff and Slower beside Play. Compact note-building keeps every animal's whole body visible.
- Compared with Snowy Mail Route and opened Beat Lab. `_scratch/recorder-concert-rehearsal/feel-comparison.png` puts the two tools side by side.
  The painted room and detailed cast meet the visual bar. Compact post-take figures are deliberately smaller to keep controls readable.
- Headless tests were muted as required. This is a visual, interaction and synthesis check, not a human headphone assessment.

#### Done when
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

#### Wave lessons
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

#### Audit leads
- Full audit completed once: 55 leads, `_scratch/recorder-concert-rehearsal/audit/audit.md`.
- Every row is dispositioned in `_scratch/recorder-concert-rehearsal/audit-responses.md`.
- Fixed: compact Read width, room-prompt overlaps, curtain focus, tiny fingering label, eight-bar widths, concert label collisions,
  phone guide scrolling, first-checklist welcome and four quick-welcome interruptions. Final held-click checks passed without console errors.
- False leads: the workspace-positioned tray is visibly clickable outside the panel, proven with elementFromPoint and a held click.
  Staff letters outside its viewport are intentional scrolling content. Music-start welcome omissions prevent narration over a take.
- Left open: phone note/history scrolling. Sound-off hush is expected. The full audit was not repeated after repairs, per the once-only rule.
- Mechanical audit reported clean Motion off, action resizing, per-control errors/Enter paths and five-click how-line counts.

#### Frames looked at
- Two bar-tool frames, every final WebP at output size, art contact sheet and the side-by-side Feel comparison.
- Early 4, checks 4, logic 1, journey 7, final-size suite 12, target fixes 6, last frames 3, repair frames 8 and lead frames 8.
- Closing live-resize frame, Space keyboard frame and both final count-in frames.
- All 33 audit frames reviewed on nine contact sheets, with close-ups of compact notes, phone manners and concert guides.
- Size suite: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 through the iframe host.
- Grayscale, Motion off, keyboard-only activation, live Score, all concert parts, clean takes and nonempty histories were inspected.
- The only early browser-host resource error was a missing parent favicon. Targeted host runs use an inline icon and report zero errors.
- An early logic-test assertion counted Lune notes incorrectly; the corrected 88-event clean list test passes. This was a test error.

#### Art made
- 10 separate built-in imagegen images: music room, school stage, and two poses each for rabbit, owl, badger and fox.
- Final art 694.4 KB. Bundle 1035.2 KB. Prompts and house style are in art/prompts.json, with drawn_by codex.
- Used only art.py --rekey for finishing. Re-keyed with despill and holes to remove edge tint; no images needed a redraw.
- Original full prompts, raw images and generated-image provenance are preserved. No generated people; audience is code silhouettes.

#### Art still to paint
None. All ten requested assets are present and placed.

#### Engine changes wanted
- kit/music-studio.js, play: stable per-event pan support. Tool-local registered instruments supply stereo panning for now.
- kit/music-studio.js, blow: optional vibrato depth multiplier. Tool-local scoped createGain adapter halves the existing vibrato assignment.
- Fractional semi already works in MS.freq. No shared file was changed. Adapter implementation and risks are documented in handoff.md.

#### Left open
- Human headphone review of tone quality and how clearly each fault stands out in the four-player mix.
- Recorded Leda narration is absent because recording was prohibited. Browser speech works; 37 requested how/event strings are prepared.
- Phone note-building/history and optional unfiltered cards at 680 use page scrolling. Core players, bars and Play remain in view.
- Specified manners-choice lengths can cue a guess. The content was kept as supplied rather than inventing replacement choices.
- The vibrato adapter depends on the current MS.blow implementation. A stable engine option is preferable in a later authorized shared-engine change.
- Final repairs received focused checks rather than a second full audit. Cold review is still the next stage; no polish round was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: recorder-concert-rehearsal

#### Played
Cold as a grade 4 learner before builder notes/source: both rehearsals, wrong and precise notes, Solo/Loop/Score, all manners, concert joining, and first/final comparison. Warm cast and earned concert are strong; projector and phone layouts were also inspected.

#### Findings fixed
- **Blocker, general, Rehearsal:** concert invitation appeared before hearing the final fix. It now requires a completed clean take; both fresh scripted pieces verified in four actual takes.
- **Should fix, general, checklist:** choosing another criterion erased the previous judgment. Independent Needs work marks now survive until the next take; the latest selection filters cards.
- **Should fix, general, layout:** unfiltered choices ran past laptop/phone folds. A three-column tray keeps all six cards, Who/Where and Give note visible. Compact Piece/New/Start over remain live beside Score.
- **Should fix, general, focus/how-to:** Give note could hide its focused button; it now returns focus to Play. The spoken instruction names an actual checklist control; the voice manifest matches.
- **Should fix, family:music-studio, Concert:** leaving tuning left its music running. Moment navigation stops transport; failed gated navigation and comparison piece changes refresh controls. Tuning labels follow sounding events.
- **Should fix, general, audit frames:** removed the redundant caption touching players and reserved readable space for four score labels. Phone join choices and empty history now fit; the transport hint identifies First/Final.
- **Should fix, general, scene state:** audience chatter could persist outside manners. Its display is now scoped to the manners scene.
- **Polish, general, weakest art:** Otis play had different eyes/plumage from rest. Redrawn with built-in imagegen from the resting reference, then finished with art.py --rekey. Original raw retained in Scratch.
- **Polish, general, flattest moment:** manners were mostly captions. Layered audience shows chatter/quiet, tuning identifies each sounding player, and a held pause precedes the shared bow.
- **Polish, family:music-studio, Score:** rushing also has a non-color underline alongside compressed note spacing.

#### Findings left
- **Should fix, general, spec-constrained:** correct manners choices remain conspicuously longer. Supplied choice content was retained; replacement wording needs a spec decision.

#### Flattest moment left
Repeated vague notes replay an unchanged full take. That is deliberate listening evidence, but it is the slowest repeated beat.

#### Graphics
All ten final WebPs checked at output size and in scenes. Kept both backdrops and the cast; replaced only Otis play. Audience remains code silhouettes; no generated people. Art 700.0 KB; final bundle 1052.4 KB.
Saved redraw: art/raw/otis-play.png and art/otis-play.webp. Full prompt/reference/provenance: art/prompts.json, otis-play. No missing art tokens. Bar-tool frames from Beat Lab and Snowy Mail Route were inspected.

#### Audit
Completed once: _scratch/recorder-concert-rehearsal/review-audit/audit.md, ports 9941/8745, 2400-second limit. All 39 frames inspected.
23 leads: ten confirmed layout leads fixed; three scrolling-staff groups and ten music-start welcome omissions are intentional. Dispositions: Scratch/audit-dispositions.md.
Only five affected frames re-shot after corrections. Targeted checks are clean except intentional offscreen staff notes; zero console errors. No second full audit.
Every required size, Motion off, grayscale/keyboard, repeated/quick clicks, Read/mode switching and live controls checked. Audit resize stress: no exceptions or stranded disabled controls.
Wrong player/bar/vague event lists stay identical; exact fixes remove one problem. Two thousand random rehearsals were distinct, solvable and sound-changing. Storage contains only first/last problem lists and notes; no network resources or microphone calls.
Numbers recomputed: G5 783.99, A5 880, B5 987.77 Hz; 40 cents factor 1.023373892; clean pieces 10.91/20 seconds, rushed bar 2.37 versus 2.73 seconds. Listed text contrast pairs all meet AA, from 5.45:1 upward.

Five actual takes, held clicks, two-second room after results:

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| welcomeRehearsal | welcome | 1 | 1 |
| markHow | how | 1 | 1 |
| noChange | event | 4 | 4 |

noteHow/toolsHow queued lines were dropped only after the learner immediately acted onward. Audit repeated/quick-click checks were clean; hints remain available through Read.

#### Left open
No subjective headphone or classroom trial; synthesis/event checks and muted Chrome do not establish perceptual clarity. Recorded Leda clips remain absent because recording is prohibited. Shared pan/vibrato adapter requests remain in handoff; no kit changes were made.
Long accumulated note histories still scroll. Compact scenes crop the backdrop to preserve whole players and visible choices. The full audit predates its final focused layout corrections, as required by the one-audit rule.
Chrome instances and host closed; host.html removed. Writes confined to this tool and its Scratch folder. No git commits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Recorder Concert Rehearsal handoff

#### Build and layout

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

#### Musical model

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

#### Voice

The requested bank is big-sister, Leda. No audio was recorded, as required by this build brief.
`Curio.voice` supplies the queue and browser-speech fallback. The tool owns the hint, with Read reading its current text.
How lines use `V.heard` through the helper; fixed, noChange, notThem, ready and manners lines are events.
The mode scope is mode plus piece. Result lines wait until a completed take and expire at the next playback.

#### Art

Ten built-in imagegen calls produced ten individual PNG assets, copied to art/raw and processed only with `art.py --rekey <name>`.
Animal assets use a green key and despill. Full prompts and house style are in art/prompts.json; `drawn_by` is codex.
The holes option removes residual green from whiskers and fur. Each asset was inspected on the contact sheet and in the scene.
The art is animals and unoccupied settings. The audience is code silhouettes. No generated people or recorded audio.

#### Open questions

The specification lists no open questions for Cory.

#### Engine changes wanted

- `kit/music-studio.js`, `play`: support per-event `pan` by routing the event bus through a StereoPannerNode.
  Current tool workaround registers per-player instruments and routes their dry sound through stereo panners.
- `kit/music-studio.js`, `blow`: accept an optional vibrato-depth multiplier, default 1, so a recorder can pass 0.5.
  Current scoped adapter intercepts the second createGain call and halves only that vibrato AudioParam assignment,
  restoring createGain in finally. This relies on the current blow implementation and deserves a stable engine option.
- No fractional pitch change is needed: `MS.freq` already accepts 0.4 semitones.

#### Next review

The 2026-11-04 cold review played the whole tool before reading the builder documents. No commit was made.
Use the saved event-list tests and held-click journey to distinguish synthesis inspection from an actual headphone review.
Browser speech quality differs from the specified recorded Leda voice; recording remains owner work.
The cold review repaired phone and compact note-building. All six unfiltered cards, the players, bars and Play fit
without scrolling, including the eight-bar phone Score view. layoutNotes and layoutJoin preserve focus when moving controls.

#### Final verification

The audit completed once with 55 leads. Dispositions are in the tool report and scratch/audit-responses.md.
Final repairs received focused held-click, keyboard, phone-guide and live-resize checks, all without console errors.
All test Chrome instances and host servers are closed, and host.html is removed.
Scratch write_tool.py generated the first draft only. The final owning source is src.html; do not rerun that generator.

#### Cold review repairs, 2026-11-04

- Concert invitation waits for a completed clean take. endTake consumes the pending result before rendering the invitation.
- Checklist marks are independent; the last-tapped criterion filters cards. Marks reset after each completed take.
- Give note returns focus to Play when the builder closes. The how-to now names an actual checklist control.
- Leaving a tuning moment stops its audio. Failed gated navigation refreshes transport controls.
- The tuning label follows the actual sounding event; the audience quiets visually and the shared bow follows a held pause.
- Otis playing pose was redrawn from his resting pose with built-in imagegen, then finished with art.py --rekey.
  All ten images remain; the layered audience remains code silhouettes. No generated people or recorded audio.
- Audit states now include all six cards and eight-bar phone Score view. Review evidence is under Scratch.

#### Cold review final verification

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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
