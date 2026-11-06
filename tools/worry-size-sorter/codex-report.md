# Codex report: worry-size-sorter

## Built
Built in `S:\CurioClass-codex`, with writes confined to this tool and its Scratch folder. No commits or polish round.
Four modes, thirteen illustrated cards, five body clues, four complete coping activities and a saved seven-day goal.
The downloadable HTML is self-contained. No typing, accounts, score, analytics or runtime network requests.
The build uses the kit starter, kit CSS, Curio.voice, kit sound and Motion. No shared file was changed.
All 27 named illustrations are embedded. The spec heading says 26 but lists 27; every named image was made.

## Numbers check
`_scratch/worry-size-sorter/calculations.json` independently recomputes the spec numbers. All agree.
Brand contrast: 6.23 on white, 5.85 on paper; ink/paper 14.81; muted/paper 6.11.
Small/Medium/Big white-text ratios: 6.09, 5.93, 8.01. Their paper ratios: 5.71, 5.56, 7.52.
Breathing: 32 seconds for two four-count rounds, 64 for four, 24 for two three-count rounds.
Squeeze: 15 seconds per part, 45 for all three. Full real-time runs completed, including count changes and the four-round cap.
All 25 meter pairs: 10 down, 10 up, 4 same, 1 calm start. Four extreme pairs also tested through the real UI.
Calendar checks cover DST start/end, month end, leap day, year end, day eight and a clock set back.
1,000 generated decks preserved thirteen unique cards, Small then Medium first, and no consecutive Big cards.

## Facts checked
Current source checks and unavailable routes are detailed in Scratch `source-verification.md`.
- Body readiness, fast heartbeat/breathing, butterflies and sweaty/shaky hands: [Nemours KidsHealth](https://kidshealth.org/en/teens/anxiety.html).
- Sleep trouble, stomachaches and interference with school/home/play: [CDC](https://www.cdc.gov/children-mental-health/about/about-anxiety-and-depression-in-children.html).
- Help for concerns lasting weeks or impairing daily life: [NIMH](https://www.nimh.nih.gov/health/publications/children-and-mental-health).
- Fast/shallow breathing, four equal phases, gentle comfortable practice: [Cleveland Clinic](https://health.clevelandclinic.org/box-breathing-benefits).
- Muscle tension cycle, hands/shoulders/toes, tense 4-10 seconds and relax 10-20: [HealthLink BC](https://www.healthlinkbc.ca/healthwise/progressive-muscle-relaxation).
- Helpful realistic self-talk: [Anxiety Canada material via HereToHelp](https://www.heretohelp.bc.ca/sites/default/files/healthy-thinking-for-younger-children.pdf).
- Worry box and avoiding use just before bedtime: [YoungMinds](https://www.youngminds.org.uk/parent/blog/how-to-make-a-worry-box-a-guide-for-parents/).
- Paper, box and grown-up conversation: [Just One Norfolk NHS](https://www.justonenorfolk.nhs.uk/media/us1bjpvw/worry-box.pdf).
- Ten minutes is a practical example, not an optimal dose; [NHS Every Mind Matters](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/tackling-your-worries/) gives 10-15 minutes.
- Unsafe secrets, inappropriate photo/secrecy requests, adult roles and continued telling: [Childhelp](https://childhelp.org/safe-vs-unsafe-secrets-how-to-talk-to-kids-about-the-difference/).
- US immediate-danger instruction: [911.gov](https://www.911.gov/calling-911/). Notes identify its US scope.
- NHES identifiers: local `data/standards/nhes-2024.txt`; their student-action map is in the spec and implemented in each mode.
The thirteen situations and eight reply sets are fictional curricular examples, not universal claims about families or swimming lessons.
Small/Medium/Big are the spec's help categories, not a diagnosis or a survey of children's preferences.
The meter is explicitly a personal rating. A lower rating is not clinical validation or proof of physical practice.
The DOJ PDF could not be fetched; the Childhelp photo/secrecy guidance supports the same action. Old YoungMinds URL was corrected.

## Break it
- No drop: tapping every empty basket does not advance progress. Each shows its meaning, without narration.
- Mash all Small or all Medium: all thirteen finish; all five Big cards still route to Big. Zero escaped Big cards.
- Put all thirteen in Big: accepted. End says Big: 13 and correctly counts the eight that a tool could also help.
- Repeated basket taps after a drop cannot count the same card twice. New worry is required.
- Repeat the same talk-back: only one distinct reply is counted. A second different reply changes to the small cloud.
- All three talk-back replies are helpful by design. This is practice, not a hidden-answer quiz or an assessment.
- Sweep the meter: it updates only the student's stated rating, with correct down/up/same/calm wording and no score.
- Stop early: goes immediately to After, as required. Helpers and check marks remain personal reports, not verified performance.
- Incomplete goal: cannot set without Tool, When, Who and a reason from a result or chosen clue.
- Select Bedtime then Worry box: Bedtime clears and cannot be selected. The readiness guard also rejects this pair.
- Future days: mouse and keyboard taps refuse them; today checks/unchecks. Early Finish honestly reports N of 7, including zero.
- Device clock can change the calendar; this is a local practice diary, not tamper-proof attendance.

## Voice walk
`voice-walk/log.json`: held clicks, roughly two seconds apart, through Sort, Talk back, Body clues, breathing, squeeze, box and My week.
Main first tap picked up the card with no speech, as specified. Tools welcome, startTalk, replies, howAfter and meter result followed.
All five Big-help events started five times. Body welcome/clue, startBreath, phase cue, startSqueeze, squeeze/let-go,
startBox, boxed, meterOther, week welcome, goalSet, checked and weekEnd were observed in order on the side path.
Repeated check/uncheck/check spoke Checked only once that day. Mode switching stopped the squeeze and emptied stale work.
Read during breathing was protected across automatic phase changes. Stop and mode changes intentionally hush it.
The initial Big Next implementation cut the line at its four-second wait cap. Fixed Sort advances to leave that event finishing.
`big-next-audio.json` confirms the targeted Next retest has a spoken Big entry without a cut marker.
`sort-welcome.json`: five same-mode taps at two-second gaps produced one wSort, without cutting it.
The week welcome was shortened to name an enabled first choice; each later builder step now has a once-only, state-checked how line.
96 authored strings are in the friendly-dad manifest. Build instructions prohibit recording, so actual playback uses browser fallback.
Headless muted logs verify queue behavior, not the audible quality of the requested friendly-dad recording.

## Feel check
Walked the full thirteen-card path and all four activities with student inputs, including real-time breathing and all three squeeze parts.
Best moment: choose two different realistic replies and watch the dark cloud change face, lighten and shrink above the card painting.
Flattest moment 1: an initially static swap. Added an actual shrinking transition and visible response bubble; repeated replies cannot shrink it twice.
Flattest moment 2: paper folding was initially rebuilt in its final state. It now visibly folds, then travels into the painted box.
The session earns a personal basket recap, helper collection and a specific goal, without rewarding lower feelings or unsafe secrecy.
`bar-comparison.png` puts Sort beside Snowy Mail Route. Both bar tools were bundled in Scratch, opened and inspected.
The tool has richer painted material and place detail than the reference frame; its quieter pace suits this topic.

## Done when
1. PASS: 1366x768 focus and controls checked in every mode; whole child, tool and meter, full builder/chart and privacy line.
2. PASS: 680x425 keeps the side panel, compact card, tool tiles/meter, stepped builder and chart. Targeted phone repairs are recorded below.
3. PASS: all Small/Medium mash strategies keep five Big cards in Big; all-Big strategy accepts thirteen with correct explanation.
4. PASS: all five rings opened their fact and Try tool; help card remains available, folded at compact sizes.
5. PASS: all four before/tool/after paths completed. All 25 meter pairs agree; UI extremes and helper-first goal choice were exercised.
6. PASS: Stop changed step in about 36 ms after release; mode change stopped squeeze. Next finishes the Big slide and respects the line wait cap.
7. PASS: complete goal gate, own-result reason, checks, future refusal, date arithmetic and day-eight reflection; UI zero/seven reflection fixtures.
8. PASS: no typing. Only wss-week and kit curio-motion keys observed. Privacy line changes when storage writes fail.
9. PASS for queue behavior: five Big starts; one Sort welcome in five repeated taps; phase/mode invalidation and Read checked. Recordings remain open.
10. PASS: keyboard sort, Talk back and Worry box completion, breathing/squeeze Stop and after rating, plus chart check/future refusal.
One keyboard test initially selected the neighboring tile because its Tab count was wrong; the corrected sequence passed for Squeeze and let go.

## Wave lessons
- Hint and voice: immediate manual hint updates; Curio.voice heard tracking and valid/needs guards; current Read context.
- Focus and layout: no focus on load; preserved choice focus and explicit next-step focus after disappearing controls.
- Sizes and targets: eight required sizes, phone iframe, no horizontal overflow. Compact meters retain 44-pixel targets.
- No giveaways: no hidden-answer score. The rating, diary and helper list are labeled personal reports; Big routing is an explicit lesson.
- Honest numbers: meter assumes a self-rating, calendar assumes the device date, diary assumes reported practice.
- Standards: body/help choices teach S1, the goal/chart/reflection teach S6, and actual tool practice/rating teaches S7.
- Motion off: idle light/cloud loops stop; breathing and squeeze durations remain unchanged.
- Short choices: compact builder uses one complete row at a time. Phone reflection was enlarged and condensed to expose all nine chips.
- Resize mid-animation: CSS relayout preserves live nodes and run state; the audit checked flips after inputs.
- Welcome timing: first card/basket taps intentionally skip speech; no delayed welcomeAfter is used.
- Unknown as unknown: personal Before/After values stay unset until chosen; there is no inferred diagnosis or measured calm score.
- One look/one meaning: named green/amber/blue baskets, numbered body rings, explicit locks and check marks; grayscale frame inspected.
- Badge truth: counts use actual placements/checks; helpers require a result path, with no claim of mastery.
- Hints change back: mode, tool step and builder step each set their own current hint immediately.
- No answer by copying: realistic self-talk offers three helpful approaches; safety routing is taught openly, not presented as a quiz.

## Audit leads
Ran the full audit once, to completion, on Chrome 9981 with host 8785. It produced 78 inspected frames and 10 leads.
The saved audit is deliberately the pre-repair evidence; there was no second full audit.
1. Body-mode Lungs/Tummy overlap: fixed by separating the rings vertically. Targeted wide geometry is clean.
2. Week welcome named disabled Set my goal: replaced with an enabled first action; later steps have valid/needs-checked how lines.
3. Same overlap in the open-clue state: the same ring repair resolves it, with focus retained.
4. Phone help-card summary below the fold: shortened the phone body scene, kept the full child, and added leaders to body locations.
5. Try a tool lost focus: mode entry from the card now focuses the Before meter. Targeted focus is meter3.
6. Finish my week lost focus: reflection now focuses its first response chip. Targeted focus is help0.
7-10. First tap on card, Small, Medium or Big skipped the welcome: intentional, exactly as the spec and BASELINE 16 require.
The premise remains in the scene, hint and Read. A first mode-button tap queues its welcome normally.
Additional repair: the initial Sound label now reserves its icon, preventing the header shift the walk observed.
Additional visual repair: compact reflection exposes all nine chips, privacy and the three next-week choices without a choice scroll panel.
Eight targeted layout/focus queries are clean: no small targets, overlaps, below-fold controls, clipped choices, failed keep regions or disabled names.
The builder capture's query was initially malformed; its first retry then lost Chrome. A smaller final retry passed with all step lines in order.
That retry spoke weekNext once and silently reused it later; the manifest matches all 96 runtime strings.
The outside-drop return was also exercised with a real drag: 300 ms, no leftover ghost and zero progress.
One early phone-host favicon request returned 404. An inline favicon fixed the host and tool; later phone captures had no console errors.
All final successful drive batches reported zero console errors, warnings or exceptions.

## Frames looked at
Two reference frames; five early frames; seventeen exercise frames; thirty-two full-size mode frames;
seven extra drag/keyboard/calm/grayscale/safety frames; eleven post-fix frames; nine final checks; three corrected-key frames;
voice-finish, two final retry frames, all art/contact sheets, the bar comparison, 78 audit frames and nine targeted lead frames.
Full size sweep ran once. Later shots were limited to changed states. All claimed frames were visually inspected, directly or in contact sheets.

## Art made
27 original illustrations, five people assets, all marked people true. Toes redrawn once, then keyed with enclosed-gap handling.
Art: 860.1 KB; recorded voice: 0 KB; final bundle: 1245.1 KB. The original budgets were 1,250 KB art and 450 KB voice against the 2 MB goal; the bundle is below that goal.
Cutouts, scenes and people sheets were inspected at UI scale. Raw PNGs and prompts remain with the tool; evidence sheets are in Scratch.

## Art still to paint
None. The owner's people contact-sheet desk check is a later shipping step, not completed by this Build run.

## Engine changes wanted
None. All fixes are tool-local; kit, scripts, docs and other tools were left untouched.

## Left open
Friendly-dad recordings were not made, following Build-only instructions. Browser speech quality needs listening in a later media pass.
The supportive no-trouble assurance is prescribed copy, not a guarantee of how every adult will respond; continued telling stays prominent.
Clinical effectiveness and student usability were not measured. This build teaches and supports practice; it does not assess mental health.
Temporary tool host.html removed. All Chrome and server ports started for this build were closed and checked. No commits or polish round.
