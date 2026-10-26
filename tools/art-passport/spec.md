# Art Passport: spec notes

The tool was built from its plan and notes; this file records the voice wiring (2026-10-26).

## Voice

`voice/lines.json`: `"bank": "knowing-guide"`, `"voice": "Sadaltager"`, `"style"` copied from the bank. 99 lines. `python scripts/neighbors.py art-passport`: no near neighbor uses this voice (line-safari, beat-buddies, orchestra-zoo and sound-elevator use other voices; the art-museum siblings are concepts).

All spoken text lives in one `VO` object in src.html (between `voice:lines-start` and `voice:lines-end`); the Look closer finds, questions, Try it activities, compare clues and passport text on screen read from the same object, so the two cannot drift. The queue is the collision-lab pattern (narrate, cue for feedback, hush, readNow, first-tap rule), playing clips through the kit (`Curio.init({clips: "voice:*"})`); a line with no recording yet falls back to the browser voice.

The tool is large, so the narrator says each stop's intro and its key feedback, not every label: the fact rows (who made it, when, made of, why) and the feelings buttons are not spoken. The tool had no Read or Sound button; both were added (the kit runs Sound; Motion stays the tool's own).

Where narration fires:
- Travel: the hello on first visit, then "Tap a picture on the map..." (the visited count stays on screen only).
- Look: arriving at a work, its name and place, "We got a passport stamp!" on a first visit, and "What do you see?"; each Look closer find; each question as the class taps through See, Think, Wonder and the work's own question.
- Compare: the question and the think prompt; the clue when it is shown; the question again for a new pair.
- Passport: the stamp page sentence.
- Read says the screen now: in Look, the name, the current question and the Try it activity (or the find while zoomed); in Compare, the question and the clue or prompt.
