# Input or Output?: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: input-or-output

#### Built

- Build only in S:\CurioClass-codex. Authored files are confined to tools/input-or-output/ and _scratch/input-or-output/.
- Four pictured gadgets, 18 tappable parts, Try It sorting, one-note Cover It predictions, jobs of five to 5.8 seconds, replay and interruption.
- Offline kit-based HTML, metadata, notes, voice manifest, audit states, handoff and code-drawn preview. No commits or polish round.

#### Numbers check

- _scratch/input-or-output/numbers.txt recomputes 30 / 6 = 5 seconds, 18 parts, 17 coverable parts and 16 distinct part announcements.
- Coverable parts: eight inputs, eight outputs and the touchscreen, which is both.
- All ten contrast ratios match the spec. White/header 5.774:1; ink/paper 14.078:1; input/paper 5.730:1; output/paper 4.714:1.
- Game clock: running at 4.9 seconds, finished at the 5.15 to 5.17 second check, with Motion on and off.
- Microwave: 0.8-second setup plus 30 / 6 = 5 seconds of countdown, total 5.8 seconds. Both Motion settings passed the full sequence.

#### Feel check

- Best moment: cover the volume button, predict that the gadget cannot tell, then watch the light and note trail show that the song still works.
- Flat moment one: the first note only covered a remote label. Changed it to a painted paper note over the pictured part, with a connected callout.
- Flat moment two: result cards lost the moving information. Kept a still directional trail and the stuck chip beside the result.
- Explored every part and every covered case. Later gadgets introduce invisible vibration, a safety switch and an input the job does not need.
- Compared with both required bar tools, bundled into Scratch. feel-comparison.png places this tool beside Snowy Mail Route.
- The paintings give this tool a richer place and more tactile hardware. The short preview necessarily crowds six microwave callouts around the gadget.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Required bar frames; every generated asset at finished size, individually or on the art contact sheet.
- early-frames, checks-frames, content-a and content-b: all gadget scenes and every covered case, plus all-found boards.
- sizes-a and sizes-b: seven desktop/preview sizes in both modes, Motion off and grayscale. Phone frames use the 375x812 host.
- interactions and final-frames: keyboard, interrupts, Read, five-tap voice, timing, compact note and 760 portrait.
- All 65 audit frames inspected through audit-gallery contact sheets. Post-repair portrait-frames (12), quick-frames (4), phone-frames and resize-frames inspected too.

#### Art made

- Fourteen new illustrations made with the built-in image tool. One existing Otter painting retained and inspected. One people asset deferred.
- Fifteen finished WebP files total 305.1 KB. Bundle 638.2 KB, below 2 MB. No image redraws needed; keyed edges were reprocessed with despill.
- Complete prompts and house style are in art/prompts.json. Raw originals are in art/raw/. No people were generated and no audio was recorded.

#### Art still to paint

- class-wave: the spec's class picture, retained as a people asset and art token. The call uses faceless code silhouettes until the owner's painter supplies it.

#### Engine changes wanted

None. No kit files were edited.

#### Left open

- Generic input-result speech says the gadget is stuck, although the specified camera and microphone call scenes continue with a missing stream. See handoff.md. This is a retained specification conflict.
- Big-sister / Leda recordings remain unmade; browser speech is the build fallback. No listening review was performed because every test Chrome is muted.
- The speaker plays the recognizable opening two phrases of Twinkle, Twinkle inside the five-second job, rather than a complete verse.
- The full audit predates the final build repairs; focused checks passed, but there was no second full audit.
- On compact screens the time is drawn in the labelled Display hotspot, avoiding the physical display under other callouts.
- A single long matrix evaluation reached drive.py's 60-second CDP limit. Its one smaller retry split by gadget passed all 17 cases.
- Earlier host favicon 404 was from drive.py's wrapper; the final phone wrapper includes a data favicon and runs cleanly. host.html was removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: input-or-output

#### Played

Cold Grade 2 solo play and teacher-led projection, before opening builder reports or source. Tried all gadgets and both modes. Rich painted hardware, clear direction arrows; long instruction queues initially buried the next action.

#### Findings fixed

- should fix, general, src.html: required classroom image was a plain silhouette. Painted and installed class-wave, 4:3 call inset; redrew its background once to make it a classroom.
- should fix, general, src.html voice entry: descriptive welcomes displaced action instructions at a two-second pace. Entry now begins with the action line; Try It queues Job before optional definitions.
- should fix, general, Motion off: the physical note's landing animation was outside the explicit calm rule. Added cover-patch to that rule.
- should fix, general, portrait 760x900: result symbols wrapped into a tall stack and pushed prediction feedback below the frame. Made the symbol fit one line and centered the low-sitting gadget. Focused portrait-result-fixed.png shows the whole result and prediction feedback in view.
- polish, general, compact board: crowded arrow/text headers collided in the narrow Think column. Compact layouts now use short IN/OUT labels and the central chip icon.
- should fix, family:hardware, game: a contained image centered inside its tall jump box made the fox float after landing. Bottom-aligned the fox; game-land-wide/compact/phone.png show its feet on the ground beyond the log.
- polish, family:hardware, completion: quiet final tap gave a tiny picker check. Completed sorting board now has a teal frame and an explicit all-parts-found heading.
- polish, general, preview: the card used a plain microwave outline unlike the tool's rich scene. Rebuilt the responsive card with the existing painted counter, microwave and note while retaining stopped input dots; preview-card.png in review-preview-final/ confirms the full frame.
- should fix, general, sources: Code.org spec URL returns 404. Preserved provenance and added live Open University definitions and Lincoln Center melody attribution in notes/metadata.
- should fix, general, audit clock overlap: the open microwave's time label met Beeper at 760x900. Extended the existing Display-callout clock to widths at or below 900; tested open, running and covered-display states.
- should fix, general, audit heading implementation: four compact layouts used zero-size THINK text. Replaced it with a proper screen-reader-only heading and preserved the visible chip/bar layout; re-shot 680, 800, 1000 and 375 widths.
- should fix, family:hardware, audit voice: Hello started only 3/5 times on two-second job restarts. It now takes its queue turn at the visible greeting beat. Post-fix: 5/5 starts, no dropped greetings, final full main path clean.

#### Findings left

- blocker, family:hardware, prediction giveaway: copying the filled IN/OUT board or cycling the two choices obtains "Your guess was right!" without explaining a consequence. The spec expressly requires the filled board and optional predictions. Left for spec correction under the review brief's no-spec-change rule; teacher notes now forbid treating this as mastery.
- should fix, family:hardware, specification: generic rInput says stuck even when a camera/microphone call continues; rOutput omits touch for the vibration motor. Fixed wording is expressly specified; review brief says do not change a disagreeing spec. Specific scene/result cards are accurate. Named in teacher notes.
- should fix, general, publication: fixed recorded narration is absent. Build brief forbids recording audio; browser fallback used and actual clip quality cannot pass a listening review here.
- should fix, general, catalog: data/modules.csv:271 still attaches E2-SYS-SE-12 to this tool's module; online consequences are not taught. Tool notes/spec exclude it. Catalog edit is outside both authorized folders.

#### Break it

- Every-part checks: tried Job only, repeated one part five times and then every unique part. Repeats leave only Camera found; all 18 unique parts fill the right board columns and earn the honest exploration check. No saved/best score.
- No score, estimate meter or reflection gate is present. A wrong prediction receives the specific consequence and a fresh look at the dots, without assuming any other mistake.
- Prediction check: tested both choices for all 17 coverable parts (34 mappings), including both touchscreen predictions and the volume exception. All agree with the specified mapping. Full jobs for all 17 matched their specific result cards.
- Trying every option/copying the filled board obtains matching feedback. This cheat passes the prediction check; the conflicting spec requirement is the blocker left above. No new assessment mechanic was added.
- Heater refuses the note. Mid-job Sticky note, Peel off, part and gadget changes stop the job with no old result. Changing the prediction clears old praise; a fresh wrong run returns a miss. Keyboard-only Tab/Enter covers Camera, predicts input, runs the call and keeps focus on Job. Evidence: review-focused/ and interrupt-cheats.json.

#### Voice walk

Held clicks, 120 ms, two-second steps and default Sound on; normal job waits. First tap on stage, Camera, Video call, each other gadget/job, Cover It, Sticky note, Door switch, prediction, Warm the soup, Read, mode change, Sound off/Read/on.
Started in order: tapPart, Camera, Job, Video call, Hello, Gadget, Game set, Jump, Smart speaker, Play a song, Microwave, Warm the soup, Cover, Sticky note on, Guess, selected input, Warm the soup, Right, rDoor, Again.
Every mode's key how-to started on this main path. Descriptive welcomes may be skipped/cut per BASELINE 16; advancing at two seconds can still cut already-started speech. Read with Sound off starts; mode change releases Read. Zero console exceptions.
Repeated the full main path after the audit's greeting fix: review-voice-final/walk.json and errors.json. All required how-to starts remain in order; interrupted older calls may cut an already-started Hello, while the latest greeting finishes.

| Repeated line | Kind | Expected | Started |
|---|---|---:|---:|
| Camera. Input. | event | 5 | 5 |
| Job instruction | how | 1 | 1 |
| Input definition | how | 1 | 1 |
| Hello on job restart | event | 5 | 5 |

#### Facts checked

- Definitions and direction of information: Open University computer systems glossary, input subsystem, output subsystem and input-output device: https://www.open.edu/openlearn/mod/oucontent/view.php?id=112559&section=_glossary
- Camera, microphone, joystick and keyboard/keypad input; screen/speaker output; touchscreen both: Open University's explicit peripheral-device table, with keypad/buttons classified by the same information-direction rule: https://www.open.edu/openlearn/mod/oucontent/view.php?id=112559&section=_unit3.5
- Controller buttons/sticks provide input and motors provide vibration feedback: Microsoft Learn, Gamepad and vibration: https://learn.microsoft.com/en-us/windows/uwp/gaming/gamepad-and-vibration
- Microwave door safety interlocks and magnetron: US FDA Microwave Ovens, safety standard and cooking sections: https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-ovens
- Melody is the anonymous French Ah vous dirai-je, maman, earliest known publication Paris 1761, not composed by Mozart: Lincoln Center Mostly Mozart program, 2017, Ah vous dirai-je maman: https://images.lincolncenter.org/image/upload/v1500392458/g7akxgkepqfos18oosf9.pdf
- CSTA hardware scope: official CSTA PK-12 standards https://csteachers.org/pk12standards/ and repository CSTA 2026 ids. E2-SYS-SE-12 is explicitly excluded by this spec.
- 2017 crosswalk: 1A-CS-02 matches naming physical hardware; 1A-CS-03 is practiced through hardware-fault description only, not software faults. CSTA's 2017 wording is broader: https://csteachers.org/wp-content/uploads/2025/03/csta-k-12-computer-science-standards-revised.pdf
- Gadget jobs are original simplified model scenarios, not empirical claims about every brand. Volume input is unnecessary for this song-starting job, not for all speaker use.
- Independent arithmetic: 30 seconds / 6 = 5 seconds; 0.8 second setup makes microwave 5.8 seconds. 18 part locations, 17 coverable, 8 input + 8 output + 1 both; 16 unique part announcements. WCAG formula: white/header 5.774, ink/paper 14.078, input/paper 5.730, output/paper 4.714; all ten specified ratios agree (review-static.json).

#### Sensitivity

New class-wave contains three children and is marked people:true. A fresh cultural reviewer should inspect skin-tone/hair representation, everyday clothing, glasses, hands, and whether the small inset remains welcoming. No cultural traditions, religion or hard history. The melody credit names its French source and anonymous authorship.

#### Flattest moment left

The covered volume button succeeds in a useful surprising way, but its generic correct-prediction message can sound like the song failed. This is a specification-level prediction-rule ambiguity, not scored mastery.

#### Graphics

Retained the strong kitchen, silver hardware, otter and fox. All original 15 finished assets inspected in scenes/contact sheet. Added class-wave via built-in imagegen with full prompt in prompts.json; 240x180, 11 KB, checked at final size and 680/1366/1920/375 call sizes. Total art 316.7 KB; bundle about 654 KB.
Looked at all cold-play, matrix, main-voice, size, grayscale, completion, calm and focused repair frames. Compared finish with the existing Snowy Mail Route and Beat Lab reference frames. Hotspots remain 72 pixels or larger; primary controls 60 pixels or larger. One full size sweep, followed only by affected frames. Microwave measured 5.827 seconds on / 5.810 off, both ending at 0:00.

#### Audit

Ran once, last, with a 2400-second limit, Chrome 9941, host 8745, profile chrome-prof-review. It finished; all 68 PNGs were examined through audit-sheet-01 to 18 and original lead frames.
15 leads answered: four compact zero-size headings fixed, one 760 clock/Beeper overlap fixed, one missed-Hello repeat fixed; nine own-line first-tap welcome skips accepted under BASELINE 16. No audit console errors, focus losses, endless calm animations or resize exceptions.
Re-shot only affected frames in review-audit-repairs/, plus the preview's responsive correction in review-preview-final/. Re-ran five job restarts and the full main voice path. No second full audit or polish sweep. host.html removed; Chrome 9940/9941/9943/9944 and host 8745 confirmed closed.
BUILD wave lessons were checked directly: hints/Read, focus, target sizes/fold, prediction giveaways, honest countdown, standard scope, calm timing, visible choices, running resize, welcome priority, unknown states, distinct directional signals, truthful checks and hints changing back. Spec/catalog exceptions are named above.

#### Left open

No questions asked in unattended session: chose to paint the specified classroom, following BASELINE's people decision, and retained disputed fixed spec lines as the review brief requires. No commits; all authored files stay in the two authorized folders. Two initial short documentation reads lacked an external process timeout; subsequent commands were bounded. The rolling report stayed in Scratch until final completion, honoring the user's stop-on-write instruction.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Input or Output?

#### Structure

src.html starts from the kit starter. It uses the kit header, motion, tone and Curio.voice queue.
G holds gadget and part definitions; L is the complete spoken line table. Each mode has per-gadget exploration state.
The stage uses a responsive gadget area, real HTML hotspot buttons, SVG wires and dots, and a separate sorting/result board.
Jobs share an elapsed-time clock: five seconds normally, 5.8 seconds for the microwave's setup and full five-second countdown.
A generation token invalidates speech and delayed sounds when interrupted.
The covered-volume case and internal-heater refusal are explicit cases, not inferred from the general input rule.

#### Open question taken

- class-wave: keep its people asset in prompts.json and its art token in src.html, following the spec's leaning.
  Cold review painted and installed the classroom call image with built-in imagegen, following BASELINE rule 11.
  class-wave is marked people:true; its full prompt and provenance are in art/prompts.json.

#### Engine changes wanted

None.

#### Next review

The build and one cold review are complete when codex-review.md exists. No commits. Browser narration is a fallback; no audio was recorded.
Use codex-review.md for current review evidence; codex-report.md preserves the earlier build evidence.

#### Build verification repairs

- The one full audit completed with 44 leads. Subsequent repairs were checked with focused frames and interaction runs,
  not another full audit. Keep that distinction when judging the evidence.
- Tall 760-pixel layouts put the board below the gadget. Phones keep it beside the gadget so all six 72-pixel hotspots,
  job controls and prediction controls fit without scrolling.
- Compact microwave layouts show the changing time inside the labelled Display hotspot, avoiding a time label under
  the right-hand callouts. A covered display hides that miniature clock too. Wide layouts draw time on the painting.
- Microwave open/shut overlays use separate geometry. Trying the heater closes the pictured door before showing warm food.
- Mode re-entry and selecting the current gadget restore the result pose and its still signal trail without replaying sounds.
- Tried tiles do not drop again. Re-selecting a mode does not cut its welcome. Cover instructions are how lines, not events.
- A rapid later part tap can cut an already-started how line. Read still speaks the current hint. Recordings and a listening
  review remain work for a later run.

#### Specification tension retained

- The generic covered-input narration says the gadget is stuck. The tablet camera and microphone Content rows
  specify a call that continues with one missing stream. This build follows those visible Content outcomes and retains
  the exact generic result line requested by the Voice section. A later editor should reconcile that line with the two cases.
- The module shown by neighbors.py still lists E2-SYS-SE-12. This tool does not claim to teach it. Catalog and module
  edits are outside the two writable folders authorized for this build.
- The song job uses the recognizable opening two phrases of Twinkle, Twinkle within the required five-second job.
- Narration manifests specify big-sister / Leda, but the build uses available browser speech because recording was prohibited.

#### Cold review changes

- Mode entry begins with actionable guidance, then the descriptive welcome while it still fits.
- Try It queues the Job instruction before optional input/output definitions. This makes Job start on the tested two-second main path.
- The completed sorting board gains a teal border and all-parts-found heading; the picker check still means only that each part was tried.
- The classroom call inset uses the finished people illustration, with a landscape aspect ratio and the same covered-camera dark state.
- Motion off explicitly suppresses the physical sticky note landing animation.
- The fox image aligns to the bottom of its animation box so its feet land on the game ground.
- Notes name the discussion-only prediction limits and the spec's generic narration conflict. Live supplemental definition and melody sources were added.

#### Sensitivity

class-wave is a new people image, drawn with built-in OpenAI imagegen and marked people:true.
It shows three children with varied skin tones and hair, everyday clothes and glasses, waving in a classroom.
One background redraw removed kitchen objects. A fresh cultural reviewer should inspect representation, hands, faces and the inset crop.
No Native, religious or hard-history content. The melody uses its anonymous French source credit.

#### Review verification

Current evidence lives in _scratch/input-or-output/review-voice/, review-checks/, review-sizes/ and review-audit/.
The main walk uses held 120 ms clicks, two-second steps, normal job waits and Sound on. Its log records starts and cuts, not a listening review.
Do not call missing fixed recordings or the inherited catalog standard resolved. Those require work beyond the review's authorization.

#### Audit-confirmed repairs

The final audit exposed the open microwave clock under Beeper at 760x900. All layouts at or below 900 pixels now use the existing labelled Display callout clock.
A covered Display still hides that clock. Four compact THINK headings used font-size zero; they now use a proper screen-reader-only style with the same visible chip/bar layout.
The call's Hello now takes the queue at its 1.6-second visual beat; it no longer waits behind the job label and disappears on two-second restarts.
Notes clarify that the 2017 troubleshooting crosswalk practices hardware-fault description only. The single full audit is not repeated after these narrow fixes.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
