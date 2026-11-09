# Codex report: toy-ad-reality-check

## Built

Built The ad, The lab and The verdict as one offline HTML file using the kit starter, stylesheet, sound helpers and Curio.voice.
The evidence-folder frame contains a large illustrated TV, seven trick controls, a six-shot timeline, plain comparisons,
five test stations, six evidence-backed claim stamps, two opinion ratings, rule mapping, a cost check and a personal case recap.
The verdict uses five short folder leaves. The case board is always one tap away.
Thirteen images were generated in this build. No people, downloaded art, audio recordings, shared-file edits, commits or polish round.
Source, metadata, notes, voice manifest, audit states, handoff and artwork are in the authorized tool folder.
Plans, scripts, generated contact sheets, logs and frames are confined to _scratch/toy-ad-reality-check.

## Numbers check

Independent Python: _scratch/toy-ad-reality-check/numbers.json, generated before implementation.
- 1 / 1.7 = 0.588235 meters per second, displayed as about 0.59.
- 1.7 / 3 = 0.566667 seconds, displayed as about 0.57; the spec's 0.6 is coarser rounding.
- 2999 + 1999 + 999 + 549 = 6546 cents; extra cost is 3547 cents.
- 3 + 3 + 3 + 2 + 2 + 2 = 15 seconds, six shots.
- Eight depicted racers were counted in the generated crowd image.
- Contrast: white/charcoal 13.160; charcoal/paper 11.608; charcoal/panel 10.183; charcoal/yellow 8.008.
- Muted/paper 5.676; muted/panel 4.979; red/paper 5.766; green/paper 5.759. All stated ratios recompute correctly.
The ruler uses evenly spaced code marks; the toy spans 12/30 of its scale. Timing acceptance is inclusive from 1.4 to 2.0 seconds.

## Facts checked

Every toy fact is fictional teaching data from spec.md Content, not a real product claim or shopping recommendation.

| Student-facing fact | Source and check |
| --- | --- |
| Six shots, 15 seconds, their order and duration | Spec Content; independent sum above; timeline and playback checks. |
| A low camera, close framing, changed playback speed and added sound can shape a toy claim | Spec's constructed shots and plain-view contrasts; Common Sense Education media literacy context. |
| 12 cm toy; 30 cm ruler; one-meter timing track | Spec Lab results and Screens; code geometry and real drag/keyboard measurement. |
| Real 1.7 s, ad about 0.57 s, about three times faster, about 0.59 m/s | Spec fictional inputs; independent division above. |
| No box-only jump; 10 cm jump with a separate ramp | Spec Lab results; both animated outcomes played and both canyon stamps accepted. |
| Eyes really glow | Spec Night and Lights out; identical Night plain view and lab image. |
| One racer, one 30 cm straight track piece, stickers; no ramp, loop or batteries | Spec box contents and disclosure; checked against the generated image and box test. |
| Eight racers do not establish universal ownership; each is sold separately | Spec Crowd and Price; inspection and box comparison. |
| $29.99, $19.99, $9.99, $5.49; $65.46 total; $35.47 extra | Spec fictional prices; exact cents arithmetic. The check explicitly counts one racer. |
| Four U.S. advertising expectations and their shot mapping | CARU guideline sections 4b, 4c and 4h, plus the spec's fictional interpretation. Summaries, not statutory verdicts. |
| Ratings are judgments; evidence supports their reasons | Spec Verdict; any 1-to-5 pair accepted with evidence, no preferred opinion. |
| Progress stays on the device | Wrapped localStorage only; self-contained bundle, no external src/href resources or runtime service calls. |

Primary sources checked during the build:
- CARU: https://assets.bbbprograms.org/docs/default-source/caru/caru_advertisingguidelines.pdf
- CARU effective-date context: https://bbbprograms.org/media/newsroom/press/caru-revised-guidelines-for-advertising-to-children
- Common Sense Education: https://www.commonsense.org/education/family-tips/k-5-news-and-media-literacy
CARU was revised in 2021 and became effective in 2022. The UI correctly calls these industry guidelines.
The spec's broad MediaSmarts reference is retained in notes; its exact named lesson was not independently located.

## Break it

- Tried pinning before pausing/selecting a spot: refused; Enter on a focused trick is the documented keyboard alternative.
- Tried a sped-up-film card on Launch: refused with an explanation; the card stays available.
- Real held pointer drags pinned a trick and aligned the ruler. Horizontal movement without vertical alignment cannot complete measurement.
- Music-only pins can fill six cards as required, but cannot validate the final message or close the case. Fixed and retested.
- An untested claim cannot receive a stamp; a pinned claim and completed test are both required.
- Early stopwatch stops do not earn evidence. A successful 1.7 s stop did; the car finishes independently of the stopwatch.
- Trying the ramp before seeing the box-only fall is blocked. Rapidly bypassing the fall was fixed by granting that flag at animation completion.
- Both canyon marks are accepted. Other wrong stamps are refused; no points, high score or saved accuracy score exists.
- Ratings without evidence cannot close the case. Evidence chips unlock only after the related test and stamp.
- Arbitrary numeric rating choices are opinions; moving through all ratings grants no missing evidence.
- Cost parsing rejects trailing text, exponent notation, extra decimals, negative values, Infinity and NaN. $65.46 passes.
- Closing early lists missing work. Reload restores the complete case; New case clears it.
- Matrix result: 88/88 assertions passed: 42 shot/trick cases, 18 stamps, 25 opinion pairs and three evidence/closure gates.
Revising a stamp after inspecting a test is deliberately allowed. These are evidence-folder judgments, not an accuracy leaderboard.

## Voice walk

Science-narrator / Charon is specified in voice/lines.json. Recording was prohibited; actual playback uses the browser voice.
Main student path was driven with held clicks: Play, Pause, picture, Low angle, Plain view, remaining shots,
five tests plus the crowd comparison, stamps, message, two supporting cards, ratings, evidence, rules, cost and Close my case.
The first Play correctly takes its own how-to and skips the stale initial welcome.
The full initial log is voice-main.json; later queue fixes are covered by voice-final.json and voice-retest.json.
New how-to lines now start promptly; V.heard suppresses repeats. Events start immediately; Read retains priority.
Final held-click sequence: playHow, pinHow, right-low, welcomeLab, timeHow, welcomeVerdict.
Five Time it actions start timeHow once. Five wrong-speed events start five times in the side-path retest.
At a two-second action pace, the next action can cut browser speech. Starts and state validity are verified; complete uninterrupted speech is not claimed.
The spec's rapid spoken one-second price disclosure is not implemented as an acted clip. The visual disclosure and readable box flap are implemented.

## Feel check

Best moment: dramatic Launch becomes an ordinary tabletop toy in Plain view, then the ruler produces a small 12 cm measurement.
The first flat moment was a shallow, heavily cropped preview TV. Moving the timeline beside the finder restored a large stage.
The second was a long verdict form with its earned stamp below the fold. Folder leaves, paired ratings and a compact end card fixed it.
I played the whole case through closure. The jump failure and extra-ramp comparison give the lab a visible consequence.
The tool is suitable for one evidence case, not endless replay; its later depth is the move from spotting to testing and defending a judgment.
_scratch/toy-ad-reality-check/bar-comparison.png places the tool beside Beat Lab at the same width. Both frames were opened.
The large glossy art and tactile folder are comparably finished. The lab's code motion is intentionally plainer than the commercial.

## Done when

1. PASS: TV is the largest Ad element at 1366x768, 680x425 and 375 wide; the board has a persistent header button.
2. PASS with content ambiguity noted: six claims pin, wrong cards explain, Music pins anywhere; real drag and keyboard paths work.
3. PASS: Sound off retains engine-roar and crowd-cheering captions; sound tricks remain selectable.
4. PASS: five tests answer six claims through the box's extra crowd comparison; expected stamps and both canyon stamps work.
5. PASS: an unsupported rating asks for evidence; accepted evidence builds the student's own reason sentence.
6. PASS: Pause freezes immediately, Slow toggles, and timeline jumps preserve playback. Checks returned true.
7. PARTIAL: how lines start once and repeat events start on each action. Fast actions can interrupt browser fallback speech; bank identity is unrecorded.
8. PASS: complete progress restored after reload, including six stamps and ratings; New case clears state and saved closure.

## Wave lessons

- Hint and voice: PASS for immediate state hints, Read and heard-based how suppression; speech completion limitation above.
- Focus and layout: PASS for stable action nodes, visible keyboard focus and preventScroll dialog return. No focus is taken on load.
- Sizes: PASS in the seven desktop sizes and 375 iframe; 44 px controls, readable 11 px ruler labels and unclipped primary controls.
- No giveaways: no score or preferred rating; Music-only shortcut fixed. The spec's correct belief is the longest option; two specific supporting tricks are required.
- Honest numbers: fictional values and one-racer cost assumption are explicit; exact cents and fixed timing are used.
- Standards: each of Re7, Re8, Re9 and Cn11 is practiced by the solo student, as mapped in notes.md.
- Motion off: no infinite animation; elapsed timing continues. A 3.5-second wall-clock test returned about 3.516 seconds.
- Short choice sets: folder leaves and the two-column compact claim sheet keep short sets visible.
- Resize mid-animation: PASS in the audit, 1366x768 to 760x900 and back after state inputs and walk actions; no exceptions or locks.
- No late welcome: Play's own line suppresses it; welcomes become invalid after their first relevant action.
- Unknown stays unknown: claim text remains unpinned until a trick is found; evidence chips require a completed test and stamp.
- One look, one meaning: highlighter means a selected/pinned item; stamp text and icons distinguish the three judgments.
- Badge truth: only tested evidence yields a stamp; no claim is labeled checked before that.
- Hints change back: mode/test changes set hints at once; restored/finished states choose the current control.
- No answer by copying: message and support are distinct from measurements. Fixed spec wording still makes one message conspicuously longer.

## Audit leads

One full audit completed, exit 0, on Chrome 9981 and host 8785 within its 40-minute deadline.
Evidence: _scratch/toy-ad-reality-check/audit/audit.md. Its 34 leads are disposed below.

- Lead 1: Plain view "1 claims" fixed to "1 claim pinned"; targeted result confirms it.
- Lead 2: phone Plain view tag/shot-label overlap fixed by moving the comparison tag; overlap is false.
- Lead 3: case-board dialog covers the global hint intentionally. Dialog instructions replace it; focus is trapped and returned.
- Lead 4: case-board singular counter is the same defect as lead 1, fixed in the shared counter.
- Lead 5: phone Close/title bounding boxes overlap; reserved title width removes it. Targeted overlap is false.
- Leads 6-31, all 26 first-tap welcome omissions: intentional multi-mode voice behavior under STANDARDS.
  #tv, #play, #pause, #back, #plain, #shot-0 through #shot-5,
  #trick-low, #trick-close, #trick-speed, #trick-effects, #trick-crowd, #trick-print, #trick-music and #new-case
  give their own current instruction or error and skip the stale welcome. #global-board and #claim-0 through #claim-5
  open a modal, suppressing an irrelevant Ad welcome. Read and later mode entry retain a route to instructions.
- Leads 32-34: quick taps on #m-ad, #m-lab and #m-verdict cut the same-mode welcome. Fixed selected-mode taps to preserve speech.
  Each targeted held double tap now starts its welcome once with zero cuts.
- Unscored Sound-toggle observation: two header controls moved. Fixed with a stable button width; targeted check is true.

All eight default sizes, five explicit states at all sizes, Motion off, resize and 33-control held walk were mechanically clean
apart from the listed leads. Ten five-repeat speech controls were clean. No runtime exceptions or focus/disabled locks appeared.
Coverage limit: the auditor searches for modes inside header; this tool's mode nav is its sibling. It discovered zero automatic modes.
The five explicit states ran, but the automatic walk did not explore all Lab and Verdict controls. The complete student path,
keyboard lab, 88-case matrix and separate all-mode checks cover those controls. Four explicit Verdict routes were added to
audit-states.json for the cold reviewer. Ratings/evidence were also inspected at five additional sizes after the fixes.

This is one pre-fix full audit, not a claimed clean full audit of the final bundle. Its source and bundle snapshots are preserved
as audited-src.html and audited-bundle.html in Scratch; audited bundle SHA256:
218d3d118cefc0e4026fa82805d57a79014b61443f1f02d27c3d70415adb4f74.
Only the touched layouts/behaviors were checked afterward: twelve targeted frames, then one focused pause proof, all without errors.
Pause preserves the camera transform and is frozen after the final 16.6 ms compositor frame. Sound controls stay in place.
Saved Verdict guidance now points to Cards/Ratings; image alt text describes all six scenes and their plain comparisons.

## Frames looked at

Opened both bar frames, the first laptop/preview frames, all five functional/drag frames, all eight full-play frames,
all twelve full-size/keyboard/grayscale/Motion/voice frames, all twelve focused frames, all nine phone/playback frames,
all nine final target frames, the corrected rating/rule frames, keyboard-lab frame, all four art sheets and the bar comparison.
Opened all 49 audit PNGs using thirteen contact sheets, then all twelve post-audit PNGs using three sheets, plus the pause-proof PNG.

## Art made

13 finished images, 652330 bytes (637.04 KB). All are marked drawn_by: codex and people: false.
One canyon redraw and one cutout correction; the cutout's magenta edge was despilled by art.py --rekey.
Voice recordings: 0 KB, as instructed. Fifty-one fixed lines are listed for later recording.
Final bundle: 1382268 bytes (1349.87 KB), below the 2 MB goal. Art 637.04 KB; voice 0 KB.
Final bundle SHA256: 771d964927d436b628c348b1d32f2cb752b729d332b5a970ab16789f53421a29. Source is 1355 readable lines.

## Art still to paint

None. No people art was needed. No placeholders remain.

## Engine changes wanted

None. A future authorized rapid disclosure clip can use the existing voice map.

## Left open

- No recorded science-narrator voice or acted rapid disclosure, because the build prohibits recording.
- Browser speech may be cut by rapid actions; line-start evidence does not prove an uninterrupted audible performance.
- The art direction calls Speed low-angle while Content assigns Speed to sped-up film and sound effects. The explicit mapping was retained.
- Minor toy molding differences across generated frames should be judged in the cold review.
- The final bundle has targeted post-audit checks, not a second full audit. The automatic mode-discovery gap is documented above.
- Process closure and temporary host removal are recorded in Scratch/process-closure.json.

Build-only boundary: no git commits, no shared-file changes and no polish round. All build Chrome/server processes are closed; host.html removed.
