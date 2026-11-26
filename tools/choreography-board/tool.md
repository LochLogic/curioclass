# Choreography Board: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: choreography-board
#### Built
Build only in the requested checkout and folders. No commits, branch operations or polish round.
Offline Build, Compare and Show; 12 starters, 24 moves, eight devices, five formations, four synthesized tracks, custom phrases, 40-version history, reasons, local save and clear.
Uses kit:curio, Curio.voice and kit:dance. The moving kit figure is temporary, as the owner requests. No people images were generated.

#### Numbers check
spec-calculations.py independently recomputed all supplied numeric claims. No discrepancies.
Contrast: mint/paper 10.400, mint/panel 9.504, dark ink/mint 10.150, ink/panel 14.193, muted/panel 7.158.
Dancer colors/paper: 8.025, 9.800, 12.747, 10.107. All specified text pairs exceed AA.
24 counts at Pulse/Drift/Strut/Storm: 12.857/18.947/15.000/10.909 seconds. 96 counts: 51.429/75.789/60.000/43.636 seconds.
Maximum block: 8 x 2 x 2 + 3 x 2 = 38 counts. Three maximum blocks = 114, refused. Double time with four dancers and Canon 1 = 7 counts.
Rise's levels per dancer: 4 Low, 2 Middle, 2 High. Half time: 8/4/4. The browser hand recount for two dancers gives 16/8/8 over 32 dancer-counts.

#### Feel check
Played the entire starter and an entire Show without seeking. Both ended naturally; Show used its title, changing light and bow. Best moment: four dancers passing Rise through a two-count canon while the playhead tracks the longer block.
Two flattest moments: paired Wave poses initially held the same arm shape, so I added folded-to-open wave keyframes; crowded Line arms crossed neighboring bodies, so I spread the line and fitted larger casts. Floor shapes also received native Low/High treatment.
The painted theater has strong foreground floor grain, middle-stage depth and a lit cyclorama. Bar tools were bundled into Scratch without altering their folders, opened, and viewed. Side-by-side frame evidence is _scratch/choreography-board/bar-comparison.jpg. The scene has comparable atmosphere; the code dancers remain visibly provisional.

#### Done when
1. PASS: starter plays, Stop acts immediately, Loop wraps, count and playhead agree. Complete starter ends at Count 24 of 24.
2. PASS: device transformations and stacked durations checked in the browser. Retrograde begins with the original final shape; Half time 16, Double time 4, Repeat doubles, Canon delays and grows the block.
3. PASS: solo Canon, 114 counts and nine blocks refused. Exactly 96 counts accepted.
4. PASS: one clock feeds both versions; Ghost outlines render. Retrograde measures are identical, with the Same ingredients line. Half time hand recount matches. One-version Compare says No changes yet.
5. PASS: Go back appends a version, Undo/Redo restore choices, reload preserves title/custom phrases/history, Clear saved removes the storage key. Forty-version cap checked.
6. PASS: Arc and fold saved with its chosen moves and levels, appears in the library, places with Enter, and survives reload.
7. PASS: full Show finished, bowed, hid the panel; Stop cancels the title delay and Back returns immediately.
8. PASS on inspected frames: stage is 998 x 496.6 at 1366 x 768 and 912 x 448.6 at 1280 x 720. Both exceed 55% width and 60% height. Compare's equal stages together exceed the panel width. Contact stays on painted boards.
9. PASS: live device edit restarts the current block; track swap keeps the current count; Stop immediate. Measured device edit about 5 ms after icon caching.
10. PASS: all specified sizes inspected; stage/timeline/Play together on laptops, block names 12 px at 1000 x 625. Phone page overflow is zero; only the timeline scrolls sideways. Main device buttons fit at 375 and 680.
11. PASS with browser speech: Mirror teaching line once over five taps; five canon refusals all started with two-second taps; Read stops play, and no welcome plays over music. Recorded hero-coach clips remain unmade, as instructed.

#### Wave lessons
- Hint and voice: PASS. Hints update synchronously, action controls named, Curio.voice heard keys, scoped validity and event keys; held-click logs saved.
- Focus and layout: PASS in targeted corrections. Phrase chips and timeline selection update in place. Keyed history focus, Try focus on editor entry, Show entry/exit focus, Save/place focus and Undo/Redo boundary focus verified. Fixed hint head prevents overlap.
- Sizes: PASS for 44 px targets and the inspected primary controls. The audit found no small-target leads. Try and Save were corrected and rechecked at 680 and 375. Secondary authoring sections intentionally scroll vertically.
- No giveaways: N/A. Open-ended studio, no scored correct option or puzzle meter.
- Honest numbers: PASS. Every-dancer/every-count definition, canon holds and rounding assumptions are stated in notes and Compare.
- Standards: PASS. Students make phrases, apply and organize devices, compare revisions and record reasons.
- Motion off: PASS. Timing is unchanged, keyframes replace interpolation, standby animation is explicitly disabled.
- Short choices: FAIL under a literal all-choices-at-once reading. The eight main devices fit, but the library, formation/history sections and 24-move palette require vertical scrolling. This preserves the specified large stage; retained as an explicit cold-review ergonomics question.
- Resize mid-animation: PASS in the full audit: no exceptions or controls left disabled. Existing actors retain state while the floor and crop resize. The later panel/focus fixes received targeted checks, not another full audit.
- Deferred welcome: PASS. No welcomeAfter; Play is a speaks control, welcome has a playback validity check.
- Unknown as unknown: N/A. No hidden factual clues.
- One look, one meaning: PASS. Badge shape and color consistently identify each dancer; device tags include symbols.
- Badge says true: PASS. Count, version, cast and formation labels derive from current data; editor labels show one dancer and eight counts.
- Hint changes back: PASS. Mode, selection, placement, reset and editor transitions replace the hint immediately.
- No answer by copying: N/A. No diagnosis quiz or answer cards.

#### Audit leads
The full audit ran once and completed, reporting 461 leads. It found no console errors, no resize exceptions or stuck controls, and no infinite Motion-off animation. It is not a clean final audit: the full run preceded the corrections below and was not rerun.
All 447 listed bullet rows have individual line-numbered answers in _scratch/choreography-board/audit/dispositions.json. The other 14 walk warnings are answered below. The original 587-line report is audit.md beside that ledger.
- 11 naming rows: FIXED. Explicit aria-labels added to title and reason-note; associated visible labels were already present.
- 308 below-fold rows: RETAINED. These are secondary library, cast, formation, move, reason and history controls in the required stacked layouts at 760 and 375. Main Play and the eight device buttons fit. See the short-choice exception above.
- 16 timeline-scroll rows: INTENTIONAL. Proportional blocks and the eight editor slots scroll within their own box, as required at 375. They remain keyboard reachable. No page-wide horizontal overflow.
- 53 overlap rows: FIXED. Transport/hint moved above a separate scrolling body; the phrase editor hides the duplicate transport. Targeted frames show no transport/hint or editor-control overlap.
- 9 editor keep/hint rows: FIXED. Editor resets scroll, focuses Try, and exposes stage, slots, Try and Save. Save's bottom is 323 px at 680x425 and 721.1 px in the 375x812 host.
- 2 editor short-panel rows: FIXED for Try/Save visibility; the 24-move palette intentionally scrolls.
- 2 state focus rows: FIXED. Show opens with focus on Play; Make opens with focus on Try.
- 1 hidden Show hint row: INTENTIONAL. Show hides the panel and presents only its stage, title and slim controls, as the spec requests.
- 43 modal coverage rows: INTENTIONAL. Confirmation covers the stage and background controls. Background is now inert, focus trapped, and audit keep regions are scoped to the dialog rather than the covered stage.
- 2 quick-mode welcome rows: FIXED. Repeating an already active mode no longer hushes the line. Held taps 0.7 seconds apart produced one complete, uncut welcome in Build and Compare.
- Additional walk warnings, 10 skipped welcomes: EXPECTED. Play suppresses narration over music; phrase and block taps give their own how line priority, per STANDARDS. No welcomeAfter is used.
- Additional walk warnings, 3 focus losses: FIXED. Show entry, the version picker/list and Back now retain or deliberately transfer focus. Targeted focus checks passed.
- Additional walk warning, 1 idle Show Stop with no change: EXPECTED. There is no performance or title delay to stop on initial Show entry.
Other walk observations: Loop selecting the first block intentionally reveals its controls. Phrase and pure timeline selection no longer rebuild their buttons. Compare timeline taps now use Compare instructions and insertion gaps are disabled there.
Post-audit checks: nine held-input/state frames passed with zero errors, covering quick welcomes, panel overlap, compact/phone editor, Show focus, Compare controls, inert dialog and Clear saved. Earlier targeted focus checks verified placement, version selection and Undo/Redo.

#### Frames looked at
Bar Snowy Mail Route and Beat Lab; early five frames; 11 main size/keyboard/Motion/grayscale frames plus targeted phone, portrait and compact corrections; eight interaction frames; seven extreme/mode frames; three voice frames; four full-play/event frames. Contact sheets and full frames are in _scratch/choreography-board/.
Audit contact sheets audit-0.jpg through audit-10.jpg were all viewed, covering all 81 audit PNGs. Final correction evidence: post-audit-frames, editor-final-frames, focus-final-frames and final-frames, also viewed. All artifacts are in Scratch.

#### Art made
One generated empty theater, 1600 x 900 WebP, 79.6 KiB (81474 bytes). Raw PNG retained in art/raw. Built-in imagegen; no redraw required. Bundle: 291.2 KiB (298171 bytes), below 2 MB.
Full prompt and fitted crop geometry are in art/prompts.json. Credit is in metadata and source.

#### Art still to paint
Owner's final direction is painted dancers. Fifty-six people:true pose assets and registration/facing/level/badge requirements are recorded for the next painter. No people assets generated in this build.

#### Engine changes wanted
kit/dance.js floor.draw: explicit options to suppress engine stage decoration over a painting.
kit/dance.js level: native low floor poses and higher variants that rise upright. Local poseFor workarounds are in this tool; the shared kit was not modified.

#### Left open
Painted dancer replacement and recorded hero-coach narration are intentionally deferred. Storm/Strut instrument colors use kit synth approximations.
Secondary-panel ergonomics remain open under the literal short-choice rule. The full audit was not rerun after the documented narrow fixes; do not call the final build audit-clean. Storm/Strut timbres are kit synth approximations, not acoustic recordings.
Cold review is next. No polish round was started. host.html was removed. Ports 8795, 9990, 9991 and 9992 were checked closed; all Chrome/server processes started here were shut down.
Final static checks: voice manifest matches all 19 fixed lines; no external resource URLs, no em dashes, and no source line exceeds 157 characters.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: choreography-board

#### Played
Grade 7 solo walkthrough before reading builder notes: starter playback, revision, split Compare, Ghost, phrase making/saving and complete Show; then projector and keyboard checks. The theater and synchronized revision were strong; the provisional figures and buried choices weakened them.

#### Findings fixed
- **Should fix, family:dance, src.html/art:** replaced the code performers with a natural range of four painted dancers, preserving costume colors, badge shapes, timing, floor registration and the isolated renderer adapter.
- **Should fix, family:dance, grounded rendering:** the first articulated painting distorted low and waist-bent bodies. Following the owner's correction, painted complete curl, kneel, crouch, sit, lie, roll and bow poses for each dancer. Corrected the fourth bow's prosthesis side. Fresh people-art review passed.
- **Should fix, family:dance, movement data:** Push and pull used an ordinary lunge without the push; Leap across repeated one running leg position. Added the extended push and alternating running keyframes.
- **Should fix, general, Build/editor:** short choice sets disappeared in long scrolling panels. Added persistent section navigation, compact native choices and one visible move group at a time. Play and the eight initial device buttons fit the checked sizes.
- **Should fix, general, Compare:** reasons were buried below measures. Separated Before, Measures and Reasons; compact reason selection and notes fit. Explicitly hid collapsed version-list content, eliminating phantom overlap boxes.
- **Should fix, general, device options:** selecting an option reset scrolling and hid focus. Preserved focus and provided compact Device/Device option pickers so choosing an option does not hide the other device choices. Meanings and the next action remain in the hint.
- **Should fix, general, history/voice:** History's instruction named unavailable Undo/Redo controls. Reworded it; section changes now update hints immediately and stop stale speech. All 31 fixed lines match the voice manifest.
- **Should fix, general, history:** Go back to Before failed to record a version when the dances matched. It now appends a version. Clear saved removes storage and returns focus to Play; empty-stage guidance names Phrases.
- **Polish, family:dance, artwork adapter:** repaired neck registration and repeated-thumbnail clip IDs; shared atlas references avoid copying large image strings into every cached icon.
- **Polish, general, Show:** the ending felt generic. Its closing title now names the student's phrase/count total and chosen devices/reason, with a complete painted bow. Fixed singular wording.

#### Findings left
- **Polish, family:dance:** complete grounded paintings change on count boundaries. Continuous floor transitions and additional facing/energy variants remain less detailed than upright movement. The fourth dancer's physical prosthesis is preserved rather than mirrored with the whole sprite.
- **Polish, general:** narration still uses browser speech. Hero-coach recordings remain unmade, consistent with the instruction not to record audio.

#### Flattest moment left
The holds between complete floor paintings are more abrupt than the continuous upright rig. They preserve natural anatomy and readable count shapes; the stage, music, canon and playhead keep their timing.

#### Graphics
Kept the warm theater, lighting, proportional timeline and detailed studio styling. Added three people:true atlases with the built-in image tool: four upright dancers in front/back views plus seven complete poses per dancer, 36 registered views in total. No unmade art tokens remain.
Prompts and provenance: art/prompts.json. Finished paintings: cb-dancer-cast.webp, cb-grounded-cast.webp and cb-floor-bow-cast.webp. Whole-body poses and upright registration remain easy to replace without changing choreography data or clocks.
Inspected the paintings at stage/thumbnail sizes, including grayscale and the final Lie palette path. People review: _scratch/choreography-board/people-review.md. Compared the finish with Beat Lab and Snowy Mail Route.
Final bundle: 1,852,639 bytes, 1809.2 KiB (1.77 MiB).

#### Audit
The single audit completed within its 40-minute limit, using Chrome 9931 and host 8735. It reported 113 grouped leads. All 97 audit PNGs were inspected in 13 contact sheets.
No audit console errors, small-target findings, resize exceptions, stuck controls or infinite Motion-off animations. Held-click focus/Enter paths and all speaking-control five-tap and quick-tap checks passed.
Confirmed Compare and option-visibility leads were fixed. Expected leads are proportional timeline/count-slot scrolling, panel hints hidden by Show or its inert confirmation dialog, first-tap welcome suppression for a control's own instruction/music, and idle Show Stop doing nothing. Closed-details overlap reports were not painted overlaps; explicit hidden state also removes their DOM boxes.
Every audit row has a disposition in _scratch/choreography-board/review-audit/dispositions.json. Twenty latest targeted layout inspections passed, leaving only intentional timeline scrolling. Final targeted batches had no console errors. The full audit was not rerun after the scoped repairs.
Independent arithmetic and browser checks confirmed 38-count maximum blocks, 7-count double-time/canon blocks, the 96-count limit, starter/maximum run lengths and Rise's dancer-count recount before/after Retrograde and Half time. Specified text contrast pairs exceed AA.

| Voice line | Kind | Expected over five taps | Spoken |
|---|---|---|---|
| Mirror explanation | how | 1 | 1 |
| Over-limit refusal | event | 5 | 5 |

Saved reasons/notes survived reload; returning to identical Before, Clear saved and empty guidance passed targeted checks. Evidence is in post-audit-verification.json, semantic-final-frames and compact-native-frames under Scratch.

#### Left open
Grounded transition/facing fidelity and recorded narration above. No kit changes, commits or deployment. Test Chrome/server processes were closed and host.html removed. This was one cold review and one full audit, followed only by repairs and targeted re-checks.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Choreography Board build handoff

#### Layout and data
src.html starts from the kit starter structure and uses kit:curio and kit:dance. Styles, movement data, devices, persistence, voice, sampling, stage rendering, playback, editing and UI wiring are in that order. The panel appears before the timeline in DOM order for keyboard access. The theater and floor are laid out in real pixels on resize, with a cover-cropped 1600 by 900 painting.

The painting's floor seam is y 59%, front contact limit y 94%; the cyc is x 22.3% to 77.1%, y 9% to 59%. fitView recomputes its crop and the floor projection together. All theater art uses art:cb-blackbox. Art prompt, source and placement geometry are in art/prompts.json.

#### Tricky parts
transformFrames applies Level, Size, Dynamics, Mirror and Retrograde. sample maps time through Tempo, Repeat and per-dancer Canon delays, holds completed dancers and walks formation changes for two counts. Dance.phrase interpolates keyframes; Dance.clock and Dance.play own time. Compare attaches two play handles to a single clock, using the current track. The composed phrases map per-block canon offsets because canon can change on every block.

History is capped at 40. Undo and Redo move the current pointer. An edit after Undo appends, preserving intervening versions. Reasons annotate versions directly. All persistence is wrapped in try/catch and uses choreography-board. Clear saved returns to a fresh unsaved starter; the next edit enables saving again.

Line spreads dancers across the floor instead of putting neighboring outstretched arms through one another. Three and four dancers use a smaller presentation scale; Cluster deliberately overlaps. These are presentation choices, separate from the Size device, which changes joint reach and travel. Future paintings must preserve this spacing and floor contact.

poseFor preserves already-low floor shapes and raises floor phrases onto the toes for Higher. The generic kit modifier alone can fold an already-low shape past its support or label a lying figure High. The local workaround keeps the level readout meaningful.

All repeated refusal events get unique queue keys. This prevents the shared queue from replacing a still-waiting identical event during two-second taps. How lines retain stable keys and speak once. Read stops music before reading. The final five-tap refusal check recorded all five events starting.

The four backing tracks use the shared engine's synthesized instruments. Storm's low drum and string-pad colors, and Strut's snap sound, are synthesized approximations, not recordings.

#### Painted dancers after cold review
Owner's final direction is implemented. art:cb-dancer-cast is three people:true atlases: four upright articulated dancers front/back, plus seven complete grounded/bending poses for each dancer (curl, kneel reach, crouch, sit, lie, roll, bow). These replace the unmade 56-pose plan. Whole-body poses are selected by groundedKey and registered in groundedPoses; upright joints remain in addPaintedRig. Atlas images are shared SVG references, avoiding repeated base64 strings in cached icons. addPaintedRig uses clipped affine pieces registered to Dance's screen joints, so all existing transforms, timing, facings and levels remain data driven. paintedRig holds the atlas URL, dimensions and registration. createPerformer, paintPerformer and paintIcon remain the swap boundaries. Ghost uses faint painted-silhouette outlines. Unique clip IDs are essential when cached icons repeat.

Fresh people-art check: _scratch/choreography-board/people-review.md. Source representation passed; initial neck and cached-thumbnail registration issues were fixed and the same reviewer confirmed the scoped repairs.

Build sections are persistent Devices, Cast, Phrases and History views. Compact screens use native short-set pickers. The editor shows one move group at a time. Audit states include the section navigation; do not target hidden controls directly. Show's closing title includes phrase/count/device choices. Push now has extended arms, and Leap across alternates running legs.

#### Open questions resolved
The spec leans toward hero-coach (Puck), so the voice manifest uses hero-coach. No recorded voice was created, per Build-only rules; browser speech is the fallback.

The move list says four groups but names five groups. All five named groups and all 24 listed moves are included. No moves were dropped.

#### Engine changes wanted
- kit/dance.js, floor.draw: add explicit options to suppress the stage background, floor fill and curtains. The tool currently clears those layers after each resize to align the painting.
- kit/dance.js, level: give crouch, sit, lie and roll native low variants. Applying the generic low modifier to an already low floor shape bends it past its support. poseFor works around this locally by preserving those native floor shapes at Low.
- kit/dance.js, level: give floor shapes meaningful high variants that rise from the floor. poseFor supplies an upright tiptoe version locally.

#### Next
The cold review is documented in codex-review.md. The owner requested complete paintings for low and waist-bent poses; those are implemented. See codex-report.md for actual verification and remaining limits.

#### Build verification and audit dispositions
The full mechanical audit ran once and completed: 461 leads, no console errors, no resize exceptions or stuck controls, and no infinite Motion-off animation. Its 81 frames were inspected in eleven contact sheets.

The original audit is in _scratch/choreography-board/audit/audit.md. dispositions.json beside it answers all 447 listed bullet rows and the additional walk warnings. Most retained rows describe secondary controls below the fold in the required stacked layout, the intentionally scrolling timeline, or an intentionally covering confirmation dialog.

Fixes after that audit: explicit input labels; a fixed transport/hint head above a separate scrolling authoring body; editor scroll reset and Try focus; keyed history focus; sensible focus after Show, Save, placement, deletion and history boundaries; inert modal background; persistent phrase/timeline controls; no stale device instruction in Compare; no welcome cut on repeated taps of an active mode. Targeted post-audit frames and browser logs verify those corrections. The entire mechanical audit was not rerun.

Long authoring panels still require vertical scrolling on 375 and 760 wide screens. The eight primary device buttons and Play fit initially; all 24 palette moves and the whole history/library cannot fit beside a large stage. Advanced device options and secondary controls remain a cold-review ergonomics question.

The build-time bundle was 298171 bytes. Cold review added the three painted cast atlases; see codex-review.md for final size. The host page was removed and every Chrome/server started by the build was closed. Recorded voice remains intentionally deferred; painted dancers were completed during cold review.

#### Whole-body pose registration
Dedicated low and bending paintings preserve natural anatomy instead of warping an upright torso. There are seven core poses per dancer, used on count boundaries; upright poses retain continuous joint interpolation. The fourth bow cell is mirrored once to correct the source prosthesis side, and fourth-dancer whole-body sprites do not mirror their physical prosthesis with the Mirror device. The other dancers demonstrate the side change. Further facing-specific floor illustrations could improve fidelity.

#### Cold review verification (current)
The single cold-review audit completed with 113 grouped leads and 97 inspected frames, using Chrome 9931 and host 8735 with a 40-minute limit. No console errors, infinite Motion-off animations, resize exceptions or stuck controls. All held-click focus/Enter paths and all speaking-control repeat/quick checks passed. Dispositions: _scratch/choreography-board/review-audit/dispositions.json.

Confirmed fixes after that audit: separate Before, Measures and Reasons views in Compare; collapsed version lists explicitly hidden; compact reason picker; compact Device and Device option pickers; preserved option focus; tab-specific hints and speech validity. Native compact choices expose every option without scrolling a short choice set. Stage and Play remain in view. Updated audit-states include these paths.

Targeted checks passed at all eight Compare sizes and selected Reasons/device sizes, including a 375-wide iframe. Twenty latest layout inspections leave only intentional proportional timeline scrolling. Reasons and notes survive reload. Returning to an identical Before still records a new version. Clear saved removes storage and returns focus to Play. Empty-stage guidance names Phrases. The 31 fixed voice lines exactly match allLines(). The full audit was not rerun after these scoped repairs.

People-art review passed for all three cast atlases and the grounded stage frames: _scratch/choreography-board/people-review.md. The real Lie palette path also updates its count thumbnail. The final offline bundle is about 1.77 MiB. No kit changes, git commits or deployment. All test Chrome/server processes were closed and host.html removed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
