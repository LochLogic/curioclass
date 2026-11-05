# Codex review: music-history-radio
## Played

Cold Grade 9-12 solo run before builder notes: all twelve stations, Compare / Flip, desk Random / Reset,
all six Mystery rounds; then projector, keyboard, jittered knob, grayscale, Motion off and hosted-phone checks.
No git commits were made. The painted radio feels substantial. The hidden-station reveal is the strongest interaction. Chrome stayed muted.

## Findings fixed

- Should fix, general, Mixing desk: tempo followed Sound rather than Beat; fixed the actual tempo / free-rhythm label.
- Should fix, general, mixed feature panel: source-era prose promised absent drums / accompaniment; now describes
  the combination and melody instrument, and labels notation as an era reference rather than the mixed score.
- Should fix, general, Compare: removed the invented metronomic tempo for chant.
- Should fix, general, conductor: a late request could miss the next boundary; commit now happens at the boundary.
  A change 70 ms before it passed. Tuning now cancels a queued Flip; the cancellation regression passed.
- Should fix, general, Mystery: recap was below the fold; moved reveal / personal six-choice recap to panel top.
- Should fix, general, graphics: postcards were cropped to strips; restored complete 4:3 compositions.
- Should fix, general, cultural content: distinguished Sundanese / Javanese artists at the 1889 fair from this
  Javanese-inspired model. Retained sourced living-tradition framing and explicit simplified-tuning disclaimer.
  Owner station: Javanese gamelan, Indonesia, retained with Smithsonian / UNESCO sources in notes.md.
  Fresh independent cultural / people-art review: PASS, refine/sensitivity.md.
- Should fix, general, notation: corrected diatonic spacing, low-C ledger lines, dotted halves, lead-sheet chords
  and four-bar eighth-note kick / snare positions. These remain simplified teaching sketches.
- Should fix, general, narration: fixed Read phrases now appear in allLines and voice/lines.json;
  Read starts with the current hint, paused hints name Resume, and returning to Dial restores the needle.
- Polish, general, weakest art: repainted the empty hip hop party with a woman DJ and a natural community,
  including a wheelchair user. Full prompt in art/prompts.json; people: true; built-in imagegen, then art.py --rekey.
- Should fix, general, audit frames: overlapping dial years at 1000 pixels now have a readable scrolling rail;
  real pointer drags map to the visible rail. Final compact / laptop / phone checks found at least 19 px between labels.
- Should fix, general, live counter: eight melody phrases are now called phrases, avoiding the false eight-bar
  count in organum. Its fourteen notated measures are explained in notes.md.
- Should fix, general, rapid voice: quick Station taps preserve still-valid Power-off instructions.
  A first Compare tap names Power; Compare followed by Station also keeps that instruction intact.

## Findings left

No confirmed blocker or should-fix remains. The by-ear criterion is unverified, as detailed under Left open.

## Flattest moment left

A desk choice can wait through the current phrase. The pending border / next-bar label answers immediately;
keeping the next musical boundary is part of the specified comparison, so this delay remains.
The former flat finish now shows the student's six guesses, actual anchors and gaps together.

## Graphics

All fifteen paintings checked, including cutouts, final postcard compositions and cultural accuracy.
One postcard redrawn; no missing art tokens. The other fourteen paintings, including radio, room and knob, retained.
Finished art 530.9 KiB; final bundle 883.8 KiB, below the 2 MB goal.
Both bar tools bundled only into Scratch and opened. review-feel-comparison.jpg places this tool beside Beat Lab.

## Audit

The single 40-minute-limited review-audit completed: 76 frames, six leads. Every frame was opened in sheets;
the crowded 1000-pixel dial and affected repair frames were also opened individually.
Two real leads, rapid Previous / Next welcome cuts, fixed and re-shot with uninterrupted voice logs.
Four expected behaviors: Power / Compare skip a welcome for their own line; Pause cuts its ident at once;
Reset at the default is unchanged. Compare now speaks the Power instruction, and Reset after real work passed.
Sizes, listed states, Motion off, focus, runtime and resize checks were clean. Five-repeat voice checks were clean.
Only affected frames followed the audit: rapid taps, first Compare, Reset, dial spacing / dragging and phrase label.
No second full audit was run. All final focused shots had zero console warnings or exceptions.
Independent arithmetic: 24 notes, eight four-beat source bars, sixteen strong-beat chord tones,
42 organum beats / fourteen measures, 1,728 mixes / 232,380 finite events, every loop under 30 seconds.
Contrast: brand / panel 8.06, ink / panel 13.03, muted / panel 6.71, dial 12.03, needle / cream 4.97.

| Voice with held taps | Expected starts | Observed |
|---|---:|---:|
| Chant ident, how | 1 | 1 |
| Organum ident, how | 1 | 1 |
| Ragtime result, event, five repeats | 5 | 5 |
| Welcome, two rapid Station taps, each direction | 1 | 1 |

Read interruption and Sound-off Read recovered without a stale queue. State changes intentionally cut stale lines.

## Left open

- By-ear historical timbre / balance certification was not performed: mandated Chrome checks are muted.
  Plan / timing / runtime evidence is not a substitute for Done when 1's by-ear criterion.
- No narration was recorded. Browser speech cannot guarantee the requested news-reader voice character.
- Spec arithmetic: 24 durations of .4-.9 seconds range from 9.6 to 21.6 seconds, not 23.6 before the gap.
- Phones intentionally scroll secondary feature content below the radio. No set results are saved.
- One early phone wrapper requested a missing favicon; fixed for the final host. No tool request caused that 404.
- Process exception: the initial read-only rules command lacked an explicit timeout and finished in 0.1 seconds.
  Subsequent commands were bounded. All started Chrome / host processes were closed; host.html was removed.
