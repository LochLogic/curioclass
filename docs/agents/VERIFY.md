# Verify agent brief

You check ONE freshly built Curio Class tool, cold. You did not build it and you owe it nothing. Your job is to find
what is wrong before Cory does. Do not fix anything: report.

## Read

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

## Report

A verdict (PASS, or FIX with the list), then each finding as: where (file:line or mode), what is wrong, how you saw
it (the frame or the check), how serious (blocker / should fix / nit). Nothing else. Don't pad a short list.
