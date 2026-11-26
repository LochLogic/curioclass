# Speech Coach: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: speech-coach
#### Built

Speech Coach is built as one offline HTML file using the kit starter, Curio.voice and theme-912.
Build, Rehearse and Review include the editable sample and My talk, all three tasks, six slide kinds, thread/listener test, opposing-view check, live timing, listener pad, optional loudness analysis, self-checks and an eight-run notebook.
Added the painted auditorium during implementation. Retained the three supplied museum artworks.
No commits, branch changes, deployment or polish round. This report is written last to honor the user's stop-on-report instruction.

#### Numbers check

PASS: independent Python recomputation in _scratch/speech-coach/recompute_numbers.py and numbers.json.
Scripts: 45, 35, 51, 52, 70, 42 words, totaling 295.
Planned sections: 20, 15, 20, 20, 30, 15 seconds, totaling 120.
Slide 5: 47 tokens, 46 shared with its script, 98 percent after rounding. Internal colons and hyphens are retained; trailing punctuation is removed.
Scripted elapsed boundaries 25, 40, 57, 80, 110, 125 give 108, 140, 180, 136, 140, 168 words per minute and 2:05 total.
The real browser run matches those six paces. Its pause clock drift was zero in the half-second pause test.
The chart's 72.7 plus 27.3 equals 100. The CDC source confirms the 2015 figure.
Contrast recomputation matches the spec: brand/panel 10.24:1, brand/section 9.70:1, brand/stage 11.11:1, dark/brand 10.92:1, script/stage 15.96:1, slow/panel 12.00:1, fast/panel 7.63:1.
Used the allowed AAP paraphrase and the allowed unattributed 150 words/minute rule-of-thumb wording.

#### Feel check

Played the sample through a complete 125-second live clock run, including Next, Pause and listener marks, then inspected its marked sheet and subsequent trial records.
Best moment: the auditorium gives way to the student's own timed evidence, including the fast first Reason and a Lost me mark on the second Reason.
Flat moment 1: the first layout crowded the cue card with transport controls. Fixed separate grid rows, readable signposts, and a compact listener row.
Flat moment 2: phone controls and the hint were buried below the form. Fixed a persistent hint and Task drawer, keeping the rehearsal clock, preview and Start/Next visible.
Also enlarged the initial slide preview, kept all six collapsed cards visible on laptops, and corrected clipped compact Busy text.
The professional stage has comparable finish to the reference instrument without copying its orange palette or synthesizer layout.
[Speech Coach beside Beat Lab](S:/CurioClass-codex/_scratch/speech-coach/feel-comparison.png).
The test used a synthetic microphone signal, not a human speech recording. A full 25-minute classroom session was not performed.

#### Done when

- PASS: six-section sample, 295 words, 2:00 plan; Club pitch shows over by 1:00 and blocks Claim/Close deletion. functional-evidence.json.
- PASS: Slide 5 Busy 47 and Reading 98; deleting the chart source produces No source. first-frames, last-frames and functional evidence.
- PASS: expected six paces and 2:05, over by five seconds. Independent Python, accelerated clock test and actual 125-second browser run.
- PASS: F marks land in Opening and Reason 1, L in Reason 2, N in Close, with section-relative and total timestamps. Two fillers over 125 seconds display 1.0 per minute.
- PASS with test limitation: a controlled three-second quiet interval gives one long pause through the real AnalyserNode path; the synthetic stream track ends at completion. A physical microphone and native permission prompt remain untested.
- PASS: no spoken line during the live run; Start hushes the welcome and queue. Read and Sound cannot interrupt a run. functional-evidence.json and voice logs.
- PASS: laptop cue/Next dominate the auditorium; Build pairs the selected editor with its slide; Review presents the marked sheet. Viewed required frames.
- PASS: Next, Pause and pad stamps use the tap time. Pause clock drift was zero; Space also advances from a focused Pause button. focus-finish.json.
- PASS: Thread contains only signposts and links; the Listener test compares with Claim; deleting Other side shows the check. Functional checks.
- PASS: eight-run cap survives reload, Clear asks first, No preserves data, and Reset sample restores the original six cards. Functional checks.
- PASS: Next, clocks and preview fit 680x425 and 1366x768. All tested page widths have zero horizontal overflow; the final phone Review also has zero sideways overflow. Geometry JSON and phone-review-contained.json.

#### Wave lessons

- PASS, Hint and voice: hints update synchronously. Count, live and paused states name enabled controls. Read uses the current hint; active runs are silent. Five held taps at two-second intervals speak Busy once.
- PASS, Focus and layout: section buttons update in place. Start retains focus through aria-disabled countdown; Pause focuses Resume; Finish focuses Review. No focus on load. Explicit field names added.
- PASS, Sizes: required eight sizes inspected, including the 375 iframe. Targets are at least 44 px; compact listener targets are 56 px. Clock captions are now 10 px and the hint cannot shrink below its text.
- PASS, No giveaways: this is an open rehearsal lab, without hidden-answer badges or scores.
- PASS, Honest numbers: pace explicitly uses script words; pauses can be unmeasured; heuristic thresholds and manual planned times are identified.
- PASS, Standards: solo students build signposts and opposing views, perform the listener test, choose media jobs, rehearse, and revise from evidence.
- PASS, Motion off: the glow stops; countdown duration and rehearsal timing remain unchanged. Audit found no infinite animation.
- PASS with layout tradeoff, Short choices: all three task choices remain visible. Long writing forms, slide fields and utility actions scroll vertically; these are not answer-choice lists.
- PASS, Resize mid-action: no runtime errors. The audit's changing timed-run label was a false disabled-control comparison; direct disabled-property checks pass.
- PASS, Welcome timing: no welcomeAfter. An action's own teaching line skips the generic welcome; empty Review has no invalid fastest-section welcome.
- PASS, Unknown states: no run and unmeasured pauses are shown as such; no speech recognition or inferred spoken fillers.
- PASS, One look/meaning: F/L/H/N have a stable legend; pace bands use both glyphs and words.
- PASS, True badges: task-limit readings use the selected task; measured versus unmeasured state stays explicit.
- PASS, Hint reversibility: mode changes, reset and rehearsal phase changes restore their own next-action hint.
- PASS, No word-copy answers: the listener writes a point before comparing with Claim; the tool does not grade a copied answer as a win.

#### Audit leads

The full audit ran once on Chrome 9991 with host 8795 and finished within its 40-minute limit.
It reported 69 leads. All 64 bullet groups and five welcome leads are answered in _scratch/speech-coach/audit-leads.md.
Nineteen bullet groups were fixed: explicit names, small clock captions, focus retention, compact Thread buttons, and containment of the phone notebook.
Thirty-four groups concern intentionally scrollable writing forms or utility actions. Retained this tradeoff for cold review; task choices and frequent rehearsal controls remain available.
Nine groups concern modal coverage of inactive background content. This is expected.
Corrected one phone keep-region recipe to match the one-card layout. One resize lead compared a changing elapsed-time label rather than a disabled property.
The five welcome leads are expected own-action teaching lines or empty Review, as required by STANDARDS.
Control walks and resize checks had no runtime errors. All ten five-tap and ten quick-tap narration checks were clean.
Concrete fixes were rechecked with targeted shots and assertions; the full audit was not repeated.

#### Frames looked at

All frames were inspected, directly or in the 19 labeled vertical audit sheets.
Scratch groups: bar-frames (2), first-frames (5), fix-frames (5), final-frames (35), last-frames (10), audit (38), post-audit-frames (8), finish-frames (4).
Also inspected live-stage.png, real-run-review.png, keyboard-run.png and feel-comparison.png.
Coverage includes every required size and mode, all slide kinds, five chart bars, missing source, Busy/Reading readings, dialogs, empty talk, storage failure, reduced motion, grayscale, keyboard and microphone lifecycle.
The first iframe host produced a favicon 404. The host wrapper was corrected; subsequent targeted and final host runs had no console errors.
qa-manifest.json and build-evidence.json preserve the final evidence map and bundle fingerprint.

#### Art made

One new image: sc-empty-house, generated with the built-in OpenAI image tool. No people, lettering or logos. No redraw needed.
Three supplied public-domain museum images retained and inspected in their actual slides.
New WebP: 107210 bytes. Total four WebPs: 422610 bytes, about 413 KiB.
Final bundle: 672217 bytes, about 657 KiB, below 2000000 bytes.
Prompts, provenance, final image and raw original are in art/. preview.svg is drawn in code as specified.

#### Art still to paint

None. The two existing museum paintings depict people and are retained following the spec's leaning. No people were generated.

#### Engine changes wanted

No kit engine changes.
Optional shared audit improvements are recorded in handoff.md: MODES_JS should discover the second header bar; ENABLED_JS/shake should compare stable control identifiers before changing timer labels.
No shared script was edited.

#### Left open

- Physical microphone hardware and the native permission prompt need an interactive check. Synthetic analyser, late-permission cleanup, completion and page-hide release passed.
- Browser fallback narration is used. Umbriel / easy-coach and all ten lines are specified; no voice audio was recorded.
- Compact writing forms and utility actions require vertical panel scrolling. The Run notebook uses its own horizontal data-table scroller on phones.
- The official California bill endpoint denied automated access. CDE confirms the high-school threshold and rural exemption; the historical implementation date remains sourced to the supplied spec.
- FAIL, process scope: required reference bundle commands regenerated ignored HTML under tools/snowy-mail-route and tools/beat-lab, outside the two allowed write folders. Their source files were not edited; no further writes were made there.
- FAIL, initial command deadlines: the first guide and memory reads lacked explicit shell deadlines. Subsequent command invocations were bounded.
- All owned Chrome and host processes are closed. host.html is absent. No commits or polish round were started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: speech-coach

#### Played

Cold Grade 12 solo play before opening the builder's report, handoff, notes or source: all sample cards, Thread/Listener test, a complete rehearsal, listener marks and Review. Then checked the teacher projection view, own-talk entry, tasks, slide kinds and extremes. The room, cue and immediate Next response are strong; the original table-first finish felt flat.

#### Findings fixed

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

#### Findings left

- No known implementation blocker or should-fix remains after the scoped rechecks. Spec-owned limitations remain under Left open.
- Polish, general: long writing forms, detailed slide data, utility buttons and the run notebook scroll; these are authoring/data surfaces, not hidden answer choices.

#### Flattest moment left

Writing a full original talk remains quiet work. The new Review prompt makes the next revision concrete; no game reward or new topic was added to this Grade 12 rehearsal tool.

#### Graphics

All four images inspected at displayed size. Retained the three supplied museum works and their people tags; the historic art deliberately differs from the editorial auditorium, as the spec requires. One auditorium redrawn using the built-in imagegen tool; prompt and final asset are in art/prompts.json and art/sc-empty-house.webp. No new people, missing art tokens or downloaded media. Art: 434 KiB; final bundle: 708273 bytes on disk, about 692 KiB. Compared beside Beat Lab in _scratch/speech-coach/review-finish-comparison.png; retained the rich finish. Both reference bundles were opened read-only.

#### Audit

One final audit completed within its 40-minute limit, Chrome 9931, host 8735: 57 leads. Every lead is answered in _scratch/speech-coach/review-audit-responses.md. Fixed five navigation/focus groups and addressed three slide-choice groups; retained 32 authoring/utility and two table-scroll groups, confirmed eight expected modal-cover groups, disproved two changing-timer-label comparisons, and explained five correct first-tap welcome substitutions. Ten five-tap and ten quick-tap checks were clean. Explicit states cover all modes.
The final scoped recheck passed real held navigation, Add/Clear/Reset focus, both navigation limits, exact Reading thresholds and Thread hints. A real resize after every Next left the run selector enabled with no exceptions. The full audit was not rerun after these narrow repairs. Inspected all 43 audit PNGs on 11 labeled sheets, alongside the direct full-size review frames.
Independent checks: 295 words; planned 120 seconds; Slide 5 has 47 words/98 percent; scripted boundaries give 108/140/180/136/140/168 words per minute, total 125 seconds. All required sizes viewed, with no horizontal page overflow. Keyboard-only Start/F/P/Space/finish passes. Synthetic microphone path counts one long pause and ends all tracks. Nine actual completions retain eight runs across reload. Motion off keeps the three-second count; grayscale remains legible.

| Line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| busy, five held taps at 2 seconds | how | 1 | 1 |
| runsaved, five completed runs | event | 5 | 5 |
| over, five completed over-limit runs | event | 5 | 5 |

Start cuts the welcome and empties the voice queue. Read works with Sound off and releases promptly on mode change. First plain tap and Sound re-enable bring one welcome. All 18 catalogued strings exactly match voice/lines.json. Fullscreen, phone-host, source and voice evidence live in _scratch/speech-coach/review-*.

#### Left open

- Browser narration remains fallback; no audio was recorded. Physical microphone hardware/native permission UI were not exercised; synthetic stream, calibration, pause counting and lifecycle were checked. The specified first-two-seconds calibration can include the speaker's voice, so quiet counts remain estimates, not recognized spoken pauses.
- Spec tension: the sample answers the objection inside its Other side script but its role/link heuristic still asks for a separate structural answer. Kept the specified sample and test, disclosed the heuristic on screen and in notes.
- Spec wording says choosing a different slide job may fix competition, but changing a job alone cannot reduce Busy/Reading token counts. Kept the mandated voice line and thresholds; wording change belongs to the spec.
- The AIC object page blocked direct access; its supplied clock metadata remains unchanged. Other museum, CDC, AAP and California primary-source checks and access limits are recorded in review-sources.md.
- Process exceptions: the opening read and one final utility check lacked explicit hard shell deadlines; the other commands were bounded. No commits or writes to other tool folders. Owned Chrome processes are closed, ports 9930/9931/8735 are closed, and host.html is absent.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Speech Coach handoff

#### Cold review changes

The cold review played the sample before reading this handoff. Section actions now remain in a fixed dock while the writing fields scroll. Planned seconds normalize to whole numbers at commit. The Other side reminder explicitly describes its structural heuristic, which cannot read the sample's embedded spoken answer.

Review now opens with measured evidence and one editable next-trial note, synchronized with the notebook. The Revise section shortcut uses the displayed run's section index in the current talk, clamped if the talk was shortened; older runs retain their original numeric measurements. Compare strips use the same seconds scale. Listener marks are vertically separated with explicit time labels. The school auditorium was repainted with the built-in OpenAI image tool, retaining the cinematic materials and lighting. Museum captions now sit on opaque dark caption bands. Hiding the page during countdown cancels the pending start and releases the microphone.

Review evidence, source checks, screenshots and the one final audit live under _scratch/speech-coach/review-*. The audit completed with 57 leads, answered in review-audit-responses.md. Scoped checks passed after the repairs; no second full audit was run. The current bundle is 708273 bytes on disk. Browser narration remains fallback; no audio was recorded.

Audit repairs keep the relocated compact section navigation visible, scroll only the inner writing fields when focusing Role after Add/Move, and place Kind/Slide's job before the preview in short landscape boxes. Reading now tests the exact overlap fraction; whole-percent rounding no longer suppresses warnings just above 60 percent. The final audit uses the preceding bundle snapshot; only these affected controls and threshold cases are re-shot afterward, with no second full audit.

Clear/Reset use the same visible-focus helper. Section navigation transfers focus to its enabled neighbor at either limit. Thread hints now name Compare with Claim after typing and Back to desk after comparing. The voice catalog has 18 fixed narration/hint strings, matching allLines exactly; only the original ten narration triggers speak automatically, and a rehearsal remains silent.

Built and cold-reviewed in one review pass. No commits, branch changes or deployment. The original Build record remains below.

#### Source map

src.html starts from the kit starter and uses kit:curio and kit:theme-912. It contains responsive styles, stable editor controls, an inline original sample, word/token rules, local persistence, slide rendering, a monotonic rehearsal clock, numeric microphone measurements, review rendering and input handlers. __tool exposes calculations, state and test hooks. The anchor setter permits accelerated timing checks; ordinary use always reads performance.now().

The museum images and public-domain.json were supplied. sc-empty-house is the new OpenAI-generated painting. art/prompts.json records the complete prompt and provenance. Raw new artwork stays in art/raw. The tool makes no requests at runtime.

At portrait widths up to 760, responsivePanel moves the hint above the work and the same task panel into a modal drawer. It moves them back on landscape resize without recreating controls or touching the rehearsal state. The Rehearse stage keeps its clock, slide and transport visible. Build scrolls its editor internally and shows Previous / Next section.

#### Tricky parts

Word counts in scripts split on spaces. Slide readings strip punctuation except internal colons and hyphens, normalize case, and count repeated tokens separately. Trimming a trailing colon is necessary for the sample's 46 of 47 matching tokens. Planned times auto-update until explicitly edited. User times keep whole seconds with a five-second minimum.

The rehearsal clock samples the tap time, not the next 100 ms display update. Pause accumulates elapsed time before changing state. The visual countdown lasts three seconds with Motion off too. Start hushes Curio.voice and disables Read and Sound during the run. The run freezes the plan so measurements cannot drift under edits. Stored runs exclude those temporary copies of scripts and slides and keep only numeric observations, section roles, self-checks and notes.

The optional microphone obtains a stream only after the checkbox is chosen. An epoch guards late permission resolution after leaving the mode. RMS analysis keeps only the current frame and numeric results. Calibration uses the first two seconds of the live run. A continuous quiet stretch is counted once, even across a section boundary. Stop releases every track and closes the audio context on completion, abandonment, mode change, visibility loss and page hide. A hidden page also pauses an active run.

Sample and My talk each have their own eight-run notebook and task. Clear My talk does not clear the sample. Reset sample restores its six sections and clears the sample's runs. A full reload restores both notebooks.

Notes only keeps the signpost as the speaker's cue; Nothing hides both signpost and script. Both display the script-based pace assumption. The link picker includes "and" because the supplied sample explicitly uses it, although the initial list of link chips omits it. Space advances from focused rehearsal buttons as well as the stage; Enter activates the focused button.

#### Open questions resolved

- Keep the two supplied museum paintings that depict people. The spec explicitly leans toward retaining these existing public-domain works. No people were generated.
- Use the allowed AAP paraphrase and label it as a paraphrase. Do not present unverified wording as a quotation.
- Use the allowed common-rule-of-thumb wording for 150 words per minute without attributing it to NCVS, whose current site did not plainly state the figure.
- There is no speech-to-text. Fillers are listener taps or a separate self-estimate. The microphone measures loudness only.

#### Engine changes wanted

scripts/audit_tool.py, MODES_JS: include `.bar .seg[aria-label="Mode"] button` in mode discovery. This tool uses a second header bar for modes. Explicit audit states cover Rehearse and Review without changing the shared script. No kit changes requested.

scripts/audit_tool.py, ENABLED_JS and shake: compare enabled controls by a stable id or data-review index before falling back to visible text. A timed run's changing 0:02 / 0:03 label produced a false disabled-control lead. The final targeted check inspects the button's disabled property directly and passes.

#### Evidence and review next

Build arithmetic is in _scratch/speech-coach/recompute_numbers.py and numbers.json. Independent cold-review arithmetic is in review_prepare.py and review-numbers.json. Functional, visual, keyboard, synthetic microphone and audit evidence is kept in that same Scratch directory. The separately requested cold review is complete; see codex-review.md for its findings and limitations.

The real browser microphone permission prompt and a physical microphone are outside the automated synthetic-stream test. A cold reviewer can test them interactively. Browser fallback narration is used; voice/lines.json specifies Umbriel / easy-coach for later recording. No audio was recorded in Build.

The official California bill endpoint denied automated access. CDE confirms the 8:30 high-school threshold and rural exemption; the historical implementation date remains sourced to the supplied spec. The AAP article search result supports the biology; its direct legacy URL redirected to authentication. The slide uses the permitted paraphrase.

The first live test scheduled pointer-down at each target, so its held clicks landed 120 ms late. The corrected schedule targets release and returns all six expected paces. The first keyboard harness omitted Chrome's virtual key codes for Enter. keyboard.py supplies them and completes the run using Tab, Enter, F, P and Space. Earlier failed harness output is preserved rather than overwritten as a success.

#### Final build checks

The full audit ran once and reported 69 leads. _scratch/speech-coach/audit-leads.md answers its 64 bullet groups and five welcome leads. Concrete fixes were checked in post-audit-frames and finish-frames, without rerunning the full audit. The retained tradeoff is vertical scrolling for long writing forms and utility actions; all three task choices and the frequent rehearsal controls remain available. The phone notebook has its own table scroller and does not make Review or the page scroll sideways.

The final bundle is 672217 bytes. build-evidence.json records its SHA-256 and static checks. Browser and host processes started for this build were closed, and host.html was removed. The final report is written only after validation, honoring the user's stop-on-report instruction.

#### Scope exception

The required reference comparison commands regenerated the ignored HTML bundles under tools/snowy-mail-route and tools/beat-lab. That crossed the user's two-folder write boundary. Their source files were not edited, and no further writes were made there. The first guide and memory read commands also lacked a shell deadline; subsequent command invocations were bounded. These are recorded as process failures rather than described as full compliance.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
