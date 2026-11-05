# Codex report: input-or-output

## Built

- Build only in S:\CurioClass-codex. Authored files are confined to tools/input-or-output/ and _scratch/input-or-output/.
- Four pictured gadgets, 18 tappable parts, Try It sorting, one-note Cover It predictions, jobs of five to 5.8 seconds, replay and interruption.
- Offline kit-based HTML, metadata, notes, voice manifest, audit states, handoff and code-drawn preview. No commits or polish round.

## Numbers check

- _scratch/input-or-output/numbers.txt recomputes 30 / 6 = 5 seconds, 18 parts, 17 coverable parts and 16 distinct part announcements.
- Coverable parts: eight inputs, eight outputs and the touchscreen, which is both.
- All ten contrast ratios match the spec. White/header 5.774:1; ink/paper 14.078:1; input/paper 5.730:1; output/paper 4.714:1.
- Game clock: running at 4.9 seconds, finished at the 5.15 to 5.17 second check, with Motion on and off.
- Microwave: 0.8-second setup plus 30 / 6 = 5 seconds of countdown, total 5.8 seconds. Both Motion settings passed the full sequence.

## Feel check

- Best moment: cover the volume button, predict that the gadget cannot tell, then watch the light and note trail show that the song still works.
- Flat moment one: the first note only covered a remote label. Changed it to a painted paper note over the pictured part, with a connected callout.
- Flat moment two: result cards lost the moving information. Kept a still directional trail and the stuck chip beside the result.
- Explored every part and every covered case. Later gadgets introduce invisible vibration, a safety switch and an input the job does not need.
- Compared with both required bar tools, bundled into Scratch. feel-comparison.png places this tool beside Snowy Mail Route.
- The paintings give this tool a richer place and more tactile hardware. The short preview necessarily crowds six microwave callouts around the gadget.

## Done when

1. PASS: all 18 parts explored; board counts tablet 3 input / 2 output, game 2 / 2, speaker 2 / 2, microwave 2 / 4. Touchscreen bridges both columns.
2. PASS: four full jobs inspected; every-part picker checks verified. Game runs and jumps; call shows Otter; soup clock runs; speaker plays the opening melody.
3. PASS for Content outcomes: all 17 covered runs verified against result keys, plus heater refusal. Volume gives rVolume; door switch gives rDoor.
4. PASS: all 34 classification/prediction mappings checked. Real held-click frames include matches and misses, with either touchscreen prediction matching. No score.
5. PASS: 1366x768 and 680x425 inspected. The gadget remains central; the separate result board does not cover it.
6. PASS: restart, Try It part interruption, gadget switching, Sticky note, Peel off and prediction interruption checked. Results clear immediately.
7. PASS: all STANDARDS sizes covered. Main controls are at least 60 pixels, hotspots at least 72; picker tiles at least 72. No gameplay scrolling.
   Focused post-repair checks covered 680x425, 760x900, 1366x768 and the 375x812 iframe.
8. FAIL for complete how-line playback at a rapid pace: five held camera taps at two-second spacing start five event announcements; how lines start once. Read priority and Sound behavior pass. Rapid mode and job retries now retain a complete latest queue entry.
   Rapid taps can cut a longer how line after it starts, and the kit then regards it as heard. This remains a voice limitation.
9. PASS: keyboard alone covers, predicts and runs; focus remains on Go. Motion uses the same clock. No real media access; clean final interaction console.

## Wave lessons

- Hint and voice: FAIL for complete rapid-tap how-line playback. Hints update at once and name controls; Read priority verified. Fast-tap how cuts remain as described above.
- Focus and layout: PASS. Stable header/picker controls, preserved hotspot focus, no focus on load, reserved hint height.
- Sizes: PASS. Full sweep followed by focused repair checks; all main controls fit, and portrait now puts the board below the gadget.
- No giveaways: PASS. Cover It intentionally shows the known part board, as specified. Prediction concerns the job outcome; no score or answer meter.
- Honest numbers: PASS. No inferred meters. The only countdown is the specified accelerated microwave clock, explained in notes.
- Standards: FAIL for the inherited module listing; PASS for the hardware activity. Hardware is directly explored and diagnosed. Inherited module still lists E2-SYS-SE-12, which this tool does not claim; catalog edits are out of scope.
- Motion off: PASS. CSS loops stop; dots become still trails, the fox takes three positions, and timing stays five seconds, or 5.8 seconds for the microwave setup and countdown.
- Short choices in view: PASS. Four gadget choices, job and the prediction pair measured on screen, including the 375 iframe.
- Resize mid-animation: PASS. Audit clean; final real-input CDP checks resized every running gadget to 760x900 and back. Covered time also stayed hidden at 680x425.
- Late welcome: PASS in focused checks. Curio.voice handles first taps, without welcomeAfter; actions with their own line skip the welcome.
- Unknown as unknown: PASS. No hidden diagnosis is painted as a successful result before a job; prefilled classification is explicit spec behavior.
- One look, one meaning: PASS. In uses inward blue arrows; out uses outward orange arrows. Direction and columns also carry meaning in grayscale.
- True badges: PASS. Picker checks require every Try It part; prediction feedback follows the result classification, including volume's exception.
- Hint changes back: PASS. Mode, gadget, note, prediction, run and peel handlers set the current hint synchronously.
- No answer by copying words: PASS. Choosing a prediction asks who loses information; the device scene then demonstrates the consequence.

## Audit leads

One full audit completed in 1758.1 seconds, with 44 leads. All 65 audit PNGs were inspected in contact sheets.
The full audit was not repeated after repairs. Focused frames, real inputs, clock tests and running resize tests checked the changes.
Every original lead has its own numbered response in _scratch/input-or-output/audit-lead-responses.md:

- 14 portrait/title/hidden-label leads: fixed by a wider portrait gadget area and board below it.
- 5 speech-bubble leads: fixed with a centred responsive bubble, checked at 680 and 375.
- 8 clock-label leads: fixed with a compact Display-target clock and separate open-door overlay geometry. Covering Display hides both clock views.
- 4 refusal-caption leads: fixed by wrapping the caption inside the gap between hotspot columns.
- 9 first-tap welcome leads: kept because STANDARDS requires skipping the welcome when that tap has its own line, without marking it heard.
- 4 rapid-tap leads: fixed. Re-selecting a mode keeps its welcome; the latest call announcement completes before the queued Hello. quick-*.json logs verify these.

No audit console errors, endless Motion-off animations, focus losses, stuck controls or resize exceptions.
Five-click audit rows were clean. The separate camera test logged five part events at a two-second tap pace.

## Frames looked at

- Required bar frames; every generated asset at finished size, individually or on the art contact sheet.
- early-frames, checks-frames, content-a and content-b: all gadget scenes and every covered case, plus all-found boards.
- sizes-a and sizes-b: seven desktop/preview sizes in both modes, Motion off and grayscale. Phone frames use the 375x812 host.
- interactions and final-frames: keyboard, interrupts, Read, five-tap voice, timing, compact note and 760 portrait.
- All 65 audit frames inspected through audit-gallery contact sheets. Post-repair portrait-frames (12), quick-frames (4), phone-frames and resize-frames inspected too.

## Art made

- Fourteen new illustrations made with the built-in image tool. One existing Otter painting retained and inspected. One people asset deferred.
- Fifteen finished WebP files total 305.1 KB. Bundle 638.2 KB, below 2 MB. No image redraws needed; keyed edges were reprocessed with despill.
- Complete prompts and house style are in art/prompts.json. Raw originals are in art/raw/. No people were generated and no audio was recorded.

## Art still to paint

- class-wave: the spec's class picture, retained as a people asset and art token. The call uses faceless code silhouettes until the owner's painter supplies it.

## Engine changes wanted

None. No kit files were edited.

## Left open

- Generic input-result speech says the gadget is stuck, although the specified camera and microphone call scenes continue with a missing stream. See handoff.md. This is a retained specification conflict.
- Big-sister / Leda recordings remain unmade; browser speech is the build fallback. No listening review was performed because every test Chrome is muted.
- The speaker plays the recognizable opening two phrases of Twinkle, Twinkle inside the five-second job, rather than a complete verse.
- The full audit predates the final build repairs; focused checks passed, but there was no second full audit.
- On compact screens the time is drawn in the labelled Display hotspot, avoiding the physical display under other callouts.
- A single long matrix evaluation reached drive.py's 60-second CDP limit. Its one smaller retry split by gadget passed all 17 cases.
- Earlier host favicon 404 was from drive.py's wrapper; the final phone wrapper includes a data favicon and runs cleanly. host.html was removed.
