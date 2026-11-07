# Codex report: letter-lanterns

## Built

Built the two-mode kindergarten village from the kit starter: 26 letters, both letter forms, five vowel pairs, 24 shops, ten twin pairs, six open/closed pairs, ten banners, checks, Teacher controls and local progress. No family engine exists or was invented.

The real-input full campaign reached 26 lit letters, 24 open shops, ten banners and an independently earned m tracing badge. Source, data, manifest, notes, art and handoff are in the tool folder. The standalone bundle is `letter-lanterns.html`. Stage is built, status beta; it remains a draft because voice production is incomplete.

No git commit, deployment, submission, outreach or polish round. The report was written last to honor the user's stop instruction.

## Numbers check

- `numbers.py` independently confirms 26 letters, 24 three-letter CVC spellings, all five short vowels, ten twins with exactly one differing position: five first, three middle, two last.
- Event prerequisites and the three-event cap were recomputed. All shops unlock after their letters; twins follow both signs; the queue drains at lantern 25.
- All ten banners occur in both supplied Dolch pre-primer and Fry first-100 sets. The art list totals 96.
- Palette contrast: ink/panel 15.32:1; amber/panel 8.93:1; letter/glass 12.26:1; muted/panel 9.85:1; long flame 14.49:1; short flame 8.72:1; signs 12.56:1; focus/night 12.38:1. The long-flame value differs from the spec's 15.8. Actual amber-button text is 8.38:1.
- Seeded 40,000-run glow simulations per case: independent 80-percent first tries yield 40.23 percent bright after four per-letter checks and 91.06 after eight; one-third guesses yield 1.22 and 10.36 percent. Perfect answers reach bright after four; no answers never do. These are model assumptions, not classroom performance claims.
- The historical 200-run child-motor percentages cannot be reproduced exactly without their noise recipe. Current all-stroke tests separately verify careful and mildly shaky paths and the named attacks; no age-based accuracy claim is made.
- Box and fox have three-letter CVC spellings but four phonemes because x represents /ks/. They are not called three-phoneme CVC words.

## Facts checked

- The four phonics actions match RF.K.3a-d: primary consonant sounds, vowel sounds, high-frequency words by sight, and different sounds in similarly spelled words. [Common Core kindergarten reading](https://www.thecorestandards.org/ELA-Literacy/RF/K/).
- Capital/small printing is supporting work for L.K.1a, with its module assignment left to Sentence Train. [Common Core kindergarten language](https://www.thecorestandards.org/ELA-Literacy/L/K/).
- The 26 mappings and anchors follow the supplied Moats/Reading Rockets table. C and g use their common hard sounds, x is final /ks/, and q is modeled with u. The phonics reference explicitly treats x as two sounds. [Reading Rockets phonics scope and sequence](https://www.readingrockets.org/sites/default/files/2023-10/NJTSS%20Phonics%20Scope%20and%20Sequence.pdf). The complete Moats book was not reread.
- All five short/name-sound anchor pairs and six open/closed examples were checked against the supplied word table and syllable definitions. [Reading Rockets syllable types](https://www.readingrockets.org/topics/spelling-and-word-study/articles/six-syllable-types). Direct article access returned 403; its indexed primary-source text was available.
- All ten sight words were checked against the supplied Dolch/Fry catalog with Python. Banners are modeled as whole words and have no letter-sound buttons.
- Stroke order is the spec's manuscript model, not a universal handwriting rule. Publisher formation resources were checked; exact paths were copied and sampled from the spec. [Zaner-Bloser practice models](https://media.zaner-bloser.com/handwriting/pdfs/ZB_HW_Manuscript_Practice_Package.pdf), [Learning Without Tears formation resources](https://www.lwtears.com/letter-number-formation-charts).
- Final-e instruction stays outside this tool, consistent with RF.1.3c. [Common Core grade-one reading](https://www.thecorestandards.org/ELA-Literacy/RF/1/).
- Privacy was checked in code: localStorage only for progress/settings, no microphone or page network calls. Teacher states that nothing leaves the device.

## Break it

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

## Voice walk

The complete manifest has 308 distinct fixed lines, warm-teacher/Sulafat, plus 31 isolated-sound production entries with IPA, three-take requirements and unreviewed status. No audio was recorded under the Build prohibition. Runtime currently uses kit browser fallback.

Held-click main walk: untouched start logs `welcome`, then `find.m`; wrong s remains asleep and logs its sound/question; correct m enters Say; the sound tap enables Next; Next enters capital tracing. A real mid-trace reload preserves letter, case and stroke. The full campaign covers every event type.

Five wrong Finds at two-second intervals logged welcome once, wrong.s five times, and find.m after each miss. No repeated how-to nag. The side walk enters Village, uses Read, returns to Wake, and replays the current question. Read wins over queued speech; mode changes can explicitly hush it.

These are muted-Chrome start logs, not listening validation. Clean consonant stops, short vowels, long vowels, phoneme-bearing questions and the chosen bank voice remain unverified by ear. Done when 9 fails.

## Feel check

Best moment: a completed letter lifts to the string, then the first readable map sign opens into a warm shop with its painted goods. The eventual street is a concrete record of the session.

Flattest moment 1: a small generic letter panel weakened the creature reveal. Letters now sit in each painting's actual glass, awake creatures are sized up for the single-letter scene, and sleepy/awake poses are matched edits.

Flattest moment 2: the street initially had crowded targets and looked disconnected from the unlock scenes. It now has a real four-section panorama, separated arrow lanes, sleeping window lanterns, banners above grounded fronts, and event views that move to their street quarter. Optional writing adds a distinct earned badge.

Played the full progression through real pointer input, with a separate keyboard letter and wrong-answer walks. No child classroom trial was performed. `feel-comparison.png` places the final Village beside Snowy Mail Route; Beat Lab was also opened. This is visually richer than the bar, with substantial progression; voice quality prevents a release-ready feel claim.

## Done when

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

## Wave lessons

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

## Audit leads

One complete audit, within its 40-minute cap, reported 90 raw leads. Its original `audit.md` and 67 PNGs are retained. It was not rerun wholesale.

- 82 state/layout leads: scene/arrow/title bounds, wrapped string coverage and the reset overlay. Fixed by fitted shop bounds, reserved title space, compact count chips, wrap-aware layout, reset hints and explicit inertness of the covered Teacher dialog. Targeted checks using the same measurement code are clean at the affected sizes, including 375.
- Seven welcome flags: accepted under BASELINE rule 16 and the spec's tap-specific entry behavior. Teacher/direct lantern taps have their own lines; Wake-tab/Motion taps do not start the lesson; the explicit begin sequence is logged as how rather than the helper's welcome kind. The untouched start sequence was independently verified.
- One rapid Village-welcome cut: accepted because an intentional mode change hushes it. The current premise/action remains available through Read.
- Resize and Motion-off stages were clean. Held-click repetition was clean. Completed drive/behavior/quiz checks report no browser console errors, warnings or exceptions. Early iframe-context/favicon and reload-assertion failures were test-harness errors and were corrected.

## Frames looked at

All captured PNGs were opened individually or on labeled contact pages. This includes the 67 audit frames, required-size sweep, both modes, every event type, Teacher/reset, phone twins, guided/free writing, mixed glow, grayscale, keyboard and targeted repairs. Scratch contact manifests enumerate them. Final high-resolution art and the panorama crop were also inspected.

Key evidence: `playthrough/result.json`, `behavior/checks.json`, `trace-checks.json`, `quiz-attacks.json`, `long-pair-attacks.json`, `choice-invariants.json`, `free-next-final.json`, `no-glow-cue.json`, `village-resume.json`, `measure-*.json`, `audit/audit.md`, and `feel-comparison.png`.

A final Village-check regression found that checking could replace an interrupted Wake lesson. Flow snapshots now preserve it while retaining earned glow. Focused Find and partial small-letter trace runs both completed the check and resumed at the original letter, case and stroke. The final frame was inspected.

## Art made

96 final images from 97 generations, including one street redraw: 52 creature poses, five anchors, 24 goods, two scenes, 12 fronts and one banner. Every asset is used. People: zero. All carry drawn_by codex and the OpenAI illustration credit.

Final art: 1720.1 KB. Voice: 0 KB. Bundle: 2705.4 KB, against the 2,048 KB goal. Quality is 72; backgrounds were reduced once. Awake creatures retain 420-pixel detail for their largest use, fronts 240 and the large banner 500. The teaching art was retained rather than removed to meet the goal. Full prompts and raw originals are preserved.

## Art still to paint

None. Phoneme audio production/listening review is still required, separately from art.

## Engine changes wanted

None. Kit, family engines, scripts and docs source were not edited.

## Left open

- The 31 clean isolated clips and all phoneme-bearing narration need listening review. This beta must not be presented as a validated solo phonics model yet. The named voice conflicts with the neighbor's stated voice; the explicit warm-teacher selection was retained.
- Historical child-motor pass percentages were not reproduced from an unspecified noise recipe. No classroom or child trial was performed.
- Literal off-letter event dropping is implemented. Re-enabling after a dependent event was dropped does not backfill it; that edge needs a reviewer decision. The default all-on campaign is complete.
- Scope deviation: following the reference-bundle instruction regenerated the two git-ignored bar-tool HTML bundles outside the user's write allowlist. No sibling source was edited and no outside-scope revert was attempted.
- Initial read-only inspection commands lacked hard process timeouts. Subsequent build/check commands used the bounded Scratch runner. No command hit its time cap.
- `host.html` is absent. The Chrome instances and servers started for this build are closed. No polish round or git commit was started.
