# Polish: letter-lanterns (Codex fix, round 1)

Curiosity override: the supplied spec and Refine describe a lesson path. The user's instruction and CODEX-CURIOSITY.md win. I removed the quiz/check ladder, star ratings, earned badges, forced sequence, welcome gate, end card and kit header. The same supplied letters, words, art and tracing mechanics are freely explorable. For a removed lesson-only interaction, FIXED below means its defect was eliminated by that removal; it does not claim the requested quiz was built.

Evidence paths below are relative to `_scratch/letter-lanterns/`. I inspected the individual frames and contact sheets named here. The original source and data are retained as `src-before.html` and `lesson-before.json`. `refine.md`, `refine/` and `spec.md` were not edited; no git commit was made. All work was inside the two authorized folders.

## Blocker

1. **NOT FIXED acoustically.** Before: `before2/S07-S08-say.png` and its voice log showed the instruction before the bare-letter sentence; the original line table includes `find.t`, `intro.a`, `short.a`, `twinDiff.0` exactly as reported. The new sequence table references reusable isolated `sound.<letter>` pieces; long vowels reference `longSound.<vowel>`. Missing isolated clips use a whole anchor-word fallback rather than reading a letter name as a short sound. `numbers.json` and `voice-flames.json` prove routing; `audioReady = 0`. There are no recordings to listen to, so neither clean stops nor all 31 clips can be approved. The direct pre-fix Find-t/a table probe did not finish because an overlapping driver batch reset Chrome; I confirmed those strings in the original source, not by a completed acoustic walk. The removed Find/wrong quiz sentences are not recorded. Forge production and listening remain open, as Refine's settled call anticipates.
2. **FIXED.** Before `before1/B02-sign-680.png`, `before1/B02-twins-1366.png`, `before2/B02-twins-375.png`: each letter had a different cropped viewBox. After `final1/sign-680.png`, `final2/twins-1366.png`, `final2/twins-375.png`: each whole word shares one SVG, .85 advance, y=0/.5/1/1.5. The p, i and g translations are `(0,0)`, `(.85,0)`, `(1.7,0)`; p/g retain their descenders. The same function draws all signs, boards and banners.
3. **FIXED by Curiosity override.** Before `before2/B03-choice-pool.png`: ten sampled checks offered only m/s/a. The check and its rating accumulation were removed. `final-checks.json` records zero check/rating widgets and no rating fields after repeated taps. An exploration mark no longer claims sound knowledge.

## Should fix

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

## Polish accepted

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

## Settled calls

Applied the Curiosity brief before lesson norms: no scored checks, answer-by-elimination tests or finish animation sequence. Kept flame shapes, both vowel anchors, the supplied art and word sets. Selected playful-friend. Reused isolated-sound sequence pieces rather than phonetic spellings in displayed text. At 680x425 the street hint does not name a hidden string. No welcome was added. Spec's open questions and the art provenance wording were left untouched.

Preserved the trace evaluator and immediately acting input. Read interruption was rechecked: a banner tap stops a running street turn and models the tapped word; no old word starts after the 4.2-second observation (`read-interrupt.json`). Settings has its own Read because the power panel is behind the modal drawer.

## Cheats tried

- Before: check distractors restricted to the same three targets, allowing elimination. After: check and knowledge rating absent; no knowledge claim can be accumulated.
- Tap the same flame side repeatedly, then alternate both sides over 24 opens: both side orders observed; every tap only plays its selected sound model, with no progress, credit or end state.
- Always tap the longer word, then sweep both boards eight times: only the chosen words/vowels play. No rating fields or quiz widgets appear in the save.
- Tap every available option: objects are deliberately available from the start; touch glow makes no assessment claim. Direct access is the intended Curiosity behavior.
- The 100 non-dot stroke paths: 100 careful passes, zero backward, zero half-stroke and zero tap-only passes. Real held mouse drags with whole-pixel rounding and timing noise advanced small m, k and i. These verify a drawing aid, not a reading score.

## Voice walk

Held clicks at a two-second pace, `voice-main.json`: letterName.m, anchor.m; another lantern tap replays its model; traceCap starts on Trace; Back returns directly; sign starts on Wordbook; twins starts on Twins. Taps cut stale speech immediately. There is no welcome or required route.

`voice-flames.json`: twoGlows once, shortLead then anchor.a; longLead then longSound.a. A short-vowel bare A never falls through to browser speech. `voice-teacher-final.json`: one automatic teacher how line across three openings; drawer Read includes teacher and privacy. Logs show starts/cuts, not listening approval. All 31 isolated takes remain unrecorded and unverified. No audio recording command was run.

## Engine changes wanted

No kit change. The audit's `MODES_JS` searches only a header; a future shared-script change should also detect `nav button[aria-pressed]`. Explicit audit states currently cover this Curiosity's three views without adding a header.

## Audit

One full audit completed once, within its 40-minute limit, on Chrome 9921 with host 8725. Its exact input is preserved as `audit-input.html`, `audit-input-src.html` and `audit-input.sha256`; results are `fix-audit/audit.md`. It reported 82 leads, grouped below. No full audit was rerun after the corrective pass; only the affected cases were re-shot and checked with the audit's page geometry checks.

- **47 overlap leads:** repaired by giving the hint its intrinsic width, fitting the vowel lantern to the work area, reserving caption space on compact slates, fitting compact word boards, separating phone street arrows from shop targets, and giving the 1000x625 street enough shop height. `corrective1/` and `corrective2/` contain same-size frames and JSON: zero overlap, clipped-text, small-target or below-fold findings in all affected states. Twins at 680x425 and both zero/full phone streets were included.
- **10 source-link target leads:** Manual links now measure at least 60x60 at 1366x768 and 375x812; the fixed minimum is shared at every size. See `fixed-manual-1366.json` and `fixed-manual-375.json`.
- **23 scroll notices:** intentional content catalogues and the scrolling Manual source appendix, not hidden short answer sets. The letter tray is keyboard reachable through q: at 680x425 its box is x=530..590, its focus is retained after Enter, and scrollLeft is 1185 (`catalogue-last-letter.json`). Main instrument controls remain outside that scroll list.
- **Two narration leads:** the Wordbook's deliberately invalid `stop` cue is logged dropped/stale because it only interrupts ordinary speech while protecting Read; it is not an unspoken event. A double tap may cut the one-time help line; the current hint and Read retain the instruction, with no gate or hidden next action. No welcome was added to satisfy the lesson-only table column.
- Motion off: no perpetual animations. Resize stress: no exceptions or controls left disabled. The held-click table reports no console errors and retains focus after rebuilding a selected lantern and after Enter twice. Read and Settings repeat/quick-tap checks are clean.

The final bundle is 3519187 bytes (about 3.36 MiB), retaining all 96 existing illustrations. The 2 MB figure is a goal; it remains below the 6 MB documentation threshold. The tool frame recorded zero external resource requests (`resource-proof.json`), and the final source scan finds no external resource tags. The browser/host processes started by this task were closed.

Verification-script note: an initial focused batch left the page-check placeholder unexpanded and returned null; a phone-only check also needed an iframe-evaluation wrapper correction. Those results were discarded and retried with valid measurements before any FIXED claim. No product error was hidden as a clean result.

## The real material

No external corpus, chart image or audio was downloaded into the product. Existing Curio Class material remains bundled: 26 letters/creatures, 24 shop words, ten twin pairs, six vowel pairs, ten whole-word banners, 52 original geometric paths and 96 illustrations. `static-verification.json` verifies the counts and that every twin changes exactly one position. Original content: CC BY 4.0; code MIT; existing images generated with OpenAI gpt-image and edited for Curio Class.

References rechecked online 2026-11-06, with no article/book/chart text copied into the tool:

- Texas Education Agency, [The Alphabetic Principle, Reading Rockets](https://www.readingrockets.org/topics/phonics-and-decoding/articles/alphabetic-principle): sound-symbol distinction and undistorted stop models. Copyright retained, reference only; [Reading Rockets reprint policy](https://www.readingrockets.org/about).
- Moats and Tolman, [Six Syllable Types](https://www.readingrockets.org/topics/spelling-and-word-study/articles/six-syllable-types): open/closed vowel examples. Copyright retained, reference only. Moats, [Speech to Print, third edition, official excerpt](https://brookespublishing.com/wp-content/uploads/2020/02/TEXTBOOK-excerpt-w.toc-1.pdf): copyright 2020 Brookes, all rights reserved. The publisher/edition were verified; the public excerpt does not expose every relevant chapter, so I do not claim a fresh full-book check.
- NGA Center and CCSSO, [RF.K.3](https://www.thecorestandards.org/ELA-Literacy/RF/K/) and [L.K.1a](https://www.thecorestandards.org/ELA-Literacy/L/K/): identifiers used as references under the [CCSS Public License](https://www.thecorestandards.org/public-license/); no standards passage reproduced.
- [Zaner-Bloser manuscript chart](https://media.zaner-bloser.com/handwriting/pdfs/ZB_HW_Manuscript_Practice_Package.pdf) and [Learning Without Tears formation charts](https://www.lwtears.com/letter-number-formation-charts): independent comparison references for shared lines and letter forms; publishers retain copyright. No chart file or graphic is bundled.
- Dolch pre-primer and Fry first 100 remain the supplied brief's selection references. I removed the unsupported assertion that all banners were freshly checked against both complete lists. The product uses ten ordinary words in its own arrangement, with no copied full list and no invented open licence for Fry.

Sources and licence status are also in the Manual, notes and `tool.draft.json`. Unsupported mastery/glow probabilities, claims of assessment, q "almost always" generalization and full-list membership assertions were not retained. Contrast independently recomputed: cream/panel 15.32:1, dark word/sign 11.01:1, letter/glass 12.26:1, cyan focus/night 12.38:1.

## Short test and lesson creep

Would a child open it voluntarily? Plausibly yes: the creature art and direct taps pay off immediately. Would an adult play? Word/shape comparison is pleasant, but sustained adult depth is uncertain. Is real sound the interface? Partially; anchor-word models work, but missing isolated recordings prevent an unqualified pass. Does it work without a score or finish? Yes, every view is directly accessible.

These are candid judgements from held-input exercises and inspected frames, not a claim of two completed human ten-minute play sessions. The side-by-side frame is `short-test-comparison.png`, using the final default and the played Beat Lab; `before3-contact.png` places the reference instruments together. The art is kept, while the lesson frame is removed.

Lesson-creep scan: score 0, level 0, goal 0, sticker 0, badge 0, correct 0, wrong 0, try again 0, complete 0, well done 0 in src.html. The 23 "points" hits are geometric point-array variable names in path sampling and tracing, not awarded points. No em dash or external resource tag. The bundle uses offline data; source links in the Manual are optional reference links.

## Left open

- Refine blocker 1 remains acoustically open: 31 isolated clips and the selected bank's fixed narration need production and listening. The fallback avoids the original false sound model but is not a replacement for clean isolated recordings.
- Accepted polish 19: precise cart seating for every creature is not claimed.
- Neither the spec nor CURIOSITIES.md assigns Letter Lanterns a plate number or its own concept entry. I used an unnumbered engraved plate and `plate: null`, without inventing an owner decision.
- The Curiosity's authenticity/long-term-depth test is not an unqualified pass while isolated audio is absent.
- All tests used the authorized Chrome/host ports. Initial quick reads and a few one-line log tails lacked a separate process timeout; all bundle, browser and audit runs used hard limits. One early before-evidence batch overlapped a second Chrome batch, causing a driver reset on its last static-line probe; the relevant reproductions succeeded. Early phone hosts logged their own favicon 404; the wrapper was corrected and later proof batches were clean.
