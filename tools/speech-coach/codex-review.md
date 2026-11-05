# Codex review: speech-coach

## Played

Cold Grade 12 solo play before opening the builder's report, handoff, notes or source: all sample cards, Thread/Listener test, a complete rehearsal, listener marks and Review. Then checked the teacher projection view, own-talk entry, tasks, slide kinds and extremes. The room, cue and immediate Next response are strong; the original table-first finish felt flat.

## Findings fixed

- Should fix, general, Review: simultaneous listener marks hid one another. Separate marks and explicit section-relative seconds preserve each observation.
- Should fix, general, Compare runs: each strip previously filled the same width regardless of duration. Both now share a labeled seconds scale.
- Should fix, general, time limits: fractional overruns could say "at the limit" while self-check said No. Review and notebook now use exact elapsed time and name sub-second differences.
- Should fix, general, Build: section actions fell below the editor fold. Docked actions, scrollable fields, and a signpost-first compact editor keep the frequent work visible.
- Should fix, general, planned time: entered values could disagree with the clamped model. Whole-second values normalize on commit.
- Should fix, general, Reading slide: rounded percentages suppressed a warning just above 60 percent. Test the exact fraction; keep the sample's 98 percent display and label the close boundary "over 60 percent".
- Should fix, general, hints: changing task in Rehearse/Review gave Build instructions; dismissing Thread left its hidden-box instruction. Hints now follow the current mode and dialog state.
- Should fix, general, voice/craft: several fixed Read hints were absent from the voice catalog. Catalogued all 18 fixed narration/hint strings; Thread now names Compare after typing and Back to desk after comparing, without extra automatic speech.
- Should fix, general, lifecycle: hiding the page during countdown could start an unattended run. Cancel countdown and release the mic.
- Polish, general, Review payoff: surfaced the selected run's fastest section or too-brief busy slide, a synchronized change note and a direct route to revise that section.
- Polish, general, art: repainted the ornate theatre as a rich school auditorium, keeping velvet, stage light and depth. Museum captions now have dedicated dark bands that preserve the whole artwork.
- Polish, general, teaching: labeled Other side as a structure check, rather than implying the code reads the script's actual answer.

## Findings left

- No known implementation blocker or should-fix remains after the scoped rechecks. Spec-owned limitations remain under Left open.
- Polish, general: long writing forms, detailed slide data, utility buttons and the run notebook scroll; these are authoring/data surfaces, not hidden answer choices.

## Flattest moment left

Writing a full original talk remains quiet work. The new Review prompt makes the next revision concrete; no game reward or new topic was added to this Grade 12 rehearsal tool.

## Graphics

All four images inspected at displayed size. Retained the three supplied museum works and their people tags; the historic art deliberately differs from the editorial auditorium, as the spec requires. One auditorium redrawn using the built-in imagegen tool; prompt and final asset are in art/prompts.json and art/sc-empty-house.webp. No new people, missing art tokens or downloaded media. Art: 434 KiB; final bundle: 708273 bytes on disk, about 692 KiB. Compared beside Beat Lab in _scratch/speech-coach/review-finish-comparison.png; retained the rich finish. Both reference bundles were opened read-only.

## Audit

One final audit completed within its 40-minute limit, Chrome 9931, host 8735: 57 leads. Every lead is answered in _scratch/speech-coach/review-audit-responses.md. Fixed five navigation/focus groups and addressed three slide-choice groups; retained 32 authoring/utility and two table-scroll groups, confirmed eight expected modal-cover groups, disproved two changing-timer-label comparisons, and explained five correct first-tap welcome substitutions. Ten five-tap and ten quick-tap checks were clean. Explicit states cover all modes.
The final scoped recheck passed real held navigation, Add/Clear/Reset focus, both navigation limits, exact Reading thresholds and Thread hints. A real resize after every Next left the run selector enabled with no exceptions. The full audit was not rerun after these narrow repairs. Inspected all 43 audit PNGs on 11 labeled sheets, alongside the direct full-size review frames.
Independent checks: 295 words; planned 120 seconds; Slide 5 has 47 words/98 percent; scripted boundaries give 108/140/180/136/140/168 words per minute, total 125 seconds. All required sizes viewed, with no horizontal page overflow. Keyboard-only Start/F/P/Space/finish passes. Synthetic microphone path counts one long pause and ends all tracks. Nine actual completions retain eight runs across reload. Motion off keeps the three-second count; grayscale remains legible.

| Line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| busy, five held taps at 2 seconds | how | 1 | 1 |
| runsaved, five completed runs | event | 5 | 5 |
| over, five completed over-limit runs | event | 5 | 5 |

Start cuts the welcome and empties the voice queue. Read works with Sound off and releases promptly on mode change. First plain tap and Sound re-enable bring one welcome. All 18 catalogued strings exactly match voice/lines.json. Fullscreen, phone-host, source and voice evidence live in _scratch/speech-coach/review-*.

## Left open

- Browser narration remains fallback; no audio was recorded. Physical microphone hardware/native permission UI were not exercised; synthetic stream, calibration, pause counting and lifecycle were checked. The specified first-two-seconds calibration can include the speaker's voice, so quiet counts remain estimates, not recognized spoken pauses.
- Spec tension: the sample answers the objection inside its Other side script but its role/link heuristic still asks for a separate structural answer. Kept the specified sample and test, disclosed the heuristic on screen and in notes.
- Spec wording says choosing a different slide job may fix competition, but changing a job alone cannot reduce Busy/Reading token counts. Kept the mandated voice line and thresholds; wording change belongs to the spec.
- The AIC object page blocked direct access; its supplied clock metadata remains unchanged. Other museum, CDC, AAP and California primary-source checks and access limits are recorded in review-sources.md.
- Process exceptions: the opening read and one final utility check lacked explicit hard shell deadlines; the other commands were bounded. No commits or writes to other tool folders. Owned Chrome processes are closed, ports 9930/9931/8735 are closed, and host.html is absent.
