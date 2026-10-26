# Marching Band: voice

This tool was built before specs were written to a file; this holds only its voice spec. Teaching notes are in
notes.md and plan.md.

## Voice

`voice/lines.json`: `"bank": "firm-captain"`, `"voice": "Alnilam"`, `"style": "Say firmly but kindly and cheerfully, like a friendly drum major giving clear directions to young kids"` (switched from playful-friend so it differs from Orchestra Zoo). 47 lines, all short and grade 2
friendly. Neighbors checked with `python scripts/neighbors.py marching-band`: no built neighbor uses this voice.

- Welcome per mode (Partners, Rows), once each: on the first tap, on switching mode, when the band stops, or Sound on.
- Feedback: the sentence along the bottom is narrated 700 ms after the last change; a newer sentence replaces it
  (a playing sentence is stopped when the band changes again).
- Never over the music: March! stops all talk and nothing narrates while the band plays; Read during a march stops
  the band first, then reads.
- Read (unchanged): the sentence along the bottom.
- Templated text made recordable: every sentence is a fixed line, 20 for Partners (1 to 20 musicians) and 25 for Rows
  (1 to 5 rows of 1 to 5), so no number-word groups are needed. Fixed while there: "one pairs" is now "one pair", and
  "One row of four makes four" (was "make").
- Browser voice fallback: none once recorded.

Queue: the collision-lab pattern (narrate, hush, readNow, first tap), written into src.html (this tool does not use the
kit). A line plays its recording (`"voice:*"`, keyed by exact text) and falls back to the browser's best voice only
when the text has none. Lines are marked said when they start, never when queued; a stop drops lines that never
started, unmarked. Read always stops other speech and is never cut off by a queued line; `hush()` resolves the pending
Read. Sound off: nothing narrates (Read still speaks); Sound back on queues the welcome if it was never said.
First tap: decided after that tap's own click ran; if it queued its own line, or was Read or Sound, the welcome is
skipped unmarked. `window.__voice` = {lines(): every line the code can speak, log: every line that started} for checks.
Not recorded yet: the integrator records with `scripts/localvoice.py` (bank voice), then `scripts/voice.py` encodes.
