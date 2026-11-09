# Codex report: morning-show-crew

## Built

Three modes, four live media canvases, a four-day crew board, daily audience snapshots and an earned Friday distribution record. Built using the starter structure and Curio Class kit. Ten original paintings, source, bundle, metadata, notes, voice manifest, audit states and handoff are present. Build only; no commits or polish round.

Evidence lives in `_scratch/morning-show-crew/`. `handoff.md` records interpretations, sensitivity and the Spanish release gap.

## Numbers check

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

## Facts checked

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

## Break it

- Tried every combination of null/right/wrong text facts across video, poster and site, and all 256 announcement subsets. Correctness requires all four facts; wrong time or sign-up overrides right content and visual support.
- Tried repeating announcement chips to pass: duplicates lengthen the time bar but never add audience meetings. A 50.4-second script turns amber. There is no score for a short or long script.
- Tried buying beyond three hours: the complete plan rolls back, with the remaining-hours message. Four days cannot bank unused hours.
- Tried repeated Run day during animation: one snapshot only. Undo removes it. Later Make edits cannot repair past validity or raise past results.
- Tried captions without an aired video, copies without design, and canceling the parent production job: no free reach. Missing design is labeled; planned copies can be canceled.
- Tried using a wrong poster widely: heard stays 802, got falls from 538 to 211. Spanish increments inherit the medium's validity.
- Tried inflating auditions with households or teachers: excluded. “What reached whom” counts meetings, not unique recipients.
- Matching badges deliberately coach consistency against a visible story brief. This is an editor, not a hidden-answer quiz; no points, mastery award or saved best can be farmed.
- Reset cancel preserves work; confirmed Reset clears it. Storage failure is caught and reported on screen.

## Voice walk

`student/results.json`: 67 real held-input actions, 21 assertions, zero browser errors. The final direct-cell route makes all four versions and runs the balanced week. Native select keys were used for fact categories.

Heard starts on that route: factHow, scriptHow, allMatch, welcomeWeek, dayDone after the first three days, then fridayHow after Thursday. The extended Friday walk below verifies the remaining queued events. welcomeMake is intentionally stale after the first fact tap, as specified. allMatch now triggers only on transition into four matching versions.

`voice-friday.json`: welcomeWeek, fridayHow, dayDone, fridayLine, noOne. Read-first side path: Read, factHow, mismatch twice, welcomeWeek, fridayHow, noOne. Context changes cancel speech that no longer fits.

`voice-how-five.json`: one shotHow start and four silent repeats. `voice-segment.json`: the segment was playing and the narration log stayed empty. Playback edits remain live. Reset now has its own contextual how-to instead of a welcome behind the dialog.

Final quick-tap checks cover active Make, The week, Friday, medium, slot and editor tabs. All six preserve their spoken instruction with no cut entries. The final direct-cell student walk was rerun after the board correction.

Fixed narration uses browser fallback with lively-host/Sadachbia metadata for future clips. Eighteen fixed lines are listed. No audio was recorded. Chrome was muted for automation, so this verifies queue behavior, not a human listening review or the bank voice's recorded identity.

## Feel check

Best moment: Friday made a production decision concrete: the balanced plan reached 84% of on-time students but only 48% of late-bus students and 15% of households. The record belongs to the student's choices, and the next attempt has a clear purpose.

Flattest moment 1: repetitive fact selection could feel like form filling. Changed the work into four distinct, painted surfaces, with immediate red wrong-fact outlines, a live shot strip, one emphasized poster line and a timed spoken script.

Flattest moment 2: the first week board looked like bookkeeping and warnings covered its controls. Added edit-progress bars, symbolic school-map meetings, persistent-job annotations and separate heard/got bars; moved warnings to the reserved hint area. Repeated active-tab taps preserve their instruction instead of cutting it off.

Compared with both reference tools. `bar-comparison.jpg` places the painted studio beside Beat Lab. The art is richer and the control hierarchy holds its own. The week board is intentionally plainer than Make, since time and audience consequences are its focus. I would replay to repair a missed group; 25-40 minutes of engagement remains a classroom evaluation, not a measured claim.

## Done when

1. PASS: canvas, crew board and Friday bars dominate their modes at laptop and preview sizes. All desktop baseline sizes passed the audit's geometry checks.
2. PASS: wrong chips outline and flip badges; correcting them restores matching. Exhaustive validity checks cover each core medium and announcement subset.
3. PASS with source corrections: all three plans reproduce the formula; balanced needs the omitted Spanish reads. Group counts and rounding policy are documented above.
4. PASS: three hours/day, four-hour edit spread, no hour banking. Balanced edit is 0.5 h Tuesday, 2.5 Wednesday and 1 Thursday, then first airing.
5. PASS: real input tested future-slot changes, next-loop edits, Stop, live Undo, mode changes and resize during a run. Timed captures show a future slot as shot 7 in slot 4, and a previously played slot as shot 3 on the next loop with its queued marker cleared.
6. PASS: five group shares/counts, never-heard counts, student-only audition estimate and per-medium meetings are present. Friday accepts partial weeks.
7. PASS for the tested queue rules: how once, events on their next fitting occurrence, Read priority and no speech over the segment. Six rapid-tap families pass without cutting their instruction.
8. PASS: versions, plan and snapshots survived reload; Reset cancel/confirm and unavailable storage were checked.

## Wave lessons

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

## Audit leads

Completed once within the 40-minute limit: 66 leads, 42 frames. No runtime exceptions, undersized targets or resize lockups were found. Final follow-ups report zero browser errors and no controls outside the viewport or under 44 px in the corrected desktop states.

The audit was run once against the pre-fix bundle. Its snapshot is retained under `audit/host/tool.html`; the final bundle has targeted follow-up evidence, not a second full audit.

- 22 phone fold/hint/keep leads: retained as the documented scrolling-layout exception. The keep requirement on the shot bin was too strong for the specified canvas-first phone flow; choices remain reachable by page scrolling. This is not claimed as a strict no-scroll pass.
- 18 layout/grammar leads: fixed. These comprise two week-legend/footer overlaps, two shot-bin/Reset overlaps, two site-header/studio-label overlaps, and twelve poster-budget leads covering the toast, audience/footer crowding and singular copy wording. Warnings now occupy the reserved hint area; space is recovered from the map while editing posters; compact redundant text is removed.
- 15 first-tap premise leads: intentional first-tap/staleness behavior required by the spec and STANDARDS. The affected controls are Friday; all four media tabs; all four slots; Play segment; Facts, Shots and Headline; and both fact variants. Their own instruction wins or the Make welcome is stale. Friday speaks fridayHow; playback stays narration-free. No late welcome is inserted.
- 3 focus handoff leads: fixed for See Friday, Try the week again and Back to Make. Native input traces now reach m-friday, m-week and m-make with preventScroll.
- 8 quick-tap speech cuts: fixed for the three mode buttons, four media-tab cases and the slot case. Repeating an active selection no longer hushes its instruction. Six representative handler families were tested afterward with no cut entries.
- Five-click how-to repetition checks were clean. Motion off was clean. All state and control resize stress checks finished with no exceptions or disabled-control lockups.
- Final spec correction: board cells now purchase/cancel directly, with separate Spanish-read, Spanish-poster, Spanish-site and caption rows. The revised board was checked at all seven desktop/preview sizes, through the phone host, and by buying all eight job types with real input. The balanced full student path was rerun and still reproduces the expected counts.

## Frames looked at

Reference frames for Snowy Mail Route and Beat Lab; all early, full-size, student, phone, targeted, keyboard, voice and final-check frames. Audit frames were inspected in five contact sheets, with problem states also opened at full size. All 42 audit PNGs appear in audit-sheets/index.json; 43 additional frames appear in final-evidence/index.json. The final eight-row board and phone week were also inspected at full size.

Evidence folders: `early/`, `early-fixed/`, `model/`, `student/`, `full/`, `targeted/`, `phone/`, `voice-frames/`, `final-voice/`, `final-check/`, `audit/`, `audit-sheets/`, and `audit-followup/`. Grayscale, long/short script, zero reach, completed week, reset modal and Motion off are included. No dragging mechanic exists.

## Art made

Ten original generated paintings, all marked people false. Eight shots at 1280×720, studio at 1600×900 and corkboard at 1600×1200. All appear in the tool; clock hands and sign-up writing are code. Prompts and raw originals retained. No subjects needed redrawing.

Final art: 1,378,672 bytes (1,378.7 KB). Recorded voice: 0 KB. Final bundle: 1,949,563 bytes (1,949.6 KB), below the 2,000 KB goal. Ten WebP images are embedded. No remote resource links are present.

All were inspected, including `art-contact/art-contact.png` and the large-screen scene. The initial 700 KB art estimate grew to support full-size pictures while retaining the 2 MB bundle goal. Quality is 72; no teaching image was dropped.

## Art still to paint

None. No people assets were needed. Spanish audio is an audio/review gap, not missing art.

## Engine changes wanted

None required. Approved Spanish clips should be supplied before release; no shared kit or family source was changed.

## Left open

- Spanish speaker approval and the required fixed Spanish recording remain incomplete. English/fixed speech uses browser fallback. This is built beta, not release approval.
- Phone controls and hints need vertical scrolling. This follows the spec's canvas-then-controls phone flow but does not meet STANDARDS' literal all-controls-without-scroll wording.
- The audit snapshot predates the listed targeted fixes; no second full audit was run, per the one-audit rule.
- One scope failure: the reference bundle command regenerated ignored `tools/snowy-mail-route/snowy-mail-route.html`. No reference source was changed. No commits or git commands were run.
- The first read-only instruction/memory commands used the tool wait setting rather than an enforced process deadline. All subsequent build and check commands used bounded `run.py` deadlines.
- Classroom pacing, recorded-voice quality and the Spanish language review remain for cold review/owner evaluation.

All owned Chrome and host processes are closed; assigned ports 8795 and 9990-9997 were checked closed. Temporary tools/morning-show-crew/host.html was removed. No commits, branch operations, uploads or polish round.
