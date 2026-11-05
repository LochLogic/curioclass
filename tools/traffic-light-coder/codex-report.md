# Codex report: traffic-light-coder

## Built

Build only, 2026-10-31, from `S:\CurioClass-codex`. No commits, shared-engine edits or polish round.
Two modes, five jobs, six-rule editor, live first-match execution through `Robot.run`, traffic, reports and replay.
The rule model and card list use the robot family. The shared kit handles Motion, Sound, Read, tones and voice.
Delivered source, offline bundle, draft metadata, teacher notes, voice lines, audit states, handoff, prompts and preview.
Source: 1418 readable lines, longest 155 characters. Only the allowed tool and Scratch folders were authored.

## Numbers check

PASS: independent `spec-numbers.py` recomputed 14 programs, all worked checkpoints and all seven contrast ratios.
The browser matches every checked light change, unsafe event, duration, wait, crossing count and pass/fail result.
35 feet / 3.5 feet per second = 10 seconds; WALK 7 seconds plus flashing hand 10 seconds.
Job 1 fixed: YELLOW 5.5, RED 8.5, WALK 9, GREEN 26.5. Job 3 broken: unsafe GREEN at 18.5.
Rush Hour: default red 86.5; long-green-only red 63; return-only green 0.5; wrong order red 63.
Rush Hour fixed: greens 30 and 30; longest red 18; longest walker wait 41.5 seconds.
Ambulance fixed: green through 43; YELLOW 46; WALK 49.5; waits 11.5 and 30.5 seconds.
Header contrast 12.191:1; ink/paper 14.642:1; muted/paper 5.899:1. All seven values are in `numbers.json`.
Full 120-second model cap measured 30.027 real seconds, including drawing and scheduling overhead.
Yellow-driver probes: a car initially over two seconds away stops; a closer one continues.

## Feel check

Played all five jobs through real held clicks, with full-length runs for jobs 4 and 5.
Best moment: the ambulance rule fails at the bottom, then succeeds at the top while both walkers still cross.
The 18.5-second replay makes the unsafe green visible beside the rule that caused it.
Flattest moment 1: curb buttons and the replay caption buried the compact crossing.
Changed: buttons moved beside the crossing; replay caption moved below it; warning moved to the curb.
Flattest moment 2: the original report hid its later unsafe line and return control.
Changed: the report uses the street area, and compact metrics use four columns so every report control fits.
Opened both bar tools. The painted street, vehicle details and signal housings meet the visual bar without copying its scene.
Frame comparison: `S:/CurioClass-codex/_scratch/traffic-light-coder/final-sheets/bar-comparison.png`.

![Traffic Light Coder beside Snowy Mail Route](S:/CurioClass-codex/_scratch/traffic-light-coder/final-sheets/bar-comparison.png)

## Done when

| Item | Result | Evidence |
|---|---|---|
| 1. Default live crossing and firing cues | PASS | Held curb input, default-program logs, 7/10-second sign model, ribbon and glow frames. |
| 2. Every starting job fails; every listed fix passes | PASS | `student/reports.json`: all five edited and solved through the UI; independent matrix agrees. |
| 3. Worked half-second checks and Rush Hour variants | PASS | `numbers.json`, browser matrix in `zero-rules-clock.json`; all 14 variants match. |
| 4. All three unsafe kinds with correct rule | PASS | Live-edit probes and `walk-while-cars-go.png`; exact names, times and rule numbers recorded. |
| 5. Ambulance bottom fails, top passes; line 14 | PASS | Student run plus focused missing-rule/bottom-rule narration checks. |
| 6. Replay and never-fired tags | PASS | Replay pauses at 18.5, selects rule index 3; duplicate fifth rule gets a never-fired tag. |
| 7. Crossing widest; rules beside it; report over street | PASS | 680x425 and 1366x768 frames; report remains inside the stage. |
| 8. Live Stop, Speed, Skip, card tap and edit | PASS | Held-input interruptions, active compact frames, Stop frame, immediate call state and next-check editor. |
| 9. Keyboard-only completion | PASS | `keyboard/result.json`: job 3 edited and passed using Tab, arrows and Enter; visible focus. |
| 10. All required sizes | PASS | Full size batch, 375 host, no horizontal overflow; laptop workbench fits; narrow layouts scroll vertically. |
| 11. Voice once/repeat/stale behavior | PASS | Audit two-second and quick-tap runs; `voice-settled.json`; repeated results and recovered instruction. |
| 12. Motion off and clean console | PASS | Zero running animations with ambulance active; all five jobs and final focused batches have zero errors. |

## Wave lessons

| Lesson | Result and check |
|---|---|
| Hint and voice | PASS: synchronous hints, Read uses the current hint, how lines use `V.heard`, no first-action wait. |
| Focus and layout | PASS: stable option nodes and deliberate focus after Skip, Replay and Next; no load focus. |
| Sizes and targets | PASS: curb buttons 60 px; compact job buttons and test controls at least 44 px; readable hints. |
| No giveaways | PASS: programs are constructed and tested; causal and never-fired feedback appears after execution. |
| Honest numbers | PASS: independent matrix; model limits labelled; priority speech requires an actual competing rule. |
| Standards | PASS: students combine conditions, decompose crossing phases, construct programs and debug all five jobs. |
| Motion off | PASS: no infinite animation; actors jump per check; the simulation clock remains unchanged. |
| Short choices stay visible | PASS: all seven condition choices fit; all four report controls fit at 680 and 760. |
| Resize mid-animation | PASS: full audit reports no exceptions or controls left disabled. |
| No late deferred welcome | PASS: no `welcomeAfter`; specified stale/action-first skips are retained, unmarked. |
| Unknown is unknown | PASS: no hidden diagnostic state is presented as known; no completed green is shown as “none ended”. |
| One look, one meaning | PASS: lamp position, words and color agree; one style for each warning and condition. |
| Badge says what is true | PASS: CALL SENT reflects waiting; reports use the tested rules; failed reruns never announce final success. |
| Hints change back | PASS: mode, reset, stop, edit, report and replay paths restore their own next-action hints. |
| No answer by word copying | PASS: this is a builder; selecting a label cannot satisfy a job without a working program. |

## Audit leads

The single full audit finished: 111 leads, zero console errors, clean resize stress and clean Motion off.
Every lead is answered individually in `S:/CurioClass-codex/_scratch/traffic-light-coder/audit-responses.md`.
49 fixed: zero-font icon label, compact job targets, lost Skip/Replay focus, compact report controls and replay overlaps.
62 accepted: narrow vertical scrolling and the spec's first-tap welcome skips. The report states these limits explicitly.
Targeted follow-up checks verify the fixes. The full audit was not repeated after them, per the one-audit build rule.
Five held clicks at two-second intervals and two quick taps were clean for every narrated control tested by the audit.
An early host-only favicon 404 was removed; final phone batches and final tool batches report zero errors.

## Frames looked at

All screenshots in `bar-frames`, `first-frames`, `layout-frames`, `check-frames`, `full-frames`, `focused-frames`,
`student`, `keyboard`, `last-frames`, `final-frames`, and all 81 audit screenshots were inspected, individually or on sheets.
The one full size batch covered 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812.
Further shots cover only fixes or unresolved checks, including grayscale, live controls, replay, report fit and SVG preview.
Scratch `README.md` maps the evidence; `final-validation.json` records checks and the final bundle hash.

## Art made

Nine images generated with the built-in `image_gen` tool; no CLI fallback, downloaded art or generated people.
Full prompt set: `S:/CurioClass-codex/tools/traffic-light-coder/art/prompts.json`.
Finished files in `S:/CurioClass-codex/tools/traffic-light-coder/art/`:

- `maple-street.webp`
- `car-red.webp`, `car-blue.webp`, `car-yellow.webp`, `van-green.webp`, `car-white.webp`
- `ambulance.webp`, `signal-head.webp`, `walk-signal.webp`
Raw originals copied to `art/raw/`; all assets processed only with `art.py --rekey <name>` and inspected at output size.
No redraws were needed. Total art 213.8 KiB; bundle 405.6 KiB (415,340 bytes), under 2 MB.
`preview.svg` embeds the painted assets and was rendered and inspected.

## Art still to paint

`walker-red`, `walker-yellow`, `walker-green`: people assets reserved for the owner's reviewed painter.
They remain marked `people: true`. The working scene uses faceless SVG silhouettes with backpacks.

## Engine changes wanted

Optional: `kit/robot.js`, `Robot.run`, a bounded `finishNow(limit)` that shares matching, execution, tick and trace
without beat waits, retaining the generation guard and one end callback. This would replace the tool's synchronous
Skip loop. Live execution and normal tests already use the engine. No shared file was changed.

## Left open

Three people images await the owner's painter. Narration has 16 fixed lines and browser fallback; no audio was recorded.
Narrow views deliberately scroll vertically. The full audit is a pre-fix record; focused checks cover the changes.
All owned Chrome ports 9970 through 9977 and host 8775 are closed. `host.html` was removed.
Build ends here. The separate cold review has not been started.
