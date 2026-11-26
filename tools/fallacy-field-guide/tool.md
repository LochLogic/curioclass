# Fallacy Field Guide: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: fallacy-field-guide

#### Built

Built Field, Guide and Make one as one offline HTML file, with all 24 specimens, eight collectible species, persistent sightings and slips, keyboard word marking, field tests and guarded reset dialogs. Metadata remains tool.draft.json, stage built, status beta. No commit or polish round.

The final bundle is 959.5 KB, including 11 generated images totaling 621.6 KB and 0 KB of recorded voice. Its bytes match the repair bundle checked in Scratch. Source has 1,391 readable lines, maximum 158 characters. Hashes and checks: _scratch/fallacy-field-guide/final-stats.json.

All build and verification subprocesses had explicit limits: bundles 120 seconds, drive batches 300 seconds, audit 2,400 seconds. The single audit completed with exit 0 within that cap. All helpers returned, host.html is absent, and ports 8795 and 9990 through 9993 were closed at the final socket check. Windows denied the optional CIM process inventory; this is recorded rather than presented as a successful enumeration.

#### Numbers check

Recomputed from the supplied spec before implementation: 24 specimens; eight species, each with two fallacies and one fair twin; field marks of 4 to 13 words; half-mark thresholds of 2 to 7 words. All whole-text selections exceed five extra words. F3, F9, F21 and F22 each have exactly six extra words, so they fail with Narrow it. No numerical discrepancy found.

Recomputed contrast: white/brand 7.02, brand/paper 5.78, brand/panel 6.49, ink/paper 13.22, muted/paper 6.25, muted/panel 7.02, focus/paper 5.30, Legit/panel 6.02, fallacy/panel 6.81. All nine match the spec to 0.01. Evidence: numbers.json and contrast.json in Scratch.

#### Facts checked

Definitions, diagnostic questions and fair uses were checked against [Bradley Dowden, Fallacies, Internet Encyclopedia of Philosophy](https://iep.utm.edu/fallacy/), opened during this build. Each visible definition uses the supplied paraphrase, with these distinctions:

| Species | Checked distinction |
|---|---|
| Ad hominem | Irrelevant personal criticism versus a relevant reliability concern. |
| Straw man | Distorted restatement versus a fair summary. |
| Black-or-white | An unfairly limited menu versus an actual binary choice. |
| Slippery slope | An unsupported chain versus supported steps. |
| Hasty generalization | Too few or biased cases versus a substantial fair sample. |
| Unqualified authority | Expertise outside the question versus relevant expertise. |
| Bandwagon | Popularity used for quality or truth versus popularity itself. |
| Post hoc | Sequence alone versus a comparison addressing other differences. |

F1-F24, all names, brands, places, times, money amounts, sample sizes and percentages are fictional content supplied by spec.md, not real statistics or findings. The numbers in F3, F13, F14 and F18 do not represent medical guidance, a real transit schedule or actual studies. All 24 texts and keyed marks were checked in the supplied data and the UI walk.

Content issues retained for review: F10's no-staff detail was added to its fictional story context from F10 itself. F13 assumes the transit office checked the timetable; distance alone cannot prove a missed connection. F15's field note mentions health although the specimen states sales and implies quality. F23 needs the dentist's title to be read as offered evidence, rather than an ordinary personal preference. These boundaries are in handoff.md and notes.md; the provided keys were retained.

#### Break it

| Check or record | Cheapest attack tried and result |
|---|---|
| Word-mark check | Whole-text selections on all 24 failed. Exact half passed; one word below half failed. Named six-extra cases failed. |
| Species and Legit calls | All eight species alternatives and inverted Legit calls were tested for every specimen. Only the keyed call passed. |
| Enumeration | Correct mark, two wrong species, then the right species: Studied, not counted. Attempts and assistance persist across reload. This is an explicit change to close the free-enumeration loophole. |
| Sightings count | Repeated Log on F2 remained one counted sighting and one Spotted card; no duplicate credit. |
| Confirmation | Fallacy alone was Spotted. Only the correctly released twin confirmed it. A studied twin could not confirm. All eight pairs were tested. |
| Edited calls | Editing F3 removed its sighting from the count. Previously earned Confirmed status stayed, as specified. |
| Field test | Selecting Hasty generalization on F1 displayed that question and its suggestions, not F1's key. The pure test never consults specimens. |
| Make one gate | Empty slips and a seven-word slip kept the test disabled. Both slips needed a finished mark. |
| Make one result | Eight repeated words plus favorable answers reached a visibly labeled self-check, earned no cards and set no verified score. Free writing is not semantically validated. |
| Storage | Sightings, confirmation and marked slips survived reload. A forced storage exception was caught and reported as current-tab-only storage. |
| Reset | Cancel preserved confirmation. Confirm cleared sightings, marks and stamp, disabled Log, and preserved the writing slips. |

Evidence: 368 passing assertions in pure-node-results.json and pure-results.json; functional-fixed, whole-student, final-gates, post-audit and last-repairs frames/results. The complete held-click UI walk logged 24 and confirmed eight. Bounded attempts stop guaranteed option cycling; they do not establish mastery or eliminate lucky guesses.

#### Voice walk

Curio.voice owns the queue, Read, Sound and scope. 42 unique lines are prepared for the kept gravel-ranger / Algenib bank voice. No speech was recorded, as required for Build; runtime uses browser speech. Verification reads speech-start logs, not the audible quality of a bank recording.

Main path used held 120 ms clicks, two seconds apart: F2, its two endpoints, Authority, Log, F3, its endpoints, Legit, Authority, Log, Guide, Make one. The repaired walk heard, in order: mark instruction, last word, pick species, Log instruction, Logged, Legit lookalike instruction, Logged, Authority confirmed, Guide welcome, Make one welcome. The Field welcome may be skipped by the first action under BASELINE rule 16. Its direction remains in the hint and Read.

The first walk exposed the Legit instruction waiting behind stale how-to speech. New step instructions now use the kit's immediate queue option and V.heard; both Logged events start. Mode/specimen changes cut stale lines as intended. A final mode-entry walk heard the revised Make one welcome, which asks for writing rather than naming a disabled test.

Side path wrote and marked two slips, answered both questions and closed the result. Hints advanced to enabled controls and restored after closing. Two taps 0.7 seconds apart on the same habitat now let its still-valid instruction finish. Repeated word taps complete or change the mark, so their obsolete instruction gives way to the next step. See voice-modes-fixed-results.json, mode-welcomes-final-results.json and same-habitat-quick results.

#### Feel check

Played the complete collection path through real UI controls, then wrote and tested the two slips. Best moment: the peacock becomes a colored Confirmed plate with its pressed flower after F3 is released, and the final book records three sightings for each of eight species.

Two flattest early moments were the anonymous F-number rail and the chat looking like another paper poster. The rail now includes specimen openings at roomy sizes; thread, feed and chat have distinct framing, and chat sits inside the large painted phone screen. Marking responds immediately with ink-colored focus and a highlighted passage; stamps land without locking input.

Looked at the tool beside Beat Lab and also opened Snowy Mail Route. The comparison is _scratch/fallacy-field-guide/bar-comparison.jpg. The watercolor collection has comparable visual care and its own restrained finish. Its replay value is the remaining twins and revised writing; it is a finite 24-case investigation.

#### Done when

| Spec item | Result and evidence |
|---|---|
| 24 specimens in four distinct habitats | PASS: whole-student UI walk, 24 logged; board, thread, feed and chat frames. |
| F3 Legit/Authority and wrong-Authority hint | PASS: confirmed-path and expert-miss results. |
| Half-mark and six-extra boundaries | PASS: 368 assertions and independently counted ranges, including all four named whole-text traps. |
| F2 Spotted, F3 Confirmed | PASS: side/rapid-stamp and functional-fixed/confirmed-path. |
| Field test selected question without key | PASS: field-test frame and all eight pure test comparisons. |
| Make one runs both tests from own answers | PASS: make results and nonsense-self-check; explicitly self-reported. |
| Persistence and reset confirmation | PASS: both reload records, cancel/confirm records and reset-field-final. |
| 375 bottom kit, no sideways scroll; 680 full specimen and kit | PASS: hosted 375 width equals 375 scroll width; phone long logged case and compact longest-headline frames. |
| Selected specimen largest; Guide plates/silhouettes | PASS: 1366 and 680 frames, full collection and Guide views. |
| Taps during stamp or card reveal work immediately | PASS: rapid-stamp queue empty; finite animations finish on interaction. |
| Waiting directions and repeated Logged | PASS with repairs: final speech logs and dialog-close records. |

The separate project-wide 44-pixel requirement for individual word targets remains FAIL, below. This table does not claim all mechanical checks pass.

#### Wave lessons

| BUILD.md lesson | Result |
|---|---|
| Hint and voice | PASS: immediate mode/step hints, Read uses the active hint; final two-second walk and dialog-close checks. |
| Focus and layout | PASS: no focus on load; Go to it focuses its specimen button with preventScroll; controls keep their DOM nodes. |
| Sizes and targets | PARTIAL / FAIL: all listed viewports examined; action buttons fit. Individual inline word targets are below 44 pixels. |
| No giveaways | PASS: no percentages or hidden-key badge in the UI; option cycling cannot earn a card after two misses. |
| Honest numbers | PASS: counts are unique keyed sightings; confirmation history is explained; self-check is labeled as judgment. |
| Standards | PASS: solo marking, classification, twin comparison and authored examples practice RI.9-10.8 reasoning and evidence. |
| Motion off | PASS: zero running infinite animations in the calm frame and audit. |
| Short choice sets in view | PASS for Field and 760 Guide after repair. The explicit 375 one-card-per-row Guide requires vertical scrolling. |
| Resize mid-animation | PASS: completed audit stress found no exceptions or stranded disabled controls. |
| No late welcome | PASS: welcomeAfter is unused; first actions may replace the welcome, as BASELINE 16 permits. |
| Unknown shown as unknown | PASS: Unseen guide plates are silhouettes; no earned stamp or flower appears before its condition. |
| One look, one meaning | PASS: species glyphs and plates match across kit, book and picker; stamps also name their call. |
| Badge says what is true | PASS: duplicate and studied calls cannot inflate counts; sticky historical confirmation is explicit. |
| Hint changes back | PASS: Field test and Make one close paths restore the mode's next action; reset refreshes the Field view. |
| No answer by copying words | PASS: classification needs the reasoning span and call; Field test gives a general diagnostic, not a specimen key. |

#### Audit leads

Ran audit_tool.py once, last among the broad checks, with Chrome 9991, host 8795 and a 40-minute cap. It completed, exit 0, with 777 leads and 92 frames. Its original input remained fixed while repairs were tested in a separate Scratch bundle, then transferred byte-for-byte. No second full audit was run.

| Lead class, covering every repeated instance | Disposition |
|---|---|
| Small Field tab, 43 pixels | Fixed: minimum 44; measured in make-680-final. |
| Small span.word targets | OPEN / FAIL: continuous text targets are smaller than 44. Kept semantic buttons and the full arrow-key/Enter route; did not lower the audit threshold or hide the controls. |
| Hidden #hint in Guide/Make and their dialogs | Probe assumption: these modes have visible #guide-hint and #make-hint. The kit's documented read callback selects the active instruction. Close restores it. |
| Guide cards cut short at 760 | Fixed: all eight now end at or above 806.7 in a 900-high viewport. |
| Guide scroll at 375, also behind dialogs | Intentional one-card-per-row gallery required by spec. Dialog backgrounds are inert. This conflicts with a literal all-choices-in-view rule; retained the explicit phone gallery. |
| Unnamed textareas and label overlap | Fixed: explicit aria-labels plus block labels with separation. Checked on laptop, compact and phone frames. |
| Make welcome names disabled test | Fixed: welcome asks for eight words; writing and marking hints advance only to available controls. Topic chips also avoid disabled marking instructions. |
| Long-comment word overlaps at 1920 | A hyphenated inline word produced a multi-line union rectangle. Fixed with individual inline boxes; checked the intact no-staff word at 1920. |
| Phone second-slip steps not found, lost focus and footer overlap | Fixed with compact phone slips. Both Edit controls end before 665; Field test ends at 802 in height 812. Both marks enable the test; no sideways overflow. |
| First-tap welcome not heard | Allowed by BASELINE rule 16; per-action instruction, visible hint and Read remain available. |
| Four same-habitat quick-tap speech cuts | Fixed: active habitat/specimen taps preserve valid speech and work. Both targeted quick-tap walks finished without a cut. |
| Quick word-tap cut | Expected state advance: the second tap finishes the mark and replaces the last-word direction with the next action. |
| Active-mode no-op and movement counts on switches/Sound | Current mode preserves work; mode switches redraw their view, and Sound changes its label. No dead action or focus loss was found in the completed walk. |

The completed audit reported clean Motion off and resize stress. Five-click checks were clean for the listed controls. Raw evidence remains _scratch/fallacy-field-guide/audit/audit.md; all its state frames were inspected in contact sheets, with flagged layouts also opened full size.

#### Frames looked at

Every generated PNG was inspected directly or on a contact sheet. Bar frames: bar-beat and bar-snow. Build frames: early, functional and functional-fixed, whole-student, side, sizes, extra, phone, targeted, post-audit, final-gates, phone-repaired, label-check, label-check-final and last-repairs. Superseded selector-failure frames are preserved and identified as failures, not passes.

All STANDARDS sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and hosted 375x812. Also checked grayscale, calm mode, a real Tab/arrows/Enter whole call, all modes, open dialogs, long specimens, confirmation and two-slip results. Audit contact sheets cover its 92 PNGs; art-sheet.jpg covers every finished asset.

#### Art made

11 images made during this build with the built-in image tool: goose, scarecrow, magpie, snail, hare, peacock, ducklings, rooster, pressed flower, cork and phone. One ink-and-watercolor house style, all people:false and drawn_by:codex. No redraws were needed after inspection.

Full prompts: art/prompts.json. Raw originals: art/raw. Finished files: art/*.webp, 621.6 KB total. art.py ran only with --rekey. The available Python lacked numpy, so the same processor used compatible existing local site-packages. No package installation, downloaded art, paid art.py generation or audio recording.

Final bundle: 959.5 KB against the 2 MB goal; recorded voice 0 KB. Credits are in tool.draft.json and the source comment. The animal plates, cork and phone are used at substantial scene/book sizes, with the flower marking actual confirmation.

#### Art still to paint

None.

#### Engine changes wanted

kit/fallacies.js is absent. The marked local pure block exposes spot, test and cards as __tool.fx; habitat rendering remains in the tool. When the shared-engine baseline is met, create the missing factory using catalog, specimens and the five-extra-word limit, and return those APIs. No kit, docs or scripts were edited. Details are in handoff.md.

#### Left open

- Individual word targets do not meet the project's 44-pixel rule. This needs an explicit design decision that preserves readable passages and compact play; the keyboard route is verified.
- F13, F15 and F23 need the content judgments described above. F15 is the clearest mismatch between text and keyed field note. Original specimen text and keys were retained.
- Make one remains a self-check, not semantic validation of free writing. It awards no confirmed cards or verified grade.
- The named bank voice is prepared, not recorded. Browser speech is the Build fallback.
- Scope error: the required bar-tool bundling step regenerated the ignored snowy-mail-route.html and beat-lab.html outside the two allowed folders. No source outside the allowed folders was edited. Subsequent writes stayed in the named tool and Scratch.
- Initial read-only shell calls used tool wait limits rather than explicit termination wrappers. All later build/check commands used explicit timeouts.
- Historical verification failures: selector quoting in the first recipe, one lost Chrome connection in a parallel size batch, and a favicon 404 in the original host wrapper. Corrected smaller/targeted runs passed; the repaired phone host had zero console errors. Windows denied CIM enumeration; helper cleanup completed and all used host/CDP ports were verified closed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: fallacy-field-guide

#### Played

Cold Grade 10 solo sampling covered all habitats, one caught/released pair, the collected guide and drafting/marking a writing slip before builder notes/source. The complete 24-case validation and finished two-slip self-check followed the source read, so this was not a full 24-case cold completion. Strong notebook identity; the peacock confirmation is the best moment. Also checked the projector/compact path.

#### Findings fixed

- Should fix, general, Make one: 4,000-character marked slips put Field test it at y=2623 on a 768-high laptop. Bounded passages now keep it at y=670; phone action bar remains visible. Arrow navigation scrolls only the passage, keeping word 81 in view.
- Should fix, general, Make one test: replacing answer buttons lost focus. The next slip retains the answer control; the final result focuses Close with preventScroll.
- Should fix, general, compact comments: the audit's 680x425 F10 frame showed the letter avatar over the habitat label. Moved it into the specimen header row; kept the avatar and scene detail. Scoped frames passed in audit-followup-after.
- Should fix, general, phone wrong path: two wrong Legit calls on long F10 crowded its words into the specimen rail and covered the habitat label. The study note and Show me now share a row, the redundant prompt stays in the hint, and the avatar stays inside the header. Scoped frames passed in audit-followup-after.
- Should fix, general, Field kit: the audit measured nine controls jumping when Legit inserted a duplicate prompt above them. The existing reserved hint now carries that prompt without adding a row. Scoped frames passed in audit-followup-after.
- Should fix, general, Guide: saved-specimen navigation was below long card text. Moved those existing Go to controls above the reading content so the short choice set is visible. Scoped frames passed in audit-followup-after.
- Should fix, general, 760-wide Make one: stacking the two slips put the lower marking control behind the action bar. Restored the specified side-by-side comparison at this intermediate width; 375 stays stacked. Scoped frames passed in audit-followup-after.
- Should fix, family:fallacies, Field: reselecting an unchanged species deleted a counted sighting. It now preserves the record; the full-guide check remained 24 before/after.
- Should fix, family:fallacies, Field voice: practice-only successes incorrectly said Logged. They now say Studied, not counted and cannot confirm a card.
- Should fix, general, rapid edit voice: editing the current call cleared its result but only dropped queued speech. It now hushes the obsolete result immediately. Rapid edit hushes Logged immediately; the complete main voice rerun passed.
- Should fix, family:fallacies, Guide: card details showed canned notes without the saved specimen. They now show the complete text and the student's marked passage beside each recorded call.
- Should fix, general, field/writing tests: prepared question lines were unused and Read omitted the question. Questions and the supplied Yes/No interpretations now speak in sequence and are included in Read. Manifest matches all 48 prepared lines.
- Should fix, general, factual framing: each selected specimen now says Invented advertisement/comment/news item/message, so students can see that the supplied survey and trial figures are fictional without opening teacher notes.
- Polish, general, graphics: the phone was cropped into metallic strips and mismatched the plates. Redrew it in sepia ink/watercolor, corrected an unwanted alpha rim in a second candidate, kept its full frame visible, and fitted chat inside its screen. Re-keyed existing magenta plates with despill.
- Polish, family:fallacies, F2 note: changed the categorical claim about a skater's knowledge to the narrower point that skating does not establish expertise in memory/tests.

#### Findings left

- Should fix, general, inline words: targets remain below 44 pixels. The mandated continuous full passage at 680x425 and direct per-word endpoints conflict with making every word a 44-pixel box. Kept the working arrow/Enter route and did not conceal targets from the audit. This needs a spec/layout decision.
- Should fix, family:fallacies, supplied content: F13 omits timetable evidence; F15 states sales but its key/note infer quality/health; F23 can be a personal movie opinion rather than an expertise argument. Kept supplied text/keys as CODEX-REVIEW requires for spec disagreements. Notes explain the limits.
- Should fix, family:fallacies, Ad hominem test: its truth wording is too strong for F8's reliability concern. Funding warrants checking, not automatically rejecting a study. The supplied question stays pending a spec correction.

#### Break it

- All 24 whole-text selections: rejected with Narrow it, no credit, before and after repairs. The four named six-extra cases reject. Independent minimum/one-below/invalid-range and every species/Legit alternative: 529 assertions passed.
- Option sweep on F1, then Show me and Log: Studied, zero credit. Correct mark plus two wrong calls on F3, then correct Legit/Authority: Studied, no confirmation, accurate spoken result.
- All 24 keyed calls through live controls: 24 unique sightings, eight confirmed pairs. Repeated Log five times: one sighting. Repeated same species: no count loss. Source retains historical confirmation independently of later edits, as specified.
- Field test Yes/No: generic suggestions, never a key verdict or guide credit. Tested Bandwagon and Hasty questions independently of the selected specimen.
- Make one: empty, seven-word and unmarked inputs stayed blocked; two completed marks enabled the test. Eight repeated nonsense words plus No/Yes produced the explicitly labeled self-judgment, but earned no card or verified grade. No semantic validation is claimed.
- Reset/clear ask first. Marked slips survive fresh tabs. Forced storage failure is caught and says current-tab-only. Keyboard-only F1 logged correctly with focus on Log.

#### Voice walk

Held clicks, 120 ms, two seconds apart: F2, endpoints, Authority, Log; F3, endpoints, Legit, Authority, Log; Guide, card, Close; Make one. Heard mark, last, pick, log, Logged, legit, Logged, Authority confirmed, Guide welcome, Make one welcome. Field welcome may be skipped on the first action under BASELINE 16; its instruction remains in hint/Read.

The main path was rerun after the final cancellation repair with the same spoken order. Side path wrote and marked both slips, answered each question, reached the self-check and focused Close. Field question plus its interpretation completed in order on a slower read-aloud check. Fast mode/reset changes left no stale queue. Read worked as first tap and with Sound off.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Logged | event | 5 | 5 |
| Miss | event | 5 | 5 |
| Mark/last/pick/log | how, main path | 1 each | 1 each |
| Legit | how, main path | 1 | 1 |
| Guide/Make one welcome | welcome | 1 each | 1 each |
| Studied | event, assisted path | 1 | 1 |

Narration is the browser fallback; no bank clips exist. Logs verify starts/order, not the sound of a recorded gravel-ranger voice.

#### Facts checked

Checked live on 2026-11-08 against [Bradley Dowden, Fallacies, Internet Encyclopedia of Philosophy](https://iep.utm.edu/fallacy/):

| Fact/specimens | Named source distinction |
|---|---|
| Ad hominem F7/F19; twin F8 | IEP Ad Hominem: relevance of the personal criticism. |
| Straw man F9/F20; twin F10 | IEP Straw Man: distortion versus fair summary. |
| Black-or-white F4/F21; twin F5 | IEP Black-or-White: unfair versus fair limited menu. |
| Slippery slope F11/F24; twin F13 | IEP Slippery Slope: support for successive steps. F13's missing timetable is open. |
| Hasty generalization F12/F22; twin F14 | IEP Hasty Generalization/Biased Statistics: sample adequacy and selection. |
| Authority F2/F23; twin F3 | IEP Appeal to Authority: expertise relevant to this question. F23 remains ambiguous. |
| Bandwagon F1/F15; twin F16 | IEP Appeal to the People: popularity does not establish quality. F15 remains ambiguous. |
| Post hoc F6/F17; twin F18 | IEP Post Hoc: sequence alone does not establish causation. |

F3 sealants on back teeth: [CDC, About Dental Sealants](https://www.cdc.gov/oral-health/prevention/about-dental-sealants.html), consistent with current guidance. F18 random allocation/comparison: [NCI, Randomized Clinical Trial](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/randomized-clinical-trial); not a guarantee of certainty.

F1-F24 names, brands, settings, amounts, times, 4,000 patients, six weeks/three miles, 1,200/58 percent, and 200/20 percent are authored fictional premises from spec.md, not sourced real results. No baseline homework total is provided to recompute an effect size. Recomputed 8x3=24; marks 4-13 words, minimum overlaps 2-7; all whole texts exceed five extras. Nine specified contrast ratios independently matched, 5.30-13.22:1.

#### Sensitivity

F3 teeth/sealants and F12 a broken wrist touch bodies. Review that readers do not mistake a fictional expert example or one injury for treatment advice or evidence that all skateparks are unsafe. F19's cartoon insult and F23's dentist/movie claim are specimens, not judgments about whose tastes count; F20's grandpa jab is quoted ridicule, not endorsed. No culture, religion, hard history or people images; the scarecrow is an inanimate object. All 11 assets are people:false.

#### Flattest moment left

After the first confirmation, later sightings still repeat the same mark/call rhythm. The four habitats and twin comparisons vary the reasoning; the new saved-passage comparison gives the guide a more personal payoff. No new modes, timers or topics were added.

#### Graphics

All 11 final images checked on cream, magenta and in scene/book frames. Kept the strong cork and animal plates. Phone redrawn and corrected; key spill reduced. Final art 674.1 KiB; bundle 1034.7 KiB. All required sizes, Motion off, grayscale, keyboard path and long slips inspected directly or in named contact sheets. Motion off had zero running infinite animations. Existing builder bar-comparison frame inspected as a finish reference, not claimed as a fresh bar-tool playthrough.

#### Audit

One final audit, exit 0, 2062.4 seconds (34 minutes), within the 2400-second cap: review-audit/audit.md, 98 frames, 2066 leads. All 98 frames inspected. This audited the frozen bundle before the narrow final layout/cancellation repairs; those repairs received the 12-shot scoped rerun, not a second full audit.

| Lead class | Disposition |
|---|---|
| Inline word targets | Open: the stated 44-pixel/spec conflict, not hidden or marked PASS. |
| Hidden Field hint in Guide/Make one | Probe assumption: visible guide-hint/make-hint and the documented Read callback are active. |
| Phone gallery / controls behind a modal | The required one-card-per-row gallery scrolls; native modal backgrounds are inert. |
| Saved Go to controls below card text | Fixed: existing jump controls moved above the content; 44-pixel controls visible at 680, 1366 and hosted 375. |
| Long passage reported sideways | False lead from rotated offscreen word bounds: actual scrollWidth equals clientWidth (605), scrollLeft is zero; passage scrolling and focused-word visibility checked. |
| Legit moves nine controls | Fixed: zero kit movement in the final held-click check. |
| Welcome not heard after a first action | Allowed by BASELINE 16; premise remains in hint/Read. Sound label movement is expected. |
| Quick word how-to cut | The second tap completes the mark, making the last-word instruction obsolete; the next-step hint replaces it. |
| Motion, runtime, focus, repeats, resize | No endless motion, console errors, stranded controls or settled/Enter focus losses. Listed five-click checks clean; resize stress completed. |

Final follow-ups also passed: phone wrong-path words clear navigation by 22.9 pixels; seven-word gate blocked; 760 marking controls visible; rapid obsolete Logged is hushed; final main voice order exact and queue empty. Pure checks remain 529/529. Bundle is offline with no external src/href and no host.html. All assigned ports are closed. Further regression states are retained for the next reviewer; no audit rerun.

#### Left open

Spec decisions above remain open, so this is not a claim that every standard passes. Missing kit/fallacies.js stays tool-local under BASELINE 13; no shared kit changes. Prepared narration remains unrecorded, as required. Make one is self-report: arbitrary writing plus No/Yes can produce the specified passing message, with no verified grade or guide credit. One review pass; evidence in _scratch/fallacy-field-guide/{cold*,before-checks,after-checks,side-checks,review-sizes,targeted-sizes,final-guard,review-audit,audit-followup-before,audit-followup-after}. A harness-only favicon 404 and a phone recipe's illegal-return error were corrected in scoped reruns. Initial read-only commands used wait limits rather than termination wrappers; every later command had a hard timeout. No git commits.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: fallacy-field-guide

#### Structure

src.html starts from the kit starter. The stylesheet lays out the cloth-and-paper field notebook, four habitat skins, field kit, guide book, writing slips and native dialogs. The script contains the species catalog, all 24 original specimens, a marked pure family block, state and persistence, Curio.voice, and DOM renderers. __tool exposes state, setMode, select, fx, specimens, catalog, allLines, vlog and vq for verification.

#### Decisions and contradictions

- No tool-specific open questions. Shared decisions follow BASELINE.md.
- The spec requests local FLUX; the owner's explicit image-tool instruction wins. All 11 images were generated with the built-in image tool, copied into art/raw, and processed with art.py --rekey. None show people.
- BUILD.md says do not draw art, while CODEX-BUILD.md and the owner require it. The build-specific and owner instructions win.
- kit/fallacies.js does not exist, and the spec says there is no family document. A marked pure block implements the requested API locally; no kit files were changed.
- After two misses, correct calls remain study-only. This closes the every-option cheat while preserving retries and Show me. Attempts and revealed status persist through reloads.
- The guide's Confirmed state is sticky as specified, even if current sighting counts later decrease. The footer explains this.
- F10's no-staff claim is absent from the original fictional news-story context. The context now includes that detail from F10, so its fair-summary key can be assessed.
- F13's distance alone cannot prove a missed bus connection. Its note is understood as an attributed timetable judgment, as the supplied key intends. No real bus timetable or numerical travel calculation is implied.
- F23 is keyed to expertise offered as support; a dentist can have a valid personal movie preference. Teacher notes preserve that boundary.
- F15's field note mentions being good for you, but the text states sales and says millions cannot be wrong. Its intended Bandwagon key depends on reading an implied quality claim. Preserve this content issue for review rather than inventing a health claim in the specimen.
- The Make one species picker is a menu beside a plate. Its welcome names the menu accurately rather than asking students to tap a card that is not present in that mode.
- The Hasty generalization and Bandwagon questions are not grammatically yes-or-no questions, and Post hoc combines two questions. Small on-screen legends make the supplied Yes/No controls unambiguous: many/fair versus few/biased; popularity itself versus quality/truth; fair comparison accounting for differences versus sequence alone.
- Make one's test is explicitly a self-check, never an automated semantic grade. Arbitrary text and favorable self-reported answers earn no guide cards.
- The processing Python on PATH lacks numpy. art.py ran using its existing compatible local site-packages without modifying the environment or installing anything.

#### Sensitivity

No culture, religion, hard history or people art. F3 mentions dentists, teeth and sealants; F12 mentions a broken wrist. These are fictional argument specimens, not health recommendations. The supplied expert-relevance example does not establish the truth of a treatment claim. Review the distinction between evaluating reasoning and judging people.

#### Art made

Eleven generated plates and habitat assets, all people:false. Full prompts in art/prompts.json; raw originals in art/raw; final WebP files in art. No downloaded art or recorded audio.

#### Art still to paint

None.

#### Engine changes wanted

kit/fallacies.js, new module: promote the marked pure fallacies block only when the shared-engine baseline is met. Preserve spot, test and cards APIs, parameterized catalog/specimens, overlap threshold, and five-extra-word rule. The requested file is currently missing. Habitat rendering remains tool-owned until a real sibling establishes a shared need.

#### Verification

Build-only evidence and remaining issues are recorded in codex-report.md. Scratch contains scripts, source-generation template, number checks, screenshot recipes and audit output. No commits or polish round.

#### Cold review repairs

Practice-only successes now use their own event voice, not Logged. Choosing an already selected species preserves a logged sighting. Long marked writing stays inside bounded slip passages, keeping Field test it reachable. Field and writing tests speak the question and the supplied Yes/No interpretation; Read repeats the current question and instructions. Guide details include the student's saved marked specimen texts, lifting the collection's comparison payoff.

Audit-frame follow-ups keep the Legit prompt in the reserved hint instead of inserting a row, put compact comment avatars in the specimen header, move saved-specimen navigation above the guide's reading content, and restore side-by-side slips at 760 wide. Selected specimens explicitly say they are invented. These local layout/copy repairs are checked with scoped frames after the single frozen-bundle audit.

The phone was redrawn in ink and watercolor, with an opaque empty screen and a magenta-key cutout, and is turned sideways in wide habitats so the whole bezel is visible. An initial native-alpha candidate had an unwanted inner transparent rim and was corrected before acceptance. Existing magenta-key plates were reprocessed with despill. Voice manifest and audit states were updated. No shared kit files changed.

Content boundaries F13, F15 and F23 and the conflict between compact continuous-word selection and uniform 44-pixel word targets remain spec decisions, recorded in the cold review. The requested missing family engine remains tool-local under BASELINE rule 13.

#### Cold review verification

The one review audit completed with exit 0 in 2062.4 seconds, with 98 frames. Its 2066 leads and their dispositions are in codex-review.md. No full audit rerun followed the narrow final repairs. The 12-shot scoped follow-up had no console errors; the main voice order, rapid-edit cancellation, stationary Legit kit, guide jump controls and phone practice path passed. The phone words clear their navigation by 22.9 pixels. Pure checks passed 529 assertions.

Bundle 1034.7 KiB, art 674.1 KiB, 48 prepared voice lines. Final bundle SHA-256: de8e2b4eb2256b717ef01fdae0d6c56e9736dd34b69667622066a5b7e9584529. Evidence and final-review-checks.json are under _scratch/fallacy-field-guide. All assigned ports closed; host.html absent. Further regression states are retained for the next reviewer.

#### Build verification repairs

The single completed audit produced 777 leads, mostly repeated inline-word target sizes. Repairs were staged in Scratch while its original input stayed fixed, checked with focused browser shots, then bundled into this folder. final-stats.json in Scratch records SHA-256 equality with the verified repair bundle.

The Field tab now measures 44 pixels wide. Writing inputs have explicit accessible names and block labels. Writing hints advance from the eight-word requirement to marking, then to the enabled test. Native dialog close and Escape restore the current mode's hint. Active habitat and specimen tabs preserve valid instructions and work. Word tokens stay in single inline boxes so a hyphenated word does not acquire a misleading rectangle spanning two lines.

At 760 wide all eight guide cards fit. At 375 wide both ordinary writing slips and their marking controls fit above the fixed action bar; longer writing scrolls within the marked passage. Phone card art sits above its explanation. Species stamps retain their glyph and name when a sighting is reopened. Confirmation flips are consumed after the first reveal.

The remaining project-standard failure is the 44-pixel size of individual word targets. The continuous passage uses smaller inline words with a complete arrow-key and Enter alternative. The 375-wide Guide scrolls as its explicit one-card-per-row specification requires. See the report for the content ambiguities and the recorded build-scope exception involving ignored reference bundles.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
