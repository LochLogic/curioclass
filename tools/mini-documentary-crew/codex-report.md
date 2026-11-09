# Codex report: mini-documentary-crew

## Built
- Completion provenance: an existing source build, 15 generated images and extensive test evidence were present at the start. Preserved that work. This pass redrew mdc-set, restored the spec's portrait approval fallback, rebundled, recomputed numbers, reran 75 functional assertions and all 396 independent scheduling cases, and completed the real-control production walkthrough. Retained earlier checks are distinguished below.
- Build only in `S:\CurioClass-codex`, limited to this tool and its Scratch folder. No commits, deployment, uploads or polish round.
- One offline production studio: constrained three-week calendar, footage from completed shoots, editing, timed screening comparisons and a printable premiere sheet.
- 15 generated images, including three flagged portraits. Painted viewer frames, a production whiteboard, physical filmstrips, audience chart, role stamps and immediate rejection feedback.
- Source uses the starter, shared kit, grade 9 to 12 theme, specified light palette and `Curio.voice`. No family engine was specified.
- Final bundle: 2,573,384 bytes (2513.07 KiB). Art: 1,837,534 bytes. Recorded voice: 0 bytes. Above the 2 MB goal to retain every requested image at 1280 pixels and quality 72. Final SHA-256: `c910af574001da986483e392721debaec740521ae4770239d98c118059ed9589`. Source syntax and offline resource checks pass; 1551 source lines, maximum 160 characters.

## Numbers check
- Independent computation: `independent-math.py` and `numbers.json` in Scratch. The browser model agrees with the independently recomputed values.
- Material: 368 seconds of interviews + 77 B-roll + 24 photos = 469 seconds, 7:49. PASS.
- Spec's 15-clip sample runtime: 330 seconds, 5:30. Its actual written-model low is 75 at 3:59, average 90.4788, ending 100, no questions. Spec claims low 80 and average 92. FAIL to reproduce those contradictory targets.
- Bad sample: 299 seconds, 4:59. Written-model low 0, average 24.5753, four questions. Spec claims low 16 and average 46. FAIL to reproduce those contradictory targets.
- Noisy sample: low 30.5, average 73.9606. Spec claims low 60. Three uncovered Ana clips total 103 seconds, ending 33.5 with missing identification; spec claims 113 seconds and 54.
- Conventions: continuous visual-kind streak across adjacent interviews; covers count as B-roll; kind-change bonus before the incoming second; floor applied immediately at zero; recovery capped at 90; closer bonus replaces the final point for averaging.
- Contrast: brand/paper 6.309:1; white/brand 6.536:1; ink/paper 16.274:1; muted/paper 6.188:1. Matches the spec after rounding.
- `matrix-results.json`: all 396 independent combinations of shoot, slot and producer-fill choice match crew, time, rain and chronology rules. The full Sources schedule is accepted.

## Facts checked
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

## Break it
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

## Voice walk
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

## Feel check
- Played the entire production through public controls: nine shoots, 15 clips, three identifying titles, three archive captions, four covers, an actual screening and a locked premiere. Native date-widget input worked. No console errors.
- Best moment: a cover appears while Ana's text continues, then the screening line changes with the actual cut. The late low point exposes two consecutive interviews as one visual streak.
- Flat moment 1: the compact viewer was a tiny letterbox. Moved its editing controls to a side rack, giving the painted frame more height while keeping every action visible.
- Flat moment 2: early drag attempts were intercepted by native image dragging. Disabled native image dragging, added pointer capture and verified real jittered card and timeline drags.
- Also added role stamps, rejected-slot feedback, a readable optional brief and a final sheet with pinned Print controls. No confetti or unrelated reward system.
- `bar-comparison.jpg` puts this tool beside Beat Lab; both bar bundles were opened. This has the requested lighter production-board identity, rich documentary art and a working multi-stage craft workflow, not a reskin of the bar.

## Done when
1. PASS: calendar, editing viewer/filmstrip, audience chart and premiere card dominate their modes at 1366 and 680. Full frames and targeted compact repairs inspected.
2. PASS: rules enforced in words; full supplied schedule accepted; rain affects outdoor shoots only. 396-case independent matrix.
3. PASS: unshot clips absent and noisy Saturday Ana retained through wrap.
4. FAIL for the spec's contradictory sample attention numbers; PASS for editing controls and the written model, independently matched. See Numbers check.
5. PASS: Stop acts immediately; real-speed editing preserves the playhead and applies trims. Full screening completes at 8x; Motion off does not shorten timing.
6. PASS: permissions and Online captions block Lock appropriately; current screened cut, runtime and form completeness also checked.
7. PASS: guarded saves restore schedule, cut, text, covers and plan fields on a new load; confirmed Start over clears the record.
8. PASS: five-action once-only how-to test; two real screenings repeat both result events; mode and side-path logs inspected.
9. PASS for generated art and the specified fallback: all 15 assets are embedded, with three marked people. OpenAI generation follows the current user brief. PORTRAITS_APPROVED is false, so interview cards, bin thumbnails, timeline frames and viewers use mdc-set until owner approval. Targeted laptop and compact browser checks verify the fallback. The three portraits are complete and held for review.

## Wave lessons
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

## Audit leads
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

## Frames looked at
- Current pass: all eight completion/*.png frames, the finished mdc-set.webp at final size, art-contact.jpg, bar-comparison.jpg, and contact sheets e2e-1, full-1, full-2 and phone-last-1. Both final portrait-gate PNGs, completion-bar-comparison.jpg and the fresh four-frame completion-e2e-sheet.jpg were also opened and inspected.
- The retained report records review of all prior PNGs in the earlier test folders, all 44 audit frames and their contact sheets. Those older visual inspections were not all repeated now.

## Art made
- 15 final images, three containing people, all marked `people: true` in prompts.json. 1794.47 KiB of WebP, 1280-pixel long side, quality 72. 2513.07 KiB bundle; 0 KiB recorded voice.
- Retained evidence records P1 and P2 each redrawn once for archival framing and monochrome. This pass redrew mdc-set with the built-in OpenAI image tool to strengthen the camera foreground, light stand and empty stool. The full prompt is in art/prompts.json; raw and finished files are local; only art.py --rekey was used for processing. Storefront title/date, lower thirds, captions and all chart text are code.
- OpenAI gpt-image credit included in metadata and source. Portrait contact sheet retained for the owner's later review.

## Art still to paint
None missing. All 15 are complete; three portraits await the owner review explicitly required by the spec. The painted empty interview setup is active meanwhile. A fresh people/cultural review also belongs to the later cold review.

## Engine changes wanted
No kit changes; shared files were left untouched. Requested test-helper improvements, also recorded in handoff.md:
- `scripts/drive.py::host`: expose the actual server PID or controlled shutdown and reject an occupied host port. A Windows launcher wrapper left a worker alive after termination; only this tool's exact host arguments were used to identify and close it.
- `scripts/audit_tool.py::Audit.size`: retain host HTTP diagnostics and a capture when iframe context lookup fails, to distinguish a wrong host from a tool defect.
- `scripts/audit_tool.py::Audit.stress`: compare generated clip IDs within the same project instead of between fresh runs; otherwise different UIDs look like disabled controls.

## Left open
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
