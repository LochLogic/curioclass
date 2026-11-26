# Field Trip Slideshow: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: field-trip-slideshow

#### Built

- All five modes: Camera, Sound, Speaker, Room, Show. Four crew badges, an actionable rehearsal, teacher-paced
  presentation, thank-you slide, synthesized applause and confirmed reset. One offline HTML file from the kit starter.
- Teacher-led K-2, MA:Pr5, MA:Pr6, MA:Cn10. Tap a sentence then a picture is the spec's alternative to dragging.
- Twelve finished generated paintings, no people. Draft metadata stays stage built. No commit or polish round.

#### Numbers check

- Independently recomputed in Scratch/prepare.py and numbers.json before implementation.
- Gains: 0.063096, 0.125893, 0.251189, 0.501187, 1.000000 at -24, -18, -12, -6, 0 dB.
- Room contrast: 2.461538, 4.166667, 10.5 to 1. These agree with the spec's rounded values.
- WCAG palette: white/brand 7.2668, brand/paper 6.7132, ink/paper 14.4635, muted/paper 5.9463 to 1.
- Six unique captions, six slides, three takes each. Eight bars at 72 bpm in four beats per bar take 26.6667 seconds.
- Logic checks covered all 36 sentence pairs and all 108 room combinations. Exactly two room states pass,
  differing only in Dim versus Off. No spec edit or numerical correction was needed.

#### Feel check

Played the full crew workflow with held real clicks, ending in four ready jobs and the complete rehearsal card.
Best moment: the light wash and star shadow disappear, chairs face the picture, and the crew's last check becomes ready.
The next step is their own teacher-paced aquarium show.

Two flattest moments and changes within Build:

- A clear picture was being accidentally cropped by layout. Full-frame paintings now preserve the animals, and the
  first tap opens a large comparison with a concrete note. Portrait Camera still has heavy letterboxing.
- The room's chair direction was muddied by painted-in chairs behind movable ones. Redrew the room without those
  chairs, so the three rows of blue cutouts alone show the change. Also fitted the compact practice card's main button.

Compared both bundled bar tools and put Camera beside Snowy Mail Route in Scratch/feel-comparison.jpg.
The aquarium paintings have richer material detail and light; the four different crew skills give the session variety.
This is an audience-preparation activity, with its payoff in the group's presentation. No ten-minute super-tool claim.

#### Done when

1. PASS: Camera, Sound, Room and Show checked at 1366x768 and 680x425. Whole paintings are letterboxed inside
   screen frames to avoid introducing accidental cropping. Compact enlargement and practice overflow were repaired.
2. PASS: 18 takes from fixed orders B/C/A/C/B/A for clear, each with blur and its specific problem. Source table,
   close-up frames, chosen-take strip and Camera completion checked. The 70% crop is applied in code.
3. PASS for the model: all five faces and gains checked; held Softer clicks changed the live test to level 1.
   The gain ramp is 50 ms. Acoustic music-to-browser-speech calibration remains open.
4. PASS: all 36 pairs exercised through the real matching functions; only the six corresponding pairs stay.
5. PASS: all 108 rule combinations checked; room toggles and passing setup inspected in frames.
6. PASS: specific Camera slide-3 blur note checked; full real-input rehearsal reached four ready rows.
   An unfinished presentation was also advanced with keyboard and real clicks.
7. PASS: repeated Test it, a mode switch during the test, and Next slide during playback all changed state immediately.
8. PASS: Curio.voice separates instructions and events. The full five-held-click audit was clean. A final
   two-second-pace check started five sentence events and one how-to; five mode double-tap rechecks also passed.
9. PASS: all required sizes and 375-wide host passed the audit; main controls, badges and hints remain visible.
   Numbered picture slots use accessible slide labels. Compact text is intentionally smaller than projector text.
10. PASS: Motion off yielded zero running animations; CSS also removes light transitions and hover scale.
    Static scan found no network or media-capture calls, external resources or em dashes in authored deliverables.

#### Wave lessons

- PASS, Hint and voice: next-action hints update synchronously and Read uses that state. Curio.voice owns how-to history;
  no action counter chooses instructions. Final interruption checks are recorded below.
- PASS, Focus and layout: permanent buttons, no focus on load, preventScroll on intentional moves; enlarged-take arrows
  return focus to a visible take. Fixed the compact close-up and practice-card overflow seen during Build.
- PASS, Sizes: all eight required sizes inspected, including 375x812 through a host. Results below qualify any audit leads.
- PASS, No giveaways: clear takes vary among A/B/C, and no ready badge appears until a job's actual rule passes.
  Speaker's word-to-picture matching is explicitly the lesson, rather than hidden-answer diagnosis.
- PASS, Honest numbers: Sound says Listening model on screen; notes give the dB assumptions and projection formula.
- PASS, Standards: choosing, testing, matching, practicing, revising and presenting are performed in the tool.
  Teacher notes connect the model aquarium recount to an actual shared class experience. No family engine applies.
- PASS, Motion off: explicit animation:none and transition:none, plus no hover enlargement; tested calm frame had zero loops.
- PASS, Short choice sets: takes, all six sentences, all six picture targets and all room toggles fit; no hidden scroll tray.
- PASS, Resize mid-animation: full audit clean, with no exceptions or stuck controls. Responsive layout retains state and has no redraw-bound mover nodes.
- PASS, Welcome after first action: no welcomeAfter; mode welcomes have validity, and completed Speaker work gets practice guidance.
- PASS, Unknown as unknown: untouched Camera slots are empty; Sound/Speaker use preview art without granting a Camera check.
- PASS, One look, one meaning: checks mean ready; open circles mean needs work; the star casts the same star-shaped shadow.
- PASS, Badge says what is true: all four badges derive from the same rules as rehearsal. Unfinished Present is not a pass.
- PASS, Hint changes back: mode entry, slide change, test outcome, wrong match, reset and modal close set a fresh next action.
- PASS, No answer by copying words: the prescribed Speaker matching task intentionally connects animal sentences to paintings;
  Camera, listening and room decisions rely on visible or audible effects rather than copied labels.

#### Audit leads

One full audit completed under the 40-minute limit: 12 leads, 95 frames. Sizes, ordinary states, Motion off,
console checks, mid-action resize, held-click focus and five-click narration repetition were clean.

- Leads 1-4: badges and hint reported covered in rehearsal and reset. These are intentional inert backgrounds
  behind native dialogs. Inspected every modal frame; their content and controls fit. Corrected the keep plan to
  test modal content rather than its background. Dialogs now also have their own Read buttons.
- Leads 5-7: the first tap on Take A, B or C speaks its note and skips the welcome. This follows STANDARDS:
  the tap's own line wins, the welcome stays unmarked, and no late welcome lands over the close-up instruction.
- Leads 8-12: quick taps on Camera, Sound, Speaker, Room and Show cut the welcome. Fixed by making a tap on the
  selected mode a no-op. Five separate held double-tap checks returned an uncut welcome in every mode.

Targeted repairs after the audited bundle also passed: Read cancels the custom test clock and later summary;
arrow navigation returns focus to the takes; level changes preserve an active sample and cancel obsolete results;
Keep it cancels reset instructions. Added accessible modal Read and its four ready-row lines to the inventory.
Read dialogs fit at 680x425 and 375x812. Tests confirmed 60 px minimums for the new phone controls.
No second full audit was run. These targeted checks qualify the full-audit evidence above.

#### Frames looked at

- Both bar frames and the full twelve-asset sheet; full-size classroom and octopus redraws inspected.
- All 12 first frames, all 4 logic/keyboard/close-up/sound check frames, all 24 final A/B frames.
- All 8 phone frames and the clean phone-host recheck. The first phone run's favicon 404 belonged to the generated
  host shell; adding a data favicon to that temporary shell made the recheck clean. host.html was removed.
- All 4 targeted frames, all 3 final octopus frames, and feel-comparison.jpg. The compact practice repair was re-shot.
- All 95 audit frames inspected through 17 numbered contact sheets. Post-audit frames: eight first repair
  frames, five mode double-tap frames, two corrected voice-clock checks, and two phone modal Read frames.

#### Art made

Twelve finished images from fourteen built-in image generations. Full house style and asset prompts are in
art/prompts.json; workspace copies are art/raw/*.png and art/*.webp. Source paths are in Scratch/art-paths.json.
Redrew the classroom to remove baked-in chairs and the octopus to show eight individually countable arm tips.
Art is 998,560 bytes, about 975 KiB. Final bundle: 1,421,111 bytes, below 2 MB. Voice inventory: 114 lines.

#### Art still to paint

None. No people were generated.

#### Engine changes wanted

None. Shared kit, documentation, scripts and other tool sources were not edited.

#### Left open

- No recordings by instruction. The fixed science-narrator / Charon inventory uses browser speech at runtime.
- Word highlighting is clock-based, not speech-boundary synchronized. Actual acoustic balance needs listening on
  the intended school device; browser speech cannot be calibrated through the music's Web Audio gain bus.
- Tall portrait Camera takes have heavy letterboxing and small paintings. The enlarged take is the close-reading view.
- The specified 70% octopus crop shows several arm sections rather than a guaranteed literal two; it clearly cuts off
  the central animal. The prescribed transform was kept rather than editing the painting into a misleading clear take.
- No explicit spec open questions were listed. Leaned decisions and implementation choices are noted in handoff.md.

All test Chrome and server processes were closed, ports 9980, 9981 and 8785 verified closed, and host.html removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: field-trip-slideshow

#### Played

Cold K-2 solo and teacher/projector paths completed before reading builder notes or source. Comparing paintings and
watching the room become usable are strong. Rehearsal and the full eight-slide presentation were played.
One review pass, scope kept to this tool and Scratch, no commits. Evidence is in _scratch/field-trip-slideshow.

#### Findings fixed

- Blocker, general, Sound: an interrupted loud test followed by Softer twice granted readiness. A complete six-second
  Sound-on test at one unchanged level is now required. Changes still alter live gain immediately; re-test to confirm.
- Should fix, general, Camera: old-animal praise played against the next animal without identifying the saved slide.
  Feedback now begins "Slide N saved" and the take screen labels the saved subject separately.
- Should fix, general, Room: correct intermediate settings had only a chime, leaving non-readers without spoken state.
  Added setting events, with validity checks; the final ready event remains distinct.
- Should fix, general, sources: BBC WHP 324 does not establish the numeric threshold attributed to it. Notes now
  distinguish illustrative gain and room settings from measured intelligibility and AVIXA compliance.
- Polish, general, Speaker: the flattest moment was passive text-to-picture tapping. Wrong captions visibly return;
  correct ones arrive with a warm stamp. Calm keeps the feedback without motion. Practice events cancel stale speech.
- Should fix, general, Room frames: the screen stretched vertically in portrait layouts. Projection and screen now
  preserve the painted fabric's proportions as the stage resizes; all seven non-phone sizes and the isolated phone recheck pass.
- Polish, general, art: redrew the green-fringed screen-down prop, with richer wall brackets, fabric and metal detail,
  and aligned the live projection with its surface. Preserved the twelve-image style and large paintings.

#### Findings left

- Blocker, general, spec conflict: Camera's prescribed pre-use feedback, Sound's prescribed faces, Speaker's immediate matching
  feedback, and Room's prescribed defaults/checks permit answer-following or trial-and-error completion. See Break it.
  Preventing these shortcuts requires changing the specified learning/assessment design; no new quiz was added.
- Should fix, general, voice: no fixed recordings exist, so the requested Charon voice is not delivered. Recording is
  forbidden in this build/review brief. Browser speech works, but acoustic balance and clock-based word highlights
  cannot be certified as synchronized or calibrated.
- Should fix, general, standard scope: MA:Cn10 is not independently established by a fixed fictional aquarium trip.
  Notes ask the teacher to connect an actual shared experience; a deeper fix needs a spec or catalog decision.
- Polish, general: portrait Camera letterboxes heavily. Three simultaneous takes and 60 px controls were retained.

#### Break it

- Camera: repeat A for all six and sweep A/B/C while always keeping the last take fail. Adaptive search using only the pre-use notes passes.
- Sound: held-click Test, switch mode, return, Softer twice passed before and fails after. Cancel-then-sweep fails.
  Muted testing and last-second level changes fail. Full steady tests pass only at levels 1-3; re-testing works.
  Reading the prescribed face then waiting out a steady test still passes without demonstrating listening skill.
- Speaker: every sentence against every picture, then We practiced, passes before and after. Self-report practice
  cannot establish actual speaking without violating the no-recording rule. Wrong matches never persist as correct.
- Room: one tap on each of the five initially wrong toggles passes. This is mandated by the spec's defaults.
  Repeated cycling changes the actual room, not a stored score. All 108 combinations tested: only the two specified setups pass.
- Rehearsal: no separate score or best score; rows derive from current crew states. Present and End show work even
  unfinished, as required. New show confirms; Keep it preserves work and reset clears every job. No reflection gate exists.

#### Voice walk

Held 120 ms clicks, two-second action pace with full listening pauses: Camera, all six clear takes; Sound, loud test,
Softer twice and a full re-test; Speaker, six matches and practice; Room, all five toggles; Show, rehearsal and Present.
The first connection dropped; one checkpointed retry completed with four ready crews and zero runtime exceptions.
Spoken order: wCamera, per-take notes/saved events, cameraDone, wSound, sample, loud result, softer, sample, clear result,
wSpeaker, card/match events, allMatched, practiced, wRoom, four setting events, roomReady, wShow, ready, six captions, end.
All five mode how-to welcomes started exactly once. hTake and hPicture each started once. No late mode welcome.
Voice log and six frames: voice-main/result.json and voice-main/*.png. Side path: five card events spoken, hPicture once.

| Line | Kind | Expected | Started |
|---|---|---|---|
| Mode welcomes | how | 1 each | 1 each |
| hTake / hPicture, main | how | 1 each | 1 each |
| Five sentence selections, side | event | 5 | 5 |
| hPicture, side | how | 1 | 1 |

#### Facts checked

Sources retrieved live on 2026-11-06; numbers independently recomputed.

- Jellyfish lack a brain and bones; nerve-net explanation: [NOAA Ocean Service](https://oceanservice.noaa.gov/facts/jellyfish.html)
  and [Smithsonian Ocean](https://ocean.si.edu/ocean-life/invertebrates/jellyfish-and-comb-jellies).
- Eight octopus arms and color change: [Monterey Bay Aquarium](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/giant-pacific-octopus).
- Sea turtles surface to breathe: [NOAA Fisheries, Green Turtle](https://www.fisheries.noaa.gov/species/green-turtle).
- Sharks replace teeth throughout life: [Florida Museum, Sharks FAQ](https://www.floridamuseum.ufl.edu/discover-fish/sharks/faq/).
- Male seahorses carry developing young in a pouch: [Smithsonian Ocean](https://ocean.si.edu/ocean-life/invertebrates/pregnant-seahorse).
- Penguins are flightless birds and swim swiftly: [Australian Antarctic Program](https://www.antarctica.gov.au/about-antarctica/animals/penguins/)
  and [Monterey Bay Aquarium](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/african-penguin).
- Speech/background mixing context: [BBC R&D WHP 324, Mike Armstrong, September 2016](https://downloads.bbc.co.uk/rd/pubs/whp/whp-pdf-files/WHP324.pdf).
  Five gains independently recomputed: 0.063096, 0.125893, 0.251189, 0.501187, 1. These are not measured speech ratios.
- Ambient light reduces projection contrast: [AVIXA Image System Contrast Ratio, 2021](https://www.avixa.org/resources/standards/image-system-contrast-ratio).
  Illustrative ratios recomputed: 2.461538, 4.166667, 10.5. Passing this model does not imply AVIXA compliance.
- WCAG palette ratios recomputed: 7.267, 6.713, 14.463, 5.946. Eight bars at 72 bpm in 4/4 last 26.667 seconds.
- Roles, presentation and experience connection checked against [NCAS Media Arts K-2](https://www.nationalartsstandards.org/sites/default/files/Media%20Arts%20at%20a%20Glance.pdf).
  MA:Pr5 and Pr6 are enacted. Cn10 depends on the teacher connecting this model to an actual shared experience.

#### Sensitivity

No cultural, Indigenous, religious or hard-history content. Seahorse father care is animal biology, not a human-family
claim. Families includes caregivers. Notes explicitly allow seated speaking practice. All people flags are false;
empty Room is a setup scene with the specified star/microphone surrogate, so no person is missing from an active role.

#### Flattest moment left

Practice is still an adult-mediated physical activity, confirmed by a button. A solitary child can skip the speaking.

#### Graphics

All twelve assets inspected as a set; six animal paintings, entrance, classroom and equipment retain one painted style.
Screen-down redrawn once with built-in imagegen, prompt in art/prompts.json, raw and finished files in art/.
No placeholders or missing art tokens. Art 1,002,206 bytes; bundle 1,435,522 bytes (1,402 KiB).
No external resources or media capture calls. All six Camera paintings were inspected at final use size.
Runtime line inventory matches voice/lines.json exactly, 152 lines. Every authored source line is under 160 characters.

#### Audit

One audit only, Chrome 9951 and host 8755. The process hit its 40-minute cap; Windows denied the stop request.
Audit not finished within the limit: the final diagnostic report arrived about 43 seconds later during cleanup.
Final report: review-audit/audit.md, 85 leads. Seven non-phone sizes, modes/states, Motion off, focus, five-click
repetition, quick taps and the eventual resize section were clean. The cap overrun is not a within-limit PASS.
82 phone leads were invalid: 127.0.0.1:8755 served Box Plot Builder, confirmed by frame and directory listing.
The other 3 leads are permitted first-tap Camera welcome skips (BASELINE 16); the hint and Read retain the instruction.
All 91 audit frames opened on 16 sheets. Scoped repairs then re-shot Room at all seven non-phone sizes; a live
1366 to 760 to 1366 resize during the light change kept screen proportions and readiness, with zero exceptions.
An isolated 127.0.0.2:8755 host verified twelve actual-tool phone states: all targets at least 60 px, no below-fold
controls, clipped hints or sideways scroll. Frames in phone-check/ and room-proportions/ were opened and inspected.
No second full audit. Review Chrome instances and the isolated server are closed; the unrelated server was untouched.

#### Left open

Spec-level shortcut/self-report conflicts and MA:Cn10 scope; unrecorded narration and a physical-device listening check.
Chose the specified teacher-led preparation flow over adding an assessment or topic, per the unattended brief.
The octopus crop follows the required 70 percent shift; it shows three arm sections rather than literally two.
No spec edit, kit change, new topic, upload, recording, or git commit. Audit cap/stop failure documented above.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Field Trip Slideshow build handoff

Built in S:/CurioClass-codex for a teacher-led K-2 aquarium recount. Build only, no commit and no polish round.

#### Structure

src.html starts from kit/starter/src.html and uses kit:curio CSS and JavaScript. Responsive CSS lays out real boxes,
without scaling a fixed desktop scene. All five mode sections and their controls persist in the DOM. Render functions
update pictures and labels inside controls while retaining the buttons. A single art map avoids duplicate image data.

The script groups slides and take orders, state, room options, fixed narration, voice, crew renderers and actions,
the rehearsal rules, the audio bus, and bindings. window.__tool exposes the state, content, rules, actions and voice log.

#### Important behavior

- Clear takes are B, C, A, C, B, A. Every slide also has blur and its specified problem. Problem takes can be kept.
- Enlarging a take hides the slide strip to give the picture and two choice buttons enough space at 680x425.
- The camera strip and the two slide arrows wrap around; Show has a title, six slides, and a thank-you slide.
- Speaker cards precede picture targets in keyboard order and visual order. Wrong matches return the card.
  Tapping a matched picture with no sentence selected returns its card and clears practice, allowing revision.
- The selected takes appear in Sound, Speaker, Room's first slide and Show. Unchosen takes use the clear painting
  as an editing preview, but rehearsal and crew badges still require an actual Camera choice.
- Sound is ready at level 1-3 after a complete six-second test at one unchanged level with Sound on.
  Changing levels, interrupting, restarting, Read, or leaving the mode cannot turn an unfinished test into readiness.
  Softer and Louder still ramp the live music immediately; re-test afterward to confirm the new balance.
- Every room control cycles immediately. Light wash fades for 400 ms with Motion on. The only passing room states
  are Dim or Off, Down, Face the screen, Beside the screen, Medium.
- Present works with unfinished work. Missing Speaker matches show a reminder instead of pretending a card was placed.
- New show confirms. Keep it preserves the choices. Yes clears every crew. Nothing about the show is persisted.
- Tapping the already selected mode is a no-op, so a quick second tap cannot cut its welcome or reset the show.

#### Art and layout

All twelve assets were generated with the built-in image tool using the house style and prompts in art/prompts.json.
The raw PNGs are in art/raw; scripts/art.py field-trip-slideshow --rekey NAME makes the finished WebPs for free.
The classroom was redrawn once to remove baked-in chairs. Three rows of painted blue chair cutouts alone show direction.
The octopus was redrawn once to make all eight arms separately visible. Its corrected eight tips were counted at full size.
Original provenance paths, the earlier classroom and comparison sheets are in _scratch/field-trip-slideshow/.
There are no people in the pictures. The star and microphone marker is the specified speaker surrogate.

The paintings use contain inside dark screen frames so a clear animal is never accidentally cropped by layout.
This causes substantial letterboxing in tall portrait Camera takes, especially on phones. Tap a take for a larger view.
Compact landscape Speaker uses two adjacent grids; phone Speaker stacks cards above pictures. Practice has a compact
icon and spacing to keep the main button above the hint. Room controls stack below the scene in tall narrow layouts: one column on phones, two at 760 wide.

#### Voice and audio

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

#### Spec questions and decisions

The spec contains no explicit open-question section. Its leaned choices were kept: teacher-led crew work, a true
aquarium recount, paintings instead of uploads, an eight-bar aquarium loop, Present allowed before all checks pass,
and nothing saved. Tap-then-picture is the specified alternative to dragging in Speaker.

The listed room contrast and palette values agree with independent calculations after rounding. No spec edit was made.
The three camera takes stay side by side even on phones; their full animal frames are preserved with letterboxing.

#### Verification and next review

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

#### Engine changes wanted

None. No kit, documentation, script or other tool source was changed.

#### Cold review repairs

Preserved the paintings, palette, five crews and teacher-paced show. Saved Camera feedback now names the saved slide,
and a small Saved label distinguishes it from the next subject on stage. Speaker gives a visible returning caption
on a wrong picture and a warm arrival stamp on a correct one. Motion off removes movement but keeps feedback time.
Correct Room changes now speak their new setting rather than leaving a non-reader with only a chime.
The screen-down prop was redrawn with the built-in imagegen tool, saved to art/raw/screen-down.png, and rekeyed using
art.py --rekey. Its landscape fabric aligns with the live projection; no people are needed for an empty setup scene.

#### Review limits requiring a spec decision

The specified matching feedback permits exhaustive trials, and the specified Room defaults can be fixed by one tap
on each control. We practiced is self-report and no microphone is allowed. These checks describe preparation only;
they do not establish independent mastery. Preventing those shortcuts would require a different assessment design,
which this review is not authorized to add. No score or best score is stored.
BBC WHP 324 does not substantiate a numeric ten dB threshold. Notes now distinguish the illustrative gain steps and
room-pass settings from actual sound intelligibility or AVIXA compliance. Device listening remains necessary.

#### Sensitivity

No cultural, Indigenous, religious or hard-history content. Seahorse fathers' brood-pouch care is an animal biology
fact, not a model for human families. Families can mean any caregivers; the practice wording can be spoken while
seated and does not require every child's body to stand. All twelve art assets are animal or equipment scenes.

#### Review audit and final geometry

The single audit reached its 40-minute cap; Windows denied the process-stop request. Its final report arrived about
43 seconds later during cleanup, with 85 leads: 82 invalid phone-host leads and 3 permitted first-tap welcome skips.
Port 8755 on 127.0.0.1 was serving Box Plot Builder. It was left untouched. An isolated host on 127.0.0.2:8755
verified this tool instead, with twelve phone states, 60 px targets, no below-fold controls or clipped hints.
The audit recorded clean size/state, focus, repetitions, double taps and resize checks for the actual tool; the cap
overrun remains a process failure, not a within-limit pass. All 91 audit frames were inspected on sixteen sheets.

layoutRoomProps now sizes the lowered screen from its natural image ratio and fits the projection to its fabric.
A ResizeObserver updates that geometry; narrow Room layouts put controls below the painted scene to avoid floating
chairs against a tall cropped wall. Seven non-phone screen-aspect checks passed, followed by the phone recheck.
No second full audit was run after these scoped frame repairs. Voice order and line text did not change.

Final scoped checks: twelve actual-tool phone states passed with all controls at least 60 px and hints inside 812 px.
The final Room layout was also flipped from 1366 to 760 and back during the light fade, with stable natural screen
proportions, unchanged readiness, and zero exceptions (room-proportions/resize-result.json). All review Chrome ports
9950, 9951, 9953, 9954, 9955 and 9956 and the 127.0.0.2:8755 host were verified closed. No tool host.html remains.
The unrelated 127.0.0.1:8755 server was not stopped or changed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
