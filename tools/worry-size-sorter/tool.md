# Worry Size Sorter: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: worry-size-sorter

#### Built
Built in `S:\CurioClass-codex`, with writes confined to this tool and its Scratch folder. No commits or polish round.
Four modes, thirteen illustrated cards, five body clues, four complete coping activities and a saved seven-day goal.
The downloadable HTML is self-contained. No typing, accounts, score, analytics or runtime network requests.
The build uses the kit starter, kit CSS, Curio.voice, kit sound and Motion. No shared file was changed.
All 27 named illustrations are embedded. The spec heading says 26 but lists 27; every named image was made.

#### Numbers check
`_scratch/worry-size-sorter/calculations.json` independently recomputes the spec numbers. All agree.
Brand contrast: 6.23 on white, 5.85 on paper; ink/paper 14.81; muted/paper 6.11.
Small/Medium/Big white-text ratios: 6.09, 5.93, 8.01. Their paper ratios: 5.71, 5.56, 7.52.
Breathing: 32 seconds for two four-count rounds, 64 for four, 24 for two three-count rounds.
Squeeze: 15 seconds per part, 45 for all three. Full real-time runs completed, including count changes and the four-round cap.
All 25 meter pairs: 10 down, 10 up, 4 same, 1 calm start. Four extreme pairs also tested through the real UI.
Calendar checks cover DST start/end, month end, leap day, year end, day eight and a clock set back.
1,000 generated decks preserved thirteen unique cards, Small then Medium first, and no consecutive Big cards.

#### Facts checked
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

#### Break it
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

#### Voice walk
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

#### Feel check
Walked the full thirteen-card path and all four activities with student inputs, including real-time breathing and all three squeeze parts.
Best moment: choose two different realistic replies and watch the dark cloud change face, lighten and shrink above the card painting.
Flattest moment 1: an initially static swap. Added an actual shrinking transition and visible response bubble; repeated replies cannot shrink it twice.
Flattest moment 2: paper folding was initially rebuilt in its final state. It now visibly folds, then travels into the painted box.
The session earns a personal basket recap, helper collection and a specific goal, without rewarding lower feelings or unsafe secrecy.
`bar-comparison.png` puts Sort beside Snowy Mail Route. Both bar tools were bundled in Scratch, opened and inspected.
The tool has richer painted material and place detail than the reference frame; its quieter pace suits this topic.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
Two reference frames; five early frames; seventeen exercise frames; thirty-two full-size mode frames;
seven extra drag/keyboard/calm/grayscale/safety frames; eleven post-fix frames; nine final checks; three corrected-key frames;
voice-finish, two final retry frames, all art/contact sheets, the bar comparison, 78 audit frames and nine targeted lead frames.
Full size sweep ran once. Later shots were limited to changed states. All claimed frames were visually inspected, directly or in contact sheets.

#### Art made
27 original illustrations, five people assets, all marked people true. Toes redrawn once, then keyed with enclosed-gap handling.
Art: 860.1 KB; recorded voice: 0 KB; final bundle: 1245.1 KB. The original budgets were 1,250 KB art and 450 KB voice against the 2 MB goal; the bundle is below that goal.
Cutouts, scenes and people sheets were inspected at UI scale. Raw PNGs and prompts remain with the tool; evidence sheets are in Scratch.

#### Art still to paint
None. The owner's people contact-sheet desk check is a later shipping step, not completed by this Build run.

#### Engine changes wanted
None. All fixes are tool-local; kit, scripts, docs and other tools were left untouched.

#### Left open
Friendly-dad recordings were not made, following Build-only instructions. Browser speech quality needs listening in a later media pass.
The supportive no-trouble assurance is prescribed copy, not a guarantee of how every adult will respond; continued telling stays prominent.
Clinical effectiveness and student usability were not measured. This build teaches and supports practice; it does not assess mental health.
Temporary tool host.html removed. All Chrome and server ports started for this build were closed and checked. No commits or polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: worry-size-sorter

#### Played
Cold grade 3-5 solo play preceded the builder report, handoff, notes and source: all 13 cards, five clues, all four tool sequences (including both full timed runs) and a week reflection. Also considered classroom projection. Warm, specific and reassuring; the shrinking cloud is the best moment.
Root: `S:\CurioClass-codex`. One review pass, no commits. Evidence stays in this tool's Scratch folder.

#### Findings fixed
- **Blocker, general, Tools:** immediate Start/Stop plus 5-to-1 claimed the tool caused calm. Results now report the child's rating; early Stop is explicitly unfinished, with its own spoken response. No score or mastery reward was added.
- **Blocker, general, My week:** Finish on day one said the week got away and spoke that it was done. Early reflection now says "so far", uses an appropriate event line and makes all chips explicitly optional.
- **Blocker, general, Talk back:** swimming reassurance guaranteed shallow water and an instructor's position. Replaced it with asking the swim teacher for help learning safely.
- **Should fix, general, Sort/Talk back:** "Many kids say" and a claim about classmates' thoughts lacked evidence. Removed the implied survey and mind-reading claim; kept flexible worry sizing and realistic self-talk.
- **Should fix, general, Tools:** selecting a different worry left the old heading above the new bubble. Re-render the current tool with focus retained; heading and reply now agree.
- **Should fix, general, voice:** breathing completion still named Start; squeeze transitions gave no specific next-part instruction. Added state-matched Done/round-cap lines, next-part how lines and short fists/shoulders/toes event cues. The premise also remains in compact Read after a skipped welcome.
- **Should fix, general, focus/Read:** timed completion lost keyboard focus; automatic squeeze completion could hush Read. Focus follows Done/Next part; automatic transitions preserve Read.
- **Should fix, general, My week:** old reflection chips carried into a new goal. Reset both chip groups when a goal is set.
- **Should fix, general, notes:** a blanket US school-staff reporting statement could hide role/state differences and direct-report duties. Notes now distinguish applicable law from school procedure.
- **Should fix, general, art:** toe pose had exposed toes despite the specified socks and did not clearly teach curling. Redrew the same child with closed socks and curled fabric; kept rich painted style and people metadata.
- **Should fix, general, compact result:** extra early-stop explanation pushed the result low. Two result buttons now share a row; 680, phone and 1280x720 results remain visible. Phone square/check-in typography now stays inside its painting.
- **Polish, general, flat result:** the breathing scene reset to the same generic square after rating. It now shows this student's before-to-after check-in, with neutral wording and no success color.
- **Polish, general:** fixed the live countdown's "1 seconds" wording and added a comfortable, pain-free squeeze instruction.

#### Findings left
- **Polish, general:** the week builder is the quietest interaction. Its complete choices, painted time tiles and personal goal are retained; no extra topic or game was added.
- Recorded friendly-dad clips remain a later media step under the build brief's no-recording rule. Browser fallback and queue behavior were tested; a specific recorded performance was not heard.

#### Break it
- Empty-basket tapping: no progress. Five duplicate placements: still one card. Real jittered outside drag: returns after 300 ms, no ghost, zero progress. Real basket drag: one placement.
- All Small, all Medium and all Big were actually driven. The first two retain five Big cards; all Big accepts 13 and explains the eight optional adult-help choices. No scored "pass" can be farmed.
- Five identical talk-back taps: one distinct reply and only the middle cloud. A second distinct reply gives the small cloud. All three replies are intentionally helpful practice, not a hidden-answer quiz.
- Meter sweep and immediate Stop: only the chosen self-rating changes. Early Stop no longer claims successful practice or causation. Helpers remain the child's own preferences, not certified skill.
- Independently checked all 25 pairs: 10 lower, 10 higher, four unchanged, one calm start. The four extremes and actual rating paths agree.
- Incomplete goal: refused. Bedtime selected before/after Worry box: cleared or blocked. Today checks/unchecks; future mouse and keyboard attempts refuse. Zero/seven and day-eight reflection fixtures are correct.
- New-goal reflection chips reset. Blocked saving updates the privacy line. The goal and checked day survive reload. A local diary can trust a child's check mark; it is not tamper-proof attendance.
- 500 generated decks: 13 unique cards, Small then Medium first, no consecutive Big cards. Calendar arithmetic independently covers both DST changes, leap day and year end.
- Four three-count rounds stop at the cap; focus is on Done. Motion off keeps the 24-second initial run. Four-count initial run is 32 seconds; squeeze remains three 15-second parts.

#### Voice walk
Held clicks at about two-second spacing, default tool settings, Sound on and Motion on. Initial card pickup correctly skips the welcome without consuming it; the premise stays in the hint and Read.
Final main path: Sort pickup, Small, Try a tool, before 4, full breathing, Done, after 3; Body clues; Talk back with two replies; all three squeeze parts; fold/post the worry; My week goal, today check and early reflection. See `final-voice-retry/results.json`.
Final timed cues: fists/shoulders/toes once each, let-go three times, inhale twice, hold four times and exhale twice; no timed cue was cut.
Side paths checked Read during breathing and the automatic squeeze transition, Sound-off Read, fast mode changes and day-eight entry. No automatic squeeze transition cut the Read log.

| Line/kind | Expected | Observed |
|---|---:|---:|
| Big safety event across five cards | 5 | 5 |
| Same reply event at two-second pace | 5 | 5 |
| howAfter across four tools, per page | 1 | 1, then silent |
| goalSet / early reflection, two new goals | 2 each | 2 each |
106 runtime strings exactly match `voice/lines.json`; no stale mode speech or console exception in successful interaction batches.

#### Facts checked
Checked live on 2026-11-06; named guidance below supports the teaching, not a diagnosis or promised treatment outcome.
- Readiness/fight-or-flight, fast shallow breathing and gentle equal breath phases: [Cleveland Clinic](https://health.clevelandclinic.org/box-breathing-benefits).
- Fast heartbeat, sweating/shaking, stomachaches and sleep trouble: [CDC, Anxiety and Depression in Children](https://www.cdc.gov/children-mental-health/about/about-anxiety-and-depression-in-children.html).
- Worry lasting weeks or disrupting school/home/friends, and seeking help: [NIMH, Children and Mental Health](https://www.nimh.nih.gov/health/publications/children-and-mental-health).
- Stress/muscle-tension cycle, clench hands/shrug shoulders/curl toes, 4-10 seconds tense and 10-20 relaxed: [HealthLink BC](https://www.healthlinkbc.ca/healthwise/progressive-muscle-relaxation). Tool uses 5/10, never into pain.
- Four equal four-count phases and comfort: Cleveland Clinic above. It suggests three to four rounds; the brief starts with two and offers a third/fourth. Three-count timing is a shorter implementation option, not a claimed clinical dose.
- Helpful, realistic self-talk and thoughts not being facts: [Anxiety Canada via HereToHelp](https://www.heretohelp.bc.ca/sites/default/files/healthy-thinking-for-younger-children.pdf). The eight situations/reply sets are fictional examples; removed unsupported guarantees and population claims.
- Asking a qualified swim instructor for help at a comfortable learning pace: [American Red Cross](https://www.redcross.org/take-a-class/swimming/swim-lessons/kids-swim-lessons).
- Paper worries, a box and adult conversation: [Just One Norfolk NHS](https://www.justonenorfolk.nhs.uk/media/us1bjpvw/worry-box.pdf). Avoid use just before bedtime: [YoungMinds](https://www.youngminds.org.uk/parent/blog/how-to-make-a-worry-box-a-guide-for-parents/).
- About ten minutes is an example within the 10-15-minute worry-time suggestion: [NHS Every Mind Matters](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/tackling-your-worries/), not a prescribed pediatric dose.
- Unsafe secrets, photo secrecy, trusted adults and continued telling: [Childhelp](https://childhelp.org/safe-vs-unsafe-secrets-how-to-talk-to-kids-about-the-difference/); online photo requests: [NCMEC NetSmartz](https://www.missingkids.org/content/dam/netsmartz/itc/downloadable/ITC%20Poster%20Kit.pdf). Doctors/help with persistent worries: NIMH above.
- Immediate US danger: [National 911 Program](https://www.911.gov/calling-911/). Teacher reporting cautions: [Michigan Department of Education](https://www.michigan.gov/mde/services/ed-serv/educator-conduct/abuse-neglect); state law and role govern the particular duty.
- S1 help/body information, S6 goal/track/reflect and S7 practice: [SHAPE America NHES 2024](https://shapeamerica.org/standards/health/new-he-standards/), checked against the spec's student-action map.
- Source-independent arithmetic: `review-numbers.json` and browser checks reproduce 32/24-second breathing, 45-second squeeze, all meter branches and date differences. Recomputed contrasts agree: brand/white 6.23, brand/paper 5.85, ink/paper 14.81; basket white-text 6.09/5.93/8.01.

#### Sensitivity
Abuse, being hurt, online exploitation, family illness and bodies warrant the next sensitivity lens. Check all five Big cards, m3/m4 replies, and the no-trouble reassurance as supportive wording rather than a guarantee about every adult's response.
The class is never asked for disclosures; one trusted adult and continued telling remain prominent. Parent/caregiver is one option among six; an unsafe family adult is not made mandatory. Notes name reporting duties. US 911 scope is explicit in notes.
All five people assets show the same specified child, naturally and fully clothed; all are marked people true. Check identity continuity and avoid reading one child's appearance as representative of who experiences worry. This review does not claim a separate cultural-review sign-off.

#### Flattest moment left
Picking the week plan is slower than changing the cloud or folding the slip. The earned personal goal and seven-day chart give it purpose. Kept the strong art, motion and calm tone.

#### Graphics
All 27 named assets checked in the contact sheet and scenes, including all five body poses, 13 vignettes, baskets/clouds/box and time tiles. One style; no missing art token. The spec's "26" heading actually lists 27.
Toe redraw uses the built-in OpenAI image tool; prompt is in `art/prompts.json`, raw PNG in `art/raw/ws-kid-toes.png`, accepted 600-pixel WebP keyed through `art.py --rekey`. No new scene or feature.
All four modes inspected at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe. Changed compact states re-shot at 680 and phone; grayscale, Motion off and keyboard frames inspected.
Bundle: 1249.4 KB. Art: about 861 KB; no recorded audio. Evidence folders include `cold-frames`, `layout`, `targeted`, `compact-recheck`, `phone-square`, cheat/input traces and `sheets`.

#### Audit
Completed once, within the 40-minute limit, on Chrome 9961 and host 8765. Inspected all 87 audit PNGs in contact sheets and confirmed the affected 1280 frame at full size. Four mechanical leads concern the card/empty-basket first-tap welcome skips. These are specified behavior under the on-load rules and BASELINE 16; compact Read now retains the premise. The audit frame also exposed slight 1280x720 button clipping that its geometry did not flag. A scoped result-row repair and two targeted 1280 captures confirm it is fixed. No second audit.
Wave checks: hints/Read, focus, required sizes/targets, honest meters, no giveaways, actual standards actions, Motion off, complete choice sets, resize during activity, timely welcomes, unknown ratings, single-meaning labels, true badges, restored hints and no answer-copy shortcut.

#### Left open
The specified browser fallback remains until the later recording pass. No clinical effectiveness, real-world practice verification or student usability study is claimed.
Two initial read commands and a few short inspections lacked explicit outer timeouts; subsequent long commands used the required bounds. A background read job initially used its default folder and was corrected before any write. Existing shared Python bytecode was unchanged; later Python runs disabled bytecode writes.
A host favicon 404 and harness startup/key/reload mistakes were isolated and corrected; successful replacement checks are named in the evidence. No unanswered questions were sent. Source guidance and the brief settled the narrow choices. All owned Chrome and host ports are closed; no temporary tool host remains. No known blocker or should-fix remains from this pass.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 1 (general 1, family 0), should fix 12 (general 12, family 0), polish accepted 18
Traced to spec: blockers 1, should fix 8

### Refine: worry-size-sorter

Lenses: refine/teaching.md, refine/play.md, refine/craft.md, refine/sensitivity.md (fresh agent; grades 3 to 5).
Shared audit: S:/CurioClass-codex-scratch/worry-size-sorter/audit-r1/. Integrator spot-checks: viewed
art/ws-card-door.webp at full size (bedroom at night, bed, lamp, stuffed bunny, light under the door: confirmed);
read src.html:574-583 (Big slide animation has no fill, card returns), 1027-1031 (because() uses any meter result),
1228-1250 (digits 1 to 4 switch mode from anywhere except SELECT and a held Sort card: confirmed).
"(spec)" = the cause is in spec.md; "(build)" = the spec was right and the build missed it.

#### Blocker
1. **Card b1 picture shows a child's bedroom at night.** art/ws-card-door.webp, Sort card b1 "A grown-up asked me to
   keep a secret, and it feels wrong." The picture is a child's bedroom (bed, quilt, stuffed bunny, lamp on) with the
   bedroom door closed and hallway light under it. Paired with a grown-up's secret that feels wrong, it is the classic
   scene of night-time abuse in the child's own room: a trigger for a child living it, met alone at home, and a
   frightening specific scene for every other child; it also narrows the secret to home. Seen: sensitivity full-size
   view and its big-b1 frame; integrator viewed the webp. Fixed: redraw with no bedroom, no bed, no night, no people,
   for example a small wrapped box or a closed notebook with a blank "shh" sticker on a school cubby or hallway bench in
   daylight. Update the ws-card-door entry in spec art list and art/prompts.json to match (keep the token name or
   rename it consistently). No person, so no contact sheet entry. (general) (spec: the spec prompt asked for "a closed
   wooden bedroom door with a soft hallway light underneath")

#### Should fix
1. **The goal's "Because" can argue against the goal.** src.html:1027-1031 because(), My week builder (1096-1102).
   Any meter result is used, so a rising meter gives "I will do Squeeze ... Because my meter went from 2 to 4 when I
   tried it", and the clue choices are hidden so the student cannot pick a better reason; "from 3 to 3" too. NHES 6.5.1
   asks how the goal supports well-being. Seen: teaching t2-week-because-up.png, t2b-week-goal-up.png; play
   because-up.png. Fixed: use the meter line only when after < before; calm 1 to 1 reads "Because I practiced it when
   I was calm."; otherwise show the clue choices (Should fix 2). (general) (spec: spec.md My week says "if the chosen
   tool has a meter result this load, the line is built from it" with no direction rule)
2. **"Pick the body clue this tool helps" accepts wrong pairings and leaves out tummy.** src.html:325, 1096-1102.
   Every clue is offered for every tool, so "Box breathing ... Because it can help with busy thoughts" is accepted while
   Body clues teaches busy thoughts go with Worry box and Talk back; the label reads as a fact question. Four clues
   here, five in Body clues (no tummy). Seen: teaching t3-week-because-mismatch.png; play cites
   audit-r1/state-week-chart-1366x768.png. Fixed: offer only the clues whose Body clues "Try" line names the chosen
   tool (from the clue data), label "Pick the body clue it helps (from Body clues)", and add tummy / butterflies with
   the tools Body clues names for it. If a tool has one clue only, preselect it. (general) (spec: the spec's four-clue
   list and "the body clue it helps" with no tie to the Body clues data)
3. **Box breathing teaches two rounds; the sources say three to four.** src.html:769 ("Two rounds, then check your
   meter."), 898. Cleveland Clinic and WebMD, and the spec's own Sources row, give 3 to 4 rounds. Seen: teaching read
   code and fetched page; audit-r1/state-breathing-stopped-1366x768.png. Fixed: default 3 rounds ("Three rounds, then
   check your meter."; 48 s at count 4, 36 s at count 3), One more round still up to 4; update voice line and Read text
   that says two. (general) (spec: spec Box breathing says "Two rounds play" against its own Sources row)
4. **Number keys pull a keyboard student out of a running tool.** src.html:1247-1250. Digits 1 to 4 switch mode
   from anywhere; the meter is drawn 1 to 5, so pressing 4 for "A lot" opens My week, 1 jumps to Sort and stops a
   breathing run. Seen: play meter-key4.png (focus on meter2, mode became week); craft digit-in-meter (mode sort,
   running false). Fixed: while focus is inside the stage or panel, digits do not switch mode; on the meter (Tools
   step 1 and step 3) 1 to 5 rate the step. Header buttons keep keys 1 to 4. (general) (spec: spec gives "keys 1 to
   4" globally and a 1 to 5 meter with no rule for focus inside a tool)
5. **A Big card dropped in Small or Medium snaps back to the stack.** src.html:576-583. The 0.6 s slide has no fill,
   so the card returns to the top at full size with "Sorted. Look at the help beside it."; only a 23 px thumbnail lands
   in Big. The one moment the tool exists to show is undone on screen. Seen: play big-drop-after.png (1.2 s after),
   big-drop-mid.png; integrator read the code. Fixed: the card ends in Big (shrinks into the Big basket and stays
   hidden from the stack), and the stack shows an empty slot or the next card back until Next worry; Motion off jumps
   there. Same settle for Small and Medium drops (Polish 6). (general) (build: spec says it "slides into Big")
6. **Saving My helpers gives no privacy line where it saves.** src.html:848-852, 1006-1008. "This one helps me"
   writes wss-week to localStorage, but the line about storage only shows in My week. BASELINE rule 7 (privacy stated
   where anything is stored). Seen: craft helps-privacy.png and its storage dump. Fixed: one small line under the step
   3 result buttons, "Saved on this device only." (plus "This browser won't save it." when storage is blocked).
   (general) (spec: spec puts the privacy line only in My week though Tools saves helpers)
7. **Read speaks hint strings that are not in the voice lines.** src.html:389-401. About 16 hints ("Tap a numbered
   ring to open a body clue.", "Tap Try a tool on it, or tap Next worry.", the My week builder hints and others) are
   not in voice/lines.json, so with recorded clips Read switches to the browser voice partway. STANDARDS "Bands".
   Seen: craft read logs. Fixed: put every hint string in L (and lines.json) and have Read speak keyed lines; regenerate
   lines.json so allLines() and the file match. (general) (build)
8. **Body clue rings sit on the face and off the body parts.** src.html:94-95, 232-233. Ring 1 (Head) covers the kid's
   nose and mouth at every size; ring 4 (Tummy) sits at the hem and waistband; at 680x425 ring 5 floats off the body
   with its leader at the thigh; ring 2 (Chest, fast heart) is on the viewer's left, the heart is on the viewer's right.
   Seen: audit-r1/state-body-clue-1366x768.png, state-body-clue-680x425.png (craft, play, sensitivity). Fixed: Head ring
   at the side of the hair or forehead edge, Tummy on the hoodie pocket, ring 5 led to the hand, and swap rings 2 and 3
   so the heart clue sits on the viewer's right; check 1366x768, 680x425 and 375 wide. (general) (build)
9. **Card b3 promises "You won't be in trouble for telling."** worry-data.json b3 reason and its voice line. The tool
   cannot keep that promise, and it misses the core message that it is not the child's fault. Seen: sensitivity
   big-b3-short frame. Fixed: "Tell a trusted adult right away, even if you already sent something. It's not your
   fault. The person who asked did something wrong." Update lines.json and the spec Content row. (general) (spec: the
   spec wrote this reason)
10. **Card b1's reason does not say the grown-up may be one you know or love.** worry-data.json b1. Fixed: keep the
    reason and add "That's true even if it's a grown-up you know, or one in your family." Update lines.json. Seen:
    sensitivity big-b1 frame. (general) (spec: the spec wrote this reason)
11. **Green chroma-key fringe in the kid's hair.** art/ws-kid-stand, ws-kid-fists, ws-kid-shoulders, ws-kid-loose
    (ws-kid-toes is clean). A green halo on the curls, visible on the Body clues stage at 560 px; on the only child in
    the tool, on textured hair, it reads as careless. Seen: sensitivity zoomed crop and five-pose contact sheet. Fixed:
    re-despill or hand-clean the hair edge on the four poses. If any pose is redrawn rather than edge-cleaned, it goes
    on Cory's contact sheet. (general) (build)
12. **Teacher notes have no route for online exploitation.** notes.md "Sensitive content and disclosures". Card b3 is
    an online photo request; notes give no US route beyond school procedure. Fixed: add one adult-facing line: "For an
    online photo request or a shared image of a child, report to NCMEC's CyberTipline (report.cybertip.org,
    1-800-843-5678) as well as through your school; Take It Down (takeitdown.ncmec.org) helps remove images." Not on
    screen (keeps the no-hotline-on-screen call). (general) (spec: the spec's Disclosure paragraph sets the notes
    content and leaves this out)

#### Polish accepted
1. **Tools step 1 note.** Replace "Picture it's really happening." with "Think about this worry for a moment." for
   every card (sensitivity 6: an imaginal-exposure prompt on m3, home arguing, alone). When Box breathing or Squeeze is
   opened from the header with no card, hide the bare worry line and the note; ask only "How worried does your body feel
   right now?" (teaching 4, t1b-tools-header.png). (general)
2. **Body clues "Try:" names become buttons** that open Tools on that tile (teaching 5). (general)
3. **Medium result names the "talk it over" half.** For a Medium-sized card add "Who could you talk this over with?"
   (one line, no new chips) (teaching 6, t4-sort-medium-into-small.png). (general)
4. **b5 reason says what help is.** "...is a sign to get help. Tell a grown-up you trust; a school counselor or doctor
   can help with worry." Update lines.json (teaching 7). (general)
5. **Reflection: "I forgot" leads somewhere.** Add **Change who helps me remember** to Next week I will; when "I
   forgot" is picked, mark it as suggested (teaching 8, audit-r1/state-reflection-1366x768.png). (general)
6. **Small and Medium drops settle into the basket** instead of the card staying on the stack (play 2,
   audit-r1/state-sorted-card-1366x768.png, play small-drag.png). Do it with Should fix 5. (general)
7. **Softer sizing line.** Small card in Medium: "Many kids put this in Small. Medium is fine too." (and the mirror
   for Medium in Small) in place of "One way to size it: Small." (play 5, small-in-medium.png). (general)
8. **Worry box fold reads as folding**: a two-step fold (halves, then quarters) lined up over the slot it drops into
   (play 8, box-folded.png). Motion off jumps to folded. (general)
9. **Tool tile icons in one style**: four small inline SVG icons in the brand color, not two text glyphs and two color
   emoji (craft 5; spec says tile icons are drawn in code). Make Box breathing and Worry box clearly different. (general)
10. **Read in the Big panel**: join the adult chips as one sentence ("A parent or caregiver, a grandparent, a teacher,
    a school counselor, a coach or a doctor.") and drop the second "Tell one grown-up you trust" (craft 6). (general)
11. **b4 and b2 reasons add "not your fault".** b4 add "It's not your fault." b2 add "It's not your fault, and it's not
    your job to fix it." Update lines.json (sensitivity 7). (general)
12. **Notes for home and the disclosure steps** (sensitivity 9): add the home line (listen calmly, thank your child,
    contact the school counselor or doctor; for abuse, Childhelp National Child Abuse Hotline 1-800-422-4453), and add to
    the teacher steps "listen, don't question for details or investigate, write down the child's own words, tell them
    who you will tell next." Adult-facing only. (general)
13. **meterOther and the a > b result say "talk to a grown-up you trust"** in place of "talk to someone" (sensitivity
    10). Update lines.json. (general)
14. (nit) **End panel count**: "In Big: N. The 5 Big worries always go to a trusted adult." (teaching 9,
    t5-sort-end-allbig.png). (general)
15. (nit) **notes.md sources**: list the same sources as spec and tool.draft.json (add WebMD, Michigan Medicine,
    eSafety, Advocates for Youth, US Attorney tip sheet; add NHS Every Mind Matters to tool.draft.json), one YoungMinds
    URL, cite YoungMinds for the no-bedtime timing, and drop "browser voice fallback in this Build-only version"
    (teaching 10). (general)
16. (nit) **Big panel wait**: while the button reads "Listening...", the hint does not name Next worry; switch the hint
    when the button enables (play 10). (general)
17. (nit) **Count toggle**: a fixed label "Shorter count (3)" with aria-pressed, not a flipping label (craft 7). (general)
18. (nit) **Sorted card label**: "Sorted" in its aria-label after a drop, not "Pick up worry card" (craft 8). (general)

#### Settled calls
- Should fix 2 (clue pairing): teaching said should fix, play said polish. Kept as should fix: the tool confirms a
  pairing its own Body clues mode contradicts, and the missing tummy clue is a gap in what S1 taught.
- Should fix 8 (rings): craft said should fix, play and sensitivity polish. Kept as should fix: a ring over the child's
  face and a heart clue on the wrong side are seen by every student in Body clues.
- Should fix 4 (digit keys): spec "keys 1 to 4" stays for the header; the fix only stops digits switching mode while
  focus is inside the stage or panel. Settled here, not routed.
- Welcome not heard after a first tap on the card or a basket: allowed (BASELINE 16, spec On load); all lenses agree.
  Do not change.
- "Danger right now? Call 911." stays (Cory, 2026-11-05: no hotline on screen); sensitivity 11 only noted. The NCMEC
  and Childhelp lines go in notes.md only, never on screen.
- No score, timer challenge or streak; all-Big is accepted with the "never wrong" note. Do not add a quiz or right
  answer to Sort.
- The door redraw has no people; do not add a person or an adult figure to any card vignette.

#### To the spec's open questions
- Spec authors: update spec.md text to match Blocker 1 and Should fix 1, 2, 3, 9, 10, 12 (art prompt, Because rule,
  clue list, rounds, b1 and b3 reasons, notes Disclosure paragraph). Codex fixes the tool; the spec text update is for
  the spec owner.

#### Not taken
- Play 7 second half (a pulse or shake on the kid when a ring is tapped): new animation beyond the spec, not needed.
- Play 9 (one-word tile labels at 680x425): spec hides names there; distinct icons (Polish 9) solve it.
- Sensitivity 11 (911 is US-only): Cory's 2026-11-05 call stands.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: worry-size-sorter (round 1)

Cold Craft lens, 2026-11-06. Bundle `tools/worry-size-sorter/worry-size-sorter.html` as built (not re-bundled).
Shared audit: `S:/CurioClass-codex-scratch/worry-size-sorter/audit-r1/audit.md`. My frames and logs:
`S:/CurioClass-codex-scratch/worry-size-sorter/craft/out/` (shots1.json, shots2.json beside it).

#### Contract
- One file, 1.28 MB (under the 2 MB goal). No `fetch`, XHR or dynamic import in the bundle; the resource list after
  visiting all four modes is empty (`net` shot). Kit used (`Curio.voice`, `Curio.tone`, motion, theme). No console
  errors in any of my 20 shots or the audit.
- Frame times at 1366x768: Box breathing running 16.7 ms median, 16.8 ms p95 and max over 5 s; Sort idle with the
  daylight and cloud loops 16.7/16.8 ms (`fps-breath`, `fps-sort-drag`). Headless Chrome, GPU off, so a floor, not a
  laptop figure.
- Words: no em or en dashes in src, notes, data or lines; "Curio Class" never "Curio" alone. Classroom-safe.

#### Lines
- `voice/lines.json` and `allLines()` match exactly: 106 and 106, none missing either way (`alllines.json`).
- Art: all 27 `art:` tokens have a prompts.json entry, none unused; the five kid poses carry `people: true`, and
  all art is gpt-image (no local model drew people).

#### Standard voice check (Sound on, Motion on, held clicks 0.12 s)

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| big (5 Big drops, into Small, Medium, Big, Small, Medium) | event | 5 | 5 |
| Head clue text (clue0 tapped 5 times) | how | 1 | 1, then 4 silent |
| bIn / bHold / bOut (two rounds at count 4) | event | every phase | 2 / 4 / 2 |
| breathDone | how | 1 | 1 |
| Talk-back replies (5 taps over three runs) | event | 5 | 5 |
| startTalk, howAfter (three runs) | how | 1 each | 1, then silent |
| meterDown (twice), meterOther (once) | event | 2, 1 | 2, 1 |
| goalSet | event | 1 | 1 |
| checked (day0 tapped 5 times) | event, once per day by spec | 1 | 1 |

- Stale: Tools, meter, Start, Stop, Sort at 0.2 s gaps: each line is cut by the next action, nothing plays after
  the switch to Sort except wSort (`stale`). Squeeze then My week mid-run: `sqz` stops, `letgo` never plays, the run
  stops (`squeezeSwitch`).
- Read: Read 0.4 s into the Tools welcome cuts it and reads; a mode switch right after lets wClues start at once
  (`readDuring`). First taps: the audit rows hold (I did not re-shoot them); the welcome skipped by a first tap on
  the card or a basket is fine under BASELINE 16, and the premise stays on screen and in Read.
- Order: in every log the spoken lines follow the actions.

#### Findings

1. **Number keys change mode while using a tool.** src.html:1247-1250. Keys 1 to 4 switch modes from anywhere
   except a SELECT. With focus on Stop during Box breathing, pressing "1" jumped to Sort and stopped the run
   (`digit-in-meter`: mode "sort", running false). The meter steps are labeled 1 to 5, so a keyboard user rating
   "2" or "4" leaves the tool and loses the rating. Better: ignore the mode digits when focus is inside the stage or
   panel (or on a meter), or let the meter take 1 to 5 itself. **should fix**, general.
2. **Saving "My helpers" has no privacy line where it happens.** src.html:848-852 and 1006-1008. "This one helps me"
   writes `wss-week` to localStorage (`helps-privacy`: `{"week":null,"helpers":[3]}`), but the Tools panel says
   nothing about storage; the privacy line only shows in My week (frame `helps-privacy.png`). BASELINE rule 7.
   Better: one small line under the result buttons: "Saved on this device only." **should fix**, general.
3. **Read uses lines that cannot be recorded.** src.html:389-401. Read speaks the hint plus the panel's
   `innerText`. About 16 hint strings ("Tap a numbered ring to open a body clue.", "Tap Try a tool on it, or tap Next
   worry.", the My week builder hints and others) are not in `voice/lines.json`, so once the friendly-dad clips
   exist, Read will switch to the browser voice partway through. STANDARDS "Bands" says the panel hints go in the
   lines so Read can use recordings. Better: put the hint strings in `L` and have Read speak keyed lines.
   **should fix**, general.
4. **Body clue rings sit over the face and in odd places.** Body clues, src.html:94-95 and 232-233. Ring 1 (Head)
   covers the kid's nose and mouth at every size; at 680x425 ring 4 (Tummy) sits on the belt and crotch, and ring 5
   floats off the body with its leader line pointing at the thigh, not the hands (audit frames
   `state-body-clue-1366x768.png`, `state-body-clue-680x425.png`). Better: Head ring on the forehead or temple
   edge, Tummy on the hoodie pocket, ring 5 led to the hand. **should fix**, general.
5. **Tool tile icons mix text glyphs and color emoji.** src.html:320. Box breathing "□" and Worry box "▣" render as
   thin black text glyphs; Talk back "☁" and Squeeze "✊" render as color emoji (frames
   `state-talk-result-1366x768.png`, `helps-privacy.png`). The spec asks for code icons; the row looks unfinished.
   Better: four small inline SVG icons in the brand color, or four emoji. **polish**, general.
6. **Read in the Big panel runs the adult chips together.** readPanel, src.html:395. The 721-character Read says
   "Parent or caregiver Grandparent Teacher School counselor Coach Doctor" with no breaks, and "Tell one grown-up you
   trust" comes twice (start and end) (`read-big`). Better: join the chips as one sentence ("A parent or caregiver,
   a grandparent, a teacher..."), and drop the repeat. **polish**, general.
7. **Count toggle states its value twice.** src.html:772 and 820-824. The button's label flips to "Count of 3"
   and it also sets `aria-pressed=true`, so a screen reader hears "Count of 3, pressed" (`count-toggle`). Better:
   a fixed label ("Shorter count (3)") with aria-pressed, or a two-button group. **nit**, general.
8. **A sorted card keeps saying "Pick up worry card".** src.html:484. After a drop the card is `aria-disabled` but
   its label still ends "Pick up worry card". Better: "Sorted" in its label. **nit**, general.

Checked and fine: keyboard sort (focus on the card, Enter, Arrow, Enter places it; 4 px blue focus ring on the
basket, `kbd-sort.png`); tab order header, card, baskets; jittered real-mouse drag lands in Medium with no ghost
left (`drag-jitter`); Motion off keeps breathing timing, the dot jumps per side and no animation runs
(`calm-breath`); storage wrapped in try/catch with the "This browser won't save it." line; week index by
calendar date.

Counts: blocker 0, should fix 4, polish 2, nit 2.

#### Audit pilot
- Leads confirmed: none to confirm; its only lead (welcome not heard after a first tap on the card or a basket) is
  allowed by BASELINE 16, and the premise stays on screen and in Read.
- Leads wrong: none.
- What it missed: the number keys pulling a keyboard user out of a running tool (finding 1), the missing privacy line
  where helpers save (2), hints outside lines.json for Read (3), and hotspot rings placed over the face and off the
  hand (4). Those are about meaning and placement, which it cannot judge.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: worry-size-sorter (round 1)

Played twice: as a grade 4 student alone at home (Sort through all 13 cards, each tool, a week goal, the
reflection) and as a teacher projecting Sort and Body clues. Not a Curiosity (lesson tool, grades 3-5 Health).
My frames: `S:/CurioClass-codex-scratch/worry-size-sorter/play/shots/` (shots s1.json, s2.json, drive.py, port 9853).
Shared audit frames cited from `S:/CurioClass-codex-scratch/worry-size-sorter/audit-r1/`.

The defaults work for a solo student: the first screen says what to do (hint plus the card caption "Tap or drag to
pick up"), every waiting moment I walked names the next action and the control in the hint, Calm keeps the
breathing and squeeze timing, and nothing overlaps or clips at any audited size. The findings below are about
feel and words matching the state.

#### Findings

1. **Sort, Big card dropped in Small or Medium (src.html:576-583)**: the card slides toward Big, then snaps back to
   the top of the stack at full size, captioned "Sorted. Look at the help beside it." The animation has no
   `fill`, so the one moment the tool exists to show (a Big worry always ends up in Big) is undone on screen; only a
   23 px thumbnail lands in the basket. A student who misses the 0.6 s slide sees the card still sitting on top.
   Better: the card stays in (or shrinks into) the Big basket and the stack shows the next card back or an empty
   slot. Seen: `play/shots/big-drop-after.png` (1.2 s after the drop, card back on top), and `big-drop-mid.png`.
   **should fix**, general.

2. **Sort, every drop (src.html:483-486, 572)**: for Small and Medium drops the card never moves either; it stays on
   the stack (scaled .94) while the basket bounces and a tiny thumbnail appears. With drag, the ghost vanishes on
   drop and the card reappears at the top. The core action of the tool lands flat. Better: the card visibly drops
   into the basket it was given (same fix as 1). Seen: `audit-r1/state-sorted-card-1366x768.png`,
   `play/shots/small-drag.png`. **polish**, general.

3. **My week, "Because" from a meter result (src.html:1027-1031, 1101)**: any result is used, whichever way it went.
   After Talk back rated 2 then 4, the goal reads "Because my meter went from 2 to 4 when I tried it," and the body
   clue choices are hidden, so the student cannot pick a better reason. Words do not match the intent of a reason.
   Better: use the meter line only when after < before; otherwise show the clue choices. Seen: drive shot
   `play/shots/because-up.png` (panel text "Because my meter went from 2 to 4 when I tried it."). **should fix**,
   general.

4. **Keyboard, number keys on the meter (src.html:1247-1250)**: the meter steps are drawn as big numbers 1 to 5,
   but the keys 1 to 4 switch modes everywhere. A keyboard student pressing 4 for "A lot" lands in My week and
   loses the tool run; 1 goes to Sort, 2 to Body clues. Better: while focus is in the meter (or in Tools step 1/3),
   1 to 5 rate; or move mode keys off bare digits there. Seen: `play/shots/meter-key4.png` (focus on meter2, key
   "4", mode became "week"). **should fix**, general.

5. **Sort result wording (src.html:529)**: a Small card put in Medium says "You put it in Medium." then "One way to
   size it: Small." To a grade 3 student alone that reads as "you were wrong," against the panel's own "Small and
   Medium can feel different to different people." The spec's "Many kids say Small" is softer. Better: "Many kids
   put this in Small. Medium is fine too." Seen: `play/shots/small-in-medium.png`. **polish**, general.

6. **My week, body clue reason for any tool (src.html:1096, 1102)**: all four clues are offered for every tool, so
   "I will do Worry box ... Because it can help with fast heart" is allowed, while Body clues ties fast heart to Box
   breathing only, and the label says "Pick the body clue this tool helps" as if one is right. Better: offer the
   clues Body clues names for that tool (or mark them "Body clues says"). Seen: code, and
   `audit-r1/state-week-chart-1366x768.png` (goal sentence built from a clue pick). **polish**, general.

7. **Body clues, Head ring on the face (src.html:94, 232)**: ring 1 sits over the kid's nose and mouth at every size;
   at 680x425 it covers the whole face. Better: put it on the forehead or hair, beside the head. Also tapping a ring
   changes nothing on the kid (no pulse at the chest, no shake at the hands), a flat moment a small code effect
   could lift. Seen: `audit-r1/state-body-clue-1366x768.png`, `state-body-clue-680x425.png`. **polish**, general.

8. **Worry box fold (src.html:131)**: "Fold it" just shrinks and tilts the slip into a thin strip with about 9 px text
   far above the box; it does not read as folding, and the slip is not lined up with the slot it then drops into.
   Better: a two-step fold (halves then quarters) over the slot. Seen: `play/shots/box-folded.png`. **polish**,
   general.

9. **Tools at 680x425 (src.html:205)**: tile names hide, leaving four glyphs where □ (Box breathing) and ▣ (Worry box)
   look nearly alike. Per spec, but a preview viewer cannot tell them apart. Better: keep a one-word label
   ("Breathe", "Talk", "Squeeze", "Box"). Seen: `audit-r1/state-mode-tools-680x425.png`. **nit**, general.

10. **Big panel button vs hint (src.html:518, 524)**: for up to 4 s the button reads "Listening..." while the hint
    says "Tap Next worry when you are ready." Small mismatch of words and state. Seen:
    `play/shots/big-drop-mid.png`. **nit**, general.

Checked and fine: Big panel fits at 1366x768 and 1280x720 with Next worry visible (`big-1280.png`); at 680x425 Next
worry is moved to the top and visible (`big-680.png`), the 911 line needs a panel scroll there (preview size only);
end of sort counts match the placements (`end-sort.png`); breathing count and phase (`breath-mid.png`), Calm
breathing keeps time (`breath-calm`: phase advanced on schedule, dot holds its corner); squeeze poses and timer
(`squeeze-mid.png`, `squeeze-let.png`); Talk back m3 shows its "gets bigger if" note (`talk-m3.png`); no console
errors in any of my shots. The cheap ways: putting all 13 in Big is accepted with the "never wrong" end note; Big
cards cannot be left outside Big; Facts, Plan and Brave all work. Nothing to give away (no quiz mode).

Content (abuse, online exploitation, family illness on the Big cards) is for the sensitivity review
(`refine/sensitivity.md`); I did not judge it.

Counts: blocker 0, should fix 3, polish 5, nit 2.

#### Audit pilot

- Leads confirmed: none to confirm as faults. The "welcome not heard" rows for #worryCard and the baskets are by
  design (spec: the first card tap makes only its own sound; BASELINE 16); the premise stays on screen
  ("Every worry is real...") and in Read.
- Leads wrong: none.
- Missed: no audit state reaches a Big card (sorted-card always uses the first card, which is Small), so the Big
  panel and the snap-back (finding 1) were never shot; the card not moving on any drop (2); the meter-result
  reason (3); the digit-key clash (4, a key path, not a click); wording and placement items 5 to 10.

<!-- end part -->

<!-- part: refine/sensitivity.md -->

NOT YET

### Sensitivity review: worry-size-sorter

Fresh agent, blind to codex-report.md and codex-review.md. Read as a child-safety and early-childhood counsellor would.
Read: spec.md, src.html (all), worry-data.json, voice/lines.json (every line), notes.md, tool.draft.json, art/prompts.json.
Looked at every .webp (13 card vignettes on a contact sheet, the five kid poses side by side, the door card and the kid's
hair at full size). Drove the bundle in headless Chrome (port 9841): b1 dropped in Small at 1366x768, b3 dropped in Medium
at 1280x600, Body clues with Tummy open, Tools with m3 at step 1, Talk back on m3.

Scope note: the brief called it K-2, but spec, tool.draft.json and the page all say Grades 3-5. I judged it for ages 8 to 11.

#### Findings

1. **where:** art/ws-card-door.webp, shown on card b1 "A grown-up asked me to keep a secret, and it feels wrong." (Sort,
   basket thumbnail).
   **what:** the picture is a child's bedroom at night (quilted bed, stuffed bunny, lamp on) with the closed bedroom door
   and hallway light coming in under it. Paired with an adult's secret that feels wrong, this is the classic picture of
   night-time abuse in the child's own room. For a child living that, met alone at home (rule 4), it is a trigger with no
   adult present; for every other child it plants a frightening, specific scene the text never says. It also narrows "a
   grown-up's secret" to home and bedroom, when grooming happens in many settings.
   **how seen:** full-size view of the webp, and the big-b1 frame (card on top of the stack beside the Big panel).
   **fix:** redraw with no bedroom and no night: for example a small wrapped box or a closed notebook with a "shh" sticker
   on a hallway bench or school cubby, daylight. Keep "No people."
   **level:** blocker. **tag:** general.

2. **where:** worry-data.json b3 reason (also voice/lines.json): "You won't be in trouble for telling."
   **what:** a promise the tool cannot keep. Some adults do react badly (take the device, scold); a child who sent a photo
   and then is punished learns not to tell next time. It also misses the core message for this card: it is not the child's
   fault. NetSmartz-style guidance leads with blame-free framing, not a guarantee about consequences.
   **how seen:** read the data; the big-b3-short frame shows it as the first line under "This one is Big."
   **fix:** "Tell a trusted adult right away, even if you already sent something. It's not your fault. The person who
   asked did something wrong." Re-record the voice line to match.
   **level:** should fix. **tag:** general.

3. **where:** worry-data.json b1 reason: "A secret that feels wrong, or that you're told to keep from your family, is always
   one to tell."
   **what:** good flag, but it reads as if the family is always the safe place to take it, and it does not say the grown-up
   may be someone the child knows and loves, which is the usual case. A child whose secret-keeper is a family adult needs
   to hear that it still counts. (The adult chips below do give non-family routes; the reason should match.)
   **how seen:** big-b1 frame, read alongside the chips.
   **fix:** add one sentence: "That's true even if it's a grown-up you know, or one in your family." Keep the rest.
   **level:** should fix. **tag:** general.

4. **where:** art/ws-kid-stand, ws-kid-fists, ws-kid-shoulders, ws-kid-loose (the hair top).
   **what:** green chroma-key fringe left in the curls (12+ clearly green pixels on stand; visible as a green halo at full
   size and on the Body clues stage at 560 px). It is the only child in the tool, and a green rim on textured hair reads
   as careless handling of a Black or brown child's hair.
   **how seen:** zoomed crop of ws-kid-stand head; five-pose contact sheet shows it on four poses (ws-kid-toes is clean).
   **fix:** re-despill or hand-clean the hair edge on the four poses.
   **level:** should fix. **tag:** general.

5. **where:** notes.md, "Sensitive content and disclosures".
   **what:** online exploitation is one of the five Big cards, but notes give the teacher no US route for it. School
   reporting procedure covers abuse; an online photo request from a stranger also belongs with NCMEC.
   **how seen:** read notes.md against the b3 card.
   **fix:** add one line: "For an online photo request or a shared image of a child, report to NCMEC's CyberTipline
   (report.cybertip.org, 1-800-843-5678) as well as through your school; Take It Down (takeitdown.ncmec.org) helps remove
   images." Adult-facing only, so it does not conflict with the no-hotline-on-screen call.
   **level:** should fix. **tag:** general.

6. **where:** Tools step 1, src.html renderToolPanel: "Picture it's really happening. This is your own rating, not a test."
   **what:** asks a child working alone to imagine the worry vividly. Fine for a spelling test; for m3 ("My grown-ups were
   arguing") it is an imaginal-exposure prompt about home conflict with no adult present.
   **how seen:** tools-m3 frame (the m3 "gets bigger if" note shows under it, which helps but comes after).
   **fix:** "Think about this worry for a moment. How worried does your body feel right now?" for every card.
   **level:** polish. **tag:** general.

7. **where:** worry-data.json b4 and b2 reasons.
   **what:** b4 ("Being hurt is never okay...") and b2 ("too heavy to carry alone") are accurate and kind but miss the line
   children most need with each: being hurt is not your fault; a family member's illness is not your fault and not your
   job to fix.
   **how seen:** read data.
   **fix:** b4 add "It's not your fault." b2 add "It's not your fault, and it's not your job to fix it."
   **level:** polish. **tag:** general.

8. **where:** Body clues hotspots (src.html #clue0, #clue1, #clue3).
   **what:** ring 1 (Head) sits on the child's face, covering eyes and nose; ring 4 (Tummy) sits at the hoodie hem and
   waistband rather than the belly; ring 2 (Chest, the heartbeat clue) is on the child's right side, the heart is on the
   left (viewer's right).
   **how seen:** clues frame at 1366x768.
   **fix:** Head ring at the side of the hair or forehead, Tummy ring up on the hoodie pocket, swap rings 2 and 3 so the
   heart clue is on the viewer's right.
   **level:** polish. **tag:** general.

9. **where:** notes.md, "Support at home" and disclosure paragraph.
   **what:** the tool stands alone and many will meet it at home, but notes tell a parent nothing about what to do if a
   Big card turns into a real worry. The teacher disclosure steps also leave out "listen, don't question for details or
   investigate, write down the child's own words, tell them who you will tell next."
   **how seen:** read notes.md.
   **fix:** one line each: home ("If a Big card brings up something real, listen calmly, thank your child, and contact your
   child's school counselor or doctor; if it involves abuse, the Childhelp National Child Abuse Hotline is 1-800-422-4453"),
   and the teacher steps above.
   **level:** polish. **tag:** general.

10. **where:** Tools step 3, meterOther / meterResult when the after rating is 4 or 5.
    **what:** "Try a different tool, or talk to someone." is gentle but vague when a child rates the worry high after
    practising.
    **how seen:** read meterResult and L.meterOther.
    **fix:** "talk to a grown-up you trust" in place of "talk to someone".
    **level:** polish. **tag:** general.

11. **where:** Big panel, "Danger right now? Call 911."
    **what:** correct scope (only immediate danger, never for worry itself) and US-only, as notes say. On a public site a
    non-US child sees 911 with no country cue. Accepted under Cory's 2026-11-05 call; noted only.
    **level:** nit. **tag:** general.

#### Checked and sound
- Class is never asked to disclose: "You never have to tell the class. Tell one grown-up you trust." on the Big panel and in
  Read; notes say keep talk on the written cards; no typing anywhere.
- A parent is one route of six (Parent or caregiver, Grandparent, Teacher, School counselor, Coach, Doctor); "If that
  grown-up doesn't help, keep telling until someone does" covers an adult who fails; week helper offers teacher, friend
  or self, not only home.
- m3 and m4 escalate correctly ("anyone gets hurt, or you feel unsafe at home"; "afraid someone will hurt you. Then it's
  Big.") and that note follows them into Tools. m3 talk-back "It isn't my job or my fault" is right.
- b5 and the "too big to carry" card match CDC/NIMH warning signs; nothing frames worry as a diagnosis.
- Nothing shames: Big cards slide to Big with "This one is Big", an over-cautious Big drop gets "Telling is never wrong",
  zero-day weeks get "That happens."
- Reporting duties in notes are accurate and appropriately hedged (state law and role; an internal report may not satisfy
  a duty to report to the agency).
- People art: one consistent 9-year-old across five poses, calm or smiling in every one, modest seated socks pose; the
  13 worry vignettes have no people, so no group is shown as the one who worries. No stereotype found beyond the hair
  fringe in finding 4.
- Other card art (bedside pills with blank labels, evening kitchen with two mugs, empty bus seat, tablet chat) is gentle
  and not frightening.

Counts: 1 blocker, 4 should fix, 5 polish, 1 nit.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: worry-size-sorter (round 1)

Cold lens, blind to codex-report*.md and codex-review.md. Read: REFINE.md, STANDARDS.md, BASELINE.md, spec.md, src.html
(all), worry-data.json, voice/lines.json, notes.md, tool.draft.json, audit-states.json, refine/sensitivity.md (its
child-safety findings are not repeated here). Drove the bundle in headless Chrome (port 9850, no host server).
My frames: S:/CurioClass-codex-scratch/worry-size-sorter/teaching/frames/. Audit frames cited from audit-r1/.

Standards checked against the SHAPE America NHES 2024 page (indicator text fetched 2026-11-06). Facts spot-checked
against Cleveland Clinic (box breathing), HealthLinkBC (PMR timing), NHS Every Mind Matters and YoungMinds (worry time).

#### Findings

1. **where:** src.html:1027-1031 `because()`, My week builder and goal sentence.
   **what:** the "Because" line is built from the tool's last meter result whatever its direction. A student whose meter
   went UP sets a goal that reads "I will do Squeeze and let go in the morning every day this week. A grown-up at home
   helps me remember. Because my meter went from 2 to 4 when I tried it." The goal's own reason argues against it.
   NHES 6.5.1 asks the student to explain how the goal supports well-being; this teaches the opposite. Same for an
   unchanged meter ("from 3 to 3").
   **how seen:** t2-week-because-up.png, t2b-week-goal-up.png (driven: Squeeze, rate 2, Stop, rate 4, then builder).
   **fix:** use the meter line only when after < before (or calm 1 to 1, worded "I practiced it when I was calm");
   otherwise show the body-clue pick.
   **level:** should fix. **tag:** general.

2. **where:** src.html:325, 1096-1102 (Because row), against worry-data.json clues.
   **what:** "Pick the body clue this tool helps" accepts any clue for any tool, so the goal says "I will do Box
   breathing ... Because it can help with busy thoughts", while the tool's own Body clues mode teaches busy thoughts
   (Head) go with Worry box and Talk back, and box breathing goes with heart, breathing and tummy. The prompt reads as
   a fact question and the tool confirms a wrong pairing. The list also has four clues where Body clues has five (no
   tummy / butterflies).
   **how seen:** t3-week-because-mismatch.png; goal sentence printed by the driver.
   **fix:** either mark the clues each tool answers (from D.clues "tools") and offer only those, or reword to "Pick the
   body clue you want help with" so it is the student's own reason. Add tummy.
   **level:** should fix. **tag:** general.

3. **where:** src.html:769 ("Two rounds, then check your meter."), 898; spec Sources row "Box breathing ... 3 to 4 rounds".
   **what:** both cited sources (Cleveland Clinic: repeat the cycle three to four times; WebMD) give 3 to 4 rounds, the
   spec's own Sources row says so, but the practice ends at 2 and the panel teaches "Two rounds". A student who
   follows the tool learns a shorter practice than the source.
   **how seen:** read code; Cleveland Clinic page fetched. Audit frame state-breathing-stopped-1366x768.png.
   **fix:** default to 3 rounds ("Three rounds, then check your meter"; 48 s at 4, 36 s at 3), still up to 4.
   **level:** should fix. **tag:** general.

4. **where:** Tools opened from the header, Box breathing and Squeeze (src.html:707, 760-764).
   **what:** step 1 says "Picture it's really happening." while the stage shows a bare "A spelling test tomorrow." with
   no "Your worry:" label, and for these two tools the student has no worry picker (only Talk back and Worry box get
   one). A student who came straight to Tools is asked to picture a worry they did not pick and cannot change.
   (Sensitivity finding 6 rewords the prompt; this is about the missing label and choice.)
   **how seen:** t1b-tools-header.png.
   **fix:** for Box breathing and Squeeze opened from the header, hide the worry line and ask "How worried does your
   body feel right now?" only, or offer the same picker.
   **level:** polish. **tag:** general.

5. **where:** Body clues panel "Try:" line (src.html:673).
   **what:** the link from a body clue (S1) to the tool that answers it (S7) is text only. The student reads "Try: Box
   breathing" and has to find Tools and the tile themselves. This is the moment the two standards meet.
   **how seen:** audit state-body-clue-1366x768.png; code.
   **fix:** make each named tool a button that opens Tools on that tile.
   **level:** polish. **tag:** general.

6. **where:** Sort, Medium drop result (src.html:528-531).
   **what:** Medium means "A tool, and talk it over with someone." but the Medium result only offers "Try a tool on it";
   the "talk it over" half (and NHES 1.5.7, when to seek help) is never prompted for a Medium card.
   **how seen:** t4-sort-medium-into-small.png (panel text) and code.
   **fix:** for Medium-sized cards add one line, "Who could you talk this over with?" with the adult chips, or a "Ways to
   start" line.
   **level:** polish. **tag:** general.

7. **where:** worry-data.json b5 reason; NHES 1.5.7 ("Explain when and why it is important to seek health care").
   **what:** the one card that maps to seeking health care ends "is a sign to get help" without saying what help. The
   Doctor and School counselor chips are there, but nothing ties this card to them.
   **how seen:** read data against the fetched indicator text.
   **fix:** "...is a sign to get help. Tell a grown-up you trust; a school counselor or doctor can help with worry."
   **level:** polish. **tag:** general.

8. **where:** My week reflection (src.html:1187-1224).
   **what:** the barrier chips (6.5.4) lead nowhere: picking "I forgot" or "Someone interrupted" changes nothing, and
   the next-week choices are only Keep / Change the time / Try a different tool; there is no "Change who helps me",
   the obvious answer to "I forgot". Reflection (6.5.6) stops at naming the barrier.
   **how seen:** audit state-reflection-1366x768.png ("I forgot" picked, panel unchanged); code.
   **fix:** add "Change who helps me remember", and when "I forgot" is picked, mark it as the suggested choice.
   **level:** polish. **tag:** general.

9. **where:** Sort end panel (src.html:547-548).
   **what:** after an all-Big sort it reads "Big: 13. Every Big one goes to a trusted adult." directly above "You put 8 in
   Big that a tool could also help." The first line counts basket contents, the second admits 8 were not Big-sized.
   **how seen:** t5-sort-end-allbig.png.
   **fix:** "In Big: 13. The 5 Big worries always go to a trusted adult."
   **level:** nit. **tag:** general.

10. **where:** notes.md Sources and "Good to know".
    **what:** notes' source list drops five sources the spec and tool.draft.json cite (WebMD, Michigan Medicine, eSafety,
    Advocates for Youth, US Attorney tip sheet) and adds NHS Every Mind Matters, which tool.draft.json lacks; YoungMinds
    has two different URLs. NHS EMM, cited for worry-time length, actually suggests worry time "before bed"; the
    no-bedtime rule rests on YoungMinds ("Avoid using the box just before bedtime"), so cite that for timing.
    "Narration uses the kit's browser voice fallback in this Build-only version" will be false once voice is recorded.
    **how seen:** read notes.md against spec, tool.draft.json and the fetched pages.
    **level:** nit. **tag:** general.

#### Checked and sound
- Codes: S1 (body clues, "too big to carry", Big cards), S6 (tool, time, helper, reason, 7-day chart, reflection) and
  S7 (four tools done with before/after rating) are each taught by something the student does. 6.5.2 (assistance) is
  the "Who helps me remember" row; 6.5.5 tracking is the chart. No code is only mentioned.
- Meter results: all 25 before/after pairs printed (t8-meter-all): down 10, up 10, same 4, calm start 1, as spec.
- Done when 3: Big cards dropped in Small/Medium go to Big with reason and panel; Small/Medium in Big accepted with
  "Telling is never wrong" (t5, audit sorted-card). Done when 7: day index by calendar date, future days refused,
  day 8 opens reflection (code 1001, 1038, 1173; audit week-chart and reflection frames).
- No giveaway problem: Sort is not a quiz; every option is accepted or corrected with a reason.
- Facts: box breathing 4-4-4-4 (Cleveland Clinic); PMR 5 s tense, 10 s relax within 4-10 s / 10-20 s (HealthLinkBC);
  worry time 10 min within NHS's 10 to 15; no bedtime per YoungMinds; body clues match the spec Sources rows.
- Language plain for grades 3-5; no score, timer challenge or streak; rule 8 note names abuse, online exploitation,
  family illness; Support at home ideas are doable tonight. Cultural / hard-history: nothing beyond what sensitivity.md
  already covers.

Counts: blockers 0, should fix 3, polish 5, nit 2.

#### Audit pilot
- Leads confirmed: none were teaching leads. The "welcome not heard after a first tap on the card or a basket" rows are
  allowed by BASELINE 16; the premise is on the stage (principle line) and in Read, so nothing lost for teaching.
- Leads wrong: none.
- Missed (outside what it can see): the goal reason built from a rising meter (1), the clue-tool mismatch (2), the
  rounds below source (3), and the reflection chips leading nowhere (8).

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: worry-size-sorter (Codex fix, round 1)

The required workspace was S:\CurioClass-codex and was verified before work. No git command or commit was made.
All authored changes stayed in tools/worry-size-sorter/ and _scratch/worry-size-sorter/. refine.md and refine/ were untouched.
Evidence paths below are relative to `_scratch/worry-size-sorter/fix/`; audit paths use `../fix-audit/`.
The original source, data, notes, manifest and prompts are preserved in `original/`.

The user's Curiosity instruction supersedes the older lesson spec: My week, goals, checks, reflection and the Sort
finish panel were removed. The material fills an open-ended desk with its own controls, lower-left Manual and maker's
plate. Nothing was converted into a quiz or scored task. The one-file bundle is 1.76 MB.

#### Blocker
1. FIXED. The b1 bedroom/night vignette was reproduced in `before/before-b1.png` and inspected full size.
   Replaced it with a closed notebook on a sunlit school bench, without people. `proof-a/after-b1-card.png` and
   `art/ws-card-door.webp` were inspected. Prompt and raw source updated with the token retained. The list's final
   section reserves spec text edits to the spec owner, so spec.md was not edited.

#### Should fix
1. FIXED by removal under the Curiosity override. `before/before-because-up.png` reproduced a 2-to-4 reason supporting
   a goal. There is now no goal builder or Because generator: `validation.json` reports zero weekly controls;
   `numeric-proof.json` shows no finish controls after 26 cards, repeated with three basket patterns.
2. FIXED by removing the conflicting goal question. `before/before-clue-mismatch.png` reproduced Box breathing with
   busy thoughts and no tummy choice. Retained clue-to-tool links are now generated from D.clues.tools, including
   both tummy tools. `proof-b/after-body-1366.png`, `proof-b/after-clue-link.png`, `clue-proof.json`: tummy to Talk back
   opens tool 1. The audit's tummy-tool-link also opens Box breathing. No new fact question was added.
3. FIXED. `before/before-breath.png`: target 2 and two-round instruction. `proof-a/after-breath-default.png`: target 3.
   Actual held-click runs in `timing/`: three rounds took 48,144 ms at count 4 and 36,098 ms at count 3 (including
   polling overhead). `fourth-proof.json`: fourth round runs, fifth disabled. Cleveland Clinic and WebMD references below.
4. FIXED. `before/before-digit.png`: meter key 4 switched to week. `retry-final/after-digit-meter-final.png` and
   `digit-proof.json`: mode tools, rating 4. `running-key.json`: digit 1 left breathing running in tools.
   Numeric view shortcuts act only on the desk selectors. Removing My week leaves three view shortcuts, 1 to 3.
5. FIXED. `before/before-settle.png`: returned card opacity .85. After 1.2 seconds, `settle-proof.json` and real jittered
   drag `drag-proof.json` both report Big and opacity 0. `proof-a/after-b1-settled.png` shows the persistent empty slot;
   `retry-settle/after-settle-b1.png` proves the immediate Motion-off destination. Small and Medium use the same mechanism.
6. FIXED. `before/before-privacy.png` reproduced saving with no line. `retry-final/after-privacy-final.png` shows
   "Saved on this device only." at the helper control. `retry-final/after-storage-blocked-final.png` adds the browser
   failure sentence. Result meters now share a horizontal row so this line stays visible at laptop height.
7. FIXED. `before/before-read.png`: the Body clues hint was unregistered. Read now uses L.hints and finite named
   content instead of arbitrary panel innerText. `voice-body.json`, `voice-tools.json`, `voice-final.json` and
   `validation.json`: 146 runtime lines, 146 manifest lines, zero missing and zero extra. See Voice walk for the override.
8. FIXED. Reproduced at all requested widths in `before/before-body-1366.png`, `before-body-680.png`,
   `before-body-375.png`. Inspected after frames `proof-b/after-body-1366.png`, `after-body-680.png`, `after-body-375.png`.
   The Head ring clears the face; Tummy is on the hoodie pocket; heart is on the viewer's right; the hand leader reaches
   the hand. Leaders now use actual ring rectangles and image anchors on render and resize. Final layout also checked by audit.
9. FIXED. `before/before-b3.png` reproduced the promise. `proof-a/after-b3.png` shows the requested blame-free reason;
   worry-data.json and the manifest agree. It makes no promise about another adult's reaction. Spec wording left to owner.
10. FIXED. `before/before-b1.png` lacked the known/family-adult line. `proof-a/after-b1-settled.png` and
    `retry-final/after-read-big-final.png` show/read it; `voice-final.json` records the same text. Spec wording left to owner.
11. FIXED. The top 23 percent hair-region test found 111, 118, 98 and 71 green-dominant pixels on stand, fists,
    shoulders and loose. Re-despill leaves 0 in all four, with 0 changed alpha pixels. `hair-proof.json` and the inspected
    `hair-comparison.png` preserve each original pose. This is edge cleaning, not a person redraw. Toes was untouched.
12. FIXED. `before-numbers.json` records no CyberTipline route in notes. `validation.json` confirms the three requested
    route strings in the adult notes. NCMEC and current DOJ independently confirm the reporting number/URL and Take It Down.
    The latter is qualified for eligible images and participating platforms; no promise of universal removal. Nothing added on screen.

#### Polish accepted
1. FIXED. The card-linked note is now "Think about this worry for a moment." Card-free breathing and squeeze have no
   worry text or that note. See `last-retry/final-tools.png` and `proof-b/after-clue-link.png` for the two relevant states.
2. FIXED. Body clue Try names are real buttons, derived from the clue data; `clue-proof.json` and the tummy-tool-link audit state.
3. FIXED. Medium results add the talk-it-over question; `proof-b/after-medium.png` and `medium-proof.json`.
4. FIXED. b5 names a trusted grown-up, school counselor or doctor; `retry-safety/after-b5.png`, data and manifest.
5. FIXED by removal under the Curiosity override. There is no weekly reflection, "I forgot" chip or next-week assignment.
6. FIXED. `retry-settle/after-settle-s1.png` and `after-settle-m2.png` show the same persistent destination for Small and Medium.
7. FIXED with a sourcing adjustment. "You can put this in Medium. Small is fine too." and the mirror keep the flexible
   tone without inventing a "Many kids" survey claim. `medium-proof.json` and `proof-b/after-medium.png`.
8. FIXED. The slip folds in two stages (halves, quarters), centers above the actual painted slot, then drops to it.
   `proof-b/after-folded.png`, `checks/after-boxed.png` and `focused-safety/fold-calm.png`; Motion off has zero slip animations.
9. FIXED. Four matching inline SVG icons, with different breathing-square and slotted-box shapes; `last-retry/final-tools.png`.
10. FIXED. Adults are one sentence in Read and "Tell one grown-up you trust" occurs once. `voice-final.json` and
    `retry-final/after-read-big-final.png`. The Big hint now only names Next worry, avoiding a repeated telling line.
11. FIXED. b4 and b2 add the requested no-blame statements; `retry-safety/after-b4.png`, `after-b2.png`, data and manifest.
12. FIXED. Home support and teacher disclosure steps added, adult-facing only; `validation.json` verifies the exact routes
    and steps. Childhelp is described as support, not as a substitute for mandated reporting.
13. FIXED. Both rising results and meterOther name a grown-up you trust; `retry-settle/after-rise.png`, `rise-proof.json`, manifest.
14. FIXED by removal under the Curiosity override. No end panel or end-count sentence exists. Baskets retain their
    current contents, and Next worry continues after card 13; `numeric-proof.json`.
15. FIXED. Notes and metadata share 24 named references and rights statements; the Manual has the 17 student-facing references. One canonical YoungMinds
    URL is used, credited for avoiding bedtime; NHS is credited for the ten-minute option. The Build-only fallback claim is removed.
16. FIXED by removing the old automatic-speech wait under the Curiosity voice rule. No Listening state or disabled Next
    remains. All adult-help content stays readable and is in Read. See `voice-final.json` and `proof-a/after-b1-settled.png`.
17. FIXED. Fixed "Shorter count (3)" label with aria-pressed; `proof-a/after-breath-default.png`, both timing frames.
18. FIXED. The placed card's accessible name says Sorted; `settle-proof.json` records it. It no longer says Pick up worry card.

#### Settled calls
- Preserved data-based body/tool pairing, with tummy included, and corrected all five ring positions.
- Digits are scoped to focused controls. The removed fourth lesson mode has no shortcut.
- The Curiosity brief supersedes per-mode welcomes and automatic Big narration. The first quiet hint may be cut by action;
  later speech is requested with Read. No new welcome screen, goal, quiz or forced finish was added.
- The US-only "Danger right now? Call 911." wording is retained. NCMEC/Childhelp details remain in adult notes only.
- No score, timer challenge or streak; all-Big remains accepted and offers adult help without marking an answer wrong.
- Replacement card art has no person. No adult figure was added to any vignette.
- Spec-owner open questions were left open; spec.md and refine.md were not edited.

#### Cheats tried
- All-Small, all-Medium and all-Big for 26 cards each: every intrinsic Big still lands in Big; no finish control appears;
  the desk remains open, with 13 unique placements. No choice earns credit. `numeric-proof.json`.
- Jittered real drag of b1 into Small: goes to Big and remains hidden from the stack, opacity 0. `drag-proof.json`.
- Rate 5, immediately Stop, then rate 1: gives a personal check-in with an early-stop note, no success or saved score.
  The audit's early-stop-rating covers this. Helpers remain an explicit personal preference, not verified mastery.
- All 25 before/after pairs: 10 decreases, 10 increases, 4 unchanged above 1, one calm-to-calm. The text reports the
  rating without making a causal claim. `numeric-proof.json`.
- Digits during a run and while rating cannot switch the view. A fifth breathing round cannot start. Results above.

#### Voice walk
Held clicks were 0.12 seconds, with 2-second gaps on body and tool Read walks. There is no lesson welcome path.
Main walk: Body clues, Tummy, Read. The log contains the ring hint, tummy fact, its two Try tools and the too-big help.
Side walk: breathing Before, Read at Practice, Start, Stop, after rating, Read. The log contains the current practice
hint, square instruction and three-round line, then the helper hint and rising-rating advice.
Big walk: b1, Small, Read. The final log contains the next-action hint, premise, card and corrected reason, Big heading,
one adult sentence, three ways to start, keep-telling advice, emergency line and one privacy/tell-one line.
All parts are registered, with 146/146 exact manifest parity. Headless test audio is muted; this verifies the actual
kit Read invocation/log and recording readiness, not a human listening session or the quality of future recorded takes.

#### Engine changes wanted
No shared file changed. `handoff.md` names the exact audit change: MODES_JS should discover Curiosity navigation outside
headers, and curiosity metadata should suppress lesson welcome-per-mode expectations. Explicit states cover this tool.

#### The real material
No external dataset, clinical record, template or source illustration was imported. The thirteen scenarios, flexible
basket assignments and example replies are fictional Curio Class content (CC BY 4.0); code is MIT. Original generated
illustrations remain credited. The replacement uses the built-in imagegen tool; its full prompt is in art/prompts.json,
and its local raw PNG is art/raw/ws-card-door.png. Hair cleanup is reproducible in fix_material.py.

Live source checks on 2026-11-06 covered Cleveland Clinic, WebMD's respiratory-therapist article, CDC, NIMH, YoungMinds,
NHS, Childhelp, eSafety, NCMEC, Take It Down and DOJ. The main WebMD URL returned 403; the old DOJ tip-sheet endpoint
was inaccessible, so the current named DOJ reference was used. No unavailable reference was invented as a successful fetch.
Other references are inherited fact-check context from the spec, not newly fetched material. The complete rights and
claim catalogue is `source-notes.json`, recorded in tool.draft.json; its student-facing subset is in the Manual. Protected articles
are references only; their copyright is not a permissive dataset licence. No publisher or government endorsement is implied.

- [Nemours KidsHealth · Anxiety](https://kidshealth.org/en/teens/anxiety.html): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [CDC · Anxiety and Depression in Children](https://www.cdc.gov/children-mental-health/about/about-anxiety-and-depression-in-children.html): US federal text is generally public domain; third-party exceptions. Facts referenced, no CDC assets copied; no endorsement. Free at the source. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NIMH · Children and Mental Health](https://www.nimh.nih.gov/health/publications/children-and-mental-health): US federal government public-domain information; no third-party assets copied. Fact-check reference only. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Cleveland Clinic · Box Breathing](https://health.clevelandclinic.org/box-breathing-benefits): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [WebMD · Box Breathing](https://www.webmd.com/balance/what-is-box-breathing): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [WebMD · Respiratory Therapist Breathing Exercises](https://www.webmd.com/lung-cancer/features/respiratory-therapist-breathing-exercises-for-lung-cancer-patients): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Michigan Medicine · Progressive Muscle Relaxation](https://www.uofmhealth.org/health-library/ta4146): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [HealthLink BC · Progressive Muscle Relaxation](https://www.healthlinkbc.ca/healthwise/progressive-muscle-relaxation): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [HereToHelp BC / Anxiety Canada · Healthy Thinking for Younger Children](https://www.heretohelp.bc.ca/sites/default/files/healthy-thinking-for-younger-children.pdf): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [YoungMinds · How to make a worry box](https://www.youngminds.org.uk/parent/blog/how-to-make-a-worry-box-a-guide-for-parents/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NHS Every Mind Matters · Tackling your worries](https://www.nhs.uk/every-mind-matters/mental-wellbeing-tips/self-help-cbt-techniques/tackling-your-worries/): NHS website content: Open Government Licence v3.0, with stated exceptions. Reference only; no source text or assets bundled. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Just One Norfolk NHS · Worry box](https://www.justonenorfolk.nhs.uk/media/us1bjpvw/worry-box.pdf): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Childhelp · Safe vs Unsafe Secrets](https://childhelp.org/safe-vs-unsafe-secrets-how-to-talk-to-kids-about-the-difference/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [eSafety Commissioner · Secrets and surprises](https://www.esafety.gov.au/sites/default/files/2026-09/secrets-and-surprises-sept-2026.pdf): Australian Government copyright; no blanket open licence verified for this PDF. Fact reference only; no PDF/text/art copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Advocates for Youth · Seeking Help](https://www.advocatesforyouth.org/wp-content/uploads/2023/07/2.5_Seeking-Help_3Rs2023.pdf): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NCMEC · NetSmartz / CyberTipline](https://www.missingkids.org/gethelpnow/cybertipline): Copyright NCMEC, all rights reserved. Facts and service names only; no banner, text or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [US Attorney · Online safety tip sheet](https://www.justice.gov/usao-ri/file/765166/dl): DOJ federal text: public domain unless otherwise marked. No source assets copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [US DOJ · Threats to Children Online](https://www.justice.gov/criminal/media/1437006/dl?inline=): DOJ federal text: public domain unless otherwise marked. Facts independently checked with NCMEC; no logos or illustrations copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [NCMEC · Take It Down](https://takeitdown.ncmec.org/): Copyright NCMEC, all rights reserved. Service facts only; no assets copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Childhelp · Responding to a disclosure](https://childhelp.org/what-to-do-if-a-child-tells-you-theyre-being-abused-a-step-by-step-guide/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Childhelp · National Child Abuse Hotline](https://childhelphotline.org/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [Michigan Department of Education · Reporting duties](https://www.michigan.gov/mde/services/ed-serv/educator-conduct/abuse-neglect): State of Michigan copyright; fact-check reference only, no source text copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [American Red Cross · Children’s swim lessons](https://www.redcross.org/take-a-class/swimming/swim-lessons/kids-swim-lessons): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.
- [SHAPE America · NHES 2024](https://shapeamerica.org/standards/health/new-he-standards/): Copyright retained by the named publisher; fact-check reference only. No article text, images or dataset copied. Sampling: none, reference only. Date: 2026-11-06 catalogue review.

#### Short test and lesson creep
The desk was exercised over more than ten minutes of interactions, including real-duration breathing and muscle practice.
Kid opening unassigned: plausible for trying the worry cloud, baskets and folding; no teacher setup required.
Adult using it: useful for trying the same techniques, but its intrinsic playful depth is narrower than Beat Lab's.
Real material is the interface: comfortable timed breathing, muscle tension/release and a personal rating are usable;
the fictional scenarios are explicitly labelled as examples, never presented as measured psychological data.
No score or finish: yes, proved by the repeated-sort traces and source search. A long-term engagement claim is not made.
The approved models were opened and used in `models/`; a side-by-side reference frame is saved as `comparison.png`.
The safety copy retains "wrong" only for unsafe secrets, adult wrongdoing and telling never being wrong. "Try again"
is optional practice advice. The local variable level is only cloud art size. No goal/score/points/sticker/badge exists.

#### Audit
The one required audit finished with exit 0 in ../fix-audit/. Its 42 leads were checked, grouped by cause below.
No console errors, exceptions, disabled-control resize failures or continuously running Motion-off animations were found.
Five held clicks and two quick taps were clean for Sort, Manual, Motion and Read. The 99 audit frames were inspected in
13 contact sheets (`audit-final-sheets/`), with problem frames also opened full size. The audit was not run a second time.

- FIXED, maker text: 9 px at 680x425, 800x500, 1000x625 and 375x812 is now 10 px. Numbers and frames in
  `lead-sort-*.json` and `focused-layout/lead-sort-*.png`; no sideways overflow.
- FIXED, all sorted-card overlap rows across the eight sizes: the audit counted text inside an opacity-zero parent.
  After its flight the card now also has inherited visibility hidden, leaving only the empty slot and thumbnail.
  Focused 680, 800, 1000 and 375 traces show hidden and both result actions visible. The flight still plays normally.
- FIXED, phone Try action: both Try a tool on it and Next worry now precede the optional prose.
  `focused-layout/lead-sort-375.png` and `lead-sort-375.json` show both above the footer.
- FIXED, #meter1 through #meter5 in talk-result, source-result, early-stop-rating and helper-privacy:
  the shared result layout now has at least 44.59 px width in all three compact landscape sizes. Focused meter frames
  and numbers cover 680x425, 800x500, 1000x625, 375x812 and 1366x768. Result text remains readable.
- FIXED, helper-privacy at 680x425 and 375x812: privacy is inside the action block, directly under its buttons.
  It is visible in normal and blocked-storage phone states. `focused-safety/blocked-storage-phone.png` shows both sentences.
- FIXED, phone Manual title/Close bounding overlap: title now clears the floated button, with a 14 px gap.
  `lead-manual-phone.json` and `focused-safety/lead-manual-phone.png` prove it.
- ACCEPTED, the Manual covers #hint: a native modal deliberately covers and makes the desk inert. Its Close button
  is visible and focus returns to Manual; the covered background hint is not a missing instrument control.
- ACCEPTED, missing welcomes on Body clues, Tools, the card and the three baskets: Curiosity policy and the settled
  first-action call supersede this lesson audit expectation. All relevant guidance is available in hints and Read.

The final targeted checks also found and corrected two details: adult reporting source rows are excluded from the
student Manual (zero hotline numbers, 17 relevant references), and the first quiet hint cannot speak over that drawer.
Phone rising-rating advice now fits in full by dropping the redundant phase strip from compact result panels.
`final-result/final-rise-680.png` and `final-rise-375.png` show the grown-up advice, with numbers confirming the full result
above the footer. Reduced-motion folding has zero active slip animations. Final voice parity is still 146/146.
`final-validation.json` contains the final measurements. The source passed `node --check`; the final bundle succeeded.
Successful drive batches have zero console errors. Transient Chrome timeout/connection failures in proof-c.log and
last.log were retained; smaller or successful-profile retries provided the actual passing frames, not inferred passes.
Bundle, drive and audit limits were 120, 300 and 2400 seconds respectively. No audit timeout occurred. Test Chrome ports are closed, the host server is stopped, and temporary host.html was removed. A final keyboard-only Tab/Enter path entered Body clues, then Tools, rated before, started and stopped breathing, and rated after; focus remained on meter3. The grayscale frame retained named baskets and clear controls. See access/final-keyboard.png, access/final-grayscale.png and keyboard-final.json.


#### Left open
- Neither the spec nor docs/CURIOSITIES.md assigns this id a Curiosity number or concept entry. The maker's plate has
  the correct family wording and name; plate is null in metadata rather than an invented number.
- The integrator should reconcile the legacy S6 curriculum mapping and spec text with this explicit Curiosity pivot.
  No shared files could be edited in this task. The tool does not claim to teach the removed goal-setting indicators.
- No new cold sensitivity verdict or recorded voice takes were produced; the next exit check remains independent.
- Adult-use appeal is a design judgement, not user research. No clinical benefit or month-long engagement is claimed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Worry Size Sorter handoff

#### Current shape
This fix follows CODEX-CURIOSITY.md and the user's explicit override. The old kit header, My week goal builder,
check-off chart, reflection and finite Sort end panel are removed. Sort is a continuing desk, with at most one current
placement per fictional card. There are no goal, score, level, quiz or finish controls. NHES S6 is not claimed by this version.
The shared curriculum map is outside this task's write boundary and may still need the integrator's update.

The desk draws its own controls and layout; only kit/curio.js supplies settings, tones and voice. The lower-left Manual
contains use, readout limits, sources and permissions. The maker's plate omits a number because neither the spec nor
docs/CURIOSITIES.md assigns this id a Curiosity number. tool.draft.json has curiosity true and plate null; do not invent a number.

#### Fix mechanisms
- All destinations animate the card into the basket with a persistent invisible end state. Motion off hides it at once.
  Re-rendering a sorted card keeps the empty slot. Big situations always land in Big regardless of the requested basket.
- The meter handles digits 1 through 5 only when it holds focus. Desk selectors handle 1 through 3 only while focused.
  A key inside a running tool cannot change mode. Arrow/Enter sorting and native Tab work.
- Breathing defaults to three full rounds, with one optional fourth. Shorter count (3) has a fixed label and aria-pressed.
  Timing remains real time with Motion off. Squeeze still has three independently tapped parts.
- Body links are derived directly from D.clues.tools. Tummy has both Box breathing and Talk back. Leaders are computed
  from actual ring rectangles to image-relative anatomical anchors after rendering and on resize.
- Folding is two phases, halves then quarters. The folded slip centers above the painted slot; the drop ends at that slot.
- Helpers save under wss-helpers and show the device-only privacy line at the saving control. Blocked storage is caught.
  Legacy wss-week is ignored; existing saved records are not erased or migrated. No new weekly record is written.
- Read uses registered L.hints and finite registered content, never arbitrary panel innerText. allLines and lines.json match.
  The Curiosity brief's voice policy wins: only the first quiet hint may speak automatically, then narration is on Read.
  The old automatic Big speech wait and Listening state were removed along with mode welcomes. No safety content was removed.

#### Safety and material
b1 is now a closed notebook on a school bench in daylight, without people, bedroom or night scene. The asset token is
unchanged. The prompt and raw source were replaced. The four affected hair edges were re-despilled, preserving alpha
and every pose; no new people image was generated. The toes pose is unchanged.

b1 names known/family adults; b3 avoids promising an adult's reaction and states that the child is not at fault.
b2, b4 and b5 include the requested support wording. Adult notes include the online exploitation and disclosure routes.
Hotlines remain out of the student interface. The on-screen immediate-danger 911 wording is the settled US-specific call.

The material is fictional Curio Class situations and original explanatory text, not an empirical dataset. Each student-facing factual
reference has a name, rights statement and URL in the Manual. Adult reporting references remain in notes and metadata. Protected source articles and illustrations
were not imported. No claim that a source's copyright has become CC BY is made. Sources are not endorsements.

#### Spec decisions
The merged list's final section reserves spec text updates to its owner, so spec.md is untouched. Its lesson-flow lines,
two-round wording and old art/safety prompts are superseded by this handoff and the user's Curiosity instruction.
The source-only replacement art has no person, so it adds no contact-sheet entry. Existing sensitivity reasoning was read;
this fix does not claim a new cold sensitivity verdict. Recorded audio is a later media step; no recording service was called.

#### Evidence
All evidence for this pass is under _scratch/worry-size-sorter/fix/, with the mechanical audit in fix-audit/.
The original source, data, notes, voice manifest and prompts are archived in fix/original/. No refine file was edited.

#### Engine changes wanted
scripts/audit_tool.py: MODES_JS currently searches only header descendants. Include a Curiosity's own navigation buttons,
such as .desk-switches button[data-mode], without requiring a lesson header. Suppress welcome-per-mode expectations when
tool metadata says curiosity true. The tool's explicit audit states cover both other views, so no engine edit was made.

#### Final audit response
The single mechanical audit exited 0. Its layout leads were corrected with focused checks: maker text is at least
10 px, compact result meter targets are at least 44.59 px wide, phone result actions and the save privacy line stay
visible, and the Manual title clears Close. The sorted card is also visibility hidden after its flight, so invisible
text is absent from hit testing. Compact results omit the redundant phase strip to keep the adult-help advice in view.
The final Manual has 17 student-facing references; all 24 remain in adult notes and metadata. No adult hotline number
is displayed in the drawer. The modal intentionally covers the background hint, and lesson welcomes remain absent.
The audited bundle was preserved until that run finished; only the confirmed leads were re-shot after the small fixes.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: refine.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/sensitivity.md folded in (last changed 2026-11-08)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-08)
- 2026-11-25: polish.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
