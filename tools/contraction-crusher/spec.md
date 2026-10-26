# Contraction Crusher: spec (voice only)

This tool was built before specs lived beside the tools; the lesson plan is plan.md and the teacher notes are notes.md.
This file holds the voice spec added on 2026-10-26.

## One idea

Smash two words together into a contraction; the apostrophe flies in where the letters fell out.

## Voice

`voice/lines.json`: `"bank": "warm-teacher"`, `"voice": "Sulafat"`, `"style": "Say warmly and clearly, like a kind
kindergarten teacher talking to the whole class"` (from voices/bank.json; no near neighbor uses warm-teacher; its only
other user is calm-corner, not a neighbor). 67 lines, recorded with scripts/localvoice.py by the integrator. The kit
(kit/curio.js) plays a clip when the exact text has one and falls back to the browser voice otherwise. Every line the
tool speaks is a fixed line, so there is no planned browser-voice fallback.

- Per pair (21 pairs, 63 lines): the sentence with the two words ("I do not like getting wet."), the sentence with the
  contraction ("I don't like getting wet.") and the change ("Do not becomes don't."). Sentences that start with the
  words are capitalized, as on the strip.
- Fixed (4 lines): the welcome ("Welcome to Contraction Crusher! Tap the letters you think will fall out, then press
  Crush."), the question ("Which letters fall out when the two words squish together?"), "You got it!" and "Not quite.
  Look where the gap is."
- Welcome: once, after the first tap (not when the first tap is Crush, which says its own result; after Read it waits
  for Read).
- Feedback (narrated after each crush, if those words are still crushed when its turn comes): "You got it!" or "Not
  quite. Look where the gap is." when letters were marked, then the change line and the new sentence.
- Read stops any speech and speaks the sentence and the question before a crush, or the change line and the new
  sentence after it. A Made today shelf button speaks its change line (only with Sound on, as before).
- Crush stops any speech, as before. The old speech said the pair lowercase and joined ("do not. don't."); it is now the
  fixed change line.
- Queue (copied from collision-lab): lines are marked said when they start; Read and Crush drop lines that never
  started; nothing cuts Read off; Sound off silences narration (Read still speaks) and turning Sound back on queues the
  welcome if it was never said.
