# Morning Show Crew: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: morning-show-crew

#### Built

Three modes, four live media canvases, a four-day crew board, daily audience snapshots and an earned Friday distribution record. Built using the starter structure and Curio Class kit. Ten original paintings, source, bundle, metadata, notes, voice manifest, audit states and handoff are present. Build only; no commits or polish round.

Evidence lives in `_scratch/morning-show-crew/`. `handoff.md` records interpretations, sensitivity and the Spanish release gap.

#### Numbers check

Independent Python: `spec-calculations.py`, `calculations.json`. Browser: `model-results.json`, 523 assertions.

| Plan | Got it by group: on time, bus, learning English, households, teachers | Heard by group | Hours |
|---|---|---|---|
| Announcement + Spanish daily | 220, 0, 38, 0, 18 | 342, 0, 58, 0, 34 | 2.5 |
| Balanced, with Spanish announcements | 346, 29, 56, 61, 32 | 395, 48, 67, 199, 41 | 12 |
| Posters first | 297, 44, 55, 116, 26 | 378, 56, 66, 263, 39 | 8 |
| Same, wrong poster | 102, 1, 19, 78, 11 | 378, 56, 66, 263, 39 | 8 |

The balanced prose omits daily Spanish reads; its quoted 80% English-learning result includes them. Without those reads that group gets 34, about 48%, and the plan costs 11 hours. With them it costs exactly 12 and reproduces the quoted shares.

Totals sum rounded group counts: announcement 276 got / 434 heard; balanced 524 / 750; posters 538 / 802; wrong poster 211 / 802. The spec's 435, 751 and 539 totals round the unrounded aggregate instead. Individual rows agree with the model.

A legal 12-hour poster/site plan reaches 180 of 400 households, about 45%. The spec's under-40% observation is about plans its author tried, not a model limit. No artificial cap is imposed.

410 + 60 + 70 = 540 students; adding 400 households and 45 teachers gives 985 mixed audience units. Households are not called people or included in auditions.

All eight sentence word counts match the spec. The 30-word correct script takes 12 model seconds. Contrast: ink/paper 15.60, ink/white 16.87, muted/paper 6.21, muted/white 6.72, brand/paper 5.27, white/brand 5.70.

#### Facts checked

| Student-visible content | Source and check |
|---|---|
| Four story facts, wrong variants, headlines, eight sentences and shot meanings | `spec.md`, Content. Fictional audition story, copied and checked against the supplied text. Clock hands drawn at 3:15. |
| Five groups and sizes | `spec.md`, Audiences; independent sum above. Notes explicitly treat student groups as disjoint. |
| Job costs, persistence, translations and caption increments | `spec.md`, Jobs; independent model cases and live balanced week. |
| Heard and got-it bars | Spec's own two-meeting Poisson model; Python independently recomputed both functions. Wrong versions contribute only to heard. |
| 8% audition estimate | Spec's own guess, labeled on screen. Calculated only from the first three student rows. |
| Announcement time | Spec's own 2.5 words/second assumption, equivalent to 150 words/minute. NCVS's supplied homepage does not establish a specific universal speaking rate; this is labeled a model. |
| Media standards | [Official NCAS Media Arts at a Glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance.pdf), checked against Pr4, Pr6 and Cn10. Students integrate forms, distribute for audiences and revise for a purpose. |
| Spanish script | Provisional translation, not speaker-approved. Exact Thursday deadline wording was corrected to “a más tardar el jueves.” Approval and recording remain open. |

Britannica's effective-frequency idea is context in the spec, not a claim that two encounters guarantee learning. No empirically validated reach or attendance claim is made.

#### Break it

- Tried every combination of null/right/wrong text facts across video, poster and site, and all 256 announcement subsets. Correctness requires all four facts; wrong time or sign-up overrides right content and visual support.
- Tried repeating announcement chips to pass: duplicates lengthen the time bar but never add audience meetings. A 50.4-second script turns amber. There is no score for a short or long script.
- Tried buying beyond three hours: the complete plan rolls back, with the remaining-hours message. Four days cannot bank unused hours.
- Tried repeated Run day during animation: one snapshot only. Undo removes it. Later Make edits cannot repair past validity or raise past results.
- Tried captions without an aired video, copies without design, and canceling the parent production job: no free reach. Missing design is labeled; planned copies can be canceled.
- Tried using a wrong poster widely: heard stays 802, got falls from 538 to 211. Spanish increments inherit the medium's validity.
- Tried inflating auditions with households or teachers: excluded. “What reached whom” counts meetings, not unique recipients.
- Matching badges deliberately coach consistency against a visible story brief. This is an editor, not a hidden-answer quiz; no points, mastery award or saved best can be farmed.
- Reset cancel preserves work; confirmed Reset clears it. Storage failure is caught and reported on screen.

#### Voice walk

`student/results.json`: 67 real held-input actions, 21 assertions, zero browser errors. The final direct-cell route makes all four versions and runs the balanced week. Native select keys were used for fact categories.

Heard starts on that route: factHow, scriptHow, allMatch, welcomeWeek, dayDone after the first three days, then fridayHow after Thursday. The extended Friday walk below verifies the remaining queued events. welcomeMake is intentionally stale after the first fact tap, as specified. allMatch now triggers only on transition into four matching versions.

`voice-friday.json`: welcomeWeek, fridayHow, dayDone, fridayLine, noOne. Read-first side path: Read, factHow, mismatch twice, welcomeWeek, fridayHow, noOne. Context changes cancel speech that no longer fits.

`voice-how-five.json`: one shotHow start and four silent repeats. `voice-segment.json`: the segment was playing and the narration log stayed empty. Playback edits remain live. Reset now has its own contextual how-to instead of a welcome behind the dialog.

Final quick-tap checks cover active Make, The week, Friday, medium, slot and editor tabs. All six preserve their spoken instruction with no cut entries. The final direct-cell student walk was rerun after the board correction.

Fixed narration uses browser fallback with lively-host/Sadachbia metadata for future clips. Eighteen fixed lines are listed. No audio was recorded. Chrome was muted for automation, so this verifies queue behavior, not a human listening review or the bank voice's recorded identity.

#### Feel check

Best moment: Friday made a production decision concrete: the balanced plan reached 84% of on-time students but only 48% of late-bus students and 15% of households. The record belongs to the student's choices, and the next attempt has a clear purpose.

Flattest moment 1: repetitive fact selection could feel like form filling. Changed the work into four distinct, painted surfaces, with immediate red wrong-fact outlines, a live shot strip, one emphasized poster line and a timed spoken script.

Flattest moment 2: the first week board looked like bookkeeping and warnings covered its controls. Added edit-progress bars, symbolic school-map meetings, persistent-job annotations and separate heard/got bars; moved warnings to the reserved hint area. Repeated active-tab taps preserve their instruction instead of cutting it off.

Compared with both reference tools. `bar-comparison.jpg` places the painted studio beside Beat Lab. The art is richer and the control hierarchy holds its own. The week board is intentionally plainer than Make, since time and audience consequences are its focus. I would replay to repair a missed group; 25-40 minutes of engagement remains a classroom evaluation, not a measured claim.

#### Done when

1. PASS: canvas, crew board and Friday bars dominate their modes at laptop and preview sizes. All desktop baseline sizes passed the audit's geometry checks.
2. PASS: wrong chips outline and flip badges; correcting them restores matching. Exhaustive validity checks cover each core medium and announcement subset.
3. PASS with source corrections: all three plans reproduce the formula; balanced needs the omitted Spanish reads. Group counts and rounding policy are documented above.
4. PASS: three hours/day, four-hour edit spread, no hour banking. Balanced edit is 0.5 h Tuesday, 2.5 Wednesday and 1 Thursday, then first airing.
5. PASS: real input tested future-slot changes, next-loop edits, Stop, live Undo, mode changes and resize during a run. Timed captures show a future slot as shot 7 in slot 4, and a previously played slot as shot 3 on the next loop with its queued marker cleared.
6. PASS: five group shares/counts, never-heard counts, student-only audition estimate and per-medium meetings are present. Friday accepts partial weeks.
7. PASS for the tested queue rules: how once, events on their next fitting occurrence, Read priority and no speech over the segment. Six rapid-tap families pass without cutting their instruction.
8. PASS: versions, plan and snapshots survived reload; Reset cancel/confirm and unavailable storage were checked.

#### Wave lessons

| Lesson | Result and evidence |
|---|---|
| Hint and voice | PASS: hints update synchronously and name controls. Read and held-click voice paths checked. Dialog instructions are contextual. |
| Focus and layout | PASS after fixes: controls stay mounted, hint space is reserved, mode handoffs focus the destination header with preventScroll. |
| Sizes | Desktop/preview PASS, 44 px targets. FAIL for the literal phone no-scroll rule: canvas precedes controls and requires vertical scrolling, as the spec's phone flow requests. |
| No giveaways | PASS for this editor: no hidden quiz or farmable score. Consistency coaching is explicitly requested. Distribution still requires valid work and time. |
| Honest numbers | PASS: fictional model and 8% guess labeled; meetings separated from unique audiences and student attendance. |
| Standards | PASS: solo actions integrate media, distribute to groups and revise for purpose/audience. No family engine is specified. |
| Motion off | PASS: day resolves immediately; no infinite animation remains. Segment timing is retained. |
| Short choices visible | PASS on desktops/previews after the shot-bin fix. FAIL for simultaneous first-screen phone visibility; the phone uses a scrolling page, not a hidden choice panel. |
| Resize mid-animation | PASS in the live walk and the completed audit: no exceptions or controls left disabled. |
| No late first-tap welcome | PASS by design: a tap's own line or stale welcome wins; welcomeAfter is not enabled. |
| Unknown stays unknown | PASS: future reach is not shown as achieved. Results include only committed days. |
| One look, one meaning | PASS: labeled group colors; striped heard and solid got bars; check/cross badges. Grayscale inspected. |
| Badge says what is true | PASS: wrong or missing facts fail; wrong text overrides images; Big names the actual emphasized line. |
| Hint changes back | PASS: tab, mode, undo and reset-cancel restore the current action hint. |
| No copying-answer quiz | PASS: the supplied facts are the editor's brief. No assessment claim is attached to copying them. |

#### Audit leads

Completed once within the 40-minute limit: 66 leads, 42 frames. No runtime exceptions, undersized targets or resize lockups were found. Final follow-ups report zero browser errors and no controls outside the viewport or under 44 px in the corrected desktop states.

The audit was run once against the pre-fix bundle. Its snapshot is retained under `audit/host/tool.html`; the final bundle has targeted follow-up evidence, not a second full audit.

- 22 phone fold/hint/keep leads: retained as the documented scrolling-layout exception. The keep requirement on the shot bin was too strong for the specified canvas-first phone flow; choices remain reachable by page scrolling. This is not claimed as a strict no-scroll pass.
- 18 layout/grammar leads: fixed. These comprise two week-legend/footer overlaps, two shot-bin/Reset overlaps, two site-header/studio-label overlaps, and twelve poster-budget leads covering the toast, audience/footer crowding and singular copy wording. Warnings now occupy the reserved hint area; space is recovered from the map while editing posters; compact redundant text is removed.
- 15 first-tap premise leads: intentional first-tap/staleness behavior required by the spec and STANDARDS. The affected controls are Friday; all four media tabs; all four slots; Play segment; Facts, Shots and Headline; and both fact variants. Their own instruction wins or the Make welcome is stale. Friday speaks fridayHow; playback stays narration-free. No late welcome is inserted.
- 3 focus handoff leads: fixed for See Friday, Try the week again and Back to Make. Native input traces now reach m-friday, m-week and m-make with preventScroll.
- 8 quick-tap speech cuts: fixed for the three mode buttons, four media-tab cases and the slot case. Repeating an active selection no longer hushes its instruction. Six representative handler families were tested afterward with no cut entries.
- Five-click how-to repetition checks were clean. Motion off was clean. All state and control resize stress checks finished with no exceptions or disabled-control lockups.
- Final spec correction: board cells now purchase/cancel directly, with separate Spanish-read, Spanish-poster, Spanish-site and caption rows. The revised board was checked at all seven desktop/preview sizes, through the phone host, and by buying all eight job types with real input. The balanced full student path was rerun and still reproduces the expected counts.

#### Frames looked at

Reference frames for Snowy Mail Route and Beat Lab; all early, full-size, student, phone, targeted, keyboard, voice and final-check frames. Audit frames were inspected in five contact sheets, with problem states also opened at full size. All 42 audit PNGs appear in audit-sheets/index.json; 43 additional frames appear in final-evidence/index.json. The final eight-row board and phone week were also inspected at full size.

Evidence folders: `early/`, `early-fixed/`, `model/`, `student/`, `full/`, `targeted/`, `phone/`, `voice-frames/`, `final-voice/`, `final-check/`, `audit/`, `audit-sheets/`, and `audit-followup/`. Grayscale, long/short script, zero reach, completed week, reset modal and Motion off are included. No dragging mechanic exists.

#### Art made

Ten original generated paintings, all marked people false. Eight shots at 1280×720, studio at 1600×900 and corkboard at 1600×1200. All appear in the tool; clock hands and sign-up writing are code. Prompts and raw originals retained. No subjects needed redrawing.

Final art: 1,378,672 bytes (1,378.7 KB). Recorded voice: 0 KB. Final bundle: 1,949,563 bytes (1,949.6 KB), below the 2,000 KB goal. Ten WebP images are embedded. No remote resource links are present.

All were inspected, including `art-contact/art-contact.png` and the large-screen scene. The initial 700 KB art estimate grew to support full-size pictures while retaining the 2 MB bundle goal. Quality is 72; no teaching image was dropped.

#### Art still to paint

None. No people assets were needed. Spanish audio is an audio/review gap, not missing art.

#### Engine changes wanted

None required. Approved Spanish clips should be supplied before release; no shared kit or family source was changed.

#### Left open

- Spanish speaker approval and the required fixed Spanish recording remain incomplete. English/fixed speech uses browser fallback. This is built beta, not release approval.
- Phone controls and hints need vertical scrolling. This follows the spec's canvas-then-controls phone flow but does not meet STANDARDS' literal all-controls-without-scroll wording.
- The audit snapshot predates the listed targeted fixes; no second full audit was run, per the one-audit rule.
- One scope failure: the reference bundle command regenerated ignored `tools/snowy-mail-route/snowy-mail-route.html`. No reference source was changed. No commits or git commands were run.
- The first read-only instruction/memory commands used the tool wait setting rather than an enforced process deadline. All subsequent build and check commands used bounded `run.py` deadlines.
- Classroom pacing, recorded-voice quality and the Spanish language review remain for cold review/owner evaluation.

All owned Chrome and host processes are closed; assigned ports 8795 and 9990-9997 were checked closed. Temporary tools/morning-show-crew/host.html was removed. No commits, branch operations, uploads or polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: morning-show-crew

#### Played

Cold Grade 7 solo trial across all four media, day planning and partial Friday before reading builder material. Then a full balanced week with native held clicks and select keys. The painted editing room is strong; the audience split gives the week a reason to replay.
#### Findings fixed

- Blocker, general, Friday: zero got-it share incorrectly triggered a never-heard reflection. Trigger now requires a genuinely unreached group; tested every group heard with zero valid meetings.
- Should fix, general, Make/The week voice: ordinary next edits cut still-relevant instructions. Preserve that instruction while dropping stale queued speech; main walk rechecked.
- Should fix, general, phone: choices and hint began below the viewport. Current choices, Run/Undo and Read hint now fit; inspected and corrected row/action overlap and clipped Friday payoff.
- Should fix, general, Make art: clock/signup overlays followed a different crop from their picture. Matched cover crops, put Friday on the clock, and made the sign-up location explicit.
- Should fix, general, completed week cells: later edits repainted old warning badges. Completed cells now use the day's frozen published validity, as their results do.
- Should fix, general, wrong announcement: feedback named an absent variant control. It now names Undo sentence, with a contextual how-to and matching voice-manifest lines.
- Should fix, general, Reset: segment/script could continue behind the dialog. Both stop before it opens; cancel and confirm checked.
- Polish, general, week: lifted the flattest reveal with daily got-it gains and redrew the weakest art, five identical map houses, as distinct school/bus/classroom/home/staff contexts with dispatch paths.
- Polish, general, Friday: the result board now repeats the assumption of two complete, matching meetings and says it is not measured understanding.
- Should fix, general, audit frames at 680x425: poster choice text, the short script and Friday's attendance explanation clipped despite clean geometry checks. Reduced redundant labels and adjusted compact line spacing; targeted preview re-shoots checked the fix.
- Should fix, general, audit Play click: the shorter Stop label shifted three shot controls. Reserved the transport column width, retaining its appearance and live controls.
- Should fix, general, Motion during a day: finishing immediately left its old timer pending, which could repeat the day result. Completion now cancels that timer; a targeted old/new side-path check covers it.
#### Findings left

- Blocker for release: the spec requires a Spanish-speaker check and fixed Spanish recording. Neither exists. CODEX-BUILD prohibits recording, and this unattended run cannot supply that language approval. The draft remains visibly pending; no release pass is claimed.
- Polish, 680x425 poster extreme: making the full sign-up fact Big crowds its photo into a thin strip. The normal poster and laptop canvas retain their painting; a further layout rebalance is left open.
#### Break it

- Four version checks: tried both variants, null/right/wrong combinations, image support, wrong overrides and all 256 announcement subsets, including duplicates. Wrong then right obtains a match immediately, as required; a remaining wrong time or signup never passes. These visible editor checks do not establish the student's mastery.
- Script time: repeated greetings did not supply missing facts; both wrong sentences overrode right ones. Sixty long sentences produced 288 seconds and amber OVER 30 s. Length alone earns no score or added reach.
- Crew hours: bought translations/captions without parents, spammed copies beyond the day's budget, and tried Run repeatedly with Undo. Invalid jobs stayed unbought; budget stopped at 3 h; one run made one snapshot; Undo removed it.
- Video progress/playback: four editing hours plus airing are charged; no caption reach without aired video. A real future-slot edit put the ticket-table shot in slot 4. Reset stopped active playback.
- Audience bars and medium meetings: independent Poisson calculation reproduced all plans; wrong poster kept 802 heard while got-it fell from 538 to 211. Later fixes did not rewrite published validity or totals. Meetings are labeled as non-unique.
- Auditions: student rows only, at the labeled fictional 8%; households and teachers cannot inflate it. No saved best, points or mastery award exists.
- Reflection: all five groups heard something but got zero did not trigger noOne; genuine zero-heard visits did, five of five times.
- Browser model suite: 967 assertions, zero failures; final reset confirmation, keyboard route, grayscale and live future-slot check also passed.
#### Voice walk

Video inclusive fact; Poster four facts using native select keys; Site four facts; Announcement sentences 1/2/3; balanced jobs with daily Spanish reads; run Monday through Thursday; Friday. Held 120 ms, ordinary taps two seconds apart, plus the animation's four seconds.
Heard in order: factHow, scriptHow, allMatch, welcomeWeek, dayDone three times, fridayHow, dayDone, fridayLine. All mode instructions and all four dayDone lines finished; allMatch was stopped on leaving Make. Zero browser errors; queue empty. welcomeMake was skipped on the first fact tap, permitted by BASELINE 16.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| shotHow, five same-step taps | how | 1 | 1 |
| mismatch, five wrong selections | event | 5 | 5 |
| fridayHow, five Friday visits | how | 1 | 1 |
| noOne, five zero-heard visits | event | 5 | 5 |

Read with Sound off spoke the hint; a new mode replaced it without a delayed old line. Segment playback had no narration. This checks queue behavior in muted Chrome, not recorded-voice quality; all fixed speech currently uses browser fallback.
#### Facts checked

- Story facts, inclusive wording, wrong alternatives, headlines and optional friend sentence: fictional Content in spec.md; exact time, room and deadline checked in text and overlays.
- Group sizes, crew/job costs, reach rates, persistence and 8% auditions: Curio Class's fictional spec model. 540 students, 400 households, 45 teachers; 985 mixed units, not people. Independent script and live cases agree.
- Heard/got formulas: [NIST, Poisson distribution](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm), complementary probabilities for zero and one events; not a validated comprehension threshold.
- Repeated exposure context: [IAB UK, Frequency](https://www.iabuk.com/jargon-buster/frequency). Britannica's spec URL was unavailable; no two-exposure learning claim is attributed to it.
- Announcement timing: 30 counted words / 2.5 = 12 s, with 150 words/minute explicitly a model assumption. [NCVS](https://ncvs.org/) does not substantiate a universal 150-word rate on the supplied page.
- Media standards: [NCAS Media Arts at a Glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance.pdf), Pr4 integrated forms, Pr6 distribution, Cn10 purpose/resources. Students perform these actions; no family engine.
- Contrast recomputed with [W3C WCAG relative luminance](https://www.w3.org/TR/WCAG21/#dfn-relative-luminance): ink/paper 15.60, ink/white 16.87, muted/paper 6.21, muted/white 6.72, brand/paper 5.27, white/brand 5.70.
- Reference plans: per-group rounding gives announcement 276 got / 434 heard, balanced with Spanish 524 / 750, posters 538 / 802. The spec's aggregate totals round differently. Without the omitted balanced Spanish reads, learning-English got is 34, not 56.
#### Sensitivity

Spanish language access needs a fresh reviewer: natural school wording, exact Thursday deadline, equivalence to all four facts, and the pending recording. Check that fictional reach rates/disjoint student groups are not presented as measured traits or real identities. Ten empty-school paintings have people:false and contain no people; no tradition, religion, bodies or hard history is taught.
#### Flattest moment left

Headline selection changes presentation but not modeled reach. All three fit by spec; I kept that choice and the strong painted surfaces instead of adding a scoring feature.
#### Graphics

Inspected all ten delivered WebPs and their canvas/thumbnail use. Retained all paintings; redrew the code map and repaired overlays. Compared with existing Beat Lab and Snowy Mail Route frames without rebuilding either. Final bundle: 1,958,613 bytes (1,958.6 KB).
#### Audit

Completed once within the 40-minute limit: 16 mechanical leads, 47 frames inspected. All 16 are first-tap welcome drops/cuts permitted by BASELINE 16; current instructions remain in the hint and Read. Sizes, listed states, focus/runtime checks, Motion off, five repeats, quick taps and resize stress were otherwise clean. Frame review found three compact text clips and the Play/Stop strip shift; local fixes were checked only in the affected states/sizes. The Motion-timer fix has targeted old/new checks and a fresh main voice walk. No second audit was run.
#### Left open

- Spanish approval/recording above. Native browser fallback does not establish the lively-host recorded identity.
- The spec's balanced prose omits Spanish reads needed for its quoted result; its under-40% household observation is not a cap. A legal 12-hour plan gets 180/400, about 45%; verified, not constrained artificially.
- Make's mandated instant badges permit trial-and-error completion without reading every fact. I kept the spec's editor feedback; preventing that route would require a new assessment gate. No mastery or best-score claim is attached to it.
- Initial read-only commands used the execution tool's wait setting before an explicit process deadline wrapper was established. Later shell/build/drive/audit commands were bounded. One CDP-disconnected after-check was retried once as a smaller batch and passed.
- All authored changes are in the assigned tool and Scratch folders. No git operations or commits. All owned Chrome/host ports are closed; temporary host.html removed. Evidence: review-audit/, review-voice-final/, review-after/, review-render-final/, and review-audit-followups/ in Scratch.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Morning Show Crew build handoff

#### Structure

The starter's kit imports, metadata and accessibility frame are retained. Tool CSS lays out three modes at real pixel sizes. The main script holds content tables, state, Curio.voice, validity and media renderers, the deterministic schedule and reach model, then static controls and event handlers. Interactive controls are created once; updates change their content and state without replacing them.

`schedule()` computes four daily production records from the plan. `runDay()` commits a snapshot including version validity and content. `results()` uses only committed snapshots. Undo pops one snapshot. This prevents later Make edits from repairing earlier meetings and prevents repeat run taps from inflating reach.

Board cells buy or cancel directly. Full layouts have separate Spanish announcement, Spanish poster, Spanish site and captions rows. The first poster cell buys design; after an earlier day has design, a later cell buys one copy or cancels that day's copies. The desk adjusts quantities and also exposes secondary jobs in compact layouts. Existing published posts/copies persist, so cancel their original unrun purchase to remove them from a plan.

During a day the map shows the new symbolic meetings, while audience numbers retain the previous day until the four-second reveal. Undo and mode changes remain immediate. Repeated taps on the active tab preserve its instruction; navigation from inside a mode focuses the destination header with preventScroll.

#### Spec decisions and contradictions

- No open-question section exists. Use the stated facts, house palette and lively-host bank metadata.
- The user requires the image tool; this supersedes the spec's local-FLUX method. All ten required paintings were generated with OpenAI gpt-image and marked people false. No people were needed by these empty-school shots.
- The brief prohibits recording audio. Spanish speaker approval and a recorded Spanish script cannot be supplied unattended. Keep the model job, show the provisional fixed script, and mark the required recording as open. Browser speech previews the variable English script. Fixed lines also use the kit fallback until recordings exist.
- The balanced reference's quoted English-learning share includes Spanish announcements all four days, though its prose omits that job. Including it makes the plan exactly twelve hours. The reference without it gives 48%, not 80%, in that group.
- Reference totals differ by rounding convention. Use per-group rounding and report computed numbers. Do not alter spec.md.
- The family share is not capped at 40%. A legal twelve-hour plan reaches about 45%: Mon poster design and site; Tue Spanish site and eight copies; Wed Spanish poster and eight copies; Thu twelve copies. The spec's statement describes only plans its author tried.
- The source calls all 985 audience units people, although 400 are households. UI and notes distinguish units and exclude households and teachers from auditions.
- A visual shot is allowed to carry its named fact, as the spec leans toward. Wrong text overrides it. This shorthand is explained in notes.
- The multi-day edit uses spare quarter-hour blocks and reserves its finishing half-hour for the first airing. Completed videos need half an hour per further airing, and a day can be paused. This resolves the unspecified allocation order without borrowing hours.
- Small landscape previews and compact phones collapse Spanish/caption subrows into cell annotations and the selected medium's job inspector. Full boards retain the subrows. Main four-media board and Run/Undo remain visible.
- Motion off makes this spec's day animation immediate, overriding the general pacing guidance for that four-second map only. Segment timing stays fourteen seconds.
- Try the week again clears run history while keeping the week plan and all versions, allowing direct revision.
- The user's stop condition takes priority over the brief's instruction to start the final report early. The final report is written only after checks, then work stops.

#### Sensitivity

Language access appears in a fictional model. Review the Spanish draft for natural school wording, the exact Thursday deadline, and equivalence to the four English facts. Check that model rates are never read as measured traits of Spanish speakers or language learners. Student categories are disjoint for the model; they do not describe the complexity of real students' identities. No cultural tradition, bodies, religion or hard history is taught.

#### Engine changes wanted

None needed for this implementation. The shared kit's fallback cannot reproduce the lively-host recording identity, and Curio.say does not select a language for mixed-language scripts. Approved Spanish audio should be supplied as a fixed clip before release.

#### Next work

Cold review evidence is in codex-review.md. Resolve the Spanish recording and speaker check before release. Do not infer release approval from the build or browser-fallback queue checks.

#### Cold review changes

The 2026-11-06 cold review retained the painted set and all production/reach rules. It corrected Friday's noOne trigger to test zero heard meetings, rather than zero got-it share. The fixed line now names a whole unreached group. The result board repeats the two-complete-meeting assumption and distinguishes it from measured understanding.

Clock and sign-up overlays use the same cover crop as their images; the clock now includes Friday, and the sheet names the outside-room location and Thursday deadline. Reset stops both playback paths before its dialog. Phone layouts keep the current controls and actions in view; compact week translations/captions remain on the selected desk. The weakest drawing, the audience map, now distinguishes the five contexts and shows dispatch paths. Daily audience counts include the gain in got-it recipients.

Completed board cells use their frozen published validity for warning badges. Editing later versions cannot repaint that history. Same-step fact edits and week purchases preserve a playing, still-relevant how-to line through `keepInstruction`; stale event speech is still stopped. Mode changes, Reset, Read and playback retain their explicit stop behavior.

Audit-frame inspection also found clipping in the 680x425 poster choices, short announcement and Friday attendance explanation. Compact line spacing and redundant fact-category labels were adjusted locally. The transport column now keeps its width when Play becomes Stop. Completing a day clears its pending timer, including when Motion is switched off mid-run. Spanish draft text has lang=es with its English status label marked separately.

The audit snapshot predates these final compact CSS, transport, language-markup and timer corrections. Targeted preview frames and old/new Motion checks verify them without a second full audit; the main voice route is rechecked after the timer correction.

Spanish speaker approval and fixed recording remain a release blocker under the no-recording constraint. No claim of completed audio review is made. See codex-review.md for independent evidence, exact remaining limits and audit disposition.

#### Validation pointers

`_scratch/morning-show-crew/validation-summary.json` records 523 model assertions, 21 live-path assertions over 67 real actions, 45 final checks, exact sizes and SHA-256 hashes. `week-final/` covers the final direct-purchase board at all seven desktop/preview sizes and all eight job rows. `audit-followup/` and `audit-voice-followup/` prove the targeted fixes. The single completed audit has 66 leads against an earlier snapshot; the report disposes of each category and retains the phone scrolling exception. No second full audit was run.

#### Build scope exception

The reference bar check accidentally regenerated the ignored `tools/snowy-mail-route/snowy-mail-route.html` using the bundler. That was outside the user's write boundary. No reference source was edited, and no git operation was performed. All other created files are inside this tool and its Scratch directory.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
