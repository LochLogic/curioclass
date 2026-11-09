# Codex report: vibration-station

## Built
- Build only, Grade 1 science, teacher driver, Bench / Find out / Reach Sam. No commits or polish round.
- One offline bundle, kit Sound / Motion / Read / voice queue, browser-synthesized apparatus sounds, optional local microphone level.
- Five prediction-and-test investigations, evidence book, cup-phone assembly, three independent random repairs, six-cell chart, secret test, designed drum code and an earned recap.
- `src.html` is readable, 3,869 lines. Every generated people asset has `people: true`.

## Numbers check
- `_scratch/vibration-station/setup.py` and `numbers.json`: all eleven listed contrast ratios match to two decimals.
- White/brand 6.94; brand/paper 6.45; ink/paper 14.25; muted/paper 6.55; ink/gold 8.40; ink/bench 8.23.
- Arcs/paper 5.41; white/arcs 5.82; ink/sky 11.86; cross/paper 5.53; arcs/bench 3.12.
- Whisper model: 8.416 dB at 12 m, -5.563 dB at 60 m. Drum model: 54.437 to 59.437 dB at 60 m. No decibel values are shown to children.
- 4 cubed = 64 codes; 4 times 3 times 2 = 24 distinct codes. All 24 accepted and all 40 repeated codes blocked through the real UI handlers.
- Random send count 1 to 6: 1/6 chance. First repair pick: 1/4. Independent fault draws with replacement leave the third kind at 1/3.
- Q2 rings 4 seconds. A 4.15-second wait rejects Hold still; a ringing hold succeeds. Story lengths conflict: 15 m string versus explicit 12 m tight-yard stop. Followed the explicit stop, documented in handoff.

## Facts checked
- Vibrating material makes sound; plucked bands shake: [NGSS 1-PS4](https://www.nextgenscience.org/dci-arrangement/1-ps4-waves-and-their-applications-technologies-information-transfer) and [Exploratorium Ear Guitar](https://annex.exploratorium.edu/science-explorer/ear_guitar.html), checked 2026-11-07.
- Holding a vibrating string still weakens or stops its signal; a loose string loses the signal; cups and a taut string carry vibration: Exploratorium Ear Guitar, verified against its explanation. The complete stop is the model's deliberate boundary.
- Sound vibrates wrap and makes loose particles move; a pan can act without touching the bowl; louder sound makes more movement: [Manchester Dancing Sprinkles](https://www.mub.eps.manchester.ac.uk/fbt-show/wp-content/uploads/sites/89/2022/02/Dancing_Sprinkles_Experiment_Guide_Portrait.pdf), checked 2026-11-07.
- The stronger mallet produces larger model jumps. Rice and sand are loose tracers; the sticker remains attached. The touching-pan trial cannot isolate transmission through the air. These are the model's investigation designs, using the Manchester separation condition.
- Hum and voice involve vibrating vocal folds: [NIDCD Taking Care of Your Voice](https://www.nidcd.nih.gov/health/taking-care-your-voice), checked 2026-11-07.
- The thicker model band gives a lower sound under comparable length and tension: [Science Buddies Rubber Band Guitar](https://www.sciencebuddies.org/teacher-resources/lesson-plans/sound-wave-frequency-amplitude), cross-checked with its authored Scientific American activity.
- Sound weakens with distance: OpenStax College Physics 17.3, named in the spec; attenuation recomputed above. Yard/park hearing outcomes, distances and string length are story assumptions, explicitly distinguished in notes.
- Cup phones and drum patterns as communication devices: NGSS 1-PS4-4 clarification. Codes, Sam, Ben, the secret and messages are fictional content from this spec.
- No student decibels, vibration rates, measured wave sizes, cultural traditions or medical claims were added.

## Break it
- 14/14 Find out assertions and 28/28 Reach Sam assertions passed in the browser; final functional run had zero console errors.
- No prediction: hidden station taps fill nothing. Prediction locks before testing; later changes cannot overwrite the saved guess. Guess correctness earns no score.
- Early Hold still, expired Hold still and doing nothing cannot fill Q2. A new pluck plus ringing hold fills it.
- Sticker sounds but leaves Q3 empty, records the attempt and returns to loose-material plans. Sand and rice both work.
- Tiny Hum tap fails; a continuous hold over one second succeeds. Microphone input is ignored outside the eligible test.
- Touching Bang records “we couldn't tell” and fills nothing. Move the pan plus Bang succeeds with a visible gap.
- Talk without parts, without the knot or with a droopy string fails. Thirty Step back taps clamp at the explicit 12-step stop.
- Talk louder never fixes. Wrong targets reveal the stopped shake. A later correct fix never upgrades an initially missed record. Each of sag, pinch and knot was also forced as an independent fixture and tested successfully.
- Chart starts unknown and fills only from six tests. Drum exposes the secret; whisper fails; cup phone works. The first pick remains recorded.
- Exhaustively tried all 64 code assignments: 24 usable, 40 blocked. Counts freeze at first send. Another message's count performs that action without advancing; six-beat mashing shrugs without advancing.
- Always sending one beat advanced at most one message in a five-send run. Three distinct correct messages completed the recap. Five wrong three-beat sends each produced a separate spoken result.
- Real timing-jittered band drag reached pull step 3. Permission-denial fixture left Mic off and named Hold Hum as the fallback.
- Synthetic Web Audio through a real MediaStream: RMS 0.0098 and 0.0394 did not complete Q4; sustained 0.1057 did. Mic stayed available on the result and released on Next. A late permission response after leaving the mode stopped its track without creating an input node. Removed double scaling of RMS.
- Fixed visible-band hit routing: tapping the painted fat wire now selects band 2; actual jittered pull still works. Real Sam-image drag reached distance 12 and Talk succeeded. Sam/Ben portrait taps repaired their respective forced faults.
- Restoring a repaired pinch scene restores its actual hint. Place changes reset the untested signal and pose. Moving the pan immediately establishes the visible gap before Bang; holding it still places the hand on the painted pan.
- Fixed an undefined image lookup during initial code assignment; rechecked the full functional path with zero console errors.

## Voice walk
- Authored bank: curious-librarian / Aoede. No recordings made, following Build instructions. Browser narration is used; recorded voice size is 0 KB.
- Real held clicks, 120 ms, at two-second intervals. Bench heard: bandSeen, bandStill, pitch, drumHow, benchNext, drumBig, humHow, panHow. Five plucks heard bandSeen once.
- Bench initially lost teaching lines when benchNext replaced them. Fixed by carrying unheard queued teaching lines into the new sequence. Final Bench queue emptied and all eight teaching lines were heard.
- Find out heard the first question, chosen predictions, each scientific result, match/surprise, both claims and toSam. At rapid pace, later questions and obsolete test instructions dropped once their controls or state no longer fitted. Final queue emptied; zero console errors.
- Reach Sam held-click main walk completed assembly, repairs, chart, secret and code. The initial run still had 15 queued lines after 45 seconds of draining. The final separate drum walk heard all five wrong-send results; its queue emptied with zero console errors.
- Side walk: simulated Mic denial, held Hum, early hold, sticker then sand. Mic-off fallback, test results and sticker explanation were heard. Two result lines remained at the initial drain deadline.
- LIMITATION: the strict two-second full-path narration requirement is not fully met. The child can act before a long browser question finishes; some later how-to lines become stale and are dropped. Read always speaks the current actionable hint. This needs cold review; no claim that every required line was heard on the rapid main path.

## Feel check
- Best moment: the wrong count makes Sam perform the wrong message, then the class repairs its own count and sends the intended message. The final card shows this class's code and honest first attempts.
- Flattest early moment: disconnected floating bands and loose-particle overlays. Fixed bands across the actual hole and anchored rice/wrap to each image's painted bounds, including portrait layouts.
- Flattest early moment: the same generic evidence picture and weak reaction for a failed message. Added apparatus-specific prediction/book pictures and redrew Sam's puzzled expression. Selected code tiles now have strong filled contrast.
- Played both complete main paths, the failed plans, secret outcomes and wrong drum outcomes. The core actions feel immediate; narration at rapid pace remains the least finished part.
- Compared `_scratch/vibration-station/bar-comparison.png`: Snowy Mail Route beside this tool. Opened Beat Lab too. This build has equally deliberate scene/world controls and substantially richer painted objects; it does not look plainer than the bar.

## Done when
1. PASS for checked layout and fold behavior, subject to final audit dispositions below. All eight base sizes checked, including 375 inside the 8795 host. Compact controls use the spec's 44 px exception; laptop controls use 60 px.
2. PASS: all four sources have distinct sounds and visible arcs; stop updates visual state immediately and cuts audio in 60 ms; frequencies and mallet ratio follow the spec. Simulated Mic refusal falls back. Live classroom microphone hardware was not available for testing.
3. PASS: locked predictions, Q1/Q3 real test gates, Q2 early/late rejection and sticker non-completion, 14 browser assertions.
4. PASS in held Hum and synthetic MediaStream tests, including thresholds, one-second gate, release, Mic lifecycle and separated-pan evidence. Actual microphone hardware input remains untested.
5. PASS: five pages sorted under the two claims with distinct We thought / We saw pictures and trial notes.
6. PASS: both cup choices, sequential parts, knot/slack failures, tight success and movement clamp tested. Real band and Sam-image drags passed; distance clamps at 12 and Talk succeeds.
7. PASS: all people and both knots remain in the repair scene, replacement draws observed, all three fault fixtures passed, louder fails, first attempts remain honest.
8. PASS: six chart outcomes, all secret outcomes, all 64 mappings, wrong/missing/right count outcomes and earned completion tested. Send prompt names the message, never its beat count.
9. FAIL against the strict complete narration requirement: actions remain immediate while speech plays and results queue before later questions. Rapid narration can lag or drop stale questions. See Voice walk.
10. FAIL for independently verified audio-only completion: choices have pictures and words; question choices and next actions are authored for narration; Sound-off arcs and ear/cross pictures work. A fully audio-only pre-reader completion was not independently validated.
11. PASS for the two explicit repetition tests: bandSeen once after five plucks; five wrong sends each spoken. Obsolete queued action lines use visibility/state checks. Remaining fast-path narration caveat is above.
12. PASS for Motion-off frame, stationary evidence, unchanged timers and offline bundle inspection; audit disposition below covers its additional motion/resize checks.

## Wave lessons
- Hint and voice: FAIL against the strict two-second complete narration rule. Hint changes immediately, Read reads it, first action is immediate, Bench unheard lines are preserved. Strict rapid narration remains open.
- Focus/layout: PASS in the full keyboard investigation run. Next focuses the new prediction; the pencil/parts sequence moves focus to the next live part. No load focus. Historical prediction cards remain visibly locked.
- Sizes and short choices: PASS in the inspected base frames. Fixed phone header clipping, tall-narrow station labels and compact build tray. The audit applies the explicit compact 44 px allowance.
- No giveaways: PASS. Predictions unscored and shuffled; blank chart cells stay unknown; repair fault is visual rather than named by badges; code reading is the required skill. First attempts cannot be improved by elimination.
- Honest numbers: PASS. No scientific meters or unexplained numeric scores. Symbol counts are actual tapped counts; story distance assumptions are in notes.
- Standards: PASS. Both listed standards have complete student actions, evidence and communication designs. No family engine is named or rewritten.
- Motion off: PASS in manual frames, no infinite idle animation while off; timers remain unchanged.
- Short choices: PASS. Prediction, material and code choices stay visible without a scrolling choice panel; final compact material cards and all twelve code tiles fit.
- Resize mid-animation: PASS. Audit resized every state and walk action to portrait and back, without exceptions or stranded controls.
- Welcome delay: PASS for the allowed first-action cancellation policy. No welcomeAfter; the next actionable hint is immediate. Strict instructional speech completeness still fails above.
- Unknown as unknown: PASS. Six chart cells begin unknown; switching place resets pose/signal instead of showing an untested success.
- One look, one meaning: PASS. Teal arcs mark sound, ear/cross marks hearing, berry marks selected choices, gold marks the next action.
- Truthful badges: PASS. Filled pages require observations, first repair records remain permanent, recap uses actual class choices.
- Hint restoration: PASS. Returning to a repaired pinch scene names Ben's released string rather than another fault; mode and step hints match current state.
- No word-copy diagnosis: PASS. Broken apparatus shows the stopped vibration; the hint asks where it stops without naming the faulty target.

## Audit leads
- Audit ran once and finished normally in 39.7 minutes, within its 40-minute limit. Original 36-lead report and all 80 PNGs remain in Scratch. Eight base sizes, Motion off and resize checks were clean; no console errors. Full audit was not repeated after fixes; affected states received focused rechecks.
- Locked prediction, four disabled-card name leads: retained and reported as a voice failure. A whole question can still be speaking after prediction locks; the hint already names the live test. Do not read these as fixed.
- Build-knot and phone-tight, four cup-name leads: first cup selection now hushes the assembly welcome. This removes that obsolete welcome, but the general rapid narration limitation remains; no claim of a clean voice re-audit.
- Drum-plan, three missing material keep regions: fixed its shared mutable fixture, which had advanced to claims. The corrected fixture shows all three 60x80 cards at 680x425. Its one focus lead and the claims focus lead share Q5 completion: now focus moves to Next, confirmed with a real held Bang.
- Chart-full, one clipped Next lead: fixed compact hint/chart layout. At 680x425, hint is 187x36, chart 187x134, Next 187x44; all fit. All regions also fit the 375-wide host.
- Code-ready, two label overlap leads: hide the redundant world label during code. Confirmed at 680 and 375.
- Earned-recap, one focus and one overlap lead: focus the live Bench control; hide code/label underlay. Confirmed at desktop and 375, including actual Next click.
- Twelve first-tap welcome leads: #m-find, all three bands, all three empty Hold still controls, Finger tap, Mallet, Hum, Bang and Mic. Retained under BASELINE's allowed first-action welcome cancellation; each meaningful action gets its own immediate line. The three empty holds deliberately do nothing, as the spec directs. Premise remains in the scene/hint/Read; rapid narration is separately open.
- Three nothing-changed leads: empty Hold still for band, drum and pan. Retained as explicit spec behavior; not false evidence or a completed check.
- Three quick-mode cuts: Bench and Sam welcomes may cancel on mode re-entry; Find out restarts its current question. The incomplete rapid question is included in the voice failure.
- These groups account for all 36 leads: 18 state, 12 welcome, three empty holds and three quick-mode cuts. The audit's ten-control five-click subset was clean; separate complete drum-send and band repetition tests are reported above.

## Frames looked at
- Both bar frames; all four initial frames; both initial and final functional end frames.
- Every base layout/mode PNG in layout-frames: all seven direct sizes, Motion off, grayscale and keyboard frame. All three phone frames were inspected and rechecked after fixes.
- Bench, each repair, chart, code, end, side and full keyboard path frames. All last-frames PNGs, both final art sheets and bar comparison.
- All 80 audit PNGs via four contact sheets, with the compact chart lead also viewed full size. All 12 final focused and three final phone PNGs, plus all ten preserved pre-fix focused PNGs, were inspected via contact sheets. Before/after artifacts and measured bounds remain in Scratch.

## Art made
- 35 generated images, including 15 marked people assets. Final art: 1118.3 KB. Final offline bundle: 1613.6 KB. Recorded voice: 0 KB. Below the 2048 KB goal.
- All assets processed only with free `art.py --rekey <name>`; no paid art script generation or downloaded art.
- Redrew the incorrect sticker as a star and changed the puzzled face. Retried initial cheering generation. A cheering continuity edit failed; its existing usable art remains, with backpack/sock differences documented.
- Fresh people review passed respectful representation and natural hands; recheck approved the puzzled face and despill. Final contact sheets are in Scratch for owner review.

## Art still to paint
None. All specified assets are generated and used. The cheering outfit continuity difference remains a small art limitation.

## Engine changes wanted
None. Voice workarounds stay tool-local; shared kit files were not edited.

## Left open
- Strict rapid full-path narration and independent audio-only child validation, as above. Browser voice is not the authored Aoede recording.
- Real microphone hardware input and direct acoustic listening were not validated. Synthetic MediaStream input and actual Sam-image drag passed. All automated Chrome runs were muted as required.
- Minor cheering-pose costume continuity. No open questions were listed in the spec; decisions and contradictions are in handoff.md.
- Required bar-tool bundling inadvertently regenerated the two ignored reference HTML bundles outside the requested write boundary. No shared source was edited, and no commits were made.
- The temporary 8795 host file was removed; all assigned ports were closed at the final check. No full audit rerun or polish round was started. Focused fixes and their before/after evidence are preserved.
