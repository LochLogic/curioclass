# Codex report: speech-coach
## Built

Speech Coach is built as one offline HTML file using the kit starter, Curio.voice and theme-912.
Build, Rehearse and Review include the editable sample and My talk, all three tasks, six slide kinds, thread/listener test, opposing-view check, live timing, listener pad, optional loudness analysis, self-checks and an eight-run notebook.
Added the painted auditorium during implementation. Retained the three supplied museum artworks.
No commits, branch changes, deployment or polish round. This report is written last to honor the user's stop-on-report instruction.

## Numbers check

PASS: independent Python recomputation in _scratch/speech-coach/recompute_numbers.py and numbers.json.
Scripts: 45, 35, 51, 52, 70, 42 words, totaling 295.
Planned sections: 20, 15, 20, 20, 30, 15 seconds, totaling 120.
Slide 5: 47 tokens, 46 shared with its script, 98 percent after rounding. Internal colons and hyphens are retained; trailing punctuation is removed.
Scripted elapsed boundaries 25, 40, 57, 80, 110, 125 give 108, 140, 180, 136, 140, 168 words per minute and 2:05 total.
The real browser run matches those six paces. Its pause clock drift was zero in the half-second pause test.
The chart's 72.7 plus 27.3 equals 100. The CDC source confirms the 2015 figure.
Contrast recomputation matches the spec: brand/panel 10.24:1, brand/section 9.70:1, brand/stage 11.11:1, dark/brand 10.92:1, script/stage 15.96:1, slow/panel 12.00:1, fast/panel 7.63:1.
Used the allowed AAP paraphrase and the allowed unattributed 150 words/minute rule-of-thumb wording.

## Feel check

Played the sample through a complete 125-second live clock run, including Next, Pause and listener marks, then inspected its marked sheet and subsequent trial records.
Best moment: the auditorium gives way to the student's own timed evidence, including the fast first Reason and a Lost me mark on the second Reason.
Flat moment 1: the first layout crowded the cue card with transport controls. Fixed separate grid rows, readable signposts, and a compact listener row.
Flat moment 2: phone controls and the hint were buried below the form. Fixed a persistent hint and Task drawer, keeping the rehearsal clock, preview and Start/Next visible.
Also enlarged the initial slide preview, kept all six collapsed cards visible on laptops, and corrected clipped compact Busy text.
The professional stage has comparable finish to the reference instrument without copying its orange palette or synthesizer layout.
[Speech Coach beside Beat Lab](S:/CurioClass-codex/_scratch/speech-coach/feel-comparison.png).
The test used a synthetic microphone signal, not a human speech recording. A full 25-minute classroom session was not performed.

## Done when

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

## Wave lessons

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

## Audit leads

The full audit ran once on Chrome 9991 with host 8795 and finished within its 40-minute limit.
It reported 69 leads. All 64 bullet groups and five welcome leads are answered in _scratch/speech-coach/audit-leads.md.
Nineteen bullet groups were fixed: explicit names, small clock captions, focus retention, compact Thread buttons, and containment of the phone notebook.
Thirty-four groups concern intentionally scrollable writing forms or utility actions. Retained this tradeoff for cold review; task choices and frequent rehearsal controls remain available.
Nine groups concern modal coverage of inactive background content. This is expected.
Corrected one phone keep-region recipe to match the one-card layout. One resize lead compared a changing elapsed-time label rather than a disabled property.
The five welcome leads are expected own-action teaching lines or empty Review, as required by STANDARDS.
Control walks and resize checks had no runtime errors. All ten five-tap and ten quick-tap narration checks were clean.
Concrete fixes were rechecked with targeted shots and assertions; the full audit was not repeated.

## Frames looked at

All frames were inspected, directly or in the 19 labeled vertical audit sheets.
Scratch groups: bar-frames (2), first-frames (5), fix-frames (5), final-frames (35), last-frames (10), audit (38), post-audit-frames (8), finish-frames (4).
Also inspected live-stage.png, real-run-review.png, keyboard-run.png and feel-comparison.png.
Coverage includes every required size and mode, all slide kinds, five chart bars, missing source, Busy/Reading readings, dialogs, empty talk, storage failure, reduced motion, grayscale, keyboard and microphone lifecycle.
The first iframe host produced a favicon 404. The host wrapper was corrected; subsequent targeted and final host runs had no console errors.
qa-manifest.json and build-evidence.json preserve the final evidence map and bundle fingerprint.

## Art made

One new image: sc-empty-house, generated with the built-in OpenAI image tool. No people, lettering or logos. No redraw needed.
Three supplied public-domain museum images retained and inspected in their actual slides.
New WebP: 107210 bytes. Total four WebPs: 422610 bytes, about 413 KiB.
Final bundle: 672217 bytes, about 657 KiB, below 2000000 bytes.
Prompts, provenance, final image and raw original are in art/. preview.svg is drawn in code as specified.

## Art still to paint

None. The two existing museum paintings depict people and are retained following the spec's leaning. No people were generated.

## Engine changes wanted

No kit engine changes.
Optional shared audit improvements are recorded in handoff.md: MODES_JS should discover the second header bar; ENABLED_JS/shake should compare stable control identifiers before changing timer labels.
No shared script was edited.

## Left open

- Physical microphone hardware and the native permission prompt need an interactive check. Synthetic analyser, late-permission cleanup, completion and page-hide release passed.
- Browser fallback narration is used. Umbriel / easy-coach and all ten lines are specified; no voice audio was recorded.
- Compact writing forms and utility actions require vertical panel scrolling. The Run notebook uses its own horizontal data-table scroller on phones.
- The official California bill endpoint denied automated access. CDE confirms the high-school threshold and rural exemption; the historical implementation date remains sourced to the supplied spec.
- FAIL, process scope: required reference bundle commands regenerated ignored HTML under tools/snowy-mail-route and tools/beat-lab, outside the two allowed write folders. Their source files were not edited; no further writes were made there.
- FAIL, initial command deadlines: the first guide and memory reads lacked explicit shell deadlines. Subsequent command invocations were bounded.
- All owned Chrome and host processes are closed. host.html is absent. No commits or polish round were started.
