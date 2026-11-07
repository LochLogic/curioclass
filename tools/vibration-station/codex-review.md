# Codex review: vibration-station
## Played
- Grade 1 solo and projector paths: all stations, five investigations, assembly, three repairs, six tests, secret, code and end card. Cold play preceded builder notes/source.
- Best moment: a wrong drum count makes Sam do the other message. The painted bench, distinct sounds, honest first attempts and lively cast stay.
- Workspace S:\CurioClass-codex; tool/Scratch writes only, no commits. Bounded bundle/drive/audit commands; Chrome 9960-9967, host 8765.
## Findings fixed
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
## Findings left
- Validation limitation: no final-bundle full audit. The one allowed audit started early while two cold drive attempts timed out, then its Chrome enabled play. Its later stages crossed source revisions. This is a procedure exception, not a final clean audit claim.
- Whole questions can finish after a prediction locks; their question remains displayed. Retained the spec's whole-question policy rather than cutting it when a fast child chooses. Historical answer words can trigger the audit's disabled-card matcher.
- Nit: some unchanged walking/waving/kicking poses retain small sock-stripe differences; the dominant outfit and identity remain consistent. Left as a nit after correcting the much more visible cheering backpack.
- Browser narration remains the fallback. No Aoede recordings were made under the build rule forbidding recording; live classroom microphone acoustics and audio-only child completion are unverified.
- The continuous same-tab attempt hit the driver's 60-second evaluation limit; its smaller retry reached Q5 but exceeded the harness's 15-second pending-action guard. Stopped that retry path. Completed mode-by-mode logs verify the required lines; the stricter continuous two-second held-input check remains unverified.
## Break it
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
## Voice walk
- Cold input used held CDP clicks; sequential CDP latency sometimes stretched the requested two-second gaps. Follow-up queue tests used a real held first action, timed UI handlers at two-second gaps, and 1.1-second held keyboard Hum; no speech mocks.
- Continuous same-tab verification: not fully verified; see review-proof.json and the mode-by-mode logs.
- Bench order: bandSeen, bandStill, drumHow, benchNext. The fuller cold Bench path also heard pitch, drumBig, humHow and panHow.
- Find out: q1, prediction, t1, r1/match; q2, prediction, t2, r2; q3, prediction, t3plan, t3, r3; q4, prediction, t4, r4; q5, prediction, t5plan, r5touch, moved, r5; claims, toSam. Match/surprise reflects the actual guess.
- Reach Sam: samWelcome; cup/pencil/string/knot/tight instructions; heard; three fixScene/cantHear/fix/heardFix cycles; fixDone; chartHow and six test results; secretAsk/secretCup; codeHow/codeReady; three message/result pairs; samEnd/endHow.
- Counts: bandSeen how 1/5 plucks; wrong drum result events 5/5; wrong-target explanation 1/5; same-cause micOff 1/2. Read matched the current hint with Sound off, and subsequent assembly speech waited for Read.
- Evidence: review-voice/*.json, cold-bench-play.json, review-five-*.json and review-read-and-stale.json. Logs distinguish spoken, dropped and cut entries; no claim of listening to an Aoede take.
## Facts checked
- Sound can vibrate matter, vibrating matter makes sound; cup phones/drum patterns meet the communication examples: [NGSS 1-PS4](https://www.nextgenscience.org/dci-arrangement/1-ps4-waves-and-their-applications-technologies-information-transfer).
- Plucked strings vibrate; cups and taut freely vibrating string transmit the signal; pinching/slack weakens or stops it: [Exploratorium, Ear Guitar](https://annex.exploratorium.edu/science-explorer/ear_guitar.html).
- Sound moves stretched wrap and loose particles; stronger sounds give more movement; pan must be near without touching the bowl: [University of Manchester, Dancing Sprinkles](https://www.mub.eps.manchester.ac.uk/fbt-show/wp-content/uploads/sites/89/2022/02/Dancing_Sprinkles_Experiment_Guide_Portrait.pdf). The touching test cannot isolate sound through air; the sticker contrast is the model's investigation design.
- Vocal folds vibrate to produce voice: [NIDCD, Taking Care of Your Voice](https://www.nidcd.nih.gov/health/taking-care-your-voice).
- Band/string pitch depends on its properties; the thicker/lower comparison assumes comparable length and tension: [Science Buddies lesson](https://www.sciencebuddies.org/teacher-resources/lesson-plans/sound-wave-frequency-amplitude), [its authored guitar activity](https://www.scientificamerican.com/article/tune-up-your-rubber-band-guitar/).
- Whispering is approximately 30 dBA: [NIDCD, How is Sound Measured?](https://www.nidcd.nih.gov/health/how-sound-measured). This is not a specified one-meter calibration.
- Distance attenuation requires the spherical/free-field assumptions: [OpenStax, Sound Intensity](https://openstax.org/books/university-physics-volume-1/pages/17-3-sound-intensity). Recomputed story-model values: whisper 8.42 dB at 12 m, -5.56 at 60 m; assumed 90-95 dB drum gives 54.44-59.44 at 60 m. Audibility also needs background/source assumptions; notes already identify story outcomes as illustrative.
- Code arithmetic independently gives 64 assignments and 24 distinct codes. All eleven spec contrasts match to rounding, including white/berry 6.94:1 and teal/wood 3.12:1. Frequencies, four-second band ring and 2.5x mallet amplitude are model settings, not measurements.
## Sensitivity
- No cultural, Native, religious or hard-history claim. The gentle own-throat hum prompt concerns bodies without diagnosis or personal disclosure; inspect respectful hands, age-appropriate clothing and Sam/Ben continuity in the people contact sheet. All 15 people assets are marked people:true; the replacement cheer is identified for the fresh people/owner look.
## Flattest moment left
- Assigning three code counts is deliberate setup and remains slower than the sends. Kept it: inventing a usable code is the standard's design task; Sam acting on the wrong and right messages provides the payoff.
## Graphics
- All 35 assets present; the rich painted set, dimensional instruments and world controls remain. One cheer redraw, improved string drawing and recap. Art 1119.3 KiB; final bundle 1621.9 KiB; 0 KiB recorded speech.
- Inspected cold course frames, base sizes, native portrait/phone/compact problem frames, focused fixes, grayscale/Motion off, both bar tools and finished Sam poses. Beat Lab and Snowy Mail Route remain read-only comparisons; neither was bundled or edited.
- Updated people sheet: review-people.jpg. Side-by-side finish comparison: review-bar-comparison.jpg, both in Scratch.
## Audit
- One audit completed within its 2,400-second limit: review-audit/audit.md, 80 frames, 31 leads. Base sizes were mechanically clean; no audit console-error lead.
- Five disabled-name leads: obsolete cup welcome was preempted; locked answer words remain historical choices under the whole-question policy. One singular-word lead fixed and checked at 375.
- Seven resize/state leads came from early fixtures advancing during the new acknowledged narration waits. Fixtures now wait for aria-busy to clear. Main-path/state/portrait checks pass, but these are not seven fresh full resize audits.
- Of twelve first-tap welcome leads, nine follow BASELINE 16 (an action may replace the welcome); the three empty Hold still cases now get the welcome. Their apparatus action remains the spec's no-op. Three active-mode cuts were fixed and all three quick-tap cases rechecked.
- Focused gates, all 64 code mappings, keyboard transition into Q2, Read/Sound, calm/grayscale and four-width geometry/recap checks passed without unexpected exceptions. The deliberate pre-fix book crash remains in evidence.
## Left open
- Full final-bundle audit and real recorded-voice/acoustic classroom validation, as above; no second audit or polish pass was started.
- Continuous two-second main-path validation remains open after the bounded harness failures. The chosen whole-explanation policy can involve listening waits; it is not an instant-physics claim for these acknowledged transitions.
- Unattended choices: paper cup, explicit 12-step yard stop despite the spec's 15 m story-length conflict, and visible acknowledgement while whole explanations finish. No new topic or shared-kit change.
