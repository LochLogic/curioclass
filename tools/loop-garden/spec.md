# Loop Garden: spec (voice only)

This tool was built before specs lived beside the tools; the lesson plan is plan.md and the teacher notes are notes.md.
This file holds the voice spec added on 2026-10-26.

## One idea

Plant flowers with repeat blocks; fewer blocks earn more stars.

## Voice

`voice/lines.json`: `"bank": "hero-coach"`, `"voice": "Puck"`, `"style": "Say with bright, encouraging energy, like a
friendly superhero coach"` (from voices/bank.json; no near neighbor uses hero-coach). 27 lines, recorded with
scripts/localvoice.py by the integrator. The kit (kit/curio.js) plays a clip when the exact text has one and falls back
to the browser voice otherwise. Every line the tool speaks is a fixed line, so there is no planned browser-voice fallback.

- Welcome (once, after the first tap): "Welcome to Loop Garden! Help the bunny plant flowers." then the current garden's
  goal. A first tap on a garden button skips it (that garden's goal is said instead); a first tap on Read says only the
  welcome sentence after Read.
- Garden goals (once per garden per page load, when the garden is opened): "Garden N: name. goal" as one line, 8 lines.
- Run feedback (each run, if still showing when its turn comes): the two Bonk lines, the seed spots still left lines
  (one or some, no count), the free garden lines, and the win: "Three stars!" (or two, one), "All planted!", then
  "That's as short as we know how to make it!" or "Can you do it with N blocks?" (N is the garden's par: 3, 4, 6, 7 or 10)
  plus "Look for more blocks that repeat." or "Try a Repeat block."
- Templated speech was rewritten into fixed lines: the old "N flowers planted with M blocks!" and "N seed spots still
  need planting" counts are gone from speech and from the message (the block count stays on screen beside Program).
- Read stops any speech and speaks the message box (as its fixed parts), or the garden goal when there is no message.
- Queue (copied from collision-lab): lines are marked said when they start; Read, Reset and a garden change drop lines
  that never started; nothing cuts Read off; Sound off silences narration (Read still speaks) and turning Sound back on
  queues the welcome if it was never said.
