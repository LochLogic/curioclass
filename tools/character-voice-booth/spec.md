# Character Voice Booth

## One idea
Say one line as different characters, and the booth draws every take as a voiceprint (how high, how fast, how loud, where you paused), so you can see exactly what you changed to become someone else, and test whether a partner can hear it.

## Not like
- two-sides-theater (ELA 2, roleplay): voices one scene as two characters to show point of view. Here the words never change; the lab is what your voice does to them, measured.
- act-it-out (story-dress-up, k-2, same group): the whole class acts a story with bodies, led by the teacher. Here one student at a time records, measures and compares takes.
- stage-blocker and director-s-chair (same group): space and staging. Here it is only the voice.
- paint-mixer (3-5 lab): mixes pigment to test a prediction. Here the experiment is a fair test on your own voice: change one dial, keep the rest.
- melody-maker, note-ninja (3-5 music): pitch as notes on a staff. Here pitch is speech, read only as "higher or lower than your usual voice", never as notes.
- depth-detective, art-style-match (3-5 arts): visual art tools.

## Who and how
- Grade 3-5, theater, module "Characters and Scenes (Theater)": voice, body and simple scripts.
- Topic line: voice, character and feeling
- Driver: students in pairs on laptops (one speaks, one listens), or a teacher on a projector with one volunteer at the mic. 20 to 30 minutes.
- Standards: NCAS TH:Cr2 (organize and develop ideas: make and revise choices), TH:Pr4 (use voice and body to show a character); also TH:Re7 (mystery listener and Compare respond to vocal choices), TH:Cr3 (try and refine voice choices), TH:Pr5 (vocal technique for a character).
- Needs a microphone to record; everything except recording works without one (Plan mode is the no-mic path).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`): `Booth` (default), `Compare`, `Plan`.

**Booth.** The stage is a recording booth: a dark foam wall, a big microphone drawn in code in the upper middle, and an ON AIR lamp above it (dark when idle; red with the word "Recording" while recording). Below it, the Take Shelf: up to six voiceprint strips stacked, newest at the top. Each strip shows the take number, the card's icon and name, the line, a `Play` button and a `Delete` button (trash icon).
- Panel, top to bottom: `Line` (a picker of 8 line chips; the chosen line shows big), `Card` (a toggle `Characters` / `Feelings`, then the 8 or 6 cards as icon tiles; the chosen card shows its body tip), the big round `Record` button (red circle and the word), a time bar 0 to 8 s, `Clear all takes`, and the optional `Change one thing` challenge button. The hint sits under Record.
- Record: a visual count-in 3, 2, 1 on the mic (no sound, so nothing beeps into the take), then the lamp lights and Record becomes `Stop` (square). Speaking fills the time bar. Stop, or 8 s, ends the take; the new strip draws itself left to right (600 ms; Motion off: at once) and its readout appears.
- Readout per take, four rows, word plus number: `Pitch` ("higher than your usual voice, +4 steps"), `Speed` ("faster, 3.1 words a second"), `Loudness` ("much louder, +9 dB"), `Pauses` ("2 pauses").
- With no microphone or a refused one: the lamp stays dark and the panel says "No microphone here. That's OK: use Plan and perform for a partner." with a `Go to Plan` button.

**Compare.** Two take pickers, `Take A` and `Take B` (chips with take number and card). The stage draws both prints on one shared chart (A solid, B dashed, each in its take color and number) with the "your usual voice" line. Below, a table: rows Pitch, Speed, Loudness, Pauses; columns A, B, and "What changed" (a word plus an up or down arrow, or "about the same"). A sentence under it: "B is higher, slower and has one more pause than A." Buttons: `Play A`, `Play B`, `Play A then B`.
- `Mystery listener` (toggle): hides every card name and icon and shuffles the order of all takes. The listener taps each strip and picks the card they think it was (the same card tiles). `Reveal` shows each guess beside the real card with a check or a cross and words ("matched 3 of 4"). Nothing is kept after Reveal.

**Plan (no-mic path; also works with a mic).** Pick a line and a card (same pickers). Four sliders, each with five labeled notches: `Pitch` (much lower, lower, usual, higher, much higher), `Speed` (much slower, slower, usual, faster, much faster), `Loudness` (much softer, softer, usual, louder, much louder), `Pauses` (none, 1, 2, 3, 4). The stage draws the planned print as a dotted ghost line. Buttons: `Perform it` (shows a big card with the line and the plan as four icons, for performing live to a partner who guesses the card), and `Record to check` (only with a mic): records a take, then draws the measured print over the ghost and shows each dial as "planned higher, got higher: match" or "planned louder, got about the same".

## Content
**Lines** (original): "Who left this door open?" / "I found it! It was under the bed." / "Please, may I have one more?" / "Hello? Is anybody out there?" / "This is the best day ever." / "Shh. Something is coming." / "I am not going to bed." / "Look what I can do!"

**Character cards** (icon drawn in code; body tip shown on the card):
- My usual voice (speech bubble): "Just talk like you, to a friend." This card is the baseline.
- Tiny mouse (round ears): "Make yourself small. Quick little hands."
- Sleepy giant (big boot): "Stand tall and heavy. Yawn first."
- Robot (antenna): "Stiff arms. Every word the same."
- Grumpy queen (crown): "Chin up. Arms folded."
- Nervous knight (helmet): "Shaky knees. Look over your shoulder."
- Excited puppy (paw): "Bounce on your toes."
- Old wizard (pointed hat): "Lean on a pretend staff. Take your time."

**Feeling cards:** Happy ("Smile while you say it."), Sad ("Let your shoulders drop."), Scared ("Hold your breath first."), Angry ("Stamp one foot."), Surprised ("Eyes wide, eyebrows up."), Bored ("Lean on your hand.").

**Change one thing** (challenge, optional): the booth picks a dial (pitch, speed, loudness or pauses) and the student records the same line twice: first usual, then changing only that dial. Met when the chosen dial lands in a different bin and the other three stay "about the same" (bins below). Result names any dial that also changed.

**Measures and bins** (the bins are this tool's own choices, labeled "about" on screen):
- Pitch: median of voiced frames in Hz; shown in steps (semitones) from the baseline: 12 times log2(take / baseline). About the same under 2 steps; higher or lower 2 to 5; much higher or lower over 5.
- Speed: words in the line divided by speaking time (first to last voiced frame, minus pauses). About the same within 15% of baseline; faster or slower 15 to 40%; much over 40%.
- Loudness: mean level of voiced frames in dB relative to the baseline. About the same under 3 dB; louder or softer 3 to 8; much over 8.
- Pauses: silent gaps of 0.3 s or more between the first and last voiced frame (count).
- Baseline: the most recent "My usual voice" take. If there is none, the first take, and the chart says "baseline: Take 1".

## Interactions in detail
- Microphone: requested only on the first Record, with echo cancellation, noise suppression and auto gain turned off (so loud and soft stay different). Audio stays in memory as buffers; nothing is saved, uploaded or kept after the page closes. `Clear all takes` and Delete free them. The mic track is stopped after each take (the browser's mic light goes off).
- Analysis: frames of 2048 samples every 10 ms; pitch by normalized autocorrelation (YIN style) between 70 and 700 Hz; a frame is voiced when its level is above -45 dBFS and its pitch clarity is 0.8 or more (tool's choices); a 5-frame median smooths the pitch line. A take with under 0.5 s of voiced frames is not shelved: "I didn't hear the words. Move closer to the mic and try again."
- Voiceprint drawing: x is time 0 to 8 s with a tick each second; y is pitch on a log scale from 70 to 700 Hz with only "lower" and "higher" labels and the dashed "your usual voice" line; line thickness 2 to 10 px follows loudness; gaps show as breaks with a small "pause" tag under each pause.
- A seventh take removes the oldest non-baseline take (a note says which). Takes are numbered in order and never renumbered.
- Narration is hushed when Record is pressed and nothing speaks until the take is shelved, so the narrator never ends up in a take. Read is disabled while recording.
- Play buttons play the buffer at its real speed; a play head runs along the strip (Motion off: no play head, the strip outline glows instead). Playing a take stops any other playback.
- Plan ghost: pitch level from the notch (0, plus or minus 3.5, plus or minus 7 steps from baseline, or from 220 Hz when there is no baseline), length from the speed notch and word count at a usual 2.5 words a second (tool's choice), thickness from loudness, gaps after commas and periods first, then between words, for the pause count.
- Changing mode keeps all takes. Switching line or card never changes a recorded take's label.
- Keyboard: R starts and stops recording when focus is in the panel; Space on a focused Play plays it.

## Look
- Accent (`--brand`) #7a5200 tape-reel brass. Paper #f2f5f4, ink #1f2a2b, muted #566466; booth wall #263236 with a wedge foam pattern in #2e3c41; mic silver #c9d1d4; ON AIR lamp #c62828 with white "Recording" text; time bar fill brass.
- Take colors on the booth wall, each with its take number and a dash pattern (never color alone): 1 #ffd166, 2 #7fdbff, 3 #ff9fb2, 4 #b9f18c, 5 #d0b3ff, 6 #ffb070.
- Contrast: white on brand 6.9:1; brand on paper 6.3:1; ink on paper 13.4:1; muted on paper 5.6:1; white on lamp red 5.6:1; booth text #e8efee on wall 11.3:1; take colors on wall 6.8 to 10.1:1.
- Different from the 3-5 arts neighbors: paint-mixer #7a3fa0, depth-detective #2e6440, art-style-match #9b2457, note-ninja #3b2d6b, melody-maker #b4532a (rust, redder and lighter), song-form-builder #0e7490, dance-pattern-puzzle #1f63c7.

## Art
none: drawn in code (booth, mic, lamp, card icons, voiceprints).

## Voice
Bank voice `smooth-narrator` (Algieba), style "Say smoothly and warmly, like an audiobook narrator": a narrator who voices every character for a living. Not used by any 3-5 arts neighbor (depth-detective gravel-ranger, art-style-match lively-host) or by this group. `Curio.voice` with `scope: () => state.mode`; all lines held while recording.

Booth:
- how, welcome: "Welcome to the booth. Pick a line, then tap Record and say it in your usual voice."
- how, after the first take: "Now pick a character card. Tap Record and say the same line as that character."
- how, after the second take: "Tap Compare to see what you changed."
- event, each new take, a sequence of fixed parts: "This take is" + one pitch part ("much higher" / "higher" / "about as high" / "lower" / "much lower") + one speed part ("and much faster" / "and faster" / "at about the same speed" / "and slower" / "and much slower") + "than your usual voice." (stale when another take starts). The first take ever says instead: "That's your usual voice. Every other take is compared to this one."
- event: "I didn't hear the words. Move closer to the mic and try again."
- event: "No microphone here. That's OK. Tap Go to Plan and perform for a partner."
- how, Change one thing: "Record the line in your usual voice. Then record it again and change only the" + "pitch." / "speed." / "loudness." / "pauses."
- event: "You changed just that one thing. That's a fair test." / "You changed more than one thing. Try again and keep the others the same."

Compare:
- how, welcome: "Pick Take A and Take B. Then tap Play A then B and listen for what changed."
- how, Mystery listener on: "Listener, tap a take, then tap the card you think it was. Then tap Reveal."
- event: "Your partner matched" + "none" / "one" / "two" / "three" / "four" / "five" / "six" + "of" + the same number words + "." (stale when Mystery listener is turned off)

Plan:
- how, welcome: "Set the four dials to plan a voice. Then tap Perform it and say it for a partner."
- event, Record to check: "Pitch matched your plan." / "Pitch didn't match your plan." (and the same pair for speed, loudness and pauses, as one sequence)

Read speaks the hint (or, in Booth, the current line and card).

## Family engine
none

## Sources
- National Core Arts Standards, Theatre, grades 3 to 5 (TH:Cr2, TH:Pr4): https://www.nationalartsstandards.org
- Pitch estimate: A. de Cheveigne and H. Kawahara, "YIN, a fundamental frequency estimator for speech and music", J. Acoust. Soc. Am. 111(4), 1917 to 1930 (2002).
- Semitone distance 12 times log2(f2/f1) and level in dB 20 times log10(rms): standard acoustics definitions.
- Mic constraints (echoCancellation, noiseSuppression, autoGainControl): W3C Media Capture and Streams, https://www.w3.org/TR/mediacapture-streams/
- Lines, cards, tips, bins and thresholds: this tool's own, labeled "about" on screen.

## Done when
1. With a mic: record the baseline and two character takes; each strip appears with four readouts, and a take said much higher and faster than the baseline reads "higher" or "much higher" and "faster" or "much faster" (check with a test tone file fed as the mic: a 220 Hz baseline and a 330 Hz take read +7 steps, "much higher").
2. Without a mic (permission refused in drive.py): no error, the no-mic line and `Go to Plan` show, and Plan works end to end.
3. The narrator never speaks between Record and the shelved take (log shows nothing `spoken` in that window).
4. Compare: the table and sentence match the two readouts; Mystery listener hides every card name and icon, and Reveal counts correctly.
5. Change one thing: changing only loudness by 10 dB meets it; changing pitch and loudness does not, and the result names both.
6. Clear all takes empties memory (no buffers left in `__tool.state`), and nothing is in localStorage.
7. Take colors always come with a number and dash pattern; contrast ratios as in Look.
8. Record, the line and the card pickers are visible without scrolling at 680x425, 1366x768 and 760 wide.
9. How-to lines are spoken once in a run of five takes; take results are spoken every time.

## Open questions
- Recording inside the tool page's embedded preview needs the iframe to allow the microphone (`allow="microphone"`). Allow it on the tool page, or show "Open full screen to record" in the preview?
