# Polish: circuit-bench (Codex fix, round 2)

Scope: the 2026-11-06 exit check retains the round 1 repairs and leaves should fix 16 open, caused by should fix 5's per-frame placement search. The integrator's concluding call also requires standards metadata and notes to match spec.md Map. No questions were asked in this unattended session. Evidence root is `_scratch/circuit-bench/`.

The first line and final Integrator call in refine.md make this a narrow round 2: short-chip placement/performance and the written standards scope. The old blockers and other should-fix items were already repaired in the checked-out source. Their original faults did not recur in the regression checks described below; they were not reintroduced to manufacture before frames. RETAINED means accepted by the supplied round 1 exit check, unchanged here, and not claimed as a newly verified fix. Scientific code, controls, narration and artwork before drawShortChips are byte-identical to the saved round 2 baseline.

## Blocker

1. FIXED, round 1 repair verified again: coil at 50/100/200/400 turns gives 28.37/46.93/64.60/76.26 degrees; core 89.07; cells 1 to 4 give 15.71/28.37/37.91/44.99; reversal -46.29; open switch essentially zero. Axial +29.17 versus beside -73.20. `r2-proof-coil.json`, `r2-proof-coil-equator.json`, viewed proof and starter-6 frames at 1366x768. Original pinned-needle fault not reproduced; no new magnetic change.
2. RETAINED: Oersted starter still reads -13.71 degrees (`r2-starter-5.json` and viewed 1366x768 frame), compass above the straight jumper. The reversal/open-switch sequence was not rerun this round; its round 1 exit acceptance remains the evidence for those steps. No new fix claimed.

## Should fix

1. RETAINED: event narration, pop and crackle code unchanged; not freshly walked through burn and short repeats. The supplied exit check accepted the round 1 repair. See Voice walk for this round's limits.
2. RETAINED: burn tag rebuild and tap-to-replace code unchanged; not freshly burned/tapped this round.
3. RETAINED: motor latch and push-button starter unchanged. Motor starter frame viewed at 1366x768 and 800x500; latch/stall sequence not rerun.
4. FIXED, round 1 repair verified again: blocked LED gives 0.00 A on both current ranges; empty and missing probes give - -. `r2-proof-ammeter-cheats.json` and viewed 1366x768 frame. Original fault not reproduced.
5. FIXED: existing clear placement retained while removing its per-frame search. Same busy-board positions before/after: (720,52), clearance 9 px for one short; (300,52), 47 px and (720,52), 9 px for two shorts. The simple short with probes retains 9.866 px clearance at 1366x768, 680x425, 800x500 and 1920x1080. All frames viewed. `r2-before-clean-*.json`, `r2-after-*.json`, `r2-proof-short-clearance.json`, `r2-short-*.json`. New WeakMap entries reject stale saved chips and refresh on relevant geometry changes. See cache attempts below.
6. FIXED, round 1 repair visually verified again: 9 V body and snaps, single label; viewed starter-3 and turn-label frames at 1366x768. Original overprinted AA label not reproduced.
7. FIXED, round 1 repair visually verified again: sharp part text in viewed starter, 680 Adjust and 1920 projector frames. The old fillText interception returns an empty list because rasterized part text is already cached; that empty diagnostic is not proof. Source shadow-reset logic is unchanged.
8. RETAINED: fuse explanation and Use A for bulbs remain in the captured Manual and unchanged event handler. Fuse was not freshly blown this round.
9. FIXED, round 1 repair verified again: captured Manual explicitly says every coil is 4 ohms with thicker wire as turns rise. `r2-proof-manual.json`; no resistance-model change.
10. FIXED, round 1 repair verified again: required real-bench heat/burn/mains sentence remains in the captured Manual and teacher notes; battery-level DC only remains in notes. `r2-proof-manual.json`.
11. FIXED, round 1 repair verified again: visible Motion OFF and Sound OFF in `r2-proof-toggle-off.json` and its viewed 1366x768 frame; labels and switch marks remain.
12. FIXED, round 1 repair verified again: four real Tabs focus board; 3 px dark outline at -6 px inset. `r2-proof-focus-board.json` and viewed 1366x768 frame.
13. FIXED, round 1 repair verified again: real Tab focus shows dark 3 px outline on the 680x425 paper tray, with the light rim retained. `r2-proof-adjust-680.json` and viewed frame. Previously documented contrast ratios are retained, not newly measured.
14. FIXED, round 1 formatter verified again: volts, milliamps, milliwatts, kilohms, no reading, fuse open and Meter off. `r2-proof-read-format.json`. These are formatter outputs, not a new audible walk.
15. RETAINED: centralized drawer pressed-state synchronization unchanged; no fresh placement sequence this round.
16. NOT FIXED to a strict 60 fps at 4x CPU throttle. The specific round 2 regression is fixed: placement is cached, obstacles sampled once per geometry, candidates scored once without sorting. Before/after measurements at 1366x768 are below. Desktop one/two-short runs now reach 59.81/60.05 fps, but 4x runs reach 42.68/43.54 fps. The no-short control is also below the bar (38.75 fps). No blanket performance PASS is claimed.
17. FIXED, round 1 repair verified again at 680x425: Adjust is non-modal, tag y204 and tray y239; resistor, LED and 20.5 mA remain visible. `r2-proof-adjust-680.json` and viewed frame. Original modal obstruction not reproduced.

## Polish accepted

1. RETAINED and viewed: warm one-bulb and parallel glow, dimmer series glow, 1366x768 starters 0 to 2.
2. RETAINED: burnout flash/smoke code unchanged; transient was not freshly captured this round.
3. FIXED, round 1 repair verified again: battery tag says supplies 9.68 A in `r2-proof-short-clearance.json` and viewed 1366x768 frame.
4. FIXED, round 1 repair verified again: discovery attributions including Oersted in 1820 remain in captured Manual (`r2-proof-manual.json`).
5. FIXED, round 1 repair visually verified again: default loose tips have open-end rings, viewed `r2-starters/r2-default.png`, 1366x768.
6. RETAINED: drawer drag ghost code unchanged; no fresh mid-drag capture.
7. FIXED, round 1 repair visually verified again: probes reach meter jacks and dial has range legends; viewed short/probe frames at 1366x768, 680x425 and 800x500.
8. FIXED, round 1 repair verified again at 1920x1080: tag font 22 px, board scale 1.437. `r2-proof-projector.json` and viewed frame.
9. FIXED, round 1 repair visually verified again: tools above board at 680x425, push button visible at 800x500. Viewed Adjust and motor frames; `r2-proof-motor-800.json` records part coordinates.
10. RETAINED: LCD settle/read announcement code unchanged; no fresh one-second live-region timing measurement.
11. RETAINED: angle-only compass tag code unchanged; no fresh selection capture of that tag.
12. FIXED, round 1 repair visually verified again: opening and idle motor tags show zeros, not leakage micro-readings; viewed default and starter-7 frames at 1366x768.
13. FIXED, round 1 repair visually verified again: reversed LED text upright in viewed `r2-proof-turn-labels.png`, 1366x768.
14. FIXED, round 1 repair visually verified again: AA polarity alternates in viewed default and starter frames, 1366x768.
15. FIXED, round 1 repair verified again: high-draw runtime and diode ohmmeter caveats remain in captured Manual (`r2-proof-manual.json`).
16. RETAINED: resistor aria-valuetext still uses spoken formatter; kilohms formatter is verified, but no fresh slider event/aria measurement.
17. FIXED, round 1 repair visually verified again: top-left keeps only DC and pitch; maker plate retained, viewed default at 1366x768.

## Settled calls
Curiosity brief wins. No goal, score, level, quiz, finish or kit header added. Physics constants and circuit solver unchanged. No coil-resistance spec change. The integrator's written standards decision is applied to tool.draft.json and notes.md; catalog files are outside this session's write scope.

- Magnetism stays an instrument readout with real field direction; no target angle or challenge added.
- First-tap hint suppression and Read behavior are retained, including opening a drawer first.
- Starter loads still dismiss the first-action hint.
- Manual and Notebook remain modal; compact Adjust remains non-modal. Existing scrolling and coverage are reported under Audit.
- Burn wording remains exactly: That part burned out. Tap it to replace it. Tap-to-replace code is retained.
- Motor starter keeps its push button; the separate shaft latch is retained.
- AA, bulb, LED and motor constants are unchanged. No score, finish or magnetic target was introduced.

## Cheats tried
No score, check to pass or finish exists. The meaningful attempts target misleading/stale instrument output.

- 240 unchanged redraws: zero new layout searches. Current changed while staying above 3 A: zero new searches.
- Add a wire, replug its endpoint, remove it: exactly one layout per change; result agrees with an independent evaluation of the original clearance rule.
- Attach, move and remove a probe: exactly one layout per change and same independent placement result.
- Move and rotate the battery: exactly one new layout for each source centre change.
- End a short: chip removed. Restart it: one fresh layout. Restore a forged save with chip (-999,-999): ignored and correctly recomputed.
- Thirty extra solves/draws: layout count unchanged. Real Red probe click and arrow/Enter input: geometry refreshes (layout count 1 to 3) and clear label retained.
- Floating-probe shortcut: empty and missing probes stay - -; a genuinely blocked but attached current branch reads zero.

Evidence: `r2-cache-invalidation.json`, `r2-probe-real-move.json`, `r2-proof-ammeter-cheats.json`. All corresponding frames viewed.

## Voice walk
No narration code, event triggers, hint or bank text changed. Current browser allLines() exactly equals voice/lines.json's three lines; recorded in `r2-proof-read-format.json` and checked by script. Read formatter outputs were rechecked as numbers/text. A new full audible burn/short repeat walk was not performed; no fresh heard-count claim is made for those retained round 1 repairs. The final audit's own voice evidence is reported below. Existing missing recordings still use browser speech fallback; none were generated.

## Engine changes wanted
None.

## Audit
FINISHED, once, last, within its 2400 second deadline. Command: `python scripts/audit_tool.py circuit-bench _scratch/circuit-bench/r2-fix-audit --port 9911 --profile S:/CurioClass-codex/_scratch/circuit-bench/chrome-r2-audit --host-port 8715`. Muted Chrome; no rerun. Report: `r2-fix-audit/audit.md`; 94 frames reviewed on contact sheets 0 to 10, with full-size phone Manual and compact/phone part-tag frames also viewed.

All 112 mechanical leads are accounted for here:

| Rows | Disposition |
|---|---|
| 38 overlaps | Board controls, cursor and hint intentionally overlay the canvas. The two phone drawer title/Close bounding boxes overlap, but the visible words do not touch; full-size phone Manual viewed. Retained settled design. |
| 3 scroll-panel leads | Phone parts strip and Manual source links are intentionally scrollable. The 680x425 AA battery Adjust tray puts Turn/Remove in horizontal overflow; cell count and Reverse stay visible with the part and its tag. This existing secondary-control limitation is recorded below, not called newly fixed. |
| 10 hidden hints | Starters and restored circuits dismiss the first-action hint. Correct under the Curiosity brief and explicit settled call. |
| 50 text-under-box leads | Manual and Notebook intentionally cover the bench beneath them. No text within the active drawer was shown hidden under an accidental box in the reviewed frames. |
| 9 keep-region leads | Eight are the intentional Manual/Notebook modal coverage; one is two phone board samples behind board tools while Adjust is open. Part, tag and adjustments remain visible. Settled instrument/drawer behavior retained. |
| 2 missing welcomes | First tap on Notebook or Manual suppresses the one-time hint. The hint remains on the mat and Read speaks it. Explicitly accepted by the supplied exit check; no lesson welcome added. |

Motion off: clean, nothing runs forever. Full final resize stress: no exceptions and no controls left disabled. All 36 held-click rows have empty error cells and focus retained; ten five-click and ten quick-tap rows are clean. Read logs the hint followed by Meter off on the opening bench. These checks do not exercise a fresh burnout/short event sequence. The audit does not measure frame rate or prove magnetic equations; the targeted numbers above do that work.

No new cache-related regression was found. A blanket gate PASS is not claimed because should fix 16's strict throttled 60 fps bar remains unproved. The owned Chrome/host listeners are checked closed before publishing this report (`r2-cleanup.json`); port 9910 was handled by the driver's owner-aware cleanup. No unrelated browser was closed.

## Left open
Strict 60 fps at 4x throttle remains unproved; physical Chromebook performance was not measured. The round 2 placement regression is removed. The standards call is applied in the permitted metadata and notes; no catalog or module files were edited. The coil-resistance scaling, schematic and generator open questions remain untouched. No ten-minute student/adult play session was repeated in this narrow rendering repair. The existing AA battery Adjust tray at 680x425 requires horizontal scrolling for Turn/Remove; the main cell-count and reversal controls remain visible. Event speech and transient burn repairs marked RETAINED were not freshly walked in this round.

## The real material
Only rendering/cache code and standards scope were changed. No scientific fact, model constant, dataset, source text, artwork or recording was added or retuned. Existing named sources and licence statements in the Manual and tool.draft.json remain. The standards-scope authority is the integrator's 2026-11-06 call in spec.md Map. Original code is MIT; original instrument text/graphics CC BY 4.0. No downloads or data sampling were needed.

The existing factual sources remain OpenStax College Physics 2e and University Physics Volume 2 (current cited licence CC BY-NC-SA 4.0, facts only), Georgia State University HyperPhysics (copyright, diode facts only), Vishay document 31001 (copyright, E12 facts only), NOAA/BGS World Magnetic Model (government context, no coefficients), Britannica (copyright, attribution only) and CPSC (public US government battery-hazard information). No material from these sources was newly copied or fetched. All constants remain declared Curio Class design assumptions. The source URLs and licensing details remain in the bundled Manual and tool.draft.json.

## Performance evidence
Same exit-check fixture, 1366x768, 30 parts and five lit bulbs. The initial broad before batch used allowed port 9910. The clean before rerun and all after/targeted batches use muted Chrome 9914. Before files are the clean rerun against the saved unmodified bundle except the one-short/4x row, which comes from the initial batch; after files use the generated fix-2 bundle. One-short fixture has 17 wires, two-short fixture 16. Units are ms unless fps is named.

| Case | Before draw | After draw | Before fps | After fps | After mean frame work |
|---|---:|---:|---:|---:|---:|
| One short, 1x | 29.01 | 0.187 | 31.38 | 59.81 | 0.521 |
| Two shorts, 1x | 52.49 | 0.172 | 18.08 | 60.05 | 0.511 |
| One short, 4x | 161.07 | 1.482 | 5.42 | 42.68 | 2.226 |
| Two shorts, 4x | 304.81 | 1.277 | 3.04 | 43.54 | 2.024 |

One-short 4x before value comes from `r2-before-1short-4x.json`; the others from `r2-before-clean-*.json`. Every after result shows shortLayouts unchanged over 180 animated frames plus 60 explicit redraws. Matching no-short control: 59.73 fps at 1x and 38.75 fps at 4x (`r2-no-short-*.json`). This control supports removal of the short-specific cost; it does not certify 60 fps under throttling.

The initial long two-short/4x browser evaluation hit the driver's 60-second per-call deadline. It was retried once with 60 frames and 10 explicit draws and completed cleanly. All shell/process commands had bounded lifetimes; bundles 120 seconds, drive batches at most 300 seconds, final audit 2400 seconds.

## Regression and bundle
Default and every one of the eight starters re-shot at 1366x768; all viewed. Existing coil, meter zero/floating, focus, 680 Adjust, 800 motor, 1920 projector, Manual and toggle repairs received targeted checks. All successful final drive batches report zero console errors. Default and performance runs report an empty automatic resource list. Physics examples remain one bulb 0.29636 A, series 0.22643 A, parallel 0.58524 A total, red LED/330 ohm/9 V 20.496 mA. No constants were changed.

Bundle: 119,919 bytes. The repository's unmodified check() and notes_sections() passed against a scratch mirror of this tool, avoiding the global rebundler's writes to other tools. `contract-results.json`. Source and voice contain no em dash. No git commands or commits were made, and refine.md and refine/ were not edited.

Viewed frame groups: `r2-before/`, `r2-before-clean/`, `r2-after/`, `r2-control/`, `r2-checks/`, `r2-proof/`, `r2-starters/`, via their r2 contact sheets and selected full-size frames. Final audit frames are listed in its audit.md. The maker plate, Manual and instrument surface remain; no lesson structure was introduced.

## Lesson creep check
The new internal score and bestScore variables rank geometric label positions; they are not displayed or saved as student scores. Existing references to electrical points and cached raster/geometry values describe the instrument. Voice lines are unchanged and contain none of the lesson terms. No goal ladder, score display, level, quiz, finish screen, welcome gate or kit header was added.
