# Letter Lanterns: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: letter-lanterns

#### Built

Built the two-mode kindergarten village from the kit starter: 26 letters, both letter forms, five vowel pairs, 24 shops, ten twin pairs, six open/closed pairs, ten banners, checks, Teacher controls and local progress. No family engine exists or was invented.

The real-input full campaign reached 26 lit letters, 24 open shops, ten banners and an independently earned m tracing badge. Source, data, manifest, notes, art and handoff are in the tool folder. The standalone bundle is `letter-lanterns.html`. Stage is built, status beta; it remains a draft because voice production is incomplete.

No git commit, deployment, submission, outreach or polish round. The report was written last to honor the user's stop instruction.

#### Numbers check

- `numbers.py` independently confirms 26 letters, 24 three-letter CVC spellings, all five short vowels, ten twins with exactly one differing position: five first, three middle, two last.
- Event prerequisites and the three-event cap were recomputed. All shops unlock after their letters; twins follow both signs; the queue drains at lantern 25.
- All ten banners occur in both supplied Dolch pre-primer and Fry first-100 sets. The art list totals 96.
- Palette contrast: ink/panel 15.32:1; amber/panel 8.93:1; letter/glass 12.26:1; muted/panel 9.85:1; long flame 14.49:1; short flame 8.72:1; signs 12.56:1; focus/night 12.38:1. The long-flame value differs from the spec's 15.8. Actual amber-button text is 8.38:1.
- Seeded 40,000-run glow simulations per case: independent 80-percent first tries yield 40.23 percent bright after four per-letter checks and 91.06 after eight; one-third guesses yield 1.22 and 10.36 percent. Perfect answers reach bright after four; no answers never do. These are model assumptions, not classroom performance claims.
- The historical 200-run child-motor percentages cannot be reproduced exactly without their noise recipe. Current all-stroke tests separately verify careful and mildly shaky paths and the named attacks; no age-based accuracy claim is made.
- Box and fox have three-letter CVC spellings but four phonemes because x represents /ks/. They are not called three-phoneme CVC words.

#### Facts checked

- The four phonics actions match RF.K.3a-d: primary consonant sounds, vowel sounds, high-frequency words by sight, and different sounds in similarly spelled words. [Common Core kindergarten reading](https://www.thecorestandards.org/ELA-Literacy/RF/K/).
- Capital/small printing is supporting work for L.K.1a, with its module assignment left to Sentence Train. [Common Core kindergarten language](https://www.thecorestandards.org/ELA-Literacy/L/K/).
- The 26 mappings and anchors follow the supplied Moats/Reading Rockets table. C and g use their common hard sounds, x is final /ks/, and q is modeled with u. The phonics reference explicitly treats x as two sounds. [Reading Rockets phonics scope and sequence](https://www.readingrockets.org/sites/default/files/2023-10/NJTSS%20Phonics%20Scope%20and%20Sequence.pdf). The complete Moats book was not reread.
- All five short/name-sound anchor pairs and six open/closed examples were checked against the supplied word table and syllable definitions. [Reading Rockets syllable types](https://www.readingrockets.org/topics/spelling-and-word-study/articles/six-syllable-types). Direct article access returned 403; its indexed primary-source text was available.
- All ten sight words were checked against the supplied Dolch/Fry catalog with Python. Banners are modeled as whole words and have no letter-sound buttons.
- Stroke order is the spec's manuscript model, not a universal handwriting rule. Publisher formation resources were checked; exact paths were copied and sampled from the spec. [Zaner-Bloser practice models](https://media.zaner-bloser.com/handwriting/pdfs/ZB_HW_Manuscript_Practice_Package.pdf), [Learning Without Tears formation resources](https://www.lwtears.com/letter-number-formation-charts).
- Final-e instruction stays outside this tool, consistent with RF.1.3c. [Common Core grade-one reading](https://www.thecorestandards.org/ELA-Literacy/RF/1/).
- Privacy was checked in code: localStorage only for progress/settings, no microphone or page network calls. Teacher states that nothing leaves the device.

#### Break it

- Trace: tested every non-dot stroke, capital and small, guided and independent. Backward, box scribble, tap and half paths all reject; careful and seeded mild-shake paths pass. The first run exposed half-path passes on G's bar and small f, k and t strokes. The added 80-percent ordered-progress requirement closes those passes. See `trace-checks.json`.
- Ink is resampled so pointer-event density cannot decide direction. Dot taps are intentionally valid dot strokes, never whole-letter passes. One pointer owns the slate.
- Three guided misses demonstrate and advance, as required, without an independent badge. A real three-miss retest reaches stroke 2 and leaves badges empty. Show me itself awards no credit.
- An optional miss initially left a flag that exposed Next and Try again later. It now clears on step changes, and both controls additionally require the corresponding trace state. The real miss/Next/reload retest returns to Find s with both controls hidden, no failure flag and no badge.
- Glow: wrong-then-right earns no streak; five extra correct taps after completion change neither glow nor streak. Credit is latched. Pools with fewer than three distinct sounds cannot award glow. Teacher Wake all is explicitly a one-star demo.
- Fixed question order and a visible weakest-letter meter offered shortcuts. The weakest set still honors glow and earliest-lit ties, but question order is shuffled, distractors prefer that set, all question poses are asleep, and the string/badges are hidden during checks. A 20-round probe produced varied orders and no outside-pool distractors.
- Visible questions no longer print target sounds or words for copying. Read and narration keep the complete question. Explicit question replay still works after an answer.
- Wrong-choice probes covered all ten twins, five vowel glows, 24 signs, ten banners and six long/short pairs. Shared twin letters and wrong signs never pass; tapping only the tall flame never skips the two models; wrong pictures never open the target; wrong banners/word boards never finish the check.
- Picture, twin and vowel practice may eventually finish with correction, as the spec requires. Those completions do not award mastery glow. Independent writing and first-try sound finds remain separate.
- First-meeting distractor property checks cover 7,800 samples across all letters and one-letter Teacher selections. They require three distinct choices containing the target and never two of b/d/p/q together. The late-x fallback was tightened to preserve this rule. C and k never compete in a sound question; their identical primary sound requires distinct-sound choices, and restricted checks stay unscored practice.

#### Voice walk

The complete manifest has 308 distinct fixed lines, warm-teacher/Sulafat, plus 31 isolated-sound production entries with IPA, three-take requirements and unreviewed status. No audio was recorded under the Build prohibition. Runtime currently uses kit browser fallback.

Held-click main walk: untouched start logs `welcome`, then `find.m`; wrong s remains asleep and logs its sound/question; correct m enters Say; the sound tap enables Next; Next enters capital tracing. A real mid-trace reload preserves letter, case and stroke. The full campaign covers every event type.

Five wrong Finds at two-second intervals logged welcome once, wrong.s five times, and find.m after each miss. No repeated how-to nag. The side walk enters Village, uses Read, returns to Wake, and replays the current question. Read wins over queued speech; mode changes can explicitly hush it.

These are muted-Chrome start logs, not listening validation. Clean consonant stops, short vowels, long vowels, phoneme-bearing questions and the chosen bank voice remain unverified by ear. Done when 9 fails.

#### Feel check

Best moment: a completed letter lifts to the string, then the first readable map sign opens into a warm shop with its painted goods. The eventual street is a concrete record of the session.

Flattest moment 1: a small generic letter panel weakened the creature reveal. Letters now sit in each painting's actual glass, awake creatures are sized up for the single-letter scene, and sleepy/awake poses are matched edits.

Flattest moment 2: the street initially had crowded targets and looked disconnected from the unlock scenes. It now has a real four-section panorama, separated arrow lanes, sleeping window lanterns, banners above grounded fronts, and event views that move to their street quarter. Optional writing adds a distinct earned badge.

Played the full progression through real pointer input, with a separate keyboard letter and wrong-answer walks. No child classroom trial was performed. `feel-comparison.png` places the final Village beside Snowy Mail Route; Beat Lab was also opened. This is visually richer than the bar, with substantial progression; voice quality prevents a release-ready feel claim.

#### Done when

1. PASS: required size sweep plus focused scene repairs. Main controls and hints remain above the fold; stage targets dominate the active scene. Compact/phone fixtures were inspected.
2. PASS: untouched held first tap logs welcome followed by Find m; the action hint changes immediately. A direct first lantern tap counts.
3. PASS on tested paths: inputs act during speech, queued old lines drop, Read is protected, arrows reposition reading and Stop stops it. The kit owns the queue.
4. FAIL for release: all five standards-map mechanics pass their structural/wrong-answer checks, but phoneme audio cannot yet be certified.
5. PASS: sign handlers speak only letters before the right picture; wrong pictures name themselves; banners never split into sounds.
6. PASS: careful traces pass, named attacks reject across the sampled path set, and the third guided miss demonstrates and advances. Assistance does not earn a free-writing badge.
7. PASS: mixed-glow frame shows sleeping window creatures, one/two/three-star halos and open/closed shops; grayscale preserves the distinctions.
8. PASS: five two-second Finds repeat event lines while the welcome/how lines do not nag. Separate replay is deliberate.
9. FAIL: zero of the required 31 isolated sound recordings are listening-approved. Production instructions are supplied; browser fallback is not treated as proof.
10. PASS: real reset confirmation clears the save; real mid-trace reload resumes; malformed JSON and an invalid event start fresh; Teacher displays the privacy line.

#### Wave lessons

| Lesson | Result and evidence |
|---|---|
| Hint and voice | PASS for scheduling, immediate hints and Read; audio-model quality remains FAIL above. |
| Focus and layout | PASS: panel controls precede the string, deliberate focus uses preventScroll, real Next focuses the slate, rebuilt lanterns retain focus. |
| Sizes and choices | PASS: all required sizes, 375 iframe, compact event fixtures; 60-pixel controls and all choices stay visible. |
| No giveaways | PASS for tested patterns after removing printed targets, visible glow cues, fixed question order, duplicate credit and the optional-skip leak. |
| Honest numbers | PASS: one star means introduced, additional stars need first tries; oral saying is explicitly practice. |
| Standards | FAIL for solo release until the phoneme models are recorded and heard; all required activities are implemented. |
| Motion off | PASS: no infinite active animation; movement stops while demonstration/reading timing stays. |
| Short choice sets | PASS: small picture/banner/flame choice sets remain in view; phone twins stack. Long Teacher lists may scroll, with Close sticky. |
| Resize mid-animation | PASS: the audit found no exceptions or stuck disabled controls; the slate uses actual bounds and the street refits. |
| No late welcome | PASS: no welcomeAfter; explicit Wake sequence and one Village entry. First-tap cuts follow BASELINE rule 16. |
| Unknown stays unknown | PASS: closed shops have blank signs, dark windows and sleeping lanterns. |
| One look, one meaning | PASS: pose, halo and stars distinguish states; short/tall flames differ in shape and anchor. |
| Badge says what is true | PASS: demo starts at one star; assistance never earns independent-writing credit. |
| Hints change back | PASS: modes, steps, Teacher, reset/cancel and partial completion update their hints immediately. |
| No answer by copying | PASS: quiz targets remain in audio/Read, not visible clue text. |

#### Audit leads

One complete audit, within its 40-minute cap, reported 90 raw leads. Its original `audit.md` and 67 PNGs are retained. It was not rerun wholesale.

- 82 state/layout leads: scene/arrow/title bounds, wrapped string coverage and the reset overlay. Fixed by fitted shop bounds, reserved title space, compact count chips, wrap-aware layout, reset hints and explicit inertness of the covered Teacher dialog. Targeted checks using the same measurement code are clean at the affected sizes, including 375.
- Seven welcome flags: accepted under BASELINE rule 16 and the spec's tap-specific entry behavior. Teacher/direct lantern taps have their own lines; Wake-tab/Motion taps do not start the lesson; the explicit begin sequence is logged as how rather than the helper's welcome kind. The untouched start sequence was independently verified.
- One rapid Village-welcome cut: accepted because an intentional mode change hushes it. The current premise/action remains available through Read.
- Resize and Motion-off stages were clean. Held-click repetition was clean. Completed drive/behavior/quiz checks report no browser console errors, warnings or exceptions. Early iframe-context/favicon and reload-assertion failures were test-harness errors and were corrected.

#### Frames looked at

All captured PNGs were opened individually or on labeled contact pages. This includes the 67 audit frames, required-size sweep, both modes, every event type, Teacher/reset, phone twins, guided/free writing, mixed glow, grayscale, keyboard and targeted repairs. Scratch contact manifests enumerate them. Final high-resolution art and the panorama crop were also inspected.

Key evidence: `playthrough/result.json`, `behavior/checks.json`, `trace-checks.json`, `quiz-attacks.json`, `long-pair-attacks.json`, `choice-invariants.json`, `free-next-final.json`, `no-glow-cue.json`, `village-resume.json`, `measure-*.json`, `audit/audit.md`, and `feel-comparison.png`.

A final Village-check regression found that checking could replace an interrupted Wake lesson. Flow snapshots now preserve it while retaining earned glow. Focused Find and partial small-letter trace runs both completed the check and resumed at the original letter, case and stroke. The final frame was inspected.

#### Art made

96 final images from 97 generations, including one street redraw: 52 creature poses, five anchors, 24 goods, two scenes, 12 fronts and one banner. Every asset is used. People: zero. All carry drawn_by codex and the OpenAI illustration credit.

Final art: 1720.1 KB. Voice: 0 KB. Bundle: 2705.4 KB, against the 2,048 KB goal. Quality is 72; backgrounds were reduced once. Awake creatures retain 420-pixel detail for their largest use, fronts 240 and the large banner 500. The teaching art was retained rather than removed to meet the goal. Full prompts and raw originals are preserved.

#### Art still to paint

None. Phoneme audio production/listening review is still required, separately from art.

#### Engine changes wanted

None. Kit, family engines, scripts and docs source were not edited.

#### Left open

- The 31 clean isolated clips and all phoneme-bearing narration need listening review. This beta must not be presented as a validated solo phonics model yet. The named voice conflicts with the neighbor's stated voice; the explicit warm-teacher selection was retained.
- Historical child-motor pass percentages were not reproduced from an unspecified noise recipe. No classroom or child trial was performed.
- Literal off-letter event dropping is implemented. Re-enabling after a dependent event was dropped does not backfill it; that edge needs a reviewer decision. The default all-on campaign is complete.
- Scope deviation: following the reference-bundle instruction regenerated the two git-ignored bar-tool HTML bundles outside the user's write allowlist. No sibling source was edited and no outside-scope revert was attempted.
- Initial read-only inspection commands lacked hard process timeouts. Subsequent build/check commands used the bounded Scratch runner. No command hit its time cap.
- `host.html` is absent. The Chrome instances and servers started for this build are closed. No polish round or git commit was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: letter-lanterns

#### Played

Cold, as a kindergarten child and projecting teacher, before opening the builder's report, handoff, notes or source. Played every activity type, the normal path through the first long/short pair, and the demo/full-village finale. The creature reveal and lantern lift are strong; Village initially felt like small shops beneath a large wall. Evidence: `_scratch/letter-lanterns/review/`.

#### Findings fixed

- Should fix, general, compact Village: Read the street read only the visible page and then claimed the whole street. It now visits all open shops across pages, then banners. Partial turns have a different ending.
- Should fix, general, voice: older words could continue after arrows or closed-shop taps. Reading redirects now interrupt ordinary narration and invalidate the old turn. Read retains priority; mode changes, Stop and reset still hush it.
- Should fix, general, Wake voice: Say's cue was dropped at a two-second pace. A shorter action cue leads the intro. Per-stroke miss/shared-letter cues are cached when heard, not queued. Plain first taps now speak the welcome or the saved Wake question. Sound back on restores the current instruction; Hear it again in Say replays the sound.
- Should fix, general, Sign: its heading crossed model letter buttons at 680 and 1366. Moved it aside without removing it; rechecked 680, 1366 and 375.
- Should fix, general, notes: "three single-letter sounds" obscured x's two sounds in box/fox. Changed this skill to blending letter sounds into a short word.
- Polish, general, art/play: redrew the street with low masonry, distant hills and foreground cobbles; enlarged the wide Sign shop and added warm light/goods feedback. Kept all 96 paintings, the palette, creature pairs, letter glass and lantern flight.
- Should fix, general, focus: Read/Stop hid the focused control; a later step could select a disabled model button as fallback. Reading now transfers focus to its replacement, and step fallback chooses a visible, enabled control. First-sign fallback passes at 680 and 1366; its post-fix phone replay is left open below.

#### Findings left

- Blocker, general: none of the 31 required isolated recordings is available or listening-approved; 310 fixed lines still use browser fallback. Solo phonics release remains blocked. CODEX-BUILD.md says "Do not download anything or record audio"; this review did not override it or certify TTS as phoneme audio.

#### Break it

- Trace: 100 non-dot strokes, guided and independent, gave 800 careful/backward/tap/half checks with zero unexpected results. Two dot strokes are intentionally taps. Real backward A, tap M, half T, scribbled O and free half-stroke reject; a careful shaky S passes. Repeated after fixes.
- Three guided misses demonstrate and advance without an independent badge. A failed optional write followed by Next leaves no badge or stale failure gate.
- Glow: five repeat correct taps earn one credit; wrong then right earns none; two-sound pools earn none. C/k never compete. All 5,200 first-meeting choice samples had three distinct choices/sounds and respected b/d/p/q separation.
- Real held wrong-option attempts covered all 24 signs, 10 twins, 6 long/short pairs, 5 vowel activities and 10 banner checks. Shared twin letters do not advance; wrong pictures do not open shops; repeated tall-flame taps cannot skip the short model. Correction completes guided practice without mastery glow.
- Wake all is a one-star demo. All off/one on, reset cancel/confirm, malformed save and a real mid-stroke reload pass. There is no saved best score or reflection assuming an unobserved mistake. Oral saying is explicitly practice checked together.
- Reading: a real phone run visited all six shops and three banners across all three pages, with no spoken-word/highlight mismatch. Redirecting to pin and tapping a closed shop stop the old turn. Motion on/off both preserve the three-second class turn; Read also works with Sound off.

#### Voice walk

Fresh Wake button, m/s/a/t, banners, three Finds, See and say, banner find, p/map Sign, Village, Read the street, Stop. Held taps 120 ms at two seconds, real drags, and a two-second air-writing pause. Nothing spoke before the first tap. First-welcome cuts follow BASELINE 16.
Heard in order: welcome, Say, capital trace, small trace, air, optional writing, two glows, See and say, first Sign, Village. Each how-to starts once, then is silent on repeats. Side paths verify Twins/long-short narration, Sound, Read and correction feedback. Evidence: review/main-voice.json and review/quiz-checks.json.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Say / capital trace / small trace | how, each | 1 | 1 |
| Air / optional writing / two glows | how, each | 1 | 1 |
| See and say / first Sign / Village | how, each | 1 | 1 |
| Wrong s feedback | event | 5 | 5 |
| Sound m replay | event | 5 | 5 |
| Shared twin letter | once per pair | 1 | 1 |

These are muted browser start logs, not listening approval of missing clips.

#### Facts checked

- RF.K.3a-d cover consonant correspondences, five vowel contrasts, sight words and differing sounds in similar words: [Common Core kindergarten reading](https://www.thecorestandards.org/ELA-Literacy/RF/K/). Each has an activity; audio accuracy remains blocked above.
- Upper/lower printing supports L.K.1a: [Common Core kindergarten language](https://www.thecorestandards.org/ELA-Literacy/L/K/). Inspected all 52 forms and 102 strokes. The model is not the only valid handwriting order: [Learning Without Tears formation charts](https://www.lwtears.com/sites/default/files/2022-01/English_print_letterCharts.pdf).
- Printed consonant mappings, hard c/g, c/k equivalence, final x=/ks/ and quail's qu follow the supplied Moats/Reading Rockets table and [WETA articulation guidance](https://readinguniverse.org/skill-explainer/articulation-pronunciation/articulation-skill-explainer/overview-what-is-articulation). The full Moats book was not reread; this mapping check is against the supplied table. No clip pronunciation is certified.
- Short anchors ant/elephant/inchworm/octopus/umbrellabird and long anchors acorn/emu/ivy/ocean/unicorn match the supplied vowel table. The six no/not, go/got, me/met, he/hen, hi/hit and we/wet pairs match [Moats and Tolman, Six Syllable Types](https://www.readingrockets.org/topics/spelling-and-word-study/articles/six-syllable-types). Indexed primary text was available; direct access returned 403.
- All ten banner words belong to both the 40-word [ReadWriteThink Dolch pre-primer list](https://www.readwritethink.org/sites/default/files/resources/lesson_images/lesson301/dolchwordlist.pdf) and [Kingsville ISD Fry first 100](https://www.kingsvilleisd.com/apps/pages/index.jsp?pREC_ID=665709&type=u&uREC_ID=460382). Membership independently recomputed.
- Final-e stays outside this tool: [Common Core RF.1.3c](https://www.thecorestandards.org/ELA-Literacy/RF/1/). Box/fox have three printed letters but four phonemes, consistent with x=/ks/ and the RF.K.2 phoneme definition.
- Recomputed 24 unique three-letter shop spellings, all five short-vowel letters, 10 one-position twins (5 first/3 middle/2 last), all prerequisites and the three-event cap. Default events drain at lantern 25 with 24 shops, 10 twins, 6 contrasts and 10 banners.
- Per-letter glow model: perfect answers brighten after four checks; independent 80% accuracy gives 40.96% after four and 91.16% after eight; guessing gives 1.23% after four. These are model probabilities, not child-validation claims.
- WCAG relative-luminance calculations confirm ink/panel 15.32:1, brand/panel 8.93:1, muted/panel 9.85:1, letter/glass 12.26:1, sign 12.56:1 and focus/night 12.38:1. Long-flame contrast is 14.49:1, not the spec's 15.8; short flame is 8.72:1 and actual button text 8.38:1. Grayscale retains poses, stars and open/closed cues.
- Privacy checked in source: device localStorage only, no microphone or external asset requests. Teacher states device-only saving. Runtime lines equal the 310-line manifest.

#### Sensitivity

No human figures, named culture, religion or hard history; this is a fictional animal-lantern village. Later listening review should check US-English short o and long u without treating a child's dialect as an error. The tool does not grade speech.

#### Flattest moment left

Long/short remains two word boards with a comparison, as specified. It is quieter than the creature reveal and shop opening; no extra game or topic was added.

#### Graphics

All 96 images inspected on contact sheets and in scenes; all 52 glyphs checked together. No people or missing art tokens. Street redrawn with built-in imagegen, processed by free art.py --rekey, final 2400x600 at quality 72. Art 1831.6 KiB; bundle 2865.2 KiB (2,933,986 bytes). Prior painting/raw kept in review Scratch. Saved art: art/raw/street-night.png and art/street-night.webp; production prompt: art/prompts.json, street-night plus house_style.
Every required size was checked, including the 375 iframe on 8765, keyboard-only navigation/tracing, Motion off and grayscale. Sign was re-shot at affected sizes. Contact manifests enumerate inspected frames. Existing Snowy Mail Route and Beat Lab reference frames were also opened; no sibling bundle was rebuilt.

#### Audit

One full audit completed in about 26 minutes on Chrome 9961 and host 8765: `_scratch/letter-lanterns/review-audit/audit.md`. Inspected all 74 PNGs. Its 25 leads were one real Read focus fault, 17 consequences of three invalid drag recipes, and seven welcome interruptions permitted by BASELINE 16. Fixed Read focus, added explicit drag returns and corrected the phone-size labels. Valid replay also exposed the disabled fallback focus fault, now fixed. Independent writing passes all three sizes; first-sign replay passes at 680 and 1366. Resume to lowercase s passes at 1366 and phone size. Read/Stop/Enter focus passes at 680, 1366 and phone size. All ten scoped recheck frames were inspected; successful corrected routes have no layout/runtime leads. No second full audit. The focused batch and smaller first-sign retry each reached their 280-second cap before the phone sign; that replay stops here under the brief.

#### Left open

- Audio production/listening remains blocked by the no-recording brief. This is a completed code/art review, not a release PASS.
- Check limit: the post-fix phone first-sign input replay did not finish after two bounded batches. Earlier phone Sign layout re-shots were clean; post-fix focus on that full phone route is unverified.
- The spec's historical child-motor percentages lack a reproducible noise recipe. They were not repeated as validated child results; defined attacks were independently checked.
- Kept literal off-letter event dropping; late re-enabling does not backfill dropped events. The named warm-teacher voice wins over the contradictory neighbor-variety sentence.
- No questions in this unattended run, no commits, and direct writes stayed in the two allowed folders. One initial read-only rules command lacked an explicit process deadline; subsequent commands used bounded jobs. Existing scripts' bytecode caches predate this session. Owned Chrome ports and host 8765 are closed; no tool-folder host.html remains.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 3 (general 2, family 1), should fix 15 (general 10, family 5), polish accepted 10
Traced to spec: blockers 1, should fix 7

### Refine: letter-lanterns

Lens files: refine/teaching.md, refine/play.md, refine/craft.md. Frames: teaching `S:/CurioClass-codex-scratch/letter-lanterns/teaching/out/`,
play `S:/CurioClass-codex-scratch/letter-lanterns/play/`, craft `S:/CurioClass-codex-scratch/letter-lanterns/craft/out/`, shared audit
`S:/CurioClass-codex-scratch/letter-lanterns/audit-r1/`. Integrator spot-checked: lesson.json find.t / intro.a / short.a /
twinDiff.0 text (blocker 1), `glyph()` at src.html:679-692 (blocker 2), `makeChoices` at src.html:717-718 (blocker 3).
(spec) = the cause is in spec.md; (build) = the spec was right and the build missed it.

#### Blocker
1. **Sounds inside sentences are bare letters, so the voice says letter names, not sounds.** lesson.json `lines`
   find.* (26), wrong.* (26), intro.* (26), short.* (5), twinDiff.* (10). Integrator read: find.t "Which lantern says t?
   Tap it.", intro.a "A. A says a, like ant.", short.a "Short glow: a, like ant.", twinDiff.0 "a. i. Pan. Pin." A lone
   "t" or "a" is read "tee", "ay" by any voice; only m s n f r l v z are spelled as sayable sounds. Effect: 18 of 26 Find
   questions ask for the letter name, intro.a teaches long a as the short sound, and short.a and long.a sound alike, so
   RF.K.3a and b are not heard (teaching out/01, 02, 04, 06 voice logs). Fixed: every line that carries a letter sound
   plays the recorded isolated clip in sequence (for example "Which lantern says" + `sound.t` + "Tap it."; intro
   "T." + "T says" + `sound.t` + "like turtle."; twinDiff `sound.a`, `sound.i`, then the words). Long-vowel lines keep
   the letter name (the long sound is the name). Play the recorded `longSound.<v>` where the long sound is meant (it is
   recorded but never referenced in src.html). The shown hint text may stay as written; only the voice changes. Update
   voice/lines.json so every sentence piece is recorded once and Done when 9 covers every place a sound is heard.
   (general) (spec: the Content intro lines and the Voice table write the sounds as bare letters)
2. **Shop signs and long/short boards draw each letter scaled to its own box: no shared baseline, lowercase reads as
   capitals.** src.html:679-692 `glyph()` (viewBox cropped to each letter's own bounds; integrator confirmed), used at
   :1510 (signs) and :1601 (boards). "cot" reads "COt", the descenders of p and g ride up level ("pup", "pig", "dog"),
   the o in "dog" sits high. These are the words the child decodes, in a tool that teaches letter forms. Seen:
   craft out/Z-signs-village2.png, out/L-sign-680x425.png, out/L-twins-1366x768.png, out/H-twins-375x812.png. Fixed:
   lay each word out in one slate box (top line 0, midline .5, baseline 1, descender 1.5) with fixed advance widths,
   as the trace slate already does; use it for signs, twins, boards and banners (should fix 9). (general) (build)
3. **Lantern check Finds use only the round's other targets as distractors, so the third Find is free by elimination
   and glow rises without knowing.** src.html:717-718 (`makeChoices(target, true)` pool = `state.checkTargets`;
   integrator confirmed). Seen: teaching out/40-check-trio (10 lit): the three Finds offered {a,m,s}, {a,s,m}, {s,m,a}.
   glow.py: a class that knows none of the three but remembers what was asked raises about 2.4 letters to two stars in
   4 checks, against 0.8 for blind guessing. Glow is the tool's outcome picture, so this misleads. Fixed: draw the two
   distractors at random from all lit, enabled letters other than the target, as the spec says; fall back to the
   round's targets only when fewer than two other letters are lit; shuffle positions. (family:letter-pals) (build)

#### Should fix
4. **The vowel flame question always has the same answer: the tall flame on the right.** src.html:1580-1585 (short
   always left, long always right) and 837-858 (only findLong is asked). Seen: teaching out/03-flames-a.png, out/04
   log. Fixed: ask for the short or the long sound at random per vowel (short plays the `sound.<v>` clip, long the
   name), and swap the flame sides at random; the flames keep their shapes (small round, tall). (family:letter-pals)
   (spec: "Which flame says ā?" names only the long sound and fixes nothing about position)
5. **The long/short word pick always asks for the short word, which is always the longer board.** src.html:1214-1215
   (`good = word === pair[1]`), lesson.json lsWhich.0-5. Cheap pass: tap the longer word. Seen: teaching
   out/05-long-0.png. Fixed: ask either word of the pair at random ("Which word says no?" / "Which word says not?") and
   shuffle board sides; record lsWhich for both words. (family:letter-pals) (spec: "Asked: the second word")
6. **Twins: open shop windows give the answer away.** Wake, Twins (for example pan/pin after lantern 7): the window
   shows a frying pan under "pan" and a pincushion under "pin", so "Which sign says pin?" is answered from pictures,
   not from the letter that differs (RF.K.3d). Seen: play f2/e03-twin-diff.png. Fixed: in the Twins step both shops
   show closed windows (goods hidden) until the sign pick is right, then the picked shop lights. (family:letter-pals)
   (spec: "Two open shops side by side")
7. **Say step speaks the instruction before the model, and the model answers it at once.** src.html:817
   (`speak([['say',{kind:'how'}],'intro.'+letter])`). Heard: "Say its sound. Tap the lantern to check." then at once
   "Mmm. M says mmm, like moth." (teaching out/02 log 8.7 s then 12.1 s; play f1/p04-right-m.png; craft v1 log). Fixed:
   intro on the right Find first, then the spec's full turn line ("Your turn. Say its sound out loud. Then tap the
   lantern to check."), and the model again only on the tap. Same order in a check's See and say. (family:letter-pals)
   (build)
8. **After the Say tap the next action is never spoken.** answerLetter, the say/seeSay branch (`hint('next');
   speak('sound.'+letter)`): the child hears "mmm" then silence beside a gold Next they cannot read; "Tap Next." only
   appears as a dropped placeholder in the log. Seen: play f1/p05-say-tap.png (log `[["spoken","mmm"]]`), f2/c02.
   Fixed: a how line "Tap Next." after the sound the first time (then hint only), the way other done moments end.
   (general) (spec: the Voice table has no line naming Next after Say)
9. **Banner words use a system font: double-story a where the fallback lands, and capital I is a bare bar like l.**
   src.html:198-199 (`'Century Gothic','Trebuchet MS',sans-serif`). Chromebooks and stock Macs have neither font.
   Seen: teaching out/24-bannerfind-fallback.png, play zoom-banner.png and f2/f02-banner-find.png ("I my the").
   Fixed: draw banner words with the shared word layout from blocker 2 (capital I with its bars, single-story a and g).
   (general) (build: the spec's Look sets ball-and-stick, single-story a and g)
10. **Sign and Twins say "lantern" over plain letter tiles.** src.html:1514-1515 vs lines `sign`, `twinIntro`: "Tap
    each lantern to hear it", "Tap the different lantern", but the sign shows cream tiles. Seen: craft
    out/L-sign-680x425.png, out/L-twins-1366x768.png; play f2/d01-sign-map.png, f2/e01-twins.png. Fixed: hang the small
    awake lantern art (already loaded) over each letter, as the spec says, so the lines are true. (general) (build)
11. **Glow levels cannot be told apart at a glance on the string.** `.string .stars { font-size:10px }`, halo via
    `::before` opacity; creatures differ in drawn size, so size reads as glow more than glow does. Done when 7 holds only
    up close. Seen: teaching out/10-string-zoom.png, play zoom-string.png, f3/v04, f3/v09. Fixed: one shared lantern box
    size on the string, stars about 16 px or more, a halo that steps visibly per level (none, small, bigger, full),
    with the sparkle on bright unless Motion is off. (family:letter-pals) (build)
12. **"Wake more lanterns to open it" plays on shops whose letters are all lit.** src.html:1424-1436 (`tapShop` says
    asleep for any shop not opened by its sign event), 1506. True for sun, fan, pen, hat between their letters and
    their sign events, and for any shop after a class leaves for Village mid-events. Seen: teaching out/11-shops-zoom.png.
    Fixed: a shop whose letters are all lit says a different line ("This shop opens soon. Tap Wake to read its sign.")
    and shows a waiting cue. (general) (spec: one asleep line for every closed shop)
13. **Village at 0 lit points at things that are not there.** Village welcome "Tap a lantern, a shop or a banner. Or
    tap Read the street." and the hint, with no lanterns or banners, every shop asleep, and Read the street answering
    "still asleep". Seen: play f3/v00-fresh-village, f3/v00b; audit lead #read-street. Fixed: at 0 lit the Village line
    and hint say the street is asleep and to tap Wake. (general) (spec: no 0-lit Village case)
14. **Below 800 px wide the Village shows no lanterns, but the welcome says "Tap a lantern".** At 680x425 and 760x900
    Village shows only the "26 lit" chip; at 760x900 the top half is empty sky. Seen: play f3/v11-680.png,
    f3/v13-760.png, audit state-demo-village-680x425.png. Fixed: at 760x900 hang the string in the sky (two rows if
    needed); at 680x425 drop "a lantern" from the line and hint when none is shown. (general) (build: the spec's chip
    is a Wake rule; Village hangs its lit lanterns)
15. **Opening Teacher speaks its how-to and the privacy line every time.** src.html:1764, 578-580 (`teacher`,
    `privacy`, `glowHonesty` queued as event lines): five opens spoke it 5 of 5 (craft v2-teacher-repeats,
    voiceA.txt). Fixed: `teacher` is a how line (once); privacy and glow lines stay on screen and in Read. (general)
    (build)
16. **The voice matches the nearest K neighbors.** voice/lines.json `bank: warm-teacher` (Sulafat), the same as
    calm-corner and sight-words. Fixed: switch to bank voice **playful-friend** (Laomedeia), kept, no K tool uses it;
    set `bank`/`voice` and the style in lines.json before the Forge records. (general) (spec: the spec named
    warm-teacher while noting Sulafat is a neighbor's voice)
17. **Teacher notes and the source list carry build-process text.** notes.md:53 ("the listening review described in
    the build report... The build is a draft and is not ready for a solo nonreader"), notes.md:57 ("spec.md and
    codex-report.md ... recomputed in Scratch"), tool.draft.json sources ("supplied catalog verified in Scratch").
    Fixed: name the real sources (CCSS RF.K.3 and L.K.1, Dolch pre-primer, Fry first 100, Moats Speech to Print,
    Reading Rockets, Zaner-Bloser and Learning Without Tears charts) and drop the build-state lines. (general) (build)
18. **Write it yourself has no way out before drawing.** Only Teacher shows; Next appears after a miss or pass, so a
    child who tapped it by accident must scribble a failure to leave. The spec says it never blocks. Seen: audit
    state-independent-writing-1366x768.png. Fixed: Next visible from the start of Write it yourself. (general) (build)

#### Polish accepted
19. 760x900: size the solo and cart lanterns from the stage height and seat them on the cart, so the lantern is the
    biggest thing (audit state-say-760x900.png). (general)
20. Trace: show the whole letter very faint under the current stroke (current stroke as now, done strokes gold), and
    after a Write it yourself miss show the full letter model over the ink, not one stroke (audit
    state-trace-1366x768.png, play f4/x07-free-miss.png). (family:letter-pals)
21. Long/short boards: the vowel's awake lantern over the vowel of each word with the same small/tall flame shapes as
    the flames step, replacing the CSS blobs (play f2/f01-long.png, craft out/L-long-1366x768.png). (family:letter-pals)
22. End card: every lantern swings onto the string and the shops light down the street before Go to Village, instead
    of the three cart lanterns (play f2/g01-end.png). (general)
23. The new lantern flies to the slot it will hang in on the string, not the top-left corner (`@keyframes fly`; audit
    state-independent-writing-1366x768.png, state-first-shop-sign-680x425.png). (general)
24. Twins marker: replace the `outline:4px solid #7fe3ff` (the kit focus ring) with the spec's flicker plus an amber
    glow, distinct from focus (craft out/L-twins-1366x768.png). (general)
25. Twins at 680x425 and 800x500: move or drop the "Find what changed" label so the tile row does not sit on it or
    crowd the chip, as `.signing` does (craft out/L-twins-680x425.png). (general)
26. Say step shows a glow star before the lantern is lit (chip "0 lit"); show no star until lit (play
    f1/p05-say-tap.png). (family:letter-pals)
27. First screen: hide Hear it again until there is something to hear, instead of a half-opacity dead button
    (src.html:1631). (general)
28. `listenLantern`, `listenBanner`, `listenSign`, `listenWord` are never spoken (Read speaks `hintSpoken`): mark them
    hint-only in voice/lines.json so the Forge does not record them. (general)

#### Settled calls
- Say order (all three lenses): Teaching called it polish, Play and Craft should fix. Settled as should fix
  (7): the spec orders intro then turn, and the model answering its own instruction defeats the step.
- Flames, long/short and twins giveaways (4, 5, 6): settled by "a check must reward the right practice" (BASELINE rule
  2), not sent to Cory. Keep the flame shapes and both anchor pictures; only which sound is asked and the sides change.
- Voice (16): settled by the curio-variety rule from voices/bank.json: playful-friend (Laomedeia). Not bright-teacher
  (bus-stop, a K sibling in this batch) and not gentle-storyteller (act-it-out, snowy-mail-route, K).
- Blocker 1 route: play the isolated `sound.<l>` clip inside sequences rather than spelling sounds in text, so each
  sound is recorded once, clean, and is the same everywhere. Do not rewrite displayed hints to phonetic spellings.
- Village below 800 px (14): a chip is fine at 680x425; the line must not name what is not shown.
- Done when 9 (clips) fails only because clips are not recorded yet; that is the Forge, not this round.
- Audit lead "#begin Wake the village: welcome not heard" is wrong (teaching out/31 and craft v1, v4, v8a logs: the
  welcome is spoken). Welcome cut by a first tap on Teacher, a cart lantern or a double tap is allowed (rule 16).
- Do not change: the trace check (backward, half, tap-only and scribble fail on every stroke of all 52 letters; three
  misses auto-finish), wrong-answer lines that name themselves, Read behavior, line order on taps, frame times.

#### To the spec's open questions
- spec.md Art says "All local FLUX"; prompts.json says gpt-image. The art is fine; the integrator updates the spec
  line (and the Voice line to playful-friend). Codex does not touch spec.md.

#### Not taken
- Craft nit 11 (Sound back on re-speaks the question): repeating the current question is helpful; leave it.
- Craft nit 13 (2.93 MB): 2 MB is a goal (rule 12); add the `Size:` line only if the bundle passes 6 MB with clips.
- Teaching nit 10 (umbrellabird anchor): the picture carries it and the art is made; not worth a redraw.
- Teaching nit 11 (short wobbly strokes fail sometimes): white-noise sim overstates real finger ink; the exit check
  does one real-touch try on m, k and i instead of a change now.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: letter-lanterns (round 1)

Cold Craft lens on the built bundle `tools/letter-lanterns/letter-lanterns.html` (2,930,709 bytes). Not a Curiosity
(K ELA lesson tool), so lesson norms apply. My frames and logs: `S:/CurioClass-codex-scratch/letter-lanterns/craft/out/`
(frames), `craft/voiceA.txt`, `craft/v56.txt`, `craft/v5.json` (voice logs), `craft/shots/*.json` (the shots).

Counts: blockers 1, should fix 6, polish 3, nit 5.

#### Contract (clean)

- One file, kit used (Curio.voice, Curio.yes, Motion, Sound, Read). No network requests: no http(s) URL, fetch or XHR
  in the bundle; `performance.getEntriesByType('resource')` empty after a full start (probe shot). No console errors
  or exceptions in any of my 60 shots (the only log line was the iframe host page's own favicon 404, not the tool).
- Frame times, Village with 12 lit lanterns and fireflies at 1366x768: median 16.7 ms, p95 16.7, max 16.8 over 3 s
  (P-frames-village).
- Art: all 96 `art:` tokens have a prompts.json entry and every entry is used; all `people: false` (creatures, goods,
  shops, scenes).
- Words: no em dashes in src, notes, spec or lines; "Curio Class" never "Curio" alone; privacy line in Teacher
  ("Lanterns are saved on this device only. Nothing leaves it.") and spoken on open.
- Targets: every visible control 60 px or more at 680x425, 800x500, 1000x625, 1366x768, 1920x1080 in the flames,
  twins, long/short, banner, banner find, sign and Village states (button sizes printed in each L-* shot). Keyboard:
  lanterns take a visible focus ring (K-focus-lantern-1366); the slate traces by keyboard (Space, 29 x ArrowDown,
  Space passed stroke 1 of capital M, v8c).

#### Findings

1. **blocker** (general). `src.html:679-692` `glyph()`, used for shop signs (`:1510`) and long/short boards (`:1601`).
   Each letter's SVG viewBox is cropped to that letter's own bounds, so every letter is scaled and centered on its own:
   x-height letters grow to near capital height and there is no shared baseline. Lowercase c and o on the "cot" sign
   read as capitals ("COt"), the descenders of p and g float up level with the other letters instead of dropping below
   the line ("pup", "pig", "dog"), and the o in "dog" sits high. These are the words kindergartners are asked to read,
   and the tool teaches letter forms. Seen: `out/Z-signs-village2.png` (zoomed signs), `out/L-sign-680x425.png`,
   `out/L-twins-1366x768.png`, `out/H-twins-375x812.png`. Better: lay each word out on one shared slate box (top line
   0, baseline 1, descender 1.5) with fixed advance widths, the way the trace slate already does.
2. **should fix** (general). `src.html:1764` and `:578-580`. Opening Teacher speaks `teacher`, `privacy` and
   `glowHonesty` as event lines every time. "Tap letters and sight words to turn them on or off. Tap Close to go back."
   is a how-to: five opens spoke it 5 of 5 (`v2-teacher-repeats`, voiceA.txt). Make it `how`; the privacy line can stay
   on screen and in Read.
3. **should fix** (general). `src.html:817`. A right Find queues `[say (how), intro.<l>]`, so the child hears "Say its
   sound. Tap the lantern to check." and then at once the model "Mmm. M says mmm, like moth." The instruction to say it
   first is answered before the class can try, and "tap to check" is stale by the time the model ends. Spec order is
   intro first, then the turn line ("Your turn. Say its sound out loud. Then tap the lantern to check.", which the
   built text also shortened). Seen: v1 log 32274 `say` spoken, 35830 `intro.m` spoken; v4 and v8c the same.
4. **should fix** (general). `src.html:1514-1515` vs lines `sign` and `twinIntro`. The lines say "Tap each lantern to
   hear it" and "Only one lantern is different. Tap the different lantern", but the screen shows cream letter tiles
   over the sign, not lanterns (spec: lit lanterns hang over the sign's letters). A child who can't read is told to
   find a lantern that isn't there. Seen: `out/L-sign-680x425.png`, `out/L-twins-1366x768.png`. Either hang the small
   awake lantern art (already loaded) over each letter, or say "tile"/"letter".
5. **should fix** (general). `voice/lines.json` `bank: warm-teacher` (Sulafat). The two nearest K neighbors that are
   built, calm-corner and sight-words, also use warm-teacher/Sulafat (checked their lines.json); STANDARDS Variety asks
   for a voice different from the nearest neighbors. The spec named it while noting Sulafat is a neighbor's voice.
   Pick another kept K-friendly voice before the Forge records about 310 lines.
6. **should fix** (general). `notes.md:53` and `:57`. Public teacher notes talk about the pipeline: "the listening review
   described in the build report", "The build is a draft and is not ready for a solo nonreader", "spec.md and
   codex-report.md", "recomputed in Scratch". A teacher can't open those. Replace with the real sources (the spec's
   Sources table, short) and drop the draft sentence once clips land.
7. **should fix** (general). `src.html:199` banner font `'Century Gothic','Trebuchet MS',sans-serif`. Banners are the
   one place words are set in a system font instead of the drawn ball-and-stick glyphs. Where Century Gothic is missing
   (Chromebooks, Macs, many school images) the fallback has a two-story a and g, against the spec's "single-story a and
   g" and against every other word in the tool; "I" also becomes a bare bar like l. Not visible on this PC (Century
   Gothic is installed), so seen by reading the stack. Draw banners with the fixed glyph layout from finding 1.
8. **polish** (general). `src.html:189` vs `kit/curio.css:11`. The "different lantern" marker on twins is `outline:4px
   solid #7fe3ff`, the exact kit focus ring. One look means two things: a keyboard user can't tell focus from the
   answer, and a class sees what looks like a selection. Seen: `out/L-twins-1366x768.png`. Better: the spec's flicker,
   or an amber glow plus a small mark, distinct from focus.
9. **polish** (general). Twins at 680x425 and 800x500: the sound-tile row sits on top of the "Find what changed" label
   and crowds the "9 lit" chip (`out/L-twins-680x425.png`, `out/K-focus-sign-680.png`). The audit did not list the
   twins state, so it never saw this. Move the label (as `.signing` already does for Sign) or drop it on short boxes.
10. **polish** (general). `src.html:195-197`. Long/short boards show the two flames as plain CSS blobs (a cream rounded
    slab and an orange oval) floating above the banners, with no vowel lantern over each as the spec says; next to the
    painted art they read as placeholders (BASELINE rule 3). Seen: `out/L-long-1366x768.png`, `out/L-long-680x425.png`.
    Better: the vowel's awake lantern over each board with the same short/tall flame shapes used in the flames step.
11. **nit** (general). `src.html:1840`. Sound back on calls `narrateStep()`, so every Sound off/on re-speaks the current
    question (v8d: `find.m` spoken again). The kit rule is the welcome only if never said; repeating the question is
    arguably helpful, so optional.
12. **nit** (general). `listenLantern`, `listenBanner`, `listenSign`, `listenWord` are in lines.json (so they would be
    recorded) but are never spoken: Read speaks `hintSpoken` (the real question). Mark them hint-only or drop them from
    the recording list.
13. **nit** (general). 2.93 MB, over the 2 MB goal (art 2.58 MB as base64; `lesson.json` `paths` is 248 KB of
    pre-sampled stroke points that could be built at load from the spec's stroke formulas). About 300 recorded clips
    still to come will likely pass 6 MB: plan the `Size:` line in notes.md now.
14. **nit** (general). `src.html:1631`. On the first screen "Hear it again" shows disabled at half opacity; a dead
    button on the first screen of a K tool. Hide it until there is something to hear.
15. **nit** (general). spec.md Art says "All local FLUX"; prompts.json says every image was drawn by Codex with OpenAI
    gpt-image. The art is fine; the spec line is out of date.

No cultural, Native or hard-history content: no sensitivity review needed from this lens.

#### Standard voice check

Held clicks (0.12 s), Sound and Motion on, 1366x768 (1920x1080 for the check run), log from `__tool.vlog`.

| line | kind | action | expected | spoken |
|---|---|---|---|---|
| welcome | how | Wake the village, then a wrong tap at 5 s | 1 (a cut is fine, rule 16) | 1 (cut by the tap) |
| find.m | event | 5 wrong taps | 5 | 5 |
| wrong.s | event | 5 wrong taps | 5 | 5 |
| say | how | right Find | 1 | 1 (but before intro, finding 3) |
| intro.m | event | right Find | 1 | 1 |
| sound.m | event | 5 taps in Say | 5 | 5 |
| teacher | how-to text, queued as event | 5 Teacher opens | 1 | **5** (finding 2) |
| twinSame | how, once per pair | 5 taps on a shared tile | 1 | 1 (4 silent) |
| twinDiff.1, then twinWhich.1 | event | different tile | 1 each | 1 each |
| word.cat + twinWhich.1 | event | 3 wrong sign picks | 3 each | 3 each |
| yes | event | right sign; 6 check finds; 2 banner finds | 1; 6; 2 | 1; 6; 2 |
| missStart | how, once per stroke per cause | 2 misses on stroke 1, 2 on stroke 2 | 1 + 1 | 1 + 1 (silent after) |
| together | once per letter | third miss on two strokes | 1 | 1 (silent second time) |
| checkIntro | event | 2 Lantern checks | 2 | 2 |
| find.x (check) | event | 6 check finds | 6 | 6 |
| seeSay | how | 2 checks | 1 | 1 (silent second) |
| bannerFind.x | event | 2 checks | 2 | 2 |
| village | how | Wake all, 2 returns from check | 1 | 1 (silent after) |

- Stale lines (v6: taps 0.25 s apart on Wake the village, s, a, s, then Village, then Wake): each wrong line cut by
  the next tap, Village welcome cut by Wake, then `find.m` for the step on screen. Nothing played after its moment.
- First tap: stage background tap, welcome at +133 ms then the start line; Tab key, welcome at +17 ms. Read, Sound,
  lanterns, Teacher, mode buttons: audit rows, confirmed in my logs where I touched them (Read speaks the hint only;
  a lantern speaks only its own line).
- Read: Read during the welcome cut it and spoke the question; a wrong tap 1.2 s later waited for Read and played after
  it (v8a); Read with Sound off spoke (v8d); a mode change right after Read started the Village welcome at once (v8b).
- Order: lines followed the actions in every run.

#### Audit pilot

- Leads confirmed: welcome not heard after a first tap on Teacher or a cart lantern (true, and fine under rule 16:
  the premise is not needed later, and Wake the village still plays it); two quick taps cut a mode welcome (rule 16,
  not reported).
- Leads wrong: "#begin Wake the village: welcome not heard". It is heard: `start()` queues it as a `how` line inside
  its own sequence (v1, v4, v8a logs: `welcome` spoken), so the audit's welcome detector misread it. "Five held
  clicks: #teacher clean" missed that the Teacher how-to is spoken on every open (finding 2).
- Missed: audit-states.json has no flames, twins, long/short, banner or banner-find state, and Sign only at three
  sizes, so the sign glyph layout (finding 1), the twins overlap at 680x425 (finding 9), the focus-colored twin marker
  (finding 8) and the placeholder-looking board flames (finding 10) never appeared in its frames. It also can't see
  line order against the screen (findings 3 and 4).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: letter-lanterns (round 1)

Played twice: as a kindergartner alone at home (sound on, no reading) and as a teacher projecting it at 1366x768.
Frames are in `S:/CurioClass-codex-scratch/letter-lanterns/play/` (f1 = the first lantern walked by real held clicks
and real drags, f2 = every event kind, f3 = Village, f4 = misses and free writing), plus the shared audit frames in
`S:/CurioClass-codex-scratch/letter-lanterns/audit-r1/`. Voice was read from `__tool.vlog` after each shot.

What works: the first screen is clear (one gold button, the hint names it), the Find, Say, Trace and Sign loop is
calm and big on a projector, wrong answers teach ("That one says sss."), the second miss beckons the right lantern,
three trace misses finish the stroke with "Let's do it together", tracing backward or scribbling never passes, and
Read the street is a good class finale. The lit string filling the sky is a real reward. Counts below.

#### Findings

1. **Say step: the next action is never spoken.** Wake, Say step (`src.html` answerLetter, the `say`/`seeSay`
   branch: `hint('next'); speak('sound.'+letter)`). After the child taps the awake lantern they hear only "mmm"; the
   hint switches to "Tap Next." but that line is never voiced (the log shows `Tap Next.` only as `dropped`, the
   invalid line `interruptNarration` uses). A non-reader alone at home hears the sound and then silence with a gold
   button they cannot read. Same in a Lantern check's See and say. Other done-moments already end with "Tap Next."
   ("Yes! You found it. Tap Next.", "Map! The map shop is open. Tap Next."), so this is the one gap. Better: say
   "Tap Next." once as a how line after the sound the first time, then hint only. Seen: f1/p05-say-tap.png, log
   `[["spoken","mmm"]]`; f2/c02 log. **should fix**, general.

2. **Say step speaks the instruction before the model.** Wake, right Find (`speak([['say',{kind:'how'}],'intro.'+letter])`).
   On the first lantern the child hears "Say its sound. Tap the lantern to check." and then "Mmm. M says mmm, like
   moth." The last thing heard before the waiting moment is the teacher's model, not the child's turn, and the
   right-answer moment opens with an instruction instead of the payoff. The spec has the intro on the right Find,
   then Say ("Your turn..."). Better: intro first, then the say line. Seen: f1/p04-right-m.png, log order
   `spoken Say its sound...` then `spoken Mmm. M says mmm, like moth.` **should fix**, family:letter-pals.

3. **Twins: the shop windows give the answer away.** Wake, Twins (e.g. pan/pin after lantern 7). Both twin shops are
   already open, so each shows its goods in the window: a pincushion under "pin", a frying pan under "pan". "Which
   sign says pin? Tap it." can be answered from the pictures the child just matched in the Sign events, without
   reading the letter that differs, which is the whole point of RF.K.3d (POLISH, Games and quizzes). Better: twins
   shops show closed windows or no goods until the sign is picked, then light up. Seen: f2/e03-twin-diff.png.
   **should fix**, family:letter-pals.

4. **Banners: capital I looks exactly like small l, and "a" turns double-story.** Village street 1 and Lantern check
   banner finds (`.banner-card` font: `'Century Gothic','Trebuchet MS',sans-serif`). The banner "I" is a bare
   vertical bar, the same shape as the l on the ladybug lantern hanging above it. On this machine the font falls back
   and the "a" banner draws a double-story a, while every lantern and sign teaches the single-story ball-and-stick a
   (spec Look). School Chromebooks have neither listed font, so most classrooms see the fallback. Better: draw banner
   words with the tool's own `glyph()` paths (capital I with its top and bottom bars, as STROKES defines it).
   Seen: play/zoom-banner.png (from f3/v04-readstreet.png), f2/f02-banner-find.png ("I my the"). **should fix**,
   general.

5. **Glow levels do not read at a glance on the string.** Village and the Wake string at 1366x768 (`.string .stars
   { font-size:10px }`, halo via `::before` opacity). With 26 lit and mixed glow, one star and two stars are 10 px
   marks under 50 px lanterns; the halo difference is not visible, and the creatures differ in drawn size (the moth m
   and the inchworm i are half the size of the ladybug l), so size reads as glow more than glow does. From the back of
   a room the four outcome states (Done when 7) cannot be told apart. Better: one shared lantern box size on the
   string, stars about 16 px, and a halo that steps visibly per level. Seen: play/zoom-string.png, f3/v04, f3/v09.
   **should fix**, family:letter-pals.

6. **Below 800 px wide the Village hides every lantern, but the welcome says "Tap a lantern".** Village at 680x425
   and 760x900. The string is replaced by the "26 lit" chip in Village too, so the glowing village (the tool's own
   outcome picture) is gone, and at 760x900 the top half of the stage is empty sky. The Village welcome still says
   "Tap a lantern, a shop or a banner." Better: hang the string (even scrolled or two rows) in the empty sky at
   760x900; at 680x425 at least drop "a lantern" from the line when none is shown. Seen: f3/v11-680.png,
   f3/v13-760.png, audit state-demo-village-680x425.png. **should fix**, general.

7. **Village before any lantern is lit points at things that are not there.** Village with 0 lit. The welcome says
   "Tap a lantern, a shop or a banner. Or tap Read the street." and the hint "Tap a shop or Read the street." There
   are no lanterns or banners, every shop is asleep, and Read the street only answers "This street is still asleep."
   A child who taps Village first gets three dead ends before learning to go to Wake. Better: at 0 lit, the Village
   line and hint say the street is asleep and to tap Wake. Seen: f3/v00-fresh-village (log), f3/v00b. Audit lead
   "#read-street ... still asleep" is this. **should fix**, general.

8. **760x900: the lantern being learned is smaller than the cart and floats above it.** Wake, Say and Find at 760x900.
   The backdrop scales to the tall stage but the lantern does not: the moth hangs mid-air about 150 px wide over a
   cart twice its size. The step's focus is not the biggest thing on stage. Better: size the solo and cart lanterns
   from the stage height there, and seat them on the cart. Seen: audit state-say-760x900.png. **polish**, general.

9. **Tracing shows one stroke, never the letter.** Wake, Trace. Stroke 1 of M is a lone vertical bar; the child
   does not see the M they are making until it is done, and the "Look at the model over your ink" after a free-write
   miss shows only that one stroke, not the letter. Better: draw the whole letter faintly under the current stroke
   (current stroke brighter, done strokes gold), and show the full model after a free-write miss. Seen:
   audit state-trace-1366x768.png, f4/x07-free-miss.png. **polish**, family:letter-pals.

10. **Sign and Twins say "lantern" for plain letter tiles.** Wake, Sign and Twins. The hint says "Tap each lantern to
    hear it" and "Tap the different lantern", but above the sign are cream rounded tiles, not lanterns (the spec has
    the lit lanterns hanging over the letters). A child looking for a lantern finds none. Better: hang small awake
    creature lanterns over the letters, or say "letter". Seen: f2/d01-sign-map.png, f2/e01-twins.png.
    **polish**, family:letter-pals.

11. **Long/short flames are loose blobs, off the vowel.** Wake, Long/short (no/not). The tall and small "flames" are a
    cream teardrop and an orange dot centered on each cloth, not over the o, and look unrelated to the flame buttons
    of the vowel step. Better: the o lantern over the o of each word with its tall or small flame, as the spec says.
    Seen: f2/f01-long.png. **polish**, family:letter-pals.

12. **The end card is three lanterns on a cart.** Wake, end. "The whole village glows!" sits over m, s and a on the
    cart, the same picture as the first screen. The moment the whole year built to is flat. Better: every lantern
    swings in, shops light down the street, then Go to Village. Seen: f2/g01-end.png. **polish**, general.

13. **The new lantern flies to the top-left corner, not to its place on the string.** Wake, trace done (`@keyframes fly
    { to { top:6px; left:20px } }`). The string is centered, so the lantern lands in an empty corner, vanishes and
    pops in elsewhere; frozen mid-flight it also covers the "5 lit" chip. Better: fly to the slot it will hang in.
    Seen: audit state-independent-writing-1366x768.png and state-first-shop-sign-680x425.png / 375x812 (creature in
    the corner). **polish**, general.

14. **Write it yourself has no way out before you draw.** Wake, Write it yourself. The panel shows only Teacher; Next
    appears only after a miss or a pass. The spec says it never blocks. A child who tapped it by accident has to
    scribble a failure to leave. Better: keep Next visible. Seen: audit state-independent-writing-1366x768.png.
    **polish**, general.

15. **Say step shows a glow star before the lantern is lit.** Wake, Say: one star under the moth while the chip reads
    "0 lit". Seen: f1/p05-say-tap.png. **nit**, family:letter-pals.

Cheap passes tried: tapping every lantern in Find (wrong taps just repeat, first meetings never score; checks reset
the streak), every picture in Sign (each wrong one names itself, which teaches), every lantern in Twins ("same"
line), scribbling, tapping and tracing backward on the slate (all fail, three fails auto-finish without a free pass).
Only Twins (finding 3) can be passed without reading. Nothing cultural, Native or hard-history to flag.

Counts: blocker 0, should fix 7, polish 7, nit 1.

#### Audit pilot

- Leads confirmed: Read the street on an asleep street says "still asleep" (finding 7, with the welcome and hint
  around it).
- Leads not reported (BASELINE rule 16): welcome not heard after a first tap on Teacher, a cart lantern or a quick
  double tap on Wake or Village. The premise is not needed later, and the Find question is in Read.
- Clean rows I relied on: every size and state clean for targets, fold and overlaps; Motion off clean; resize
  mid-action clean.
- Missed by the audit: the unspoken "Tap Next." in Say (it logs the dropped placeholder, not a missing line), the
  intro/say order, the twins window giveaway, the I/l and double-story a on banners, glow levels unreadable at a
  glance, the Village string vanishing below 800 px, the 760x900 floating lantern, and the end card.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: letter-lanterns (round 1)

Cold read of spec.md, src.html, notes.md, lesson.json, voice/lines.json, tool.draft.json, audit-r1. Driven with
scripts/drive.py (port 9868, muted). My frames and logs: `S:/CurioClass-codex-scratch/letter-lanterns/teaching/out/`
(shot lists shots.json to shots4.json, glow sim glow.py beside them).

Counts: blocker 2, should fix 4, polish 3, nit 2.

#### Blockers

1. **Every sound inside a sentence is written as a bare letter, so the voice says letter names, not sounds.**
   Where: lesson.json `lines` find.* (26), wrong.* (26), intro.* (26), short.* (5), twinDiff.* (10): "Which lantern
   says t? Tap it.", "T. T says t, like turtle.", "A. A says a, like ant.", "Short glow: a, like ant.", "a. o. Cat.
   Cot." Only m, s, n, f, r, l, v, z are spelled as sayable sounds (mmm, sss); t p d b c k g h j w y, x (ks), q (kw)
   and all five vowels are single letters. How seen: the voice log in out/01, 02, 04, 06 shows these exact texts going
   to the voice; a lone "t" or "a" is read "tee", "ay" by the browser voice and by any text-to-speech model. In
   voice/lines.json only the 31 `sound.*` / `longSound.*` ids carry the "isolated sound, not the letter name"
   instruction (`phoneme_takes_required`); the 93 sentence lines that also carry a sound have none, and Done when 9
   checks only the 31 clips. Effect: the Find question for 18 of 26 letters asks for the letter name; intro.a says
   "Ay says ay, like ant", which teaches the wrong short a; short.a and long.a sound the same ("ay"), so RF.K.3b's
   contrast is never heard in words. This is the core of RF.K.3a and b. Fix direction: play the recorded `sound.<l>`
   clip inside these lines (sequence: "Which lantern says" + sound clip + "Tap it."), or give every such line its own
   phoneme direction and add them all to Done when 9. Also longSound.* is recorded but never played (src.html has no
   `longSound` reference); findLong.* should use it. Tag: general (any phonics tool).

2. **Lantern check Finds always use the same three lanterns, so the third Find is free by elimination and glow
   inflates.** Where: src.html:717-718 (`makeChoices(target, true)` pool = the other check targets only), spec
   Interactions "choices from lit letters". How seen: out/40-check-trio (10 lit letters): the three Finds offered
   {a,m,s}, {a,s,m}, {s,m,a}; the last one is the only letter not yet asked. glow.py: a class that knows none of the
   three sounds but remembers which were asked raises about 2.4 letters to two stars in 4 checks, against 0.8 for
   blind guessing (spec's sim assumed blind 1/3 guessing). Glow is the tool's picture of what the child knows (One
   idea), so a meter that rises on elimination misleads. Fix: draw the two distractors from all lit letters (spec), or
   at least not from the round's other targets. Tag: family:letter-pals.

#### Should fix

3. **The vowel flame question always has the same answer: the tall flame on the right.** Where: src.html:1580-1585
   (short always left, long always right, labelled "Short" / "Long") and 837-858 (only `findLong` is ever asked).
   How seen: out/03-flames-a.png and out/04 log (short, long, then "Which flame says A?" and the right answer is the
   tall flame every time, for all five vowels). A child passes RF.K.3b's flame check without listening. Fix: ask for
   the short or the long sound at random, and swap the flame sides at random. Tag: family:letter-pals.

4. **The long/short word pick always asks for the short word, which is also always the longer word with the small
   flame.** Where: src.html:1214-1215 (`good = word === pair[1]`), lesson.json lsWhich.0-5 (not, got, met, hen, hit,
   wet), spec "Asked: the second word". How seen: out/05-long-0.png: the answer board is the 3-letter one with the
   small flame, in all six pairs. Cheap way: always tap the longer word. Fix: ask either word of the pair (for example
   "Which word says no?"). Also the spec's vowel lantern over each board is missing (only a loose flame shape, set
   between n and o on "no", not over the vowel). Tag: family:letter-pals.

5. **"Wake more lanterns to open it" plays on shops whose lanterns are all awake.** Where: src.html:1424-1436
   (`tapShop` says `asleep` for any shop not yet opened by its sign event) and 1506 (no sleeping lantern is drawn when
   every letter is lit). How seen: out/11-shops-zoom.png (street 2 with every letter lit, shops closed, no sleeper);
   by the EVENTS table this is the real state of sun after lantern 12, fan after 13, pen after 15 and hat after 16,
   and of any shop after a class leaves for Village mid-events. The line is false then. Fix: for a shop whose letters
   are all lit, a line such as "This shop opens soon. Tap Wake to read its sign." (and a waiting cue on the shop).
   Tag: general.

6. **Teacher notes and the public source list carry build-process text.** Where: notes.md:53 ("Clean isolated sound
   recordings still require the listening review described in the build report. The build is a draft and is not ready
   for a solo nonreader until that check passes."), notes.md:57 ("spec.md and codex-report.md ... recomputed in
   Scratch"), tool.draft.json sources ("supplied catalog verified in Scratch"). A teacher reading the tool page sees
   internal files and a "draft" warning. Fix: name the real sources (Dolch pre-primer, Fry first 100, the CCSS PDF,
   Moats, Reading Rockets) and drop the build-state lines. Tag: general.

#### Polish

7. **Say step: the model sound plays right after "Say its sound", before the class can try.** Where:
   src.html:817 (`speak([say, intro.<l>])`). How seen: out/02 log: "Say its sound. Tap the lantern to check." at 8.7 s,
   then "Mmm. M says mmm, like moth." at 12.1 s with no tap. notes.md Key skills says "Say a sound before checking it
   against the model", which is not what Wake does. Better: intro first (as the spec orders it), then the "Your turn"
   line, and the model again only on the tap. Tag: family:letter-pals.

8. **Banner words fall back to a double-story a.** Where: src.html:198 (`'Century Gothic','Trebuchet MS',sans-serif`).
   Century Gothic is not on Chromebooks or a stock Mac; out/24-bannerfind-fallback.png shows the sight word "a" as a
   double-story a while every lantern and sign teaches the single-story form (spec Look). Better: draw banner words
   with the same `glyph()` paths as the signs (they exist for a, g, and capital I). Tag: general.

9. **Glow states are hard to see on the string.** out/10-string-zoom.png: 1 to 3 stars at about 10 px, halos not
   visible at string size. Done when 7 holds only up close. Better: bigger stars on the string, or show glow on the
   lanterns in Village's own view. (Play/Craft may weigh this more.) Tag: family:letter-pals.

#### Nits

10. umbrellabird (short u anchor) is a word few five-year-olds know; the picture carries it, but "up" or "umbrella"
    is the usual anchor. Tag: general.
11. Trace check on short straight strokes rejects some wobbly but right traces through the direction rule: with
    white jitter of plus or minus .03h, m stroke 1 passed 85%, k stroke 3 88%, i stroke 1 90% (out/20-dbg); long
    strokes 97-100%. Real finger ink is smoother than white noise, so this may overstate it; worth one real-touch try.
    Tag: family:letter-pals.

#### Done when

| # | Result | How |
|---|---|---|
| 1 | pass | audit sizes and states clean at every size |
| 2 | pass | out/31: welcome at 1.4 s, then "Which lantern says mmm?" at 6.8 s; hint changed at once |
| 3 | not re-tested | audit voice rows clean; left to Play/Craft |
| 4 | pass with blockers 1-4 | Find wrong stays asleep (out/02); See and say silent until tapped (code, src.html:1265); banner check 3 choices; twins: all 10 pairs differ in one place, shared lantern gives twinSame (out/06) |
| 5 | pass | out/07: three sound keys and two wrong pictures, "map" first spoken in open.map after the right pick; banners have no sound keys |
| 6 | pass | out/12: backward, half, tap-only and scribble failed on every stroke of all 52 letters, guided and free; third miss auto-completes (audit assisted-stroke) |
| 7 | weak | see polish 9 |
| 8 | not re-tested | Craft |
| 9 | fail | no clips in the bundle yet; and see blocker 1 (the check covers only 31 of the 120+ lines that carry a sound) |
| 10 | pass | out/13: Start over clears `curio-letter-lanterns`, shows Wake the village; reload resumed (out/02 loaded out/01's Find); privacy line in Teacher |

Event schedule recomputed in Python from lesson.json with every letter on: all 56 events play, none dropped, all 24
shops open, every twin follows both its signs, every long/short pair's letters are lit when it plays.

Facts spot-checked against my own knowledge of the sources: all 10 sight words are on the Dolch pre-primer list and
in Fry's first 100; c /k/, g /g/, x /ks/ at word end, qu /kw/; anchors ant, inchworm, octopus, elephant and
umbrellabird start with the short vowel; acorn, emu, ivy, ocean and unicorn with the long one; the six open/closed
pairs follow the open-syllable rule; stroke paths for a, b, c, d, e, g, s, u, J, U checked for direction
(counterclockwise a/c/d/e/g, clockwise b/p bowls, ball-and-stick). No cultural, Native or hard-history content; no
sensitivity review needed. No sensitive standard topics for the teacher notes.

#### Audit pilot

- Leads confirmed: none that bear on teaching. The first-tap welcome rows for a lantern and Teacher are real but
  allowed by BASELINE rule 16 (nothing the welcome says is needed later).
- Leads wrong: "#begin Wake the village: welcome not heard". out/31 polled the voice every second: the welcome was
  spoken whole (no cut) and the Find question followed at 6.8 s.
- Missed (outside what it can see): blockers 1 and 2, should fix 3 to 6, polish 7 to 9. Tooling note: in my shots a
  drive.py `"wait"` after clicks did not seem to delay the `"after"` script (out/22 read an unplayed queue at "16 s");
  polling inside `"after"` gave the true timeline.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: letter-lanterns (Codex fix, round 1)

Curiosity override: the supplied spec and Refine describe a lesson path. The user's instruction and CODEX-CURIOSITY.md win. I removed the quiz/check ladder, star ratings, earned badges, forced sequence, welcome gate, end card and kit header. The same supplied letters, words, art and tracing mechanics are freely explorable. For a removed lesson-only interaction, FIXED below means its defect was eliminated by that removal; it does not claim the requested quiz was built.

Evidence paths below are relative to `_scratch/letter-lanterns/`. I inspected the individual frames and contact sheets named here. The original source and data are retained as `src-before.html` and `lesson-before.json`. `refine.md`, `refine/` and `spec.md` were not edited; no git commit was made. All work was inside the two authorized folders.

#### Blocker

1. **NOT FIXED acoustically.** Before: `before2/S07-S08-say.png` and its voice log showed the instruction before the bare-letter sentence; the original line table includes `find.t`, `intro.a`, `short.a`, `twinDiff.0` exactly as reported. The new sequence table references reusable isolated `sound.<letter>` pieces; long vowels reference `longSound.<vowel>`. Missing isolated clips use a whole anchor-word fallback rather than reading a letter name as a short sound. `numbers.json` and `voice-flames.json` prove routing; `audioReady = 0`. There are no recordings to listen to, so neither clean stops nor all 31 clips can be approved. The direct pre-fix Find-t/a table probe did not finish because an overlapping driver batch reset Chrome; I confirmed those strings in the original source, not by a completed acoustic walk. The removed Find/wrong quiz sentences are not recorded. Forge production and listening remain open, as Refine's settled call anticipates.
2. **FIXED.** Before `before1/B02-sign-680.png`, `before1/B02-twins-1366.png`, `before2/B02-twins-375.png`: each letter had a different cropped viewBox. After `final1/sign-680.png`, `final2/twins-1366.png`, `final2/twins-375.png`: each whole word shares one SVG, .85 advance, y=0/.5/1/1.5. The p, i and g translations are `(0,0)`, `(.85,0)`, `(1.7,0)`; p/g retain their descenders. The same function draws all signs, boards and banners.
3. **FIXED by Curiosity override.** Before `before2/B03-choice-pool.png`: ten sampled checks offered only m/s/a. The check and its rating accumulation were removed. `final-checks.json` records zero check/rating widgets and no rating fields after repeated taps. An exploration mark no longer claims sound knowledge.

#### Should fix

4. **FIXED by Curiosity override.** Before `before1/S04-flames.png`: short left, long right, long always requested. Both freely playable flames now keep their shapes and randomize sides. Across 24 opens, `final-checks.json` observed both `short,long` and `long,short`; `final3/voice-flames.png`/`voice-flames.json` shows short and long routes. There is no hidden answer or credit to earn.
5. **FIXED by Curiosity override.** Before `before1/S05-long.png`: always "not". After `final2/long-680.png` and `final2/long-1366.png`: either board speaks its own word and vowel; sides shuffle. Eight alternating longer/shorter word sweeps in `final-checks.json` produced no score or advancement. No word-length quiz remains.
6. **FIXED.** Before `before1/S06-twins-goods.png`: two visible goods windows. After `final2/twins-1366.png`, `twins-680.png`, `twins-375.png`: zero goods before reveal, six actual lantern controls. Entering a pair hides even previously opened windows. Either word can then be revealed without a right/wrong gate.
7. **FIXED by Curiosity override.** Before `before2/S07-S08-say.png` log: say instruction first, intro immediately after. The Say/check step is gone. A lantern tap directly models the selected letter/anchor; no instruction asks a child to answer just before revealing an answer. See `voice-main.json` and `final3/voice-main.png`.
8. **FIXED by Curiosity override.** Before the same log: only the sound after the Say tap, with no Next cue. There is no Say-done waiting state or required Next. Trace and Write it yourself are directly available, and optional writing has Back to lantern and Next stroke from the outset. `final2/free-miss.png`, `proof/free-exit-before-draw.png`.
9. **FIXED.** Before `before1/S09-banners.png`: system font, bare-bar I. After `final2/banner-a.png` and `banner-I.png`: shared geometric word layout, single-story a, barred I. No installed school font is required.
10. **FIXED.** Before `before1/B02-sign-680.png`: plain cream sound tiles. After `final1/sign-680.png`, `final2/sign-375.png`, `final2/twins-1366.png`: the existing awake creature art carries every sound letter above the sign. Six lantern targets in Twins, with no tile/voice mismatch.
11. **FIXED by Curiosity override.** Before `before1/S11-string.png`: 10px stars with hard-to-read mastery distinctions. There are no mastery levels or stars now. Every string lantern has a 60x80 box and a simple touched glow, explicitly described as exploration in Settings and Manual. `last/street-wrap.png`: 26 boxes, all inside the viewport; `final1/street-760.png`: all 26 visible in three rows.
12. **FIXED.** Before `before3/S12-closed-ready.png` and log: all letters lit, yet "Wake more". Shops now remain directly explorable. A ready shop opens its sign and names its window action, without requiring more letters. The obsolete asleep/unlock line is gone; `pre-audit/ready-shop.png`/`ready-shop.json` and Wordbook frames show directly accessible signs. No shop depends on a later event queue.
13. **FIXED.** Before `before1/S13-empty-village.png`: hint named unavailable reading objects. After `after1/street-empty.png`: the hint says the street is asleep, names the existing Lanterns control, and offers a visible shop. Every shop is actually explorable at zero touched letters. No phantom lantern/banner invitation.
14. **FIXED.** Before `before1/S14-village-760.png` and `S14-village-680.png`: no lantern string at either width. After `final1/street-760.png`: 26 in three rows, last q box bottom 375px, shops begin at 390px. At 680x425 the string is intentionally hidden and the hint omits lanterns, verified in `after1/street-680.png` and the audit. Phone Street uses the same conditional wording. The 1000x625 layout also hides the string to give the shops room, with a matching hint. Zero touched letters with an already-opened shop use the normal shop hint; a fresh unopened street uses the asleep hint (`final-hints/`). All-hidden content retains its Settings cue after resize (`all-off-resize.json`). An empty filtered street has no dead Read-the-street button, and a filtered Wordbook selects an allowed item or points to Settings. The one-letter a banner and empty m street are proved in `empty-state-proofs/`.
15. **FIXED.** Before `before2/S15-teacher.png`: Teacher began speaking on three of three openings. After `voice-teacher-final.json`: teacher how line spoken once, later openings silent because heard. Privacy remains visible and drawer Read explicitly reads it. `last/settings-read.png` and `pre-audit/phone-settings-read.png`. No repeated automatic privacy or rating lecture.
16. **FIXED manifest selection.** Before voice/lines.json selected warm-teacher/Sulafat. It now selects playful-friend/Laomedeia with the matching style. The 187 deduplicated manifest lines equal observed `allLines()`. This confirms the requested bank configuration, not unmade recordings.
17. **FIXED.** The old notes' draft/listening-review/build-report prose and source list's "verified in Scratch" wording were removed. Notes, Manual and metadata name the real sources and their rights, distinguish references from bundled original material, and contain no readiness claims. `static-verification.json` records the material and licence check.
18. **FIXED.** Before `before3/S18-free-reproduced.png`: `nextHidden = true` before any mark. After `after1/free-1366.png`: both exit and next exist at onset; `proof/free-exit-before-draw.png` verifies leaving without drawing at 680x425. `final2/free-miss.png`: the same controls remain 60px after a miss.

#### Polish accepted

19. **NOT FIXED fully: precise seating is still open.** `final1/default-760.png` and `corrective2/fixed-solo-760.png` use stage-height sizing and make the selected lantern the largest control/object. Cart figures are much larger than before. Painted transparent margins vary, so I cannot claim every creature is precisely seated on the cart rim; the solo moth still floats above it.
20. **FIXED.** `after1/trace-1366.png` shows the whole letter faintly under the active stroke; `final2/free-miss.png` shows all three M paths over the ink, numerically `fullModelPaths = expected = 3`.
21. **FIXED.** `corrective1/fixed-boards-1366.png` and `fixed-boards-680.png` use the vowel's awake lantern over the measured vowel position, with the same small/tall flame grammar as the vowel control. The old isolated CSS blob was replaced by the lantern-and-flame composition. Maximum measured center error is 0.00940 px, below 0.01 px at both named sizes.
22. **FIXED by Curiosity override.** There is no end card or Go to Village gate. Light all directly opens the still-interactive street; touching every letter does not trigger a finish. `last/street-wrap.png` and the demo-village audit state.
23. **FIXED.** A newly touched lantern can fly into its actual string slot when Street is opened; no completion step is involved. `flight.json` compares its CSS destination with the target slot, and `proof/flight-slot.png` shows the flight. Motion off omits movement.
24. **FIXED.** `final2/twins-1366.png` after a changed-letter tap: two amber-marked shops. Changed lanterns use amber glow/flicker; the cyan outline remains keyboard focus only. The calm grayscale frame keeps the same selection state without animation.
25. **FIXED.** `final2/twins-680.png` and `twins-800.png`: no floating "Find what changed" label or lit-count chip remains. The hint and every lantern target occupy separate regions.
26. **FIXED by Curiosity override.** The Say step and all reward stars were removed. Zero `.stars` nodes and zero rating widgets in `numbers.json`/`final-checks.json`; glow means touched, not learned.
27. **FIXED.** The disabled initial Hear it again was removed. `proof/default-1366-final.png` and `last/default-680.png` start with immediately playable lanterns and Read for the hint.
28. **FIXED.** The four legacy matching-question hints are named under `hint_only`, outside the recording `lines` array. Their matching quizzes were removed. The recording list equals the 187 strings returned by `allLines()`; no stale Find/quiz sentence is recorded.

#### Settled calls

Applied the Curiosity brief before lesson norms: no scored checks, answer-by-elimination tests or finish animation sequence. Kept flame shapes, both vowel anchors, the supplied art and word sets. Selected playful-friend. Reused isolated-sound sequence pieces rather than phonetic spellings in displayed text. At 680x425 the street hint does not name a hidden string. No welcome was added. Spec's open questions and the art provenance wording were left untouched.

Preserved the trace evaluator and immediately acting input. Read interruption was rechecked: a banner tap stops a running street turn and models the tapped word; no old word starts after the 4.2-second observation (`read-interrupt.json`). Settings has its own Read because the power panel is behind the modal drawer.

#### Cheats tried

- Before: check distractors restricted to the same three targets, allowing elimination. After: check and knowledge rating absent; no knowledge claim can be accumulated.
- Tap the same flame side repeatedly, then alternate both sides over 24 opens: both side orders observed; every tap only plays its selected sound model, with no progress, credit or end state.
- Always tap the longer word, then sweep both boards eight times: only the chosen words/vowels play. No rating fields or quiz widgets appear in the save.
- Tap every available option: objects are deliberately available from the start; touch glow makes no assessment claim. Direct access is the intended Curiosity behavior.
- The 100 non-dot stroke paths: 100 careful passes, zero backward, zero half-stroke and zero tap-only passes. Real held mouse drags with whole-pixel rounding and timing noise advanced small m, k and i. These verify a drawing aid, not a reading score.

#### Voice walk

Held clicks at a two-second pace, `voice-main.json`: letterName.m, anchor.m; another lantern tap replays its model; traceCap starts on Trace; Back returns directly; sign starts on Wordbook; twins starts on Twins. Taps cut stale speech immediately. There is no welcome or required route.

`voice-flames.json`: twoGlows once, shortLead then anchor.a; longLead then longSound.a. A short-vowel bare A never falls through to browser speech. `voice-teacher-final.json`: one automatic teacher how line across three openings; drawer Read includes teacher and privacy. Logs show starts/cuts, not listening approval. All 31 isolated takes remain unrecorded and unverified. No audio recording command was run.

#### Engine changes wanted

No kit change. The audit's `MODES_JS` searches only a header; a future shared-script change should also detect `nav button[aria-pressed]`. Explicit audit states currently cover this Curiosity's three views without adding a header.

#### Audit

One full audit completed once, within its 40-minute limit, on Chrome 9921 with host 8725. Its exact input is preserved as `audit-input.html`, `audit-input-src.html` and `audit-input.sha256`; results are `fix-audit/audit.md`. It reported 82 leads, grouped below. No full audit was rerun after the corrective pass; only the affected cases were re-shot and checked with the audit's page geometry checks.

- **47 overlap leads:** repaired by giving the hint its intrinsic width, fitting the vowel lantern to the work area, reserving caption space on compact slates, fitting compact word boards, separating phone street arrows from shop targets, and giving the 1000x625 street enough shop height. `corrective1/` and `corrective2/` contain same-size frames and JSON: zero overlap, clipped-text, small-target or below-fold findings in all affected states. Twins at 680x425 and both zero/full phone streets were included.
- **10 source-link target leads:** Manual links now measure at least 60x60 at 1366x768 and 375x812; the fixed minimum is shared at every size. See `fixed-manual-1366.json` and `fixed-manual-375.json`.
- **23 scroll notices:** intentional content catalogues and the scrolling Manual source appendix, not hidden short answer sets. The letter tray is keyboard reachable through q: at 680x425 its box is x=530..590, its focus is retained after Enter, and scrollLeft is 1185 (`catalogue-last-letter.json`). Main instrument controls remain outside that scroll list.
- **Two narration leads:** the Wordbook's deliberately invalid `stop` cue is logged dropped/stale because it only interrupts ordinary speech while protecting Read; it is not an unspoken event. A double tap may cut the one-time help line; the current hint and Read retain the instruction, with no gate or hidden next action. No welcome was added to satisfy the lesson-only table column.
- Motion off: no perpetual animations. Resize stress: no exceptions or controls left disabled. The held-click table reports no console errors and retains focus after rebuilding a selected lantern and after Enter twice. Read and Settings repeat/quick-tap checks are clean.

The final bundle is 3519187 bytes (about 3.36 MiB), retaining all 96 existing illustrations. The 2 MB figure is a goal; it remains below the 6 MB documentation threshold. The tool frame recorded zero external resource requests (`resource-proof.json`), and the final source scan finds no external resource tags. The browser/host processes started by this task were closed.

Verification-script note: an initial focused batch left the page-check placeholder unexpanded and returned null; a phone-only check also needed an iframe-evaluation wrapper correction. Those results were discarded and retried with valid measurements before any FIXED claim. No product error was hidden as a clean result.

#### The real material

No external corpus, chart image or audio was downloaded into the product. Existing Curio Class material remains bundled: 26 letters/creatures, 24 shop words, ten twin pairs, six vowel pairs, ten whole-word banners, 52 original geometric paths and 96 illustrations. `static-verification.json` verifies the counts and that every twin changes exactly one position. Original content: CC BY 4.0; code MIT; existing images generated with OpenAI gpt-image and edited for Curio Class.

References rechecked online 2026-11-06, with no article/book/chart text copied into the tool:

- Texas Education Agency, [The Alphabetic Principle, Reading Rockets](https://www.readingrockets.org/topics/phonics-and-decoding/articles/alphabetic-principle): sound-symbol distinction and undistorted stop models. Copyright retained, reference only; [Reading Rockets reprint policy](https://www.readingrockets.org/about).
- Moats and Tolman, [Six Syllable Types](https://www.readingrockets.org/topics/spelling-and-word-study/articles/six-syllable-types): open/closed vowel examples. Copyright retained, reference only. Moats, [Speech to Print, third edition, official excerpt](https://brookespublishing.com/wp-content/uploads/2020/02/TEXTBOOK-excerpt-w.toc-1.pdf): copyright 2020 Brookes, all rights reserved. The publisher/edition were verified; the public excerpt does not expose every relevant chapter, so I do not claim a fresh full-book check.
- NGA Center and CCSSO, [RF.K.3](https://www.thecorestandards.org/ELA-Literacy/RF/K/) and [L.K.1a](https://www.thecorestandards.org/ELA-Literacy/L/K/): identifiers used as references under the [CCSS Public License](https://www.thecorestandards.org/public-license/); no standards passage reproduced.
- [Zaner-Bloser manuscript chart](https://media.zaner-bloser.com/handwriting/pdfs/ZB_HW_Manuscript_Practice_Package.pdf) and [Learning Without Tears formation charts](https://www.lwtears.com/letter-number-formation-charts): independent comparison references for shared lines and letter forms; publishers retain copyright. No chart file or graphic is bundled.
- Dolch pre-primer and Fry first 100 remain the supplied brief's selection references. I removed the unsupported assertion that all banners were freshly checked against both complete lists. The product uses ten ordinary words in its own arrangement, with no copied full list and no invented open licence for Fry.

Sources and licence status are also in the Manual, notes and `tool.draft.json`. Unsupported mastery/glow probabilities, claims of assessment, q "almost always" generalization and full-list membership assertions were not retained. Contrast independently recomputed: cream/panel 15.32:1, dark word/sign 11.01:1, letter/glass 12.26:1, cyan focus/night 12.38:1.

#### Short test and lesson creep

Would a child open it voluntarily? Plausibly yes: the creature art and direct taps pay off immediately. Would an adult play? Word/shape comparison is pleasant, but sustained adult depth is uncertain. Is real sound the interface? Partially; anchor-word models work, but missing isolated recordings prevent an unqualified pass. Does it work without a score or finish? Yes, every view is directly accessible.

These are candid judgements from held-input exercises and inspected frames, not a claim of two completed human ten-minute play sessions. The side-by-side frame is `short-test-comparison.png`, using the final default and the played Beat Lab; `before3-contact.png` places the reference instruments together. The art is kept, while the lesson frame is removed.

Lesson-creep scan: score 0, level 0, goal 0, sticker 0, badge 0, correct 0, wrong 0, try again 0, complete 0, well done 0 in src.html. The 23 "points" hits are geometric point-array variable names in path sampling and tracing, not awarded points. No em dash or external resource tag. The bundle uses offline data; source links in the Manual are optional reference links.

#### Left open

- Refine blocker 1 remains acoustically open: 31 isolated clips and the selected bank's fixed narration need production and listening. The fallback avoids the original false sound model but is not a replacement for clean isolated recordings.
- Accepted polish 19: precise cart seating for every creature is not claimed.
- Neither the spec nor CURIOSITIES.md assigns Letter Lanterns a plate number or its own concept entry. I used an unnumbered engraved plate and `plate: null`, without inventing an owner decision.
- The Curiosity's authenticity/long-term-depth test is not an unqualified pass while isolated audio is absent.
- All tests used the authorized Chrome/host ports. Initial quick reads and a few one-line log tails lacked a separate process timeout; all bundle, browser and audit runs used hard limits. One early before-evidence batch overlapped a second Chrome batch, causing a driver reset on its last static-line probe; the relevant reproductions succeeded. Early phone hosts logged their own favicon 404; the wrapper was corrected and later proof batches were clean.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Letter Lanterns

#### Structure

This fix follows the user's Curiosity instruction over the older lesson-shaped spec and Refine. The village fills the screen, with its own wooden controls and power panel. There is no kit stylesheet, header, welcome gate, quiz, score, mastery rating, earned badge or end screen. The lower-left Manual contains operation, model limits, privacy, discoveries and named sources with licence status.

`src.html` uses the kit only for `Curio.voice`, tones, Motion, Sound and Read. `lesson.json` bundles the supplied names, words, letter geometry and art placement. All 96 existing illustrations remain available through their existing asset map. No new artwork or topic was added. `tool.draft.json` has `curiosity: true`; `plate` is null because neither the spec nor the concept catalogue assigns Letter Lanterns a Curiosity number. The engraved plate therefore omits an invented number.

The three freely selectable views are Lanterns, Street and Wordbook. The tray chooses any enabled letter or any supplied sign, twin pair, vowel pair or banner. Touching a letter lights it; this is an exploration mark, never a measure of knowledge. Settings can hide content, light all, or clear the village. No activity unlocks another.

#### Tricky parts

- `wordGlyph` renders a whole word in one SVG with fixed .85 advances, top line 0, midline .5, baseline 1 and descender 1.5. Signs, twins, vowel boards and banners use this layout. `glyph` may still crop a single isolated letter to fit a lantern's painted glass.
- Sound sequences are separate from displayed text. `intro.<letter>`, `short.<vowel>`, `long.<vowel>` and `twinDiff.<pair>` reference reusable `sound.<letter>` or `longSound.<vowel>` pieces. `resolveSequence` substitutes an anchor-word line if an isolated recording is unavailable; a bare consonant or short-vowel letter never falls through to browser TTS as its sound. All fixed narration remains in `voice/lines.json`, equal to `allLines()`.
- The voice manifest selects playful-friend / Laomedeia. No recordings were made. All 31 isolated sound recordings still need Forge production and listening approval. Queue logs prove routing and timing, not acoustic correctness. This remains the substantive limitation of Refine blocker 1.
- Twin windows always begin hidden on entering a pair, including previously opened shops. Both windows are freely revealable. The changed letter gets amber light and flicker; cyan is reserved for keyboard focus.
- The slate retains the reviewed direction, coverage, end and ordered-progress evaluator. It is an optional drawing aid. A matching stroke moves to the next trail; three misses can demonstrate the trail. Next stroke and Back to lantern are always available. No badge, score or required sequence is attached. A free-drawing miss overlays every path of the whole letter.
- Street lanterns have identical 60 by 80 hit boxes. Their string wraps with room reserved above the shops. Compact landscape and phone layouts hide the string and use a hint that does not name it. The 760 by 900 view shows all 26 in three rows.
- Version 2 local saves hold exploratory choices and touched/opened objects. Version 1 saves can retain touched letters and opened shops, with their former ratings discarded. Invalid saves start from the default village.
- Read owns the current hint. Settings Read includes its privacy line. Routine Settings narration is a how line, once per load; privacy stays visible and readable. Taps invalidate stale queued speech and act immediately. Mode changes cancel street reading.

#### Inspection and evidence

`window.__tool` exposes state, setMode, render, save, validSave, allLines, vlog, vq, data, assessTrace, resample, currentPath, slatePoint, wordGlyph, selectLetter, section, beginTrace, resolveSequence, sequences, reading and audioReady.

Before evidence, scripts, numerical results and after frames are under `_scratch/letter-lanterns/`. The unmodified source and data are preserved there. The final mechanical audit is `fix-audit/`. Read `polish.md` for item-by-item status and any audit limitations. Do not mistake an old lesson audit state or historical build report for the current interface.

The audit's automatic mode selector only searches headers. This tool has no header, so `audit-states.json` explicitly walks all three views and every material interaction, with real clicks. No shared audit script was changed.

#### Sources and rights

The Manual, teacher notes and `tool.draft.json` name the same source families and distinguish original Curio Class material (CC BY 4.0, code MIT) from copyrighted reference works. Reading Rockets, Speech to Print, CCSS, Zaner-Bloser and Learning Without Tears are references; their articles, books and chart images are not bundled. The supplied ten-banner selection is retained without copying a full Dolch or Fry compilation or asserting an open licence for Fry. No external dataset or artwork was downloaded into the product.

#### Sensitivity

Fictional village, no human figures, no personal prompts and no microphone. US English anchor words do not model every dialect. No cultural or medical claims were introduced.

#### Art still to paint

None. The existing art is retained. Isolated phoneme recording and listening review are separate from art.

#### Engine changes wanted

None in the kit. A future audit enhancement could include `nav button[aria-pressed]` in `scripts/audit_tool.py` `MODES_JS`, so Curiosity views are detected without a lesson header. The current explicit audit states cover them.

#### Left open

- Produce and listen to the 31 isolated sound clips and the fixed narration in the selected bank voice. No acoustic pass is claimed.
- Assign the Curiosity plate number outside this task; no number was supplied and none was invented.
- The four-question Curiosity test is a judgement, not a mechanical pass. The real sounds must be finished before the authenticity question can receive an unqualified yes.

#### Final audit and corrective verification

The full audit completed once with 82 leads. Its frozen input is preserved in Scratch as `audit-input.html` and `audit-input-src.html`, with SHA-256. After that audit, a focused corrective pass fixed the confirmed geometry and source-link targets. The full audit was not repeated. `corrective1/`, `corrective2/`, `final-hints/` and their JSON measurements cover the affected cases; `final-validation.json` records the final bundle hash. The source-link minimum is 60x60, and board lanterns are centered on the actual drawn vowel bounds to within 0.01 px. The final zero-letter hint distinguishes a fresh street from an already-opened shop, and all-hidden content keeps its Settings hint after resize.

Accepted polish 19 remains only partly addressed: height-based sizing is in place, but exact cart-rim seating for every creature is not approved. The 31 isolated recordings remain acoustically open. See `polish.md` for the complete per-item dispositions.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
