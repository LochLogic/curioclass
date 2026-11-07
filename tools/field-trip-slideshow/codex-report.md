# Codex report: field-trip-slideshow

## Built

- All five modes: Camera, Sound, Speaker, Room, Show. Four crew badges, an actionable rehearsal, teacher-paced
  presentation, thank-you slide, synthesized applause and confirmed reset. One offline HTML file from the kit starter.
- Teacher-led K-2, MA:Pr5, MA:Pr6, MA:Cn10. Tap a sentence then a picture is the spec's alternative to dragging.
- Twelve finished generated paintings, no people. Draft metadata stays stage built. No commit or polish round.

## Numbers check

- Independently recomputed in Scratch/prepare.py and numbers.json before implementation.
- Gains: 0.063096, 0.125893, 0.251189, 0.501187, 1.000000 at -24, -18, -12, -6, 0 dB.
- Room contrast: 2.461538, 4.166667, 10.5 to 1. These agree with the spec's rounded values.
- WCAG palette: white/brand 7.2668, brand/paper 6.7132, ink/paper 14.4635, muted/paper 5.9463 to 1.
- Six unique captions, six slides, three takes each. Eight bars at 72 bpm in four beats per bar take 26.6667 seconds.
- Logic checks covered all 36 sentence pairs and all 108 room combinations. Exactly two room states pass,
  differing only in Dim versus Off. No spec edit or numerical correction was needed.

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

- Both bar frames and the full twelve-asset sheet; full-size classroom and octopus redraws inspected.
- All 12 first frames, all 4 logic/keyboard/close-up/sound check frames, all 24 final A/B frames.
- All 8 phone frames and the clean phone-host recheck. The first phone run's favicon 404 belonged to the generated
  host shell; adding a data favicon to that temporary shell made the recheck clean. host.html was removed.
- All 4 targeted frames, all 3 final octopus frames, and feel-comparison.jpg. The compact practice repair was re-shot.
- All 95 audit frames inspected through 17 numbered contact sheets. Post-audit frames: eight first repair
  frames, five mode double-tap frames, two corrected voice-clock checks, and two phone modal Read frames.

## Art made

Twelve finished images from fourteen built-in image generations. Full house style and asset prompts are in
art/prompts.json; workspace copies are art/raw/*.png and art/*.webp. Source paths are in Scratch/art-paths.json.
Redrew the classroom to remove baked-in chairs and the octopus to show eight individually countable arm tips.
Art is 998,560 bytes, about 975 KiB. Final bundle: 1,421,111 bytes, below 2 MB. Voice inventory: 114 lines.

## Art still to paint

None. No people were generated.

## Engine changes wanted

None. Shared kit, documentation, scripts and other tool sources were not edited.

## Left open

- No recordings by instruction. The fixed science-narrator / Charon inventory uses browser speech at runtime.
- Word highlighting is clock-based, not speech-boundary synchronized. Actual acoustic balance needs listening on
  the intended school device; browser speech cannot be calibrated through the music's Web Audio gain bus.
- Tall portrait Camera takes have heavy letterboxing and small paintings. The enlarged take is the close-reading view.
- The specified 70% octopus crop shows several arm sections rather than a guaranteed literal two; it clearly cuts off
  the central animal. The prescribed transform was kept rather than editing the painting into a misleading clear take.
- No explicit spec open questions were listed. Leaned decisions and implementation choices are noted in handoff.md.

All test Chrome and server processes were closed, ports 9980, 9981 and 8785 verified closed, and host.html removed.
