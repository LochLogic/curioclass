# Codex review: toy-ad-reality-check

## Played

Played cold as a grade 4 student through all three modes, Plain view and initial lab experiments before reading the builder's report, handoff, notes or source.
The cold completion script finished during those reads; the fully completed, held-click, voice-on path was also run afterward. The vivid ad-to-tabletop reveal is strong.
Reviewed projector and solo use, both reference tools, every STANDARDS size, full evidence extremes, Motion off, grayscale and keyboard input.

## Findings fixed

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

## Findings left

- Nit: slight molding differences remain across the generated commercial pictures. The green racer, flame stickers, wheels and yellow eyes remain consistent identifiers.

## Break it

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

## Voice walk

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

## Facts checked

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

## Sensitivity

None: fictional consumer literacy, no named cultures, religion, hard history, human bodies or people images. Affording the toy is never assumed.

## Flattest moment left

The rule book is still the most static part. It now requires the student's tested evidence; adding a new rule puzzle would exceed the spec.

## Graphics

Inspected all 13 finished assets at their output sizes and in the tool. No people or missing art tokens. Preserved the glossy ad and tactile folder.
Redrew art/raw/lab-table.png with built-in imagegen; full house style/prompt in art/prompts.json. Processed with art.py --rekey lab-table.
The same painted lab racer replaces the weaker SVG movers. New tabletop, paired replay and personal closing evidence lift the weak lab/payoff moments.
Bundle: 1,410.0 KB (1,409,989 bytes), self-contained. Reference frames and all inspection evidence are under _scratch/toy-ad-reality-check/review-*.

## Audit

Audit not finished: the single run hit its 40-minute limit during resize/shake stress. Its partial audit.md is retained; no second audit was run.
Inspected all 108 audit frames. Of 81 leads, 53 repeated confirmed observations were fixed: focus, phone/footer overlaps, compact Cost/closure and the total's name.
The other 28 are 26 intentional own-action welcome omissions (BASELINE 16), the modal covering the background hint, and empty corners of a rotated stamp's bounding box; visible content is intact.
All 13 explicit states ran; automatic mode discovery found no sibling-nav buttons. Manual whole-path mode coverage supplements that limitation.
Ten repeats and ten quick taps were clean in the partial audit; its final resize/shake result is unavailable.
Re-shot 30 affected final frames plus four final main-path frames. Rechecked phone controls, all-size focus, closed questions, native trick drag, stamp recovery, welcome and jump geometry; no measured overlaps or out-of-window controls remained in those checks.
Wave lessons were checked directly: current hints/Read, stable controls, focus, 44 px targets, honest unknowns/progress, evidence-backed opinions, bounded short sets, repeat input, Motion off and saved/reset state. Contrast/grayscale and keyboard paths were inspected separately.
Audited source/bundle snapshots and final SHA-256 are preserved in Scratch. All owned test browsers and host 8755 are closed. Shared files and git history were untouched.

## Left open

- Audit resize/shake stress did not finish; targeted final screenshots and geometry checks do not replace that missing result.
- Fixed timing can be memorized, and every supplied rule is applicable. These spec choices are retained; neither is presented as a mastery score.
- Speed art specifies a low camera while Content assigns speed/effects cards. Accurate feedback preserves both facts; changing the accepted mapping needs a spec decision.
- The requested science-narrator identity and rapid acted price disclosure are unrecorded. Recording is prohibited by CODEX-BUILD; browser fallback and the visual disclosure remain.
- Unattended choices followed the explicit spec/brief. No new topics, shared engine changes or git commits.
