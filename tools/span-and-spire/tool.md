# Span and Spire: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: span-and-spire

#### Built

Built the offline draft in `tools/span-and-spire/`: readable source, generated HTML, built-stage draft metadata,
teacher notes, 27 art prompts, 24 firm-captain voice lines, audit states and handoff. No git commit or polish round.
Scratch, frames, profiles, scripts and audit evidence are in `S:/CurioClass-codex-scratch/span-and-spire`.

Bridge has direct-stiffness live loads, pin/roller supports, tension-only cables, material swaps, undo/redo,
worst-use sweeps, buckling and snapping, nonlinear collapse, truck sliding/splash/recovery, promises and inspection tags.
Tower has six-mode dynamics, pluck, wind, steady shakes, pressure, resonance dots and an explicit failure engine.
Yard saves on this device, compares and tests designs, opens copies, borrows ghost members and replays tests.
Game prices are explicit; Old farm bridge appears after the first save. Steady shakes remain easy to extend.
The final draft bundle is well under 2 MB. No network dependency, generated art or recorded voice was added.

#### Numbers check

Independent NumPy/SciPy checks: `reference_check.py`, `numbers.json`, `more-numbers.json`, `comparison.json`.
Browser bridge results agree with independently rounded Python results within 0.005 percentage points.
The product uses full stated member self-weight and the specified masses; it contains no fitted reference answers.

| Check | Spec reference | Computed result |
|---|---|---|
| Pratt 4 m, semi | 99.6%, passes | 101.66%, fails |
| Pratt 6 m, fire | 115.6% peak | 119.12% peak |
| Warren cost / grain / semi | $8,783 / 57.4 / 56.3% | $8,783 / 58.75 / 57.57% |
| Shoestring cost / semi | $8,364 / 56.0% | $8,364 / 57.10%, all promises possible |
| Crossed cables, semi | 99.6%, passes | 101.74%, fails; cables do take turns |
| 20 m narrow tank sway | 0.77/s | 0.76286/s, displayed 0.76/s |
| Narrow tank, 0.8 / 1.4 | fails / holds | fails near 1.88 s / holds 15 s at about 36.24% |
| Wide tank, 1.4 | fails near 2.1 s | fails near 2.07 s |
| Empty / bell top sway | 4.32 / 1.47/s | 3.57909 / 1.43343/s |

All listed bridge prices except the incompletely specified largest reference shape were reproduced. Pressure,
Euler limits, Bridge Formula and contrast calculations were recomputed. The full comparison table and unresolved
prestressed-cable calibration are in `handoff.md`. The spec was left unchanged.

#### Feel check

Best moment: the plucked sway line beside the student's own shake dots makes the next experiment obvious.
The fresh player found a shake near 2.03/s that broke its tank tower, then changed the top mass and survived the same shake.
The bridge changing from loose timber to moving cyan/amber force arrows was a close second.

Two flattest moments and repairs:
- Tower's hint initially intercepted drags from its starting joints. It moved into free side space; the fresh player verified the repair.
- Motion off initially skipped collapse integration, leaving an intact-looking failure. Physics now continues and still failed poses are shown.
  Builder checks also repaired tank pluck targeting, magnification, stale redraws and truck/deck occlusion.

Would I still play after ten minutes? Yes, because shape, material, axle spacing and top mass change the result in
different ways. The fresh checker independently chose another experiment at 10 minutes 22 seconds. That run needed
a mid-session repair, so it is a conditional result rather than a clean cold usability pass.

Compared `preaudit-frames/opening-splash.png` beside Beat Lab in `feel-comparison.png`; Snowy Mail Route was also bundled
in scratch, opened and inspected. Moving structural graphics are layered and physical. The overall scene is still
plainer than the painted bar tools because all 27 paintings remain labeled placeholders as instructed. No replacement
art was invented. Finished illustration quality is an explicit draft dependency, not a claimed pass.

#### Done when

1. PASS: bare deck failure begins about 0.17 s after Go; segment tilt triggers sliding, water contact triggers the splash,
   and recovery restores the deck and pickup. Fresh-play captures show the connected bridge at 76.5 s and the heavier-truck test at 99.5 s.
2. FAIL at the exact references: Pratt 4 m semi is 101.66%, so it fails; Pratt 6 m fire reaches 119.12%. See Numbers check.
3. FAIL at the exact percentages and crossed-cable semi result. Both Warren prices match; the shoestring passes the tests
   and all six promises. Cable slack and the Pratt cable mechanism were independently reproduced.
4. FAIL at the exact sway and peak figures. The resonance reversal, approximately two-second failures, full fifteen-second
   survival, pluck and per-run chart dots work. Plate/member mass discrepancies are preserved in handoff.
5. PASS for the named main controls: Go, all five trucks and all five materials stay visible without scrolling.
   All eight sizes were inspected; the phone repair retains 84 by 44 pixel Go and Rebuild targets.
6. PASS: a truck swap changed forces within the same evaluation while the run stayed live. Edits invalidate and re-solve
   immediately; shake input changes immediately and starts a new fifteen-second qualification window.
7. FAIL for the untested Chromebook requirement. On this Windows machine, 60 members / 40 joints collapsed at p95 about
   3.2 ms per frame. Member 61 was refused. This is local evidence, not a Chromebook performance claim.
8. FAIL for complete verification: paced held-click logs and source checks cover heard how-lines, scope and Read,
   but the full voice walk timed out. No Rebuild line precedes failure in observed logs. Modal first-tap welcome is suppressed.
9. PASS for observed tags and persistence: reload retained tags, Yard Test all filled the comparison table, and
   the shoestring earned Every promise. All 25 conditions were reviewed; not every rare tag was separately earned in play.
10. FAIL for a clean uninterrupted cold run: the fresh checker did choose to continue after 10:22 and explained resonance,
    but needed the Tower hint repair mid-session. Later builder checks verified the subsequent repairs.

#### Wave lessons

- FAIL for complete hint / voice verification: hints change immediately and Read uses current text; heard how-lines use
  kit state. Paced logs were examined, but the audit did not finish proving every event at a two-second tap pace.
- PASS in inspected states: no load focus grab, focus survives retained controls, hints have reserved space and labels
  remain readable. Closed-details descendants reported by the checker are not visible overlaps.
- PASS in inspected frames: eight sizes, all three modes, real 375-wide iframe, unclipped hints and 44-pixel targets.
  The phone failure-state Go / Rebuild regression was repaired and re-shot.
- PASS, no giveaways: a free structural builder has no hidden right-choice badge or answer meter.
- PASS, honest numbers: game prices, half-side loads, magnification and pressure are labeled; discrepancies are not fitted away.
- PASS, standards: students choose promises, compare evidence, borrow parts and re-test the model. No family engine is specified.
- PASS in observed Motion-off states: no idle drift, still failure poses, physics continues, no recovery tween.
  Both early and later calm recovery frames were opened; the placeholders remain legible at their allotted sizes.
- FAIL for the broad short-choice visibility rule: Bridge trucks and materials stay visible, but Tower top-mass choices
  need panel scrolling at 680x425. This remains open; it was not hidden by a clean audit claim.
- PASS: resized an active shake from 680 through a 350-wide stage and back; it continued to fifteen seconds without
  exceptions, losing state or locking the action.
- PASS, late welcome: the kit queue uses mode scope, validity and no welcomeAfter; held inputs were checked.
- PASS, unknown as unknown: unrun comparisons say not tested; a mechanism is identified as loose rather than assigned a fake force.
- PASS, one look / one meaning: pull has outward arrows; squeeze has double lines and inward arrows; slack is gray and wavy.
- PASS for inspected outcomes: untested promises remain circles / unknown, tested results use the actual structural
  outcome, Valley results stay distinct, and inspection tags use explicit model checks. See the numerical exceptions above.
- PASS, hint changes back: mode, tool, material and view changes set the hint at once; Read uses the current hint.
- PASS, no answer by copying: success comes from the structural model, not matching wording to an answer card.

#### Audit leads

audit not finished. The one full audit ran on Chrome 9971 / host 8775, hit its 1,800-second limit and was stopped.
It saved 79 PNGs but no audit.md. No second full audit was run.

Visible lead: phone Go and Rebuild squeezed below 44 pixels after failure. Fixed; focused checks measure both at 84 by 44.
Harness lead: Tower drag steps lacked the return required by the audit helper. Fixed; replay created four members / four
joints at 680, 1366 and phone sizes. Slider replay reached 0.60 g, 4.00/s and wind 70 at all three sizes.
Intentional overlaps: world chips lie on the canvas; Tags is a modal overlay; closed Promises children are not painted.
Focused rechecks have no console errors, missing targets, lost actions, clipping or unnamed controls. The full audit
voice / input results remain unavailable. `repair-states.json` preserves the focused evidence.

#### Frames looked at

Initial, numerical, focused, full Bridge/Tower/Yard size passes, grayscale, Motion off, keyboard, limits, live changes,
collapse, borrow, storage fallback and opening/recovery frames in scratch were inspected. The full size pass covered
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe on host 8775.
Only repair-related sizes/states were re-shot. The fresh agent inspected all 21 of its captures.
All 79 audit PNGs were viewed: eight defaults individually, the remaining landscape states in sixteen contact pages,
and ten phone states individually. All ten `repair-state-frames` PNGs were also viewed. Tower work / extremes were
replayed only at the three affected sizes; the fold phone target, modal welcome and calm recovery were checked separately.

#### Engine changes wanted

None in shared kit files. Structural engines live inside this tool. See handoff for the steady-shake extension point.

#### Left open

- Resolve the exact reference self-weight / mass discrepancies and calibrate nonlinear prestressed cable transitions.
- Complete the full voice / input audit and a clean final ten-minute check in a later authorized round.
- Benchmark on an actual school Chromebook; Windows timings do not satisfy that hardware gate.
- Resolve Tower top-mass choice visibility at the smallest landscape size.
- Painted art and recorded narration remain absent by instruction. Automated Chrome was muted, so audio quality was not heard.
- No polish round or commits were started. All owned Chrome instances and servers were closed; no host.html remains in the tool.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: span-and-spire

#### Played
Cold grade-8 play before builder notes: Go, fold/recovery, real build drag, Tower, save, Yard tests, old-bridge grain failure and Tags.
The live force paths, buckling and resonance reversal are strong. I would keep experimenting with shape and top mass.
Repaired checks include keyboard-only construction, a complete 15-second shake, pluck, cable slack and borrowing.

#### Findings fixed
- blocker, general, Tower explicit shake: stale modal forces and peaks survived cable slack.
  Rendering and scoring now use explicit forces/displacements; shake classification and slow simulation time follow that engine.
- blocker, general, Yard Borrow: matching endpoints silently discarded donor materials.
  Borrow now upgrades matching members as well as adding geometry; verified Timber to Big timber without duplicate members.
- should fix, general, wind tests: elapsed hold could survive a design edit. Edits restart the five-second window.
- should fix, general, live shake edits: restart qualification and clear the old explicit engine.
- should fix, general, small Tower: top-load choices hid below settings. Moved beside the primary controls.
- should fix, general, compact Promises: short choices hid in a scrolling panel.
  A native dialog presents the whole set; reasons appear inline for touch and keyboard users.
- should fix, general, Yard entry: no sample until saving contradicted the spec and left an empty ledger.
  Old farm bridge is available immediately; card thumbnails are larger; tower truck cells say not applicable.
- should fix, general, voice: cable slack never reached its teaching line; a fold falsely implied no triangles anywhere.
  Connected bSlack, corrected tFold, and tied crossing speech to the actual truck and design revision.
- should fix, general, voice pace: five gap events lost prompts at two-second input.
  Shortened the spoken event while retaining the full control instruction in the hint; recheck spoke all five.
- polish, general, Worst spots: the hint could stay on the previous instruction. It updates immediately and names the exit.
- should fix, general, graphics: every painted asset was a labeled placeholder. Added and inspected all 27.
  Redrew wrong cloud/dust subjects, inaccurate vehicle axles, extra tank legs and a landscape masquerading as soil texture.
  Corrected cutout spill and vehicle aspect ratios; retained the rich palette and all live structural drawing.
- should fix, general, borrowed ghosts: donor geometry could follow a mode change. Ghosts now stay with their mode.

#### Findings left
- verification open: the full automatic input, voice and resize audit did not finish within its required limit.
- polish, general, Yard: the ledger is still the quietest screen, especially with the full 13-card catalog.
- nit, general, simultaneous tag awards share the last transient stamp; every earned tag remains in the book.

#### Flattest moment left
Reading the comparison ledger after a lively collapse. First entry now offers a real old bridge to test and borrow;
the large catalog and numerical comparisons still ask for more reading than Bridge or Tower.

#### Graphics
27 assets generated individually with the built-in imagegen tool; 7 redrawn, all inspected after keying and at scene size.
No people, downloaded images or missing art tokens. Prompts/provenance: art/prompts.json; raw originals: art/raw/.
Art 545 KiB; actual UTF-8 bundle 893 KiB (914,434 bytes), under 2 MB.
Opened all 24 mode/size frames and every focused frame. Compared the finished scenes with Beat Lab and Snowy Mail Route.
The dusk valley, real trucks and noon test yard now support the structural action instead of covering it with placeholders.

#### Audit
Audit not finished. The single full run reached its 1,800-second limit and was terminated at 1,800.2 seconds.
It produced 82 inspected PNGs but no audit.md. Its owned Chrome and host server are closed. No second audit was run.
The full automatic input, voice and resize verdict remains unavailable; focused checks above do not replace it.

Focused voice counts, held inputs at two-second gaps:
| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Worst spots | how, 3 activations in 5 taps | 1 | 1 |
| Add a road beam | event, 5 taps | 5 | 5 |
Read/mode-switch logs matched the current hint; the old Read released immediately. Browser narration was muted.

#### Left open
Independent NumPy/SciPy checks confirm reference disagreements: Pratt 4 m/semi 101.6595%, Warren/semi 57.5738%,
narrow tank 0.762857/s, empty top 3.579094/s. Prices, Euler limits, hydrostatics, Bridge Formula and AA contrast recompute.
The spec was not changed and no physics was fitted to its examples. Exact reference acceptance needs that discrepancy resolved.
Actual Chromebook 60 fps and an independent human ten-minute usability check were not established here.
Not every rare inspection tag was independently earned; their conditions were inspected in source.
Recorded clips remain absent; no voice was recorded. Nonlinear prestressed-cable calibration remains a model limitation.
All evidence and the durable working report are in C:/Users/Cory/AppData/Local/Temp/curio-codex/span-and-spire.
No commits, branch changes, kit changes or deployment. One generated Python cache outside the tool was removed;
subsequent commands disabled bytecode output. No host.html remains; owned browsers and servers are closed.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (pivot to an instrument; Cory approved it and the look, 2026-11-04)
Counts: blockers 0, should fix 0, pivot items 7

### Pivot: span-and-spire becomes an instrument (owner's decision, Cory, 2026-11-04)

This is not a normal Refine list. Cory decided that Span and Spire becomes an **instrument**: read docs/VISION.md
("Instruments: the second shape") and docs/CURIOSITIES.md ("The look" and "Pivoting the super tools") first. An
instrument is shaped around a real thing, the student drives, and there is no score or finish line. Span and Spire's
real thing is an engineer's test yard. The structural model, the buckling, the force colours, the trucks, the wind
and the shake table are its strength and stay exactly as honest as they are. What changes is the frame around them.

Owner's decision overrides the spec: update the affected sections of `spec.md` (Goals, Screens and modes, Look,
Teacher note) to match what you build, and say so in `polish.md`. The no-new-features rule in CODEX-FIX.md does not
apply to the items below; it still applies to anything else.

#### Pivot items

1. **Free build is the front door.** On first open the student is in the yard with a span to cross and the truck
   tray in reach. No promise list, budget or tag target is on screen until the student opens it.
2. **The student picks the test.** Any truck, any wind, any shake, in any order, on any design. Nothing is locked
   behind an earlier result.
3. **Budget becomes a dial.** Costs still exist and still show on each member, but the budget limit is off by
   default; a `Budget` switch turns on a limit the student sets (or the county's $9,000). The game-price line goes.
4. **Tags become the yard logbook.** The 25 Tags stay as an optional logbook the student opens from the Manual or
   a logbook button: each entry is a real test the yard has recorded ("Semi crossed, worst beam 64%: margin kept"),
   stamped when it happens. No count badge in the header, no flying stamp, no "0 of 25" anywhere on the main screen.
   Promises (criteria and constraints) live in the logbook too, as a brief the student or teacher can pick up.
5. **The look of an engineer's test yard** (docs/CURIOSITIES.md "The look"): blueprint or drafting paper for the
   build surface, members glowing in stress colours with a readable legend, needle gauges for load, worst member and
   sway, monospace readouts with units. The painted landscape can stay behind the yard if it reads as the site, but
   the kit frame goes: no header pill row and no right-hand pill panel. Controls sit where a yard's would: a truck
   tray, a material rack, a test console.
6. **Family marks.** A small engraved maker's plate in a corner: "Curio Class Instruments · No. 01 · Span and Spire".
   A `Manual` drawer in the same corner as Pocket Universe's holds the how-to, the honesty notes and the logbook.
   Motion, Sound and Read stay, on the yard's own power panel.
7. **Keep BASELINE.** Keyboard building and testing, contrast, reduced motion, the Read voice, one offline file,
   school Chromebook speed, and every size the tool supports now (re-shoot each). The force model, its checks and
   the voice lines stay correct; reword any line that names a removed control.

#### Size of this round

This is a bigger change than a normal fix: the frame of the tool is redrawn around an unchanged engine. Take the
time a build would. If something cannot be done well in one pass, do the parts you can do well, leave the rest,
and list it under "Not done" in `polish.md` with what it would need. A half-made look is worse than the old one.

#### Settled calls

- Keep the Yard, Save, the Old farm bridge and Borrow: they are what a real yard does.
- Keep Bridge and Tower as two test rigs in the same yard, not two modes in a pill row.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: span-and-spire (Codex fix, round 1)

The current refine.md is an owner-approved instrument pivot: 0 blockers, 0 should-fix items, 7 pivot items.
Evidence root: _scratch/span-and-spire/. All listed PNGs were inspected, directly or in the named contact sheets.
The source, notes, voice inventory, audit states, handoff and owner-authorized spec sections were updated.
No refine file or shared engine was edited. No commits were made.

#### Blocker
None in the current list.

#### Should fix
None in the current list.

#### Pivot items
1. FIXED: Free build is the front door. No header, target badge, promise card or budget limit appears on entry. Before: before/before-bridge-1366.png and before/before-bridge-680.png. After: sizes-bridge/bridge-1366x768.png and size-repairs/bridge-680x425.png. front-door.json: budget false, promises hidden, badge elements 0, headers 0.
2. FIXED: All five trucks and every wind/shake/top-load choice are available independently. No progression gate was introduced. 24 final mode/size results in size-summary.json show 263 primary-target measurements without coverage, clipping or size failures. A steady wind and a full shake were run directly on a fixture with no earlier crossing: wind-steady.json and shake-steady.json.
3. FIXED: Budget starts off and opens a $3,000 to $30,000 dial, initially $9,000. Done closes its native adjustment dialog while retaining the limit on the switch. It compares costs without locking tests. The game-price line is gone; the Manual states the estimate caveat. A real member tap reads Timber, 4.00 m, $200, pull 450 kN, squeeze 312 kN (member-price.json, misc/member-cost-current.png). At cost $9,863, dial values $3,000/$9,000/$30,000 all leave the county brief failed and create no county record (budget-cheat.json, repeated after the dialog repair in budget-final-cheat.json).
4. FIXED: All 25 Tags are optional logbook observations with timestamps and real evidence, opened from Manual. Promises live there as an optional brief. No badge, flying stamp, stamp sound or tag narration remains. Before: before/before-tags-1366.png. After: focused/logbook-semi-proof.png and cheats-extra/voice-side-fixed.png. semi-proof.json records Semi crossed, worst member 57.6%, and a $8,783 margin record. Subsequent fresh tabs retained these records. Legacy date-only records explicitly disclose missing historical measurements. The book updates if a test finishes while it is open. All crossing observations now require a whole-crossing pass, including no lost member. Test all records the tested design rather than a different current rig.
5. FIXED: Blueprint drafting surface, stress colors/arrows, live needle gauges, monospace units and a bottom truck tray/material rack/test console replace the kit header and right panel. All 27 existing paintings and the structural drawings remain. Gauges show total mass, actual current use and unmagnified top sway; NO FRAME and LOOSE replace false zero readings. The 141.6% over-scale reading keeps its number while the needle stops (gauge-over.json). All five masses match (gauges-mass.json); 50 m/s wind reads 72.31% and 13.0 cm (wind-steady.json). After frames: sizes-bridge/, sizes-tower/, sizes-yard/, with size-repairs/ superseding only touched compact/phone frames. Contrast: 12.35:1 text/button, 8.50:1 muted/panel, 7.17:1 pink-button text, 10.05:1 dial labels.
6. FIXED: Engraved lower-left plate reads Curio Class Instruments ? No. 01 ? Span and Spire. Manual opens beside it and holds how-to, honesty notes, keyboard instructions and a first-position logbook button. Motion, Sound and Read remain on a yard power panel. Escape restores focus to Manual from both dialogs (manual-focus.json, logbook-focus.json). Phone telemetry is stacked to keep the top load clear: size-repairs/tower-375x812.png. Compact Manual clipping was reproduced and repaired at both 680x425 and 800x500; final measured targets are fully inside.
7. NOT FIXED in full (hardware check unavailable): Keyboard construction, testing, reduced motion, contrast, browser Read voice and offline operation were preserved and observed. Keyboard made an eight-member/eight-joint first triangle (keyboard.json); Motion-off Go still fails the bare deck without shortening the run (calm-fold.json). All 23 model function bodies are unchanged (engine-preserved.json). The 60-member fixture refused member 61, with Windows callback mean 1.05 ms, p95 2.10 ms, max 3.20 ms (capacity-timing.json). Actual school Chromebook performance remains unverified. The software checks passed, including the repaired quick-tap welcomes; no claim is made about unseen Chromebook hardware.

#### Polish accepted
None separately listed.

#### Settled calls
- Applied: Yard, Save, Old farm bridge, Open and Borrow remain. A real Borrow all adopted the sample's 21 members and cleared its ghost (borrow.json). Test all populated a saved tower's comparisons (misc/yard-test-all-current.png).
- Applied: Bridge and Tower are test rigs in the same yard console; there is no pill mode row.
- Applied: spec.md Screens and modes, Goals, Look and Teacher note now describe the approved instrument. Related obsolete stamp/voice wording was aligned. Open questions were left in place.

#### Cheats tried
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

#### Voice walk
- Real held clicks, 0.12 s presses and 2 s gaps, followed by enough quiet time for the speech queue to finish.
- Main path: bWelcome, bLoose, bBuild, once each and without cuts (voice-main-complete.json).
- Side path: Manual, logbook, brief, checkbox: updated bPromise heard once, without a cut (voice-side-fixed.json).
- Tower welcome and Yard welcome each heard once without cuts (voice-tower-complete.json, voice-yard-complete.json).
- The semi-crossing event started in its matching state, then Manual intentionally hushed it; the full-shake result played without a cut (semi-proof.json, shake-steady.json).
- voice/lines.json equals allLines(), 23 unique strings. The removed stamp line is absent. Existing browser speech fallback remains; no clips were recorded. Automation was muted, so this is the kit's spoken-event log, not an audio-quality review.
- Same-rig rapid taps and repeated Enter now preserve one complete welcome (same-rig-*.json). An intentionally fast Tower-to-Yard switch cuts Tower narration at scope change; settled-path reruns above confirm its full welcome. Early diagnostic after fields ran before drive.py wait; corrected proofs wait inside after and supersede those pre-completion reads.

#### Feel check
The best moment remains a real load changing the force path. The gauge follows current forces while the member bends or fails.
The old reward badge distracted from that instrument; it is now a quiet evidence book. The compact console and phone gauge
placement were the two flattest visual points; the targeted layout repairs leave the structure clear.
Existing Beat Lab and Snowy Mail Route bundles were viewed without writing to their folders. comparison/ and contact-comparison-0.jpg
place the yard beside Beat Lab. Painted site detail and moving structural detail remain, with the new drafting/steel grammar.
This was an operator play/check pass, not a new human usability study or a repeated three-lens review.

#### Engine changes wanted
No runtime kit change. Audit harness follow-up: scripts/audit_tool.py MODES_JS should include
.rig-selector > button[id^="m-"] alongside its header-only selectors, so it discovers the instrument rigs for
full per-mode control walks. Tower/Yard still have explicit audit states and manual input/size evidence here.
The shared script was not edited; handoff.md records the exact change.

#### Audit
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

#### Left open / Not done
- Actual school Chromebook hardware timing and independent calibration of the pre-existing nonlinear cable/ground-contact model.
- Existing exact spec-reference disagreements were preserved rather than fitted: Pratt 4 m/semi 101.6595% (fails), Warren/semi 57.5738%, narrow tank own rate 0.762856919/s. Current engine-numbers.json reproduces them.
- No new recordings or all-25-observations positive earning sweep. These are not claimed.
- Unattended choices: lower-left maker/Manual corner; budget as a nonblocking comparison dial; county brief independent of the dial; legacy dates retained without invented measurements. These follow the instrument brief.

#### Evidence and command notes
All proof assets, plans, contact sheets and Chrome profiles are under _scratch/span-and-spire/. The final manifest is final-manifest.json.
The 24 mode/size sweep is summarized in size-summary.json. Every PNG from the proof batches and all 82 audit PNGs was inspected; contact-fix-audit-0.jpg through contact-fix-audit-20.jpg cover the complete audit set.
Validation commands used hard limits: 120 s bundle, 300 s drive batches, 2,400 s audit. Early Chrome connection resets on port 9910 were retried in smaller batches on an allowed port; successful proofs supersede those driver failures. No shared tool, script or engine was patched.
No host.html was created in the tool folder. Hosts and browser profiles stayed in Scratch, and owned processes were closed after their batches.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Span and Spire: instrument pivot handoff
Fix round 1, 2026-11-05. This section supersedes the older frame and tag descriptions below.

#### Current instrument frame
Free build opens on a blueprint drafting surface with the painted site behind it. Bridge and Tower are two rigs
at a bottom test console, next to Yard. Truck tray, material rack and test settings remain always available.
Three live needle gauges show total mass, current worst-member use and actual top sway, with numeric units.
LOOSE and NO FRAME are explicit; needles saturate without capping numeric readings.

Manual sits beside the engraved lower-left maker's plate. Its first action opens the optional yard logbook,
which holds all 25 former Tags as timestamped test observations and the original Promises as an optional brief.
No progress badge, automatic stamp, tag sound or tag narration remains. Older date-only records retain their date
and explicitly say their measurements were not stored. New observations store actual evidence and design metadata.
The logbook refreshes in place if a test finishes while it is open. Native dialogs provide focus containment.

Budget starts off. Its native adjustment dialog sets a comparison limit. Done closes the dialog while the
limit stays enabled, shown on the power switch, without locking build operations or tests. This prevents the
phone adjustment controls from permanently covering Build/Save/Read. Repeated selection of the current rig
offers any unheard welcome without hushing the one in progress. The county brief
continues to use $9,000 regardless of the dial. This follows the instrument's student-driven scope. Material and
member costs remain, with the estimate caveat in Manual. Motion, Sound and Read remain on the power panel.

#### Engine and evidence
The 23 core geometry, direct-stiffness, cable, modal and explicit integration function bodies are unchanged.
Whole-crossing logbook observations now require a genuine sweep pass, including no lost member; this closes a
pre-existing observation loophole while preserving solver results. Saved-design Test all passes the tested design
to its observation recorder, so the logbook never describes a different currently open rig.
Source section order remains data, model, state/actions, drawing, Yard, input, and initialization. Gauges are
initialized before the first setMode. Utility controls use a contents wrapper, then a single row in compact Tower.

All evidence, bounded harnesses and reports for this round live in _scratch/span-and-spire/. The final status
and frame paths are in polish.md. Exact historical reference disagreements and actual Chromebook testing remain
as documented below; no solver numbers were fitted. No shared kit files, refine files or other tools were edited.

#### Engine changes wanted
No runtime kit change. Audit harness follow-up only: in scripts/audit_tool.py, MODES_JS currently queries only
header mode controls. Extend its selector with .rig-selector > button[id^="m-"] so the full per-mode control
walk recognizes the instrument's rig console. Explicit audit states and the manual size/control tests cover
Tower and Yard in this round, but the automatic per-control walk otherwise starts from Bridge only.
The shared audit script was not edited.

#### Historical review handoff
### Span and Spire: current review handoff
Cold review, 2026-10-30. No commit, deployment or voice recording. The original build handoff is preserved below
as historical evidence; its missing-art and layout statements have been superseded.

#### Current files and behavior
The readable source is src.html. The kit owns Motion, Sound, Read, narration queues and basic tones.
The direct-stiffness solver, modal solver and explicit collapse engine remain local to the tool.
All 27 paintings are now present in art/, with original PNGs in art/raw/ and provenance in art/prompts.json.
They were generated individually with the built-in imagegen tool and packed only through art.py --rekey.
Seven assets were redrawn for subject accuracy, axle counts, a tank without extra support legs and full soil texture.
Cutout edge spill was removed through the existing pipeline. No images contain people.

#### Review repairs
- Nonlinear cable shakes render and score the actual explicit forces and displacements, track peak sway,
  classify failure as a shake and use simulated time when the 600-step cap slows the model.
- Design edits reset wind qualification. Shake edits restart a full qualification window and clear prior explicit state.
- Borrow replaces a matching member's material, so borrowing stronger tower legs works. Ghosts stay with their mode.
- Top loads remain with Go and materials before scrolling settings. Primary shelves stay available while scrolling.
- Compact Promises opens all choices in a native dialog; reasons are inline for touch users. Focus returns without scrolling.
- Old farm bridge is always present, including first Yard entry. Card thumbnails are larger.
  Truck results in a tower column say not applicable.
- Cable mechanisms trigger bSlack. The tFold line no longer claims that every loose structure has no triangles.
  Worst spots updates its hint immediately. Crossing narration captures the actual truck and design revision.
  The road-gap event is short enough for repeated two-second input; its hint retains the full building instruction.
- Vehicle proportions use actual cutout dimensions. Turning hub marks no longer paint a second set of tires.

#### Verification and open reference questions
Evidence: C:/Users/Cory/AppData/Local/Temp/curio-codex/span-and-spire.
Independent NumPy/SciPy calculations confirm the full-member-weight and plate-mass disagreements in the historical
table below. Pratt 4 m / semi is 101.6595%, Warren / semi 57.5738%, and narrow tank sway 0.762857/s.
No solver values were fitted to the reference examples. Nonlinear cable slack was exercised live:
current forces matched the explicit engine exactly while the shake continued.
All 24 mode/size frames were inspected, including a real 375-wide iframe. The host favicon 404 is a harness
request, not a request made by the tool. Keyboard-only construction, Motion off, grayscale, a full 15 s shake,
material borrowing, a fresh wind window, member 61 refusal and minimum settings were checked.
Recorded narration remains absent and browser audio was muted; voice timing is assessed from the kit log.
The cold review audit reached its 1,800-second limit without producing audit.md. All 82 captured frames were inspected.
Its owned Chrome and host were closed. No second audit was run. See codex-review.md for the verification limits. Actual Chromebook performance and exact spec reference
numbers remain open. The local frame-time measurements are not a hardware certification.

#### Historical build handoff

### Span and Spire: build handoff

Build only, 2026-10-30. No commit, deployment, art generation, voice recording or polish round.

#### Files and structure

`src.html` is the readable source, adapted from the kit starter. The palette, responsive layout and controls come first.
The script contains material and truck data, kit voice lines, direct stiffness algebra, cable active-set iteration,
mass-normalized modal analysis, the explicit collapse integrator, session state, canvas rendering, Yard and input handlers.
The generated `span-and-spire.html` is the offline draft bundle, not an alternate source.

The kit owns Motion, Sound, Read, narration queuing and basic tones. Ambient engine and wind synthesis is gesture-gated
Web Audio, follows the kit Sound state, and makes no files or requests. `voice/lines.json` uses firm-captain / Alnilam.
No recordings were made. `art/prompts.json` lists the 27 specified assets; nothing was painted, downloaded or drawn as
replacement art. The bundler supplies labeled draft placeholders. Source, notes and JSON have no em dashes.

#### Settled choices

- Prices are game prices. The material shelf, cost display, tooltips and notes say so.
- Old farm bridge appears only after the first save. It cannot be renamed or deleted; Open makes an editable copy.
- Steady sine shakes only. No historical earthquake record was fetched or invented.
- `shakeInput.acceleration(t, settings)` is the extension point for a future verified record. Its companion
  `displacement(t, settings)` drives the true-size table drawing. Add a record only with provenance, units, time-step
  and integration checks; keep the existing two-second ramp and fifteen-second steady test distinct from that record.

#### Physics

All calculations use SI units. Each side gets half the axle loads and a 2.0 kN/m slab load. Each member gets its full
stated self-weight, split between its ends. Bridge supports are a pin and roller; extra terrain footings are pins.
Truck axles use lever-rule interpolation between road joints. Stiffness matrices, factorizations and loose modes are
cached by design object and active cable mask. The smallest stiffness eigenvalue is checked against 1e-9 of the largest.
Cables drop the most squeezed active member and re-add a stretched inactive member, bounded by twice the cable count.

Towers use six mass-normalized modes, 20 kg plates, the chosen top mass, 5% damping and 1 ms integration steps. Tower
cables include 100 kN installation pull and geometric stiffness. Slack switches to nonlinear central differences.
Collapse recomputes axial forces from lengths and directions, removes failed members, includes ground contact and
uses centered Rayleigh damping. The damping increment is solved with a cached factorization, avoiding numerical
explosion from a separate high-frequency damping restriction. At most 600 explicit steps run per frame; excess demand
shows slow motion. A failed bridge member is removed and the remaining structure is re-solved before a full collapse.
The slab contributes inertial mass in bridge collapse. The truck rides its road segment until a twenty-degree tilt,
then slides and falls; its axle mass detaches from the deck. Water contact triggers the splash before crane recovery.

Motion off keeps physical time and integration. The failed tower is shown as still poses rather than a motion loop.
Pluck input accounts for displayed magnification, so the top follows the pointer instead of moving twenty times
farther than it. The load body and highest joints are pluck targets. Shift with an arrow provides a keyboard pluck.

#### Editing and persistence

Drag from a joint to add a member. Shift drag moves a free joint, resolving the spec's two competing uses of a drag
from a joint. Tap a member to change its material. Keyboard arrows / Enter build; Delete erases; 1 to 5 choose material;
Space runs or stops; R rebuilds after failure. Undo and Redo retain fifty edits. Crossings never become joints by accident.

Changing a truck or design re-solves immediately. A saved design is a snapshot. Yard Open edits a copy; Borrow maps
joint coordinates and overlays selectable pink member ghosts. Save stores designs, promises, test results and resonance
dots. Tags and the first-save flag also persist in `curio-span-and-spire`; every storage access is guarded. Session
storage fallback is visible in the panel. No transfer code, upload, account or network service exists.
Mode changes pause and retain each mode's current test. Changing shake or wind settings during a shake starts a new
fifteen-second qualification window while motion responds immediately. Valley quake results are stored separately
from other shake speeds, so the comparison table never relabels a different shake as the Valley quake.

#### Numbers check and spec disagreements

Scratch evidence: `S:/CurioClass-codex-scratch/span-and-spire/reference_check.py`, `numbers.json`, `more-numbers.json`,
`comparison.json` and the `*-browser.json` files. Python uses NumPy / SciPy independently of the browser implementation.
No reference percentage is fitted into the product. Keep the spec unchanged until its reference calculations are resolved.

Full stated member self-weight produces these whole-crossing worst uses, in percent:

| Design | Game price | Pickup | Bus | Fire | Grain | Semi |
|---|---:|---:|---:|---:|---:|---:|
| Bare deck | 3,300 | loose | loose | loose | loose | loose |
| Pratt 2 m | 7,442 | 39.60 | 80.56 | 102.63 | 116.64 | 114.29 |
| Pratt 4 m | 8,297 | 32.46 | 67.46 | 85.37 | 97.09 | 101.66 |
| Pratt 5 m | 8,771 | 38.16 | 78.78 | 99.55 | 113.15 | 118.45 |
| Pratt 6 m | 9,263 | 46.04 | 94.39 | 119.12 | 135.30 | 141.61 |
| Old farm Howe 2 m | 7,442 | 35.64 | 74.05 | 93.45 | 105.76 | 109.05 |
| Pratt cable diagonals | 8,071 | 31.93 | loose | loose | loose | loose |
| Crossed cables | 8,976 | 32.54 | 67.54 | 85.45 | 97.17 | 101.74 |
| Warren 4 m | 8,783 | 20.23 | 40.71 | 51.74 | 58.75 | 57.57 |
| Warren shoestring | 8,364 | 19.75 | 40.23 | 51.26 | 58.27 | 57.10 |
| Pratt 2 m with pier | 9,992 | 22.99 | 44.71 | 58.16 | 64.94 | 66.53 |
| Pratt 6 m with braces | 10,224 | 13.97 | 27.63 | 34.98 | 39.66 | 38.87 |
| Pratt 6 m, big end posts | 10,273 | 14.06 | 27.72 | 35.07 | 39.74 | 38.96 |

The browser agrees with the independently rounded Python bridge values within 0.005 percentage points. In particular,
the spec's Pratt 4 m semi 99.6% pass and crossed-cable semi pass are not reproduced: both slightly exceed 100% using
the stated loads. Warren and shoestring still pass comfortably, and shoestring keeps all six promises. The cable bus
mechanism begins at front 5.15 m rather than 4.7 m. A 55-member, 24-joint, twelve-panel crossed-cable interpretation
costs $16,295 and reaches semi 55.05%; the source's $14,656 shape does not fully specify its cable assignments.

Tank tower, 20 m: 2 m timber sway 0.76286/s; shake 0.30 g at 0.8 reaches about 426% and first fails near 1.88 s;
1.4 holds at about 36.24%. Width 4 m: 1.42140/s; 1.4 fails near 2.07 s. Steel: 1.35554/s and fails near 2.49 s.
Empty top gives 3.57909/s, not the spec's 4.32; bell gives 1.43343/s, not 1.47. These use the specified joint plate
and full member masses. The qualitative stiffness / resonance and lighter-top discoveries remain reproducible.

Wind checks reproduce the supplied main comparisons: narrow tank tower wind 50 at 72.31%, wind 70 at 132.35%; the
30 m stepped spire wind 70 at 97.81%. The 26 m 4-then-2 m town tower reaches wind 61.04% and Valley quake 51.28%.
The guyed tower is 1.89996/s; it survives 0.8 and fails 1.4 after the cable/slack explicit transition. Its exact peak
and failure time differ from the reference. The nonlinear cable transition deserves further independent calibration.

Tap pressure recomputes as 127.53, 225.63, 284.49 and 323.73 kPa at heights 10, 20, 26 and 30 m. Bridge Formula
results are about 52,732 and 85,525 lb before the semi's 80,000 lb cap. Euler timber squeeze limits are 312.28,
156.14 and 78.07 kN at 4 m, square root of 32 m, and 8 m. Contrast ratios reproduce the spec: ink/panel 14.29,
muted/panel 7.69, pink button text 7.17, pull/paper 9.15, squeeze/paper 9.31 and focus/paper 7.07.

#### Play and graphics checks

A fresh agent played for 10 minutes 22 seconds through real held clicks, whole-pixel drags and keys, with no fixtures
or builder hooks. It chose another tower experiment at the end and explained resonance using its own runs. The
original hint blocked Tower's starting joints; that was repaired mid-session and verified by the fresh player.
Later builder checks verified the Motion-off collapse, tank pluck target and redraw invalidation repairs.

Graphics use lit material layers, wood grain / steel highlights, gusset bolts, force arrows, double squeeze lines,
slack waves, bowing failure, nonlinear falling geometry, creek ripples, recovery hook and inspection stamps. The
painted places, trucks and props remain labeled placeholders. Their finish is not equivalent to the painted bar
tools; art and recorded voice remain explicit draft dependencies, not a reason to make replacement art in this run.

All STANDARDS sizes were shot once in every mode, including the real 375-wide iframe on host 8775. Only sizes touched
by a repair were re-shot. Scratch contains frames, test plans, browser profiles, logs and the side-by-side bar frame.
The single full audit stopped at its 30-minute limit. It saved 79 frames but never produced `audit.md`.
All 79 frames were inspected. A focused repair check then verified the phone Go / Rebuild targets, actual Tower
drags, slider endpoints, modal welcome suppression and still recovery poses. It saved ten additional frames.
The overlap checker includes intentional canvas overlays and descendants of closed Promises details; those are
not visible collisions. The complete voice / input audit remains unfinished. See the final `codex-report.md`.

#### Engine changes wanted

None in the kit. Both structural engines live inside this tool as specified. Do not patch shared kit files to resolve
the reference-number discrepancies.

#### Still to verify or resolve

- Resolve the reference self-weight / mass calculations before accepting Done when 2 to 4 at their exact figures.
- Independently calibrate nonlinear prestressed cable transitions and large-motion ground contact.
- Benchmark on an actual school Chromebook. Windows frame timing is useful evidence, not that hardware test.
- Painted art and recorded narration remain absent by instruction. Review their integration in the later authorized phase.
- The fresh play check was an agent play check, not a human usability study. Sound was muted in browser automation.
- Complete the interrupted voice / input audit and a clean final ten-minute play check in the later authorized round.
- At 680x425, Tower's top-mass choices require scrolling the control panel. The main action and material row stay visible,
  but the broader short-choice visibility rule is not fully met. Resolve without reducing the scene to a thumbnail.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: refine.md folded in (last changed 2026-11-05)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
