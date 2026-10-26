# Orchestra Zoo: spec notes

The tool was built from its plan and notes; this file records the voice wiring (2026-10-26).

## Voice

`voice/lines.json`: `"bank": "playful-friend"`, `"voice": "Laomedeia"`, `"style"` copied from the bank. 62 lines. `python scripts/neighbors.py orchestra-zoo`: no near neighbor uses this voice (line-safari, beat-buddies, art-passport and sound-elevator use other voices). marching-band (grade 2, not a listed neighbor) is also triaged to playful-friend.

All spoken text lives in one `VO` object in src.html (between `voice:lines-start` and `voice:lines-end`); the family blurbs, instrument facts and right-answer lines on screen read from the same object, so the two cannot drift. The queue is the collision-lab pattern (narrate, cue for feedback, hush, readNow, first-tap rule), playing clips through the kit (`Curio.init({clips: "voice:*"})`); a line with no recording yet falls back to the browser voice.

The narrator never talks over an instrument: every tune, the band and Play all call `music()`, which cuts the line now talking (and Read), and queued lines wait until the sound has finished. Hush (Sound off, Escape) stops talk at once.

Where narration fires:
- Welcome per mode (zoo, guess, band), once, on entering it after the first tap.
- Zoo: a family's intro when its home opens; an instrument's fact after its tune ends; the Play all lines after the whole family has played.
- Guess: the question when it changes, after the mystery tune; "Not that one" on a miss; the right-answer line after the reveal tune.
- Band: the welcome only (the band itself is music).
- Read stops all sound, then says the instructions on screen.

Fixes on the way: changing mode now resets the playing flag (a tune cut by a mode change could leave buttons stuck), and the header subtitle hides below 760px so the buttons stay on one row.
