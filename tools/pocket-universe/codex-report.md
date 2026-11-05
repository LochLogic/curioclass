# Codex report: pocket-universe
## Built
Build only, in S:/CurioClass-codex-pocket-universe/tools/pocket-universe/.
No commits, branch changes, shared-kit changes, art generation, recordings or polish round.
The self-contained draft is 152598 bytes; readable source has 2840 lines, none over 160 characters.
Pocket and Real Solar System, 24 discovery stickers, seven loads including Empty/Starter, live prediction,
150-second tape, branching ghosts, Undo, local saves/replay, keyboard input and synthesized sound are implemented.
The 27 art tokens are laid out and preloaded. Paintings and recordings remain absent, as instructed.
The owned Chrome ports were 9990-9994; the only host port was 8795. All owned browsers and servers were closed.

## Numbers check
Evidence: S:/CurioClass-codex-scratch/pocket-universe/numbers.json and numeric-results.json.
Independent Python constants/periods/radii/contrast checks plus 38 passing model assertions.
All 24 goal detectors were reached using real integrations; successful search starts are frozen in the results.
Starter: separation 250.000000-250.009801 px over 30 s; period 7.815004 s.
Rescue: original crash 15.747917 s; five Slower taps earns Rescue within 15 s; five Faster taps crashes at 2.933333 s.
Mars's first direction reversal is at world time 2.733333 s, in May 2001; five Venus passes occur by 2007.
Neptune's two-body period is 327.625983 world seconds, about 20.48 s at a fully achieved x16.
Earth's true diameter is 0.00852686 world px at 100 px/AU; its on-screen label also accounts for zoom.
Jupiter/Sun mass ratio is 1/1047.68177; Giant/Planet Hill radii at 300 px are 96.54894/44.81405 px.
38 assertions include momentum conservation, deterministic replay, gravity off, moons, ring, binary, Trojan,
capture, slingshot, Grand tour, black-hole equivalence, Figure eight, moving-frame prediction and star mass limits.
Contrast: brand/panel 8.93:1; brand/section 8.23:1; brand ink/brand 9.25:1; text/panel 16.29:1; muted/panel 7.90:1.
Source discrepancy: the finite Planet mass gives circle speed 200.9975 and escape 284.2534 px/s at 250 px.
The lone-star test-particle circle is 200.0, rather than the source's 200.3. Some example numbers mix conventions.
Halving the Starter star alone leaves its planet slightly bound. One Faster nudge before halving releases it.
The Lightweight finding was corrected to that fact; spec.md was left unchanged.
Whirl dust already beyond 4000 px is dropped. At Gravity 0.45, every remaining mote is beyond 1500 px by 20 s.
The source agent's retrospective random-trial counts and every quoted error estimate were not reproduced exactly.

## Feel check
Yes, I would keep experimenting after ten minutes: a small nudge can rescue a moon or change a shared orbit.
The required fresh-agent proxy actually played for 10m10s, still wanted to play and earned eight discoveries.
Its best moment was making a binary from Empty, naming it Twin Fireflies, saving and replaying it.
It could explain how sideways speed and gravity combine to bend a path. This was not a human student study.
The two flattest moments were an empty field after escapes and ten seconds of waiting before a replay's first throw.
Changed: off-screen recovery now names World > Fit and 0, and changes back after recovery; quiet replay intervals
show a countdown and name x4. The recorded waiting time is preserved rather than silently changing the replay.
Other build fixes: flush the last quick drag prediction, draw ghosts/trails in the Follow frame, expose all nine
body buttons in the preview, show all seven Wonders, and keep hints visible when the panel scrolls.
Comparison: Scratch/feel-comparison.png places the nudged dance beside Beat Lab. Trails, motion and feedback have
visual depth; the missing painted sky and disks remain visibly plainer than finished art. No finished-art parity claim.
Sound was muted in every test, as required, so audible quality was not judged by ear.

## Done when
1. PASS: Starter already moves; real held drags hold time, show a live ghost and launch on release. Final aim frame
   shows the 300 px/s escape prediction after the last quick movement, rather than the earlier at-rest crash path.
2. PASS: drag 40 crashes at 1.533 s; drag 100 orbits; drag 150 passes 1500 px and gets an edge arrow.
   Snapshot/restore plus the same step sequence reproduces body data exactly.
3. PASS: Rescue, five Slower taps and the faster-crash contrast match the numerical checks above.
4. PASS: every detector 1-24 reached; representative UI discoveries contain actual 160x100 trail snapshots.
5. PASS: J2000 start, May 2001 Mars reversal, five Venus passes/flower by late 2007, true radii and real periods.
   Wall-clock periods lengthen whenever the tool explicitly reports a reduced achieved speed.
6. PASS: scene dominates laptop and preview; tray/time bar are visible at every required size, including the 375 host.
   Scene labels are at least 10 px. Advanced portrait panels scroll below them, as the specified stack requires.
7. PASS: held drag, Pause/speed, mass/speed/turn, Gravity and scrub act immediately. Aiming keeps world time at zero.
   Gravity off also removes pull arrows. Source controls clamp mass to the current kind's tray limits.
8. PASS via the specified fallback/actual-speed alternative: 240 dust did not sustain x4 under 4x CPU throttle,
   so dust is 160. Final 20-mass/160-mote run: mean 16.58 ms, p95 16.70 ms, achieved x1.8 displayed on requested x4.
   Prior runs ranged to x2.9. This is a 60 fps result, not a claim that requested x4 was achieved at full budget.
9. PASS: save/reload preserves stickers; replay body data matches the saved endpoint exactly; blocked storage still plays.
   Save limit, rename, replace/cancel, Delete and Clear confirmations are recorded in save-limit-results.json.
10. FAIL as a finished-art gate: all 27 labeled draft images load and contain no people, but paintings are not present.
    Required voice lines, two-second held taps, Read, Motion off, no external requests and no em dashes were checked.
    Narration uses browser fallback; recording was forbidden. This is the requested built draft, not an art-complete release.
11. PASS for the required fresh-agent proxy: 10m10s, still choosing experiments, eight discoveries and a stated concept.

## Wave lessons
PASS, Hint and voice: hints update synchronously; Read uses current context. V.heard and pending keys prevent nagging
or competing Follow lines. A first-tap mode action has no late welcome. The stale True size line drops correctly.
PASS, Focus/layout: no focus on load; buttons are not rebuilt under a pointer; book loads restore focus;
hint height is reserved and Flight notes are sticky. Compact body actions come before the longer readout.
PASS, Sizes: all eight STANDARDS sizes, both modes, required host, 44 px controls/body hit diameters and 10 px labels.
PASS, No giveaways: no quiz answer or progress shortcut; stickers depend on measured physical outcomes.
PASS, Honest numbers: Pocket honesty line, real units, scaled true-size caption, finite-mass correction and actual speed.
PASS, Standards: gravity/orbits/galaxies, scale, forces and mass/distance changes are student actions; no family engine.
PASS, Motion off: decorative pulse, twinkle, ring growth, sparks and chip glow stop; content motion and timing continue.
PASS, Short choices: all nine selected-body actions fit the 680 preview; all seven Wonders are visible.
The phone tray is the spec's explicit horizontally scrolling exception.
PASS, Resize mid-animation: the smaller audit found no exceptions or controls left disabled after resize.
PASS, Deferred welcome: welcomeAfter false follows the higher-priority multi-mode standing rule.
PASS, Unknown as unknown: no hidden puzzle clues; missing paintings are labeled placeholders.
PASS, One look/one meaning: solid trails, dashed prediction and dotted discarded future remain distinct, including grayscale.
PASS, Truthful badge: body/parent/lap data, true-size state, Pause/Play and measured running speed match state.
PASS, Hint changes back: True size off, Fit recovery, finished replay and capacity changes return to fitting instructions.
PASS, No copying words: there are no word-matching answers; the science is the mechanic.

## Audit leads
The first audit timed out on mouseReleased inside its control walk after the driver's internal 60 s limit.
The command's outer limit was 30 minutes. Its frames survived, but it did not write audit.md.
The brief permits one smaller retry: --no-walk completed. Full control-walk/repeat coverage remains uncompleted.
Report: Scratch/audit-retry/audit.md. Every one of its 333 rows has a disposition in audit-lead-ledger.json.
9 small targets: FIXED with 44 px minimum widths; targeted measurements confirm Read/Clear/Close are 44 px.
6 apparent closed-section overlaps: FIXED by explicitly hiding closed disclosure content; Gravity height is zero.
1 scrolled-out hint: FIXED with sticky Flight notes; saved-book 680 frame measures hint within the viewport.
190 canvas overlaps: intentional canvas application surface under its scene labels and the specified overlay tray.
97 below-fold advanced controls: specified portrait page stack; primary throw, tray and time controls stay in view.
26 hidden underlying scene texts: intentionally covered by an open book; its own contents and Close remain readable.
2 covered keep regions: portrait books intentionally cover time/tray until Close; physics continues behind them.
1 clipped phone choice row: the spec explicitly calls for a sideways scrolling tray; Wonders is fully visible.
1 dropped how line: student already enabled True size, exactly the spec's stale condition; it must not speak afterward.
Motion-off and resize sections were clean. Targeted fixes were re-shot; the full audit was not repeated again.
Independent held-input, keyboard, persistence and ten-minute play checks captured no tool console exceptions/warnings.

## Frames looked at
Scratch is S:/CurioClass-codex-scratch/pocket-universe/.
Both bar frames; quick-frames/*; Pocket/Real at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080,
760x900 and hosted 375x812 in full-frames/*; phone books/library; extreme-frames/* including grayscale and Motion off.
All 102 PNGs from the audit attempts were inspected on paired contact sheets, with representative native-size checks.
Final-layout-frames/*, buttons-first-frames/*, render-final-frames/*, keyboard-real-input.png,
final-aim-escape.png, final-aim-follow.png, final-replay-idle.png, final-true-size-off.png and feel-comparison.png.
The fresh agent inspected its representative student-run frames; its full evidence/report is in Scratch/playtest/.

## Engine changes wanted
No production kit or family changes. Audit tooling request: scripts/audit_tool.py, Audit.walk_mode/press,
log the current control, handle native confirmations explicitly and preserve partial results on CDP timeout.
A native-confirmation cause is plausible, not proven for the failed audit's unlogged control.

## Left open
Painted art, recorded narration and human-student/audio-by-ear validation. No generation or polish was authorized.
The complete audit control walk/repeat pass did not finish; the smaller audit and independent checks are not a substitute
for claiming it completed. The original source's exact random-trial rates/error estimates were not all reproduced.
Performance varies with hardware and encounter geometry; the full-budget benchmark kept all counts alive on outer orbits.
The initial location lookup finished in 0.14 s but used the tool's default wait rather than an explicit stop deadline.
All subsequent build/test subprocesses had explicit deadlines. host.html was removed and owned test processes closed.
