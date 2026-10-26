# Line Safari: spec notes

The tool was built from its plan and notes; this file records the voice wiring (2026-10-26).

## Voice

`voice/lines.json`: `"bank": "bright-teacher"`, `"voice": "Autonoe"`, `"style": "Say brightly and cheerfully, like an upbeat first grade teacher"`. 107 lines. `python scripts/neighbors.py line-safari`: no near neighbor uses this voice (paint-mixer, art-passport, beat-buddies, orchestra-zoo and sound-elevator use other voices).

All spoken text lives in one `VO` object in src.html (between `voice:lines-start` and `voice:lines-end`); the screen reads its Lines card text from the same object, so the two cannot drift. The queue is the collision-lab pattern (narrate, cue for feedback, hush, readNow, first-tap rule), playing clips through the kit (`Curio.init({clips: "voice:*"})`); a line with no recording yet falls back to the browser voice.

Where narration fires:
- Welcome per mode, once, on entering it after the first tap (Lines also asks about the stop on screen).
- Lines: the stop question when a stop opens; on Name it, the spoken name plus the card's two sentences; the finale.
- Shapes: picking a shape (find + what it looks like); a right tap ("That's a circle!" + "Keep looking!"), all found, every shape found; a wrong tap ("That one is a square." + "Find every circle!").
- Colors: one primary, a mix, a miss during hide and seek (miss + the hide prompt again), the hide prompt, hidden.
- Draw: the welcome only.
- Read speaks the on-screen instructions: the Lines card, the Shapes or Colors message, the Draw welcome.

Small behavior change: in hide and seek, the first primary on the way to a mixed color now says "I'm red! Now mix in another primary color." instead of counting as a miss.
