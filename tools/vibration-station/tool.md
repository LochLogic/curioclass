# Vibration Station: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: vibration-station

#### Built
- Build only, Grade 1 science, teacher driver, Bench / Find out / Reach Sam. No commits or polish round.
- One offline bundle, kit Sound / Motion / Read / voice queue, browser-synthesized apparatus sounds, optional local microphone level.
- Five prediction-and-test investigations, evidence book, cup-phone assembly, three independent random repairs, six-cell chart, secret test, designed drum code and an earned recap.
- `src.html` is readable, 3,869 lines. Every generated people asset has `people: true`.

#### Numbers check
- `_scratch/vibration-station/setup.py` and `numbers.json`: all eleven listed contrast ratios match to two decimals.
- White/brand 6.94; brand/paper 6.45; ink/paper 14.25; muted/paper 6.55; ink/gold 8.40; ink/bench 8.23.
- Arcs/paper 5.41; white/arcs 5.82; ink/sky 11.86; cross/paper 5.53; arcs/bench 3.12.
- Whisper model: 8.416 dB at 12 m, -5.563 dB at 60 m. Drum model: 54.437 to 59.437 dB at 60 m. No decibel values are shown to children.
- 4 cubed = 64 codes; 4 times 3 times 2 = 24 distinct codes. All 24 accepted and all 40 repeated codes blocked through the real UI handlers.
- Random send count 1 to 6: 1/6 chance. First repair pick: 1/4. Independent fault draws with replacement leave the third kind at 1/3.
- Q2 rings 4 seconds. A 4.15-second wait rejects Hold still; a ringing hold succeeds. Story lengths conflict: 15 m string versus explicit 12 m tight-yard stop. Followed the explicit stop, documented in handoff.

#### Facts checked
- Vibrating material makes sound; plucked bands shake: [NGSS 1-PS4](https://www.nextgenscience.org/dci-arrangement/1-ps4-waves-and-their-applications-technologies-information-transfer) and [Exploratorium Ear Guitar](https://annex.exploratorium.edu/science-explorer/ear_guitar.html), checked 2026-11-07.
- Holding a vibrating string still weakens or stops its signal; a loose string loses the signal; cups and a taut string carry vibration: Exploratorium Ear Guitar, verified against its explanation. The complete stop is the model's deliberate boundary.
- Sound vibrates wrap and makes loose particles move; a pan can act without touching the bowl; louder sound makes more movement: [Manchester Dancing Sprinkles](https://www.mub.eps.manchester.ac.uk/fbt-show/wp-content/uploads/sites/89/2022/02/Dancing_Sprinkles_Experiment_Guide_Portrait.pdf), checked 2026-11-07.
- The stronger mallet produces larger model jumps. Rice and sand are loose tracers; the sticker remains attached. The touching-pan trial cannot isolate transmission through the air. These are the model's investigation designs, using the Manchester separation condition.
- Hum and voice involve vibrating vocal folds: [NIDCD Taking Care of Your Voice](https://www.nidcd.nih.gov/health/taking-care-your-voice), checked 2026-11-07.
- The thicker model band gives a lower sound under comparable length and tension: [Science Buddies Rubber Band Guitar](https://www.sciencebuddies.org/teacher-resources/lesson-plans/sound-wave-frequency-amplitude), cross-checked with its authored Scientific American activity.
- Sound weakens with distance: OpenStax College Physics 17.3, named in the spec; attenuation recomputed above. Yard/park hearing outcomes, distances and string length are story assumptions, explicitly distinguished in notes.
- Cup phones and drum patterns as communication devices: NGSS 1-PS4-4 clarification. Codes, Sam, Ben, the secret and messages are fictional content from this spec.
- No student decibels, vibration rates, measured wave sizes, cultural traditions or medical claims were added.

#### Break it
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

#### Voice walk
- Authored bank: curious-librarian / Aoede. No recordings made, following Build instructions. Browser narration is used; recorded voice size is 0 KB.
- Real held clicks, 120 ms, at two-second intervals. Bench heard: bandSeen, bandStill, pitch, drumHow, benchNext, drumBig, humHow, panHow. Five plucks heard bandSeen once.
- Bench initially lost teaching lines when benchNext replaced them. Fixed by carrying unheard queued teaching lines into the new sequence. Final Bench queue emptied and all eight teaching lines were heard.
- Find out heard the first question, chosen predictions, each scientific result, match/surprise, both claims and toSam. At rapid pace, later questions and obsolete test instructions dropped once their controls or state no longer fitted. Final queue emptied; zero console errors.
- Reach Sam held-click main walk completed assembly, repairs, chart, secret and code. The initial run still had 15 queued lines after 45 seconds of draining. The final separate drum walk heard all five wrong-send results; its queue emptied with zero console errors.
- Side walk: simulated Mic denial, held Hum, early hold, sticker then sand. Mic-off fallback, test results and sticker explanation were heard. Two result lines remained at the initial drain deadline.
- LIMITATION: the strict two-second full-path narration requirement is not fully met. The child can act before a long browser question finishes; some later how-to lines become stale and are dropped. Read always speaks the current actionable hint. This needs cold review; no claim that every required line was heard on the rapid main path.

#### Feel check
- Best moment: the wrong count makes Sam perform the wrong message, then the class repairs its own count and sends the intended message. The final card shows this class's code and honest first attempts.
- Flattest early moment: disconnected floating bands and loose-particle overlays. Fixed bands across the actual hole and anchored rice/wrap to each image's painted bounds, including portrait layouts.
- Flattest early moment: the same generic evidence picture and weak reaction for a failed message. Added apparatus-specific prediction/book pictures and redrew Sam's puzzled expression. Selected code tiles now have strong filled contrast.
- Played both complete main paths, the failed plans, secret outcomes and wrong drum outcomes. The core actions feel immediate; narration at rapid pace remains the least finished part.
- Compared `_scratch/vibration-station/bar-comparison.png`: Snowy Mail Route beside this tool. Opened Beat Lab too. This build has equally deliberate scene/world controls and substantially richer painted objects; it does not look plainer than the bar.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
- Both bar frames; all four initial frames; both initial and final functional end frames.
- Every base layout/mode PNG in layout-frames: all seven direct sizes, Motion off, grayscale and keyboard frame. All three phone frames were inspected and rechecked after fixes.
- Bench, each repair, chart, code, end, side and full keyboard path frames. All last-frames PNGs, both final art sheets and bar comparison.
- All 80 audit PNGs via four contact sheets, with the compact chart lead also viewed full size. All 12 final focused and three final phone PNGs, plus all ten preserved pre-fix focused PNGs, were inspected via contact sheets. Before/after artifacts and measured bounds remain in Scratch.

#### Art made
- 35 generated images, including 15 marked people assets. Final art: 1118.3 KB. Final offline bundle: 1613.6 KB. Recorded voice: 0 KB. Below the 2048 KB goal.
- All assets processed only with free `art.py --rekey <name>`; no paid art script generation or downloaded art.
- Redrew the incorrect sticker as a star and changed the puzzled face. Retried initial cheering generation. A cheering continuity edit failed; its existing usable art remains, with backpack/sock differences documented.
- Fresh people review passed respectful representation and natural hands; recheck approved the puzzled face and despill. Final contact sheets are in Scratch for owner review.

#### Art still to paint
None. All specified assets are generated and used. The cheering outfit continuity difference remains a small art limitation.

#### Engine changes wanted
None. Voice workarounds stay tool-local; shared kit files were not edited.

#### Left open
- Strict rapid full-path narration and independent audio-only child validation, as above. Browser voice is not the authored Aoede recording.
- Real microphone hardware input and direct acoustic listening were not validated. Synthetic MediaStream input and actual Sam-image drag passed. All automated Chrome runs were muted as required.
- Minor cheering-pose costume continuity. No open questions were listed in the spec; decisions and contradictions are in handoff.md.
- Required bar-tool bundling inadvertently regenerated the two ignored reference HTML bundles outside the requested write boundary. No shared source was edited, and no commits were made.
- The temporary 8795 host file was removed; all assigned ports were closed at the final check. No full audit rerun or polish round was started. Focused fixes and their before/after evidence are preserved.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: vibration-station
#### Played
- Grade 1 solo and projector paths: all stations, five investigations, assembly, three repairs, six tests, secret, code and end card. Cold play preceded builder notes/source.
- Best moment: a wrong drum count makes Sam do the other message. The painted bench, distinct sounds, honest first attempts and lively cast stay.
- Workspace S:\CurioClass-codex; tool/Scratch writes only, no commits. Bounded bundle/drive/audit commands; Chrome 9960-9967, host 8765.
#### Findings fixed
- **Blocker, general, Find out/book:** reopening page 1, then page 4 and finishing page 5 left a null page and crashed the summary. Reproduced in review-book-before; summary now returns to the missing investigation with the correct question/hint. Exact replay is safe, with no exception.
- **Blocker, general, voice:** main-path questions, test/plan instructions and whole explanations became stale or ran against a changed scene. Next and teaching-dependent choices acknowledge immediately, keep the relevant scene/choices present while narration finishes, then proceed. Mode switches and reopened questions cancel obsolete work.
- **Should fix, general, Reach Sam geometry:** tall 760x900 frames attached the string above Sam. Anchors now use the actual contained painting bounds; every relevant pose has a cup. Knots and curled loose ends show connection states. Checked at 680, 1366, 760 and 375 iframe widths.
- **Should fix, general, repair evidence:** the stopped-shake ring vanished before its spoken instruction finished. It now remains until the fault is repaired, also with Motion off. A 2.8-second delayed inspection passed.
- **Should fix, general, truthful badges:** a cup-at-ear pose added a heard icon before a successful Talk, and new parts could retain the old failed result. Icons now follow test outcomes, not poses; new assembly work clears stale feedback. Four ready/fail/fixed/retested assertions passed.
- **Should fix, general, prediction cue:** the question header reused a shaking outcome picture. It now uses a neutral magnifier/question mark, distinct from both choices; apparatus art and prediction cards remain intact.
- **Should fix, general, first tap:** empty Hold still controls were incorrectly declared to have their own speech, suppressing the welcome. Narrowed that selector so these first taps explain how to begin while still awarding no evidence.
- **Should fix, general, narration:** assembly/device changes queued obsolete lines, repeated wrong targets nagged, repeated mic denial repeated its fallback. Context changes use the kit's Read-preserving immediate speech; wrong targets speak once per scene, mic fallback once per cause. Critical repair/secret lines retain their scene while they finish.
- **Polish, general, recap:** tiny evidence pairs sat over a mostly empty board. Cards now use the available space, larger evidence pictures, shaded edges and the existing painted apparatus.
- **Polish, general, art:** redrew sam-cheer with OpenAI imagegen using sam-hear as costume/identity reference; removed backpack and striped socks. Preserved textured shading, pose and cheerful expression; inspected final 280 px WebP and scene. Prompt/provenance in art/prompts.json.
- **Polish, general, craft:** corrected singular "1 fix"; tapping an active mode no longer cuts/restarts its speech. Three rapid active-mode rechecks spoke each entry once without cuts.
- Updated notes, handoff and audit states, including pending-action waits, portrait coverage and the reopened-page regression. Voice texts are unchanged; all 165 runtime lines match lines.json.
#### Findings left
- Validation limitation: no final-bundle full audit. The one allowed audit started early while two cold drive attempts timed out, then its Chrome enabled play. Its later stages crossed source revisions. This is a procedure exception, not a final clean audit claim.
- Whole questions can finish after a prediction locks; their question remains displayed. Retained the spec's whole-question policy rather than cutting it when a fast child chooses. Historical answer words can trigger the audit's disabled-card matcher.
- Nit: some unchanged walking/waving/kicking poses retain small sock-stripe differences; the dominant outfit and identity remain consistent. Left as a nit after correcting the much more visible cheering backpack.
- Browser narration remains the fallback. No Aoede recordings were made under the build rule forbidding recording; live classroom microphone acoustics and audio-only child completion are unverified.
- The continuous same-tab attempt hit the driver's 60-second evaluation limit; its smaller retry reached Q5 but exceeded the harness's 15-second pending-action guard. Stopped that retry path. Completed mode-by-mode logs verify the required lines; the stricter continuous two-second held-input check remains unverified.
#### Break it
- Predictions: hidden tests and changing a guess after observing cannot fill/alter a page. Guess accuracy earns no score.
- Evidence pages: empty/Next mashing cannot skip a test. Filled-page hopping reproduced the crash above; after repair it returns to the missing page, with no fabricated evidence.
- Q2: early Hold still and a hold after 4.2 seconds fail; a new ringing pluck plus hold succeeds.
- Q3: sticker fails and remains recorded; sand/rice tests work. The sticker-to-sand voice side path heard plan, sticker explanation, test instruction and sand result.
- Q4: 120 ms Hum fails; 1.1 seconds succeeds; release stops it. Mic denial leaves Mic off and Hum usable; two identical denials speak the fallback once.
- Q5: repeated touching bangs fill nothing; moving away plus Bang fills the page and retains the touching-trial note.
- Build: missing parts/knot and droopy string fail; 30 Step back taps stop at 12 story steps; tied and tight succeeds.
- Repairs: fixing before Talk fails; louder never fixes. Trying all targets after a miss never upgrades the first attempt. Five repeated wrong targets speak that explanation once.
- Chart/secret: empty chart cannot advance; six actual tests fill six cells. Drum/whisper/phone elimination keeps the original wrong secret pick.
- Code: all 64 mappings tried through UI handlers, 24 accepted and 40 blocked. One-beat repetition advances only its one message; six-beat mashing cannot advance. Correct distinct messages finish. Five wrong sends produced five spoken results.
- No best-score, saved-score or reflection gate exists. Progress stays in this page load; the final first-attempt recap uses actual choices.
#### Voice walk
- Cold input used held CDP clicks; sequential CDP latency sometimes stretched the requested two-second gaps. Follow-up queue tests used a real held first action, timed UI handlers at two-second gaps, and 1.1-second held keyboard Hum; no speech mocks.
- Continuous same-tab verification: not fully verified; see review-proof.json and the mode-by-mode logs.
- Bench order: bandSeen, bandStill, drumHow, benchNext. The fuller cold Bench path also heard pitch, drumBig, humHow and panHow.
- Find out: q1, prediction, t1, r1/match; q2, prediction, t2, r2; q3, prediction, t3plan, t3, r3; q4, prediction, t4, r4; q5, prediction, t5plan, r5touch, moved, r5; claims, toSam. Match/surprise reflects the actual guess.
- Reach Sam: samWelcome; cup/pencil/string/knot/tight instructions; heard; three fixScene/cantHear/fix/heardFix cycles; fixDone; chartHow and six test results; secretAsk/secretCup; codeHow/codeReady; three message/result pairs; samEnd/endHow.
- Counts: bandSeen how 1/5 plucks; wrong drum result events 5/5; wrong-target explanation 1/5; same-cause micOff 1/2. Read matched the current hint with Sound off, and subsequent assembly speech waited for Read.
- Evidence: review-voice/*.json, cold-bench-play.json, review-five-*.json and review-read-and-stale.json. Logs distinguish spoken, dropped and cut entries; no claim of listening to an Aoede take.
#### Facts checked
- Sound can vibrate matter, vibrating matter makes sound; cup phones/drum patterns meet the communication examples: [NGSS 1-PS4](https://www.nextgenscience.org/dci-arrangement/1-ps4-waves-and-their-applications-technologies-information-transfer).
- Plucked strings vibrate; cups and taut freely vibrating string transmit the signal; pinching/slack weakens or stops it: [Exploratorium, Ear Guitar](https://annex.exploratorium.edu/science-explorer/ear_guitar.html).
- Sound moves stretched wrap and loose particles; stronger sounds give more movement; pan must be near without touching the bowl: [University of Manchester, Dancing Sprinkles](https://www.mub.eps.manchester.ac.uk/fbt-show/wp-content/uploads/sites/89/2022/02/Dancing_Sprinkles_Experiment_Guide_Portrait.pdf). The touching test cannot isolate sound through air; the sticker contrast is the model's investigation design.
- Vocal folds vibrate to produce voice: [NIDCD, Taking Care of Your Voice](https://www.nidcd.nih.gov/health/taking-care-your-voice).
- Band/string pitch depends on its properties; the thicker/lower comparison assumes comparable length and tension: [Science Buddies lesson](https://www.sciencebuddies.org/teacher-resources/lesson-plans/sound-wave-frequency-amplitude), [its authored guitar activity](https://www.scientificamerican.com/article/tune-up-your-rubber-band-guitar/).
- Whispering is approximately 30 dBA: [NIDCD, How is Sound Measured?](https://www.nidcd.nih.gov/health/how-sound-measured). This is not a specified one-meter calibration.
- Distance attenuation requires the spherical/free-field assumptions: [OpenStax, Sound Intensity](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity). Recomputed story-model values: whisper 8.42 dB at 12 m, -5.56 at 60 m; assumed 90-95 dB drum gives 54.44-59.44 at 60 m. Audibility also needs background/source assumptions; notes already identify story outcomes as illustrative.
- Code arithmetic independently gives 64 assignments and 24 distinct codes. All eleven spec contrasts match to rounding, including white/berry 6.94:1 and teal/wood 3.12:1. Frequencies, four-second band ring and 2.5x mallet amplitude are model settings, not measurements.
#### Sensitivity
- No cultural, Native, religious or hard-history claim. The gentle own-throat hum prompt concerns bodies without diagnosis or personal disclosure; inspect respectful hands, age-appropriate clothing and Sam/Ben continuity in the people contact sheet. All 15 people assets are marked people:true; the replacement cheer is identified for the fresh people/owner look.
#### Flattest moment left
- Assigning three code counts is deliberate setup and remains slower than the sends. Kept it: inventing a usable code is the standard's design task; Sam acting on the wrong and right messages provides the payoff.
#### Graphics
- All 35 assets present; the rich painted set, dimensional instruments and world controls remain. One cheer redraw, improved string drawing and recap. Art 1119.3 KiB; final bundle 1621.9 KiB; 0 KiB recorded speech.
- Inspected cold course frames, base sizes, native portrait/phone/compact problem frames, focused fixes, grayscale/Motion off, both bar tools and finished Sam poses. Beat Lab and Snowy Mail Route remain read-only comparisons; neither was bundled or edited.
- Updated people sheet: review-people.jpg. Side-by-side finish comparison: review-bar-comparison.jpg, both in Scratch.
#### Audit
- One audit completed within its 2,400-second limit: review-audit/audit.md, 80 frames, 31 leads. Base sizes were mechanically clean; no audit console-error lead.
- Five disabled-name leads: obsolete cup welcome was preempted; locked answer words remain historical choices under the whole-question policy. One singular-word lead fixed and checked at 375.
- Seven resize/state leads came from early fixtures advancing during the new acknowledged narration waits. Fixtures now wait for aria-busy to clear. Main-path/state/portrait checks pass, but these are not seven fresh full resize audits.
- Of twelve first-tap welcome leads, nine follow BASELINE 16 (an action may replace the welcome); the three empty Hold still cases now get the welcome. Their apparatus action remains the spec's no-op. Three active-mode cuts were fixed and all three quick-tap cases rechecked.
- Focused gates, all 64 code mappings, keyboard transition into Q2, Read/Sound, calm/grayscale and four-width geometry/recap checks passed without unexpected exceptions. The deliberate pre-fix book crash remains in evidence.
#### Left open
- Full final-bundle audit and real recorded-voice/acoustic classroom validation, as above; no second audit or polish pass was started.
- Continuous two-second main-path validation remains open after the bounded harness failures. The chosen whole-explanation policy can involve listening waits; it is not an instant-physics claim for these acknowledged transitions.
- Unattended choices: paper cup, explicit 12-step yard stop despite the spec's 15 m story-length conflict, and visible acknowledgement while whole explanations finish. No new topic or shared-kit change.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Vibration Station

#### Build scope

Build only, no git commits, no polish round. Source, metadata, art prompts, voice text, teacher notes, audit states and one offline bundle are tool-local. Build evidence and people contact sheets are in `_scratch/vibration-station/`.

#### Code map

`src.html` starts from the kit starter frame and uses kit CSS, Sound, Motion, Read and `Curio.voice`. Its own sections are responsive layout, source lines, bench synthesis, station interactions, Find out state machine, Reach Sam state machine, and science canvas drawing. Painted images are referenced once in the asset table. The string, arcs, rice, sprinkles, bands, prediction icons, chart and book are drawn in code.

`window.__tool` exposes `state`, `setMode`, `allLines`, `vlog` and `vq` for review. Student progress is in memory only. No debug shortcuts are shown in the tool. Prediction choices shuffle on question entry; repair faults are independent draws with replacement; drum messages shuffle after code creation.

#### Tricky behavior

- Q2 needs a real pluck and Hold still within the four-second ring.
- Q3 keeps sticker evidence without filling the page. Rice and sand both work.
- Q5 keeps the touching trial and requires a separated pan before a successful Bang.
- The first repair attempt is permanent in that scene's record. Subsequent fixes cannot upgrade it.
- Code counts stay editable until the first beat; duplicate counts are blocked. The pause, not a Send button, ends a message.
- Held Hum stops on release, cancellation or loss of focus. Microphone input is ignored until the hum investigation's test step.
- Speech and pictures are separate. Actions happen immediately while voice feedback queues. Read uses the current hint.

#### Spec decisions and contradictions

- No open questions were listed in the spec.
- String length is called 15 m in Content, but both build instructions and Done when demand a tight yard stop at 12 m. Followed the explicit 12-step yard stop, with the string ending at a nearby park bench. Distances are story values; no numeric distance is displayed.
- CODEX-BUILD overrides BUILD's older “Do not draw art” instruction. All 35 listed assets are drawn with the image tool. It also overrides the older Gemini-only people instruction with OpenAI image generation and `people: true`.
- CODEX-BUILD says do not record audio. The requested bank is authored, but this build uses browser speech and 0 KB recorded audio.
- Voice scope is the mode, with control-visibility and state validity on step instructions. This preserves a result before a later question instead of dropping the result on a numeric step change. Rapid two-second taps can still outrun browser narration; see the report's Voice walk limitation.
- The source list's count of “25 images plus poses” resolves to 35 named output assets when the four hands and two Ben poses are counted explicitly. The manifest lists each one.
- The audit normally demands 60 px everywhere for K-2, while this spec explicitly allows 44 px at 680x425. The compact exception is documented in audit-states.json.

#### Sensitivity

No cultural, Native, religious or hard-history content. Children and hands are people assets. The contact sheet supports the BASELINE representation review: inspect age-appropriate clothing, natural hands, consistency of Sam and Ben, and respectful representation without stereotypes. No personal prompts.

The gentle hum prompt invites children to feel their own throat vibrate. It makes no health diagnosis or personal-body inquiry. A fresh people review passed representation and natural hands; the revised puzzled face passed a recheck. Cold review redrew Sam's cheering pose with the same plain shirt and white socks, preserving its joyful full-body pose.

#### Engine changes wanted

None. All implementation changes stay tool-local.

#### Final build checks

The full audit completed once with 36 leads. The report accounts for each; remaining rapid speech failures are explicit. Focused compact/phone rechecks fixed chart clipping, code-label overlap and completion focus. Actual Sam dragging and Sam/Ben portrait repair taps were exercised. Visible band hit testing follows the painted wire positions.

Microphone validation used an oscillator through a real Web Audio MediaStream, covering the RMS thresholds, sustained test gate, visible stop control after success, release on Next and cancellation of a late permission response. This does not validate classroom microphone hardware or actual acoustic listening. Held Hum remains independent of microphone level. Returning to a repaired scene restores its actual hint; switching chart place resets the untested pose and signal.

The generated bundle is 1613.6 KB, with 1118.3 KB art and 0 KB recorded voice. Browser voice can be outrun at a two-second tap pace; audio-only pre-reader completion has not been independently validated.

#### Review next

Read codex-report.md for final test results, image sizes, source verification, audit leads and any remaining limitations. A cold review is the next phase; this session performs no polish round or publication.

#### Cold review repairs

- Next acknowledges a tap immediately with an outline and aria-busy, retains the current evidence while speech drains,
  and then advances. Mode changes cancel pending navigation. Material selection uses the same acknowledgement so the
  whole drum-plan line retains its visible choices before the test controls appear. Audit fixtures wait for this state.
- Questions remain valid through their own test; they never carry into another question. Assembly and place/device
  changes clear obsolete speech. Chart/code how-to lines use stable once-only keys. Early Talk does not repeat Sam's welcome.
- String geometry follows the actual object-fit painted bounds, including bottom alignment in tall windows.
  Sam's separate cup fills the poses without a painted cup. Knots and a loose curled end distinguish connection states.
  A missed repair keeps a stopped-shake ring visible until the fault is fixed, including with Motion off.
- The discovery recap fills its cards with larger evidence pairs and existing apparatus pictures. Singular fix wording
  is correct. sam-cheer was redrawn with OpenAI imagegen and resized with the free art.py rekey path, preserving alpha.
- Review evidence, source checks, bounded runners and focused tests are in _scratch/vibration-station/review-*.
  The review audit was launched early while cold browser launches were failing; it is not a final-bundle audit.
  No shared kit changes, commits, paid generation scripts, or recorded audio were made.

#### Review validation limits

The cold review fixed the reopened-page summary crash, stale question feedback on a book-page jump, and hearing icons
that reported success from a ready-to-listen pose. A missing page now reopens with its own hint; assembly clears an old
failed outcome; a repaired but untested phone has no heard icon. Focused browser assertions passed.

The one review audit finished within 40 minutes with 31 leads. It started early during cold-driver failures and later
crossed source revisions, so it is not a final-bundle clean audit. Pending-action waits were added to the fixtures.
Mode-by-mode voice checks heard the required instructions and whole explanations, but continuous same-tab attempts
hit the driver's evaluation cap and then the harness's pending-action wait guard at Q5. That retry path was stopped.
Do not claim strict continuous two-second held-input or independent audio-only child validation from these results.

The updated people contact sheet is _scratch/vibration-station/review-people.jpg. Some unchanged small sock-stripe
differences remain across poses. No cultural content or stereotypes were found in the cold people check; the revised
cheer remains clearly identified for the later fresh people/owner look.

Question headers use a neutral inspection icon, so a child cannot copy an outcome pictogram into a prediction.
Empty Hold still buttons are excluded from the first-tap speech-owning selector: their first tap now gets the welcome,
while their apparatus action remains the specified no-op.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
