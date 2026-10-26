# Hamburger Paragraph: voice

This tool was built before specs were written to a file; this holds only its voice spec. Teaching notes are in
notes.md and plan.md.

## Voice

`voice/lines.json`: `"bank": "curious-librarian"`, `"voice": "Aoede"`, `"style": "Say curiously and warmly, like a friendly school librarian"`. 44 lines, all short and grade 2
friendly. Neighbors checked with `python scripts/neighbors.py hamburger-paragraph`: no built neighbor uses this voice.

- Welcome (once, on the first tap): "Let's build a paragraph burger! ..."; the Write your own burger has its own intro (once).
  Start over or a new burger stops any talk, then queues the welcome if never said.
- Feedback: after Serve, the bear's line is narrated once its sound effect is over (400 ms, 800 ms after the yum),
  dropped if the bubble changed first. Serve waits for it before the buttons come back.
- Read (unchanged order): the finished paragraph, else the bear's bubble, else the picked sentence, else the burger top
  to bottom, else "Pick a sentence. ...". Each sentence is its own recorded part.
- Templated text made recordable: the boot line is one line per burger (4); "wrong filling" is spoken as two parts,
  the sentence itself and "That one sounds like a bun, not a filling. Try moving it." (the bubble still shows the
  sentence in quotes).
- Browser voice fallback, by design: only sentences the class types in Write your own.
- Also fixed: the yum flag and steam were drawn at NaN (layers() made fresh objects with no position); now drawn.

Queue: the collision-lab pattern (narrate, hush, readNow, first tap), written into src.html (this tool does not use the
kit). A line plays its recording (`"voice:*"`, keyed by exact text) and falls back to the browser's best voice only
when the text has none. Lines are marked said when they start, never when queued; a stop drops lines that never
started, unmarked. Read always stops other speech and is never cut off by a queued line; `hush()` resolves the pending
Read. Sound off: nothing narrates (Read still speaks); Sound back on queues the welcome if it was never said.
First tap: decided after that tap's own click ran; if it queued its own line, or was Read or Sound, the welcome is
skipped unmarked. `window.__voice` = {lines(): every line the code can speak, log: every line that started} for checks.
Not recorded yet: the integrator records with `scripts/localvoice.py` (bank voice), then `scripts/voice.py` encodes.
