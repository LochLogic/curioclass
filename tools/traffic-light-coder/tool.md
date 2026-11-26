# Traffic Light Coder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: traffic-light-coder

#### Built

Build only, 2026-10-31, from `S:\CurioClass-codex`. No commits, shared-engine edits or polish round.
Two modes, five jobs, six-rule editor, live first-match execution through `Robot.run`, traffic, reports and replay.
The rule model and card list use the robot family. The shared kit handles Motion, Sound, Read, tones and voice.
Delivered source, offline bundle, draft metadata, teacher notes, voice lines, audit states, handoff, prompts and preview.
Source: 1418 readable lines, longest 155 characters. Only the allowed tool and Scratch folders were authored.

#### Numbers check

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

#### Feel check

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

#### Done when

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

#### Wave lessons

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

#### Audit leads

The single full audit finished: 111 leads, zero console errors, clean resize stress and clean Motion off.
Every lead is answered individually in `S:/CurioClass-codex/_scratch/traffic-light-coder/audit-responses.md`.
49 fixed: zero-font icon label, compact job targets, lost Skip/Replay focus, compact report controls and replay overlaps.
62 accepted: narrow vertical scrolling and the spec's first-tap welcome skips. The report states these limits explicitly.
Targeted follow-up checks verify the fixes. The full audit was not repeated after them, per the one-audit build rule.
Five held clicks at two-second intervals and two quick taps were clean for every narrated control tested by the audit.
An early host-only favicon 404 was removed; final phone batches and final tool batches report zero errors.

#### Frames looked at

All screenshots in `bar-frames`, `first-frames`, `layout-frames`, `check-frames`, `full-frames`, `focused-frames`,
`student`, `keyboard`, `last-frames`, `final-frames`, and all 81 audit screenshots were inspected, individually or on sheets.
The one full size batch covered 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812.
Further shots cover only fixes or unresolved checks, including grayscale, live controls, replay, report fit and SVG preview.
Scratch `README.md` maps the evidence; `final-validation.json` records checks and the final bundle hash.

#### Art made

Nine images generated with the built-in `image_gen` tool; no CLI fallback, downloaded art or generated people.
Full prompt set: `S:/CurioClass-codex/tools/traffic-light-coder/art/prompts.json`.
Finished files in `S:/CurioClass-codex/tools/traffic-light-coder/art/`:

- `maple-street.webp`
- `car-red.webp`, `car-blue.webp`, `car-yellow.webp`, `van-green.webp`, `car-white.webp`
- `ambulance.webp`, `signal-head.webp`, `walk-signal.webp`
Raw originals copied to `art/raw/`; all assets processed only with `art.py --rekey <name>` and inspected at output size.
No redraws were needed. Total art 213.8 KiB; bundle 405.6 KiB (415,340 bytes), under 2 MB.
`preview.svg` embeds the painted assets and was rendered and inspected.

#### Art still to paint

`walker-red`, `walker-yellow`, `walker-green`: people assets reserved for the owner's reviewed painter.
They remain marked `people: true`. The working scene uses faceless SVG silhouettes with backpacks.

#### Engine changes wanted

Optional: `kit/robot.js`, `Robot.run`, a bounded `finishNow(limit)` that shares matching, execution, tick and trace
without beat waits, retaining the generation guard and one end callback. This would replace the tool's synchronous
Skip loop. Live execution and normal tests already use the engine. No shared file was changed.

#### Left open

Three people images await the owner's painter. Narration has 16 fixed lines and browser fallback; no audio was recorded.
Narrow views deliberately scroll vertically. The full audit is a pre-fix record; focused checks cover the changes.
All owned Chrome ports 9970 through 9977 and host 8775 are closed. `host.html` was removed.
Build ends here. The separate cold review has not been started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: traffic-light-coder
#### Played
Before builder notes: Grade 3 student play of the live crossing, all five starting jobs, two solved jobs and replay.
Then finished the remaining three UI fixes, checked projection frames and walked Teaching, Play and Craft.
The ambulance rule moving to the top remains the strongest moment; the painted street is worth keeping.
#### Findings fixed
- **Blocker, family:robot, teaching, src.html/summarize:** a missing yellow rule could produce “Rule 0”.
  Attribution now follows the light cycle active at ambulance arrival, including earlier-cycle cases.
  `audit-fixed-arrival-cause.png` verifies Rule 5; the standard ambulance case still names Rule 1.
- **Should fix, general, play, paused Watch hints:** calls said to watch a street that was stopped.
  Walker and ambulance hints now name Step and Play immediately; Read uses those hints.
- **Should fix, general, craft, narrow layout:** test controls followed the street and disappeared while editing.
  Hint and controls precede the street; test controls remain visible while the rules scroll.
- **Should fix, general, graphics:** the three specified walkers were temporary silhouettes.
  Painted and integrated all three, with natural skin/hair variation, backpack detail and correct travel facing.
- **Should fix, general, craft, compact unsafe reports:** the added trace pushed return/replay controls out of view.
  Repaired after audit: all three unsafe lines and Back to rules fit at 680, 800, 1000, 760 and 375 widths.
- **Polish, general, play, report:** the failed Rush Hour result was a large empty receipt of numbers.
  Added the student's actual car-light intervals, with words/patterns; content-sized cards reveal some street.
  Compact unsafe reports keep their existing replay chronology; the other reports retain the light trace.
- **Polish, general, notes:** stated that saved kit settings never leave the device.
#### Findings left
- **Polish, general:** stacked narrow pages still require vertical scrolling to reach every rule and card action.
  Primary test controls now stay visible. Five/six-rule internal scrolling is explicitly permitted by the spec.
- **Nit:** no further cosmetic changes accepted; the original street, cars, signals and palette remain intact.
#### Flattest moment left
A program with no matching rule waits to the 120-street-second cap. Skip to report is available throughout.
The flat failed report was lifted; this remaining wait is the specified test behavior.
#### Graphics
Checked all 12 finished images, the three people cutouts at scene size, grayscale, and all 89 audit frames.
Retained the nine original paintings; added walker-red, walker-yellow and walker-green using built-in imagegen.
Prompts/provenance: `art/prompts.json`; originals: `art/raw/`; finished assets: `art/*.webp`.
All three people assets have `people: true`; contact sheet: `_scratch/traffic-light-coder/walkers-contact.png`.
Matched the warm gouache set; no text artifacts or stereotypes found. Compared with both bar-tool frames.
Art: 232.0 KiB. Final offline bundle: 432.8 KiB.
#### Audit
One audit completed within 40 minutes using Chrome 9941 and host 8745; no second full audit.
79 leads: 8 addressed (compact report fit/clipping geometry), 61 narrow-scroll leads retained,
2 permitted six-rule scroll leads retained, 8 first-tap welcome skips required by the spec retained.
Every lead has an indexed response in `_scratch/traffic-light-coder/review-audit-responses.md`.
Motion off, held clicks, repeated speech, rapid taps and resize stress were clean; no audit console errors.
Eight targeted final frames passed with zero console errors. Rechecked only the affected layouts and attribution.
Independent Python results match 14 browser programs, including every Rush Hour variant and ambulance order.
Recomputed 35 / 3.5 = 10 seconds and all seven contrast ratios (minimum 5.333:1).
Keyboard-only Job 3 was edited, tested and passed with visible focus. Unsafe replay paused at 18.5 s on Rule 4.
Wave lessons checked: immediate hints, stable focus, targets, short choices, no giveaways, honest numbers,
standards practiced, Motion off, resize, truthful badges and first-tap timing. Notes open with the required sections.

| Spoken line | Kind | Expected | Observed |
|---|---|---|---|
| w-jobs | welcome | 1 | 1 |
| miss | event across five tests | 5 | 5 |

Evidence: `_scratch/traffic-light-coder/review-final-validation.json`, `review-numbers.json`,
`browser-numbers.json`, `keyboard-review.json`, `voice-review.json`, and `audit-fix-frames/`.
#### Left open
Narration uses browser fallback; no audio was recorded, as instructed. No classroom/headphone test was performed.
Narrow-page scrolling remains as described above. The optional shared runner finishNow request stays in handoff.
People contact sheet is available for the owner's pre-ship review. This review does not publish the tool.
Only the tool and its Scratch folder were written; no commits or shared-engine changes.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 0, family 2), should fix 10 (general 8, family 2), polish accepted 8

### Refine: traffic-light-coder

Lenses: `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity file; none needed, see Settled calls).
Lens scratch: `S:/CurioClass-codex-scratch/traffic-light-coder/` (teaching/, play/, craft/, audit-r1/).
Integrator spot-checks: src.html:796, 818-848, 1210-1224 and 1284-1300 read; `play/out/job5-y10-at43.png` opened
(44.0 s, light YELLOW, ambulance stopped in the queue behind the yellow car, detector on). Both blockers confirmed.

#### Blocker
1. **Job 5 "Ambulance never stopped" lies under a long yellow.** src.html:796
   (`if (j === 4 && w.t === 43) w.ambulanceStopped = w.light === 'RED';`), shown at src.html:1216. The check only asks
   "is the light RED at 43.0 s". Change job 5's rule 2 to "If YELLOW and been 10 s then turn RED" (one chip): yellow runs
   38.5 to 48.5, the driver model stops the ambulance (more than 2 s from the line on yellow) from 42.5 s to past 50 s,
   yet every check is green, "Job complete", and the stat says "Never stopped". "been 30 s" on rule 2 and "If YELLOW and
   ambulance coming then keep lights" pass the same way; none needs rule order, which is what job 5 teaches. The same
   10 s yellow also passes job 4. Seen: `play/out/job5-y10-at43.png`, `play/out/job5-y10-report.png`, teaching
   `sim-out.json` j5_yel10 and `amb-out.json` yel10. Fixed: set `ambulanceStopped` from the ambulance car's own
   `stopped` flag on any beat while it is on the street (`ambulanceAt` to `ambulanceUntil` and until it clears the
   crossing), not from the light at 43. Re-run the spec's job 5 worked checks (unfixed: "Had to stop"; top rule: passes)
   and the three cheap programs above (all must now fail with "Had to stop"). Keep the arrival-cause line working.
   (family:robot)
2. **Job 3 passes with the light stuck on red.** src.html:642 (job 3 start) and src.html:822-834 (job 3 checks only
   "Nothing unsafe" and "Every walker crossed"). The brief says the light turns green too soon; the natural grade 3 move,
   deleting rule 4, gives "Job complete", "Every goal is met. Job finished." and Next job, while the same report shows
   "Longest red: 81.5 s" and "Cars waited 10 s or more". Play's brute force (`play/bf.json`) found 82 single edits that
   pass job 3, most broken: delete rule 4, "keep lights", "turn RED" or "turn GREEN" on the wrong light, an ambulance
   condition that never fits, and "If RED then turn YELLOW" (red to yellow, longest red 1 s). Five such passes also earn
   the finale. Seen: `play/out/job3-delete-r4.png`. Fixed: give job 3 one more goal check, in the report's plain words,
   that the cars get their green back after each walk (for example "Cars get a green again": every red ends in GREEN
   and the longest red is under 45 s, reusing the job 4 limit and its "the tool's own limit" label). Then re-run the
   single-edit brute force for job 3: only "walk is done" style fixes may pass, the listed fix ("been 10 s" to "walk is
   done") still passes, and the starting rules still fail with three "Green while crossing". Add one line to notes.md
   saying job 3 now has this check. (family:robot)

#### Should fix
3. **Each job's problem is spoken only, never on screen.** Street Jobs job card (src.html:939-942) and `waitingHint()`
   (src.html:873-877). The brief ("Walkers press the button, but the light never changes...", "The light turns green
   too soon...") is the only place the student learns what is wrong; the card shows title and goal, and the hint (which
   Read speaks) is the same generic line for all five jobs. Sound off, a first tap that hushes the brief (it starts at
   8.1 s on a fresh page) or a second visit loses it (BASELINE rule 16). Seen: `audit-r1/state-mode-street-jobs-1366x768.png`,
   Play's flow-jobs log. Fixed: one plain problem line per job on the job card (the brief's first sentence, without the
   fix), and the job's next step in the waiting hint so Read brings it back. Do not state the fix. (general)
4. **The order line blames a rule that did not change the light.** src.html:1219. In job 4 with rule 4 changed but left
   below rule 3 the report says "Rule 3 changed the light first. Rules are checked from the top."; rule 3 starts WALK,
   it does not change the car light, so a student looks at the wrong card. In job 5's starting report the same words
   ("changed the light first") suggest a contest when only one rule existed. Seen: `play/out/job4-order.png`, teaching
   sim `j4_r4below`. Fixed: use the spec's own wording, "Rule N fired first. Rules are checked from the top." (spec
   worked check, job 5), and for job 4 name what it did ("Rule 3 fit first and started WALK."). (family:robot)
5. **Rush Hour's missed-fairness report names no rule.** src.html:839-844 and 1218-1220: the order note only shows when
   rule 4 already has "been 10 s". With only "been 30 s" added (the natural first try) the report shows "Reds under
   45 s" failed and "Longest red: 63 s" and nothing else; the cause (rule 3 starting WALK again and again) is only in
   the ribbon chips. A solo student (rule 4) is stuck. Seen: teaching `sim-out.json` j4_30only. Fixed: when "Reds under
   45 s" (or "Greens at least 30 s") fails, add one line naming the rule that fired most during the longest red, in the
   "Rule N did it" pattern ("Rule 3 started WALK 4 times while cars waited 63 s."). Leave the walker spacing alone; that
   is the spec's open question. (family:robot)
6. **At 760x900 the rule list and Add rule start below the fold.** src.html:393-411 and 473-487, stacked layout. In
   Street Jobs the rules begin about y 690 and Add rule is off screen, so the student scrolls between Run test and the
   rules every round; report and replay push them further. Seen: `audit-r1/state-mode-street-jobs-760x900.png`,
   `audit-r1/state-job-report-760x900.png`. Fixed: at 760x900 keep stage and panel side by side with the compact panel
   (as the short-landscape layout does), or shrink the stage so the first rules and Add rule are visible without page
   scroll. 375 wide in the host stays a stacked page (allowed). (general)
7. **The chip picker hides the rule it edits.** `#picker`, src.html:275-295 and 1293-1300. At 1366x768 the dialog covers
   the left of the rule list; at 680x425 every rule. The slot tabs read only "If light / and... / and... / then...", so
   the student edits one slot of a sentence they can no longer see. Seen: `audit-r1/state-chip-picker-1366x768.png`,
   `craft/v2/picker-680.png`, `audit-r1/state-all-condition-choices-1366x768.png`. Fixed: show the live rule sentence
   at the top of the picker, and put the current value in each tab ("If GREEN", "and button pressed", "and +", "then
   turn YELLOW"). (general)
8. **PUSH TO WALK buttons cover the crosswalk and stopped cars at small sizes.** src.html:155-163 (60 px buttons). At
   680x425 and 375 wide the street is about 100 px tall: the south button sits on the crosswalk and hides the east-lane
   car stopped at the red and its signal dot, the north one covers the west stop line. Seen: `audit-r1/size-680x425.png`,
   `craft/v2/red-stop-680.png` and `craft/v2/zoom-red-680.png`, `audit-r1/size-375x812 (iframe host).png`. Fixed: put
   the buttons on the sidewalks clear of the crosswalk and stop lines (or draw them smaller with the street while the
   hit area stays 44 px or more). 1366x768 is fine; keep it. (general)
9. **The goal card uses symbols and "model limit".** src.html:940-942: "Model limits: green ≥ 30 s; red < 45 s; walker
   wait < 60 s." Grade 3 meets ≥ nowhere else, and the report already says it in words. The spec requires these to be
   labeled as the tool's own limits, so keep that, in plain words: "Fair-time rules (this tool's own): greens at least
   30 s, reds under 45 s, walkers wait under 60 s." Same for job 1. Also rename the job 4 stat "Longest empty red" to
   plain words ("Cars stopped with nobody crossing: N s"), here and in the Empty crosswalk stat. Seen:
   `audit-r1/state-mode-street-jobs-1366x768.png`, `audit-r1/state-rush-hour-1366x768.png`. (general)
10. **The chip line says "Press Add rule" right after Add rule, behind a modal.** src.html:1288-1290 with 1443-1455.
    The first thing heard after pressing Add rule is "...Press Add rule to write a new one.", spoken while the picker
    is open and Add rule is inert behind the backdrop (STANDARDS: no line names a control that is off). Seen:
    `craft/v1` v-add-first log; audit "one held click" row 10. Fixed: the picker's how line names what is in front of
    the student ("Pick a chip, then press Done."); keep the Add rule half for the hint after Done. Update `L`,
    `voice/lines.json` and the spec-matching line table together. (general)
11. **A talk question teaches the wrong rule.** notes.md:51 "Why can a rule at the bottom never get a turn even when its
    condition fits?" is false: job 1's fix passes with the new rule at the bottom (teaching sim `fix1bot`). Fixed: "Why
    can a rule lower down lose its turn even when its condition fits?" (general)
12. **Notes overclaim the standards.** notes.md:77 says the three codes are "practiced directly". All three grade 3
    codes name a combination of sequence, events, iteration and selection; the student authors selection and uses
    events, but never writes the loop (the engine's fixed half-second check) and sequence only emerges from rules.
    Fixed now, inside the spec: notes say honestly which part each code gets here; the panel foot and Step name the
    loop where the student already sees it ("Every half second the light goes once round the loop: check from rule 1.")
    and the job 1 and 2 notes frame the fix as building the GREEN, YELLOW, RED, WALK sequence out of rules. Whether a
    code should move or be shared goes to the spec's open questions below. (general)

#### Polish accepted
13. **Mark the finale on screen.** After all five jobs, the last report looks like every other; only the spoken line
    (needs Sound) says it is done. Add a small "All five jobs done" line with the five filled dots on that report. No
    stars, no score. Seen: `play/out/alljobs.png`. (general)
14. **Two ↻ icons at 680x425.** "Default rules" shrinks to a bare ↻ next to "↻ Reset street"; one keeps the program,
    one throws it away. Use a different icon or the short word "Defaults". Seen: `audit-r1/size-680x425.png`. (general)
15. **Watch the Street: one thing to try.** After the first full cycle the hint names one change to try ("Change rule 1
    to turn RED, then press a walk button. What does the street say?"). Hint only, not spoken again. Seen:
    `play/out/watch-walk.png`, `play/out/watch-flash.png`. (general)
16. **Bigger rule text at 1366x768.** src.html:218-221: rule-line 12 px, words and chips 11 px, cards a third empty. Use
    14 px chips and words at 1280x720 and up. Re-check six rules still fit with the allowed inner scroll. Seen:
    `audit-r1/size-1366x768.png`. (general)
17. **Picker option dots in lamp colors.** src.html:1307-1310: GREEN, YELLOW, RED and the three "turn" actions share a
    plain black dot. Color the dot by lamp (the word stays), and give the "turn" actions a small arrow. Seen:
    `audit-r1/state-chip-picker-1366x768.png`. (general)
18. **Announce the report when a played test ends.** src.html:595 and 1147-1160: no focus move, `#hint` not live, the
    report has `role="dialog"` but is not modal. Focus the report heading (preventScroll) on every finish, and drop
    `role="dialog"` (or make it behave like one). (general)
19. **Grey tab on the job card.** `.job-card::before` (src.html:195) reads as a dead drag handle in every Street Jobs
    frame and pokes above the report card at 680x425. Remove it or keep it inside the card. Seen:
    `play/out/grey-bar.png`, `audit-r1/state-job-report-680x425.png`. (general)
20. **Ribbon dots by color only.** src.html:1101-1103. Add a letter (G, Y, R, W) on each fired-rule dot so the light
    each rule set does not rest on color alone. (general)

#### Settled calls
- Blocker 1 is fixed inside the spec (its goal says the ambulance never stops; the readout must follow the ambulance).
  A new "Yellow too long" unsafe kind (MUTCD 4D.26, 6 s maximum, already in the spec's sources) adds a fourth unsafe
  kind to a list the spec fixes at three, so it goes to the open questions, not to Codex this round.
- Blocker 2 adds one goal check to job 3. Taken as a fix, not a spec change: the job's brief and its listed fix only
  make sense if the light still turns green, and the check reuses wording and a limit the spec already has. It is
  also raised below so Cory can confirm the job table row.
- Picker (should fix 7): Play tagged it family:robot polish, Craft general should fix. Settled as should fix, general:
  the picker is this tool's own dialog, and hiding the sentence being edited is a flaw a student meets every edit.
- Push buttons (should fix 8): Play said polish, Craft should fix with the stopped car hidden. Settled as should fix.
- Order line (should fix 4) and goal card words (should fix 9): Teaching said polish, Play should fix. Settled as
  should fix; both send a grade 3 reader the wrong way.
- Do not change: job 4's two-change fix and walker spacing (open question); the 375 wide stacked page; the six-rule
  inner scroll; the welcome being skipped after a first tap on a rule card, push button or Send walker (rule 16, the
  premise stays in the panel foot); the "Green while crossing" collision moment (a strong moment, keep it).
- Not a Curiosity; no sensitive topic, nothing cultural or hard-history, so no sensitivity agent. The three walker
  pictures still need Cory's people review (BASELINE rule 11); that is not a Refine item.
- Contract is clean (443 KB, no network, no console errors, kit used, voice table matches lines.json, no em dashes).

#### To the spec's open questions
- Add a "Yellow too long" unsafe kind (over 6 s, MUTCD 4D.26) so a long yellow is named with its rule in every job?
- Job 3 now checks that cars get their green back (blocker 2). Confirm the job table row: "safe; all cross; cars get a
  green again".
- Standards: the student never writes the loop or a sequence directly. Keep E3-ALG-PS-01 and E3-PRO-PD-04 here with the
  honest notes from should fix 12, or share them with a grade 3 sibling where the student authors the loop?

#### Not taken
- Dead "Six rules is the most" line (Craft nit 9): it is in the spec's line table; harmless; settle at the voice step.
- Reset street hushes the welcome and drops the queued press line (Craft nit 10): the hint still shows the step.
- Seeded Watch traffic mostly blue cars (Play nit 13): random kit draw, cosmetic, no student cost.
- Job 5 starting report wording as its own item (Teaching nit 7): folded into should fix 4.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: traffic-light-coder (round 1)

Cold Craft lens on the built bundle `tools/traffic-light-coder/traffic-light-coder.html` (not re-bundled). Grade 3
lesson tool, not a Curiosity. My frames and logs: `S:/CurioClass-codex-scratch/traffic-light-coder/craft/` (v1, v2,
v3 folders; drive.py with held clicks, port 9851). Shared audit: `S:/CurioClass-codex-scratch/traffic-light-coder/audit-r1/`.

#### Contract (clean)

- One file, 443 KB (well under the 2 MB goal). The only URL in the bundle is the SVG namespace; no network requests.
- No console errors or exceptions in any of my 21 driven shots (voice runs, five-test loops, keyboard runs, Motion off,
  picker at three sizes) or in the audit.
- Kit used, not re-implemented: `Robot.program`, `Robot.strip`, `Robot.run` (style rules), `Curio.voice`. Skip to
  report re-runs the check loop by hand (src.html:1173-1184) but in the same order as the kit runner (check, fire,
  then tick; kit/robot.js:117-131), so a skipped test and a watched one give the same report.
- Frame times while a walk cycle plays at 1366x768: 400 frames, median 16.7 ms, p95 16.7, max 16.8
  (`v2` frametimes shot).
- Every `art:` token (12) has a prompts.json entry; the three walkers carry `"people": true`. Cory's people review
  of the three overhead children is still owed (BASELINE rule 11), not a lens finding.
- Words: no em dashes in src.html, notes.md, lines.json or the bundle; "Curio Class" everywhere; classroom-safe.
- `voice/lines.json` and the tool's line table `L` match word for word (16 of 16, checked by script); `allLines` is
  exposed on `__tool`.

#### Findings

1. **should fix, general.** src.html:1288-1290 and 1443-1455. The `chip` how line ("Tap a chip in a rule to change it.
   Press Add rule to write a new one.") plays right after the student presses Add rule, so the first thing they
   hear after pressing Add rule is "Press Add rule". It also plays with the picker modal open, where Add rule sits
   inert behind the backdrop, so it names a control that cannot be pressed at that moment (STANDARDS: no line
   names a control that is off). Seen: `v1` v-add-first (first tap on Add rule, log `chip spoken`, focus on Done in
   the open picker); audit "one held click" row 10 shows the same. Better: a line for the open picker that names
   what is in front of the student ("Pick a chip, then press Done."), and the Add rule half kept for the hint after
   Done.

2. **should fix, general.** src.html:275-295 and 1297-1300. The chip picker hides the rule it edits. At 1366x768 the
   centred dialog covers the left of the rule list, including rule 1's light chip; at 680x425 it covers every rule.
   The slot tabs read only "If light / and... / and... / then...", never the current values, so the student
   changes one slot of a sentence they can no longer see (a grade 3 student editing "and..." cannot tell which
   condition is already set without opening each tab). Seen: `audit-r1/state-chip-picker-1366x768.png`,
   `craft/v2/picker-680.png`, `craft/v2/picker-action-1366.png`. Better: put the live sentence at the top of the
   dialog (or the current value inside each tab: "If GREEN", "and button pressed", "and +", "then turn YELLOW"),
   or place the dialog over the street so the card stays visible.

3. **should fix, general.** src.html:155-163 (push buttons fixed at 60 px) at 680x425 and 375 wide. In the preview
   sizes the street is about 100 px tall, and the two 60 px PUSH TO WALK buttons sit on the road: the south button
   hides the east-lane car stopped at the red stop line and the east signal dot, the north one covers the west-lane
   stop line. The moment the tool exists to show (cars stopped at red while a walker crosses) is half hidden there.
   Seen: `craft/v2/red-stop-680.png` (zoom: `craft/v2/zoom-red-680.png`), `audit-r1/size-375x812 (iframe host).png`;
   1366x768 is fine (`craft/v2/red-stop-1366.png`). Better: move the buttons onto the sidewalks clear of the stop
   lines (each curb's far end), or shrink them with the street while keeping a 44 px hit area.

4. **should fix, general.** src.html:393-411 and 473-487, 760x900 (and 375 wide). The stacked layout puts the rule
   list, the card buttons and Add rule below the fold in Street Jobs: the main controls a student edits every few
   seconds need a page scroll (STANDARDS, Sizes: main controls visible without scrolling at every size). Audit
   lead confirmed on `audit-r1/state-mode-street-jobs-760x900.png` (rule 3 and Add rule out of view) and the
   job-report, replay, rush-hour and ambulance rows at 760x900. Better: at 760x900 keep stage and panel side by
   side with the compact panel (as the short-landscape layout already does), or shrink the stage so the rule list
   starts above the fold.

5. **polish, general.** src.html:218-221 (rule-line 12 px, `.word` and `.chip` 11 px). On the main size, 1366x768,
   the rule sentences a grade 3 student reads all lesson are 11 to 12 px, while each card is 70 px tall and about
   a third empty. Seen: `audit-r1/size-1366x768.png`. Better: 14 px chips and words at 1280x720 and up (the 1600 px
   rule already goes to 14 to 15 px).

6. **polish, general.** src.html:1307-1310. Picker options for GREEN, YELLOW, RED and the three "turn" actions all
   use the same plain black dot icon, so the 60 px rows look alike. Seen: `audit-r1/state-chip-picker-1366x768.png`,
   `craft/v2/picker-action-1366.png`. Better: the dot in the lamp color (the word stays, so color is not the only
   signal), and a small arrow or lamp for the "turn" actions.

7. **polish, general.** src.html:595 and 1147-1160. When a test plays to its end (not skipped), the report opens with
   no announcement and focus stays on Run test; the report is marked `role="dialog"` but is not modal and takes no
   focus, and `#hint` is not a live region. A keyboard or screen-reader user gets no sign the result arrived.
   Seen: code read plus `craft/v3` (focus log). Better: focus the report heading (preventScroll) on every finish,
   or make the hint `aria-live="polite"`; drop `role="dialog"` or make it behave like one.

8. **nit, general.** src.html:1101-1103. The fire ribbon tells which light each rule set by a colored dot only (the
   number gives the rule, the tooltip the action, neither on screen). Better: a letter G/Y/R or the trace bar's
   stripe and underline patterns on the dot.

9. **nit, general.** src.html:1443-1447 with 935. Line 16 ("Six rules is the most. Change a rule instead.") can never
   play: Add rule is disabled at six rules, so its click handler never runs. The hint already says it. Drop the line
   from `L` and lines.json so it is not recorded for nothing, or say it from the disabled state another way.

10. **nit, general.** src.html:1405-1414. Reset street in Watch the Street hushes the welcome mid-sentence (marked
    said) and drops the queued "press" how line without queuing it again. The hint still shows the press step, so
    nothing is lost; noted only because it is the one place a mode's how line is lost without a first tap.
    Seen: `craft/v2` stale-fast log.

11. **nit, general.** src.html:195. At 680x425 the job card's grey tab (`.job-card::before`) pokes out above the
    report card's top edge. Seen: `audit-r1/state-job-report-680x425.png`.

#### Standard voice check

Sound on, Motion on, held clicks (0.12 s), gaps longer than the lines. Logs in `craft/v1` and `craft/v2` drive output.

| line | kind | action, five times | expected | spoken |
|---|---|---|---|---|
| chip | how | open a rule card, Done (x5, 4 s apart) | 1 | 1 |
| report | how | Job 3: Run test, Skip (x5, 7 s apart) | 1 | 1 |
| unsafe | event | Job 3: Run test, Skip (x5) | 5 | 5 |
| miss | event | Job 1: Run test, Skip (x5, 6 s apart) | 5 | 5 |
| w-jobs | how (welcome) | enter Street Jobs | 1 | 1 |
| job1 brief | how | Run test pressed while it was queued | dropped, said again later | dropped (hush), not marked said |
| w-watch / press | how | push buttons x5, 2.5 s apart | 0 (stale on first push) | 0 |

- Stale lines: fast taps 0.2 s apart (Street Jobs, job 2, job 4, Run test, Skip, Watch the Street, Reset street):
  every line was cut by the next action's hush or dropped unplayed; none played after its moment.
- First tap: the stage gets the welcome about 0.2 s after the tap; Sound says nothing; Tab then Enter gets the
  welcome; Read speaks the hint only (audit row 4); a push button or rule card skips the welcome (rule 16; the
  premise "first rule that fits wins" stays on screen in the panel foot and the ribbon header).
- Read: Read during w-jobs cut it and spoke the hint; Read with Sound off spoke the hint.
- Order: spoken lines followed the actions in every run; no older line after a newer one.
- Every spoken line matched the screen at its time except finding 1.

#### Access (clean apart from findings 2, 7, 8)

- Keyboard: Tab order (Street Jobs) is header, Run test, Speed, Start over, rule cards, Add rule, job dots 1-5, as the
  spec asks; every stop showed a 3 px focus outline (`craft/v2` kb-order-jobs). Enter on Add rule opens the picker
  with focus on Done; Tab reaches slot tabs then chips; Escape returns focus to the card; plain ArrowDown on a card
  moves focus, not the rule (`craft/v3`).
- Targets: every control is 44 px or more; picker rows 60 px; push buttons 60 px (audit, all sizes clean).
- Motion off: transitions and blinking stop, timing unchanged (audit "Motion off" clean, `craft/v2/calm-walk.png`).

#### Audit pilot

- Leads confirmed: 760x900 rule list and Add rule below the fold (finding 4); the welcome is not heard after a first
  tap on a rule card, Add rule, a push button or Send walker (true, and allowed by rule 16; the premise stays on
  screen, so not reported).
- Leads wrong or not worth a finding: the 375x812 below-the-fold rows are a stacked phone page, which the spec allows;
  "keep region #strip x% inside the window" at 375 and 760 is the same stacking as finding 4; six-rules "choices cut
  short" is the scrolling the spec permits over four rules.
- Missed by the audit: the chip line naming Add rule right after Add rule and behind a modal (1); the picker hiding the
  rule it edits (2); push buttons covering the stopped cars at preview sizes (3); small rule text at 1366x768 (5);
  look-alike picker icons (6); no announcement when a played test ends (7); the dead six-rules line (9).
- Nothing cultural, Native or hard-history here; no sensitivity review needed. The three walker images still need
  Cory's people review.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: traffic-light-coder (round 1)

Played twice: as a grade 3 student alone at home (Watch the Street first, then Street Jobs one to five), and as a
teacher projecting at 1366x768. Frames are in `S:/CurioClass-codex-scratch/traffic-light-coder/play/out/` (mine) and
`S:/CurioClass-codex-scratch/traffic-light-coder/audit-r1/` (the shared audit). I also tried every job the cheap way:
a brute force over every single edit of each job's starting rules (every chip change, every delete, every swap, and
one added rule of any shape at any position: 1819 to 2281 programs per job) through `__tool.simulate`, saved in
`play/bf.json`.

Counts: blocker 2, should fix 4, polish 5, nit 2.

#### Blockers

1. **Job 3 passes with the light stuck on red: delete the "turn GREEN" rule and the job is "complete".**
   Where: Street Jobs, job 3 (src.html:643 starting rules; src.html:822-834 goal checks: job 3 checks only "Nothing
   unsafe" and "Every walker crossed"). What: the brief says "The light turns green too soon. Find the rule that does
   it." The most natural kid move is to delete that rule. The report then says "Job complete", the voice says "Every
   goal is met. Job finished.", and Next job appears, while the same report shows "Longest red: 81.5 s" and "Cars
   waited 10 s or more" (the car-light bar is one long RED). The brute force found 82 single edits that pass job 3;
   most are broken programs: delete rule 4, change it to "keep lights", "If RED and been 10 s then turn RED", "If
   GREEN and been 10 s then turn GREEN", "If RED and ambulance coming then turn GREEN" (all leave the light red to the
   end), and "If RED then turn YELLOW" (red to yellow, longest red 1 s). Five such passes in a row also earn the
   finale "Maple Street is safe and fair". How seen: `play/out/job3-delete-r4.png` (real clicks Run test, Skip to
   report on job 3 with rule 4 removed), bf.json job 3. Fix direction: job 3 needs a check that the cars get their
   green back (for example "Cars get a green again" or the "Reds under 45 s" check jobs 4 uses), so the only passes
   are "walk is done" fixes. Tag: family:robot (the job table's goal checks).

2. **Job 5 "Ambulance never stopped" lies: a long yellow stops the ambulance on the street and the report still
   passes.** Where: Street Jobs, job 5 (src.html:796 `ambulanceStopped = w.light === 'RED'` at t = 43 only). What:
   change rule 2 to "If YELLOW and been 10 s then turn RED" (one chip). Yellow then runs 38.5 to 48.5; the ambulance
   reaches its stop line at 42 and sits STOPPED from 42.5 to past 50 (the driver model stops any car more than 2 s
   from the line on yellow), yet at 43 the light is YELLOW, so the report says "Ambulance never stopped", "Job
   complete", and every check is green. "been 30 s" on rule 2 passes the same way with a 30 s yellow, and so do
   "If YELLOW and ambulance coming then keep lights" programs (yellow held 7.5 s). None of these needs rule order,
   which is what job 5 teaches, and a 10 or 30 s yellow is never called unsafe even though the spec's own source
   (MUTCD 4D.26) puts a yellow at 3 to 6 s. How seen: `play/out/job5-y10-at43.png` (street at 44.0 s: YELLOW, the
   ambulance stopped behind the queue, detector line on), `play/out/job5-y10-report` result text (all checks pass,
   "Never stopped"), and the simulated history in the drive log (`42.5 YELLOW amb x=0.275 STOPPED` ... `50 RED
   STOPPED`). Fix direction: set "Had to stop" from the ambulance's own stopped flag at any time while it is on the
   street, and add a "Yellow too long" unsafe kind over 6 s (sourced). Tag: family:robot.

#### Should fix

3. **The job's problem is spoken only, never on screen; Read cannot bring it back.** Where: Street Jobs job card
   (src.html:939-942) and `waitingHint()` (src.html:875). What: the brief ("Walkers press the button, but the light
   never changes. Press Add rule and write the rule that starts it.", "Fix rule one, and add a rule for yellow", "The
   light turns green too soon") is the only place a student learns what is wrong. The card shows only the title and
   goal; the hint is the generic "Tap a rule to change its chips, or press Add rule. Then press Run test." for all
   five jobs, and Read speaks that hint. A student with Sound off, a first tap that cuts the brief, or a second visit
   to the job never sees it (on a fresh page the brief only starts at 8.1 s, after the 6.7 s welcome:
   flow-jobs log). BASELINE rule 16: what the welcome says must stay reachable in the hint or by Read. Better: one
   plain line on the job card ("Walkers press, but the light never changes.") and the job's next step in the hint.
   How seen: `audit-r1/state-mode-street-jobs-1366x768.png`, Read row in the audit table, my flow-jobs log. Tag:
   general.

4. **Job 4's order note blames a rule that does not change the light.** Where: report, src.html:1219. What: job 4
   with rule 4 changed but left below rule 3 says "Rule 3 changed the light first. Rules are checked from the top."
   Rule 3 is "start WALK"; it did not change the car light, it fired first and kept rule 4 from getting a turn. A
   grade 3 reader looking at rule 3 sees no light change and is lost. Use the spec's words ("Rule 3 fired first").
   How seen: job4-order run (report text in the drive log, `play/out/job4-order.png`). Tag: family:robot.

5. **At 760x900 the rule list and Add rule start below the fold.** Where: stacked layout under about 1000 px wide.
   What: in Street Jobs the rules begin at y 690 and Add rule is far below; the student scrolls between Run test and
   the rules every round (STANDARDS: main controls visible without scrolling at every size). Report and replay at the
   same size push them further (audit "choices cut short" leads). How seen:
   `audit-r1/state-mode-street-jobs-760x900.png`, `audit-r1/state-job-report-760x900.png`. Tag: general.

6. **Grade 3 goal card uses symbols and jargon.** Where: src.html:940-942. What: "Model limit: walker wait < 60 s." and
   "Model limits: green ≥ 30 s; red < 45 s; walker wait < 60 s." A grade 3 student meets ≥ nowhere else and "model
   limit" means nothing to them; the report's own check labels are already plain ("Walker waits under 60 s", "Greens
   at least 30 s"). Use those words on the card too ("Fair rules for this job: ..."). Report stat "Longest empty red"
   is the same problem (say "Cars stopped with nobody crossing"). How seen:
   `audit-r1/state-mode-street-jobs-1366x768.png`, `audit-r1/state-rush-hour-1366x768.png`. Tag: general.

#### Polish

7. **The chip picker hides the rule it edits and the street.** Where: `#picker` dialog. What: the modal covers the
   rule card and its slot tabs only say "If light / and... / and... / then...", so while choosing a student cannot see
   the sentence they are building, and in Watch the Street ("Changes count at the next check") the street they are
   meant to watch is behind the dialog. Better: show the live rule sentence at the top of the picker and put the
   current value in each tab ("and button pressed"). How seen: `audit-r1/state-all-condition-choices-1366x768.png`.
   Tag: family:robot.

8. **The finale is flat.** Where: job 5 pass after all five. What: the last report looks like every other report;
   the job dots are under it and nothing on screen says all five jobs are done (only the spoken line, which needs
   Sound). Better: a small "All five jobs done" line on the report with the five filled dots, still with no stars.
   How seen: `play/out/alljobs.png`. Tag: general.

9. **At 680x425 the south PUSH TO WALK button sits on the crosswalk.** Where: Watch the Street, compact layout. What:
   the 60 px button covers the lower half of the crosswalk and the near stop line, exactly where walkers step out.
   Better: keep the buttons on the sidewalks or beside the crosswalk at small sizes. How seen:
   `audit-r1/size-680x425.png`. Tag: general.

10. **Two ↻ icons mean different things at 680x425.** Where: Watch the Street, compact panel. What: "Default rules"
    shrinks to a bare ↻ next to the "↻ Reset street" button; one keeps the program, one throws it away. Better: a
    different icon or the short word "Defaults". How seen: `audit-r1/size-680x425.png`. Tag: general.

11. **Watch the Street has nothing to try once the light cycles.** Where: Watch the Street. What: after one press the
    default program cycles and there is no suggestion of what to break or change; the unsafe kinds only show if the
    student happens to edit a chip. Better: the hint, after the first full cycle, names one thing to try ("Change
    rule 1 to turn RED and press the button. What does the street say?"). How seen: `play/out/watch-walk.png`,
    `play/out/watch-flash.png`, `play/out/watch-unsafe.png`. Tag: general.

#### Nits

12. A short grey bar sits on the top edge of the job card in every Street Jobs frame (inside `#job-card`, it reads as
    a drag handle that does nothing). `audit-r1/state-mode-street-jobs-1366x768.png`. Tag: general.
13. The seeded Watch traffic is mostly blue cars (three of three in `play/out/watch-ambulance.png`, four of six in
    `watch-walk.png`); the five-car kit rarely shows. Tag: general.

#### Checked and fine

Default screen and every mode at all sizes (audit clean rows), Watch press cycle YELLOW, RED, WALK 7 s, FINISH 10 s,
GREEN with the ribbon in step (`watch-walk.png`, `watch-flash.png`), unsafe flash and Watch out line
(`watch-unsafe.png`), replay pause on the named rule (`audit-r1/state-replay-1366x768.png`), job 1, 2 and 4 have no
single-edit pass (job 2 and 4 need the spec's two changes), job 5's rule-order failure and "Two rules fit at once"
line, Motion off (audit clean), voice order on a fresh Street Jobs page (welcome, brief, result: no stale lines).

#### Audit pilot

- Leads confirmed: 760x900 rules below the fold / cut by the panel in Street Jobs, report and replay (finding 5);
  375x812 controls below the fold are the expected stacked layout inside the host (not reported).
- Leads wrong or not worth a finding: "welcome not heard" after a first tap on a rule card, push button or Send walker
  in Watch the Street: rule 16 allows it and the premise stays on screen in the panel foot ("Every half second, check
  from rule 1. Only the first rule that fits gets a turn."). Six rules at 1366x768 with one card scrolled is the
  spec's allowed inner scroll.
- Missed by the audit: both blockers (cheap passes and a lying ambulance check need the job logic run with wrong
  programs), the spoken-only job briefs (the audit saw Read speak the generic hint but cannot judge that the brief is
  lost), the wrong rule wording in job 4's order note, the button over the crosswalk at 680x425, and the flat finale.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens, round 1: traffic-light-coder

Cold read of spec.md, src.html, notes.md, voice lines in src, audit-r1. Checks run with `scripts/drive.py` on port 9831
through the page's own `__tool.simulate` (the same `when`, `execute`, `tickWorld` and `summarize` the live tool uses):
every job's starting rules, every listed fix, job 4's three variants, job 5 top and bottom, plus cheap-pass attempts.
Scratch: `S:/CurioClass-codex-scratch/traffic-light-coder/teaching/` (sim-out.json, amb-out.json, frames/).

#### Findings

##### 1. Job 5 passes with a 10 s yellow, and the report says "Never stopped" while the ambulance sits stopped (blocker, family:robot)
- Where: src.html:796 (`if (j === 4 && w.t === 43) w.ambulanceStopped = w.light === 'RED';`), src.html:713-716 (no
  upper limit on yellow), src.html:1216 ("Never stopped").
- What: the ambulance check only asks "is the light RED at 43.0 s". Change job 5's rule 2 from "been 3 s" to "been
  10 s" (no ambulance rule at all): YELLOW 38.5 to 48.5, every goal check passes, "Job complete", and the Ambulance
  stat reads "Never stopped". On the street the ambulance is stopped behind a queued car from 42.5 s to past 50 s
  (x = 0.275, `stopped` true each beat): the driver model stops cars more than 2 s from the line on yellow. The
  readout lies, and the job's whole lesson (an ambulance rule placed at the top wins) is skipped by a cheap tweak a
  grade 3 student will find by sweeping chips. The same 10 s yellow also passes job 4 (j4_yel in sim-out.json).
- Also: the spec's own source (MUTCD 4D.26) gives a 6 s maximum yellow, but the tool never flags a long yellow.
- Better: decide "Had to stop" from the ambulance itself (any beat with the ambulance `stopped` while
  `ambulanceUntil` is live), and add a "Yellow too long" unsafe kind (over 6 s, MUTCD 4D.26) so a long yellow is
  reported with its rule. Re-run the job 5 worked checks after.
- Seen: sim-out.json `j5_yel10` (passed true, amb false); amb-out.json `yel10` trace.

##### 2. Two of the three codes ask for sequence and iteration the student never writes (should fix, general)
- Where: module codes E3-ALG-PS-01, E3-PRO-PD-04, E3-PRO-TR-08; notes.md:77 ("practiced directly").
- What: all three grade 3 codes name "a combination of sequence, events, iteration, and selection" (ALG-PS-01:
  create an algorithm with that combination; PD-04: develop code from a student-created algorithm with it; TR-08:
  debug a program with it; wording checked in the CSTA-based BootUp alignment PDF, csteachers.org). The student
  authors selection (rule cards) and uses events (button, ambulance detector). Iteration is the engine's fixed
  half-second check, never written or changed by the student; sequence only emerges from rules as the light cycle.
  The tool teaches selection, events and debugging very well; the "combination" part is mostly mentioned.
- Better (rule 2, no thin activity): either make the existing structure explicit where the student already sees it
  (Step and the panel foot named as "one time round the loop", the job 1 and 2 fixes framed as building the
  GREEN, YELLOW, RED, WALK sequence out of rules, and notes saying honestly which part each code gets) and confirm a
  sibling grade 3 tool covers authored loops and sequences; or note in the spec that ALG-PS-01 and PD-04 are shared
  with a tool where the student writes the loop. Notes.md:77 should not claim the codes are "practiced directly" as
  written today.
- Seen: standard texts vs. src.html controls; no control edits the check cycle.

##### 3. Rush Hour's missed-goal report gives a grade 3 student no rule to look at (should fix, family:robot)
- Where: src.html:839-844 and 1218-1220 (order note only when rule 4 already has "been 10 s"); job 4 in spec.
- What: job 4 needs two changes, one of them moving a rule. With only "been 30 s" added (the natural first try,
  and what the brief "long greens" invites), the report shows "Reds under 45 s ✕, Longest red: 63 s" and nothing
  else: no rule number, no order line. The cause (Rule 3 starting WALK four times while the light stays red) is
  only visible by reading the ribbon chips. Solo student (rule 4) is likely stuck here; this is the spec's own open
  question.
- Better: for a failed fairness check, name the rule that fired most during that stretch ("Rule 3 started WALK 4
  times in a row while cars waited 63 s"), the same "Rule N did it" pattern the unsafe lines already teach. Or
  settle the open question by spacing job 4's walkers so one change is enough.
- Seen: sim-out.json `j4_30only` (order false, orderRule shown nowhere for this case).

##### 4. Talk question teaches the wrong rule (should fix, general)
- Where: notes.md:51 "Why can a rule at the bottom never get a turn even when its condition fits?"
- What: false as written. A bottom rule fires whenever no higher rule fits: job 1's fix passes with the new rule at
  the bottom (sim `fix1bot`, Rule 4 turns YELLOW at 5.5 s). The point is "when a higher rule fits at the same check".
- Better: "Why can a rule lower down lose its turn even when its condition fits?" or add "when a rule above it fits
  too".

##### 5. Order line names "changed the light" for a rule that started WALK (polish, family:robot)
- Where: src.html:843 and 1219.
- What: in job 4 with rule 4 changed but left below rule 3, the report says "Rule 3 changed the light first. Rules
  are checked from the top." Rule 3 starts WALK; it does not change the car light. A student scanning for the rule
  that changed the light will look at the wrong cards.
- Better: "Rule 3 fit first and started WALK. Rules are checked from the top."
- Seen: sim `j4_r4below` (order true, orderRule 3).

##### 6. Goal card uses ≥ and < for grade 3 (polish, general)
- Where: src.html:941-942 ("green ≥ 30 s; red < 45 s; walker wait < 60 s").
- What: ≥ is not grade 3 notation, and the goal checks in the report already say it in words ("Greens at least
  30 s", "Reds under 45 s"). Two wordings for one rule.
- Better: "Model limits: greens at least 30 s, reds under 45 s, walkers wait under 60 s." matching the report.

##### 7. Job 5's starting report points at order before any second rule exists (nit, family:robot)
- Where: src.html:1218-1220 with job 5's starting rules.
- What: "Rule 1 changed the light first. Rules are checked from the top." shows when no ambulance rule exists yet, so
  nothing competed. It is in the spec and is true, but "first" suggests a contest. "Rule 1 turned the light yellow
  at 38.5 s, so the ambulance met a red." would say what happened.

#### Checked and clean
- Done when 1 and 3: worked checks hold to the half second (sim-out.json): job 1 fixed Y 5.5, R 8.5, WALK 9, GREEN
  26.5; job 3 unfixed GREEN 18.5 "Green while crossing" x3; job 4 unfixed WALK 7, 24.5, 42, 59.5, 77, red 86.5;
  "been 30 s" only red 63; rule 4 only greens 0.5; both Y 30, R 33, W 33.5, G 51, Y 81, R 84, W 84.5, longest wait
  41.5; job 5 unfixed Y 38.5, R 41.5, had to stop; top rule Y 46, WALK 49.5.
- Done when 2: each start fails for the table's reason (job 1 0 of 3 crossed, job 2 three "Yellow too short", job 3
  three "Green while crossing", job 4 green 3.5 and red 86.5, job 5 had to stop); each listed fix passes.
- Done when 4: all three unsafe kinds caused on purpose in Watch the Street, each with words and rule number in the
  Watch out line and hazard tag (frames/watch-*.png; "Green while crossing" shows a car driving into the walker, a
  strong moment).
- Done when 5: ambulance rule at the bottom fails with `order` true (line 14); at the top passes.
- Done when 6: replay pauses on the named rule (audit state-replay-1366x768.png); "never fired" tags (audit
  state-job-report-1366x768.png).
- Facts: MUTCD 2009 yellow 3 s minimum (4D.26), walk 7 s, 3.5 ft/s clearance, 35 ft / 3.5 = 10 s (4E.06), all as
  cited; fairness limits labeled as the tool's own. Notes "Good to know" matches the code.
- No hidden-information mode; job briefs guide without stating the fix except job 2 (fine for a builder job).
- Support at home ideas are doable tonight; Key skills are true of this tool. No sensitive topic for rule 8.
- Nothing cultural, Native or hard-history. The three walker images are people art (rule 11, Cory's sheet), not a
  sensitivity item.

#### Audit pilot
- Leads confirmed: none bear on teaching; the 375 and 760 fold leads are layout (Play/Craft).
- Leads wrong: none checked as wrong from this lens.
- Missed (outside what it can see): the job 5 "Never stopped" readout that lies under a long yellow (finding 1), the
  standards gap (2), the silent fairness miss in job 4 (3) and the false talk question (4).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: traffic-light-coder (Codex fix, round 1)

Curiosity override: the user's instruction and CODEX-CURIOSITY.md win over the legacy lesson spec
and Refine's "Not a Curiosity" settled call. Kept the crossing, painted assets, rule engine,
traffic scripts, timing and replay. Replaced jobs with freely selectable setups and observations.
Removed the kit header/CSS, goals, check badges, completion state, Next job and finale.
Added the lower-left Manual, engraved family plate and instrument power panel. No number was
invented: neither the supplied spec nor CURIOSITIES.md assigns this tool a Curiosity number.

Evidence is in `_scratch/traffic-light-coder/`, including `before-src.html` and `before-notes.md`.

#### Blocker

1. **FIXED, with the Curiosity override.** Reproduced all three cheap yellow programs in the
   browser before repair: `before-numbers.json` (10 s and 30 s) and `before-third-cheat.json`
   (YELLOW plus ambulance KEEP above the normal yellow rule). All reported success and
   `ambulanceStopped:false` despite stopped vehicle frames beginning at 42.5 s. The result now
   latches the ambulance's own stopped flag each beat until it clears the crossing, including
   queues after detector expiry. `final-numbers.json`: all three true, stop at 42.5 s; original
   setup true; top priority rule false. `additional-cheats.json`: bottom priority rule true.
   `fix-final-detail/final-stopped-ambulance.png`, 1366x768, shows Had to stop, 42.5 s, Rule 1.
   No goal or completion claim remains. The original half-second worked light changes hold. The post-audit any-vehicle check is in `two-ambulances.json`.
2. **FIXED, with the Curiosity override.** Reproduced deletion of rule 4: legacy success,
   longest red 81.5 s (`before-numbers.json`). The record now retains each red's next state,
   distinguishes a still-open red from a return to GREEN, and has no success grade. Internal
   `carsReturn` additionally requires every red to end in GREEN within the existing 45 s model
   reference. Re-ran 64 single edits: before, 12 unsafe/broken or valid variants earned success;
   after, only `extra-3-done` meets safe + everyone crossed + carsReturn (`final-numbers.json`).
   Original starting rules still give three Green while crossing moments; DEFAULT has none and
   carsReturn true. `fix-after/after-held-red.png`, 1366x768, shows the 81.5 s held red without
   congratulation; the later record wording explicitly labels the interval still open. Notes updated.

#### Should fix

3. **FIXED, adapted to setups.** `fix-before/before-jobs.png`, 1366x768, had only title and goal.
   Each setup now has a persistent, plain problem line, and its waiting hint repeats that
   observation plus Tap a rule / Run script. No solution is disclosed. `fix-final/final-setup-1.png`
   through `final-setup-5.png` show all five at 1366x768; held Read evidence is `voice-side.json`.
4. **FIXED.** Reproduced the false changed-the-light attribution in `fix-before/before-order.png`,
   1366x768. Ambulance cause now says Rule N fired first. Rush Hour names WALK requests rather
   than a car-light change. `fix-final-detail/final-order-below.png` and
   `final-stopped-ambulance.png`, same size, show the corrected causes.
5. **FIXED.** The 30-only variant had longest red 63 s and `order:false`, so no cause sentence
   (`before-numbers.json`, j4_30only). Counts now come from actual firings in the longest red.
   `fix-after/after-order.png`, 1366x768: Rule 3 requested WALK 34 times, four actual new walks,
   while cars waited 63 s. `final-order-below.png` confirms the same attribution with the timed
   return rule still below WALK. WALK requests during an active walk remain honest no-ops.
6. **FIXED.** At 760x900, before Add rule was y=1017.98..1061.98, outside the viewport
   (`fix-before/before-760.png` and drive output). Side-by-side compact cabinet now keeps it
   y=364..408 in Setups (`fit-760.json`, `fix-behaviour/after-760-setups.png`). Live Add rule
   also fits. The 375-wide page remains stacked.
7. **FIXED.** Reproduced the hidden sentence / generic tabs at 1366x768 and 680x425:
   `fix-before/before-picker.png`, `before-picker-680.png`. The picker now shows the live rule
   sentence, current tab values and updates them after every choice; focus stays on the chosen
   option. `fix-final-detail/final-picker-1366.png`, `final-picker-680.png`; latest dialog with
   its own explicit Read control: `fix-contacts/picker-actions.png`, 680x425, and
   `fix-last/phone-picker-fixed.png`, 375x812 host.
8. **FIXED.** Reproduced the 60 px buttons over the crossing/stop areas in
   `fix-before/before-buttons-680.png` and `fix-phone-models/before-phone.png` (375-wide host).
   Compact buttons now occupy the outer sidewalk corners with 44x44 hit areas. At 680x425 the
   south button is x=332.45..376.45, clear of the central crosswalk and stopped traffic;
   at 375x812 it is x=316.48..360.48, y=181.47..225.47. Evidence: `layout-680.json`,
   `phone-fixed.json`, `fix-last/phone-street-fixed.png`, `fix-behaviour/after-680-fit.png`.
   The 1366x768 60 px positions are retained. Phone street now precedes the editor.
   Final compact text is 10 px and the decorative label is hidden; see `fix-audit-followups/`.
9. **FIXED by removing the goal card.** Reproduced symbolic goal language in
   `fix-before/before-rush.png`, 1366x768. Fair-time references are now plain words in the
   Manual and labelled this tool's own. Empty red is Cars stopped with nobody crossing in the
   record. `fix-final-detail/final-order-below.png`, same size; `fix-last/manual-fixed.png`
   demonstrates the usable Manual at 680x425. No goal was added.
10. **FIXED with the Curiosity voice rule.** `before-voice.json` reproduces the spoken Add rule
    instruction behind the picker. The old line and job speech are removed. Picker hint and its
    explicit Read now say Pick a chip, then press Done. Read is inside the native dialog, so it
    is usable there. After Done the normal hint offers Add rule. Latest `voice-main.json` has
    the curb hint once and exactly two deliberate picker Reads; `allLines()` equals lines.json.
    No automatic picker speech was added. The legacy spec line table is preserved as history;
    it is superseded by the Curiosity rule and the matching runtime/voice table.
11. **FIXED.** Reproduced the false absolute in `before-notes.md`: bottom rule can never get a
    turn. Current notes ask why a rule lower down can lose its turn. The original lower-rule
    behavior is retained; priority only matters when a higher rule also matches.
12. **FIXED within scope.** Reproduced practiced directly in `before-notes.md`. Current notes
    identify authored selection, used events, indirect sequence and inspected fixed iteration,
    rather than claiming full direct coverage. The panel foot names the half-second loop;
    Step's accessible name and Manual do too. The first two setup notes describe constructing
    GREEN, YELLOW, RED, WALK transitions from rules. `fix-contacts/after-1280-fit.png` and
    `fix-final/final-live-1366.png`; keyboard rule edit is in `keyboard.json`. Module reassignment
    stays an owner decision outside the allowed write scope.

#### Polish accepted

13. **NOT APPLIED, Curiosity override.** No all-five-jobs finale, dots, completion state or finish
    screen was added. The legacy completion machinery was removed. Every setup remains available.
14. **FIXED.** Compact restore button reads Defaults; Reset street keeps its circular arrow.
    `fix-behaviour/after-680-fit.png`, 680x425.
15. **FIXED, exploratory hint only.** After the first full return to green, a quiet hint invites
    a different action on rule 1 and another curb press. No goal or repeated speech.
    `cycle-hint.json`, `fix-behaviour/cycle-hint.png`, 1366x768; GREEN returned at 22.5 s in that run.
16. **FIXED.** Chips and rule words compute to 14 px at 1366x768 (`additional-cheats.json`).
    Six rules retain the permitted internal scroll, while Add rule and edit controls stay visible:
    `fix-final-detail/final-six-1366.png`. Four-rule cards fit without that scroll.
17. **FIXED.** Options retain words and use actual lamp colors. Turn actions add an arrow.
    `fix-contacts/picker-actions.png`, 680x425: arrow-dot colors rgb(31,157,85),
    rgb(242,183,5), rgb(217,58,43). Current values also remain in the sentence and tabs.
18. **FIXED.** Every scripted observation endpoint focuses `#record-heading` with preventScroll.
    The record is a section, with the false dialog role removed.
    `fix-final-detail/final-unsafe-680.png` and drive result `focus:record-heading`, 680x425.
19. **FIXED.** The setup card's pseudo-element tab is removed. All five setup frames at 1366x768
    and the compact unsafe record frame show no grey drag-handle tab.
20. **FIXED.** Firing tape includes G, Y, R or W inside the dot beside each rule number.
    `fix-behaviour/grayscale.png`, 1366x768, and `fix-last/phone-street-fixed.png`, 375-wide host.

#### Settled calls

- Applied: no fourth unsafe kind; no walker spacing or Rush Hour timing change; six-rule internal
  scroll and the 375-wide stacked page retained; unsafe green-while-crossing replay retained.
- Applied cause/wording priorities. Third-setup return-to-green is an observation/diagnostic,
  not a newly added goal check. No curriculum/module file was edited.
- Rejected only the settled statement Not a Curiosity and all implied lesson requirements,
  because the user's explicit instruction takes precedence. Existing people art is unchanged.
- The initial curb hint may be cut by action; its instructions remain visible and available to Read.

#### Cheats tried

- Yellow 10 s, yellow 30 s, and YELLOW/ambulance KEEP above the normal yellow transition:
  all originally lied; all now report the observed stop at 42.5 s. Top priority keeps the
  ambulance moving; the same rule at the bottom reports its actual stop.
- Deleted return-to-green rule: 81.5 s red, now explicit, with no success/advance/finale to earn.
- Replaced RED return with YELLOW: six red intervals end in yellow; internal carsReturn false.
- Put ANY/KEEP first: walkers remain waiting; the record exposes that stall, with no reward.
- Expanded the 64-case probe to 96 edits, 77 distinct programs (`before-96.json`, `after-96.json`).
  Before, 16 edit attempts earned success. After, only replacing or augmenting the return rule
  with done yields safe crossings, every walker across and timely green returns (two valid programs).
- 100 presses per curb create two waiting manual walkers total, not 200 (`extremes.json`).
  One Step advances exactly 0.5 s. Empty program observes 0 of 3 crossed at the 120 s cap.

#### Voice walk

- Held clicks, 0.12 s holds, 2 s gaps. `voice-main.json`: initial curb hint spoken once;
  Pick a chip, then press Done read twice, only on the two deliberate dialog Read presses.
- Side path: setup problem/next action on Read, then observational record instructions on Read
  (`voice-side.json`). No job welcome, success/failure event or finale. Curiosity's voice rule wins.
- Three bank lines exactly equal `allLines()`. Existing browser fallback is retained; no new recording.
- Keyboard: edited rule 4 from timed condition to walk is done, escaped the picker and returned
  focus to rule 4 (`keyboard.json`). Record focus is checked separately at the endpoint.

#### Engine changes wanted

No tool engine change required. Audit limitation: `scripts/audit_tool.py` `MODES_JS` detects only
header mode groups. A future shared audit update should include instrument `[role=group]` mode
selectors outside a header. This run uses explicit audit states and held setup input instead;
no header was added to satisfy the auditor and no shared script was edited.

#### Audit

The single 40-minute-limited audit finished: `fix-audit/audit.md`, 92 frames, 581 leads.
No console/runtime errors, infinite Motion-off animation, resize exceptions or stuck controls.
Every lead has an indexed disposition in `audit-responses.md` and `audit-response-index.json`:
115 repeated rows fixed through four causes; 466 accepted as intentional opaque overlays,
the specified phone/six-rule scrolling, or permitted first-hint skips/cuts. No unreviewed row remains.

- Fixed decorative label/curb overlap in compact sizes, preserving the street art and hit areas.
- Fixed 9 px curb text and record headers to 10 px. `fix-audit-followups/audit-fix-680.png`
  through the 800/1000/760 frames and `audit-record-font.png`; Back to rules ends at y=352.19
  in the 680x425 record, above the power row at y=377.
- Fixed the phone's power-panel occlusion at its cause: the 375x812 scrolling work area now
  ends at y=698 and the separate 114 px power row begins there. A scrolled Add rule ends at
  y=637.47; a focused rule ends at y=446.47. `phone-scrolled-rules.png`, `phone-focused-rule.png`
  and `post-audit-verified.json` prove the controls remain above the panel.
- Also guarded the initial hint while Manual is open (`manual-first-voice.json`: no speech),
  and checked two ambulances together: the second vehicle's stop is latched at 0.5 s even
  while the first keeps moving. Original ambulance setup still stops; top-priority setup does not.
- Matched privacy copy to `kit/curio.js`: only Motion persists; Sound and rules are page-lifetime.
  Removed an unnecessary, unconfirmed publication year from the secondary-source reference.

The audit used the frozen `audited-src.html` / `audited-bundle.html`. The four new causes and
small follow-ups were then rechecked in one focused 11-shot drive, zero errors, and visually
inspected. The full audit was not repeated. Final bundle: 451,208 bytes; hashes in `validation.json`.
No external resource attributes or HTTP resource entries in the instrument. Chrome and host
ports 9920..9927 and 8725 are closed (`port-cleanup.json`).

#### The real material

- FHWA MUTCD 2009 4D.26, 4D.27: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4d.htm
- FHWA MUTCD 2009 4E.06, 4E.08: https://mutcd.fhwa.dot.gov/htm/2009/part4/part4e.htm
  Public domain, explicitly stated at https://mutcd-dr.fhwa.dot.gov/knowledge/faqs/faq_general.htm.
  Fetched 2026-11-06; originals and record in `data/`. Historical timing facts only, no traffic dataset.
- Independent cross-check: Minnesota DOT Traffic Signals 101 Course Manual,
  https://www.dot.mn.gov/trafficeng/signals/docs/signals-101-manual.pdf. Reference only;
  no text, figures or dataset incorporated. It confirms 7 s WALK, 3.5 ft/s clearance example and
  roughly 3..6 s yellow guidance. No current engineering-compliance claim is made.
- `verify_sources.py` recomputes 35 / 3.5 = 10 s. Half-second loop, fixed-speed driver,
  two-second yellow decision, traffic scripts and fairness references are original Curio Class
  model choices: content CC BY 4.0, code MIT. No external traffic dataset was needed.
- Existing twelve OpenAI-generated illustrations retained, including all three marked people assets.
  Sources/licences are also in the Manual and tool.draft.json. CSTA identifiers remain reference-only
  in notes; no standards text or Code.org glossary wording is incorporated.

#### Curiosity check and frames

The crossing is the working material: a curb press changes lamps, moving traffic and the firing tape.
A child can poke it without reading; an adult can explore priority, timing and the detector. The real
first-match controller is central, with explicitly simplified traffic. It works without a score or
finish line. These are assessments from the repair walks, not evidence of a separate timed ten-minute
student/adult study. The original art is preserved; the cabinet has its own controls and finish.

| Traffic Light Coder | Beat Lab reference, opened and played |
|---|---|
| ![Street controller](../../_scratch/traffic-light-coder/fix-latest/latest-default.png) | ![Beat Lab](../../_scratch/traffic-light-coder/fix-phone-models/model-beat-lab.png) |

Looked at all targeted before/after frames directly or on `fix-contacts/` contact sheets, including
every standard size, all five setups at 1366x768, held input, picker, records, replay, zero/six rules,
Motion off and grayscale. Beat Lab was played; Elements Inspector was opened and searched. All 92 audit frames
were also inspected on the 12 `fix-audit-contacts/` contact sheets, plus the 11 focused follow-up frames.
Source and voice lesson-creep searches have zero matches; src.html has no header or em dashes.
Computed text contrast from the actual CSS: ink/panel 12.83:1, muted/panel 5.17:1, plate 6.23:1,
power 11.03:1, firing letters at least 4.57:1 (`contrast.json`, original code/CSS, MIT).
The idle/live browser measured 60 fps (`fps.json`); this is this machine, not a Chromebook benchmark.

#### Left open

- Owner assignment of the Curiosity number; the maker's plate omits an unassigned number and metadata plate is null.
- The legacy spec, its voice table and Done when ladder are not rewritten; conflicting lesson requirements are
  explicitly superseded here. The module's combined standards coverage needs the owner decision described in notes.
- No separate timed ten-minute student/adult study, Chromebook hardware run or fresh people-art review was performed.
- Accepted Polish 13 is intentionally omitted. No new Yellow too long unsafe kind or walker-spacing change.
- One earlier phone harness requested its own missing favicon, producing a host 404; that was a harness issue.
  The corrected host has a data favicon, and the final phone drive has zero errors. All tool resources are bundled.
- No commits, no refine.md edits and no shared-engine/docs/other-tool edits. Every substantive command after setup
  used the Scratch timeout wrapper: bundle 120 s, drive 300 s, audit 2400 s; downloads 15 s each.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Traffic Light Coder Curiosity fix handoff

#### Structure

The user's 2026-11-06 Curiosity instruction supersedes the lesson-shaped spec and Refine.
The street, all twelve existing painted assets, robot-family program/runner and half-second
model remain. The source owns its instrument CSS; it no longer loads kit/curio.css or a kit header.
Motion, Sound, Read and voice still use kit/curio.js. Only Motion persists between visits; Sound is page-lifetime state. No shared file changed.

Live street is open-ended. Setups selects any of the five original traffic scripts, without
progression or completion state. The street record is observational telemetry, not a grade.
It preserves actual light intervals and unsafe-moment replay. The lower-left Manual contains
controls, readouts, exploratory findings, model assumptions, privacy and source licences.
No Curiosity plate number exists in the supplied spec or concept list. The engraved maker's
plate therefore uses the family name and tool name without inventing a number.

#### Tricky parts

`makeWorld`, `when`, `execute` and `tickWorld` hold the original model. `summarize` now returns
observations only. `ambulanceStopped` is latched from the vehicle's stopped flag each beat
until the ambulance clears the crossing, including queues beyond the detector window.
`ambulanceStopAt` anchors the cause line to actual light history. Long yellow holds are covered.

Red intervals retain their next state, or null if still open at the observation endpoint.
`carsReturn` is an internal diagnostic requiring each red to end in GREEN within the existing
45 s tool reference. It never grades the user. An open interval is explicitly labelled open.
The dominant rule during the longest red is counted from actual firings, distinguishing
WALK requests from new walks. A request during an active walk does nothing, as before.

The robot runner restarts scheduling after a live program edit and halts a scripted run on edit.
The picker redraws the sentence and tabs after a change and restores focus to the chosen option.
Each script record focuses its heading with preventScroll. The record is a section, not a
non-modal dialog. The true picker and Manual use native modal dialogs.

#### Voice

`voice/lines.json` equals `allLines()`. The three strings are the initial curb hint, the explicit
Read response in the picker, and the six-rule capacity line. Only the initial hint may speak
automatically. Every other utterance follows Read, as required for a Curiosity. Old job briefs,
success events and finale are removed. Browser fallback remains; this session records no audio.

#### Verification

Scratch holds original source and notes, before/after numerical checks, 64 single-edit variants,
same-size frames, real held-input voice walks, keyboard edits, source downloads and the final audit.
See polish.md for item-by-item dispositions and the measured limits of the verification.
`verify_sources.py` preserves the public-domain federal originals and recomputes 35 / 3.5 = 10 s.
No outside traffic dataset or executable was downloaded. Existing people art was not changed;
the standing people-art desk review is unchanged.

#### Engine changes wanted

None required. The existing local instant-advance loop uses the same matching, execution and
tick functions as the family runner. No engine change was made.

#### Left open

Owner assignment of a Curiosity number and the legacy module's combined standards coverage.
No new unsafe kind, walker spacing change, external submission, commit or shared-file edit.

#### Fix verification complete, 2026-11-06

The single audit completed with 92 frames and 581 indexed leads. Four layout/type causes
were repaired and re-shot in an 11-frame focused follow-up; intentional opaque overlays,
permitted scrolling and Curiosity first-hint behavior are indexed as accepted. Resize stress
finished without exceptions or stuck controls. No full audit was repeated.

The 96 single-edit attempts (77 distinct programs) leave only the two done-condition repairs
with safe crossings and timely green returns. All three long-yellow shortcuts now expose
the actual ambulance stop. A two-ambulance probe verifies any stopped vehicle is observed.
Phone focus and scroll use a work viewport above the power row. Compact text is at least 10 px.
Final bundle is 451,208 bytes; validation.json holds hashes, source/voice searches and metadata.
All started Chrome and host ports are closed. No refine.md edit or commit was made.

Optional audit improvement: scripts/audit_tool.py, MODES_JS, recognize instrument mode groups
outside header as well as lesson headers. Explicit audit states and a held Setups walk cover
that blind spot here; no shared script was edited to accommodate this Curiosity.

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
