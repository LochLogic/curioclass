# Character Voice Booth

## One idea
Say one line as different characters, and the booth draws every take as a voiceprint (how high, how fast, how loud, where you paused), so you can see exactly what you changed to become someone else, and test whether a partner can hear it.

## Not like
- two-sides-theater (ELA 2, roleplay): voices one scene as two characters to show point of view. Here the words never change; the lab is what your voice does to them, measured.
- act-it-out (story-dress-up, k-2, same group): the whole class acts a story with bodies, led by the teacher. Here one student at a time records, measures and compares takes.
- stage-blocker and director-s-chair (same group): space and staging. Here it is only the voice.
- paint-mixer (3-5 lab): mixes pigment to test a prediction. Here the experiment is a fair test on your own voice: change one dial, keep the rest.
- melody-maker, note-ninja (3-5 music): pitch as notes on a staff. Here pitch is speech, read only as "higher or lower than your usual voice", never as notes.
- near-and-far, art-style-match (3-5 arts): visual art tools.

## Who and how
- Grade 3-5, theater, module "Characters and Scenes (Theater)": voice, body and simple scripts.
- Topic line: voice, character and feeling
- Driver: students in pairs on laptops (one speaks, one listens), or a teacher on a projector with one volunteer at the mic. 20 to 30 minutes.
- Standards: NCAS TH:Cr2 (organize and develop ideas: make and revise choices), TH:Pr4 (use voice and body to show a character); also TH:Re7 (mystery listener and Compare respond to vocal choices), TH:Cr3 (try and refine voice choices), TH:Pr5 (vocal technique for a character).
- Needs a microphone to record; everything except recording works without one (Plan mode is the no-mic path).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`): `Booth` (default), `Compare`, `Plan`.

**Booth.** Focus: the Take Shelf, and on it the newest voiceprint, which is the largest strip (the One idea is reading the print). The stage has two bands. The top band (about a third of the stage height) is the painted recording booth: the foam wall, the painted microphone in the middle and the painted ON AIR lamp above it (dark when idle; lit with the word "Recording" in code over its blank glass while recording). The lower two thirds is the Take Shelf: up to six voiceprint strips stacked, newest at the top and twice the height of the others. Each strip sits on a solid booth-colored card (#263236) and shows the take number, the card's picture and name, the line, a `Play` button and a `Delete` button (trash icon).
- Panel, top to bottom: `Line` (a picker of 8 line chips; the chosen line shows big), `Card` (a toggle `Characters` / `Feelings`, then the 8 or 6 cards as picture tiles; the chosen card shows its body tip), the big round `Record` button (red circle and the word), a time bar 0 to 8 s, `Clear all takes`, and the optional `Change one thing` challenge button. The hint sits under Record.
- Record: a visual count-in 3, 2, 1 on the mic (big numbers in code; no sound, so nothing beeps into the take), then the lamp lights and Record becomes `Stop` (square). While recording, the focus moves to the lamp and the time bar, which fills as time passes. Stop, or 8 s, ends the take; the new strip draws itself left to right (600 ms; Motion off: at once) and its readout appears.
- Readout per take, four rows, word plus number: `Pitch` ("higher than your usual voice, +4 steps"), `Speed` ("faster, 3.1 words a second"), `Loudness` ("much louder, +9 dB"), `Pauses` ("2 pauses").
- With no microphone or a refused one: the lamp stays dark and the panel says "No microphone here. That's OK: use Plan and perform for a partner." with a `Go to Plan` button.

**Compare.** Focus: the shared chart of the two prints, the biggest thing on the stage. Two take pickers, `Take A` and `Take B` (chips with take number and card). The stage draws both prints on one shared chart (A solid, B dashed, each in its take color and number) with the "your usual voice" line. Below, a table: rows Pitch, Speed, Loudness, Pauses; columns A, B, and "What changed" (a word plus an up or down arrow, or "about the same"). A sentence under it: "B is higher, slower and has one more pause than A." Buttons: `Play A`, `Play B`, `Play A then B`.
- `Mystery listener` (toggle): hides every card name and picture and shuffles the order of all takes. The listener taps each strip and picks the card they think it was (the same card tiles). `Reveal` shows each guess beside the real card with a check or a cross and words ("matched 3 of 4"). Nothing is kept after Reveal.

**Plan (no-mic path; also works with a mic).** Focus: the planned print (the dotted ghost line), center stage. Pick a line and a card (same pickers). Four sliders, each with five labeled notches: `Pitch` (much lower, lower, usual, higher, much higher), `Speed` (much slower, slower, usual, faster, much faster), `Loudness` (much softer, softer, usual, louder, much louder), `Pauses` (none, 1, 2, 3, 4). The stage draws the planned print as a dotted ghost line, redrawn at once on every notch. Buttons: `Perform it` (shows a big card with the line, the card's picture and the plan as four icons, for performing live to a partner who guesses the card), and `Record to check` (only with a mic): records a take, then draws the measured print over the ghost and shows each dial as "planned higher, got higher: match" or "planned louder, got about the same".

## Content
**Lines** (original): "Who left this door open?" / "I found it! It was under the bed." / "Please, may I have one more?" / "Hello? Is anybody out there?" / "This is the best day ever." / "Shh. Something is coming." / "I am not going to bed." / "Look what I can do!"

**Character cards** (each shows a painted prop or animal, Art; body tip shown on the card):
- My usual voice (a blank paper speech bubble): "Just talk like you, to a friend." This card is the baseline.
- Tiny mouse (a small grey mouse): "Make yourself small. Quick little hands."
- Sleepy giant (a huge worn boot): "Stand tall and heavy. Yawn first."
- Robot (a tin toy robot): "Stiff arms. Every word the same."
- Grumpy queen (a gold crown): "Chin up. Arms folded."
- Nervous knight (a steel helmet): "Shaky knees. Look over your shoulder."
- Excited puppy (a puppy): "Bounce on your toes."
- Old wizard (a starry pointed hat and a wooden staff): "Lean on a pretend staff. Take your time."

**Feeling cards** (simple face icons drawn in code, like emoji): Happy ("Smile while you say it."), Sad ("Let your shoulders drop."), Scared ("Hold your breath first."), Angry ("Stamp one foot."), Surprised ("Eyes wide, eyebrows up."), Bored ("Lean on your hand.").

**Change one thing** (challenge, optional): the booth picks a dial (pitch, speed, loudness or pauses) and the student records the same line twice: first usual, then changing only that dial. Met when the chosen dial lands in a different bin and the other three stay "about the same" (bins below; for pauses, the same count). Result names any dial that also changed.

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
- Play buttons play the buffer at its real speed; a play head runs along the strip (Motion off: no play head, the strip outline glows instead). Everything stays live while a take plays: another Play stops the first and starts at once; Delete, Record, a mode switch or a picker tap stops playback at once. `Play A then B` stops if either take is deleted. Stop during the 3, 2, 1 count-in cancels the take.
- Plan ghost: pitch level from the notch (0, plus or minus 3.5, plus or minus 7 steps from baseline, or from 220 Hz when there is no baseline); speed from the notch as a share of a usual 2.5 words a second (much slower 0.55, slower 0.8, usual 1, faster 1.25, much faster 1.6; tool's choices, each landing inside its own bin); length from that speed and the line's word count; thickness from loudness (0, plus or minus 5, plus or minus 10 dB); a 0.5 s gap per pause, after commas and periods first, then between words.
- Changing mode keeps all takes. Switching line or card never changes a recorded take's label.
- Keyboard: R starts and stops recording when focus is in the panel; Space on a focused Play plays it.

## Look
- Accent (`--brand`) #7a5200 tape-reel brass. Paper #f2f5f4, ink #1f2a2b, muted #566466; the painted booth wall reads dark slate, and the take cards and chart sit on solid #263236; booth text #e8efee; time bar fill brass; lamp glow #c62828 behind the white "Recording" text.
- Take colors on the take cards, each with its take number and a dash pattern (never color alone): 1 #ffd166, 2 #7fdbff, 3 #ff9fb2, 4 #b9f18c, 5 #d0b3ff, 6 #ffb070.
- Contrast: white on brand 6.92:1; brand on paper 6.31:1; ink on paper 13.44:1; muted on paper 5.61:1; white on lamp red 5.62:1; booth text on #263236 11.31:1; take colors on #263236 6.82 to 10.07:1.
- Different from the 3-5 arts neighbors: paint-mixer #7a3fa0, near-and-far #2e6440, art-style-match #9b2457 on teal felt, note-ninja #3b2d6b, melody-maker #b4532a (rust, redder and lighter), song-form-builder #0e7490, dance-pattern-puzzle #1f63c7.

## Art
Local FLUX (`scripts/localart.py`), one session, no people. One style: "soft painted picture-book style, warm studio light".
- booth-wall: "the inside of a small recording booth, a wall covered in dark slate grey acoustic foam wedges, a strip of warm wooden floor at the bottom, soft studio light from above, soft painted picture-book style"; 16:9; cutout no; people no; the top band of Booth, cropped to the band.
- mic: "a big silver studio microphone with a round mesh head on a short black desk stand, front view, soft painted picture-book style, plain white background"; 3:4; cutout yes; people no; center of the booth band; it gives a small pulse in code while recording (Motion on).
- lamp-off: "a rectangular vintage studio warning lamp box in dark red metal with a blank smooth glass front, unlit, soft painted picture-book style, plain white background"; 4:1; cutout yes; people no; above the mic when idle.
- lamp-on: the same lamp with its blank glass glowing bright red; 4:1; cutout yes; people no; swapped in while recording, with "Recording" in code over the glass.
- Character card pictures (8 cutouts, kit of parts): each "<item>, one object, front view, bright friendly colors, soft painted picture-book style, plain white background"; 1:1; cutout yes; people no; shown on the card tiles at tile size, on the take strips at 32 px, and big on the Perform it card. Items: a blank paper speech bubble cut from cream card; a small grey mouse sitting up with round pink ears; a huge worn brown leather boot; a tin toy robot with a short antenna; a gold crown with red jewels; a steel knight's helmet with a closed visor; a happy brown and white puppy sitting; a starry blue pointed wizard hat leaning on a wooden staff.
- 12 images in all, none with people (the giant, queen, knight and wizard are shown by a prop, not a person). Drawn in code: the feeling face icons (symbols like emoji, six expressions that must read at 32 px), voiceprints, charts, the count-in numbers, the time bar, buttons and labels.

## Voice
Bank voice `smooth-narrator` (Algieba), style "Say smoothly and warmly, like an audiobook narrator": a narrator who voices every character for a living. Not used by any 3-5 arts neighbor (near-and-far gravel-ranger, art-style-match lively-host, dance-pattern-puzzle clear-teacher) or by this group. `Curio.voice` with `scope: () => state.mode`; all lines held while recording.

Booth:
- how, welcome (on entering Booth with no takes; stale when Record is tapped): "Welcome to the booth. Pick a line, then tap Record and say it in your usual voice."
- how, after the first take (stale when Record is tapped): "Now tap a character card. Tap Record and say the same line as that character."
- how, after the second take (stale when Compare is tapped or Record is tapped): "Tap Compare to see what you changed."
- event, each new take, a sequence of fixed parts: "This take is" + one pitch part ("much higher" / "higher" / "about as high" / "lower" / "much lower") + one speed part ("and much faster" / "and faster" / "at about the same speed" / "and slower" / "and much slower") + "than your usual voice." (stale when another take starts). The first take ever says instead: "That's your usual voice. Every other take is compared to this one."
- event, too little voice (stale when Record is tapped): "I didn't hear the words. Move closer to the mic and try again."
- event, no microphone (stale when the mode changes): "No microphone here. That's OK. Tap Go to Plan and perform for a partner."
- how, Change one thing (on tapping it; stale when its second take is shelved): "Tap Record and say the line in your usual voice. Then tap Record again and change only the" + "pitch." / "speed." / "loudness." / "pauses."
- event, Change one thing result (stale when Record is tapped): "You changed just that one thing. That's a fair test." / "You changed more than one thing. Try again and keep the others the same."

Compare:
- how, welcome (on entering Compare with two or more takes; stale when a Play button is tapped): "Pick Take A and Take B. Then tap Play A then B and listen for what changed."
- how, welcome with fewer than two takes (stale when the mode changes): "You need two takes to compare. Tap Booth and record another."
- how, Mystery listener on (stale when Reveal is tapped): "Listener, tap a take, then tap the card you think it was. Then tap Reveal."
- event, after Reveal: "Your partner matched" + "none" / "one" / "two" / "three" / "four" / "five" / "six" + "of" + the same number words + "." (stale when Mystery listener is turned off)

Plan:
- how, welcome (on entering Plan; stale when a slider moves): "Slide the four dials to plan a voice. Then tap Perform it and say it for a partner."
- event, Record to check (stale when a slider moves or Record is tapped): "Pitch matched your plan." / "Pitch didn't match your plan." (and the same pair for speed, loudness and pauses, as one sequence)

Read speaks the hint (or, in Booth, the current line and card).

## Family engine
none

## Sources
- National Core Arts Standards, Theatre, grades 3 to 5 (TH:Cr2, TH:Pr4): https://www.nationalartsstandards.org
- Pitch estimate: A. de Cheveigne and H. Kawahara, "YIN, a fundamental frequency estimator for speech and music", J. Acoust. Soc. Am. 111(4), 1917 to 1930 (2002).
- Semitone distance 12 times log2(f2/f1) and level in dB 20 times log10(rms): standard acoustics definitions.
- Mic constraints (echoCancellation, noiseSuppression, autoGainControl): W3C Media Capture and Streams, https://www.w3.org/TR/mediacapture-streams/
- Lines, cards, tips, bins, Plan notches and thresholds: this tool's own, labeled "about" on screen.
- Checks run (Python, 2026-10-29): 220 Hz to 330 Hz is 12 log2(1.5) = 7.02 steps, "much higher" (over 5). Plan pitch notches 0, 3.5 and 7 steps land in about the same, higher and much higher. Plan speed shares 0.55, 0.8, 1, 1.25 and 1.6 (added; the old spec gave no numbers) read much slower (-45%), slower (-20%), about the same, faster (+25%) and much faster (+60%), each inside its own bin and clear of the 15% and 40% edges. Longest Plan ghost: 8 words at much slower (1.375 words a second) plus 4 pauses of 0.5 s is 7.82 s, inside the 8 s take; shortest line at much faster is 1.0 s, above the 0.5 s voiced minimum. Loudness: 2.9 dB about the same, 3 and 8 dB louder, 8.1 and 10 dB much louder (Done when 5 uses 10 dB). Contrast ratios in Look recomputed with the WCAG 2.1 formula (values as stated).

## Done when
1. With a mic: record the baseline and two character takes; each strip appears with four readouts, and a take said much higher and faster than the baseline reads "higher" or "much higher" and "faster" or "much faster" (check with a test tone file fed as the mic: a 220 Hz baseline and a 330 Hz take read +7 steps, "much higher").
2. Without a mic (permission refused in drive.py): no error, the no-mic line and `Go to Plan` show, and Plan works end to end.
3. The narrator never speaks between Record and the shelved take (log shows nothing `spoken` in that window).
4. Compare: the table and sentence match the two readouts; Mystery listener hides every card name and picture, and Reveal counts correctly.
5. Change one thing: changing only loudness by 10 dB meets it; changing pitch and loudness does not, and the result names both.
6. Clear all takes empties memory (no buffers left in `__tool.state`), and nothing is in localStorage.
7. Take colors always come with a number and dash pattern; contrast ratios as in Look.
8. Focus: at 1366x768 and 680x425 the newest voiceprint is the largest strip on the Booth stage, the shared chart fills most of the Compare stage, and the ghost print is center stage in Plan.
9. Tap while it plays: during playback, another Play, Delete, Record or a mode tap acts at once and the old playback stops; Stop during the count-in cancels the take with no strip shelved.
10. Record, the line and the card pickers are visible without scrolling at 680x425, 1366x768 and 760 wide.
11. How-to lines are spoken once in a run of five takes; take results are spoken every time; no line names a disabled control (Compare's welcome with one take names Booth, not Play).

## Open questions
- Recording inside the tool page's embedded preview needs the iframe to allow the microphone (`allow="microphone"`). Allow it on the tool page, or show "Open full screen to record" in the preview?
