# Toy Ad Reality Check: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: toy-ad-reality-check

#### Built

Built The ad, The lab and The verdict as one offline HTML file using the kit starter, stylesheet, sound helpers and Curio.voice.
The evidence-folder frame contains a large illustrated TV, seven trick controls, a six-shot timeline, plain comparisons,
five test stations, six evidence-backed claim stamps, two opinion ratings, rule mapping, a cost check and a personal case recap.
The verdict uses five short folder leaves. The case board is always one tap away.
Thirteen images were generated in this build. No people, downloaded art, audio recordings, shared-file edits, commits or polish round.
Source, metadata, notes, voice manifest, audit states, handoff and artwork are in the authorized tool folder.
Plans, scripts, generated contact sheets, logs and frames are confined to _scratch/toy-ad-reality-check.

#### Numbers check

Independent Python: _scratch/toy-ad-reality-check/numbers.json, generated before implementation.
- 1 / 1.7 = 0.588235 meters per second, displayed as about 0.59.
- 1.7 / 3 = 0.566667 seconds, displayed as about 0.57; the spec's 0.6 is coarser rounding.
- 2999 + 1999 + 999 + 549 = 6546 cents; extra cost is 3547 cents.
- 3 + 3 + 3 + 2 + 2 + 2 = 15 seconds, six shots.
- Eight depicted racers were counted in the generated crowd image.
- Contrast: white/charcoal 13.160; charcoal/paper 11.608; charcoal/panel 10.183; charcoal/yellow 8.008.
- Muted/paper 5.676; muted/panel 4.979; red/paper 5.766; green/paper 5.759. All stated ratios recompute correctly.
The ruler uses evenly spaced code marks; the toy spans 12/30 of its scale. Timing acceptance is inclusive from 1.4 to 2.0 seconds.

#### Facts checked

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

#### Break it

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

#### Voice walk

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

#### Feel check

Best moment: dramatic Launch becomes an ordinary tabletop toy in Plain view, then the ruler produces a small 12 cm measurement.
The first flat moment was a shallow, heavily cropped preview TV. Moving the timeline beside the finder restored a large stage.
The second was a long verdict form with its earned stamp below the fold. Folder leaves, paired ratings and a compact end card fixed it.
I played the whole case through closure. The jump failure and extra-ramp comparison give the lab a visible consequence.
The tool is suitable for one evidence case, not endless replay; its later depth is the move from spotting to testing and defending a judgment.
_scratch/toy-ad-reality-check/bar-comparison.png places the tool beside Beat Lab at the same width. Both frames were opened.
The large glossy art and tactile folder are comparably finished. The lab's code motion is intentionally plainer than the commercial.

#### Done when

1. PASS: TV is the largest Ad element at 1366x768, 680x425 and 375 wide; the board has a persistent header button.
2. PASS with content ambiguity noted: six claims pin, wrong cards explain, Music pins anywhere; real drag and keyboard paths work.
3. PASS: Sound off retains engine-roar and crowd-cheering captions; sound tricks remain selectable.
4. PASS: five tests answer six claims through the box's extra crowd comparison; expected stamps and both canyon stamps work.
5. PASS: an unsupported rating asks for evidence; accepted evidence builds the student's own reason sentence.
6. PASS: Pause freezes immediately, Slow toggles, and timeline jumps preserve playback. Checks returned true.
7. PARTIAL: how lines start once and repeat events start on each action. Fast actions can interrupt browser fallback speech; bank identity is unrecorded.
8. PASS: complete progress restored after reload, including six stamps and ratings; New case clears state and saved closure.

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

Opened both bar frames, the first laptop/preview frames, all five functional/drag frames, all eight full-play frames,
all twelve full-size/keyboard/grayscale/Motion/voice frames, all twelve focused frames, all nine phone/playback frames,
all nine final target frames, the corrected rating/rule frames, keyboard-lab frame, all four art sheets and the bar comparison.
Opened all 49 audit PNGs using thirteen contact sheets, then all twelve post-audit PNGs using three sheets, plus the pause-proof PNG.

#### Art made

13 finished images, 652330 bytes (637.04 KB). All are marked drawn_by: codex and people: false.
One canyon redraw and one cutout correction; the cutout's magenta edge was despilled by art.py --rekey.
Voice recordings: 0 KB, as instructed. Fifty-one fixed lines are listed for later recording.
Final bundle: 1382268 bytes (1349.87 KB), below the 2 MB goal. Art 637.04 KB; voice 0 KB.
Final bundle SHA256: 771d964927d436b628c348b1d32f2cb752b729d332b5a970ab16789f53421a29. Source is 1355 readable lines.

#### Art still to paint

None. No people art was needed. No placeholders remain.

#### Engine changes wanted

None. A future authorized rapid disclosure clip can use the existing voice map.

#### Left open

- No recorded science-narrator voice or acted rapid disclosure, because the build prohibits recording.
- Browser speech may be cut by rapid actions; line-start evidence does not prove an uninterrupted audible performance.
- The art direction calls Speed low-angle while Content assigns Speed to sped-up film and sound effects. The explicit mapping was retained.
- Minor toy molding differences across generated frames should be judged in the cold review.
- The final bundle has targeted post-audit checks, not a second full audit. The automatic mode-discovery gap is documented above.
- Process closure and temporary host removal are recorded in Scratch/process-closure.json.

Build-only boundary: no git commits, no shared-file changes and no polish round. All build Chrome/server processes are closed; host.html removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: toy-ad-reality-check

#### Played

Played cold as a grade 4 student through all three modes, Plain view and initial lab experiments before reading the builder's report, handoff, notes or source.
The cold completion script finished during those reads; the fully completed, held-click, voice-on path was also run afterward. The vivid ad-to-tabletop reveal is strong.
Reviewed projector and solo use, both reference tools, every STANDARDS size, full evidence extremes, Motion off, grayscale and keyboard input.

#### Findings fixed

- Blocker, general, Lab: stamp enumeration granted a correct stamp. A wrong stamp now requires repeating that experiment; dependent rating chips and rule confirmation are invalidated.
- Blocker, general, Rules: ticking everything confirmed rules without evidence. Six tested, stamped claims are now required.
- Should fix, general, trick finder: keyboard guesses could cycle freely. After an error, revisit the picture before another card; pointer guesses also clear the selected spot.
- Should fix, general, Verdict: the correct message's length stood out. The three options now have comparable lengths and retain their meanings.
- Should fix, general, voice/hints: Cards instructions and success copy named hidden controls. They now name Cards and Ratings correctly; lab result lines include the next stamp action.
- Should fix, general, Graphics: the lab had a ghost duplicate toy and a different cartoon mover. Redrew the table and use the measured racer cutout throughout.
- Should fix, general, compact layouts: populated phone ratings hid fairness; 680 reasons clipped. Both rating groups and all chips now fit; compact reasons summarize two results and name additional selections.
- Should fix, general, paired timing: stopwatch labels and tracks collided in the preview. Separated the watch, tracks and finish label.
- Should fix, general, reset: ramp/light appearance survived New case. Both reset; Open box also restores the box's claim after the crowd comparison.
- Should fix, general, audit frames: Message hid its focused control on opening Cards. Focus now transfers to the first supporting claim; verified at all eight sizes.
- Should fix, general, phone: footer and claim strip overlapped content. Reserved grid rows and scrolling leaves keep controls, strip and hint separate.
- Should fix, general, Cost/closure: compact Close controls and closed-case questions could disappear. Compact prices, feedback and stamp now fit; the total also has an explicit accessible name.
- Should fix, general, jump geometry: a 12 cm toy looked smaller than the 10 cm gap. Its drawn width now equals 1.2 times the gap, verified at 375, 680, 1366 and 1920 widths.
- Should fix, general, ruler recovery: a rejected stamp left alignment intact. The ruler and 12 cm marker now reset before a retest.
- Should fix, general, welcome: Sound toggles could revive the pre-Play welcome. Playing makes it stale across Pause and Sound changes.
- Should fix, general, factual feedback: Speed's visibly low camera was denied. Feedback now acknowledges it while following the spec's speed-claim mapping.
- Polish, general: real/ad runs replay together instead of leaving the real racer parked. The closing stamp now names the student's evidence.

#### Findings left

- Nit: slight molding differences remain across the generated commercial pictures. The green racer, flame stickers, wheels and yellow eyes remain consistent identifiers.

#### Break it

- Music on all six shots: cards fill as the spec requires, but message confirmation and closure fail without two specific technique pins.
- Card sweep after one wrong guess: fails until the picture is revisited. Keyboard recovery and normal keyboard pinning pass.
- Stamps: pre-test taps, all three options in succession, and premature ramp attempts fail. Re-observing permits a justified new stamp; both canyon marks work.
- Rules: checking all boxes before testing now fails. All four provided rules apply by design; confirmation is an evidence review, not an accuracy score.
- Ratings: sweeping 1 through 5 with no chips cannot close a case. All 25 opinion pairs with evidence are accepted; no preferred rating or best score exists.
- Cost: trailing text, exponents, negative numbers, NaN, Infinity and extra decimals fail; 65.46 passes.
- Ruler: actual drag aligns zero with the toy; a vertical/horizontal mismatch fails. Align, wrong stamp, Check, another stamp now fails until realignment. This is guided measurement, not a hidden-number quiz.
- Stopwatch: early/late stops fail; a 1.7-second observation passes. A learned rhythm can also pass because the fixed crossing is required by the spec. It awards no reaction score.
- Before the audit: independent logic matrix 126/126 assertions, including 42 trick pairs, stamps, recovery, evidence gates and opinion pairs. Final affected paths were checked separately.
- The real completed case restores on a fresh page; New case clears saved pins, tests, marks, opinions, rules, total and closure.

#### Voice walk

Play, Pause, picture, Low angle, Plain view, remaining shots, The lab, Measure it, Time it, Jump it, Lights out, Open box, stamps, The verdict, message/cards, ratings, rules, cost, Close my case.
Stopwatch input follows its 1.7-second crossing; other held clicks use 120 ms holds and a two-second gap.
Heard in order: playHow, pinHow, right-low, plainHow, right-speed, right-close, right-crowd, right-music, right-print;
welcomeLab, measureHow, alignRight, timeHow, timeRight, jumpHow, jumpFall, jumpClear, lightsHow, lightsRight, boxHow, boxRight, crowdRight, labDone;
welcomeVerdict, intentHow, intentRight, ratingHow, ruleHow, costHow, costRight, closing.
Repeated the whole path after the final changes: case closed, 31 spoken starts, all nine relevant how-to lines once, no console errors. All 55 manifest lines exactly match allLines().

| Repeat line | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| pinHow | how | 1 | 1 |
| timeHow | how | 1 | 1 |
| wrong-speed | event | 5 | 5 |

Read works with Sound off and speaks the current hint. Rapid changes drop stale lines; no delayed welcome is required after Play.
Browser speech can be cut by the next action; these logs verify starts and current-state validity, not complete recorded takes.

#### Facts checked

- Fictional 12 cm toy, 30 cm ruler, 1 m run, 1.7 seconds, 10 cm ramp jump, glowing eyes and three box items: spec Content; checked against geometry, tests and pictures.
- 1/1.7 = 0.588235 m/s; 1.7/3 = 0.566667 seconds; six shot durations sum to 15 seconds: independent review-numbers.py.
- [W3C WCAG 2.1 relative luminance](https://www.w3.org/TR/WCAG21/#dfn-relative-luminance): independently recomputed all eight ratios: 13.16, 11.61, 10.18, 8.01, 5.68, 4.98, 5.77 and 5.76 to one; these match the spec.
- $29.99 + $19.99 + $9.99 + $5.49 = $65.46; difference $35.47: exact Decimal arithmetic, using the spec's fictional prices.
- Eight racers counted in ad-crowd. Multiple toys do not prove everyone owns one: fictional case evidence; each is separately sold per the box disclosure.
- Performance presentation and reproducible demonstrations: [CARU sections 4(b)(1)-(5)](https://assets.bbbprograms.org/docs/default-source/caru/caru_advertisingguidelines.pdf).
- Understandable, conspicuous accessory/battery disclosures: CARU section 4(c), same source.
- Peer acceptance/social pressure: CARU section 4(h)(3), same source. The classroom rule is an application to this fictional implied claim, not a general ban on crowds.
- Camera angles, music and effects can make products exciting: [MediaSmarts, Adversmarts teacher material](https://textbook.mediasmarts.ca/blocks-teachertext/chapter/adversmarts/).
- Looking up from a low camera can make a subject impressive; close framing removes scale context: [MediaSmarts, Camera Frame, Angle, and Distance](https://textbook.mediasmarts.ca/navigating-teacher/chapter/2473/).
- CARU is industry self-regulation, not a claim that every example violates a statute. Current primary guidance checked during this review.
- Progress privacy: inspected wrapped localStorage and the self-contained bundle; no external runtime resources found.

#### Sensitivity

None: fictional consumer literacy, no named cultures, religion, hard history, human bodies or people images. Affording the toy is never assumed.

#### Flattest moment left

The rule book is still the most static part. It now requires the student's tested evidence; adding a new rule puzzle would exceed the spec.

#### Graphics

Inspected all 13 finished assets at their output sizes and in the tool. No people or missing art tokens. Preserved the glossy ad and tactile folder.
Redrew art/raw/lab-table.png with built-in imagegen; full house style/prompt in art/prompts.json. Processed with art.py --rekey lab-table.
The same painted lab racer replaces the weaker SVG movers. New tabletop, paired replay and personal closing evidence lift the weak lab/payoff moments.
Bundle: 1,410.0 KB (1,409,989 bytes), self-contained. Reference frames and all inspection evidence are under _scratch/toy-ad-reality-check/review-*.

#### Audit

Audit not finished: the single run hit its 40-minute limit during resize/shake stress. Its partial audit.md is retained; no second audit was run.
Inspected all 108 audit frames. Of 81 leads, 53 repeated confirmed observations were fixed: focus, phone/footer overlaps, compact Cost/closure and the total's name.
The other 28 are 26 intentional own-action welcome omissions (BASELINE 16), the modal covering the background hint, and empty corners of a rotated stamp's bounding box; visible content is intact.
All 13 explicit states ran; automatic mode discovery found no sibling-nav buttons. Manual whole-path mode coverage supplements that limitation.
Ten repeats and ten quick taps were clean in the partial audit; its final resize/shake result is unavailable.
Re-shot 30 affected final frames plus four final main-path frames. Rechecked phone controls, all-size focus, closed questions, native trick drag, stamp recovery, welcome and jump geometry; no measured overlaps or out-of-window controls remained in those checks.
Wave lessons were checked directly: current hints/Read, stable controls, focus, 44 px targets, honest unknowns/progress, evidence-backed opinions, bounded short sets, repeat input, Motion off and saved/reset state. Contrast/grayscale and keyboard paths were inspected separately.
Audited source/bundle snapshots and final SHA-256 are preserved in Scratch. All owned test browsers and host 8755 are closed. Shared files and git history were untouched.

#### Left open

- Audit resize/shake stress did not finish; targeted final screenshots and geometry checks do not replace that missing result.
- Fixed timing can be memorized, and every supplied rule is applicable. These spec choices are retained; neither is presented as a mastery score.
- Speed art specifies a low camera while Content assigns speed/effects cards. Accurate feedback preserves both facts; changing the accepted mapping needs a spec decision.
- The requested science-narrator identity and rapid acted price disclosure are unrecorded. Recording is prohibited by CODEX-BUILD; browser fallback and the visual disclosure remain.
- Unattended choices followed the explicit spec/brief. No new topics, shared engine changes or git commits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Toy Ad Reality Check handoff

#### Cold review changes, 2026-11-06

Wrong stamps require repeating the current experiment before another choice. The rejected test's rating chips and
rule confirmation are invalidated; other experiments stay intact. Rule confirmation requires six tested, stamped claims.
Keep this protection when changing the controls: free stamp enumeration previously granted correct evidence.

Lab motion now uses the same painted racer cutout as measurement. A redrawn table removes the static duplicate toy.
After a close stop, real and ad runners replay from the same instant at 1.7 and about 0.57 seconds.
The closing stamp names the student's selected evidence. New case resets ramp and light appearances as well as data.

The three intended-message choices have comparable lengths. Cards and success hints name the actual next tab.
Lab outcome lines include the stamp action, so a late queued instruction is not required for the main path.
Low-angle feedback on Speed acknowledges what is visible while retaining the Content list's speed-evidence mapping.
Current checks and remaining spec limitations are recorded in codex-review.md.

The review audit reached its 40-minute limit during resize stress; the partial report is in Scratch/review-audit/audit.md.
Its confirmed leads drove a reserved phone footer/claim strip, compact cost controls, and focus transfer when an answer opens Cards.
The jump racer now spans 12/10 of the drawn gap: deck width 84% times gap 18% gives 15.12%; racer width is 18.144%.
Wrong measurement stamps also reset the ruler. The Ad welcome remains stale after Play, including across Sound toggles.
The audited source/bundle are preserved in Scratch; final corrections receive targeted checks, not a second audit.
Final review verification closed a voice-on case with 31 spoken starts, all nine how-to lines once, and no console errors.
Thirty affected final screenshots and four main-path screenshots were inspected after the audit fixes. All eight focus sizes pass.
The current review bundle is 1,409,989 bytes; its hash and closed test-port results are in Scratch/review-final-verification.json.
The later Build verification closure below describes the original builder snapshot, not this review's partial audit.

#### Structure

src.html adapts kit/starter/src.html. Tool CSS lays out the evidence folder, TV, finder, lab and verdict.
The script defines shot/trick content, validated device storage, stable controls, playback, lab actions and verdict checks.
Curio.voice owns narration queues, Read and welcome behavior. Curio.audio supplies the context for original synthesized sounds.
No family engine is specified. No shared files were changed. The bundle is self-contained and generated by the standard bundler.
window.__tool exposes state, the voice log, action functions and content for review.

The five test stations answer six claims: Open box also has an explicit action to inspect the eight-racer claim.
Tests can be completed before the matching ad claim is pinned, but stamps require both a completed test and a pinned claim.
The stopwatch uses elapsed wall-clock time, not animation frames. A resize does not restart its clock.
Transient playback, pointer position and unfinished experiments are not restored. Validated completed work is restored.
New case resets only this tool's work and leaves the shared Motion preference alone.

#### Spec choices and contradictions

- Open questions: the spec lists none. No owner response was expected in this unattended run.
- Six trick cards plus Music means seven controls. Music is separate and pins to every shot, as explicitly required.
  Night has no visual trick. Music pins its honest claim; Plain view is identical for Night.
- Timing uses 1.7 / 3 = 0.5667 seconds. The spec's 0.6 seconds is the coarser rounding of the same example.
- Five tests answer six claims. The box's contents and separately sold disclosure supply the sixth comparison about eight racers.
- The cost check explicitly counts one racer, matching the specified $65.46. The eight-racer scene would cost more.
- CODEX-BUILD requests an early report; the user's specific instruction says to stop when it is written.
  Progress was kept in Scratch/report-progress.md and codex-report.md is the final build action.
- BUILD says not to draw art; the current user and CODEX-BUILD explicitly require image generation. All 13 images were made.
- Older docs request FLUX/Gemini; the user requests the available image tool. Built-in OpenAI image generation was used.
- Recording is prohibited by the build brief. The bank selection is science-narrator / Charon, but browser speech cannot enforce
  that identity. Fixed voice lines are provided for a future authorized recording pass. No audio recordings were made.
- CARU guidelines were revised in 2021 and took effect in 2022. The UI calls them industry guidelines, not statutes.

#### Graphics

Thirteen finished WebP images are in art, with raw PNGs under art/raw and prompts/provenance in prompts.json.
The first plain-canyon ramp looked flat; it was redrawn with a clearly inclined ramp and white table.
An extra side-view lab-racer cutout lets the precise ruler align to the toy's actual image edges.
Its first drawing included a ruler; an image-tool edit removed it, followed by the free rekey/despill pass.
All images have people:false. No people, hands or crowd figures are shown. The crowd is synthesized sound.
Code draws the timed racers, tracks, ruler, TV, folder, stamps, labels and price text.

#### Sensitivity

Consumer literacy uses fictional purchases and does not assume students can afford toys or accessories.
CARU summaries teach expectations for advertising directed to U.S. children. They are not legal advice.
There is no named culture, religion, hard history or human-body content, and no people art.

#### Engine changes wanted

None.

#### Review focus

Review the ad-to-plain comparison, the ruler's alignment affordance, compact lab visibility, and the distinction between
an evidence-backed opinion and a correct factual answer. No high score exists. See codex-report.md for measured verification
and unresolved limitations. This is Build only, with no git commit and no polish round.

#### Final build details

The verdict is split into Message, Cards, Ratings, Rules and Cost folder leaves. This keeps each short choice set in view.
The final message needs two shot-specific trick pins. Music still pins to every shot, but Music-only claims cannot close a case.
The case board is always one tap away through the header. Short landscape layouts show its six cards as a two-column sheet.
The stopwatch stops independently of the car. The car always finishes its fixed 1.7-second run, including after an early stop.
Ad pacing uses elapsed wall time. Motion off removes movement and preserves the fifteen-second timeline and race timing.
New how-to lines take priority over stale speech; heard how-to lines remain silent. Events start immediately and Read retains priority.
At a two-second tap pace, browser speech may be cut by the next action or mode. The report distinguishes line starts from complete playback.

The price disclosure flashes for one second. A separately acted rapid spoken disclosure was not made because recording was prohibited.
The synthesized soundtrack includes a rock-like bass pulse, chord, filtered roar, boom and cheering noise, with visible sound captions.
The painted ad-speed direction calls for a low camera while the Content mapping names Sped-up film and Sound effects.
The mapping follows the explicit Content list; a reviewer should check this art-versus-card ambiguity before release.

The old bounded host outlived its Python launcher after a denied PID-based shutdown. Its actual process was identified by its exact
argument list and verified workspace, then terminated. The replacement host has a tool-specific shutdown route and its own deadline.


#### Build verification closure

The single full audit completed with 34 leads. Seven were fixed and 27 reflect intentional modal or multi-mode first-tap behavior.
The audit's header-only mode selector missed the sibling mode nav; its five explicit states still ran at all eight sizes.
Four explicit Verdict routes were added for future review. Manual full-path, keyboard, matrix and separate mode checks supplement it.
See the report for every lead, all frame inspection and the distinction between the audited snapshot and targeted final checks.
Targeted fixes cover phone tags/title spacing, singular progress, stable Sound width and repeated active-mode welcome preservation.
Saved Verdict instructions now point to Cards/Ratings, Pause preserves its camera position, and scene alt descriptions are complete.
The final bundle is 1,382,268 bytes. Thirteen images total 637.04 KB; recorded voice is 0 KB; 51 fixed lines are supplied.
The assigned build Chrome/server processes are closed and temporary host.html is removed. No polish round or git commit was made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
