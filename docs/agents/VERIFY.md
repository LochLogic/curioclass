# Verify agent brief

You check ONE freshly built Curio Class tool, cold. You did not build it and you owe it nothing. Your job is to find
what is wrong before Cory does. Do not fix anything: report.

## Read

0. `docs/agents/STANDARDS.md`: standing rules; check the tool against every one of them.
1. `tools/<tool-id>/spec.md` (what it must do) and `docs/POLISH.md` (how it must feel).
2. `tools/<tool-id>/src.html`, `notes.md`, `art/prompts.json`, `voice/lines.json`.

## Check

1. **Spec:** every mode, button and content item in the spec exists and behaves as written. Test each "Done when".
2. **Play it:** `CURIO_DRAFT=1 python scripts/bundle_tool.py <tool-id>`, then `python scripts/shoot.py` frames of the
   default screen, every mode, the extremes (smallest and largest values, empty states, the end of a round) and a
   narrow window. Look at every frame: overlaps, clipping, text over art, unreadable sizes, placeholder art in odd spots.
3. **Facts:** every number, date and claim on screen or in notes matches the spec's Sources. Flag anything unsourced.
4. **Contract:** one file, no network requests, kit used (not re-implemented), keyboard and focus, 44 px targets
   (60 px for K-2), color never the only signal, Motion and Sound and Read work.
5. **Lines:** every line the tool speaks is in `voice/lines.json` and `allLines()`, word for word.
6. **Art:** every `art:` token has a prompts.json entry, people are marked `people: true`.
7. **Words:** no em dashes, "Curio Class" never "Curio" alone, plain grade-level language, nothing that gives an answer
   away in a predict or quiz mode.
8. **Guardrails:** K-2 teacher-led; hard history has no points, timers or win states; health topics are neutral.
9. **Voice balance:** repeat each action five times with held clicks and count spoken lines in `vlog`: each how-to line
   once, each event line (praise, a result) every time. Check every spoken line against what the screen shows then.
   Use the standard voice check below.

## Standard voice check

Drive it with `scripts/drive.py` and held clicks (`"hold": 0.12`, a `"gap"` longer than the lines), Sound on, Motion on.
Read the log after each run: `__tool.vlog` (on `Curio.voice` it is `V.log`, with `as` = spoken, silent, dropped or read).

1. **Repeats:** each action five times in a row. Count how often each line is spoken. How-to and teaching lines: once,
   then `silent` (the hint still shows them). Event lines (praise, results, failures, "that code doesn't work"): five.
   A result that goes quiet after the first time fails, and so does a how-to that comes back after every tap.
2. **Stale lines:** tap fast (gap about 0.2 s) through two or three actions, then switch mode and Reset. No line may
   play after its moment has passed: compare each spoken line with the frame at its time. A line naming a control that
   is hidden or off must not play.
3. **First-tap timing:** one fresh page per kind of first tap: the stage, a control that speaks for itself, a mode
   button, Read, Sound, a key. Nothing speaks before the tap. A plain tap gets the welcome within about half a second; a
   control with its own line gets only that line; Read speaks the hint only; Sound says nothing. Then Sound off and on,
   or the next mode entry, must bring a skipped welcome, once.
4. **Read:** Read during a line stops it and speaks the hint, with Sound off too; nothing cuts Read off; a mode change
   right after Read lets the next line start at once.
5. **Order:** spoken lines follow the order of the actions; no line from an older action plays after a newer one.

Report the counts as a small table (line, kind, expected, spoken). On `Curio.voice`, the helper's own rules are covered
by `python scripts/test_voice.py`; the tool's job is choosing the right kind, `valid` and `needs` for each line.

## Report

A verdict (PASS, or FIX with the list), then each finding as: where (file:line or mode), what is wrong, how you saw
it (the frame or the check), how serious (blocker / should fix / nit). Nothing else. Don't pad a short list.
