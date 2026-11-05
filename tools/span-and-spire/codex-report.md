# Codex report: span-and-spire

## Built

Built the offline draft in `tools/span-and-spire/`: readable source, generated HTML, built-stage draft metadata,
teacher notes, 27 art prompts, 24 firm-captain voice lines, audit states and handoff. No git commit or polish round.
Scratch, frames, profiles, scripts and audit evidence are in `S:/CurioClass-codex-scratch/span-and-spire`.

Bridge has direct-stiffness live loads, pin/roller supports, tension-only cables, material swaps, undo/redo,
worst-use sweeps, buckling and snapping, nonlinear collapse, truck sliding/splash/recovery, promises and inspection tags.
Tower has six-mode dynamics, pluck, wind, steady shakes, pressure, resonance dots and an explicit failure engine.
Yard saves on this device, compares and tests designs, opens copies, borrows ghost members and replays tests.
Game prices are explicit; Old farm bridge appears after the first save. Steady shakes remain easy to extend.
The final draft bundle is well under 2 MB. No network dependency, generated art or recorded voice was added.

## Numbers check

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

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

audit not finished. The one full audit ran on Chrome 9971 / host 8775, hit its 1,800-second limit and was stopped.
It saved 79 PNGs but no audit.md. No second full audit was run.

Visible lead: phone Go and Rebuild squeezed below 44 pixels after failure. Fixed; focused checks measure both at 84 by 44.
Harness lead: Tower drag steps lacked the return required by the audit helper. Fixed; replay created four members / four
joints at 680, 1366 and phone sizes. Slider replay reached 0.60 g, 4.00/s and wind 70 at all three sizes.
Intentional overlaps: world chips lie on the canvas; Tags is a modal overlay; closed Promises children are not painted.
Focused rechecks have no console errors, missing targets, lost actions, clipping or unnamed controls. The full audit
voice / input results remain unavailable. `repair-states.json` preserves the focused evidence.

## Frames looked at

Initial, numerical, focused, full Bridge/Tower/Yard size passes, grayscale, Motion off, keyboard, limits, live changes,
collapse, borrow, storage fallback and opening/recovery frames in scratch were inspected. The full size pass covered
680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a real 375x812 iframe on host 8775.
Only repair-related sizes/states were re-shot. The fresh agent inspected all 21 of its captures.
All 79 audit PNGs were viewed: eight defaults individually, the remaining landscape states in sixteen contact pages,
and ten phone states individually. All ten `repair-state-frames` PNGs were also viewed. Tower work / extremes were
replayed only at the three affected sizes; the fold phone target, modal welcome and calm recovery were checked separately.

## Engine changes wanted

None in shared kit files. Structural engines live inside this tool. See handoff for the steady-shake extension point.

## Left open

- Resolve the exact reference self-weight / mass discrepancies and calibrate nonlinear prestressed cable transitions.
- Complete the full voice / input audit and a clean final ten-minute check in a later authorized round.
- Benchmark on an actual school Chromebook; Windows timings do not satisfy that hardware gate.
- Resolve Tower top-mass choice visibility at the smallest landscape size.
- Painted art and recorded narration remain absent by instruction. Automated Chrome was muted, so audio quality was not heard.
- No polish round or commits were started. All owned Chrome instances and servers were closed; no host.html remains in the tool.
