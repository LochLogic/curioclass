# Codex report: scarf-juggling-ladder

## Built

Six distinct scarf demonstrations, Slow/Real speed, Step and cue holds, mirrored hands, practice countdown,
60-second timer with one extension, partner count/drop/undo, local tries, goals, cue checks, reset reflection,
and guided chart reading with Ren's separate fictional log. All six rungs stay open.
Kit starter and Curio.voice used. No shared code changes, commits, uploads or polish round.
All build artifacts are under the named tool; helpers, evidence and reference bundles are in its Scratch folder.

## Numbers check

`numbers.py` independently confirms sample session bests 2, 3, 2, 5, 7; dip S3; goal first met S4;
cue Got it counts 13/15, 6/15, 10/15; reset helped counts 5 and 2. Axis floor 10, values 0-99.
All 10,000 possible integer first/latest pairs were checked against the two-unit up/down rule.
Contrast recomputation: ink/paper 15.07, muted/paper 6.29, brand/paper 7.33, white/brand 7.90,
focus/paper 4.80, muted/white 6.78; scarf contrasts 3.30, 4.80, 4.26. These match the spec's rounding.
Seeded 10,000-learner recomputation: growing up 85.15%, same 14.59%, down 0.26%; flat up 17.57%,
same 64.89%, down 17.54%. The spec gives no seed; these support its approximate rates, not exact tenths.
The suggested rung goals and 60/10/30-second rules are design choices, not performance norms.

## Facts checked

- Middle grip, palm down, high release, palm-down claw, cross-body release, three-scarf finger grip and starting
  with the hand holding two: [Alberta Education A(K-3)13](https://education.alberta.ca/media/3402228/physicaleducationonline/teacherresources/ToolBox/a_k_3/a_k3_13.pdf).
- Two scarves make an X; throw, throw, catch first, catch second:
  [Maine State Library scarf sheet](https://www.maine.gov/msl/libs/services/documents/scarfjugglingsheet.pdf).
- Next toss at the prior peak: [Gopher/Dynamic PE ASAP, Juggling Lesson Plan 1](https://www.dynamicpeasap.com/pages/secondary-lesson-plans/juggling/juggling-lesson-plan-1/).
  Bethel and Gopher's additional progression sources remain credited from the supplied spec.
- Throw-first coaching and learning a cascade in stages: [Circomedia, Juggling 3 Scarves](https://www.circomedia.com/juggling-3-scarves/).
- Adults practiced for three months; motion-processing regions changed, then changes reduced after stopping:
  [University of Washington, summarizing Draganski et al. 2004](https://faculty.washington.edu/chudler/jugg.html).
  Teacher notes explicitly distinguish the adult three-ball study from this child scarf activity.
- Distributed motor practice: Shea et al. 2000, Human Movement Science 19:737-760,
  [doi:10.1016/S0167-9457(00)00021-X](https://doi.org/10.1016/S0167-9457(00)00021-X), and Lee and Genovese 1988, as supplied in the spec.
- Throwing/catching and goal/strength/reset indicators: [SHAPE America 2024, 1.5.10, 1.5.12, 4.5.6, 4.5.7, 4.5.9](https://shapeamerica.org/standards/pe/new-pe-standards/).
- Clear arm space is the spec's setup rule, consistent with Circomedia's flailing-arm caution. No catch height is prescribed.
- Privacy statement checked against implementation: no remote resources, fetch, analytics or transfer feature; localStorage is guarded.
- Ren, all sample counts, coaching resets, goal thresholds, chart categories and ready suggestions are explicitly fictional or tool rules.

## Break it

- Entering 99, mashing plus, logging zero and entering a goal twice: accepted only as personal observations.
  Values stop at 99; nothing unlocks and no comparison score exists. Ready is a suggestion, as the spec requires.
- Attempted Save below ten seconds: rejected by entry creation and again by Save. Countdown-only Done early logs nothing.
- Partner counter: 2,187 seven-action sequences independently checked catches, drops and undo. Longest run and prior
  best restore correctly across an undone Drop. 120 catches cap at 99. Real-pointer runs 4 then 10 yielded best 10.
- Repeated +30 s: second press has no effect; total stays 90. Stop invalidates pending work and saves no try.
- Biggest/last/random dot shortcuts: a wrong first-session dot records false and explains the actual best.
  Two numbers stay hidden until both selections. The detailed spec explicitly advances after an explained wrong tap.
- All sentence options, always-up and fixed-position strategies: one attempt; cards shuffle; all 10,000 value pairs checked.
  Wrong down on Ren cannot be changed to up by another tap. No correct-completion score is stored.
- Lowest-dot dip shortcut: session 1 rejected; only a session whose best fell from its predecessor is a dip. Ren accepts S3.
- Goal already reached or edited after results: result is recomputed from matching-rung tries; edits show Changed on session N.
  Missing goal sessions get an empty labeled band so the flag cannot silently land in another session.
- Cue/random-reset shortcuts: not scored. Tallies hidden before both picks; sample tallies and Yes counts verified.
  A little is separate, ties are explicit, and no selection claims a universally best reset.
- Sample contamination, clear cancellation and blocked storage: sample leaves personal tries alone; Keep it preserves data;
  Clear requires the dialog; blocked reads on load and later blocked writes both show the session-only warning.

## Voice walk

Muted Chrome, 120 ms held presses and a two-second action pace. Full real-time practice minute completed.
Main heard order: cue1-0, cue1-1, cue1-2, afterShow, breathe, go, dropPartner, half, ten, time, logHow, tip1-0.
The timer starts when Go begins; the log card waits for Time. A second real try and save earned the ready suggestion.
Chart side path heard wLog, chart1, chart2, chart3, result, dip and recovery; final two-second recheck confirms all
three chart how-to prompts start. Step side path heard r4 and all three cues once; repeated cue taps then stayed silent.
Read priority was checked separately: the queued cue waited behind Read. Hints always update immediately.
Fixed-line manifest: 75 lines, easy-coach / Umbriel. Audio recording was prohibited, so browser speech is used.
Prompts originally lost chart2 behind chart1; the next step now starts its prompt immediately, with a matching validity check.
Welcome wording was generalized to remain accurate on a resumed rung and in a stacked layout.

## Feel check

Played through demonstration, a real-time minute with scripted partner counts, logging, ready suggestion and all
four sample chart steps. No child's motor performance was observed or certified.
Best moment: selecting S3's dip rings S4's recovery, making the student's practice story visible.
Flattest 1: the first compact layout buried Set up and squeezed the figure. Reworked the control grid, folded More,
and stacked portrait layouts; Show me, Start a try, Partner counts and Set up are now visible.
Flattest 2: chart narration lagged quick taps and made the next step feel stalled. The current step now changes
its hint and starts its prompt immediately; the two-second held-click recheck hears each prompt.
The gym, layered character and patterned cloth hold their own beside Snowy Mail Route. Beat Lab was also opened
as a finish reference. `feel-comparison.png` places this tool beside Snowy Mail Route.
This is physical practice with a screen coach. Multi-session chart progress supplies the reason to return.

## Done when

1. PASS: default hint names Show me; full rung-1 two-cycle play; all six timeline assertions and cue coverage passed.
   Rung 5 event times 1, 3, 4, 5, 6, 8 encode toss, toss, claw, toss, claw, claw.
2. PASS: full figure/toss space and main controls at 1366x768; largest My log chart; compact and portrait controls inspected.
3. PASS: held cue, Show me, Step and rung input changes state immediately; count/drop/undo changes synchronously.
4. PASS: actual go/half/ten/time/logHow order; short tries rejected; Time completes before entry.
5. PASS: exhaustive counter sequences, cap, and real-pointer two-run history.
6. PASS: Not yet tip speaks once per cue; two qualifying saves earn a ready suggestion; no rung is locked.
7. PASS under detailed Interactions: correct sample dots and dip accepted; incorrect dots explained and marked false;
   sentence permits one attempt. The contradictory strict wording is documented in handoff.md.
8. PASS: sample met S4, own unmet best 7, edited S5 label, and empty goal-session flag checked.
9. PASS: both cue picks required; 13/6/10 tallies; reset helped 5/2; none and A little handled separately.
10. PASS: privacy visible in both modes; blocked-on-load and blocked-write tests passed without runtime exceptions.
11. PASS: hand mirror changes figure, paths and Step words; calm keyframes retain the actual peak beat and timer pacing.

## Wave lessons

- Hint and voice: PASS, main path and final two-second chart/Step checks; no queued prerequisite blocks input.
- Focus and layout: PASS, native modal focus, preventScroll restoration, persistent controls, keyboard dot focus retained after redraw.
- Sizes: PASS, every STANDARDS size and 375 iframe inspected; compact clipping corrected; controls at least 44 pixels.
- No giveaways: PASS, equal dots, shuffled one-attempt sentences, hidden numbers/tallies, no performance score.
- Honest numbers: PASS, suggested goals and personal observations, fictional sample, computed met/changed labels.
- Standards: PASS, solo motor practice, goal setting, cue reflection and reset evaluation each have an action.
- Motion off: PASS, no looping CSS animation; actual clock minute and quantized key positions.
- Short choice sets: PASS, three chart answers and three cue choices fit together; optional cards disclose separately.
- Resize during animation: PASS, 760x900 and back while Show me ran, then Step; no exception or lost state.
- Late welcome: PASS, welcomeAfter false; a first action can cut the welcome; no late mode welcome is queued.
- Unknown stays unknown: PASS, first/latest fields and cue tallies remain hidden until their required actions.
- One look, one meaning: PASS, scarves use stripe/dot/border, cue highlight means current cue, ring means selected/explained chart dot.
- Truthful badge: PASS, ready means two self-reported qualifying tries and is explicitly a suggestion.
- Hint changes back: PASS, rung, mode, stopped try and dialog return refresh the hint immediately.
- No copied-word answer: PASS, chart sentences require comparing actual first/latest values; order varies.

## Audit leads

AUDIT NOT FINISHED. The one final mechanical audit exited at its first DevTools WebSocket connection:
ConnectionResetError, WinError 64. No audit.md, leads or frames were produced. Not rerun, per the single-audit rule.
Scratch `audit/audit-failure.md` preserves the command and traceback. This is not a clean mechanical audit.
Targeted release-pose, keyboard focus, resize, storage and calm-keyframe checks followed the startup failure.
Cold review must run the complete mechanical audit on the final bundle.

## Frames looked at

Inspected every shot in bar-frames (2), first-frames (1), test-frames (6), responsive-frames (12), final-frames (3),
play-frames (7), edge-frames (6), voice-frames (3), last-frames (4), final-art-frames (2), resize-frames (2),
and calm-final-frames (1), plus art-contact.png and feel-comparison.png. Early failed layouts are retained as evidence.
The full size sweep ran once successfully after a startup failure was retried in smaller batches; later shots targeted fixes.

## Art made

Nine self-generated OpenAI gpt-image paintings: gym, setup scarves, body and six arms. Seven people assets marked true.
All raw PNGs retained, keyed/resized by the authorized art.py --rekey form, then inspected on magenta and in scene.
No paintings redrawn; pose placement was aligned in code. Final art 296.89 KB; audio 0 KB;
final self-contained bundle 517,009 bytes / 504.89 KB, comfortably below the 2 MB goal.
Prompt set and body reference links are in art/prompts.json. Credit is in tool.draft.json and notes.md.

## Art still to paint

None. Cory contact-sheet and fresh representation review remain in the cold review/shipping workflow.

## Engine changes wanted

None. Shared kit left untouched.

## Left open

- Mechanical audit startup failure; no exhaustive audit size/state/walk result is claimed.
- Independent people-art review and Cory's contact-sheet review have not occurred in this unattended Build.
- Browser speech is functional; the requested easy-coach recordings are not recorded, as instructed.
- Initial short guide/spec reads completed before the explicit timeout helper existed. Subsequent build/check commands
  used deadlines: bundle 120 s, drive batches 300 s, audit 2,400 s, smaller checks 20-30 s.
- First supplied neighbor entries lacked handoff/refine files; Target Toss's source, handoff and refine were read instead.
- Spec conflicts and choices are itemized in handoff.md. No spec file was edited.
- Every owned Chrome and host process is closed. Three lingering host workers were identified by exact command line
  and stopped. Host HTML removed; no commits, external messages, uploads or deployment.
