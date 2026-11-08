# Polish: span-and-spire (Codex fix, round 1)

The current refine.md is an owner-approved instrument pivot: 0 blockers, 0 should-fix items, 7 pivot items.
Evidence root: _scratch/span-and-spire/. All listed PNGs were inspected, directly or in the named contact sheets.
The source, notes, voice inventory, audit states, handoff and owner-authorized spec sections were updated.
No refine file or shared engine was edited. No commits were made.

## Blocker
None in the current list.

## Should fix
None in the current list.

## Pivot items
1. FIXED: Free build is the front door. No header, target badge, promise card or budget limit appears on entry. Before: before/before-bridge-1366.png and before/before-bridge-680.png. After: sizes-bridge/bridge-1366x768.png and size-repairs/bridge-680x425.png. front-door.json: budget false, promises hidden, badge elements 0, headers 0.
2. FIXED: All five trucks and every wind/shake/top-load choice are available independently. No progression gate was introduced. 24 final mode/size results in size-summary.json show 263 primary-target measurements without coverage, clipping or size failures. A steady wind and a full shake were run directly on a fixture with no earlier crossing: wind-steady.json and shake-steady.json.
3. FIXED: Budget starts off and opens a $3,000 to $30,000 dial, initially $9,000. Done closes its native adjustment dialog while retaining the limit on the switch. It compares costs without locking tests. The game-price line is gone; the Manual states the estimate caveat. A real member tap reads Timber, 4.00 m, $200, pull 450 kN, squeeze 312 kN (member-price.json, misc/member-cost-current.png). At cost $9,863, dial values $3,000/$9,000/$30,000 all leave the county brief failed and create no county record (budget-cheat.json, repeated after the dialog repair in budget-final-cheat.json).
4. FIXED: All 25 Tags are optional logbook observations with timestamps and real evidence, opened from Manual. Promises live there as an optional brief. No badge, flying stamp, stamp sound or tag narration remains. Before: before/before-tags-1366.png. After: focused/logbook-semi-proof.png and cheats-extra/voice-side-fixed.png. semi-proof.json records Semi crossed, worst member 57.6%, and a $8,783 margin record. Subsequent fresh tabs retained these records. Legacy date-only records explicitly disclose missing historical measurements. The book updates if a test finishes while it is open. All crossing observations now require a whole-crossing pass, including no lost member. Test all records the tested design rather than a different current rig.
5. FIXED: Blueprint drafting surface, stress colors/arrows, live needle gauges, monospace units and a bottom truck tray/material rack/test console replace the kit header and right panel. All 27 existing paintings and the structural drawings remain. Gauges show total mass, actual current use and unmagnified top sway; NO FRAME and LOOSE replace false zero readings. The 141.6% over-scale reading keeps its number while the needle stops (gauge-over.json). All five masses match (gauges-mass.json); 50 m/s wind reads 72.31% and 13.0 cm (wind-steady.json). After frames: sizes-bridge/, sizes-tower/, sizes-yard/, with size-repairs/ superseding only touched compact/phone frames. Contrast: 12.35:1 text/button, 8.50:1 muted/panel, 7.17:1 pink-button text, 10.05:1 dial labels.
6. FIXED: Engraved lower-left plate reads Curio Class Instruments ? No. 01 ? Span and Spire. Manual opens beside it and holds how-to, honesty notes, keyboard instructions and a first-position logbook button. Motion, Sound and Read remain on a yard power panel. Escape restores focus to Manual from both dialogs (manual-focus.json, logbook-focus.json). Phone telemetry is stacked to keep the top load clear: size-repairs/tower-375x812.png. Compact Manual clipping was reproduced and repaired at both 680x425 and 800x500; final measured targets are fully inside.
7. NOT FIXED in full (hardware check unavailable): Keyboard construction, testing, reduced motion, contrast, browser Read voice and offline operation were preserved and observed. Keyboard made an eight-member/eight-joint first triangle (keyboard.json); Motion-off Go still fails the bare deck without shortening the run (calm-fold.json). All 23 model function bodies are unchanged (engine-preserved.json). The 60-member fixture refused member 61, with Windows callback mean 1.05 ms, p95 2.10 ms, max 3.20 ms (capacity-timing.json). Actual school Chromebook performance remains unverified. The software checks passed, including the repaired quick-tap welcomes; no claim is made about unseen Chromebook hardware.

## Polish accepted
None separately listed.

## Settled calls
- Applied: Yard, Save, Old farm bridge, Open and Borrow remain. A real Borrow all adopted the sample's 21 members and cleared its ghost (borrow.json). Test all populated a saved tower's comparisons (misc/yard-test-all-current.png).
- Applied: Bridge and Tower are test rigs in the same yard console; there is no pill mode row.
- Applied: spec.md Screens and modes, Goals, Look and Teacher note now describe the approved instrument. Related obsolete stamp/voice wording was aligned. Open questions were left in place.

## Cheats tried
- Crossing observations 1, 5-8, 10-18: select every truck on the bare deck and press Go. It records only the truthful fold, with no crossing or margin record (bare-cheat.json).
- Switch from a pickup to the semi late in a weak Pratt crossing to skip its hardest position. The full sweep still returns 101.6595%, pass false, no semi record (late-truck.json).
- Add eight crossed cables and rely on the cable count or slack to earn a crossing observation. The semi still fails; only the actual buckle is recorded, with no Pull only or Taking turns record (cable-cheat.json).
- Sweep the budget or raise it to $30,000. The independently fixed $9,000 county constraint stays failed at $9,863; no record appears (budget-cheat.json).
- Tick every promise without testing. Load checks and county remain unknown, the two genuinely clear geometry checks are true, and Every promise is absent (all-promises.json).
- Failure observations 2-4 and 9 are observations, not skill gates. A real bare-deck fold, squeezed-member buckle, stretched-member snap and failing Old farm bridge produce their respective evidence; none claims a successful design (bare-cheat.json, cable-cheat.json, snap-proof.json, old-observation.json). The first attempted snap fixture buckled instead and was not counted as a snap.
- Tall-tank observations 19, 21-22 and 25: remove the tank, use a shorter tower, or substitute an easier shake. Empty top earns no tank observation; 20 m in 70 m/s wind fails without Spire; a 26 m tower surviving 2.5/s leaves Valley quake and Town tower unrecorded (empty-top-cheat.json, spire-cheat.json, town-cheat.json).
- Pluck observation 20: restart a pluck every second for six taps. It never reaches three sways and gives no Pluck record. A single uninterrupted pluck does record three sways (pluck-reset.json, pluck-three.json).
- Wind observation 21: hold 50 m/s for 3 s, change speed and return for 2.5 s. No wind pass is stored. A steady 5 s produces the real wind record (wind-reset-cheat.json, wind-steady.json).
- Shake checks 23-25: sweep speed every 1.9 s for over 17 s. No completed shake is stored (shake-sweep-cheat.json). Real resonance failure at 0.80/s records failure near the 0.76/s own rate (resonance-observation.json).
- Pass an easier 2.0/s shake after a stiffer tower failed 1.4/s. No comparison record appears. Holding the same 0.30 g / 1.40/s setting on the less stiff tower does record the valid comparison (easy-shake-cheat.json, same-shake.json).
- Meter shortcuts: empty rig says NO FRAME; bare deck says LOOSE; all five vehicle masses match the chosen loads; numeric worst use remains 141.6% above the needle scale. Changing display magnification never enters the actual-sway calculation. The budget shortcut was repeated on the final dialog implementation and still produced no county record.
- Capacity check: request member 61 on a 60-member tower. It is rejected and the count remains 60 (capacity-timing.json).
- Margin, On the edge, Shoestring, Brace it and Pier shortcut: the known working Warren crosses at 57.6% and $8,783 without any prior buckle or stream footing. It earns only the applicable semi, margin and county records; 10, 13, 16 and 17 remain absent (semi-proof.json). Rare brace/pier and shoestring observations were not each re-earned. Their physical gates remain unchanged except for the shared genuine-crossing guard. No claim is made that every possible observation path received a new positive test.

## Voice walk
- Real held clicks, 0.12 s presses and 2 s gaps, followed by enough quiet time for the speech queue to finish.
- Main path: bWelcome, bLoose, bBuild, once each and without cuts (voice-main-complete.json).
- Side path: Manual, logbook, brief, checkbox: updated bPromise heard once, without a cut (voice-side-fixed.json).
- Tower welcome and Yard welcome each heard once without cuts (voice-tower-complete.json, voice-yard-complete.json).
- The semi-crossing event started in its matching state, then Manual intentionally hushed it; the full-shake result played without a cut (semi-proof.json, shake-steady.json).
- voice/lines.json equals allLines(), 23 unique strings. The removed stamp line is absent. Existing browser speech fallback remains; no clips were recorded. Automation was muted, so this is the kit's spoken-event log, not an audio-quality review.
- Same-rig rapid taps and repeated Enter now preserve one complete welcome (same-rig-*.json). An intentionally fast Tower-to-Yard switch cuts Tower narration at scope change; settled-path reruns above confirm its full welcome. Early diagnostic after fields ran before drive.py wait; corrected proofs wait inside after and supersede those pre-completion reads.

## Feel check
The best moment remains a real load changing the force path. The gauge follows current forces while the member bends or fails.
The old reward badge distracted from that instrument; it is now a quiet evidence book. The compact console and phone gauge
placement were the two flattest visual points; the targeted layout repairs leave the structure clear.
Existing Beat Lab and Snowy Mail Route bundles were viewed without writing to their folders. comparison/ and contact-comparison-0.jpg
place the yard beside Beat Lab. Painted site detail and moving structural detail remain, with the new drafting/steel grammar.
This was an operator play/check pass, not a new human usability study or a repeated three-lens review.

## Engine changes wanted
No runtime kit change. Audit harness follow-up: scripts/audit_tool.py MODES_JS should include
.rig-selector > button[id^="m-"] alongside its header-only selectors, so it discovers the instrument rigs for
full per-mode control walks. Tower/Yard still have explicit audit states and manual input/size evidence here.
The shared script was not edited; handoff.md records the exact change.

## Audit
The single full audit finished within its 40-minute limit: fix-audit/audit.md, 352 mechanical leads and 82 inspected frames.
Motion off, input/Enter paths, repeated 2 s clicks and resize-mid-action checks had no runtime errors, no endless motion and no controls left disabled.
Every lead has an individual disposition in audit-dispositions.md (352 rows: 335 accepted, 17 resolved by the focused repairs).

- Canvas/readout hit-box intersections are intentional noninteractive overlays, not concealed text. Actual frames show the readouts above the canvas.
- Compact fader labels share the 44 px input hit area while their text sits above the track. The zero-font Wind speed text is a redundant visual abbreviation; the Wind control, units and accessible label remain.
- Closed Promises details retain phantom descendant rectangles in the audit. Their contents are not painted or active; opening the brief shows all six choices clearly.
- Modal underlay/hint coverage is intentional; each native dialog provides its own heading and Close/Done action.
- Eight first-action welcome leads are accepted: Go/Worst use their own action lines, non-pickup trucks invalidate the pickup-specific welcome, and New/Manual use modal context. Selected-truck hints and Read remain correct.
- FIXED: three 0.7 s same-rig retaps cut their welcome. Repeat selection now offers an unheard welcome without calling setMode/hush. same-rig-bridge/tower/yard.json each shows one spoken line and no cut; same-rig-enter.json and same-rig-four.json close the same cause through two more input patterns.
- FIXED: the persistent budget overlay covered phone utility controls. A native adjustment dialog now closes with Done while the chosen limit remains on the switch. budget-final/ and budget-final-*.json prove clear main controls at every supported size, including both phone rigs. budget-modal-keyboard.json confirms R cannot rebuild behind the dialog but works after it closes.
- FIXED: the phone loose-frame readout covered the empty resonance heading. The chart now starts below the readout. Before: fix-audit/state-tower-with-work-375x812.png. After: post-audit/phone-loose-chart-after.png, plus the empty and valid Tower frames at the same 375x812 size.

The broad audit was run exactly once. Its preserved report precedes these contained audit-lead repairs; only their focused proof batches followed, not another broad audit or lens round. The final source/bundle manifest records the resulting revision. The audit state's new closed-budget case mirrors the focused proof for the next reader.
The automatic mode detector is header-only, so its per-control walk starts from Bridge. Explicit Tower/Yard states, held mode-entry tests and the 24-frame size sweep cover those rigs here; the exact harness follow-up is in handoff.md.
Final bundle: 928,090 bytes, one offline file. No tool network requests or console errors were observed. All task debugging/host ports were closed (closed-ports.json).

## Left open / Not done
- Actual school Chromebook hardware timing and independent calibration of the pre-existing nonlinear cable/ground-contact model.
- Existing exact spec-reference disagreements were preserved rather than fitted: Pratt 4 m/semi 101.6595% (fails), Warren/semi 57.5738%, narrow tank own rate 0.762856919/s. Current engine-numbers.json reproduces them.
- No new recordings or all-25-observations positive earning sweep. These are not claimed.
- Unattended choices: lower-left maker/Manual corner; budget as a nonblocking comparison dial; county brief independent of the dial; legacy dates retained without invented measurements. These follow the instrument brief.

## Evidence and command notes
All proof assets, plans, contact sheets and Chrome profiles are under _scratch/span-and-spire/. The final manifest is final-manifest.json.
The 24 mode/size sweep is summarized in size-summary.json. Every PNG from the proof batches and all 82 audit PNGs was inspected; contact-fix-audit-0.jpg through contact-fix-audit-20.jpg cover the complete audit set.
Validation commands used hard limits: 120 s bundle, 300 s drive batches, 2,400 s audit. Early Chrome connection resets on port 9910 were retried in smaller batches on an allowed port; successful proofs supersede those driver failures. No shared tool, script or engine was patched.
No host.html was created in the tool folder. Hosts and browser profiles stayed in Scratch, and owned processes were closed after their batches.
