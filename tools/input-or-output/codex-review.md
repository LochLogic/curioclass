# Codex review: input-or-output

## Played

Cold Grade 2 solo play and teacher-led projection, before opening builder reports or source. Tried all gadgets and both modes. Rich painted hardware, clear direction arrows; long instruction queues initially buried the next action.

## Findings fixed

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

## Findings left

- blocker, family:hardware, prediction giveaway: copying the filled IN/OUT board or cycling the two choices obtains "Your guess was right!" without explaining a consequence. The spec expressly requires the filled board and optional predictions. Left for spec correction under the review brief's no-spec-change rule; teacher notes now forbid treating this as mastery.
- should fix, family:hardware, specification: generic rInput says stuck even when a camera/microphone call continues; rOutput omits touch for the vibration motor. Fixed wording is expressly specified; review brief says do not change a disagreeing spec. Specific scene/result cards are accurate. Named in teacher notes.
- should fix, general, publication: fixed recorded narration is absent. Build brief forbids recording audio; browser fallback used and actual clip quality cannot pass a listening review here.
- should fix, general, catalog: data/modules.csv:271 still attaches E2-SYS-SE-12 to this tool's module; online consequences are not taught. Tool notes/spec exclude it. Catalog edit is outside both authorized folders.

## Break it

- Every-part checks: tried Job only, repeated one part five times and then every unique part. Repeats leave only Camera found; all 18 unique parts fill the right board columns and earn the honest exploration check. No saved/best score.
- No score, estimate meter or reflection gate is present. A wrong prediction receives the specific consequence and a fresh look at the dots, without assuming any other mistake.
- Prediction check: tested both choices for all 17 coverable parts (34 mappings), including both touchscreen predictions and the volume exception. All agree with the specified mapping. Full jobs for all 17 matched their specific result cards.
- Trying every option/copying the filled board obtains matching feedback. This cheat passes the prediction check; the conflicting spec requirement is the blocker left above. No new assessment mechanic was added.
- Heater refuses the note. Mid-job Sticky note, Peel off, part and gadget changes stop the job with no old result. Changing the prediction clears old praise; a fresh wrong run returns a miss. Keyboard-only Tab/Enter covers Camera, predicts input, runs the call and keeps focus on Job. Evidence: review-focused/ and interrupt-cheats.json.

## Voice walk

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

## Facts checked

- Definitions and direction of information: Open University computer systems glossary, input subsystem, output subsystem and input-output device: https://www.open.edu/openlearn/mod/oucontent/view.php?id=112559&section=_glossary
- Camera, microphone, joystick and keyboard/keypad input; screen/speaker output; touchscreen both: Open University's explicit peripheral-device table, with keypad/buttons classified by the same information-direction rule: https://www.open.edu/openlearn/mod/oucontent/view.php?id=112559&section=_unit3.5
- Controller buttons/sticks provide input and motors provide vibration feedback: Microsoft Learn, Gamepad and vibration: https://learn.microsoft.com/en-us/windows/uwp/gaming/gamepad-and-vibration
- Microwave door safety interlocks and magnetron: US FDA Microwave Ovens, safety standard and cooking sections: https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-ovens
- Melody is the anonymous French Ah vous dirai-je, maman, earliest known publication Paris 1761, not composed by Mozart: Lincoln Center Mostly Mozart program, 2017, Ah vous dirai-je maman: https://images.lincolncenter.org/image/upload/v1500392458/g7akxgkepqfos18oosf9.pdf
- CSTA hardware scope: official CSTA PK-12 standards https://csteachers.org/pk12standards/ and repository CSTA 2026 ids. E2-SYS-SE-12 is explicitly excluded by this spec.
- 2017 crosswalk: 1A-CS-02 matches naming physical hardware; 1A-CS-03 is practiced through hardware-fault description only, not software faults. CSTA's 2017 wording is broader: https://csteachers.org/wp-content/uploads/2025/03/csta-k-12-computer-science-standards-revised.pdf
- Gadget jobs are original simplified model scenarios, not empirical claims about every brand. Volume input is unnecessary for this song-starting job, not for all speaker use.
- Independent arithmetic: 30 seconds / 6 = 5 seconds; 0.8 second setup makes microwave 5.8 seconds. 18 part locations, 17 coverable, 8 input + 8 output + 1 both; 16 unique part announcements. WCAG formula: white/header 5.774, ink/paper 14.078, input/paper 5.730, output/paper 4.714; all ten specified ratios agree (review-static.json).

## Sensitivity

New class-wave contains three children and is marked people:true. A fresh cultural reviewer should inspect skin-tone/hair representation, everyday clothing, glasses, hands, and whether the small inset remains welcoming. No cultural traditions, religion or hard history. The melody credit names its French source and anonymous authorship.

## Flattest moment left

The covered volume button succeeds in a useful surprising way, but its generic correct-prediction message can sound like the song failed. This is a specification-level prediction-rule ambiguity, not scored mastery.

## Graphics

Retained the strong kitchen, silver hardware, otter and fox. All original 15 finished assets inspected in scenes/contact sheet. Added class-wave via built-in imagegen with full prompt in prompts.json; 240x180, 11 KB, checked at final size and 680/1366/1920/375 call sizes. Total art 316.7 KB; bundle about 654 KB.
Looked at all cold-play, matrix, main-voice, size, grayscale, completion, calm and focused repair frames. Compared finish with the existing Snowy Mail Route and Beat Lab reference frames. Hotspots remain 72 pixels or larger; primary controls 60 pixels or larger. One full size sweep, followed only by affected frames. Microwave measured 5.827 seconds on / 5.810 off, both ending at 0:00.

## Audit

Ran once, last, with a 2400-second limit, Chrome 9941, host 8745, profile chrome-prof-review. It finished; all 68 PNGs were examined through audit-sheet-01 to 18 and original lead frames.
15 leads answered: four compact zero-size headings fixed, one 760 clock/Beeper overlap fixed, one missed-Hello repeat fixed; nine own-line first-tap welcome skips accepted under BASELINE 16. No audit console errors, focus losses, endless calm animations or resize exceptions.
Re-shot only affected frames in review-audit-repairs/, plus the preview's responsive correction in review-preview-final/. Re-ran five job restarts and the full main voice path. No second full audit or polish sweep. host.html removed; Chrome 9940/9941/9943/9944 and host 8745 confirmed closed.
BUILD wave lessons were checked directly: hints/Read, focus, target sizes/fold, prediction giveaways, honest countdown, standard scope, calm timing, visible choices, running resize, welcome priority, unknown states, distinct directional signals, truthful checks and hints changing back. Spec/catalog exceptions are named above.

## Left open

No questions asked in unattended session: chose to paint the specified classroom, following BASELINE's people decision, and retained disputed fixed spec lines as the review brief requires. No commits; all authored files stay in the two authorized folders. Two initial short documentation reads lacked an external process timeout; subsequent commands were bounded. The rolling report stayed in Scratch until final completion, honoring the user's stop-on-write instruction.
