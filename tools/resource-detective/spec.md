# Resource Detective: voice

This tool was built before specs were written to a file; this holds only its voice spec. Teaching notes are in
notes.md and plan.md.

## Voice

`voice/lines.json`: `"bank": "gravel-ranger"`, `"voice": "Algenib"`, `"style": "Say warmly with a gravelly voice, like an old park ranger telling stories"`. 77 lines, all short and grade 2
friendly. Neighbors checked with `python scripts/neighbors.py resource-detective`: no built neighbor uses this voice.

- Welcome: the open case's opener ("A new case! Where did this pencil come from? ..."), once, on the first tap.
  Picking a case stops any talk and says that case's opener (after the pin sound).
- Next clue: stops any talk, then the clue text and the detective's question (250 ms after the card sound); a newer
  clue or case drops it.
- Follow the trail: each detective line (aha, how it was made, each resource) is narrated and the trail waits for it;
  the result is narrated 600 ms after the stamp or hmm.
- Read (unchanged): the newest clue as "Clue one." + the clue right after a clue was found, else the detective's bubble.
- Templated text made recordable: the result is now a list of short fixed lines (opener, "The pencil came from trees
  and rocks.", "You found trees.", "It also came from rocks.", the fair-answer notes, and one "No water in this one."
  per wrong pick), shown joined in the bubble. The old "X and Y weren't part of this one" (any subset of six) is
  replaced by one line per resource, which also fixes "Trees wasn't". Openers use "this pencil" / "these wool
  mittens" (was "this wool mittens"). All six picks were tried on all six cases by the checker: 77 lines in all.
- Browser voice fallback: none once recorded.

Queue: the collision-lab pattern (narrate, hush, readNow, first tap), written into src.html (this tool does not use the
kit). A line plays its recording (`"voice:*"`, keyed by exact text) and falls back to the browser's best voice only
when the text has none. Lines are marked said when they start, never when queued; a stop drops lines that never
started, unmarked. Read always stops other speech and is never cut off by a queued line; `hush()` resolves the pending
Read. Sound off: nothing narrates (Read still speaks); Sound back on queues the welcome if it was never said.
First tap: decided after that tap's own click ran; if it queued its own line, or was Read or Sound, the welcome is
skipped unmarked. `window.__voice` = {lines(): every line the code can speak, log: every line that started} for checks.
Not recorded yet: the integrator records with `scripts/localvoice.py` (bank voice), then `scripts/voice.py` encodes.
