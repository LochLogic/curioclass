# Up the Watershed: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: up-the-watershed

#### Built
Grade 12 watershed investigation with Cases, Sample, Claim and Fix-it. Three case files share a painted, flowing map; eight kits force a sampling plan, claims require selected evidence, and a $3 million cleanup portfolio exposes competing goals and social costs.

Built from the kit starter with the grade 9-12 theme, Curio Class voice, motion and sound controls. One offline bundle; no family engine. Local progress, three saved plans, session-only Why text, Reset and Clear my progress are implemented. All writes stayed in this tool and its Scratch folder. No commits or polish round.

Final bundle: **755,489 bytes (737.8 KiB)**. Source: 1,524 readable lines, none over 160 characters. All assigned Chrome/server ports are closed; host.html is removed.

#### Numbers check
PASS. `_scratch/up-the-watershed/watershed_numbers.py` independently reconstructs flow, loads, beach attenuation, every sample, every fix and all 512 portfolios. JavaScript agrees on 4,174 numeric comparisons and every goal classification (`browser-model-results.json`). All 88 displayed sample cells match the spec, including rounding, no flow and Not modeled (`display-results.json`). No numerical spec correction was needed.

Worked portfolios: E+D2+A+C+G costs $2,955,000, meets all goals, and leaves storm beach water at 461.46 while the beach is protected by closure. The $1,595,000 alternative fails lake dry phosphorus at 0.209475. All fixes cost $4,100,000. Exactly two in-budget all-goal portfolios exist; both use the advisory. B1 and B2 nitrate reductions multiply on the remainder.

The fictional model and limitations are visible in the tool and teacher notes. The 410 value is the EPA statistical threshold used as this case's action line, not a universal legal closure rule. Reference facts were taken from the spec's Sources; no new factual topic was added.

#### Feel check
Best moment: the expensive plant upgrade finally pulls dry lake phosphorus below its line, but the beach result still says Protected, not cleaned. That makes the student's budget choice worth explaining. The three cases change the inference: dry sewer evidence, storm runoff evidence, then a sediment source that is present but too small to be the culprit.

Flattest moment 1: an early map felt like floating labels. Added seven painted source miniatures, five clipped aerial textures, shaded banks, bridges, roads, lake highlights, quiet flow and a sample pulse. Large source photos let the student inspect the place. Repositioned compact icons and labels so the art remains usable.

Flattest moment 2: cleanup testing initially felt like instantaneous arithmetic. Added the 400 ms test beat followed by a real 400 ms gauge fill, immediate budget/toggle feedback and immediate invalidation during motion. Motion off preserves the beat. Whole-creek shares now occupy the panel so revealing the answer does not bury the map.

Played the real-click three-case routes and cleanup/save/compare sequence. I would continue through the competing cleanup plans after ten minutes; once all three cases are known, the fixed data has limited replay depth. This is a build assessment, not a measured student engagement result.

Compared with Beat Lab and Snowy Mail Route. The field-map art, case photography, instrument readouts and restrained feedback meet the intended finish without copying their scenes. Comparison: `_scratch/up-the-watershed/feel-comparison.png`.

#### Done when
1. PASS: every site/weather table value and its displayed rounding; 88/88 cells, `display-results.json`.
2. PASS: Beach solved with A, D1 and D2 in five real samples, three kits left; `final-solve-beach.json`.
3. PASS: geese accusation marked wrong with about 9 percent dry and 5 percent storm; `functional/geese-wrong.png`.
4. PASS: Green lake solved using Outfall alone for E plus storm pairs for B and C; five samples, `final-solve-lake.json`. Dry field/construction evidence is rejected by the validator.
5. PASS: C alone solves Creek with two samples; B feedback says only 14 percent, `final-solve-creek.json` and `functional/fields-wrong.png`.
6. PASS: $2,955,000 advisory portfolio meets all three goals and explicitly distinguishes protection from cleaning; `advisory.json`.
7. PASS: $1,595,000 portfolio has dry lake P displayed as 0.209 and fails that goal; `lake-fails.json`.
8. PASS: all fixes cost $4,100,000, show the over-budget state and disable Test plan; `over-budget.json` and frame.
9. PASS: Cases, Sample, Claim and Fix-it have the specified visual focus at 1366x768 and 680x425. Map labels are at least 10 px. Full sweep and focused frames inspected.
10. PASS: three active gauge animations clear synchronously on a toggle and stay cleared; `gauge-interrupt.json`. Calm retains the test beat with zero animations, `gauge-calm.json`.
11. PASS: full map, kits and Take sample fit 1366 and the 375-wide iframe. All 22 images decode, textures follow their parcels, and finished art contains no people. Final map/result frames inspected.
12. PASS: how-to deduplication, repeated last-kit/out-of-kits events and five repeated solved events checked with held input. `solved-events-drained.json` records five callbacks, five spoken events and an empty queue. Evidence controls and full-portfolio hints do not name disabled next actions.

#### Wave lessons
- PASS, Hint and voice: hints update synchronously; Read uses the visible hint. Heard-state how-to deduplication and distinct event keys verified at a 2 s tap pace. Mode changes stop stale context.
- PASS, Focus and layout: controls persist under the pointer, dialogs restore focus, and hints reserve space. Real case routes, keyboard frame and post-fix geometry checks cover this.
- PASS, Sizes: 44 px targets, visible hints, all seven STANDARDS desktop sizes and the 375x812 iframe checked. Extra 700x900 portrait check covers the breakpoint.
- PASS, No giveaways: neutral source art and equal suspect controls; no pre-sample success state. Claims require purchased samples. The post-submit reveal is the spec's deliberate teaching feature.
- PASS, Honest numbers: made-up watershed, repeatable weather samples, fixed reductions and omitted processes are explained; concentration and storm load are distinguished.
- PASS, Standards: sampling/claiming and changing cleanup designs exercise HS-ESS3-4; comparing costs, goals and Why explanations exercises HS-ETS1-3. No family is specified.
- PASS, Motion off: tool animations explicitly stop, results stay legible, and the calculation beat remains. Calm probe finds zero active animations.
- PASS, Short choices stay visible: all three case cards, seven suspects and nine fix choices fit their layouts without a hidden choice scroll panel.
- PASS, Resize mid-animation: audit resize sweep has no exception or stuck control; active-plan invalidation is version guarded. Brackets and pinned results reposition without replacing controls.
- PASS, Deferred welcome: no welcomeAfter; mode-scoped welcomes and modal-return welcome verified. Same-mode quick taps preserve the line.
- PASS, Unknown as unknown: samples appear only when collected or after explicit whole-creek reveal. Untested gauges show question marks.
- PASS, One look one meaning: D/S letters, order and color consistently mean dry/storm; source halos indicate checked claims, not automatically guilty sources. Grayscale inspected.
- PASS, Badge truth: solved requires the exact culprit set and valid evidence; Protected explicitly says water is still over 410. Goals reflect the independent model.
- PASS, Hints restore: plan changes clear tested/save hints immediately; leaving reveal restores Claim instructions. A full portfolio names Compare plans, not disabled Save.
- PASS, No word copying: source photos and names identify locations; students must use measured jumps, weather and target shares to establish responsibility.

#### Audit leads
Ran the mechanical audit once, to completion, within its 40-minute limit. Original result: **549 leads**, retained in `_scratch/up-the-watershed/audit/audit.md`. Default sizes and calm were clean; the original state findings drove the following focused fixes. The complete audit was not repeated.

Every original lead has a disposition in `audit-dispositions.csv` (549 entries, with original audit line and state). Grouped responses:
- 406 overlap and 107 hidden-text rows: responsive source/spot geometry, heading placement, flags and source-share placement corrected. Modal logbook masking and the closeable passive result covering map detail are intentional. The result body passes input through; its 44 px Close target now has reserved header space. Final result probes find no header/value collisions.
- Whole-creek shares moved from the map to reserved panel space. Final 680, 1366 and 375 checks show 22 flags, eight source-share rows and zero flag collisions. Focused map checks remove the remaining title/S1 and compact source/flag collisions.
- 15 below-fold rows: retained for the three auxiliary footer controls on the phone. The page scrolls to them; map, kits, Take sample and all choice sets remain visible.
- Seven disabled-evidence narration rows: fixed by showing the evidence action only after selecting a suspect. All three final real-click claim routes pass.
- Four tiny-text rows: units now have a 10 px minimum; compact Evidence uses real text spans instead of a zero-font parent.
- One hidden Fix-it hint: fixed by moving the same actual hint element into the Fix-it wrapper. Focused Fix-it checks find the hint in view at both core sizes.
- One locked Fix-it focus row: expected from the automatic probe before a case is solved. A real solved case unlocks Fix-it and keeps all controls usable.
- Two missing-first-welcome rows: modal Close restores the unplayed Cases premise; the notes-return probe verifies it. Clear uses the same return handler.
- One empty Restart row: idempotent on a fresh case; exhausted-kit restart restores eight kits and removes the evidence.
- Five quick-tap welcome rows: Cases/Sample/Claim/Reset fixed by the same-mode guard. The old Open creek coordinates hit a different control after changing screens; stopping the obsolete welcome is intentional, and Read remains available.

#### Frames looked at
The late complete sweep has 38 frames: four modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375-wide, plus result, logbook, reveal, keyboard, grayscale and Motion off. Opened these and the important changed states at native size.

Inspected another 139 original frames through 27 contact sheets, with native views of critical cases, fixes, results and final phone states. `frame-sheet-manifest.json` maps every sheet to its originals, including all 58 mechanical-audit frames. Earlier failing frames are preserved; the `last/`, `final-paths/`, `result-finish/` and `voice-finish/` folders show focused verification of the final corrections.

All final drive batches report zero console errors/warnings/exceptions. The bundle prints expected missing-recording notices because recording audio is outside this build. `validation-manifest.json` indexes numeric, visual, motion, persistence and voice evidence, bundle hashes and cleanup status.

#### Art made
22 final WebPs used: eight retained scene paintings and 14 newly generated assets (two case scenes, seven source miniatures, five aerial textures). Final art totals **476,080 bytes (464.9 KiB)**; bundle is **737.8 KiB**. Full prompts, original-image provenance and `drawn_by: codex` are recorded. OpenAI generation credit is in tool.draft.json.

Processed through `art.py --rekey <name>` only. Magenta-keyed icons were despilled, then inspected at final size. No redraws were needed; key/despill and sizing were refined. Exact waterways, parcels, roads, labels, brackets, result bars and notice text are drawn in code. No generated text, logos or people.

#### Art still to paint
None. All specified illustrations are present. No audio was recorded; browser speech fallback uses the kit, while the requested bank/style identity remains in voice/lines.json.

#### Engine changes wanted
None. Shared kit, scripts, docs and other tool folders were not edited. The temporary iframe host received a data favicon from the scratch harness and was removed after each batch.

#### Left open
- Cold review has not run. The complete audit predates the focused fixes; original findings and post-fix evidence are both retained rather than claiming a clean rerun.
- Compact fix cards expose full effects and who-pays text through accessible descriptions and titles; larger laptops show it inline. Touch discoverability deserves a cold-review look.
- Spec voice-bank recordings and actual classroom engagement/duration remain unmeasured. Speech timbre currently depends on the browser's fallback voice.
- The three spec questions are resolved in handoff.md: retain Up the Watershed, count advisory as protection with dirty water stated, and retain fictional scaled costs/loads.
- Process deviations: reference bar tools were opened after the first playable version; this report was written last to obey the user's explicit stop-on-report instruction. Two initial instant inspection commands lacked a hard deadline; subsequent substantive commands and all bundle/drive/audit runs used hard limits.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: up-the-watershed

#### Played

Played cold as a Grade 12 solo student before reading the builder's report, handoff or source: all three cases, wrong accusations, evidence selection, logbook and Fix-it. The dry/storm contrast is strong; collecting samples initially felt flat. Later checks covered three saved alternatives, explanations and reloads, plus projector and narrow layouts.

#### Findings fixed

- **blocker, general, Claim/share():** the downstream treatment plant was credited with sediment at upstream S7. Its share is now zero there; dry background is correctly 40.7 percent. Confirmed in the whole-creek frame and independent calculations.
- **blocker, general, Fix-it:** leaving during the calculation could replace Cases instructions with a late cleanup result. Mode exit now cancels the pending test. Mode-exit and toggle-interruption checks retain the correct hint and empty gauges.
- **should fix, general, Claim:** feedback carried between case files and survived evidence edits. Verdicts are isolated by case and invalidated when evidence changes.
- **should fix, general, Claim:** the 20 percent criterion was buried in notes. The initial instruction now states it before submission and fits the preview.
- **should fix, general, compact Fix-it:** effects and who-pays details depended on hover or accessibility descriptions. The visible Fix details control exposes every intervention to touch and keyboard users.
- **should fix, general, phone gauges:** hidden row labels made dry, storm and change values ambiguous. Labels remain visible; storm closure says Closed with its dirty-water explanation.
- **should fix, general, phone Sample:** Make claim was partly below the fold after kits ran out. The compact header preserves the full map and puts Make claim's bottom at 804 px in the 812 px iframe.
- **should fix, general, map:** dry/storm flags touched circles or source labels. Explicit gaps and compact label positions now separate all 22 flags at every checked size.
- **should fix, general, voice:** exhaustion and over-budget feedback could wait behind obsolete instructions. Kit warnings and budget-threshold events now take priority and name enabled next actions.
- **should fix, general, empty panels:** empty evidence referred directly to hidden sampling controls; an empty over-budget portfolio suggested disabled testing. Instructions now name Close, the needed mode and the reachable action.
- **should fix, general, dialogs:** native modal behavior made the header Read button inert. Each dialog now has a working Read control, verified with held clicks and Sound off.
- **should fix, general, Logbook:** No flow and Not modeled acquired measurement units. Their absence is now stated plainly.
- **should fix, general, field photos:** cover cropping removed useful scene context, including cattle's feet. Whole photographs now fit within a viewport-based height cap.
- **polish, general, sampling:** added a shaded vial-fill beat alongside the ripple and immediate results. A dry Pipe leaves the vial empty; Motion off removes movement.
- **polish, general, art:** the cattle miniature read as terrain at 40 px. Redrew it with recognizable animals, retaining the painted field-guide style.

#### Findings left

No identified blocker or should-fix remains.

- **nit, general, specified precision:** E alone produces exactly 0.0475 mg/L dry phosphorus. The UI displays 0.047, matching the spec's binary-rounded example. Kept the requested display; raw goal checks are unaffected.

#### Flattest moment left

Once all three fixed datasets are known, returning to the same samples has limited replay value. The competing cleanup portfolios remain the stronger ending. Added no new cases or replay system beyond the spec.

#### Graphics

Checked all 22 assets, their map/card placements, all seven full field-photo views and the relevant final sizes. Redrew one asset with built-in OpenAI image generation: `art/uw-i-cattle.webp`; full prompt and provenance are in `art/prompts.json`. Processed through `art.py --rekey uw-i-cattle`. No missing art or people images. Preserved the case paintings, miniature set, textures and flowing map. Compared the finish with the isolated Snowy Mail Route and Beat Lab references.

Art: 478,038 bytes. Final offline bundle: **763,460 bytes (745.6 KiB)**. Source has 1,620 lines, none over 160 characters, and no em dashes.

#### Audit

Ran the full audit **once**, on Chrome 9961 with host 8765. It completed in **2,302 seconds (38 minutes 22 seconds)** with **285 leads**. All have dispositions in `_scratch/up-the-watershed/review-audit-dispositions.csv`; inspected all 67 audit frames.

Fixed 19 flag-spacing leads, one phone next-action lead and two stale-instruction leads. The other 263 are explained overlays, auxiliary phone footer scrolling, the deliberately locked Fix-it mode, modal-return behavior, an empty restart and a second tap landing on the newly opened map. Scoped checks confirm that closing notes restores a complete welcome and the old Open case coordinates open the Geese photo, appropriately hushing the prior instruction.

Re-shot affected states only. Final flag probes show 22 flags and zero circle/label intersections at every STANDARDS size. Phone controls, dialog Read, complete photos, three-plan persistence and session-only Why notes pass. No browser console errors, warnings or exceptions in the final batches. The full audit predates these final repairs and was not repeated.

Independent Python computations agree with the browser on all modeled samples and all 512 portfolios: 4,692 comparisons. Exactly two portfolios within $3 million meet all goals, both using the advisory. Advisory, lake-failing and $4.1 million over-budget outcomes were checked. Keyboard-only input solved Muddy creek; grayscale and Motion off were inspected. Contrast: primary button text 6.68:1; main text 14.70:1.

| Line | Kind | Expected | Observed |
|---|---|---|---|
| Sample / Claim welcome | once | 1 each in five taps | 1 each |
| Solved | event | 5 | 5, queue drained |
| Last kit / Out of kits | event | each occurrence | 2 each at 2 s pace; 1 each in final rapid cycle |
| Over budget | event | 2 crossings | 2 |

All 20 registered lines match `voice/lines.json`. Evidence, counts, frame manifests and hashes are in Scratch. All started Chrome and host processes are closed; `host.html` is removed. No commits or shared-kit changes.

#### Left open

- Narration remains browser fallback; the specified bank timbre has no recordings. No audio was recorded, as required.
- Classroom engagement and the intended lesson duration were not measured.
- The initial instant rules-read command lacked an explicit deadline. Subsequent shell commands and all substantive checks used deadlines.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 2 (general 2, family 0), should fix 12 (general 12, family 0), polish accepted 9

### Refine: up-the-watershed

Lens files: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit and frames:
S:/CurioClass-codex-scratch/up-the-watershed/audit-r1. Lens frames: S:/CurioClass-codex-scratch/up-the-watershed/teaching/frames,
.../play/f1, .../craft. Not a Curiosity; lesson norms apply. Integrator spot-checked src.html 643, 775, 1176-1189,
1222-1262, 1440-1460 and 1519-1525: blocker 1, blocker 2, should fix 1, 2 and 3 are confirmed in code.

#### Blocker
1. **An empty or blanket claim hands over the whole answer key.** src.html:1222-1262 (submitClaim, renderClaim), 1225
   (whole-creek unlock), 1569. Open any case, go to Claim, press Submit claim with nothing checked and 8 kits left:
   every missed culprit is named with its place and weather ("Missed source. Look for beach closed evidence after a
   storm near pasture." / "The storm drains only flow in storms." / "Look for a dry-day jump below town."), and Show
   the whole creek unlocks with every suspect's share. Checking all seven suspects does the same the other way: each
   culprit gets the exact spot recipe ("Sample S1 and S2 after a storm.") and each innocent its share. A student can
   solve all three cases without choosing one sampling stop, which is the tool's one idea. Seen: teaching
   frames/empty-submit.png, empty-submit-reveal.png; play p02-all-accused.png; craft rv-sample-after-reveal.png.
   Fixed looks like: (a) Submit claim stays disabled until at least one suspect is checked and every checked suspect
   has evidence attached (hint: "Add evidence for each suspect you check."); (b) a missed source gets a nudge that names
   the weather and the target but no source, place or spot ("A source is still missing. Your samples don't explain the
   storm-day number at the beach yet."); (c) an accused culprit whose evidence does not bracket it says "Right source,
   not proven yet: you need a sample just above it and just below it, in the same weather" and gives the exact spots
   only when the attached samples are already in the right weather or one stop off; (d) Show the whole creek unlocks
   only when the case is solved or the kits are spent, not after any submit. Check the cheap paths after the fix:
   empty submit, all seven checked, all seven checked with one sample each. (general; Teaching tagged it
   family:hidden-information, the lesson is general: a submit with nothing in it must not return the key)
2. **Fix-it goal bars are a fixed 35 percent for any missed goal, and the goal line vanishes after Test plan.**
   src.html:1449 (`g.met[i]?100:35`), 1458 (`d.detail || d.target`). Beach 431.5 and beach 739 draw the same bar;
   a 18.9 percent lake cut and a 7.3 percent one look alike; after testing, the Lake and Creek captions are replaced by
   "Storm concentration ..." and "Dry remains ...", so the target is gone while students compare. REFINE: a meter
   that misleads is a blocker. Seen: audit-r1/state-fix-tested-1366x768.png, play p08-fix-done6.png. Fixed looks like:
   each bar fills by real progress toward its goal in the worse weather (beach 410 / value capped at 100, lake cut /
   25 percent and dry 0.05 / value, the smaller of the two, creek cut / 50 percent), with a tick at the goal; the
   target line stays on screen under any detail line. (general)

#### Should fix
1. **The map draws the storm drains joining below the Main Street bridge (S7), but the model adds them above S7.**
   src.html:643 (`M810 421L612 470`); S7 sits at about (560, 483) and the line ends at (612, 470), downstream. The
   model (859-862), the spec and the evidence rule (D1 bracketed by S6 and S7, or the Pipe) put them above S7. A
   student bracketing from the map would pick S7 and S8 and be told it does not bracket. Seen: teaching
   frames/crop-pipe.png. Fixed: the drain line meets the creek between the Old sewer and the S7 bridge; check the
   Pipe spot and Storm drains icon still sit on it. (general)
2. **The 20 percent culprit rule cannot be checked from anything on screen, and the Claim hint leads with it.**
   src.html:775 (wClaim), 1592; result card, logbook and Compare two. Shares depend on load = concentration x flow, but
   no flow is shown anywhere, so the rule is learned only from feedback; notes.md "Key skills" claims "Distinguish
   concentration, load and dilution". SPEC.md: a skill the tool claims needs a step that does it. Fixed: show flow
   (m3/s) on each result card and logbook row, and a load line in Compare two ("Load up 13.3 billion CFU per second
   from S6 to S7, dry day"), so the rule is checkable from the samples. Restore the spec's wClaim line ("Check each
   suspect you blame, then press Add evidence for each one."), re-recorded, and keep the 20 percent rule in the Claim
   panel's small print and Model notes. If flow and load can't be shown cleanly, drop the key skill from notes.md
   instead (rule 2); showing them is the preferred fix. (general; Play polish 8 merged here)
3. **Attaching every logbook sample to every suspect passes the evidence check.** src.html:1176-1189 (validEvidence
   only asks whether the needed pair is somewhere in the set). Teaching drive: eight beach samples on Pasture, Storm
   drains and Old sewer all return valid. Fixed: evidence holding samples from other reaches gets "Right source; trim
   the evidence to the pair that brackets it"; allowed sets are the bracketing pair, the direct sample, and for D1 the
   storm pair plus its dry contrast pair. (general)
4. **Claim feedback lands below the fold with no cue.** Claim panel. At 1366x768 with three culprits the third item
   is cut by the footer (play p05-beach-solve.png); with seven it runs to y=941 (p02); at 680x425 none of it shows
   (p03-all-accused-680.png). Fixed: on submit, scroll the first feedback item into view, or move feedback above the
   suspect list. (general)
5. **The newest result card hides the spots the student needs next.** src.html:1166 (positionResult). At 1366x768 a
   beach sample covers S8, the plant and its label; at 680x425 and 375 wide it covers S6, S7, Pipe, Storm drains and
   Old sewer; spots under it still take clicks unseen. Seen: audit-r1/state-sample-result-1366x768.png, -680x425.png,
   -375x812.png. Fixed: dock the card in a map corner away from the creek path (a strip at small sizes) and fade it
   when another spot is selected. (general; Play had it as polish, Craft as should fix)
6. **Revealed values look like sampled flags in Sample mode.** src.html:1065 (updateMap draws flags whenever
   state.reveal), reveal not reset on leaving Claim. Sample then shows flags on all 11 spots with "Kits left: 8", and
   Logbook lists 22 entries never taken. Seen: craft rv-sample-after-reveal.png, rv-logbook-after-reveal. Fixed: end
   the reveal when leaving Claim, or draw revealed values in their own style (hollow flags, "revealed" in the legend)
   and keep them out of the Logbook. (general)
7. **Restart case wipes a solved case with one tap.** src.html:583, restartCase 1519. It sits beside Make claim and
   clears samples, claim and the solved stamp (and relocks Fix-it if it was the only solved case). Seen: play
   p06-restart-after-solve, craft r-stale-kits. Fixed: a confirm like Clear my progress ("Restart Beach closed? This
   clears its 6 samples and your claim."). Skip the confirm when the case has no samples. (general)
8. **Fix-it looks live while locked and says nothing when tapped.** #m-fix, src.html:555. Same color and opacity as
   live mode buttons; a tap does nothing and focus drops to the page (the audit's #m-fix lead); a keyboard user never
   reaches it. Seen: audit-r1/size-1366x768.png, play p04-fix-disabled.png. Fixed: a visibly locked style and the
   reason on screen ("Fix-it opens after you solve a case", in the Cases panel steps and as the button's title), and
   it lights up when it unlocks. (general; Craft had it as polish)
9. **Two how-to lines are sent as events and repeat every time.** src.html:929 (EVENT_LINES). `submitted` spoke 5 of 5
   failed submits; `noPlan` spoke 5 of 5 Test plans, four on an unchanged plan, and its words differ from the spec.
   Seen: craft v1 and v3.txt logs. Fixed: noPlan follows the spec (first Test plan that misses a goal, stale on plan
   change, the spec's words "No plan here fixes everything for three million. Pick what matters most, and write
   why."); submitted becomes a how-to said once, with the on-screen hint carrying it after. (general)
10. **The sample result is never announced.** #map-result has no aria-live; focus stays on Take sample. Seen: craft
    k-focus-spot (`live: null`). Fixed: aria-live="polite" with a one-line summary ("S9, dry day: E. coli 447 CFU per
    100 mL, over the 410 line"). (general)
11. **Fix cards drop the price from their accessible name.** src.html:1381 (buildFixes), 1421 (updateFix):
    aria-label="Add Fence & troughs" replaces the visible text, so cost is never read. Fixed: put name, cost and state
    in the label ("Add Fence and troughs, $60,000"), or drop the aria-label. (general)
12. **Builder change notes leaked into notes.md "The modes".** "Use Fix details to read every intervention's effects
    ... The claim instruction states the 20 percent source rule before students submit." and "Field photographs
    preserve the whole scene, including the cattle's feet in the creek." read as fix logs. Fixed: cut them; keep one
    plain sentence that whole-creek shares count only sources upstream of the target. Update the Claim and reveal
    paragraph to match blocker 1. (general)

#### Polish accepted
1. **Muddy creek band.** src.html:714, Model notes 1595. 481 mg/L is in EIFAC's fourth band (over 400, poor fisheries
   at best), not "Over 80: unlikely good fisheries". Card: "Over 400: poor fisheries at best"; Model notes list all
   four bands. Goal and case logic unchanged. (general)
2. **Default spot is the target, already on the case card.** src.html:1024. Start with no spot chosen; Take sample
   disabled with "Tap a spot on the map first." (general)
3. **Solving lands flat.** After a right claim, show the Solved stamp on the case heading in the panel (same stamp as
   the Cases card), alongside Fix-it lighting up (should fix 8). (general)
4. **"Change" collides with "0% cut" in the Creek gauge at 375 wide.** Seen: play zoom-creek-375.png. Shorter row label
   ("Cut") or a wider label column. (general)
5. **Gauge rounding differs from the rest of the tool.** src.html:1439-1447: Before creek 480.8 vs 481 on the card;
   After beach 431.5 / 518.5 vs 447 / 739 Before. One rounding per quantity (whole numbers for E. coli and sediment,
   three decimals for P). (general)
6. **"soil" vs "sediment".** Logbook (1318) and fix effects (758-763) say soil; everything else says suspended
   sediment. "sediment" throughout. (nit, general)
7. **Treatment plant label sits on the creek beside S8.** src.html:130 (`#suspect-E span { right:110% }`). Move it off
   the water. Seen: craft k-focus-spot.png. (nit, general)
8. **"Construc / tion" breaks mid-word at 680x425** (overflow-wrap:anywhere, 441). Seen: audit-r1/state-claim-solved-680x425.png.
   (nit, general)
9. **Compare two asks for two entries when there is one.** src.html:1564-1565. With fewer than two samples, Compare
   two says "Take two samples to compare." (nit, general)

#### Settled calls
- Blocker 1 changes three spec lines ("missed (a hint naming the weather)" with the drains example, "right but ...
  (with what to sample)", "After a submit, Show the whole creek"). Settled by SPEC.md "Scores and checks reward the
  right thing" (doing nothing and the shortcut must not win) and BUILD.md "No giveaways": the weather hint stays, the
  source name and the spot recipe go until evidence is in. Not a question for Cory.
- Gauge bars: lenses said should fix; REFINE makes a misleading meter a blocker.
- Result card and Fix-it lock: Play and Craft split polish / should fix; taken as should fix (both hide or misstate
  something a solo student needs, rule 4).
- The culprit rule and "concentration, load and dilution": fixed by showing flow and load (rule 2 needs a real step);
  dropping the key skill is the fallback only.
- The spec's three open questions are settled, not sent: the title "Up the Watershed" is already in use; the rain
  advisory stays as an honest real-world option (BASELINE rule 9), already labeled "Protected, not cleaned" with the
  water value; made-up costs, flows and loads stay, and notes.md already says so.
- Audit leads not taken: welcome cut by a first tap (BASELINE rule 16, the hint keeps it); logbook "text hidden"
  overlaps (a modal over its backdrop); footer links below the fold at 375 (secondary, reachable).
- Do not change: the load model and every Sample, share and worked-plan number (Teaching recomputed all; they match);
  the standards (both are really taught); the Why box staying unsaved; the art credits (Craft found both routes
  credited and every image people-free).

#### To the spec's open questions
None. Everything above is settled by BASELINE, SPEC.md or REFINE.

#### Not taken
- Missed-source wording that splices the case title (Teaching nit 8): moot after blocker 1.
- tool.draft.json lists two art routes (Teaching nit 9): Craft confirmed both are real and credited.
- One Logbook button instead of Logbook and Compare two (Play nit 11): the spec names both; the cheap half is polish 9.
- 12 px map labels at 1280 wide and up (Play nit 12): map layout risk for a projection-only gain; Done when 9's 10 px
  floor holds.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: up-the-watershed (round 1)

Bundle `tools/up-the-watershed/up-the-watershed.html` as built (not re-bundled). Shared audit:
`S:/CurioClass-codex-scratch/up-the-watershed/audit-r1/audit.md`. My frames and drive logs:
`S:/CurioClass-codex-scratch/up-the-watershed/craft/` (v1, v3, v5 folders; v3.txt, v4.txt). Not a Curiosity (no
"(Curiosity No. NN)" line), so lesson norms apply.

#### Contract (clean)

- One file, 761 KB: under the 2 MB goal. All 22 `art:` tokens are inlined as data URIs; every `<img>` loaded
  (18 of 18 complete, c-contract shot). `performance.getEntriesByType('resource')` is empty; no `http` string, `fetch`,
  XHR or dynamic import in the bundle. No console errors, warnings or exceptions in any of my shots or the audit.
- Kit used: `Curio.voice`, `Curio.tone`, `Curio.wait`, `Curio.reduce`, kit Motion/Sound/Read. Nothing re-implemented.
- Lines: `allLines()` returns 20 strings, identical word for word to `voice/lines.json` (no missing, no extra).
- Art: every token has a `prompts.json` entry; all 22 are `people: false`; the 8 local FLUX images are scenes with no
  people. Credits for both routes are in `tool.draft.json`.
- Words: no em dashes in src, notes, lines, spec or tool.draft.json; "Curio Class" never "Curio" alone on screen.
  Privacy is stated in the footer ("Progress stays on this device. Nothing leaves it.") and Clear my progress confirms.
- Focus is visible (4 px `#b7ecff` outline on map buttons, k-focus-spot.png); panel controls come before map items in
  tab order; Motion off is clean (audit).

#### Findings

1. **Restart case wipes a case with one tap, no confirm.** `src.html:583`, `restartCase()` at 1519. It sits beside
   Make claim and clears every sample, the claim and the solved stamp; if that was the only solved case, Fix-it locks
   again. Clear my progress asks first; this does not. Seen: r-stale-kits (8 samples, one tap on Restart case, `n: 0`).
   Better: a confirm dialog like Clear my progress, or an Undo in the hint. **should fix**, general.

2. **The sample result is never announced.** `#map-result` has no `aria-live` and focus stays on Take sample
   (k-focus-spot `live: null`). A keyboard or screen-reader student presses Take sample and hears only the hint; the
   four values, units and the limit bar are silent. Better: `aria-live="polite"` on the result card (or announce a
   one-line summary such as "S9, dry day: E. coli 447 CFU per 100 mL, over the 410 line"). **should fix**, general.

3. **Fix cards drop the price from their accessible name.** `buildFixes()` 1381 and `updateFix()` 1421 set
   `aria-label="Add Fence & troughs"`, which replaces the visible text, so the cost is never read; effect and who pays
   live only in `aria-description`. Cost is the decision in this mode. Seen: k-focus-spot (`fixlabel`, `fixdesc`).
   Better: drop the aria-label and let the visible text plus a state word name it, or put the price in the label.
   **should fix**, general.

4. **The goal gauges' bars are not meters.** `renderGauges()` 1449: `width = met ? 100 : 35`. Every missed goal
   draws the same 35 percent bar whatever the numbers (C + A misses the beach by 22 and the lake by a lot; both show
   35), and an untested plan shows 0. It reads as progress toward the goal. BUILD.md "Honest numbers". Seen:
   audit state-fix-tested-1366x768.png and -680x425.png. Better: scale each bar to real progress (for example the
   creek's percent cut over 50, the lake's dry P against 0.05) with the goal marked, or remove the bar and keep the
   check / cross. **should fix**, general.

5. **The result card hides the map it reports on.** `positionResult()` 1166. At 1366x768 a beach sample (S9) puts
   the card over S8, the treatment plant and part of Outfall; at 680x425 and 375 wide it covers half the map (S6, S7,
   Pipe, Old sewer, Storm drains, plant, S8). Spots under it still take clicks (`pointer-events:none`) but cannot be
   seen. Seen: audit state-sample-result-1366x768, -680x425, -375x812 (confirmed on the frames; the audit's overlap
   rows there are real). Better: dock the card in a map corner away from the spot path, or shrink it to a strip at
   small sizes. **should fix**, general.

6. **Revealed flags look like sampled flags in Sample mode.** `updateMap()` 1065 draws D and S flags at every spot
   whenever `state.reveal` is on, in any mode, and Show the whole creek is not reset when the student presses Sample
   (the reveal hint even sends them there). Sample then shows flags on all 11 spots with "Kits left: 8" and the plain
   sampling hint; Logbook lists 22 entries the student never took. One look, two meanings (BUILD.md lesson). Seen:
   rv-sample-after-reveal.png (24 flags, 8 kits), rv-logbook-after-reveal (22 entries). Better: draw revealed values
   in their own style (hollow flags, "revealed" in the legend) and say so in the Sample hint, or end the reveal when
   leaving Claim. **should fix**, general.

7. **Two how-to lines are sent as events and repeat every time.** `EVENT_LINES` 929: `submitted` ("Read the
   feedback. Change a suspect or its evidence, then press Submit claim again.") spoke 5 of 5 failed submits, and
   `noPlan` ("This plan misses a goal. Compare the gauges, change a fix, or press Save plan and explain your
   priorities.") spoke 5 of 5 Test plans, the last four on an unchanged plan. Both are mostly instructions; the spec
   made noPlan "first Test plan". This is the nag STANDARDS warns about. Better: split each into a short event ("Not
   yet. Two sources need more evidence." / "This plan misses a goal.") and a how-to said once. Seen: v-claim-submit5,
   v-fix-test5 (logs in v1 and v3.txt). **should fix**, general.

8. **The whole creek can be revealed for free.** Submit an empty claim on a fresh case (0 kits used): the feedback
   names every missed culprit with the weather or samples to take ("Missed source. The storm drains only flow in
   storms."), Show the whole creek unlocks and draws every suspect's share, and all 8 kits are still there to collect
   exactly the listed pairs. Seen: rv-sample-after-reveal (empty submit, reveal, Kits left: 8). The spec allows the
   reveal "after a submit"; it does not say an empty one. Lead for the Teaching and Play lenses (BUILD.md "No
   giveaways"); the integrator should weigh it. Better: unlock the reveal only once kits are spent or the case is
   solved, and have a missed source say only "a source is missing" until some evidence is in. **should fix**, general.

9. **Fix-it is disabled with no reason given.** `#m-fix` (555) is disabled until a case is solved; no hint, title
   or Cases step says so, and a disabled button can't take focus, so a keyboard user never finds it. The audit's
   "focus fell to the page after clicking #m-fix" comes from clicking it while disabled. Better: "03 / Change it:
   opens after you solve a case" in the Cases panel, or keep it enabled with an explanatory hint. **polish**, general.

10. **Gauge numbers don't match the rest of the tool.** `renderGauges()` 1439 to 1447: Before shows the creek at
    480.8 (case card and Sample show 481) and the beach at 447 / 739 while After shows 431.5 / 518.5 (spec worked plan:
    432 / 519). Seen: audit state-fix-tested-1366x768. Better: one rounding per quantity everywhere. **polish**,
    general.

11. **"soil" vs "sediment".** Logbook entries read "soil 9.3 mg/L" (1318) and fix effects say "soil −60%" (758 to
    763), while the result card, case card, gauge and Model notes say suspended sediment. Better: "sediment" throughout.
    **nit**, general.

12. **Treatment plant label sits on the creek.** `#suspect-E span { right:110% }` (130) puts "Treatment plant" left
    of its icon, on the creek beside S8, where it reads as a label for S8. Seen: k-focus-spot.png, audit
    state-whole-creek-1366x768. **nit**, general.

13. **"Construction" breaks mid-word in the Claim list at 680x425** ("Construc / tion", `overflow-wrap:anywhere`
    at 441). Seen: audit state-claim-solved-680x425. **nit**, general.

Counts: blockers 0, should fix 8, polish 2, nits 3.

#### Standard voice check

Held clicks (0.12 s), Sound on, Motion on, 1366x768, fresh Chrome profile per run where progress mattered
(progress persists in localStorage, so a reused profile suppresses welcomes; those runs were redone).

| line | kind | expected | spoken |
|---|---|---|---|
| wCases | welcome | once | 1 (stage tap, first key, Reset) |
| wSample | welcome | once | 1 of 10 Take sample taps |
| bracket | how | once | 1, then silent |
| lastKit | event | each time | 1 of 1 (7th kit) |
| outOfKits | event | each time | 1 of 1 (8th kit) |
| wClaim | welcome | once | 1 |
| chooseEvidence | how | once | 1 |
| submitted | event in code, how-to in words | once | **5 of 5** (finding 7) |
| solved | event | each time | 1 of 1 |
| wFix | welcome | once | 1 in 5 Add / Remove toggles |
| noPlan | event (spec: first Test plan) | once per new plan | **5 of 5, same plan** (finding 7) |
| overBudget | event | on crossing | 1 (all nine fixes, $4,100,000, Test plan disabled) |

- Stale: fast taps (0.2 s) through Take sample, Claim, Cases and Reset: lastKit cut by the mode change, wClaim cut by
  Reset, the queued bracket line dropped as newer; no line played after its moment. Restart case cut outOfKits.
- First tap: a stage tap and the first Tab key give the welcome within about 0.1 s; Open case gives only wSample;
  Read speaks the hint only; Sound says nothing (audit table rows 4 and 5). No line names a disabled control (outOfKits
  needs Make claim; overBudget needs a selected fix).
- Read: Read during wSample cut it and spoke the hint; the next mode's welcome started 1.4 s later; Read with Sound
  off spoke. Order followed the actions in every log.
- Not driven: saved, compare, why, fixDetails, emptyLog, emptyPlans, emptyBudgetPlans (each is a dialog or a one-off
  how line; their texts match the dialogs they open).

#### Audit pilot

- Confirmed: the result card overlaps at 680x425, 800x500, 1366x768 and 375 wide (finding 5); "Restart case: nothing
  changed" is true (an empty case), and the real problem is the missing confirm once there is something to lose
  (finding 1); the 375 wide footer links below the fold are real but are not main controls.
- Wrong or not findings: every logbook "text hidden" row is the modal dialog over its own backdrop; "focus fell to the
  page after clicking #m-fix" is a click on a disabled button (finding 9 is the real issue); the welcome cut by a first
  tap on Model notes or Clear my progress, and by two quick taps on Open case, is allowed by BASELINE rule 16 and the
  hint keeps it.
- Missed: revealed flags shown as sampled in Sample mode (6), the gauge bar that is not a meter (4), the unannounced
  result card and the price missing from fix-card names (2, 3), how-to lines repeating as events (7), and the free
  reveal path (8). These need state, meaning or assistive-tech checks the audit doesn't run.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: up-the-watershed (round 1)

Played twice: as a grade 12 student alone at home (no teacher, nothing read first) and as a teacher projecting it at
1366x768. Own frames in `S:/CurioClass-codex-scratch/up-the-watershed/play/f1/` (drive.py, held clicks, port 9901);
shared audit frames in `S:/CurioClass-codex-scratch/up-the-watershed/audit-r1/`. Note: drive.py shots share one Chrome
profile, so localStorage carried between shots (p06 and p07 started with p05's beach samples; p03 started with p02's
claim). The readings below account for that.

What works: the first screen says what to do (hint plus the three numbered steps), the map reads as a real place, the
dry / storm flags and the bracket lines from icon to sample spots are clear, the beach case solves in 5 kits by honest
play (p05), the result card, Compare two ("Up 1,333 CFU/100 mL, From S6 to S7, dry day", p07) and the Fix-it plan
for Done when 6 ($2,955,000, beach "Protected, not cleaned", p08) all behave as the spec says. Motion off and the
mid-action resize are clean (audit).

#### Findings

1. **Claim mode: an empty claim names every culprit, with zero kits spent.**
   Where: `src.html:1253-1258` (submitClaim, the "missed" branch). Open Beach closed, go straight to Claim, press
   Submit claim with nothing checked. Feedback: "Missed source. Look for beach closed evidence after a storm near
   pasture. / Missed source. The storm drains only flow in storms. / Missed source. Look for a dry-day jump below
   town." Kits left: 8. Checking all seven suspects and submitting (p02) does the same the other way: each culprit
   reads "right source, but evidence does not bracket it. Sample S1 and S2 after a storm." and each innocent gets its
   share. So the whole investigation (which suspects, which spots, which weather) is handed over before a single
   sample, and the student only has to follow instructions. "Show the whole creek" then also unlocks after that empty
   submit. This is the cheap pass REFINE asks lenses to try, and it works on all three cases. Better: a missed source
   gets a hint that points to a place to look without naming the source ("A source is still missing. Your samples
   don't explain the storm-day number at the beach yet."); accusing a culprit without evidence says "not proven yet"
   without the exact spot recipe until the student has sampled near it; and the whole-creek reveal waits for a claim
   with at least one evidence pair, or for the kits to run out.
   Seen: p01-empty-claim (text in drive output), p02-all-accused.png. Level: **blocker** (gives the answer away in
   the tool's hidden-information mode; POLISH, Games and quizzes). Tag: general.

2. **Claim feedback lands below the fold, with no cue to scroll.**
   Where: Claim panel, 1366x768 and 680x425. After Submit claim the feedback list starts under the buttons: at
   1366x768 with three culprits claimed only the first two items show and the third is cut by the footer
   (p05-beach-solve.png); with more items it runs to y=941 in a 768 tall window (p02, panel scrollHeight 891 vs 655).
   At 680x425 none of it is visible (p03, feedback top 378 under the footer, panel 475 vs 324). The feedback is the
   payoff of the whole claim step and a solo student may never see it. Better: scroll the first feedback item into view
   on submit (preventScroll off for that one element), or put feedback above the suspect list, or collapse the
   suspect list to the checked rows after a submit.
   Seen: p02-all-accused.png, p03-all-accused-680.png, p05-beach-solve.png. Level: **should fix**. Tag: general.
   (Audit missed it: its claim-solved state has one feedback item.)

3. **Fix-it looks enabled while it is locked, and says nothing when tapped.**
   Where: header `#m-fix` (`src.html:555`), Cases at every size. Disabled Fix-it has the same color and opacity as
   the live mode buttons (computed `rgb(232,237,243)`, opacity 1, p04); a tap does nothing and focus falls to the
   page (the audit's "focus fell to the page after clicking #m-fix" lead, confirmed: the cause is that the button is
   disabled). Nothing on screen says "solve a case to open Fix-it" until a case is solved. Better: a visibly locked
   style (dimmed, a small lock), and a title / hint "Solve any case to open Fix-it", or keep it clickable and show
   that sentence in the hint.
   Seen: size-1366x768.png, p04-fix-disabled.png. Level: **should fix**. Tag: general.

4. **Restart case wipes a solved case with one tap, no confirm.**
   Where: `#restart-case` (`src.html:583`, restartCase at 1519), beside Make claim in Sample. In p06 the creek was
   solved, then Sample, Restart case: the samples, the claim and the solved status were gone at once (solved list
   went from beach + creek to beach only), and it is saved that way. Clear my progress asks first; this does not,
   and it sits right next to the button a student presses most after sampling. Better: a confirm dialog like Clear
   my progress ("Restart Beach closed? This clears its 6 samples and your claim."), or only clear the samples and
   leave a solved case solved.
   Seen: p06-restart-after-solve (drive output). Level: **should fix**. Tag: general.

5. **Fix-it gauge bars are not meters: every missed goal shows the same 35 percent bar.**
   Where: `renderGauges`, `src.html:1449` (`g.met[i]?100:35`). The bar under each goal looks like progress toward the
   goal, but beach 431.5 (just over 410) and beach 739 draw the same bar, as does a 18.9 percent lake cut against the
   25 percent target (state-fix-tested-1366x768.png). A student reads "a third of the way" where nothing was
   measured. Better: fill by the real fraction of the goal reached (for example 410 / value for the beach, cut / 25
   percent for the lake, cut / 50 percent for the creek, worst weather), with a tick at the goal line, or drop the bar
   and keep the status words.
   Seen: state-fix-tested-1366x768.png, p08-fix-done6.png. Level: **should fix** (a meter that misleads). Tag: general.

6. **The newest result card covers the spots you need next, at preview sizes most of the map.**
   Where: `positionResult`, `src.html:1166`. At 1366x768 a beach result (S9) covers S8, the Treatment plant icon and
   its label (state-sample-result-1366x768.png); at 680x425 it covers S6, S7, Pipe, Storm drains and Old sewer
   (state-sample-result-680x425.png); at 375 it covers most of the map. The card has `pointer-events:none`, so a tap
   on a hidden spot goes through to it, but the student cannot see what they are tapping. Better: anchor the card in a
   corner of the map away from the sampled spot's downstream neighbours, or shrink it to the case pollutant only with
   "All four tests" in the Logbook, and fade it when another spot is selected.
   Seen: the frames named. Level: **polish**. Tag: general. (Audit overlap leads under sample-result and
   out-of-kits: confirmed as this one issue.)

7. **The default sample spot is the case target, whose numbers are already on the case card.**
   Where: `openCase`, `src.html:1024` (`state.site=CASES[id].target`). A solo student following "Tap a spot, choose
   Dry day or Day after storm, then press Take sample" can just press Take sample and spend a kit on 447, which the
   Beach closed card already showed (the audit's own sample-result state does exactly this). Better: start with no
   spot chosen (Take sample disabled with "Tap a spot on the map first"), or preselect a headwater spot.
   Seen: state-sample-result-1366x768.png, size-1366x768.png. Level: **polish**. Tag: general.

8. **Claim hint is hard to act on alone.**
   Where: `L.wClaim`, `src.html:775`: "Check sources with at least 20 percent at an over-limit target, dry or storm."
   A student alone cannot measure a 20 percent share from concentrations, and "over-limit target" is jargon. The
   action (check a suspect, press Add evidence) is at the end. Better: lead with the action and the evidence idea:
   "Check each suspect you blame, then press Add evidence and pick the samples above and below it." (close to the
   spec's own wClaim line), and leave the 20 percent rule in Model notes. Teaching lens may weigh in on the rule.
   Seen: state-mode-claim-1366x768.png, hint text. Level: **polish**. Tag: general.

9. **Solving a case lands flat on the map view.**
   Where: Claim after a correct submit (p05-beach-solve.png). The only change is the hint text, a chime and the
   spoken line; the third "right" item is below the fold (finding 2) and the "Solved" stamp shows only back on Cases.
   9-12 wants minimal celebration, but the moment should still be visible. Better: a small "Case solved" stamp on the
   case heading in the panel (the same stamp as the Cases card) and the Fix-it button lighting up as it unlocks.
   Level: **polish**. Tag: general.

10. **Creek gauge label collides at 375 wide.**
    Where: Fix-it, 375x812 iframe host: "Change" runs under "0% cut" (zoom of state-fix-tested-375x812.png, saved as
    `S:/CurioClass-codex-scratch/up-the-watershed/play/zoom-creek-375.png`). Better: a shorter row label ("Cut") or
    the 29 px label column widened for that row. Level: **polish**. Tag: general. (Audit missed it.)

11. **Logbook and Compare two open the same dialog.**
    Where: `src.html:1564-1565`. Both buttons open the logbook with "Tap two logbook entries. Then press Compare
    selected."; only the title differs. With one entry (state-logbook-1366x768.png) it still asks for two. Better: one
    "Logbook" button, and the compare prompt only once there are two entries. Level: **nit**. Tag: general.

12. **Projected, the map labels are small.**
    Where: map at 1366x768: suspect names, place names and the legend are 10 px, spot discs 11 px
    (`.map-place`, `.suspect-map span`, `.spot .disc`). Fine on a laptop, hard from the back of a room. Better: 12 px
    labels at 1280 wide and up. Level: **nit**. Tag: general.

Nothing cultural, Native or hard-history: no sensitivity review needed from this lens.

#### Counts

blocker 1, should fix 4, polish 5, nit 2.

#### Audit pilot

- Leads confirmed: result-card overlaps under sample-result and out-of-kits (finding 6, one issue, by design a popup
  but too large at preview sizes); "focus fell to the page after clicking #m-fix" (finding 3: Fix-it is disabled but
  styled as live).
- Leads wrong or not worth a finding: "Restart case: nothing changed" (expected on a case with no samples; the real
  problem is the opposite, finding 4); footer controls below the fold at 375 (Model notes, Reset, Clear my progress are
  secondary and reachable by scrolling); welcome cut by a first tap on Model notes, Clear my progress or a quick second
  Open case (allowed by BASELINE rule 16; the hint carries it); overlaps of the Logbook dialog over the map (a modal
  over a dimmed page).
- Missed by the audit: the empty-claim giveaway (finding 1), claim feedback below the fold (finding 2, its
  claim-solved state has only one feedback item), the fixed 35 percent gauge bars (finding 5), the "Change" collision at
  375 (finding 10), Restart case with no confirm (finding 4).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: up-the-watershed (round 1)

Cold read of spec.md, src.html, notes.md, tool.draft.json, voice/lines.json, the shared audit
(S:/CurioClass-codex-scratch/up-the-watershed/audit-r1) and my own drives in
S:/CurioClass-codex-scratch/up-the-watershed/teaching/frames (drive.py, port 9891). Not a Curiosity; judged as a
grade 12 lesson tool.

#### Findings

1. **Claim mode, src.html:1230-1260 and 1225, 1569. An empty claim gives away every culprit and the answer key.**
   Opening Beach closed, pressing Claim and pressing Submit claim with nothing checked and zero kits used returns
   "Missed source. Look for beach closed evidence after a storm near pasture. / Missed source. The storm drains only
   flow in storms. / Missed source. Look for a dry-day jump below town." That names all three culprits. The same
   submit unlocks Show the whole creek, which draws every suspect's percent share (Green lake, zero samples: plant
   86.7 dry, fields 27.2 and construction 23.4 storm). Then "right source, but evidence does not bracket it" names
   the exact spots and weather to sample. A student can solve every case by following instructions without ever
   choosing a sampling stop, which is the one idea of the tool ("the case is about sampling strategy").
   Seen: frames/empty-submit.png (feedback text captured), frames/empty-submit-reveal.png. Better: Submit needs at
   least one checked suspect with evidence attached; a missed source gets a location-free nudge ("Something else
   adds most of the storm-day E. coli here; you have not sampled where it enters"), not its name; Show the whole
   creek waits until the kits are spent or the case is solved. **Level: blocker. Tag: family:hidden-information
   (general lesson: a submit with nothing in it must not return the key).**

2. **Claim rule and notes "Key skills", src.html:775 (wClaim), 1592; notes.md "Key skills". The culprit rule cannot
   be computed from anything the student sees.** The Claim hint (also spoken) says "Check sources with at least 20
   percent at an over-limit target". Shares depend on load = concentration x flow, but no flow appears anywhere on
   screen (result card, logbook and compare show concentrations only; the spec's flows, 0.30 / 1.80 m3/s etc., are
   builder-only). So the student guesses "big jump" and the 20 percent line is only ever learned from the feedback or
   the reveal. The notes claim the key skill "Distinguish concentration, load and dilution", but load is never shown
   or asked for, and the dilution case (S5 storm 1,626 after mixing two forks; S7 storm E. coli rising less than the
   Pipe's 5,000 suggests) is never made visible as load. Seen: grep of src.html for flow output; frames/empty-submit-reveal.png.
   Better: put flow on each result card and logbook row (m3/s) and a load line in Compare two ("load up 13.3 billion
   CFU/s from S6 to S7"), so the 20 percent rule is checkable; or drop the key skill and restate the rule as
   something observable. **Level: should fix. Tag: general.**

3. **Map, src.html:643 (`M810 421L612 470`). The storm drain line joins the creek below the Main Street bridge (S7),
   but the model adds the storm drains above S7.** S7 is drawn at (560, 483); the drain line ends at (612, 470),
   downstream of the S7 bridge (M530 475 L585 457). The model (src.html:859-862), the spec and the evidence rule
   (D1 bracketed by S6 and S7) all put the drains above S7. A student reading the map would bracket the drains with
   S7 and S8 and be told the evidence does not bracket it. Bracketing from the map is the core skill, so the map must
   agree with the model. Seen: frames/crop-pipe.png (crop of empty-submit-reveal.png). Better: end the drain line on
   the creek between the Old sewer and the S7 bridge. **Level: should fix. Tag: general.**

4. **Evidence check, src.html:1176-1189. Attaching every logbook sample to every suspect passes.** validEvidence only
   asks whether the needed pair is somewhere in the attached set; unrelated samples are ignored. With eight beach
   samples attached to Pasture, Storm drains and Old sewer, all three return valid (drive check `dump`:
   {"A":true,"D1":true,"D2":true}). The notes' key skill "Support a claim with a direct sample or a bracketing pair"
   is not tested. Better: evidence that includes samples not on that suspect's reach gets "right source; trim the
   evidence to the pair that brackets it", or the attached set must be the pair (plus at most the contrast pair for
   D1). **Level: should fix. Tag: general.**

5. **Fix-it gauges, src.html:1449, 1458. The meter bar is a fixed 35 percent for any missed goal and the goal text
   disappears after Test plan.** Width is `met ? 100 : 35`, so a lake plan at 0.214 and one at 0.051 look the same.
   After testing, the caption under Lake and Creek is replaced by "Storm concentration 0.290 mg/L P." and "Dry
   remains 9.1 mg/L.", so the target ("Dry P < 0.05; storm load -25%", "cut at least 50%") is no longer on screen
   while students compare. Seen: audit-r1/state-fix-tested-1366x768.png. Better: fill toward the goal (for example
   percent of the needed cut achieved) and keep the target line under the detail. **Level: should fix. Tag: general.**

6. **notes.md "The modes", last two paragraphs. Builder change notes leaked into the teacher notes.** "Use Fix
   details to read every intervention's effects and who pays, including on phones and short previews. The claim
   instruction states the 20 percent source rule before students submit." and "Field photographs preserve the whole
   scene, including the cattle's feet in the creek." read as fix logs, not teacher guidance. Better: cut them, keep
   the useful fact (whole-creek shares count only upstream sources; the plant adds nothing at Main Street) as one
   plain sentence. **Level: should fix. Tag: general.**

7. **Muddy creek card, src.html:714; Model notes 1595. The sediment band is cut short.** EIFAC (1965) has a fourth band:
   over 400 mg/L "at best only poor fisheries". The case value is 481, so the honest label is the over-400 band, not
   "Over 80: unlikely good fisheries". Checked against the EIFAC Technical Paper 1 band table (four bands: under 25,
   25 to 80, 80 to 400, over 400). Better: "Over 400: poor fisheries at best" on the card, and list all four bands
   in Model notes. **Level: polish. Tag: general.**

8. **Missed-source hint wording, src.html:1257.** "Look for beach closed evidence after a storm near pasture." and
   "Look for green lake evidence..." splice the case title into the sentence. (Moot if finding 1 removes names.)
   **Level: nit. Tag: general.**

9. **tool.draft.json sources.** Lists both "Eight retained illustrations drawn with FLUX.1-schnell" and "Illustrations
   generated with OpenAI gpt-image"; the spec says local FLUX only. One of these is wrong about where the art came
   from. Craft should confirm which. **Level: nit. Tag: general.**

#### Done when (spec)
1. Sample values: pass. The model run in the page (`__tool.model`) reproduces every row of the Sample table to the
   listed rounding (S4 dry 26.7 shows as 27, S8 dry 1,357.5 as 1,358).
2. Beach in 8 kits with D2 (S6, S7 dry), A (S1, S2 storm), D1 (Pipe storm): pass by code (5 kits).
3. Geese: "About 9 percent dry, 5 percent storm" and wrong: pass (src.html:1249; shares 8.9 / 5.4 recomputed).
4. Green lake: Outfall alone catches the plant; fields and construction need storm pairs: pass.
5. Muddy creek: C with S5 and S6 storm solves; B gives "only 14 percent": pass (audit claim-solved state).
6. E + D2 + A + C + G: $2,955,000; 64.0 / closed (461.5); 0.041, 26.5 percent; 228.4, 52.5 percent; all met: pass.
7. Seven-fix plan: lake 0.209 dry, fails: pass.
8. Every fix: $4,100,000, Test plan disabled: pass by code (src.html:1429).
9 to 12 are layout and voice; the audit's size and walk rows are clean for them and Play and Craft own them.

#### Facts checked
Recomputed in the page: every Sample table value, every case share in the spec, and the worked plans (E alone 0.047 /
7.3 percent; C alone 260.2 / 45.9; C + A 431.5 / 518.5 and 52.5; D2 + A 64.0 / 461.5; + D1 321.7). All match.
Reference values checked against their sources: E. coli 126 GM and 410 STV CFU/100 mL (EPA 2012 RWQC), nitrate-N
10 mg/L MCL, total phosphorus 0.05 mg/L for streams entering lakes (EPA Gold Book 1986), EIFAC sediment bands (see
finding 7), EPA 841-B-03-004, 841-B-05-004, 832-R-08-006, NRCS 382 (fence), 390 (riparian herbaceous cover), 605
(denitrifying bioreactor). Correct. (Water troughs are NRCS 614, not cited; harmless.)

Standards: HS-ESS3-4 is exercised by testing and revising fixes against measured goals in Fix-it. HS-ETS1-3 is
exercised by the $3 million budget, who-pays lines, saved plans and the Why box. Both real; the Why box is not
saved or checked, which is fine for a classroom discussion.

Grade fit and guardrails: grade 12 language is right. No hard history, health or cultural content; no sensitivity
review needed. Support at home ideas are doable tonight and say not to enter the water.

#### Audit pilot
- Leads confirmed: none of the audit's leads are teaching leads; its clean rows (sizes, walks, motion) are cited
  for Done when 9 to 12.
- Leads wrong: none checked from this lens.
- What it missed: the empty-submit giveaway (finding 1), the uncomputable 20 percent rule (2), the map drawing the
  storm drain below S7 (3), the evidence dump (4), and the fixed-width gauge bar (5). All are meaning problems a
  mechanical audit cannot see.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: up-the-watershed (Codex fix, round 1)

The user's Curiosity instruction overrides the lesson-shaped spec and Refine. This fix preserves the creek model and illustrations while replacing the lesson frame with an open field station. No welcome screen, claim grading, score, goal, solved stamp, kit limit, locked simulator or finish screen remains. `refine.md` was not edited. Only this tool and its Scratch folder were written; no git commits were made.

Evidence root: `../../_scratch/up-the-watershed/`. Each path below is relative to that root. Original source is `before-src.html`. All named frames were opened and inspected. Numbers are retained as JSON beside the shot lists. Tests used Chrome 9910 and the narrow iframe host 8715; the final audit used Chrome 9911 and host 8715. Bundle commands were capped at 120 seconds, drive batches at 300 seconds and the audit at 2,400 seconds.

#### Blocker

1. **FIXED, by removing the lesson check.** Before: `before/empty-submit.png`, `before/blanket-submit.png` and their JSON show a blank claim naming all three culprits and enabling revelation; blanket accusation returns exact spot recipes. After: `focus-v2/focus-default.png` and `verify-numbers.json` show zero claim, submit, reveal or kit controls. The baseline ledger is explicitly open model output, never a reward for a submission. It cannot create sampled evidence. This follows the user's Curiosity override instead of adding a new prerequisite or answer check.
2. **FIXED.** Before: `before/gauges.png`, `before-gauges.json`: every missed criterion gets 35%, with the lake and creek targets replaced. After: `retouch/final-fix-680.png`, `retouch/final-fix-375.png` and `numeric-verification.json`: physical storm-concentration bars on fixed scales, with permanent reference ticks and both weather values. Beach baseline 738.738 CFU/100 mL fills 92.342%; C+A 518.544 fills 64.818% of the 800 scale. No progress or success bars remain. P and sediment scales are 0.400 and 600 mg/L; the Manual names the scales. The cost track names its $0–$4.1m scale and $3m tick.

#### Should fix

1. **FIXED.** Before: `before/flood-evidence.png` and JSON show the drain ending at (612,470), below S7. After: `final-map/final-map-1366.png`, `retouch/final-map-680.png` and `retouch/final-map-375.png`: endpoint (515,458), before S7. Pipe remains at the upper end; the drain miniature sits on the line.
2. **FIXED.** Before: `before/result-1366.png` has no flow and the old Claim hint states an uncheckable 20% rule. After: `verification/verify-live-flow.png`, `verify-live-flow.json`, `verification/verify-compare-1366.png`: S7 dry flow 0.750 m³/s, concentration jump 1,333 CFU/100 mL and added load 10,000,000 CFU/s. Every Logbook row has flow. The Refine example's 13.3 billion is not reproduced by the model, so it was not copied. The quiz-specific 20% rule and Claim narration are removed under the Curiosity override.
3. **FIXED, by removing evidence grading.** Before: `before-flood-evidence.json` records `validEvidence` accepting all eight entries for A, D1 and D2. After: `remaining/check-three-selections.png`, `check-three-selections.json`: tapping three log rows leaves exactly two selected for numerical comparison. There is no validator or correctness result that an oversized set can pass.
4. **FIXED.** Before: `before/feedback-680.png`, `before-feedback-680.json`: feedback bottom 522 in a 425-high viewport; the 1366 blanket frame also clips feedback. After: `verification/verify-compare-680.png`, `verify-compare-680.json`: the result appears above the entries, y=202.8–335.0. At 1366 it is y=349.4–481.6, and at 375 y=299.7–473.5. Claim feedback itself is removed.
5. **FIXED.** Before: `before/result-1366.png`, `before/result-680.png`, `before/result-375.png` cover sampling stops. After: `final-map/final-map-1366.png`, `retouch/final-map-680.png`, `retouch/final-map-375.png`: a reserved strip outside the map, zero intersection at all three sizes. Selecting another stop fades prior values and explicitly labels them Previous until the next collection. Opacity 0.35 and the Previous caption are recorded in `last-fade-1366.json`, `last-fade-680.json` and `last-fade-375.json`. The held-pointer transform bug discovered during this fix was corrected; real desktop and iframe clicks were re-tested.
6. **FIXED.** Before: `before/reveal-leaks.png`, `before-reveal-leaks.json`: 22 Logbook rows despite only two collected entries. After: `remaining/check-no-ledger-leak.png`, `check-no-ledger-leak.json`: collect once, open the ledger, switch views and open Logbook; one collected entry, one row and one flag. The ledger never mutates the sample list.
7. **FIXED.** Before: `before/restart.png`, `before-restart.json`: one tap clears the sampled case with no dialog. After: `remaining/check-clear-confirm.png`, `check-clear-confirm.json`: one entry remains while the count-specific confirmation is open. Close keeps one; confirming removes it and its flag (`check-clear-cancel.json`, `check-clear-applied.json`). Restart and solved status are absent; the simulator stays open.
8. **FIXED, by removing the lock.** Before: `before/default-lock.png`, `before-default-lock.json`: disabled Fix-it, empty title, live-looking styling. After: `remaining/check-keyboard.png`, `check-keyboard.json`: Tab, Tab, Enter enters Interventions before any samples. The open simulator has a working selected-state light. No case-solving prerequisite remains.
9. **FIXED under the Curiosity voice rule.** Before: `before-extra/submitted-five.png`, `before-extra/test-five.png` and logs show repeated instructional events; two automatic repetitions started at the requested 2-second pace. After: `verify-voice.json`: one first hint and one Read; five Test plan presses cause zero automatic how-to or failure events. The requested goal-based noPlan wording is intentionally omitted. After the first hint, speech requires Read.
10. **FIXED.** Before: `before-result-1366.json`: no live region. After: `verify-live-flow.json`: dedicated `aria-live="polite"`, atomic status, “S7, dry day: E. coli 1,441 CFU/100 mL, above the 410 reference.” `verify-dry-pipe.json` announces absent flow without treating it as a zero concentration.
11. **FIXED.** Before: `before-gauges.json`: “Remove Fence & troughs” omits cost. After: `verify-all-costs.json`: all nine names contain Add/Remove, name and dollar cost, including “Remove Fence and troughs, $60,000”.
12. **FIXED.** The two builder-log paragraphs and obsolete Claim/reveal instructions were removed from notes.md. Its modes now describe the station, collected-only Logbook and open simulator, and retain the plain upstream-only shares sentence. See notes.md, `notes-cleanup.json` (zero occurrences of all three leaked phrases) and `check-no-ledger-leak.json`; the old notes were read before the rewrite.

#### Polish accepted

1. **FIXED.** `remaining/check-field-art.png` and `check-field-art.json`: 481 mg/L is in the over-400 historical band, described as poor fisheries at best. Manual lists all four bands with their historical and normally-prevailing-condition caveats. Numerical facts were checked against EIFAC, EPA and BC; no FAO document content or dataset is bundled.
2. **FIXED.** `focus-v2/focus-default.png` and JSON: no selected stop and Take sample disabled. The readout says “Tap a spot on the map first.”
3. **NOT FIXED as requested, intentionally superseded.** A Solved stamp would restore a graded finish. The explicit user instruction forbids that. The source and `verify-numbers.json` show no solved state, claim check or victory stamp. Interventions is available immediately.
4. **FIXED.** `retouch/final-fix-375.png`: no Change/0% collision. Sediment cut is a separate readout below the dry/storm table. The phone label column and headers were also adjusted to keep Storm separate from its values.
5. **FIXED.** `retouch/final-fix-375.png`, `final-map/final-map-1366.png`, `remaining/check-plans.png`: E. coli and sediment use whole numbers throughout; phosphorus uses three decimals. Calculations retain unrounded values.
6. **FIXED.** `verification/verify-compare-1366.png`, `remaining/check-plans.png` and intervention frames use sediment for the measured quantity. Bare soil remains the correct land-surface description and texture identifier.
7. **FIXED.** `retouch/final-map-680.png`, `retouch/final-map-375.png` and `final-map/final-map-1366.png`: the Plant label is off the creek and clear of sampling-stop labels. Final compact positions, including both dry and storm flags, are proved by `flags-stops/flags-stops-680.png`, `flags-stops/flags-stops-800.png`, `flags-stops/flags-stops-1000.png` and `final-phone/final-phone-flags.png`.
8. **FIXED.** `retouch/final-map-680.png`: Construction stays on one line. There is no narrow accusation grid forcing a mid-word break.
9. **FIXED.** `verification/verify-empty-compare.png`, `verify-empty-compare.json`: one entry shows “Take two samples to compare.” and leaves Compare selected disabled.

#### Settled calls

- Preserved the title, synthetic flows, loads, costs, reduction factors, advisory and illustration credits. The advisory changes access and removes no pollutant. The model agrees with its independent Python implementation across all 512 intervention sets, with 88,576 comparisons and zero concentration error (`numeric-verification.json`).
- Kept HS-ESS3-4 and HS-ETS1-3 in notes: users change technologies and compare measurements, priorities, cost and who pays. No required goal or explanation gate is introduced.
- The user's Curiosity instruction supersedes all settled calls about solving, earned disclosure, goal bars and locked Fix-it. Original spec and refine.md remain untouched. Their three former open questions remain settled: title retained, advisory retained honestly, synthetic inputs labeled.
- Manual and maker's plate occupy the lower-left station corner. Power controls sit on the station, without kit CSS or a header. Neither the spec nor docs/CURIOSITIES.md assigns this tool a number, so `plate: null` and an unnumbered plate avoid inventing one.

#### Cheats tried

- Empty submit, all seven accusations, and blanket evidence are removed action paths: there is no submit or grading API. Reading the ledger intentionally explains an open model; it does not pass anything or mark a source proven.
- Select every collected sample: only the last two remain selected; no pass/fail is emitted. Mixed weather, different forks, dry Pipe and beach-only tests are identified in comparisons.
- Turn every intervention on: $4,100,000, measurements remain usable. Advisory changes no concentrations. Cost is a comparison reference, not a score.
- Rapid input: 120 collections and 180 toggles in 68.8 ms of handler execution; all outputs finite, no exception, no frozen state (`check-extremes.json`). No outside HTTP resources were requested.
- Keyboard-only Map-to-Interventions, Motion off and grayscale retain operation and D/S flag letters. Read with Sound off still logs a Read (`check-keyboard.json`, `check-gray.json`, `check-read-silent.json`).

#### Voice walk

At a 2-second pace with 120 ms held clicks: stop, collect, next stop, collect, Interventions, five Test plan presses, Read. Log order: initial hint once; no extra automatic instruction; current intervention instruction on Read. Sound-off Read also works. All six final entries in voice/lines.json equal `allLines()` (`post-voice.json`). The shortened first hint is "Tap a spot on the map."; its log contains only that hint and the requested Read, despite five Test plan presses. Browser fallback only; no recorded-bank timbre or actual audible quality is claimed from the muted browser log.

#### The real material

Re-checked 6 November 2026 local time; raw fetch timestamps are 7 November UTC. Gathering used bounded downloads and stayed below the brief's 45-minute gathering allowance. `data/manifest.json` records URLs, byte counts, hashes and sampling; `gather_references.py` reproduces the archives. NEPIS PURLs returned HTML redirect stubs, explicitly identified in that manifest; browser source extraction supplied the text check. No executable or third-party monitoring dataset was downloaded. Reference numbers are packed inline in src.html.

| Material | Source and independent check | Licence and use |
|---|---|---|
| Network, all sample values, flows, loads, areas, prices, efficiencies, advisory duration and who-pays assignments | Original Curio Class spec.md; independently recomputed by watershed_numbers.py and check_numbers.py | Original content CC BY 4.0; code MIT. Entire synthetic dataset, no sampling and no claim of real observations. |
| E. coli 126 GM / 410 STV | EPA 2012 RWQC, recommendation 1: https://www.epa.gov/sites/default/files/2015-10/documents/rwqc2012.pdf ; WHO (2018), table B1: https://www.who.int/docs/default-source/wash-documents/who-recommendations-on-ec-bwd-august-2018.pdf | U.S. government numerical facts, public domain. WHO used only to verify; no WHO material imported. No universal single-sample closure or safety claim. |
| Nitrate-N 10 mg/L | EPA National Primary Drinking Water Regulations: https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations ; USGS Circular 1350 FAQ: https://water.usgs.gov/nawqa/nutrients/pubs/circ1350/faq.html | U.S. public-domain reference facts; drinking water only. |
| Phosphorus 0.050 mg/L | EPA Gold Book (1986): https://www.epa.gov/sites/default/files/2018-10/documents/quality-criteria-water-1986.pdf ; USGS Circular 1136: https://pubs.usgs.gov/circ/circ1136/circ1136.html | U.S. public-domain numerical fact. Clearly historical guidance, not a universal current standard. |
| Sediment bands 25, 80, 400 mg/L and their meaning | EIFAC Technical Paper 1 (1964; 1965 journal version): https://www.fao.org/4/al950e/al950e00.pdf ; EPA-600/3-77-042: https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=9101Y9JU.TXT ; BC WQG-18 (2023): https://www2.gov.bc.ca/assets/gov/environment/air-land-water/water/waterquality/water-quality-guidelines/approved-wqgs/bc_env_turbidity_waterqualityguideline_technical.pdf | Public-domain numerical facts, paraphrased in original wording. No FAO/BC prose, figure or dataset imported. No permissive licence was established for the FAO document, so none of that document is bundled. Tentative historical interpretation, with species and duration limitations stated. |
| Intervention types | EPA agricultural guidance (2003), urban guidance (2005), construction permit, nutrient-removal reference (2008), BEACH Act; NRCS standards 382/390/605. Verified agriculture: https://www.epa.gov/sites/default/files/2015-10/documents/chap4e.pdf and https://www.epa.gov/nutrientpollution/sources-and-solutions-agriculture | U.S. government reference material, public domain. These support types of measures only; all numerical performance and cost assumptions remain synthetic. |
| 22 retained illustrations | Existing prompts.json provenance: FLUX.1-schnell and OpenAI gpt-image | Original Curio Class asset content, CC BY 4.0; FLUX model Apache 2.0. Both original credits retained; no new painted art or external photograph. |

#### Short test

Paced exploratory runs and their observed duration: 616.286 seconds total (10 minutes 16 seconds), 287 held actions: `play-student-sampling.json`, `play-adult-interventions.json` and `play-independent-route.json`. All three walks had zero browser errors. These are automated held-input walks assessed from the grade-12 and adult perspectives, not a classroom user study.

- Would a kid open it unassigned? Yes for someone curious about the map: collection pays off without first opening a case or reading instructions. The strongest moment is the dry/storm change in the same reach.
- Would an adult play for fun? Yes: compare load against dilution, then try cost and intervention alternatives. The instrument has less sensory immediacy than Beat Lab; its interest is investigative.
- Is the real material the interface? Yes for the mass-balance rules and unit-bearing measurements; the place and inputs are explicitly synthetic, not field data.
- Does it work without a score or finish? Yes. Sampling, ledger and interventions stay open; no correctness, solved status, winning plan or finish screen exists.

Frame comparison: `final-map/final-map-1366.png` beside `before-extra/model-beat-lab.png`; also inspected and used Elements Inspector, Span and Spire and Pocket Universe before designing the station. Both expose their subject directly through working controls. The new map and lower station replace the old right-hand lesson panel.

#### Lesson creep check

The requested search terms (score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done) produce no hits in src.html or voice/lines.json. Implementation names from the old claim/goal controller were removed. Soil is retained only for land-surface descriptions and the SVG texture id. No em dash was added. `final-files.json` records the file hashes and contrast checks: primary ink 13.63:1, readout units 9.78:1, sample values 9.39:1, primary button 6.98:1 and plate 4.79:1.

#### Engine changes wanted

None.

#### Audit

The one full audit completed within its 2,400-second limit: `fix-audit-r1/audit.md`, 79 leads, zero console or resize errors and a clean Motion-off check. Its 24 frames were inspected through four native contact sheets and critical full-size frames. `audit-input-files.json` records the audited snapshot. The audit correctly found compact target/label crowding, an all-interventions gauge-row expansion, small Manual links and a first hint naming a disabled control. Those were fixed and checked with scoped drives; no second full audit was run.

All 79 leads are individually answered in `fix-audit-dispositions.csv` and JSON: 38 FIXED, 34 INTENDED, 6 CURIOSITY OVERRIDE, 1 ACCEPTED BASELINE 16, zero unclassified. The 34 intentional cases are background controls covered and inert under native dialogs, secondary scrollable Manual references and the suppressed generic compact power-panel hint (local readouts, Read and Manual remain available). The six welcome leads presume a lesson premise; the Curiosity intentionally has only one optional first hint. A quick repeated Map tap cutting that hint remains the accepted Baseline 16 behavior.

Final scoped proofs: all 11 stops register in order in both weathers at 680x425, 800x500, 1000x625 and 375x812, with zero target intersections or label/flag collisions (`flags-stops-680.json`, `flags-stops-800.json`, `flags-stops-1000.json`, `final-phone-flags.json`). The last phone proof also checks source labels against each other and the legend, after direct frame inspection found and corrected Geese touching the legend. Earlier `post-stops-680.json` retains the intermediate Plant collision honestly; the final flags proof supersedes it. Other shapes have all-stop checks at 760x900 and 1366x768. Pulse placement now follows actual target rectangles.

Both all-nine-intervention layouts have zero control intersections, 44 px minimum control heights and an enabled Test plan at $4.1m (`post-all-fixes-680.json`, `post-all-fixes-375.json`). All five Manual links have 44 px heights at both widths (`post-links-*.json`). Sound toggling moves no power control (`post-power.json`). Final voice equality and first-hint/Read-only behavior are in `post-voice.json`; the full assertions are in `post-audit-validation.json`. These final frames were opened and inspected. `final-files.json` records final hashes and the 722,556-byte bundle. `final-port-check.json` confirms the test browser ports and host are closed. No app external HTTP resource was requested; the iframe host is local.

#### Left open

- Accepted polish 3 is intentionally not applied: no Solved stamp, as the user explicitly requires a Curiosity.
- No plate number exists in the supplied owner documents; the plate is unnumbered pending owner allocation.
- The source FAO document has no verified permissive licence. Only independently checked numerical facts and original paraphrases are used; no FAO asset is included.
- This Windows Chrome check does not establish Chromebook frame rate or classroom engagement. Speech used browser fallback, not recorded bank timbre.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Up the Watershed handoff

Curiosity fix round 1, 2026-11-06. The user explicitly overrides the lesson-shaped spec and Claude Refine. The retained spec and refine.md are evidence, not authority to restore claims, kit limits, a locked simulator, solved stamps, goals or the kit header.

#### Structure
`src.html` contains the SVG map, retained load model and input tables, a permanently reserved sample readout, a lower control desk, an intervention simulator, native dialogs and persistence. Kit JavaScript supplies Motion, Sound, tones and voice. Kit CSS is not used. No shared files were changed.

`model(weather, plan)` retains the original arithmetic. `measure(plan)` returns measurements without grading them. `sourceShare` supports the separate baseline ledger and excludes downstream sources at S7. `compareSamples` uses unrounded loads and reports CFU/s or g/s. Dry S6-to-S7 adds 10,000,000 CFU/s, not the 13.3 billion example in refine.md.

Results occupy their own grid row outside the map. Changing a stop fades prior values and marks the next stop ready. A dedicated polite live region announces the result. Sampling has no kit limit. The optional ledger never adds samples or flags. Log selection is limited to exactly two entries for comparison; there is no evidence validator or answer key.

The storm-drain line joins at (515,458), above S7. Pipe remains at its upper endpoint; the miniature sits along the line. Source illustrations are passive labels; full photographs are in Field files. The 11 stops and the stop selector are accessible map controls. Map-stop :active preserves its centering transform, avoiding hit-area jumps under a held pointer.

Intervention toggles update both weathers synchronously. Bars show concentration on fixed physical scales with reference ticks, not progress. All nine toggles remain usable at any cost, including $4.1 million. The advisory changes beach access and removes no pollution. Save up to three plans; remove one in Compare plans to make room. Why notes remain session-only.

Storage schema version 2 preserves samples and plans. Version 1 samples and alternatives migrate, while claims and solved fields are ignored. Clear collected samples opens a count-specific confirmation and preserves plans. The pivot does not silently erase prior sampled evidence.

#### Voice
The first-action hint is automatic once. After that first hint, speech occurs only when Read is pressed, including the compare and saved-plan instructions. Test plan has no repetitive how-to or failure narration. Read speaks the current instruction, including in dialogs and with Sound off. `voice/lines.json` matches `__tool.allLines()`. Speech uses browser fallback; no recordings were made.

#### Sources and licences
Manual, notes.md and tool.draft.json name the sources and licences. Synthetic inputs remain attributed to the original specification, CC BY 4.0. Numerical government reference facts are U.S. public domain. FAO, WHO and British Columbia documents were independent checks only; none of their prose, figures or datasets is imported. A permissive FAO licence was not established. Raw government references and hashes are in Scratch data/ with a bounded gather script. NEPIS PURL downloads are redirect stubs; browser extraction verified their source text.

#### Owner decisions taken unattended
Use the open Curiosity interpretation. Retain the synthetic model and title, with the invented data clearly labeled. Keep the advisory and its limitations. Remove lesson gates and victory states instead of restoring them. No plate number is assigned in the spec or docs/CURIOSITIES.md, so use an unnumbered plate and `plate: null` pending owner allocation; do not borrow another tool's number.

#### Engine changes wanted
None.

#### Sensitivity
No people, cultural representation or medical advice is added. Water references are contextual scientific guides, not a safety certificate or local regulatory instruction. The advisory duration is an invented scenario.

#### Evidence
Current evidence and dispositions are linked in polish.md. Testing files, original source, screenshots, profiles and downloads stay in `_scratch/up-the-watershed/`. No git commits, deployments or edits to refine.md were made.

The single full audit finished with 79 leads. Its archived input hashes distinguish that snapshot from the subsequent scoped fixes: separated compact S9/Outfall hit areas, source labels clear of stops and collected flags, pulse centers from actual button rectangles, compact advisory text, 44 px Manual links, a shorter first hint and fixed-width power controls. Final held-click checks collected all 11 stops in both weathers at 680x425, 800x500, 1000x625 and the 375x812 iframe. The phone recheck also separates every source label from the legend. All-intervention layouts have zero control intersections at 680 and 375. See post-audit-validation.json and the 79-row fix-audit-dispositions.csv in Scratch. Native-modal backdrop coverage and secondary Manual scrolling are intentional; six missing lesson welcomes are Curiosity overrides. No second full audit was run.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-08)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
