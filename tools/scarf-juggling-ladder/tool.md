# Scarf Juggling Ladder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: scarf-juggling-ladder

#### Built

Six distinct scarf demonstrations, Slow/Real speed, Step and cue holds, mirrored hands, practice countdown,
60-second timer with one extension, partner count/drop/undo, local tries, goals, cue checks, reset reflection,
and guided chart reading with Ren's separate fictional log. All six rungs stay open.
Kit starter and Curio.voice used. No shared code changes, commits, uploads or polish round.
All build artifacts are under the named tool; helpers, evidence and reference bundles are in its Scratch folder.

#### Numbers check

`numbers.py` independently confirms sample session bests 2, 3, 2, 5, 7; dip S3; goal first met S4;
cue Got it counts 13/15, 6/15, 10/15; reset helped counts 5 and 2. Axis floor 10, values 0-99.
All 10,000 possible integer first/latest pairs were checked against the two-unit up/down rule.
Contrast recomputation: ink/paper 15.07, muted/paper 6.29, brand/paper 7.33, white/brand 7.90,
focus/paper 4.80, muted/white 6.78; scarf contrasts 3.30, 4.80, 4.26. These match the spec's rounding.
Seeded 10,000-learner recomputation: growing up 85.15%, same 14.59%, down 0.26%; flat up 17.57%,
same 64.89%, down 17.54%. The spec gives no seed; these support its approximate rates, not exact tenths.
The suggested rung goals and 60/10/30-second rules are design choices, not performance norms.

#### Facts checked

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

#### Break it

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

#### Voice walk

Muted Chrome, 120 ms held presses and a two-second action pace. Full real-time practice minute completed.
Main heard order: cue1-0, cue1-1, cue1-2, afterShow, breathe, go, dropPartner, half, ten, time, logHow, tip1-0.
The timer starts when Go begins; the log card waits for Time. A second real try and save earned the ready suggestion.
Chart side path heard wLog, chart1, chart2, chart3, result, dip and recovery; final two-second recheck confirms all
three chart how-to prompts start. Step side path heard r4 and all three cues once; repeated cue taps then stayed silent.
Read priority was checked separately: the queued cue waited behind Read. Hints always update immediately.
Fixed-line manifest: 75 lines, easy-coach / Umbriel. Audio recording was prohibited, so browser speech is used.
Prompts originally lost chart2 behind chart1; the next step now starts its prompt immediately, with a matching validity check.
Welcome wording was generalized to remain accurate on a resumed rung and in a stacked layout.

#### Feel check

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

#### Done when

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

#### Wave lessons

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

#### Audit leads

AUDIT NOT FINISHED. The one final mechanical audit exited at its first DevTools WebSocket connection:
ConnectionResetError, WinError 64. No audit.md, leads or frames were produced. Not rerun, per the single-audit rule.
Scratch `audit/audit-failure.md` preserves the command and traceback. This is not a clean mechanical audit.
Targeted release-pose, keyboard focus, resize, storage and calm-keyframe checks followed the startup failure.
Cold review must run the complete mechanical audit on the final bundle.

#### Frames looked at

Inspected every shot in bar-frames (2), first-frames (1), test-frames (6), responsive-frames (12), final-frames (3),
play-frames (7), edge-frames (6), voice-frames (3), last-frames (4), final-art-frames (2), resize-frames (2),
and calm-final-frames (1), plus art-contact.png and feel-comparison.png. Early failed layouts are retained as evidence.
The full size sweep ran once successfully after a startup failure was retried in smaller batches; later shots targeted fixes.

#### Art made

Nine self-generated OpenAI gpt-image paintings: gym, setup scarves, body and six arms. Seven people assets marked true.
All raw PNGs retained, keyed/resized by the authorized art.py --rekey form, then inspected on magenta and in scene.
No paintings redrawn; pose placement was aligned in code. Final art 296.89 KB; audio 0 KB;
final self-contained bundle 517,009 bytes / 504.89 KB, comfortably below the 2 MB goal.
Prompt set and body reference links are in art/prompts.json. Credit is in tool.draft.json and notes.md.

#### Art still to paint

None. Cory contact-sheet and fresh representation review remain in the cold review/shipping workflow.

#### Engine changes wanted

None. Shared kit left untouched.

#### Left open

- Mechanical audit startup failure; no exhaustive audit size/state/walk result is claimed.
- Independent people-art review and Cory's contact-sheet review have not occurred in this unattended Build.
- Browser speech is functional; the requested easy-coach recordings are not recorded, as instructed.
- Initial short guide/spec reads completed before the explicit timeout helper existed. Subsequent build/check commands
  used deadlines: bundle 120 s, drive batches 300 s, audit 2,400 s, smaller checks 20-30 s.
- First supplied neighbor entries lacked handoff/refine files; Target Toss's source, handoff and refine were read instead.
- Spec conflicts and choices are itemized in handoff.md. No spec file was edited.
- Every owned Chrome and host process is closed. Three lingering host workers were identified by exact command line
  and stopped. Host HTML removed; no commits, external messages, uploads or deployment.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: scarf-juggling-ladder
#### Played
Cold as a grade 4 learner, then with a teacher projecting in mind: all six demonstrations, a full real minute,
save, both modes and Ren's four chart steps before opening builder report, handoff, notes or source.
Warm gym, patterned scarves and the real-practice purpose are strong. No child's motor performance was observed.
#### Findings fixed
- Blocker, general, chart reading: two wrong dots and a wrong sentence led to the same apparent success.
  Preserved the spec's explained progression, but final feedback now identifies help and correction explicitly.
- Blocker, general, entry: keyboard navigation could reach an underlying rung and change the saved skill.
  Rung, demo and mode controls now stay locked through entry, including number-key mode shortcuts.
- Blocker, general, reset reflection: asked about restarting after a drop without a no-drop response.
  Conditional question and Not needed response now cover an unused reset without adding to helped counts.
- Should fix, general, demonstration: an unrelated beat lowered the other arm while its caught scarf floated.
  Each arm now retains its own latest pose until that hand acts again.
- Should fix, general, timer: countdown +30 allowed a 90-second try introduced as one minute.
  Extension starts only during practice, once; extended tries use Thirty seconds left instead of Halfway at 30 left.
- Should fix, general, chart: Ren's preset prediction and recovery were attributed to the student. Named Ren.
- Should fix, general, voice/hint: Goal prompt named a hidden control; terminal chart feedback named no action.
  Goal now says Open Goal; final chart names Ladder. Old chart feedback has a generation validity guard.
- Should fix, general, Save voice: logHow continued over the saved card and delayed the cue tip. Save now hushes
  the stale entry line. The real-clock two-second recheck hears the tip before My log.
- Should fix, general, science: universal spacing claim exceeded the studies. Changed to can help.
- Polish, general: moved scene heading clear of flying scarves; rekeyed seven people cutouts with despill.
  Rejected the generated body cleanup because its colored edges were worse. Kept the painted identity and style.
- Polish, general: a solid curved recovery link makes the dip-to-next-session payoff visible; calm mode holds it still.
- Should fix, general, compact entry: reset replies pushed Save partly out of view. Compact replies retain 44px
  targets; phone entry uses the full space below the header. Duplicate saved instructions and singular units corrected.
- Should fix, general, narrow payoff: the next session could be off screen. The two ringed sessions now center
  together. Phone entry repeats the privacy line inside its full-height card.
- Should fix, craft, audit: closed disclosure geometry, timer/underlay text, zero-dot label clearance and phone
  hint coverage corrected. SVG dimensions now preserve 44px chart targets despite the horizontal scrollbar.
- Should fix, play, audit: saved card blocked next-rung clicks and Show ran behind it. Rungs stay accessible;
  Show, Step, cue and rung dismiss the card. See my log exits sample data. Shortened rung 4's wrapping goal.
- Should fix, teaching/voice, audit: no tries no longer reports a best of zero; edited goals say Change goal.
#### Findings left
- Spec-limited blocker under the cheap-pass rubric: invented personal counts can set best/ready. The prescribed
  self-report log cannot verify motor skill. No sensor, teacher gate or new scoring feature was added; see Left open.
- Nit, art: modular arm joins still look slightly assembled. Correct held-scarf poses and the painted style retained.
#### Break it
- Best run/ready: 0 and 99 accepted, two invented 99s make the explicit self-report suggestion; no rung unlocks,
  mastery score or certification. All six rungs remain open. This is the prescribed personal record, with the limit above.
- Timer: sub-ten-second finish/Save rejects; Stop saves nothing; repeated extension stops at 90. Countdown
  extension does nothing. In calm mode the clock still advances and extended thirty-seconds narration is accurate.
- Partner: 4, Drop, 7, Drop, Undo restores run 7, previous best 4 and one drop; run caps at 99.
- Best dots: wrong first/last dots are recorded false and explained, with no independent-success claim.
- Sentences: wrong down then up cannot change the first answer. All 10,000 integer trend pairs passed.
- Dip: lowest first-session dot rejected; displayed help is recorded. Assisted finish says so, even after correction.
- Goal: already-met goal is computed from matching rung; edit is marked; 100 rejected; zero-best chart valid.
- Strength/reset: random same-cue picks reveal only personal tallies after both choices; sample counts 13/6/10 and
  resets 5/2 match. Not needed stores without adding helped. Sample data never enters the personal log.
- Persistence/clear: storage-blocked load still logs in memory with visible warning; Escape keeps two tries,
  explicit Clear removes them. 36 zero/99 tries in 12 sessions scroll with the latest in view.
- Keyboard: original entry changed saved rung 1 to 6 behind its card; fixed path stays on 1 and unlocks after Save.
  Keyboard-only chart navigation selected both correct best dots and an answer; focus remains visible.
#### Voice walk
Final real-clock, 120ms held presses, two-second pace: cue1-0, cue1-1, go, half, ten, time, logHow, tip1-0, wLog, goal.
First Show me appropriately skips the welcome; a later tap cuts speech at its state change. No late welcome.
Side chart at two seconds: wLog, chart1, chart2, chart3, result, dip. The full correct chart also speaks recovery
and chartDone. Five cue taps speak the how line once, then four silent entries; all 78 fixed lines match manifest.
Read works with Sound off, mode changes release Read promptly, and a queued demo cue drops on leaving Ladder.
Editing an empty goal speaks editGoal, then Read repeats Change goal; all 78 runtime lines equal the manifest.
Extended calm try speaks thirty, not half, at thirty seconds left; Motion off preserves time.
Harness failures and retries are retained in Scratch; the final sequential real-clock walk completed.
#### Facts checked
- Grip in middle, palms down, high release, claw from above, crossing and three-scarf grip/start:
  Alberta Education A(K-3)13 and Dynamic PE ASAP Juggling Lesson Plan 1.
- Two-scarf X and first-up/first-caught sequence: Maine State Library Scarf Kit sheet, p2.
- One/two/three progression and slow float: Chris Nichols, Gopher Sport, Tips for Teaching Juggling in PE.
- Next toss near the previous peak: Dynamic PE ASAP Juggling Lesson Plan 1.
- Throw quality before catch, staged cascade and arm-space caution: Circomedia, Juggling 3 Scarves.
- Adult three-month study, visual-motion regions, reduced changes after stopping: Draganski et al.,
  Nature 427:311-312 (2004), doi:10.1038/427311a; Eric Chudler, University of Washington, Juggling Juggles the Brain.
- Days-spaced motor practice can help: Shea, Lai, Black and Park (2000), Human Movement Science 19:737-760,
  doi:10.1016/S0167-9457(00)00021-X. Notes distinguish an adult study from this child's scarf activity.
- Throw/catch, goal, strength and reset standards: SHAPE America 2024 official PE standards,
  1.5.10, 1.5.12, 4.5.6, 4.5.7 and 4.5.9. Each has a student action.
- Sample recomputation: bests 2/3/2/5/7; dip S3; goal first met S4; cue counts 13/6/10; helped resets 5/2.
- Six rungs, 60/10/30 seconds, goals 10/10/5/5/3/10, two qualifying entries, 0-99 cap and +/-2 trend
  are labeled design rules or personal observations, not population norms. Privacy checked against guarded local storage.
Sources with URLs and retrieval limits: `_scratch/scarf-juggling-ladder/review-sources.md`.
#### Sensitivity
Child's body and movement: seven people assets marked true. Friendly, fully clothed, ordinary PE clothing,
no appearance scoring or comparison. Further reviewer should inspect the modular shoulders/fingers, comfortable
reach and the standing figure's ability representation. Notes support seated practice and adapting reach.
No cultural or historical representation. Brain example is adult research, with no promise about a child's brain.
#### Flattest moment left
Repeated practice is intentionally off-screen; the screen cannot observe or certify juggling skill.
The weakest screen moment was the terminal chart result, lifted with the recovery link, honest help recap and next action.
#### Graphics
All nine paintings opened, including the seven people cutouts on a current contact sheet, and in assembled scene.
Original style, lighting, gym depth, figure and patterned cloth retained. Both modes checked at every required size,
including 375 iframe; grayscale and calm checked. Pose corrections re-shot at all eight sizes; three-catch pose
also at 680, 1366 and 375. Art 297.29 KB; final bundle 511.23 KB. No image placeholders.
Viewed the supplied Snowy Mail Route comparison and Beat Lab reference frame; this scene keeps the same care.
#### Audit
Completed once in about 31 minutes under the 40-minute cap, Chrome 9951, host 8755: 424 raw leads.
All eight default sizes, calm animation, resize stress and held-repeat checks were clean.
Confirmed fixes and scoped re-shoots: entry/try/saved overlays, clock, chart targets/labels, closed disclosure
children, goal status/edit voice, personal-log return and rung 4 wrap. Details: Scratch review-audit-disposition.md.
Native Setup covers its background intentionally. Optional cards scroll; chart sessions scroll sideways with a visible
instruction and automatic best/dip centering. Closed native content was a phantom geometry lead, now explicitly hidden.
First-tap own narration may skip welcome per BASELINE 16. Rapid Show/Step deliberately cuts old cue speech; Read
and the visible cue remain. No late welcome or stale chart feedback. Audit was not rerun after fixes.
#### Left open
Spec Done when 7 conflicts with its detailed explain-and-advance instructions; followed detailed guidance,
with visible assisted-reading status instead of adding a new score or gate. Verifying self-reports needs a spec decision.
No spec or shared kit changes. No commits. Temporary host file removed; Chrome ports 9950-9957 are closed.
Host 8755 still serves the tool directory. Process lookup was denied, so its unidentified owner was left running.
No authored recordings exist. Browser narration used; no audio recorded, no external contact or deployment.
Initial root/doc commands preceded the explicit timeout wrapper; all subsequent shell work used bounded processes.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Scarf Juggling Ladder handoff

Build only, 2026-11-07. Run every command from `S:\CurioClass-codex`.
Only this tool and `_scratch/scarf-juggling-ladder/` were written. No commits or polish round.

#### Layout and logic

`src.html` starts from the kit starter. It keeps the kit header, Motion, Sound, Read and Curio.voice.
Tool-local CSS lays out the painted gym, six-rung navigation, SVG performer, HTML timer and log cards,
and a real-size SVG chart. Compact landscape stays side by side. Portrait screens stack.
The controls precede scene items in DOM tab order. Modal setup and clear dialogs use native focus trapping.

The `R` table contains exact rung content and tips. `pattern(n)` supplies beat and flight timelines:
rung 4 has three falling flights and no catches; rung 5 is toss, toss, claw, toss, claw, claw;
rung 6 continues alternating throws. Painted body and six arms are keyed assets.
SVG scarves carry stripes, dots or a border plus an ink outline. Hand mirroring affects the complete group and beat words.
Motion off quantizes flight positions without changing any timer or demonstration pacing.

`demoToken` cancels a demonstration immediately on a rung change, cue tap, restart, Step or try.
`timerToken` prevents a stopped countdown or ending narration from opening an old log card.
Practice elapsed time is measured from performance.now after Go begins. Entry and Save both enforce ten seconds.
The partner history stores run, previous best and drops before each action, so Undo also undoes a Drop.

The localStorage schema is versioned and validated on reading. Storage errors leave the same in-memory log
and show the session-only warning. Sessions are global to the log, not separate per rung.
The fictional sample is a separate array and immutable goal; it never writes to the personal log.
Every chart dot has equal visible size and a 44-pixel input region. Narrow charts scroll rather than overlap input regions.
Screen-reader names include dot coordinates as the nonvisual equivalent of the graph.

Chart reading records whether the first/latest selection was correct, but has no score.
The explicit Interactions rule explains wrong taps and advances; a wrong dot is never recorded as correct.
The sentence has one attempt, shuffled placement, then an explained result. Dip checks compare session bests.
Cue tallies remain hidden until both reflection choices. Yes and A little reset answers are counted separately.

#### Checks and evidence

Scratch contains the number recomputation, generated-image paths, art contact sheet, two reference-tool bundles,
frames, functional assertions, 2,187 counter sequences, timed held-click play walk and voice logs.
The full report is `codex-report.md`. It records the final audit leads and any unfinished verification.
The single mechanical audit failed during its first DevTools connection with WinError 64 and produced no leads or frames.
The audit was not rerun. Targeted release-pose, keyboard-focus, resize and blocked-on-load checks followed;
the final bundle has no completed mechanical audit. See Scratch `audit/audit-failure.md`.
Build and test helpers in Scratch are evidence, not runtime dependencies.
The distributed HTML bundles the kit and nine WebP images and makes no network requests.
Build-stage narration had 75 fixed lines, easy-coach / Umbriel. No audio was recorded, per the build brief.
Variable chart results use browser speech. Recordings can be added in a later authorized stage.

#### Decisions and open questions

- People art: took the spec's clear leaning and painted the child and all six arm poses. All seven assets carry
  `people: true`. OpenAI gpt-image replaces the older Gemini wording, as explicitly authorized by CODEX-BUILD.
- Independent people/representation review and Cory's contact-sheet review remain for the cold review and shipping
  workflow. No approval was requested in this unattended Build. Contact sheet: `_scratch/scarf-juggling-ladder/art-contact.png`.
- The spec requests welcomeAfter true, while BUILD and KIT restrict it to one-mode tools. Used false for these two modes
  to prevent a late welcome, following the standing voice rules and BASELINE rule 16.
- Welcome wording uses "the pattern" and "Read my chart" so it remains true on a resumed rung and in stacked layouts.
- CODEX-BUILD asks for an early report scaffold; the direct prompt says to stop when the report is written.
  Kept intermediate evidence in Scratch and wrote the final report only at completion.
- Done when 7 says the dot steps accept only correct dots; Interactions explicitly advances after an explained wrong dot.
  Followed the detailed interaction, with a separate correctness record and no success score.
- Session numbers belong to the whole log. For a rung first practiced after session 1, its first visible session is used,
  with that actual number in the prompt, rather than asking for a nonexistent session 1.
- At narrow widths the chart can scroll before ten sessions to keep 44-pixel hit regions from overlapping.
- The no-motion-on-load requirement takes precedence over the general request for quiet idle movement.
- The ten-session maximum is only for choosing the goal deadline. Actual logs can extend past ten sessions.
- Rung 6's ready line invites continued cascade practice, rather than naming a nonexistent rung 7.
- A goal larger than the largest logged result expands the y axis so its dashed line stays visible. This resolves
  the conflict between the prescribed data-only axis maximum and the requirement to display every chosen goal.

#### Sensitivity

The tool depicts a child's body in ordinary PE clothing and teaches a movement skill. Review the assembled arms,
finger shapes, range of reach and representation without treating one body type as a performance ideal.
The child is friendly and fully clothed; the tool does not judge appearance or compare students.
The reset question includes I'd rather not say. Teacher notes identify the SHAPE body/movement standards,
the adult-only scope of the brain study, comfortable reach, and the disagreement about catch height.

#### Engine changes wanted

None. No shared file was changed.

#### Cold review changes, 2026-11-07

The review preserved the painted gym, child and patterned scarves. A hand holding a caught scarf retains its
claw while an empty throwing hand lowers. Two scarves held together remain separately visible. Cutouts were rekeyed with despill
enabled after a generated cleanup introduced worse edge artifacts and was rejected.
Entry locks the underlying rung/demo/mode controls and keyboard mode shortcuts until Save, preventing a saved
try from changing rungs behind its card. The reset reflection has a Not needed choice, stored without adding
to helped counts. Countdown extension is disabled; the running timer accepts +30 once and uses an accurate
thirty-seconds-left line on an extended try.

Phone entry fills the area below the header, keeps Save and all five reset responses in view, and repeats the
device-only privacy line inside the card. Compact landscape keeps the same controls at 44 pixels.
Chart progression still follows the spec's detailed explain-and-advance rule. Its final card now distinguishes
an independent response from an answer shown or corrected after help, with no mastery score. Ren's chart and
prediction name Ren. A curved recovery link lifts the dip moment and is still in Motion off. Completed chart
reading names Ladder as the next action. Small charts center the dip and next session together. A reading-generation
token prevents old feedback from advancing a newly selected chart. Answering hushes the prior prompt, and Save hushes
entry narration before its cue tip. Goal narration now names the disclosure students must open first.
The practice-spacing sentence now says can help, matching the limits of the cited motor-learning research.
See codex-review.md for independent evidence and the final audit disposition.

The review audit completed once within its 40-minute limit. Its raw leads include closed native disclosure
geometry, intentional modal/background coverage and deliberate fast-tap speech cuts. Confirmed layout leads
were corrected with explicit closed-content hiding, overlay label cleanup, clock line height, chart label
clearance and a visible phone-entry hint. Saved cards now leave rung navigation accessible and dismiss on
Show, Step, cue or rung actions. See my log explicitly returns to personal data after sample viewing.
Goal feedback distinguishes no tries from a real zero, and edit narration names Change goal. Current fixed
narration count: 78. The final contact sheet is `_scratch/scarf-juggling-ladder/review-final-art-contact.png`.

Final scoped chart rechecks preserve 44px dot targets at all eight required sizes, including the horizontal
scrollbar case. The chart uses explicit SVG pixel dimensions rather than shrinking its hit regions to fit.
All six post-audit partner frames and the phone-entry, saved-to-Show and saved-to-next-rung paths were re-shot.
The bundle is 511.23 KB. Source syntax and the nine-asset manifest pass the final static check.
The review leaves the prescribed self-report limitation explicit: invented counts can produce best/ready
marks, and the tool cannot certify physical skill. Changing that requires a product/spec decision.
The final real-clock main-path voice recheck and edited-goal Read check passed; all 78 runtime lines match
the voice manifest. Temporary host.html is removed and Chrome ports 9950-9957 are closed. Port 8755 still
serves this tool directory; Windows denied process lookup, so its unidentified owner was not terminated.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
