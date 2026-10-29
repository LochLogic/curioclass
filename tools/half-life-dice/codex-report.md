# Codex report: half-life-dice

## Built
src.html: three labs, seeded dice, actual-size Plane plots, nuclear equations and carbon dating.
tool.draft.json: beta metadata, Grade 10, students, 25-40 minutes, updated 2026-10-29.
notes.md: pairs start, three modes, discussion, sources, dating limits and device-only privacy.
voice/lines.json: curious-librarian, Aoede, five spec lines plus twelve Read hints; no recordings.
audit-states.json: eleven student states, real clicks, keys and drag, with keep regions.
handoff.md: architecture, numerical rounding, narration inventory and local engine workarounds.
codex-report.md: this report, maintained during the build.
Generated bundle: about 103 KB, below 2 MB. No git commands, engine edits, external images or network access.
Evidence below is under S:/CurioClass-codex-scratch/half-life-dice/.

## Numbers check
Node numbers.cjs recomputed every requested number before implementation.
Spec / Node half-lives: 1.000/1; 2.409/2.409421; 3.802/3.801784; 5.191/5.190893; 6.579/6.578813; 7.966/7.966167; 13.513/13.513407 rolls.
Spec / Node expected at 10: 1.0/0.976563; 56.3/56.313515; 161.5/161.505583; 263.1/263.075576; 348.7/348.678440; 418.9/418.903888; 598.7/598.736939.
Spec / Node ages: 1906/1905.656693; 3349/3348.796481; 0/0; 5730/5730; 11460/11460; 22920/22920; 53916/53915.810064 years.
340 counts: sqrt = 18.439089. Exact range 11023.412792 to 11920.936689 years; spec 11020 to 11920 rounds to tens.
Methane: 9.230419 eV. Fission/methane: 21668472, about 22 million. Fusion/fission values retain the supplied spec's 17.6 and about 200 MeV.
No numerical disagreement; 5,730 remains the dating half-life, and the owner's NNDC question stays open.

## Done when
1. PASS: validation.json, d6 expected 161.5056; twenty-run mean 164.45 at 10, maximum deviation 5.5944 over all rolls.
2. PASS: all seven exact half-lives above; real-half.json accepts an observed 4.0 reading; keyboard-roll.json accepts 3.5.
3. PASS: tracked.json keeps 1 in 6 at every age; final-state.json covers decay, a new live die and the restored hint.
4. PASS: validation.json, all seven correct products accepted, mass-only and charge-only errors rejected; compact-right-* and extreme-* viewed.
5. PASS: compact-right-* and ladder-final-680 show all four labeled rungs and 22 million ratio, including the smallest landscape view.
6. PASS: validation.json gives 1906, 3349, 22920 and 53916 with too-old flag. Noise uses sqrt(count); core-flag-final-680 retains its warning with noise.
7. PASS: identical seed reproduces faces, live mask and points. reload.json retains 7 cards and 7 samples; clear.json resets both. Calm timing measured below.
8. PASS: final/ covers all desktop sizes, host-final/ covers 375x812 in an iframe; keyboard paths pass, requests are zero and tool console is clean. Outer host favicon warning is recorded below.

## Self-check (section 6)
PASS: hint names the next control; voice-read.json records Read speaking exactly the current hint.
PASS: mode handlers set hints synchronously before queuing welcomes; voice-read and keyboard paths verify the visible state.
PASS: Track instruction uses V.heard; welcomes use Curio.voice's once-only keys; no welcomeAfter or custom speech queue.
PASS: controls update immediately; no action awaits narration, including a first Roll click.
PASS: voice entries use valid/needs. Calculate is actionable and explains the Estimate gate without revealing an age.
PASS: held 120 ms clicks at a 2 s pace, voice-track has one teaching line; voice-event starts all five tooOld events.
PASS: final-state.json verifies tracked decay, replacement and noise-off hints return to the matching state.
PASS: controls are created once, inputs retain focus, no load focus; keyboard-nucleus ends focused on Check.
PASS: no controls rebuild under the pointer; graph resize defers during dragging and redraws on drop.
PASS: fixed-height hint bar prevents hint-driven panel jumps.
PASS: critical labels reviewed at 680 and 375; four-rung and graph-bottom clipping were fixed and re-shot.
PASS: all seven dice, cards and samples stay visible, with no scroll panels.
PASS: full audit resized after every state input and active walk click, no exceptions or stuck controls.
PASS: phone-half.json and phone-ruler.json measure both rendered handles at 48x48 px; audit-targets reports no small targets. Buttons are at least 44 px.
PASS: steppers start at 10, 3, away from every answer. Check identifies failed sums; no sample-age marker appears before Estimate.
PASS: sweeping shows only the proposed values. A student must press Check to test conservation, or Estimate then Calculate to compare an age; no hidden answer or score is exposed while dragging.
PASS: observed solid circles, expected long dashes, mean dotted diamonds; live faces, gray x marks and tracked ring remain distinct in grayscale.
PASS: tracked cards distinguish live and decayed nuclei; final-state.json checks both wordings.
PASS: on-screen model labels give dice-as-nuclei, 5,730 years, 13.6 dpm/g and 100 modeled minutes compressed to 1 second.
PASS: HS-PS1-8 actions are rolling/marking decay, balancing all nuclear products, and selecting/checking decay, fission and fusion to compare their energy rungs.
PASS: Plane owns axes, curves, points, segments, keyboard handles, dashes and formatting. SVG dimensions follow actual box sizes; no animated g.view is needed.
PASS: no infinite animations. timing.json measured calm roll 418.6 ms, mean 2193.9 ms and counter 1060.3 ms, including rendering/scheduling overhead.
PASS: the same 400 ms, twenty 100 ms waits and 1000 ms count timer run with either Motion setting.
PASS: keyboard-only roll, half-life, balanced card and dated sample, inputs/keyboard-*.png and JSON.
PASS: validation.json resource requests = []; no tool console errors in the driven sweeps.
PASS: accent contrast computed as 8.24:1 on panel, 7.81:1 on section background, 8.79:1 for brand ink on accent.
PASS: progress persistence and Clear verified; visible totals and Saved on this device only appear with Clear.

## Audit leads
Full audit: audit/audit.md, 36 leads; audit-final rechecked all sizes and changed states without repeating the unchanged full control walk.
A01 FIXED: 680 Roll tab 38 px wide, explicit minimum width 44 px.
A02 FIXED: 800 Roll tab 38 px wide, same fix.
A03 FIXED: 1000 Roll tab 38 px wide, same fix.
A04 FIXED: 375 Roll tab 40 px wide, same fix plus full-width phone mode row.
A05 FIXED: Dating hint named disabled Calculate; enabled validation button now explains the Estimate gate.
A06 FIXED: mode Dating, Roll tab outside phone edge, phone header now has its own mode row.
A07 FIXED: mode Dating, Nucleus tab outside phone edge, same fix.
A08 INTENTIONAL: expected curve crosses the marker's transparent hit region; the visible handle remains clear and marks a mathematical crossing.
A09 FIXED: dated state, phone Roll tab outside edge, header fix.
A10 FIXED: dated state, phone Nucleus tab outside edge, header fix.
A11 FIXED: too-old state, phone Roll tab outside edge, header fix.
A12 FIXED: too-old state, phone Nucleus tab outside edge, header fix.
A13 FIXED: noise state, phone Roll tab outside edge, header fix.
A14 FIXED: noise state, phone Nucleus tab outside edge, header fix.
A15 EXPECTED: m-roll welcome unheard with Sound off by default; Sound on queues the unheard welcome.
A16 EXPECTED: m-nucleus welcome unheard with Sound off; spoken on sound-enabled entry, voice-read.json.
A17 EXPECTED: m-dating welcome unheard with Sound off; spoken in voice-event.json.
A18 EXPECTED: Motion first tap remains silent while Sound is off.
A19 EXPECTED: Coin first tap remains silent while Sound is off.
A20 EXPECTED: d4 first tap remains silent while Sound is off.
A21 EXPECTED: d6 first tap remains silent while Sound is off.
A22 EXPECTED: d8 first tap remains silent while Sound is off.
A23 EXPECTED: d10 first tap remains silent while Sound is off.
A24 EXPECTED: d12 first tap remains silent while Sound is off.
A25 EXPECTED: d20 first tap remains silent while Sound is off.
A26 EXPECTED: New seed first tap remains silent while Sound is off.
A27 EXPECTED: Roll once first tap remains silent while Sound is off; actions never wait for a welcome.
A28 EXPECTED: Roll to 10 first tap remains silent while Sound is off.
A29 EXPECTED: Reset first tap remains silent while Sound is off.
A30 EXPECTED: Show expected first tap remains silent while Sound is off.
A31 EXPECTED: Average first tap remains silent while Sound is off.
A32 EXPECTED: Track one first tap remains silent while Sound is off; sound-enabled five-tap test speaks its teaching line once.
A33 EXPECTED: Mark first tap remains silent while Sound is off.
A34 EXPECTED: Clear in Nucleus changes nothing when saved progress is already empty; 7-to-0 reset separately verified.
A35 EXPECTED: Clear in Dating changes nothing when saved progress is already empty; same reset evidence.
A36 EXPECTED: clicking the ruler handle without dragging changes nothing; real-ruler.json and keyboard-date.json verify dragging and arrows.
F01 INTENTIONAL: audit-final flags curve crossing the marker's transparent hit region at four sizes, same as A08.
F02 FIXED: phone half-life target was 41 px; geometry observers and 48 px hit area yield 48x48 rendered pixels, phone-half.json.
F03 FIXED: phone age target was 41 px; same fix yields 48x48 rendered pixels, phone-ruler.json.
T01 INTENTIONAL: compact Dating age handle overlaps the 13.6 label only in its transparent hit rectangle; visible glyphs are separate, native frame reviewed.
T02 INTENTIONAL: compact Dating handle is reported under its transparent rectangle; this is its own hit area, no visible occlusion.
T03 INTENTIONAL: compact Dating 6.8 label is reported under that transparent rectangle; text remains legible and pointer input works.
T04 INTENTIONAL: expected curve crosses the half-life transparent hit region at every size, same mathematical crossing as A08.
T05 INTENTIONAL: compact core-noise age hit rectangle touches 13.6; visible glyphs are separate, native frame reviewed.
T06 INTENTIONAL: compact core-noise handle is reported under its transparent rectangle; no visible occlusion.
T07 INTENTIONAL: compact core-noise 6.8 label is under transparent hit geometry only; legible, pointer input verified.
All three audits completed with clean resize stress, no stuck controls, focus loss, infinite animations or tool console errors.
The outer drive.py host emitted favicon.ico 404, and two connection-reset traces on browser shutdown. The tool itself requested no resources and produced no console errors.

## Frames looked at
Viewed every first/ PNG through contact sheets, plus the three 680 originals; initial clipping was fixed.
Viewed every final/ PNG: all three modes at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900.
Viewed fixed/ and last/: 375x812 iframe modes, F1, core noise, four-rung ladder and compact graph.
Viewed every extremes/ PNG: all seven cards at A 240 with Z 94 and -1, all seven correct cards, Coin/d20 at 10, mean and grayscale.
Viewed validation/ reload, Clear and numerical result frames.
Viewed all ten inputs/ frames: keyboard paths, real drags, voice, calm roll and calm mean.
Viewed all 102 audit/ PNGs in seventeen contact sheets; reviewed small previews at full size elsewhere.
Viewed all nine compact/ PNGs, including every checked card at 680, tracking and calm noise.
Viewed all 57 audit-final/ and 29 audit-targets/ PNGs in contact sheets; inspected compact Dating/core and phone marker originals.
Viewed end/ (3), host-final/ (7), shipping/ (4) and fission-final/ (1): lifecycle, gate, phone drags, core noise, exact 340 counts and compact F1.
Final F1 frame shows all three emitted neutrons; model has 236 nucleons before and 236 after, 472 circles total.

## Engine changes wanted
None. Local handle-focus wrappers use preventScroll; geometry observers rebuild the actual-size Plane and defer redraw during a drag.

## Chromes and servers
Muted Chrome profiles used ports 9980, 9981 and 9982; all profiles, captures and temporary scripts are in scratch.
All drivers and audits finished and closed their launched Chrome process trees. Exact drive.py host parent 648 and verified child server 19672 were stopped; host.html was removed.
ports-final.json confirms 8796 and every port 9980 through 9987 inactive. All audit servers are stopped.
PowerShell Get-CimInstance was denied. A native read-only query found no readable owned match, but all 11 remaining Chrome command lines were inaccessible; a complete machine census cannot be certified.
No test output was written into the tool folder, aside from the required generated bundle.

## Left open
No functional or visual checks remain open. Full machine Chrome command-line verification is permission-limited as described above.
The owner's 5,730 versus 5,700 question remains unchanged. No narration was recorded, as requested.
Source values were checked against the supplied spec and recomputed locally; source pages were not re-fetched.
