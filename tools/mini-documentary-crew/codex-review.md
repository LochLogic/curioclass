# Codex review: mini-documentary-crew

## Played

Cold as a grade 10 solo producer, through all nine shoots, a weak 4:48 cut, a real screening and a locked premiere before opening builder notes or source. Replayed the continuous main path with Sound on, 120 ms held clicks and two-second pauses. The production board and consequential schedule are strong; covering an interview now gives an immediate visual payoff.

## Findings fixed

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

## Findings left

- **should fix, spec examples:** numerical examples contradict the written rules. They remain unchanged under the review's spec boundary; independently computed values are below.
- **polish, spec portrait gate:** three finished respectful portraits remain inactive because Done when 9 explicitly requires owner approval. This unattended run uses the specified painted setup and does not infer approval.
- Free-prose quality remains human judgment. Distinct word salad can fill a form; no reasoning score, mastery badge or claim of validated argument is awarded for it.

## Break it

- Schedule counter, forms, weather, occupancy and crew: 396 independently calculated shoot/slot/fill cases matched. Tried moving forms after interviews, rain outdoors versus indoors, and filling two absent roles; illegal work stayed out. A jittered real drag placed forms; missing-camera Fill in worked and spoke its how-to.
- Wrap/bin: unshot Walt cannot be added. Empty wrap produces no footage and offers Start over. Saturday Ana is noisy. Reset/reload outcome: confirmed Start over clears schedule, cut, wrap state and curio-mini-doc; reload retains eligible work and rechecks old best lines.
- Runtime/Trim/Cover: under 4:30 cannot screen; an overlong cut cannot lock. Two-second, fractional, negative and beyond-source trims stay in the dialog with a reason. Zero, fractional and excessive covers stay blocked. A valid cover shows immediately; playback/resize recheck: trim applied while the playhead advanced from 302.02 to 307.42 seconds, including resize; no exception or restart.
- Lower third/Caption: punctuation and wrong speakers/dates fail; actual name plus role and date plus place pass. Seven misleading name/date strings were accepted before the boundary repair and rejected afterward; seven ordinary correct labels still pass. A saved false question-free curve is recomputed with two missing-identification questions. Uncaptioned P1 shows no date in the viewer. These are structural label checks, not semantic truth detection.
- Closer: a nonfinal marked interview earns no bonus; silent B-roll cannot be marked as an ending line. Final marked interview works.
- Attention/best: actually screened 28 copies of B2 and an all-covered 4:48 interview cut. They flag 270 and 80 repeated seconds respectively, with no best and no clean event. An old saved cover cheat is reclassified on reload. The formula remains a declared model, not an overall documentary-quality score.
- Premiere: tried missing archive request, Online without captions, a changed unscreened cut, short/overlong runtime, punctuation title and repeated filler. Lock stays blocked. Ordinary meaningful fields and an eligible screened cut reach the printable sheet.
- 35 targeted assertions passed, including the 396-case scheduling comparison. Evidence: review-checks.json, review-side-a/, review-side-b/, review-legacy.json and the independent recompute.py in Scratch.

## Voice walk

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

## Facts checked

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

## Sensitivity

Fictional older adults, a family shop, a named repairer and a changing community. Review portraits for age, anatomy, occupational dignity and cultural assumptions; do not infer ethnicity from Ruiz or Park. The three portraits show a natural range of skin tones and respectful adult roles, all correctly flagged people:true. Nothing claims to represent a whole culture. No hard-history game or real community is simulated. The spec's separate owner portrait approval remains open.

## Flattest moment left

Long interviews still show the painted empty setup while the portrait approval gate is active. The required fallback stays. Applying Cover is now a clear visual transformation, and the Main Street image tells its part of the story without extra text.

## Graphics

All 15 finished assets opened at native resolution and their active frames checked in the tool. Main Street redrawn with the imagegen skill and built-in tool, processed only with art.py --rekey; full style/prompt/provenance in art/prompts.json. No image dropped. Bundle 2506.5 KiB; art 1787.6 KiB. Above the 2 MB goal to retain the set, below 6 MB. Compared with the existing Beat Lab bundle; retained the mature whiteboard, tactile art and filmstrip. Motion off and grayscale checked; all seven desktop sizes plus true 375-wide host inspected.

## Audit

Audit not finished: the single 2400-second run saved 69 leads and 59 inspected frames, through trim-handle stress checks. Five-held-click and quick-double-tap sections are clean; later resize sections are incomplete. Confirmed phone plan spacing, heading hitboxes and metadata naming were fixed and re-shot in eight targeted frames, with zero browser errors. The brief hit area, intentional catalogs/filmstrip scrolling, inert modal backgrounds, prerequisite-disabled modes and permitted first-tap welcome skips stay. Fresh-project clip-ID comparisons are false resize leads: the same-project follow-up retained all 15 enabled IDs and selection. Full dispositions: _scratch/mini-documentary-crew/review-audit-disposition.md. Audited bundle SHA-256 d761459a63f693763220f658d5216a1c1630642c084ba95c3dcd1fbadecc7746; final scoped-repair bundle 66fb34756a977ebb0a0fc0c2905174a13cd84a1ba0b7762942178b0ad7d8829b. No second audit.

## Left open

Spec corrections: worked attention examples and the noise waiver during covers. Wednesday historian and week-2-Friday-morning Ana availability has no feasible crew under the written constraints; retained those constraints. Kept all written constraints and disclosed the model limit. No kit changes, new topics, commits, uploads or publication. One initial read used the tool yield limit rather than an explicit command deadline; every later shell command was bounded. Browser and fixture failures are retained in Scratch. Smaller scoped rechecks distinguish those harness failures from product behavior. Recorded narration and owner portrait approval remain outside this review's authority. Owned Chrome ports 9940, 9941 and 9943 and host port 8745 were verified closed. The temporary phone host was removed. The final phone server logged two connection resets during browser shutdown after all eight shots passed; these are harness shutdown messages, not tool errors.
