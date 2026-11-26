# Dancers on Tour: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: dancers-on-tour

#### Built
- Scout, Adapt and Warm up for all three venues, with independent saved settings and venue reset.
- Original six-dancer formations, per-phrase spread/swaps, four fronts, live tempo, run counts, transitions and synthesized music.
- SVG plan with safe margin, surface textures, obstacles, numbered dancer inspection, collision rings and four live lights. Kit figures in an audience inset.
- Warm-up blocks toggle, reorder by arrows or real pointer drag, show duration and exact risk-point breakdown.
- All required files made. No commits, no changes to kit/docs/scripts/other tools, no polish round. Temporary evidence stays in Scratch.

#### Numbers check
- Scratch `numbers.json` recomputes every source formation width, depth, closest distance and feasible spread interval. The spec's rounded results match.
- Exact theater split interval: 0.8320503 to 0.9285714, so slider settings 0.85 and 0.90 work. Original diagonal needs at least 0.6708204 but fits only through 0.65.
- 32 counts at 112 bpm = 17.142857 s. Four setup counts and three transition counts give 20.89 s at 100%, unchanged by Motion off.
- WCAG ratios: ink/background 15.47, ink/panel 13.78, muted/background 8.05, muted/panel 7.17, brand/background 11.36, brand/panel 10.13. Dark text/brand 11.36.
- Sixteen focused model checks pass in `functional-results-final.json`, including safety totals, both hand-checked seats, note predicates and venue reset.
- Explicit spec conflict: a complete gym warm-up leaves 2 hard-floor jump points. Done when 4 expects green. Implemented the explicit point formula and reported the mismatch.

#### Feel check
- Best moment: the theater diagonal is too wide while the smaller original is too close. The split swap at 0.90 makes Fit and Spacing pass without changing dancer identities. The run carries changes into the current count.
- Flattest moment 1: the first warm-up layout hid half its choices in the short preview. Reworked its compact layout so all six blocks stay visible, and made the timeline show short readable block names and durations.
- Flattest moment 2: a bare plan and unexplained amber Seen light felt abstract. Added painted surface texture, tape corners, visible too-close rings, a specific blocked-seat caption, and a parallel posed audience view. Reframed the plan to keep outlying dancers clear of the inset.
- The Scout painting has at least the bar tool's visual richness. `feel-comparison.jpg` puts our Park Scout beside Snowy Mail Route; Beat Lab was also bundled and opened before building.
- The fixed sight model still limits the satisfaction of finishing a venue. No all-green solution was found with the chosen plausible sample seats. This is a content-model limitation, not a completed win path.

#### Done when
1. PASS: plan is the largest central element, with four readable lights at 1366x768 and 680x425. Every prescribed size was opened; phone uses a 375px iframe.
2. PASS for Fit/Spacing: exhaustive theater slider checks reject the original diagonal at every setting, and accept split at 0.85 and 0.90 only. Exact continuous bounds match Sources.
3. PASS rule, FAIL intended recovery: gym A2 at (0,-1.4), eye 1.0, loses dancer 6 behind dancer 1 on the same ray; C2 at (0,-4), eye 2.6, sees all. Park Circle at spread 1 goes from 0 to 1 seats seeing all six after the middle-level swap. It does not clear all nine under the supplied rule and chosen seats.
4. PASS explicit formula, FAIL conflicting example: gym defaults 5; full warm-up 2; full warm-up plus relevés 0. Park defaults 8; tempo 95% plus 12-minute preparation 1. Long holds add the adjacency point exactly as specified.
5. PASS predicates, FAIL reachable completion: gym notes pass with the proper swaps/preparation, 1.3 Window and low Circle. Park predicates check all four formations against the sprinkler. Theater split and jump notes work. Its all-nine-seats note and normal venueReady event remain unreachable in tested discrete settings. Did not relax thresholds to manufacture a pass.
6. PASS: real jittered slider drag changes Spread to 1.35 while the clock advances from count position 1.61 to 2.73. Another live run takes Window's swap and 105% tempo, bpm 117.6, at position 12.65 without stopping. Stop is immediate.
7. PASS: separate venue settings survive navigation, reset affects only the current venue, and a fresh tab restores saved tempo, swaps and warm-up.
8. PASS start/log behavior: no line during Run; only the welcome before it and result after it. Five keys at two-second intervals produce all three tooClose starts on three amber crossings. No how-to repeats. Browser speech may be cut when a newer urgent event starts.

#### Wave lessons
- Hint and voice: PASS in focused runs. Hints update synchronously, Read uses the current hint, welcomes/events use state validity and note acknowledgments use V.heard. No delayed welcome during Run.
- Focus and layout: PASS for first focus, slider editing, dancer inspection and arrow reorder; FAIL full no-scroll layout on phone; no load focus. Arrow reorder restores its button with preventScroll. Secondary lists can need scrolling on compact screens.
- Sizes/targets: PASS main prescribed focus and target checks; FAIL full phone no-scroll criterion. Main Spread and Run stay in view at all eight sizes. Phone stage is before controls. Header and HTML buttons are at least 44px; dancer hit circles have a 46px diameter before negligible viewBox fitting.
- No giveaways: PASS. This is a visible planning model, not a hidden-answer quiz. Live feedback is the specified lesson; the student weighs conflicting constraints.
- Honest numbers: PASS. Rules of thumb and centers in meters are labeled; sight thresholds and compressed seat-icon geometry are explained; risk has a full additive breakdown. Fifteen-minute overage is shown honestly, including an 18-minute bar and 15-minute target marker.
- Standards: PASS. Students adjust space/time, apply preparation to conditions, and adapt for three audience arrangements. Notes explain DA:Pr4, Pr5, Pr6 in the solo actions.
- Motion off: PASS in the focused run: no idle ring loop, no gliding, same count timing. Counts, poses and lights continue.
- Short choices: PASS for all six warm-up choices after the compact repair. All six selected blocks and twelve arrow controls fit at 680x425 after repair. Phone reorder and checks still scroll: FAIL full no-scroll criterion there.
- Resize mid-animation: PASS in the one audit, no exceptions or stuck disabled controls. The running clock survives redraws; ResizeObserver redraws current positions and preserves focused dancer ids.
- First-tap welcome: PASS standing first-action priority rule. No welcomeAfter; the kit handles first-action priority. Current controls work immediately.
- Unknown information: PASS. Scout facts are revealed by rings; the plan is an explicit model, with no hidden diagnosis.
- One look, one meaning: PASS in grayscale and normal frames. Green check versus amber exclamation, red rings plus “too close”, numbered dancers, dashed safe edge. Grayscale frame checked.
- Badge truth: PASS focused model checks. Light values come from the same points used on the plan. Safety always includes the whole piece.
- Hint changes back: PASS focused stop, live-edit and reentry checks. Mode/venue switches replace it immediately; stop and completed run give the next action.
- No answer by copying words: PASS. No answer-card activity. Notes ask the learner to change and observe the system.

#### Audit leads
- One full audit completed, exit 0: 276 repetitive mechanical leads in `_scratch/dancers-on-tour/audit/audit.md`. No second full audit. All 83 audit PNGs inspected in contact sheets 00-13.
- All eight default sizes were clean. Motion off was clean; resize mid-action had no exceptions or controls left disabled. Held-click/Enter checks had no console errors; five held clicks at two-second intervals were clean.
- Scout caption/ring overlaps (Park/Theater, compact/phone): FIXED by clamping rings clear of caption bands. Focused all-venue checks report no caption overlap at 680 and 375.
- Dancer/dancer, dancer/text and text/circle/image leads repeated across Adapt, min/max and running states: transparent 46px hit areas intentionally overlap in a dense metric plan. FIXED ambiguous pointer choice by nearest displayed center and adaptive visible circles/numbers (minimum 10.2px text). Keyboard retains individual ids. Dense real tap selects dancer 3. Small phone audience figures and dense plan readability remain review limits; coordinates were not shifted to hide actual crowding.
- Rules/privacy overlaps: FIXED section flex shrinking; expanded details bottom 971.19, privacy top 995.19 in the focused check. Rules summary below compact fold remains LEFT OPEN as secondary explanation.
- Phone Tempo, Swap and rule summary below fold: LEFT OPEN. Main Spread and Run are visible. Phone needs scrolling for these secondary controls.
- Warm-up Back to Adapt hidden/below fold and focus lost: FIXED by removing the redundant button; header Adapt remains. Reorder comes before long checks; all six blocks' twelve arrows fit at 680. Phone reorder/checks remain LEFT OPEN.
- Phone floor-card keep region (only 9% inside): FIXED by placing tapped fact, swatch and Go to Adapt before the dossier. Focused phone check: fact bottom 558.67, Go bottom 738.67 in the 812px viewport.
- Go to Adapt focus lost in each venue: FIXED explicit Spread focus with preventScroll; final Go frame inspected. Dancer/arrow reorder focus and Run/Stop keyboard paths also checked.
- Hotspot first tap speaks its fact instead of generic welcome: INTENTIONAL per STANDARDS first-action priority. Hint carries the next action; no delayed welcome. Sound-off cuts are intentional. Read speaks the current hint.
- Same-mode/venue quick-tap welcome cuts: FIXED idempotent mode/venue setters. Focused double Adapt tap logs one welcome with no cut. Five-tap event behavior remains covered by the earlier focused pacing check.
- Initial audit min/max drag fixtures returned undefined and stayed at default: fixture bodies now return arrays. Separate real-input/fixed-fixture checks verify 0.50 and 1.50. Added warm-max for the next audit; did not mislabel those original frames as extremes.
- Other focused build repairs: corrected right/left quarter-turn formation and actor facings; Stop/live hints; clarified available swaps; rescaled 18-minute timeline with 15-minute target; singular point wording. All were scoped rechecks, not a new polish or full audit.

#### Frames looked at
- Bar frames: Snowy Mail Route and Beat Lab, 1366x768, Scratch copies bundled before building.
- Initial/diagnostic Scout, Adapt and Warm up frames at 1366 and 680; every existing diagnostic PNG opened, including the early art-pending model frame.
- Full size run: Scout, Adapt and Warm up at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900. Phone modes at 375x812 in host 8775.
- Extremes, grayscale, Motion off, keyboard-only, live slider, completed run, voice pacing, warm-up arrow reorder and real drag, live tempo/swap and fresh saved-state reload frames.
- After repairs, only affected plan extremes/sizes, phone order and drag were re-shot. Home/End were unsupported by drive.py; retried those two shots with Arrow keys. No tool exception was involved.
- Focused final drive batches reported zero console errors, warnings or exceptions. Final split choice, adapted completed run, Go focus, phone Adapt and phone maximum warm-up PNGs were opened. Audit frames and leads are covered above.

#### Art made
- 6 images, 459,210 bytes total WebP art, about 448.4 KiB. Final bundle 791,315 bytes, about 772.8 KiB, under 2 MB.
- `art/venue-gym.webp`, `venue-park.webp`, `venue-theater.webp`, `swatch-wood.webp`, `swatch-grass.webp`, `swatch-marley.webp`.
- Built-in OpenAI image tool, full prompts in `art/prompts.json`; raw PNGs copied into `art/raw/`; only art.py --rekey used. All six finished images inspected at final dimensions. No redraw needed.

#### Art still to paint
- 32 people assets: stand, arms-wide, relevé, star-jump, low crouch, middle standing and step, each in front/left/back/right views. Four additional arms-wide eighth-turn views cover turning transitions. All have people:true and art tokens. No people images were generated.
- Owner decision preserved: painted dancers are the destination. Kit figures are temporary and isolated behind audienceRenderer.

#### Engine changes wanted
None. Kit files unchanged.

#### Left open
- Supplied sight-rule thresholds plus current sample-seat positions make several all-green outcomes unreachable. Exact sample seat positions were unspecified; current choices and search evidence are in handoff.md and Scratch. This needs a content decision in review.
- The gym warm-up/green example conflicts with the explicit risk formula. The warm-up checklist also has start-order/minimum-time conditions not included in warm-venue risk points; both are shown separately.
- Browser narration only, no recordings, per Build instructions. By-ear music/voice review was not performed with the muted test browser.
- Audience figures are small in the preview and phone inset. Phone Tempo/Swaps, long notes, warm-up checks and selected-block reorder can require vertical scrolling; Spread and Run remain visible.
- The audit preceded scoped repairs. Its 276 leads are answered above; a cold reviewer should rerun it. Dense transparent dancer targets intentionally overlap, and phone secondary controls still scroll.
- Park sprinkler notes check phrase formation positions, not swept transition paths.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: dancers-on-tour

#### Played

Evidence root: `_scratch/dancers-on-tour/`. One cold review pass, then scoped repairs and rechecks.
Grade-7 solo play and a projected-classroom reading: Gym Scout rings, Adapt and Run; a 15-minute warm-up; Park raised Circle and Run; Theater split/facing and Run. Strong venue paintings and precise live plan; blocked sightline goals make the finish frustrating.
#### Findings fixed

- Blocker/general: Safety became green with only an eight-minute gym warm-up, or an out-of-order plan with static holds. Safety and ready now require the existing warm-up checklist; exact numeric risk points remain unchanged.
- Should fix/general: unrelated edits praised notes that were already true. Note acknowledgments now require an actual false-to-true transition.
- Should fix/general: painted dancers deferred despite the owner's decision. Added three people:true cast atlases with six consistent identities and five teaching poses; replaced the visible kit figure behind audienceRenderer.
- Should fix/general: phone frequent controls extended well below the viewport. Packed the existing control desk beneath the plan with 44px targets.
- Polish/general: every run ended with the same generic failure and success sound. Added a personal count of phrases that retained fit, spacing and sightlines; failed runs use a neutral completion tone.
- Should fix/general: a scouting fact could continue over a different card, and result speech could survive an invalidating edit. Stopped stale speech while preserving Read priority; fixed one malformed apostrophe in the manifest. hot-facts-final.json confirms new facts wait for Read.
- Blocker/general: Motion off skipped travel collisions, improving the run recap. Separated path checking from reduced-motion pictures. path-on.json and path-off.json now return identical results.
- Blocker/general: the sprinkler note rewarded endpoint-only clearance although the default run crosses the head exactly. The final repair checks every dancer segment between formations, with the unchanged 0.75 m threshold.
- Should fix/general: stale completed-run captions survived edits/reset. Captions now invalidate with the result; actual Run then Reset returns 32 counts and preserves Park settings.
- Should fix/general: Sound restored after edits could leave mode instructions unheard. Valid current-state welcomes recover in Scout, Adapt and Warm up; all three focused logs pass.
- Should fix/general: phone selected-block arrows fell below the fold. Moved them into the warm-up builder at phone widths, preserving the wide panel layout, focus and real dragging.
- Polish/general: phone theater rings crowded each other. Separated the exits ring without reducing the art.
#### Findings left

- Blocker/general, spec conflict: supplied visibility thresholds make whole-venue all-green and theater note 3 unreachable. No threshold was relaxed. Independent calculations/search in numbers-review.json and an exact current-seat, every-slider-step check in canonical-seat-check.json. The straight Park travel paths also lack a joint Fit/Spacing/sprinkler solution in the discrete control search; sprinkler-review.json. These remain blockers, not PASS results.
- Should fix/general, spec conflict: gym warm-up cannot erase its two hard-floor jump points, contrary to Done when 4. Preserved the explicit, safer formula.
#### Break it

Before repairs, real held taps set gym [Pulse, Dynamic] to eight minutes and Safety 0/green; theater [Dynamic, Pulse, Holds, Feet] to thirteen minutes and Safety 0/green. After repairs both retain their honest zero point total but show amber Prep and ready=false; correctly ordered theater [Pulse, Dynamic, Feet] still shows green. Evidence: cheats-after.json.
Original/split theater diagonal: swept every slider step; original never passes Fit and Spacing together, split does at 0.85 and 0.90 only. A single green Seen light at too-small spread does not pass spacing or ready.
Warm-up toggles cannot add duplicate blocks. There is no saved best score, quiz, hidden-answer badge or reflection gate. Endpoint-only edits do not clear a run if transitions fail.

- Sprinkler cheat: cold Park Run kept the note ticked with endpoint minimum 1.0 m, while dancer 4 crosses the head on Window-to-Circle travel (minimum 0.0 m). Independent geometry in sprinkler-review.json; post-fix default path is rejected and a geometrically clear probe is accepted; sprinkler-path-after.json. A sweep finds no all-fit/all-spaced Park solution with those straight travel paths, another authored-constraint conflict.
#### Voice walk

Held clicks were 0.12 s at a 2 s pace. Cold logs are play-gym.json, play-warm.json, play-park.json, play-theater.json and cold-warm-filled.json. Final main path: plain stage tap, floor ring, Go to Adapt, Warm up, Pulse, Dynamic, Feet, Key moves, Adapt, Diagonal, Run. Heard in order: Scout welcome, gym floor fact, Adapt welcome, Warm up welcome, earned gym-note event, afterRun. No speech during Run. main-final-post.json. Sound-off edits followed by Sound on also recover the current instructions in each mode; sound-*-recovery.json.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Scout, Adapt, Warm up welcomes | how | 1 each on main path | 1 each |
| tooClose | event | 5 crossings | 5 |
| staticHow | how | 1 after unsafe ordering | 1 |
| afterRun | how | 1 per page | 1 |

Five crossing evidence: event-repeat-after.json; static ordering: static-order-voice.json. Side Read/reset/Sound-off Read logs checked; a main-path navigation fixture failed once because it reloaded its own evaluation context, then was replaced with a smaller non-navigating fixture. One initial cheat drive lost Chrome; bounded retry succeeded. No tool exceptions in successful focused runs.
#### Facts checked

- Formations, dimensions, nearest distances, all venue spread intervals and 17.142857 seconds: independently recomputed from the authored coordinates in spec.md; numbers-review.json.
- Warm-up sequence and dynamic movement: IADMS, The Importance of a Good Warm-Up, revision June 22, 2025: https://iadms.azurewebsites.net/media/glfba5xu/iadms-resource-paper-the_importance_of_a_good_warm-up.pdf
- Hard floors and sprung floors: Ausdance Safe dance practice, https://ausdance.org.au/articles/details/safe-dance-practice; CDMT Safe Dance and Floors, https://cdmt.org.uk/safe-dance-and-floors/
- Long static stretching can acutely affect power, depending on dose/context: Behm and Chaouachi 2011, PMID 21373870, https://pubmed.ncbi.nlm.nih.gov/21373870/. This is not a universal ban on all static stretching.
- DA:Pr4, 5, 6: NCAS Dance handbook, https://www.nationalartsstandards.org/; planning activities support spatial design, preparation decisions and adapting to venues. They do not demonstrate physical technique by themselves.
- Venues, temperatures, distances, safety points, minutes, blanket/seat eye heights, obstacles and sun direction are fictional model inputs from spec.md, not universal guidance. Fit and sight rules are explicitly labeled rules of thumb.
- Hand checks of sight rule: gym A2, x 0/z -1.4/eye 1.0, loses Wedge dancer 6 behind dancer 1; C2, x 0/z -4/eye 2.6, sees all six. Park Circle at spread 1: low 0/9, middle 1/9 under the same model.
- WCAG 2.1 contrast, independently recomputed: ink/background 15.47, ink/panel 13.78; muted 8.05/7.17; brand 11.36/10.13. contrast-review.json uses the W3C relative-luminance formula.
#### Sensitivity

Bodies and safe preparation need review. Painted cast varies skin tone, hair and lean-to-broad builds without assigning cultural or gender roles. Inspect anatomy and ordinary forefoot-supported releve, consistent identity, low/middle heights, and representation. No physical task or body ranking; the invented dance claims no cultural lineage. Contact sheet: painted-contact.jpg.
#### Flattest moment left

The new phrase-specific recap lifts the former generic end-of-run message, and the painted cast lifts the weakest art.
The specified visibility goal cannot be completed. Repeated amber after a good fit is the largest remaining frustration and requires a spec decision.
#### Graphics

Kept six strong venue/surface paintings. Added front/back/right cast atlases, mirrored left; five poses reuse arms-wide as jump preparation and the traveling step as middle-level Circle. All atlases people:true, generated with built-in OpenAI image tool; front releve redrawn once. Raw assets and atlas prompts retained; 32 superseded prompt records are archived outside the active nine-asset queue. Final bundle 1,567,093 bytes (about 1530.4 KiB); nine finished WebPs total 1,043,356 bytes. Contact sheet and final-size stage frames opened.
#### Audit

One full audit completed, exit 0, within the 40-minute cap, port 9961, host 8765: review-audit/audit.md, 279 leads and 95 frames, all inspected (review-audit-contact-00 through -15). No second full audit.

- Default eight sizes, Motion off, resize stress, console checks, repeated clicks and quick taps completed. Compact and phone states were also inspected individually.
- Confirmed and fixed: phone warm-up reorder controls and clipped menu edges; close theater rings. Post-fix all 18 warm-up targets end by y=660 at 375x812 and remain at least 44px. Actual drag and 375-to-760-to-375 resize pass with focus retained and scrollY=0.
- Dense plan overlaps are transparent 46px targets over exact metric positions; real dense tap plus Enter twice selects dancer 3 correctly. Visible numbers stay legible; bodies were not shifted to disguise crowding.
- Closed-disclosure text/privacy overlaps are not painted. The open-disclosure check measures a 24px gap. The optional rule summary and long preparation checks may scroll on short screens; the short choice sets and frequent controls fit.
- Five first-ring welcome leads follow STANDARDS first-action priority: the ring speaks its own fact and skips the generic welcome. The main stage-first path hears Scout, Adapt and Warm up once each.
- Successful direct-file drives have no console errors. HTTP wrapper shots log only its favicon.ico 404, not a tool resource failure. The one-file tool has no external resource URLs. All started browsers/servers are closed and host.html removed.
- Live real drag: spread 1.35 while clock position advances 0.30 to 1.50. Live Window swap and 105% tempo remain running. Reset clears completed status and preserves Park; run-status and post-resize evidence.
- Final receipt: review-verification.json. The audit preceded these scoped final repairs; only touched states and the main voice path were re-shot.
#### Left open

Not release-ready: the spec-level completion conflicts above remain. Browser fallback narration is tested by starts/logs in muted Chrome; recorded-voice and by-ear quality are not claimed.
No questions were asked in the unattended session. Chose explicit formulas over conflicting worked examples, preserved the specified thresholds, used five poses and three views to minimize redundant art, kept browser narration per the no-recording rule. No commits; manual file writes stayed in the allowed tool/scratch folders. Generated-image service outputs were copied into the tool as the build rules require.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Dancers on Tour: review handoff

#### Structure
`src.html` contains styles, the original piece and venue data, model functions, the audienceRenderer adapter, the plan, warm-up controls and events. `window.__tool` exposes the model and voice log. All review scripts and evidence are in `_scratch/dancers-on-tour/`.

#### Painted dancers
The owner asked for painted dancers. Three generated `people: true` cast atlases now supply five poses in front, back and right profile; right mirrors for left. Six dancers retain their identity, skin, hair, build and clothing across the set. The middle step doubles as the raised Circle, and arms-wide doubles as jump preparation. Turning uses four readable facing keyframes. No kit code figure is displayed.

`PAINTED_POSES`, `painted-dancers.json` and `audienceRenderer.setup/resize/draw` form the swap boundary. The JSON holds tight [x,y,width,height] cells by view, pose row and dancer index. Keep raw atlas dimensions 1086x1448 or update the adapter. Height is normalized against each dancer's standing row so a low crouch stays low. Projection, independent dancer position and depth ordering still use Dance.floor. The owner contact sheet is `_scratch/dancers-on-tour/painted-contact.jpg`.

#### Review repairs
- Low point totals no longer turn Safety green when the warm-up is too short, out of order or includes long holds. Points remain the spec's exact sum. The complete checklist feeds Safety and ready, as the warm-up mode requires.
- Note praise fires only when an edit actually changes a note from unmet to met. Default notes do not earn praise after unrelated warm-up taps.
- A completed run recaps the number of phrases that kept fit, spacing and sightlines throughout the run. Failed runs use a neutral completion sound rather than the success chime.
- Phone Adapt packs Spread/Run/Reset, Front, Tempo and Swaps into a compact control desk beneath the plan, retaining 44px targets.
- All existing venue paintings, surface textures, music, precise plan geometry and live edits remain.

#### Spec conflicts left open
Do not relax the sight thresholds to manufacture completion. Independent review recomputed the formation numbers and searched possible low sample seats within the stated audience areas; no common low seat could see all four fit/spaced/note-compliant formations. With the current sample seats no whole venue can meet all-green. In particular the theater's all-nine-seat note is unreachable. `numbers-review.json` records the search assumptions. This is a blocker requiring a content decision under CODEX-REVIEW section 3.

The explicit gym risk formula leaves 2 hard-floor jump points after a complete warm-up, whereas Done when 4 says that preparation should make it green. Kept the explicit formula and the safer amber result. A warm-up does not remedy floor impact. The distances, minutes, temperatures and points are authored model thresholds, not medical prescriptions.

The park note now checks every straight travel segment as well as the four formations. Default endpoint clearance is 1.0 m, yet dancer 4 crosses the sprinkler exactly between Window and Circle. The repaired check rejects that path. A discrete search found no joint Fit/Spacing/sprinkler solution at the available controls with the current straight paths. That is another authored-constraint conflict; do not clear it by pretending endpoint clearance proves travel clearance.

#### Voice
Curio.voice uses wise-mentor, with browser fallback and no recorded clips. All fixed lines are in voice/lines.json. Run hushes narration and intercepts Read, as the spec requires. The main path and side/repeat logs are in review scratch. How-to lines are once per page; tooClose remains an event on each transition into inadequate spacing.

#### Sensitivity
Bodies and preparation are involved. Inspect the full painted contact sheet for anatomy, ordinary releve rather than pointe, consistent identities and natural representation. No body is scored or presented as the ideal dancer. The cast does not portray every ability; no unsupported claim of universal representation is made. The invented dance claims no cultural lineage.

#### Engine changes wanted
None. No kit, scripts, docs or other tools were changed.

#### Verification
See codex-review.md for the final bounded audit, confirmed leads, frame evidence and remaining conflicts. No commits were made.


#### Final review checks
One full review audit completed within 40 minutes: 279 mechanical leads, 95 frames. Every frame was inspected through contact sheets and focused full-size views. All default sizes, Motion off, resize stress, console checks and held/quick click checks completed. Most leads measure overlapping transparent dancer targets or unpainted closed-disclosure text. Dense real taps select the nearest dancer; an expanded disclosure leaves 24px before privacy text.

Post-audit repairs and scoped checks: phone warm-up menu plus all twelve reorder arrows fit above 660px at 375x812; real drag reorders; resize moves the list between stage and panel without losing focus or scrolling. Theater rings are separated. Sound-on after edits recovers valid instructions in all three modes. The repeated main voice walk starts all three mode instructions once and stays silent during Run. Run captions clear on edits/reset; reset preserves other venues. Live spread, swap and tempo edits keep the clock moving.

The active art list contains nine delivered images. The 32 superseded single-figure prompt records are preserved under superseded_assets, rather than left in the active paint queue. Verification receipts and final bundle SHA-256 are in `_scratch/dancers-on-tour/review-verification.json`. No second full audit was run. Long explanatory notes and preparation checks still scroll on short screens.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
