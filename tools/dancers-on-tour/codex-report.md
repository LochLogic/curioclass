# Codex report: dancers-on-tour

## Built
- Scout, Adapt and Warm up for all three venues, with independent saved settings and venue reset.
- Original six-dancer formations, per-phrase spread/swaps, four fronts, live tempo, run counts, transitions and synthesized music.
- SVG plan with safe margin, surface textures, obstacles, numbered dancer inspection, collision rings and four live lights. Kit figures in an audience inset.
- Warm-up blocks toggle, reorder by arrows or real pointer drag, show duration and exact risk-point breakdown.
- All required files made. No commits, no changes to kit/docs/scripts/other tools, no polish round. Temporary evidence stays in Scratch.

## Numbers check
- Scratch `numbers.json` recomputes every source formation width, depth, closest distance and feasible spread interval. The spec's rounded results match.
- Exact theater split interval: 0.8320503 to 0.9285714, so slider settings 0.85 and 0.90 work. Original diagonal needs at least 0.6708204 but fits only through 0.65.
- 32 counts at 112 bpm = 17.142857 s. Four setup counts and three transition counts give 20.89 s at 100%, unchanged by Motion off.
- WCAG ratios: ink/background 15.47, ink/panel 13.78, muted/background 8.05, muted/panel 7.17, brand/background 11.36, brand/panel 10.13. Dark text/brand 11.36.
- Sixteen focused model checks pass in `functional-results-final.json`, including safety totals, both hand-checked seats, note predicates and venue reset.
- Explicit spec conflict: a complete gym warm-up leaves 2 hard-floor jump points. Done when 4 expects green. Implemented the explicit point formula and reported the mismatch.

## Feel check
- Best moment: the theater diagonal is too wide while the smaller original is too close. The split swap at 0.90 makes Fit and Spacing pass without changing dancer identities. The run carries changes into the current count.
- Flattest moment 1: the first warm-up layout hid half its choices in the short preview. Reworked its compact layout so all six blocks stay visible, and made the timeline show short readable block names and durations.
- Flattest moment 2: a bare plan and unexplained amber Seen light felt abstract. Added painted surface texture, tape corners, visible too-close rings, a specific blocked-seat caption, and a parallel posed audience view. Reframed the plan to keep outlying dancers clear of the inset.
- The Scout painting has at least the bar tool's visual richness. `feel-comparison.jpg` puts our Park Scout beside Snowy Mail Route; Beat Lab was also bundled and opened before building.
- The fixed sight model still limits the satisfaction of finishing a venue. No all-green solution was found with the chosen plausible sample seats. This is a content-model limitation, not a completed win path.

## Done when
1. PASS: plan is the largest central element, with four readable lights at 1366x768 and 680x425. Every prescribed size was opened; phone uses a 375px iframe.
2. PASS for Fit/Spacing: exhaustive theater slider checks reject the original diagonal at every setting, and accept split at 0.85 and 0.90 only. Exact continuous bounds match Sources.
3. PASS rule, FAIL intended recovery: gym A2 at (0,-1.4), eye 1.0, loses dancer 6 behind dancer 1 on the same ray; C2 at (0,-4), eye 2.6, sees all. Park Circle at spread 1 goes from 0 to 1 seats seeing all six after the middle-level swap. It does not clear all nine under the supplied rule and chosen seats.
4. PASS explicit formula, FAIL conflicting example: gym defaults 5; full warm-up 2; full warm-up plus relevés 0. Park defaults 8; tempo 95% plus 12-minute preparation 1. Long holds add the adjacency point exactly as specified.
5. PASS predicates, FAIL reachable completion: gym notes pass with the proper swaps/preparation, 1.3 Window and low Circle. Park predicates check all four formations against the sprinkler. Theater split and jump notes work. Its all-nine-seats note and normal venueReady event remain unreachable in tested discrete settings. Did not relax thresholds to manufacture a pass.
6. PASS: real jittered slider drag changes Spread to 1.35 while the clock advances from count position 1.61 to 2.73. Another live run takes Window's swap and 105% tempo, bpm 117.6, at position 12.65 without stopping. Stop is immediate.
7. PASS: separate venue settings survive navigation, reset affects only the current venue, and a fresh tab restores saved tempo, swaps and warm-up.
8. PASS start/log behavior: no line during Run; only the welcome before it and result after it. Five keys at two-second intervals produce all three tooClose starts on three amber crossings. No how-to repeats. Browser speech may be cut when a newer urgent event starts.

## Wave lessons
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

## Audit leads
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

## Frames looked at
- Bar frames: Snowy Mail Route and Beat Lab, 1366x768, Scratch copies bundled before building.
- Initial/diagnostic Scout, Adapt and Warm up frames at 1366 and 680; every existing diagnostic PNG opened, including the early art-pending model frame.
- Full size run: Scout, Adapt and Warm up at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900. Phone modes at 375x812 in host 8775.
- Extremes, grayscale, Motion off, keyboard-only, live slider, completed run, voice pacing, warm-up arrow reorder and real drag, live tempo/swap and fresh saved-state reload frames.
- After repairs, only affected plan extremes/sizes, phone order and drag were re-shot. Home/End were unsupported by drive.py; retried those two shots with Arrow keys. No tool exception was involved.
- Focused final drive batches reported zero console errors, warnings or exceptions. Final split choice, adapted completed run, Go focus, phone Adapt and phone maximum warm-up PNGs were opened. Audit frames and leads are covered above.

## Art made
- 6 images, 459,210 bytes total WebP art, about 448.4 KiB. Final bundle 791,315 bytes, about 772.8 KiB, under 2 MB.
- `art/venue-gym.webp`, `venue-park.webp`, `venue-theater.webp`, `swatch-wood.webp`, `swatch-grass.webp`, `swatch-marley.webp`.
- Built-in OpenAI image tool, full prompts in `art/prompts.json`; raw PNGs copied into `art/raw/`; only art.py --rekey used. All six finished images inspected at final dimensions. No redraw needed.

## Art still to paint
- 32 people assets: stand, arms-wide, relevé, star-jump, low crouch, middle standing and step, each in front/left/back/right views. Four additional arms-wide eighth-turn views cover turning transitions. All have people:true and art tokens. No people images were generated.
- Owner decision preserved: painted dancers are the destination. Kit figures are temporary and isolated behind audienceRenderer.

## Engine changes wanted
None. Kit files unchanged.

## Left open
- Supplied sight-rule thresholds plus current sample-seat positions make several all-green outcomes unreachable. Exact sample seat positions were unspecified; current choices and search evidence are in handoff.md and Scratch. This needs a content decision in review.
- The gym warm-up/green example conflicts with the explicit risk formula. The warm-up checklist also has start-order/minimum-time conditions not included in warm-venue risk points; both are shown separately.
- Browser narration only, no recordings, per Build instructions. By-ear music/voice review was not performed with the muted test browser.
- Audience figures are small in the preview and phone inset. Phone Tempo/Swaps, long notes, warm-up checks and selected-block reorder can require vertical scrolling; Spread and Run remain visible.
- The audit preceded scoped repairs. Its 276 leads are answered above; a cold reviewer should rerun it. Dense transparent dancer targets intentionally overlap, and phone secondary controls still scroll.
- Park sprinkler notes check phrase formation positions, not swept transition paths.
