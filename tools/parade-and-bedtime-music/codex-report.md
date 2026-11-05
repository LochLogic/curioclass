# Codex report: parade-and-bedtime-music

## Built
- Sort: eight original synthesized tunes, four painted moments, Somewhere else, tap and real drag placement,
  ten clue chips, earned badges, a gentle composer reveal, one class favorite, and confirmed reset.
- Turn it: looping Big Drum March, live Speed and Loudness dials, a spatial street-to-bedroom reveal,
  beat-driven drum and teddy, mood meter, March again, keyboard controls and shared Read / Sound / Motion.
- All requested build files are present. No git commit, branch change or polish round.
- The report was written last to honor the user's explicit stop-on-report instruction.

## Numbers check
- Independently recomputed in `_scratch/parade-and-bedtime-music/number-check.py`; results in `numbers.json`.
- Tune lengths: 10.909, 12.414, 8.000, 8.571, 6.667, 7.500, 11.429 and 13.714 seconds.
- March at 50 bpm: 19.2 seconds. Gains at levels 1, 5, 9, 10: .080, .195312, .476837, .596046.
  Dynamic span: 17.4438 dB. Start meter .833333; both mixed extremes .5; endpoints 0 and 1.
- All supplied high/low note-attack fractions check out. All supplied contrast ratios check out:
  white/brand 8.770, brand/paper 8.106, ink/paper 15.504, muted/paper 6.360.
- Difference: Tune 5 at 108 bpm is Fast under the stated >=100 rule, despite middle in the supplied table.
  The computation wins, as CODEX-BUILD directs. spec.md is untouched; notes and handoff explain it.
- Difference: Tune 8 exceeds the summary's 13-second ceiling. Its full written 16 beats are retained.

## Feel check
- Walked the full listening flow: all eight tunes finished, placements were made, clues and a favorite chosen,
  modes switched, the scene changed through both boundaries twice, and Keep it / Start over were exercised.
- Best moment: the same march notes continue while the bedroom enters from the right and the teddy takes over the movement.
- Flattest moment 1: the first mixed scene looked like two ghosted pictures. Replaced full-frame opacity with a spatial reveal.
- Flattest moment 2: a compact clue tray squeezed the painted scenes. It now opens over them with all ten choices together,
  then Scenes returns to the full painted grid. The phone uses the same clear, large-target tray.
- Compared against both bundled reference tools. The side-by-side frame is
  `_scratch/parade-and-bedtime-music/bar-comparison.jpg`; the tool does not look plainer than Snowy Mail Route.
- All Chrome checks were muted as required. Headphone review of the instrument balance is still open.

## Done when
1. PASS: 1366x768 and 680x425 scene grids and Turn it controls viewed. All visible controls measured at least 60 px.
2. PASS for implementation and timing: all exact melody events, tempos and gains checked; all eight full runs finished.
   Replacement tunes stop the preceding transport. Audible timbre quality remains for headphone review.
3. PASS with the documented Tune 5 correction: all 80 chip choices across the 40 pairs match independent expected results.
4. PASS: real jittered drag and held taps; tempo state updated in .5 ms in the recorded check, preserving beat position.
   The next brass and snare events were scheduled at 110 bpm. Only 100 ms is scheduled ahead; unstarted nodes are canceled.
5. PASS: two stopped-at-boundary trips each into Bedtime and Parade logged four spoken event lines.
   Rapid continued turning correctly expires queued lines after a further dial change.
6. PASS: (140,1) and (50,10) both returned .5 and displayed In between.
7. PASS for queue behavior: Sort starts no narrator line during music; wrong clues speak before replay.
   How lines were spoken once in the multi-action run. FAIL for the exact requested voice: recordings are pending.
8. PASS: any scene and Somewhere else accept every tune. Composer reveal names the intended moment without wrong feedback.
9. PASS: Sound off mutes the music bus and displays its hint while timing continues. Motion off has no prop movement
   or infinite animation, and switches among three scene states. Read follows the kit's explicit speech override.
10. PASS: no external resources or network API calls in the source or bundle. No class work is stored.
    Shared kit Motion preference storage remains, as required by STANDARDS.

## Wave lessons
- Hint and voice: PASS. Immediate hints name controls, Read uses the current hint, queue validity follows the mode and step.
- Focus and layout: PASS. Outer buttons persist, deliberate focus prevents scrolling, and compact tray focus is contained.
- Sizes: PASS on the full set: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe.
- No giveaways: PASS. Intended moments are hidden until Composer's note. Shape marks convey identity, never an answer.
- Honest numbers: PASS. Original notes and computed values are retained; equal meter weighting is named in its tooltip and notes.
- Standards: PASS for teacher-led scope. Expressive clues, personal preference with a reason, and everyday connections are practiced.
- Motion off: PASS. No infinite CSS animation or JavaScript prop movement; music duration stays unchanged.
- Short choice sets: PASS. All ten clues stay visible together; no short choices hide in a scroll panel.
- Resize mid-animation: PASS. Full audit found no exceptions or controls left disabled after resizing every reached state and walk control.
- Welcome after first action: PASS. Two-mode welcome validity and first-tap suppression use Curio.voice; no welcomeAfter.
- Unknown as unknown: PASS. No intended-moment label appears before reveal; badges appear only after earned clues.
- One look, one meaning: PASS. Consistent tune shape marks, paired clue icons and a single favorite heart.
- Badge says what is true: PASS. Badges are earned from the verified table, including the computed Tune 5 Fast correction.
- Hint changes back: PASS. Mode, stop, reset, close-tray and Read-pause paths update the current action.
- No answer by copied words: PASS. Students hear original music before naming a clue; scene placements have no right/wrong score.

## Audit leads
- Full audit completed normally, once, using Chrome 9981 and host 8785. Report: `_scratch/parade-and-bedtime-music/audit/audit.md`.
- Sizes, reached states, Motion off, resize stress, console checks, settled focus and five held clicks at a 2 s pace were clean.
- Leads 1 to 8, Tune 1 through Tune 8 welcome not heard: intentional. A first tap plays its tune immediately;
  the specified Sort welcome becomes stale once a card is tapped, and narration must not compete with music.
- Lead 9, Somewhere else welcome not heard: intentional. Its first-tap instruction names the needed tune card and scene,
  so Curio.voice correctly skips the welcome without marking it heard.
- Leads 10 to 13, Bedtime, Parade, Birthday and Rainy day welcome not heard: same required first-tap own-line behavior.
- Lead 14, Start over welcome not heard: the reset question takes precedence on that first action, as specified.
- Leads 15 and 16, quick Sort and Turn it taps cut the welcome: fixed. Re-selecting the current mode now leaves its speech
  and work alone. Targeted held double taps at .7 s confirmed one whole welcome per mode, with no cut entry.
- Two additional build fixes received targeted checks: a placed tune's end reopens its clue tray and names the next action;
  numeric shortcuts retain focus on the replay card, then on a clue when stopped. Read's paused hint follows placement state.
- The full audit was not rerun after these focused fixes. Wide and compact end states and shortcut focus were rechecked.

## Frames looked at
- Both reference frames, all four quick frames, all 23 full-run frames, three phone frames, the deep-check frame,
  four session frames, all six finished artworks and the bar comparison.
- Full-run frames were viewed in seven labeled contact sheets; phone views, key interactions and session frames
  were also opened at full size. Every claimed generated PNG was viewed.
- Viewed all 41 audit PNGs in 11 labeled contact sheets and the six final targeted frames.

## Art made
- Six built-in image-tool illustrations, 574.35 KiB total finished art. Bundle: 1,293,095 bytes, about 1,262.79 KiB.
- Four watercolor scenes, one toy drum and one teddy; no generated people. No image needed a redraw.
- Drum and teddy received a second keying pass with despill. The parade background is about 197 KiB,
  above the suggested per-background target, while the total bundle remains well below 2 MB.
- Prompts are in art/prompts.json; original PNGs in art/raw; all generated assets are credited in draft metadata.

## Art still to paint
- None.

## Engine changes wanted
- kit/curio.js, voice / speakOne and init: optional speech-volume callback applied to clip volume and utterance volume.
  Crossing narration should track selected music loudness. Current tool ducks the music by 6 dB, but browser speech
  remains at normal speech volume because the public kit API has no volume hook. Full detail is in handoff.md.

## Left open
- Friendly-dad / Achird recordings: 47 fixed lines are manifested and match runtime allLines, but no audio was recorded,
  as the build instructions require. Browser narration is the current fallback.
- Speech-to-music volume matching needs the kit extension above. Full headphone review remains for cold review.
- Compact tray presentation and the persistent replay row are explicit layout adaptations documented in handoff.md.
- drive.py's iframe host requests favicon.ico and logs a 404 outside the tool. Its top-level host is temporary;
  the bundled tool has a data favicon and no external requests. The audit intentionally filters this known host artifact.
- No audit-confirmed layout or runtime repair remains. The final focused fixes have targeted evidence; a fresh full audit
  and the already planned cold review can independently check the final bundle.
