# Traffic Light Coder build handoff

## Structure

`src.html` starts from the kit starter and contains its palette, responsive street and workbench,
then the half-second model, robot-family integration, reports, replay and chip editor.
`makeWorld`, `when`, `execute` and `tickWorld` contain the model. `summarize` performs goal checks.
The same model drives live runs, skip-to-report and the reviewer simulation hook.
`Robot.program`, `Robot.strip` and `Robot.run` supply the family model, editing list and first-match runner.
No shared engine or other tool was changed.

The tool owns the hint. `Curio.voice` manages welcomes, once-only briefs and repeated result events.
The 16 lines use firm-captain / Alnilam metadata; no audio was recorded, per the build brief.
Browser speech is the offline fallback. Art is embedded with `art:` tokens by the standard bundler.

## Open questions resolved for this build

- Keep Rush Hour's specified two-part fix and 10-second-spaced walkers. It teaches timing and priority together;
  the independent calculation reproduces why either change alone fails. The starting traffic script is unchanged.
- All three walker assets are now painted with OpenAI image generation and marked `people: true`.
  The overhead children match the street palette and show varied skin tones and hair; their facing follows their curb.

## Tricky parts

Presses and sign-interval endings are ingested after that half-second's rule evaluation, so the rule sees them
on the following check. Color changes happen during evaluation. Time checks use time in the current color.
A WALK request during an active walk is a no-op but still fires. Repeated manual taps represent one waiting walker.
Red duration includes an unfinished red at test end; shortest green excludes an unfinished green.

The robot runner stops on a program-generation change. Live edits restart its scheduling while retaining the
street world; job edits stop the test. No test silently changes its program while running.
Report replay reads frozen half-second snapshots and leaves the editable rules beside the street.
All job programs and completion dots are page-lifetime state only.

## Engine changes wanted

Optional: in `kit/robot.js`, `Robot.run`, add a bounded `finishNow(limit)` for rules runs that invokes
the same matching, execution, tick and trace path without waiting between beats, with the existing
generation guard and one end callback. Skip to report currently uses a small synchronous matching loop
because the engine has no instant-completion path. The live street and normal tests use the engine.
No engine file was changed. Local CSS positions its card action buttons in a fixed workbench row.

The tool's beat callback uses an absolute deadline so rendering costs do not accumulate in a 120-second test.
Skip, Next job and Replay deliberately move focus to the new available control with `preventScroll`.

## Evidence and next handoff

Build evidence lives in `_scratch/traffic-light-coder/`. `spec-numbers.py` independently recomputes the spec examples,
14 program variants and contrast ratios. Browser checks, screenshots and audit findings are documented in
`codex-report.md`. The next stage is the separate cold review; this build does not start a polish round.

## Build verification complete, 2026-10-31

All five jobs were solved with held real input; jobs 4 and 5 also ran for their full test lengths.
Job 3 was solved with keyboard input only. Fourteen browser program variants match the independent Python model.
The full audit completed with 111 leads. `audit-responses.md` in Scratch answers each one: 49 fixed,
62 accepted as narrow scrolling or the specified first-tap welcome behavior. The full audit was not repeated;
focused follow-up checks cover the fixes. All 81 audit frames and all build screenshots were inspected.

Final focus destinations are Back to rules after Skip, Back to report during Replay, and Run test after Next job.
Compact job buttons and live test controls are at least 44 px. Report choices fit at 680x425 and 760x900.
The priority-conflict narration requires a competing ambulance rule, and a failed test never announces the all-jobs success.
Yellow driver decisions are kept for the whole yellow interval. Rendering does not accumulate in the test clock.

The 120-street-second cap measured 30.027 real seconds in Chrome, including scheduling and drawing overhead.
The final validation manifest in Scratch records the bundle hash and size. Chrome and host processes are closed.

The cold review replaced `walkerSVG` with the three keyed cutouts in the hidden asset bank.
Final prompts and provenance are in `art/prompts.json`; raw originals are in `art/raw/`.

## Cold review changes, 2026-11-03

Preserved the street, vehicles, signal art and model timing. Added three painted overhead walkers with
correct facing, replacing the temporary silhouettes. Full prompts use the built-in imagegen tool;
finished cutouts use only `art.py --rekey`. Contact sheet is in Scratch.
The report now draws actual car-light intervals with words and patterns, and fits its content to keep
some street visible. Narrow screens put the hint and live test controls before the street, with rules below.
Paused calls name Step and Play. Ambulance report attribution uses a recorded light change and never Rule 0.
Independent review calculations match 14 browser programs. Keyboard-only Job 3 passes.
Narration remains the existing browser fallback; the review does not record audio.

## Cold review audit and close

The single review audit completed within its 40-minute limit: 79 leads, no console errors,
clean repeated speech and rapid taps, and clean resize stress. Indexed responses are in
`_scratch/traffic-light-coder/review-audit-responses.md`.
Confirmed compact unsafe-report overflow is fixed. All three replay buttons and Back to rules
fit at 680, 800, 1000, 760 and 375 widths. Compact unsafe reports use their replay chronology;
the new light strip remains on the flat safe/missed-goal reports and on roomy unsafe reports.
Narrow test controls remain visible while rules are scrolled. The display:contents aside
uses visible overflow so its zero layout rectangle does not mislead clipping checks.
Ambulance attribution now uses the red-light cycle active at arrival, verified with an earlier-cycle
regression and the standard Rule 1 case. Eight targeted re-shoots passed without console errors.
No second full audit was run. Narrow stacked pages still require vertical scrolling;
five/six-rule lists retain the internal scrolling allowed by the spec.
The final validation manifest records the reviewed bundle. No shared files or commits were made.
