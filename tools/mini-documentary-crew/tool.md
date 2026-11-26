# Mini Documentary Crew: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: mini-documentary-crew

#### Built
- Completion provenance: an existing source build, 15 generated images and extensive test evidence were present at the start. Preserved that work. This pass redrew mdc-set, restored the spec's portrait approval fallback, rebundled, recomputed numbers, reran 75 functional assertions and all 396 independent scheduling cases, and completed the real-control production walkthrough. Retained earlier checks are distinguished below.
- Build only in `S:\CurioClass-codex`, limited to this tool and its Scratch folder. No commits, deployment, uploads or polish round.
- One offline production studio: constrained three-week calendar, footage from completed shoots, editing, timed screening comparisons and a printable premiere sheet.
- 15 generated images, including three flagged portraits. Painted viewer frames, a production whiteboard, physical filmstrips, audience chart, role stamps and immediate rejection feedback.
- Source uses the starter, shared kit, grade 9 to 12 theme, specified light palette and `Curio.voice`. No family engine was specified.
- Final bundle: 2,573,384 bytes (2513.07 KiB). Art: 1,837,534 bytes. Recorded voice: 0 bytes. Above the 2 MB goal to retain every requested image at 1280 pixels and quality 72. Final SHA-256: `c910af574001da986483e392721debaec740521ae4770239d98c118059ed9589`. Source syntax and offline resource checks pass; 1551 source lines, maximum 160 characters.

#### Numbers check
- Independent computation: `independent-math.py` and `numbers.json` in Scratch. The browser model agrees with the independently recomputed values.
- Material: 368 seconds of interviews + 77 B-roll + 24 photos = 469 seconds, 7:49. PASS.
- Spec's 15-clip sample runtime: 330 seconds, 5:30. Its actual written-model low is 75 at 3:59, average 90.4788, ending 100, no questions. Spec claims low 80 and average 92. FAIL to reproduce those contradictory targets.
- Bad sample: 299 seconds, 4:59. Written-model low 0, average 24.5753, four questions. Spec claims low 16 and average 46. FAIL to reproduce those contradictory targets.
- Noisy sample: low 30.5, average 73.9606. Spec claims low 60. Three uncovered Ana clips total 103 seconds, ending 33.5 with missing identification; spec claims 113 seconds and 54.
- Conventions: continuous visual-kind streak across adjacent interviews; covers count as B-roll; kind-change bonus before the incoming second; floor applied immediately at zero; recovery capped at 90; closer bonus replaces the final point for averaging.
- Contrast: brand/paper 6.309:1; white/brand 6.536:1; ink/paper 16.274:1; muted/paper 6.188:1. Matches the spec after rounding.
- `matrix-results.json`: all 396 independent combinations of shoot, slot and producer-fill choice match crew, time, rain and chronology rules. The full Sources schedule is accepted.

#### Facts checked
| Student-facing content | Source and check |
|---|---|
| Ruiz Shoe Repair, opening in 1962, Ana aged 71, closing next spring, three weeks to shoot and one to edit | Original fictional brief in `spec.md`; fiction stated on screen and in the brief. |
| Jae, Priya, Sam, producer availability; rain days; shoot restrictions | Fictional production rules in `spec.md`; independently enumerated in `matrix.py`. |
| A1: father opened in 1962; Ana swept at seven | Original invented interview A1, `spec.md`. |
| A2: new sole, heel, hand stitching and ten more years | Original invented testimony A2; attributed to Ana, not presented as general footwear guidance. |
| A3: three repair shops then, one now | Original invented testimony A3. |
| A4: cheaper shoes, glue and repair difficulty | Original invented testimony A4, not a verified technical rule. |
| A5: wedding shoes, soldier's boots, first cleats | Original invented testimony A5. |
| A6: closing and who will repair the town's shoes | Original invented testimony A6. |
| W1 to W3: forty-year boots, fiftieth anniversary, keeping repairable things | Original fictional customer testimony W1 to W3. |
| H1 to H3: 1960 shop counts, 1974 mall, repair and replacement | Original fictional town history H1 to H3. No real town is claimed. |
| B1a to B5: lasts, sole, awl, storefront, empty shops, tools, shop sounds | Given clip descriptions; all paintings inspected. Bell and machine tones are synthesized, not recordings. |
| P1 to P4: 1962, 1960, 1974 and 1980s | Given fictional archive dates. P1/P2 redrawn as full-frame monochrome archives. |
| Lower thirds, B-roll coverage, release-first production and test screenings | Spec conventions, attributed to Hampe, *Making Documentary Films and Videos*, second edition, 2007. Book chapters were not independently page-verified. |
| Archive request in this assignment | Fictional production requirement. [CMSI's statement](https://cmsimpact.org/code/documentary-filmmakers-statement-of-best-practices-in-fair-use/) checked: permission is not universally necessary; fair use exists. Notes distinguish the assignment from law. |
| Online captions | [W3C WCAG 2.1 SC 1.2.2](https://www.w3.org/TR/WCAG21/#captions-prerecorded), checked against its prerecorded synchronized-media requirement. |
| Audience line, thresholds, questions and ending bonus | Explicit invented model in `spec.md`, with on-screen assumptions. No empirical audience or overall quality claim. |
| Media arts goals | [NCAS](https://www.nationalartsstandards.org/): Pr4 through combining forms, Pr5 through production choices, Pr6 through screening/premiere, Cn10 through the student's audience/community connection. Broad anchors, not a mastery claim. |
| Device-only saving, no upload or recording | Source inspected: guarded `curio-mini-doc` storage, no microphone/camera access, no external resource requests or network calls. |

#### Break it
- Schedule counter: tried interviews before forms, moving forms after interviews, removing required forms, occupied slots, school mornings, wrong guest times, rain on exteriors and missing crew. Illegal cases stay out of the record. Rainy library interviews remain legal.
- Fill in: Wednesday boot shoot and Saturday afternoon Walt work with one producer role. Week 2 Friday morning Ana fails because both camera and sound are absent. A producer cannot fill both.
- Wrap: confirmed missing footage never appears; adding unshot W1 is rejected. Saturday Ana stays marked noisy. Empty wrap now offers Start over and cannot trap the student.
- Trim/cover: two-second cuts, fractional/out-of-source values and overlong covers rejected. Whole-second changes apply. Tail trimming selects the matching source transcript rather than compressing all the words into the trim.
- Identification: punctuation-only lower thirds, a wrong speaker and meaningless/wrong-year captions rejected. Correct name and role or date and place accepted. Removing identification restores its model consequences.
- Closer: a marker before the last clip earns no ending bonus. Silent B-roll cannot earn an ending-line bonus. Moving a marked interview to the end works.
- Attention/best line: repeated B2 can mathematically keep this deliberately simple model high. Reused source seconds are detected, cannot set a saved best line and cannot trigger clean narration. The actual formula remains visible; no story-quality score is claimed.
- Runtime/screening: under 4:30 cannot screen; an overlong cut warns and cannot lock a five-minute plan. Editing invalidates the current screening signature. Partial screenings are not stored; five completed comparisons are retained.
- Premiere: absent archive request, Online without captions, an unscreened changed cut and empty/punctuation-only invite or audience text block locking.
- Free prose remains a human judgment: word salad can satisfy a basic field-completeness check. The tool awards no reasoning or quality credit for it. No offline semantic assessor is claimed.
- Evidence: 75 functional assertions and 396 independent schedule cases rerun now; retained earlier evidence includes 79 assertions, real jittered drags, held clicks, keyboard placement, reload restoration, playback edits and full public-control end-to-end run.

#### Voice walk
- The two-second voice logs below are retained build evidence. The current full-control walkthrough also completed before the final visual-only portrait fallback switch, at its faster test pace. Both final gate frames then passed targeted browser checks. No claim that the two-second voice suite was rerun in this completion pass.
- Friendly-dad selected as the spec recommends despite its younger bank label. No recordings made, as instructed; actual speech uses the kit's browser fallback, not a claimed Achird recording.
- Main schedule path at two-second taps: welcomeSchedule, wrapHow, then welcomeEdit. Mode transition now hushes stale scheduling speech immediately.
- Five Add actions: welcomeEdit once and coverHow once. Superseded pending copies remain unmarked; the current how-to is eventually heard once.
- Missing-camera side path: fillHow starts before Fill in, even at the two-second pace. Its urgent current instruction supersedes the older welcome.
- Screen: welcomeScreen, timed lowPoint at 3 minutes 59 seconds, then clean. Two real complete screenings each speak both event lines again.
- Premiere: welcomePremiere when fields are incomplete; lockHow when ready; locked after the sheet is made. No help names a currently disabled Lock control.
- Interview testimony is confined to subtitles and visual transcripts. Final Read checks speak bin metadata or timeline editing instructions, never the invented interview quotation.
- Read interrupts through the kit and reads the current mode/dialog instruction. Motion off keeps time. Tests used held clicks and muted Chrome; no claim of listening to recorded clips.
- Evidence: `voice-*.json`, `two-screenings.json`, `e2e-results.json` and `read-bin.json`, `read-timeline.json`, `trim-visible.json` and `model-final.json` in Scratch.

#### Feel check
- Played the entire production through public controls: nine shoots, 15 clips, three identifying titles, three archive captions, four covers, an actual screening and a locked premiere. Native date-widget input worked. No console errors.
- Best moment: a cover appears while Ana's text continues, then the screening line changes with the actual cut. The late low point exposes two consecutive interviews as one visual streak.
- Flat moment 1: the compact viewer was a tiny letterbox. Moved its editing controls to a side rack, giving the painted frame more height while keeping every action visible.
- Flat moment 2: early drag attempts were intercepted by native image dragging. Disabled native image dragging, added pointer capture and verified real jittered card and timeline drags.
- Also added role stamps, rejected-slot feedback, a readable optional brief and a final sheet with pinned Print controls. No confetti or unrelated reward system.
- `bar-comparison.jpg` puts this tool beside Beat Lab; both bar bundles were opened. This has the requested lighter production-board identity, rich documentary art and a working multi-stage craft workflow, not a reskin of the bar.

#### Done when
1. PASS: calendar, editing viewer/filmstrip, audience chart and premiere card dominate their modes at 1366 and 680. Full frames and targeted compact repairs inspected.
2. PASS: rules enforced in words; full supplied schedule accepted; rain affects outdoor shoots only. 396-case independent matrix.
3. PASS: unshot clips absent and noisy Saturday Ana retained through wrap.
4. FAIL for the spec's contradictory sample attention numbers; PASS for editing controls and the written model, independently matched. See Numbers check.
5. PASS: Stop acts immediately; real-speed editing preserves the playhead and applies trims. Full screening completes at 8x; Motion off does not shorten timing.
6. PASS: permissions and Online captions block Lock appropriately; current screened cut, runtime and form completeness also checked.
7. PASS: guarded saves restore schedule, cut, text, covers and plan fields on a new load; confirmed Start over clears the record.
8. PASS: five-action once-only how-to test; two real screenings repeat both result events; mode and side-path logs inspected.
9. PASS for generated art and the specified fallback: all 15 assets are embedded, with three marked people. OpenAI generation follows the current user brief. PORTRAITS_APPROVED is false, so interview cards, bin thumbnails, timeline frames and viewers use mdc-set until owner approval. Targeted laptop and compact browser checks verify the fallback. The three portraits are complete and held for review.

#### Wave lessons
- PASS, hint/voice: immediate state hints, Read and heard-key how-to selection. Two-second held-click logs and stale-scope tests.
- PASS, focus/layout: panel controls precede calendar slots; keyboard forms placement works; modal focus returns with preventScroll; no initial focus grab. Fresh-project disabled mode buttons explain the audit focus leads; reachable modes and keyboard placement were tested independently.
- PASS, sizes: all STANDARDS dimensions captured, including genuine 375 iframe runs. Core controls fit; timeline and bin scroll by design. The automatic phone audit could not enter its iframe; separate phone and native-touch probes passed. This does not complete that audit.
- PASS, no giveaways: no hidden-answer quiz or fake mastery badge; saved best rejects repeated-footage padding.
- PASS, honest numbers: named fictional model, explicit assumptions, independently recomputed examples and disclosed contradictory spec values.
- PASS, standards: solo scheduling/editing, screening/presentation and audience/community explanation map to the four stated anchors.
- PASS, Motion off: no perpetual animation in the audit; timing remains unchanged.
- PASS, short choice sets: all nine shoot cards remain visible; compact edit actions use a two-column rack or phone grid. Trim ranges: both numeric inputs and both ranges visible at 680x425 after the scoped repair.
- PASS, resize mid-animation: same-project CDP resizes retained the 15 clip IDs, selected clip and advancing playback/screening; zero exceptions.
- PASS, deferred welcome: no welcomeAfter; first taps and mode changes use the kit's current-state rules.
- PASS, unknown as unknown: missing shoots explicitly say Not shot and produce no clips; missing identifying text produces the model's questions.
- PASS, one look/one meaning: separate kind colors plus icons/labels; hatching means cover; red means question or rejection.
- PASS, truthful badges: crew assignments match actual availability; noisy status persists; already-last closers say so; failed-slot flash clears.
- PASS, hints change back: each mode/render and modal close restores the current instruction. Empty-footage recovery names its available control.
- PASS, no word-copy answer: metadata is intentionally available for production; the skill is arranging and presenting the material, not guessing a hidden name.

#### Audit leads
Retained audit evidence, not rerun in this completion pass. Audit not finished. The single assigned-port run was stopped at 2400 seconds during stress checks, through trim-handles. Partial report: `_scratch/mini-documentary-crew/audit/audit.md`, 56 leads and 44 frames. Frozen audited bundle SHA-256: `144425596c0e0a347c3c8bb37f3caa6268ece1ae587d48014d7f8ba593c5c8ff`. Scoped repairs were checked directly afterward; the full audit was not rerun.
- Overlap leads across seven desktop sizes: `#brief` is a transparent whole-scene button over its own readable heading, label and story. Inspected frames; intentional shared hit area, no obscured type.
- Phone iframe/no-hint leads: the audit could not enter the iframe. A lingering own host was found and closed; its involvement is an inference. Separate genuine 375-wide iframe runs show the hint, Read, visible controls and native bin/timeline touch scrolling. Mechanical phone audit remains unverified.
- Edit/Screen/Premiere focus leads on a fresh project: these native buttons are intentionally disabled until their prerequisite exists. The audit's mode-click walk remained in Schedule. Reachable modes were exercised by authored states, the real student run and direct focus tests.
- Bin/timeline scroll leads: editing collections intentionally scroll; these are footage and ordered filmstrip, not hidden quiz alternatives. Phone native touch gestures moved bin 303 px and timeline 350 px. All nine scheduling choices remain visible together.
- Trim background hint keep lead: corrected audit-states.json to keep the modal dialog, not its inert background hint. Normal authored states still keep the hint. This is a configuration repair, not a claim of an audit rerun.
- Two trim range controls below the 680x425 fold: fixed with a compact two-column Trim layout. Direct bounds check and frame show both number inputs and both ranges visible together.
- Unnamed Date/Invite/audience leads: added explicit aria-labels to all three controls and inspected the compact Premiere frame. Their visible labels remain.
- Resize left-disabled clip leads: fresh runs created different timestamp UIDs. Same-project resizes during playback and screening retained all 15 enabled clip IDs, selection and advancing time; zero exceptions. Stop still worked.
- Welcome-not-heard leads: Wrap and Brief speak their current dialog instructions, superseding an obsolete welcome. A slot tap places the default selected forms and retires the scheduling welcome; the current result is in the hint. Read speaks the same current instruction. Sound off intentionally silences speech. No late welcome was restored.
- The recorded held-click and two-quick-tap subsections are clean for the controls actually listed. Later stress/shake sections were not completed. No full clean-audit claim.

#### Frames looked at
- Current pass: all eight completion/*.png frames, the finished mdc-set.webp at final size, art-contact.jpg, bar-comparison.jpg, and contact sheets e2e-1, full-1, full-2 and phone-last-1. Both final portrait-gate PNGs, completion-bar-comparison.jpg and the fresh four-frame completion-e2e-sheet.jpg were also opened and inspected.
- The retained report records review of all prior PNGs in the earlier test folders, all 44 audit frames and their contact sheets. Those older visual inspections were not all repeated now.

#### Art made
- 15 final images, three containing people, all marked `people: true` in prompts.json. 1794.47 KiB of WebP, 1280-pixel long side, quality 72. 2513.07 KiB bundle; 0 KiB recorded voice.
- Retained evidence records P1 and P2 each redrawn once for archival framing and monochrome. This pass redrew mdc-set with the built-in OpenAI image tool to strengthen the camera foreground, light stand and empty stool. The full prompt is in art/prompts.json; raw and finished files are local; only art.py --rekey was used for processing. Storefront title/date, lower thirds, captions and all chart text are code.
- OpenAI gpt-image credit included in metadata and source. Portrait contact sheet retained for the owner's later review.

#### Art still to paint
None missing. All 15 are complete; three portraits await the owner review explicitly required by the spec. The painted empty interview setup is active meanwhile. A fresh people/cultural review also belongs to the later cold review.

#### Engine changes wanted
No kit changes; shared files were left untouched. Requested test-helper improvements, also recorded in handoff.md:
- `scripts/drive.py::host`: expose the actual server PID or controlled shutdown and reject an occupied host port. A Windows launcher wrapper left a worker alive after termination; only this tool's exact host arguments were used to identify and close it.
- `scripts/audit_tool.py::Audit.size`: retain host HTTP diagnostics and a capture when iframe context lookup fails, to distinguish a wrong host from a tool defect.
- `scripts/audit_tool.py::Audit.stress`: compare generated clip IDs within the same project instead of between fresh runs; otherwise different UIDs look like disabled controls.

#### Left open
- The spec's worked attention targets cannot be reproduced from its formula. The formula is implemented and the discrepancy is preserved; the spec was not edited.
- Teacher-day morning Ana and Wednesday historian availability conflict with the stated crew. Those slots remain blocked when two roles are missing; viable alternatives are provided.
- Covers may hold a painted B-roll frame beyond its standalone duration because the sample asks for 20-second covers while the longest standalone B-roll is 15 seconds. This interpretation is disclosed in the UI and handoff.
- The model forgives noisy-audio attention loss during cover even though the interview's sound continues. That is its stated assumption, not a claim that B-roll repairs audio.
- The portrait approval gate is deliberately false. Change it only after the required review.
- The default Python lacked NumPy/Pillow; the required art.py --rekey succeeded using read-only packages from the available AI environment. No packages were installed.
- Book chapter claims were not page-verified. Free-text reasoning is not semantically graded. No real printing, publishing or audience validation is claimed.
- Single audit timed out; later stress/shake coverage and mechanical 375 iframe inspection remain open for the separate cold review. Direct post-fix checks do not replace a complete audit.
- Cleanup is checked again at report creation. Retained checks reported all launched test servers and assigned browser ports closed; temporary tool host.html removed. Final probes report Chrome 9990 and 9991 and host 8795 closed (`process-results.json`).
- Open questions and scope conflicts, including voice choice, people permission, early-report stop and bar write boundaries, are recorded in handoff.md. Final report created last, as requested.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: mini-documentary-crew

#### Played

Cold as a grade 10 solo producer, through all nine shoots, a weak 4:48 cut, a real screening and a locked premiere before opening builder notes or source. Replayed the continuous main path with Sound on, 120 ms held clicks and two-second pauses. The production board and consequential schedule are strong; covering an interview now gives an immediate visual payoff.

#### Findings fixed

- **blocker, general, Edit/Screen:** uncaptioned archive photos automatically displayed their dates while the model asked when they were taken. Removed automatic descriptive subtitles from documentary visuals; student captions now supply archive identification. B5 retains its meaningful-sound caption.
- **blocker, general, model/best:** reusing B2 across covers passed the source-reuse guard, earned a high line and could set best. Counted cover source seconds across uses, guarded clean narration, and rechecked older saved screenings on reload. Kept the specified attention formula unchanged.
- **blocker, general, identification checks:** substring matching accepted Banana Ruiz, Parksville, noncustomer, 19620 and a caption listing every date. Required one correct named identity and a bounded role, plus one exact source date and place. Recomputed saved screening curves under the repaired checks.
- **should fix, general, viewer CSS:** a tall narrow viewport stretched the overlay box away from its image. Preserved a 16:9 image-and-overlay rectangle inside the monitor; checked every desktop size and the phone host.
- **should fix, general, keyboard:** 23 bin choices preceded the transport and inspector. Moved frequent editing controls ahead of the bin in DOM order without changing their visual arrangement; keyboard focus is visible and stable.
- **should fix, general, Premiere voice:** readiness speech could continue after Lock. Hush immediately before making the sheet, then speak the finished-sheet event. The focused held-click recheck hears locked immediately.
- **should fix, general, screening feedback:** a clean cut was still told to fix a mistake. Clean results now invite review of the low point; cuts with low attention, questions or repeated material retain the repair instruction.
- **should fix, general, model guidance:** explicitly state in Cover and How it works that B-roll does not repair noisy interview sound. The spec's noise waiver remains a disclosed fictional-model limitation.
- **should fix, general, plan completeness:** repeated filler and punctuation-only titles could fill required fields. Reject those obvious empty inputs; preserve authored prose and make no automated reasoning-quality claim.
- **polish, general, flattest action:** Apply Cover changed a small hatch and words. It now previews the covered tail immediately with the interview subtitle continuing; active playback keeps its playhead.
- **should fix, general, art/B3:** the description said several shops were empty but windows looked stocked. Redrew Main Street in the same detailed house style with visibly vacant rooms beside the warm repair shop. Preserved the original in Scratch.
- **should fix, general, comparison chart:** earlier cuts of different lengths were stretched onto the current time axis. Align them by actual elapsed seconds and crop only what lies beyond the current cut. The 4:40 versus 5:30 rendering check confirms the earlier line ends at its true time.
- **polish, general, state feedback:** Stop now names a usable next action in empty Edit and Screen. An adjacent drop reports that its position is already correct instead of falsely saying it moved.
- **polish, general, Sensitivity:** removed an unsupported ethnic identification inferred from Ana's surname in handoff.md. The fiction identifies her by name and occupation.
- **should fix, general, phone Premiere:** the fixed action bar covered permission text. Reserved its height outside the scrolling plan. Also separated the bin heading hitbox from Add and explicitly named the caption field for assistive technology.

#### Findings left

- **should fix, spec examples:** numerical examples contradict the written rules. They remain unchanged under the review's spec boundary; independently computed values are below.
- **polish, spec portrait gate:** three finished respectful portraits remain inactive because Done when 9 explicitly requires owner approval. This unattended run uses the specified painted setup and does not infer approval.
- Free-prose quality remains human judgment. Distinct word salad can fill a form; no reasoning score, mastery badge or claim of validated argument is awarded for it.

#### Break it

- Schedule counter, forms, weather, occupancy and crew: 396 independently calculated shoot/slot/fill cases matched. Tried moving forms after interviews, rain outdoors versus indoors, and filling two absent roles; illegal work stayed out. A jittered real drag placed forms; missing-camera Fill in worked and spoke its how-to.
- Wrap/bin: unshot Walt cannot be added. Empty wrap produces no footage and offers Start over. Saturday Ana is noisy. Reset/reload outcome: confirmed Start over clears schedule, cut, wrap state and curio-mini-doc; reload retains eligible work and rechecks old best lines.
- Runtime/Trim/Cover: under 4:30 cannot screen; an overlong cut cannot lock. Two-second, fractional, negative and beyond-source trims stay in the dialog with a reason. Zero, fractional and excessive covers stay blocked. A valid cover shows immediately; playback/resize recheck: trim applied while the playhead advanced from 302.02 to 307.42 seconds, including resize; no exception or restart.
- Lower third/Caption: punctuation and wrong speakers/dates fail; actual name plus role and date plus place pass. Seven misleading name/date strings were accepted before the boundary repair and rejected afterward; seven ordinary correct labels still pass. A saved false question-free curve is recomputed with two missing-identification questions. Uncaptioned P1 shows no date in the viewer. These are structural label checks, not semantic truth detection.
- Closer: a nonfinal marked interview earns no bonus; silent B-roll cannot be marked as an ending line. Final marked interview works.
- Attention/best: actually screened 28 copies of B2 and an all-covered 4:48 interview cut. They flag 270 and 80 repeated seconds respectively, with no best and no clean event. An old saved cover cheat is reclassified on reload. The formula remains a declared model, not an overall documentary-quality score.
- Premiere: tried missing archive request, Online without captions, a changed unscreened cut, short/overlong runtime, punctuation title and repeated filler. Lock stays blocked. Ordinary meaningful fields and an eligible screened cut reach the printable sheet.
- 35 targeted assertions passed, including the 396-case scheduling comparison. Evidence: review-checks.json, review-side-a/, review-side-b/, review-legacy.json and the independent recompute.py in Scratch.

#### Voice walk

- Main path, in order: welcomeSchedule, wrapHow, welcomeEdit, coverHow, cover dialog instruction, welcomeScreen, lowPoint, welcomePremiere, lockHow, locked. The first continuous log exposed the late readiness line; fixed-lock-voice.json confirms its hush and the immediate locked event.
- Side paths: fillHow starts for the missing role. Five Add actions speak coverHow once. Read speaks the current hint with Sound off; turning Sound back on in Screen starts its still-unheard welcome. Stale Edit welcomes are dropped, not played over a populated timeline.
- Fixed lines match voice/lines.json and allLines: PASS, exact fixed-line sets. Counts combine the initial scoped runs with three additional real screenings and four additional held Lock events.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| coverHow over five Adds | how | 1 | 1 |
| lowPoint over five full screenings | event | 5 | 5 |
| clean over five full screenings | event | 5 | 5 |
| locked across fixed-lock checks | event | 5 | 5 |

- Motion/resize timing and result narration: Five complete 5:29 screenings produced identical lines with Motion on and off; after the initial two-second tap, 38.60 to 39.16 seconds remained. Both result events started each time. A live screening survived a 680-wide resize. Browser narration only, as the no-recording rule requires; no claim of a recorded Achird take or an audible listening test in muted Chrome. The four-Lock harness saved its complete passing log before its console-summary counter raised a missing-default error; direct inspection confirms four whole locked events and no browser errors.

#### Facts checked

| Fact or rule | Named source and result |
|---|---|
| Shop opens 1962; Ana is 71 and closes next spring; three shooting weeks and one editing week | Original fictional brief in spec.md. On-screen fiction notice retained. |
| A1: father founded shop, childhood sweeping | Fictional A1 in spec.md; not real biography. |
| A2: resole, heel, hand stitching, ten more years | Fictional Ana testimony A2; no general repair-life guarantee is taught. |
| A3: three shoe shops then, one now | Fictional A3, spec.md. |
| A4: cheap/glued shoes and repair difficulty | Fictional A4, spec.md; character testimony, not verified footwear science. |
| A5: wedding shoes, soldier's boots, first cleats; A6: who repairs after closing | Fictional A5/A6, spec.md. |
| W1 forty-year boots; W2 fiftieth-anniversary repair; W3 keeping repairable things | Fictional customer testimony W1/W2/W3, spec.md. |
| H1 1960 shop counts; H2 1974 mall and fewer walkers; H3 repair/replacement | Fictional historian testimony H1/H2/H3, spec.md; no actual town history claimed. |
| B1a/B1b/B1c last, sole and awl; B2 evening shop; B3 empty shops; B4 tools; B5 bell/machines | Given clip descriptions, spec.md; all finished images inspected, B3 corrected, sounds synthesized. |
| P1 1962; P2 1960; P3 1974; P4 1980s | Fictional archive dates in spec.md, with students responsible for visible captions. |
| Crew availability, forecasts, guest hours, one role per producer and one shoot per slot | Fictional rules in spec.md, independently enumerated in this review. |
| 368 interview + 77 B-roll + 24 archive seconds = 469, or 7:49; sample cut 330; bad cut 299 | Independent recompute.py from spec's clip list. Good low75/mean90.4788; bad low0/mean24.5753; noisy good low30.5; first three Ana103 seconds/end33.5. The spec's contrary examples fail. |
| Attention starts80; 20-second streak; 0.5 recovery/loss; kind-change5; identification5; noise1; closer10; caps/floor | Explicit fictional formula, spec.md. Independent implementation matches browser values; thresholds are not audience research. |
| B-roll can accompany interview sound; lower thirds identify speakers; archives combine with interviews | [CUNY BMCC Documentary Intro](https://openlab.bmcc.cuny.edu/mes153-rowell_scriptwriting-26sp/week-1/), checked live; consistent with spec's Hampe 2007 reference. Hampe chapters not independently page-verified. |
| Consent/release before this production's interviews | [Gallaudet Schuchman Documentary Center](https://gallaudet.edu/schuchman-documentary-center/informed-consent-and-video-release/), checked live. This assignment's scheduling rule is not a universal legal rule. |
| An archive request is this assignment's requirement; licensing is not always mandatory | [CMSI Documentary Filmmakers' Statement](https://cmsimpact.org/code/documentary-filmmakers-statement-of-best-practices-in-fair-use/), checked live: fair use can apply. |
| Online prerecorded captions provide access to speech and meaningful sounds | [W3C SC1.2.2 guidance](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html), checked live; source speaker/meaningful-sound identification included in its definition. |
| Pr4, Pr5, Pr6, Cn10 | [NCAS Media Arts at a Glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance.pdf): combining forms, scheduling/editing, screening/premiere and audience/community explanation are student actions. Broad-anchor support, not complete substandard mastery. |
| Privacy, offline operation, contrast | Guarded device-only storage, no external resource requests or capture APIs, 15 embedded WebPs; checked source/bundle. Brand/paper6.31, white/brand6.54, ink/paper16.27 and muted/paper6.19 agree with independent contrast computation. |

#### Sensitivity

Fictional older adults, a family shop, a named repairer and a changing community. Review portraits for age, anatomy, occupational dignity and cultural assumptions; do not infer ethnicity from Ruiz or Park. The three portraits show a natural range of skin tones and respectful adult roles, all correctly flagged people:true. Nothing claims to represent a whole culture. No hard-history game or real community is simulated. The spec's separate owner portrait approval remains open.

#### Flattest moment left

Long interviews still show the painted empty setup while the portrait approval gate is active. The required fallback stays. Applying Cover is now a clear visual transformation, and the Main Street image tells its part of the story without extra text.

#### Graphics

All 15 finished assets opened at native resolution and their active frames checked in the tool. Main Street redrawn with the imagegen skill and built-in tool, processed only with art.py --rekey; full style/prompt/provenance in art/prompts.json. No image dropped. Bundle 2506.5 KiB; art 1787.6 KiB. Above the 2 MB goal to retain the set, below 6 MB. Compared with the existing Beat Lab bundle; retained the mature whiteboard, tactile art and filmstrip. Motion off and grayscale checked; all seven desktop sizes plus true 375-wide host inspected.

#### Audit

Audit not finished: the single 2400-second run saved 69 leads and 59 inspected frames, through trim-handle stress checks. Five-held-click and quick-double-tap sections are clean; later resize sections are incomplete. Confirmed phone plan spacing, heading hitboxes and metadata naming were fixed and re-shot in eight targeted frames, with zero browser errors. The brief hit area, intentional catalogs/filmstrip scrolling, inert modal backgrounds, prerequisite-disabled modes and permitted first-tap welcome skips stay. Fresh-project clip-ID comparisons are false resize leads: the same-project follow-up retained all 15 enabled IDs and selection. Full dispositions: _scratch/mini-documentary-crew/review-audit-disposition.md. Audited bundle SHA-256 d761459a63f693763220f658d5216a1c1630642c084ba95c3dcd1fbadecc7746; final scoped-repair bundle 66fb34756a977ebb0a0fc0c2905174a13cd84a1ba0b7762942178b0ad7d8829b. No second audit.

#### Left open

Spec corrections: worked attention examples and the noise waiver during covers. Wednesday historian and week-2-Friday-morning Ana availability has no feasible crew under the written constraints; retained those constraints. Kept all written constraints and disclosed the model limit. No kit changes, new topics, commits, uploads or publication. One initial read used the tool yield limit rather than an explicit command deadline; every later shell command was bounded. Browser and fixture failures are retained in Scratch. Smaller scoped rechecks distinguish those harness failures from product behavior. Recorded narration and owner portrait approval remain outside this review's authority. Owned Chrome ports 9940, 9941 and 9943 and host port 8745 were verified closed. The temporary phone host was removed. The final phone server logged two connection resets during browser shutdown after all eight shots passed; these are harness shutdown messages, not tool errors.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Mini Documentary Crew handoff

Build only. No commits, publication, uploads or polish round.

#### Source map

`src.html` starts from the kit starter structure and loads the kit and grade 9 to 12 theme, then overrides it with the specified production-whiteboard palette. Responsive CSS comes first. The script defines art, shoot rules, source clips, voice lines, persistence, calendar validation, editing, the attention model, playback, premiere and input handlers. `window.__tool` exposes live state, data, rule functions, model and voice log for review.

Images occur once in the ART table so the bundle does not repeat their data. Painted frames fill the viewer; exact calendar, timeline, subtitles, lower thirds, poster type and line chart are code. All 15 images are embedded; the 12 place/object frames are active and the three portraits are held behind the approval switch. Raw originals and generated WebP files are under art; review sheets and discarded candidates stay in Scratch or the generator's own cache.

#### Rules and tricky parts

- Calendar validation checks occupancy, time, availability, weather, crew and form chronology at once. Moving or removing forms cannot invalidate an existing interview. The producer can fill exactly one missing role. Wrap freezes the production record.
- `placement` is a pure query; `place` owns feedback and persistence. Clip creation checks that its shoot exists. Missing shoots never enter the bin.
- Each timeline instance has a stable uid. In and out are whole source seconds. Editing during playback retains the playhead. Playback generations prevent an old animation loop from joining a restarted run. Motion off removes panning, not elapsed time.
- Selecting a bin clip while stopped previews its source frame and clears timeline selection. Editing actions then require a timeline selection. Subtitles follow the original source time through trims rather than squeezing all testimony into a shorter cut.
- A low point at a clip boundary selects the outgoing responsible interview. Structural edits reveal the selected clip inside the timeline only. An edited cut hides the stale low-point marker until screened again.
- Compact Saturday cells reserve extra width for two crew assignments. Phone bin and timeline accept native horizontal touch scrolling. At short heights, Trim shows all four numeric/range controls together.
- A covered interview has B-roll visual kind, resets the continuous uncovered interview streak and retains interview text. Covers may hold a painted frame longer than its standalone source duration, as permitted by the spec's interview-minus-three-second limit.
- Identification requires the actual speaker and role; captions require the source year and a place. Punctuation-only and wrong-person inputs are rejected. Empty text removes an identification and restores its model penalty.
- Completed screenings snapshot the cut and line. Partial tests are not saved. A changed cut needs a new screening before locking a plan. Five comparisons are retained.
- Wrapping without any footage exposes the existing Start over action in Edit and a matching voice line. This recovery avoids a dead end when Screen and Premiere cannot open. It does not add a new production mode.
- The attention model measures its literal formula, not documentary competence. Repeated B-roll is an explicit blind spot. Free-text invite and audience fields are completeness checks, not automated judgments of good reasoning.
- The user's anti-cheat instruction takes precedence for saved best lines: overlapping reuse of the same source seconds is flagged, cannot set a saved best screening and cannot trigger the clean narration. Its actual attention trace remains the unmodified formula. Cover and standalone overlaps both count toward the reuse warning. A single held frame remains permitted within one cover.
- Every storage operation is guarded. The footer states device-only persistence. All student text is escaped before HTML rendering or assigned with textContent.

#### Decisions and spec questions

- Use friendly-dad as the spec leans toward, despite its younger bank label. It represents a patient retired producer; interview testimony stays as subtitles. The no-recording build instruction means the kit's browser fallback is used.
- All three people portraits are generated and marked `people: true`. The spec separately requires owner approval before display. `PORTRAITS_APPROVED` therefore starts false; `paintedFrame` uses mdc-set for interview cards, thumbnails and viewers until that review. The actual speaker metadata and model remain unchanged. The contact sheet is in Scratch for review.
- Use the written attention formula when its worked example differs. Independent results are in Scratch `numbers.json`; the final report lists the conflicts. Continuous interview means no visual-kind break, even across different interview clips.
- Apply kind-change bonuses at the first second of the incoming visual kind, then that second's gain or penalty. Recovery uses the formula's explicit cap of 90. The end bonus replaces the last second's point for averaging. These conventions make the otherwise underspecified discrete model reproducible.
- Wednesday historian slots and week 2 Friday morning Ana slots pass the guest's availability rule but fail the stated crew rules because both camera and sound are absent. Do not silently extend the crew's availability. Thursday historian and Saturday morning noisy Ana are fully feasible alternatives. The full Sources schedule is accepted.
- The archive scan includes requesting the license. The spec has no separate request card or control; the shoot label makes that linkage explicit.
- Keep all 15 images at the requested 1280-pixel long side and quality 72. The bundle exceeds the 2 MB goal. No image was dropped to meet a size target.
- The early-report instruction conflicts with the user's stop-on-report instruction. Evidence was accumulated in Scratch `report-draft.md`; the final tool report is written only after checks finish.
- The written model forgives noisy-audio attention loss during a cover although interview sound continues. This assumption is disclosed; a cover does not repair audio.
- Existing bar bundles were opened rather than rebuilt in their tool folders, which would violate this run's write boundary.

#### Sensitivity

Fictional occupational and community story with older adults and a shoe repairer named Ana Ruiz. Nothing depicts a real family or town. Review the three portraits for respectful age, cultural and occupational representation, natural anatomy and stereotypes. The story's economic changes and shoe-repair claims are invented testimony, not historical or technical generalizations. A fresh cultural review remains part of the later cold review, not this build-only session.

#### Engine changes wanted

No kit changes. No shared scripts, docs or another tool was edited. These test-helper changes would improve later runs:

- `scripts/drive.py`, `host`: expose the actual server PID or a controlled shutdown endpoint, and reject an occupied host port. On this Windows Python launcher, terminating the wrapper left a worker listening on 8795. This build closed only processes whose full arguments identified this tool and that port.
- `scripts/audit_tool.py`, `Audit.size`: include the host response and a diagnostic capture when the iframe execution context is missing. The 375-wide audit could not inspect its iframe; separate genuine iframe tests passed after the stale host was closed.
- `scripts/audit_tool.py`, `Audit.stress`: compare generated control IDs within the same project run, or match their semantic positions. Fresh projects generate different clip UIDs, producing false disabled-after-resize leads. A same-project resize probe retained all 15 enabled clips and the playhead.

#### Evidence

All test scripts, independent numbers, generated-image contact sheets, bar frames, functional results, screenshots, voice walks and the partial audit are in `_scratch/mini-documentary-crew/`. Final checks passed 79 functional assertions and 396 independent scheduling cases. A public-control run completed all nine shoots, a 330-second edit, a real screening and a locked premiere. Same-project resize and native phone touch probes reported no exceptions.

The single audit reached its 2400-second limit during stress checks, through trim-handles. It preserved 56 leads and 44 frames; it is not a completed clean audit. Its frozen bundle SHA-256 is `144425596c0e0a347c3c8bb37f3caa6268ece1ae587d48014d7f8ba593c5c8ff`. Later scoped repairs and direct probes are recorded in the final report. The modal audit-state keep region now names its dialog, without requiring the inert background hint to be unobscured. Do not infer that the whole audit was rerun after those repairs.

#### Build completion provenance

The source, 15 images and extensive Scratch evidence already existed when this completion pass began. They were preserved. The report distinguishes retained evidence from checks rerun now. The empty interview setup was redrawn with the built-in OpenAI image tool, its full prompt saved in prompts.json, its raw PNG copied locally, and art.py run only with --rekey. The earlier version is retained in Scratch. The completed WebP was inspected at 1280 by 720 pixels.

The default shell Python lacks NumPy and Pillow. The available AI environment's interpreter could not launch under this session's restrictions. Running the same required art.py script through the shell Python with that environment's read-only site-packages on sys.path succeeded. No dependency installation or shared-file change was made.

See codex-report.md for every lead group's disposition, final bundle hash, resource cleanup and unresolved numerical contradictions. The next step is the separate cold review, not a polish round in this session.

Current completion checks: 75 functional assertions and 396 independent schedule cases passed; a real-control nine-shoot, 15-clip, 330-second screening and locked premiere passed before the final visual-only approval fallback. Final 1366 and 680 fallback checks passed with no broken images or console errors. See completion-*.json, portrait-gate-*.json and completion-bar-comparison.jpg in Scratch. Final bundle SHA-256: c910af574001da986483e392721debaec740521ae4770239d98c118059ed9589.

#### Cold review repairs

- Uncaptioned archive frames no longer receive automatic date subtitles. Bin descriptions remain reference metadata; the viewer uses the student's Caption. B5 retains an explicit door-bell and machines caption.
- Cover now previews its covered tail immediately after Apply when stopped. It does not move an active playhead. The dialog and model note explicitly say that B-roll does not repair noisy interview sound.
- The source-reuse guard now includes cover source seconds. A held frame is counted once within a cover, but reuse in another cover or standalone instance cannot set a saved best or trigger clean narration. Previously saved screenings are rechecked on load. The spec's numeric attention formula is unchanged.
- Editing transport and inspector controls precede the long bin in keyboard order. Add to end precedes bin items in DOM order while retaining its familiar visual position.
- mdc-main was redrawn in the same house style to show bare vacant windows beside the active repair shop. Full review prompt and provenance are in art/prompts.json; the prior WebP is preserved in Scratch.
- The explicit portrait-approval switch remains false, as the spec requires. This unattended review does not infer owner approval. The three completed respectful portraits remain available for that review.
- Independent review calculations confirm material 469 s, good sample 330 s / low75 / average90.4788, bad sample299 s / low0 / average24.5753, noisy good low30.5, and first-three-Ana103 s / end33.5. The contradictory spec examples remain a spec correction request.
- Current fact checks: W3C SC1.2.2 supports prerecorded captions, including meaningful sounds and speaker identification; CMSI confirms fair use may avoid licensing. Gallaudet Schuchman Documentary Center documents informed consent and releases before interviews. NCAS Media Arts at a Glance supports the four broad production anchors. The fictional dates, characters, testimony, schedule and audience formula come from spec.md.
- The viewer now maintains its 16:9 image-and-overlay rectangle inside tall narrow monitors. All seven desktop dimensions and the genuine 375-wide host were checked after the change.
- Lock hushes a readiness instruction immediately before the finished-sheet event. A clean screening invites review of its low point, rather than assuming that the student must fix a mistake.
- Repeated filler in Invite and audience text, and punctuation-only titles, do not satisfy completion. These remain field-completeness checks; they do not grade the meaning of free prose.

Comparison curves now use actual elapsed seconds rather than stretching an earlier runtime onto the current axis. The review verified a 280-second earlier line ending at its true time beneath a 330-second current cut. Adjacent no-op drops and Stop in empty Edit also retain truthful, usable feedback.

The final cold-review audit reached its single 2400-second deadline with a preserved partial report, 69 leads and 59 frames. Confirmed phone action-bar spacing, heading hitboxes and an explicit caption-field name were repaired. Named-identity and exact-date boundaries now reject substring/all-options cheats. Saved screening curves are recomputed with the repaired validators, preserving each original label. See codex-review.md and review-audit-disposition.md in Scratch for completion limits and targeted rechecks.

Final cold-review bundle SHA-256: 66fb34756a977ebb0a0fc0c2905174a13cd84a1ba0b7762942178b0ad7d8829b. Metadata boundary probes, historical-score refresh, phone layout/accessibility and stable-ID resize checks passed. All review-owned browser/server ports are closed and the temporary host is removed. The audit remains explicitly partial; it was not repeated.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
