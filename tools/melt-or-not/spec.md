# Melt or Not: spec (voice only)

This tool was built before specs lived beside the tools; the lesson plan is plan.md and the teacher notes are notes.md.
This file holds the voice spec added on 2026-10-26.

## One idea

Sort changes into "can go back" (melting ice, freezing juice) and "can't go back" (baking a cake, burning paper).

## Voice

`voice/lines.json`: `"bank": "clear-teacher"`, `"voice": "Iapetus"`, `"style": "Say clearly and kindly, like a patient
elementary school teacher"` (from voices/bank.json; no near neighbor uses clear-teacher). 46 lines, recorded with
scripts/localvoice.py by the integrator. The kit (kit/curio.js) plays a clip when the exact text has one and falls back
to the browser voice otherwise. Every line the tool speaks is a fixed line, so there is no planned browser-voice fallback.

- Welcome (once, after the first tap): "Welcome to Melt or Not! We will change things, then test if they can go back."
  A first tap on Read speaks the label first and the welcome after it.
- Feedback (narrated after each test, if the class is still on that thing when its turn comes): the thing's yes or no
  line, then its why line.
- Summary (narrated when all ten are sorted): "What did we find out?" then "Melting and freezing can go back. Cooking,
  baking and burning cannot."
- Read stops any speech and speaks the big label as fixed parts: "A slice of bread. What happens if we warm it up?"
  (one line per thing), then "Now it's toast." with "Can it go back to how it was?", or with "You predicted: it can (or
  can't) go back. Let's test it!", then the yes or no line and the why line, then the summary.
- Per thing: intro, "Now it's ...", yes or no, why (4 x 10 = 40 lines), plus 6 fixed lines.
- Queue (copied from collision-lab): lines are marked said when they start; Read and Start over drop lines that never
  started; nothing cuts Read off; Sound off silences narration (Read still speaks) and turning Sound back on queues the
  welcome if it was never said.
