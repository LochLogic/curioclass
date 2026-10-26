# Beat Buddies: spec notes

The tool was built from its plan and notes; this file records the voice wiring (2026-10-26).

## Voice

`voice/lines.json`: `"bank": "lively-host"`, `"voice": "Sadachbia"`, `"style"` copied from the bank. 20 lines. VOICE-TRIAGE suggests hero-coach, but its voice is Puck and near neighbor sound-elevator already uses Gemini Puck, so lively-host (a kept voice no neighbor uses) was picked instead.

All spoken text lives in one `VO` object in src.html (between `voice:lines-start` and `voice:lines-end`); the banner text on screen reads from the same object, so the two cannot drift. The queue is the collision-lab pattern (narrate, cue for feedback, hush, readNow, first-tap rule), playing clips through the kit (`Curio.init({clips: "voice:*"})`); a line with no recording yet falls back to the browser voice.

The narrator never talks over the beat: starting the march or a rhythm calls `music()`, which cuts the line now talking, and queued lines wait while the clock runs. The freeze is quiet, so "Everybody freeze!" plays during it. Hush (Sound off) stops talk at once.

Where narration fires:
- Welcome per game (march, rhythm cards, echo), once, after the first tap.
- March: the tips; the Freeze game switch; "Everybody freeze!" in each freeze.
- Rhythm cards: each card's sound after it is picked ("Bear says ta. One sound."); the build and fill prompts; "Again? Or change a card." after play.
- Echo: listen (before the pattern plays), clap your turn, then "Was that it? Let's look."
- Read stops the beat and says the instructions on screen; in echo it resets an interrupted round to ready.

The header subtitle hides below 760px so the Read button fits on one row.
