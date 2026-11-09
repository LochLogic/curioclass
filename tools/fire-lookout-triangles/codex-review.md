# Codex review: fire-lookout-triangles

## Played
Cold, as a grade 12 student: Spot exploration, a full Smoke 1 dispatch, all three Radio calls, and Burn 1, with held clicks and Sound on, before reading codex-report.md, handoff.md, notes.md or src.html. The map and crew arrival are strong. Then checked the Teaching, Play and Craft lenses, projection sizes, keyboard-only dispatch, cheap paths and errors. One review pass; fixes received focused re-checks.

## Findings fixed
- **blocker, general, Dispatch checks:** 624 blind numerical trials, copying Spot answers, and restarting a worked example each earned an independent saved mark. Two rejected checks or exposed answers now keep that triangle guided for the page session, including restarts; it can finish but earns no mark. All three exact attacks now yield marks `[]`, with guided labels in the step and log.
- **blocker, general, Burn:** copying Show me received ordinary success; changing that answer to 999 square miles and 0 acres left success and its answer visible. Guided work now has distinct feedback/voice. Editing a checked answer clears its result, worked card and map answer immediately. Error hints update immediately and Read names Check area.
- **should fix, general, Radio:** count enumeration led to unqualified result feedback. A wrong count or two missed pins now labels the comparison guided; distinct intersections remain mandatory.
- **should fix, general, compact Radio:** the painting covered call text because compact section padding overrode its reserved space. Restored image padding and fitted the quote. Zero-spot confirmation now replaces the answered count row, keeping No spot visible and focused at 680x425.
- **should fix, general, map labels:** Cedar Creek overlapped C at small scales; phone Radio pin distances were clipped by the map frame. Moved these labels into clear side margins. North-facing sight aria readings now wrap to 0, matching 000 degrees on screen.
- **should fix, general, art:** colored cutout fringes, weakest on the radio. Redrew the radio with the built-in image tool; re-keyed all five cutouts with hole detection and spill removal using the required free pipeline.
- **polish, general, opening:** tighter preview readouts expose the full welcome painting and copy at 680x425.
- **polish, general, Radio payoff:** the old ending was a paragraph that supplied the lake answer. Its existing clue now also marks the farther pin and the southward lake connection on the map. Both mathematical solutions remain visible.
- **should fix, general, Read:** fixed hints were absent from the narration inventory, and Show me left its earlier error hint behind. All 44 narration/Read lines are now inventoried; Show me immediately names Check as the next action. The main voice walk and Read were re-run. Corrected voice token quoting for future recordings.
- **should fix, general, audit-confirmed craft:** raised covered B/F labels, separated phone AC/BT labels and the lake/handle, set Spot to at least 44 px, and made input names explicit. Expired sight handles now disappear immediately when the angle step opens. Reserved Sound width to prevent header shifts.
- **should fix, general, audit-states.json:** eight drag expressions omitted the required outer return, so named states were never reached. Corrected them; real-input replays now reach angles, guided readiness, crew arrival and both Radio pins.

## Findings left
- **should fix, spec-level scope:** G-SRT.D.9 requires deriving the area formula; D.10 includes proofs. The spec supplies applications. Notes disclose this; no new activity or shared curriculum mapping was invented. Owner must resolve the coverage claim.
- **polish:** the requested gravel-ranger timbre has no recording. Browser speech works; the build rules prohibit recording audio in this run.

## Break it
- **Sight gate:** swept keyboard bearings until each instrument locked; one sight alone does not open the angle form. The valid directions are still required, and bearings/lock status do not reveal the later distances.
- **Angles, AF, CF:** exact angle checks and separate distance checks remain. The 624-check sweep is guided with no mark. All four independent preset solutions still pass and earn their marks. Empty/nonfinite/arithmetic/trailing-garbage inputs fail parsing. Smoke 1 AF 18.0 fails; 18.2 mi passes; CF 25.69 passes.
- **Show me and marks:** copied work can reach the crew as guided practice. No mark is awarded, including after restarting and re-entering the copied answers. Copying the exact visible Spot triangle also stays guided. An independent path still earns Smoke 1's mark only at arrival. Keyboard-only arrival also earns its mark and moves focus to Smoke 2.
- **Radio:** tried 0, 1 and 2 in turn; count-only never finishes. A repeated pin leaves exactly one location and cannot satisfy the two-location case. Wrong locations fail. Count guessing plus the true pins is labeled guided. Calls 2 and 3 finish only at their tangent point and No spot confirmation respectively.
- **Burn:** both units are required: correct square miles with zero acres fails. Burn 2 rejects 0.41 and accepts 1.41/902; Burn 3 accepts 0.32/205. Show me and repeated checks stay guided. A post-success edit removes success before another check; incorrect replacement values fail with no lingering answer overlay. Repeated correct checks create no score or saved achievement.
- **Random smoke:** 1,200 new cases passed bounds, two-mile tower clearance, 25 to 155 degree fire angle, and reconstruction from the rounded sightings. Collinear smoke reports no triangle. Replacing a smoke during its swing and a burn during zoom settles on the latest case. A canceled independent drive earns no mark; a resize during arrival still completes correctly. There is no best score, reflection gate, or competitive meter.
- Evidence: `../../_scratch/fire-lookout-triangles/pre-*.json`, `post-*.json`, `recomputed-review.json`, `review-post/`, `review-focused/`.

## Voice walk
120 ms held clicks, two-second gaps, default student path first; repeated with Sound and Motion on after repairs. Main sequence heard: spotC, dispatch, sight, angles, right, af, right, cf, right, crew, onScene, radio, radioPin, two, right, radioNone, right, burn, right.
Spot's first map tap skips its welcome under BASELINE rule 16; the current hint still tells the student to tap another clearing. Each later mode/how-to starts once, in context. Read interrupts speech, works with Sound off, and releases on a mode change. No stale-mode speech or console exception was found in the captured walks.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Each main-path how-to above | how | 1 | 1 |
| miss, five side-path failed checks | event | 5 | 5 |
| right, five side-path correct checks | event | 5 | 5 |

Evidence: `review-voice-summary-final.json`, `review-voice-after-audit/`, earlier five-repeat counts in `review-voice-final/side-voice.json`, and its separate `keyboard-only.json`. This verifies browser narration behavior, not a recorded Algenib performance.

## Facts checked
- Laws of sines/cosines, opposite-side pairing, the 180 degree angle sum, positive SSA alternatives, and half-ab-sine-C area: [OpenStax 10.1](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-1-non-right-triangles-law-of-sines) and [10.2](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-2-non-right-triangles-law-of-cosines), checked live. All example numbers independently recomputed in `recompute-review.py`.
- Towers B (13.15569669, 4.78828201), C (6, -10.39230485), baselines 14/12 mi, reverse azimuths 250/330 degrees: independent coordinates from the fictional spec, with the same trigonometry sources.

| Smoke | A/B/F degrees | AF/BF/CF miles, independently rounded |
|---|---|---|
| 1 | 35/95/50 | 18.21 / 10.48 / 25.69 |
| 2 | 30/80/70 | 14.67 / 7.45 / 11.53 |
| 3 | 60/50/70 | 11.41 / 12.90 / 22.00 |
| 4 | 50/50/80 | 10.89 / 10.89 / 6.02 |

- Radio's perpendicular height is 7 mi. Radii 9/7/6 give two/one/zero solutions; AT is 6.46750140 or 17.78120990, then 12.12435565 mi; T is 128.94 or 51.06, then 90 degrees. Independent ray-circle and sine-law calculations agree with OpenStax 10.1. The far point's north coordinate 13.6212 minus the specified lake shore 11.5 is 2.1212 mi, so the approximately two-mile south clue fits.
- Burn areas: 0.40129821, 1.40953893, 0.32000000 square miles; 256.83085, 902.10492, 204.8 acres. Formula: OpenStax 10.1. Conversion 1 square mile = 640 acres: [NIST Handbook 44, 2026 Appendix C](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf), checked live.
- Azimuth clockwise from north and crossing lookout sightings: USDA Forest Service/NWCG, [Firefighter Math 6.2, Azimuths](https://www.nwcg.gov/course/ffm/location/firefighter-math-62-azimuths) and [6.8, Intersection](https://www-nwcg.fs2c.usda.gov/course/ffm/location/firefighter-math-68-intersection). No inventor or date is claimed.
- Derivation/proof/application coverage: [CCSS G-SRT.D.9 to D.11](https://www.thecorestandards.org/Math/Content/HSG/SRT/), checked live. Fictional geography and crews are clearly identified; this is a geometry model, not operational dispatch guidance. Local storage and no-request claims checked against source and the embedded bundle, not an external authority.

## Sensitivity
None: fictional forest and crews, no real community, culture, religion, hard history, body or people image. The scene needs no identifiable figure at this map scale. All eight assets were inspected; people flags are false. Fire depiction is quiet, with no injury.

## Flattest moment left
Repeated calculation forms remain deliberate calculator work. That is the specified grade 12 task. The formerly flat Radio ending now has a visible, case-specific lake-clue payoff; the forest scene and earned truck arrival were retained.

## Graphics
Inspected all eight assets at display scale: dusk lookout, forest canopy, tower, smoke, flame, truck, radio and burn scar. Radio redrawn once; five keyed assets cleaned. No missing art or added topic. Art 257.2 KiB; bundle 588.5 KiB, below 2 MB. Computed palette contrasts: accent/panel 5.83:1, accent/section base 5.53:1, dark ink/accent 6.12:1, map ink/halo 15.42:1. Compared fresh read-only Snowy Mail Route and Beat Lab frames, with `review-bar-comparison.jpg` side by side; preserved this tool's richer forest and restrained instrument style.
Opened all manual captures in `review-cold`, `review-play`, `review-break`, `review-post`, `review-sizes`, `review-changed`, `review-focused` and `review-voice-final`, plus the focused audit, current voice, copy/restart, fixture and edge re-check folders. Covered all STANDARDS sizes, all four phone modes through the 375x812 host, grayscale, Motion off, visible focus and keyboard-only completion. Secondary worked cards scroll; main input controls remain available.

## Audit
Completed once, last, within the 40-minute command cap: `review-audit/audit.md`, 109 mechanical leads and 66 frames. Confirmed target, text-layer and label collisions were repaired and re-shot at their affected sizes. Explicit input names were added. The broken drag-state definitions explain the hidden-step and lost-focus leads; corrected real-input replays reach the promised states, including a resized drive. The audit was not run again.
Intentional map/field-sheet/handle layering stays. Clear marks is secondary log maintenance; all actual smoke choices remain available. The clipped duplicate Burn card error has its complete copy and next action in the visible hint. Passive map clicks are not promised actions. First-tap welcome leads are covered by BASELINE 16 and the independently verified current-mode instructions. Calm, repeated-click and rapid-tap checks were clean. Full dispositions: [review-audit-disposition.md](../../_scratch/fire-lookout-triangles/review-audit-disposition.md).
Wave lessons were checked through the cold play, all sizes, real input and the scoped repairs: immediate state hints/Read, preserved focus, 44 px controls, non-color sight styles, honest numbers/marks, visible choice sets and Motion off. The standards coverage exception remains named above.

## Left open
- Curriculum coverage and requested recorded timbre above need a later scope decision; no kit changes, spec edits, recording, commit or deployment was made.
- Unattended choices: two rejected checks use the spec's two-miss assistance threshold; already exposed or guided triangles remain guided for this page session; preserve both SSA solutions; retain the unnamed fire finder; retain Burn 2's documented larger viewport because its exact geometry cannot fit a two-mile square.
- Process deviation: initial workspace/brief reads and memory search completed without an explicit command wrapper in under one second each. All subsequent commands used explicit deadlines. Review notes stayed in Scratch until this final report, honoring the stop-on-write instruction.
- Host file removed. All assigned Chrome and host ports verified closed; only the named tool and Scratch hold authored project changes. No git operation was made.
