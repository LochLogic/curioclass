# Field Trip Slideshow build handoff

Built in S:/CurioClass-codex for a teacher-led K-2 aquarium recount. Build only, no commit and no polish round.

## Structure

src.html starts from kit/starter/src.html and uses kit:curio CSS and JavaScript. Responsive CSS lays out real boxes,
without scaling a fixed desktop scene. All five mode sections and their controls persist in the DOM. Render functions
update pictures and labels inside controls while retaining the buttons. A single art map avoids duplicate image data.

The script groups slides and take orders, state, room options, fixed narration, voice, crew renderers and actions,
the rehearsal rules, the audio bus, and bindings. window.__tool exposes the state, content, rules, actions and voice log.

## Important behavior

- Clear takes are B, C, A, C, B, A. Every slide also has blur and its specified problem. Problem takes can be kept.
- Enlarging a take hides the slide strip to give the picture and two choice buttons enough space at 680x425.
- The camera strip and the two slide arrows wrap around; Show has a title, six slides, and a thank-you slide.
- Speaker cards precede picture targets in keyboard order and visual order. Wrong matches return the card.
  Tapping a matched picture with no sentence selected returns its card and clears practice, allowing revision.
- The selected takes appear in Sound, Speaker, Room's first slide and Show. Unchosen takes use the clear painting
  as an editing preview, but rehearsal and crew badges still require an actual Camera choice.
- Sound is ready at level 1-3 after Test it has been used once. A later volume change recomputes readiness.
- Every room control cycles immediately. Light wash fades for 400 ms with Motion on. The only passing room states
  are Dim or Off, Down, Face the screen, Beside the screen, Medium.
- Present works with unfinished work. Missing Speaker matches show a reminder instead of pretending a card was placed.
- New show confirms. Keep it preserves the choices. Yes clears every crew. Nothing about the show is persisted.
- Tapping the already selected mode is a no-op, so a quick second tap cannot cut its welcome or reset the show.

## Art and layout

All twelve assets were generated with the built-in image tool using the house style and prompts in art/prompts.json.
The raw PNGs are in art/raw; scripts/art.py field-trip-slideshow --rekey NAME makes the finished WebPs for free.
The classroom was redrawn once to remove baked-in chairs. Three rows of painted blue chair cutouts alone show direction.
The octopus was redrawn once to make all eight arms separately visible. Its corrected eight tips were counted at full size.
Original provenance paths, the earlier classroom and comparison sheets are in _scratch/field-trip-slideshow/.
There are no people in the pictures. The star and microphone marker is the specified speaker surrogate.

The paintings use contain inside dark screen frames so a clear animal is never accidentally cropped by layout.
This causes substantial letterboxing in tall portrait Camera takes, especially on phones. Tap a take for a larger view.
Compact landscape Speaker uses two adjacent grids; phone Speaker stacks cards above pictures. Practice has a compact
icon and spacing to keep the main button above the hint. Room toggles use a two-column grid on small screens.

## Voice and audio

voice/lines.json inventories science-narrator / Charon with the specified nature-documentary style.
No narration was recorded, as instructed. Curio.voice supplies browser speech, once-only how-to lines, events,
Read priority, scope checks and logs. Scope is mode plus slide. A finished Speaker job does not queue the obsolete
sentence-matching welcome. Event callbacks validate their current selection, job readiness or open dialog.
Read also cancels the custom test clock and music. Its canceled timer cannot later cut Read. An arrow key that
leaves an enlarged take returns focus to the first take using preventScroll.
Both native dialogs include a Read button, since the header becomes inert while a modal dialog is open.
Opening New show voices its confirmation instruction once; subsequent opens still show it and support Read.
Keep it cancels that instruction. A music-level change cancels old test-result speech while preserving an active
sample sentence, so the music can change beneath that same sentence.

An original D-major, eight-bar loop uses sine pads, a slow bell arpeggio and bubble notes at 72 bpm. One gain bus uses
the exact -24, -18, -12, -6 and 0 dB factors, ramping changes over 50 ms. Test it restarts immediately, runs at most
six seconds, and highlights successive words on an approximate clock. All scheduled nodes and timers are canceled
on a mode change or test restart. Sound off silences the custom bus as well as the kit. Applause is synthesized noise.

Browser speech is outside Web Audio, so actual acoustic music-to-voice balance and exact word alignment cannot be
calibrated to a browser voice. The listening symbols are explicitly labeled as a classroom model on screen.
A headphone check and fixed recordings remain for a later owner-authorized pass. No audio was recorded in this run.

## Spec questions and decisions

The spec contains no explicit open-question section. Its leaned choices were kept: teacher-led crew work, a true
aquarium recount, paintings instead of uploads, an eight-bar aquarium loop, Present allowed before all checks pass,
and nothing saved. Tap-then-picture is the specified alternative to dragging in Speaker.

The listed room contrast and palette values agree with independent calculations after rounding. No spec edit was made.
The three camera takes stay side by side even on phones; their full animal frames are preserved with letterboxing.

## Verification and next review

Scratch contains numbers.json, logic.json, student-run.json, voice.json, all shot plans and frames, bar-tool copies,
and the single mechanical audit output. The 36 sentence pairs, 108 room combinations, five music levels, camera
choices, ready rehearsal and eight-slide presentation path were checked. A separate real-input run completed all crews.
The report records final audit leads and any targeted follow-up. Do not infer a second full audit after repairs.

The single full audit completed within its 40-minute cap. All eight sizes, mode and interaction layouts, motion off,
mid-action resizing, console checks, and five-held-click checks passed. Its 95 frames were inspected on 17 contact
sheets, with relevant Build frames also viewed full size. It reported twelve leads: four native-modal background keep
regions, three intentionally skipped welcomes on a take's own first-tap note, and five repeated-mode welcome cuts.
The last five were fixed by making the selected mode a no-op; held double-tap checks passed in all five modes.
The keep plan now tests each modal itself rather than its inert background. The three first-tap skips follow STANDARDS.

Targeted checks after the full audit passed for Read canceling the test and its later summary, visible focus after an
arrow leaves the enlarged take, live level adjustment without cutting the sample, Keep it canceling the reset line,
and dialog Read at 680x425 and 375x812. At a two-second pace, five sentence picks started five event lines and one how-to.
The full audit was not rerun after these repairs. Fixed narration now inventories 114 lines. Final bundle: 1,421,111 bytes.
Every test Chrome and server was closed, verified on 9980, 9981 and 8785. The temporary host.html was removed.

## Engine changes wanted

None. No kit, documentation, script or other tool source was changed.
