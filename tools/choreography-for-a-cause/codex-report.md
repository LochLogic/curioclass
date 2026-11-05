# Codex report: choreography-for-a-cause

## Built
Offline grades 9-12 choreography studio with three research folders, 15 source-to-movement proposals, editable eight-count motifs, four composition forms, devices, modeled audience readings, real viewer cards and eight saved versions. Uses kit:curio and kit:dance. Seven original paintings form the evidence and rehearsal space. Final bundle: 1,377,374 bytes, below 2 MB.

Build only. No commits, branch operations, shared-engine edits, recordings or polish round. All writes stayed in this tool and its Scratch folder. Commands used explicit time limits. Chrome ports 9980/9981 and host 8785 were used and closed; host.html was removed.

## Numbers check
Scratch/check_numbers.py recomputed the examples and contrasts. Presence: A=96, B=16. Hidden and Glow size=2; Searching=.5. The example yields 0 of 4, then 4 of 4 after replacing both A slots with Glow. Contrast ratios: brand/paper 7.104, white/brand 7.828, ink/paper 15.438, muted/paper 6.422.

96 counts at 100 bpm take 57.6 seconds. Adding four count-in clicks makes exactly 60 seconds, not under 60 including the introduction. The UI, notes and handoff state this clarification. River arithmetic: 7.5+7.5=15 million acre-feet/year. One in three is 33.33%, an approximate movement analogy for the historical 31% food figure, not a restatement of it. Weight and dollars use separate labeled units rather than misleading equal bars. About 40 million is represented by 40 dots. Historical values and invented voices are labeled.

## Feel check
Best moment: a real held-input session earned 0 of 4, revised the returning motif and earned 4 of 4 with two versions saved. The teacher still noticed weak contrast, making recognition a reason to examine the composition rather than a final artistic score. The result feels earned and specific to the student's arrangement.

Flat moment 1: generic A/B alternation initially made different stimuli feel too similar. Added source-specific pauses, sequential floor drops, accumulation, four-step sinking, converge/diverge pathways and continuous phrase transitions. Flat moment 2: selecting saved motifs required scrolling past parameters. Moved both complete libraries above the secondary editor, preserving selection and button identity.

Looked at Beat Lab and Snowy Mail Route reference frames. Scratch/bar-comparison.png puts the completed six-motif studio beside Beat Lab. The painted light, floor reflections and large moving ensemble give this tool a rich scene with a distinct quiet editorial character. The temporary articulated figures still lack the owner's intended painted finish; their replacement is explicitly pending. The play has a useful revision loop; real audience interpretation adds a reason to return beyond optimizing the model.

## Done when
1. PASS: folder, stage, strip plus stage, and cards around the stage dominate their respective workspaces at 1366x768 and 680x425. Full and targeted frames inspected. Compact text and secondary controls scroll as noted below.
2. PASS: all 15 authored proposals sampled and visually checked at counts 1, 4 and 8. Final regression sampled 7,200 performer/device/count combinations without invalid positions. Source pauses checked explicitly. Motion off retains the same clock and count-step poses.
3. PASS: both exact Sources outcomes and teacher/stranger rule boundaries checked in functional.js; full student revision produced 0 then 4. Model reads source words, not edited prose. Notes and on-screen language identify it as a model.
4. PASS: transport replacement, immediate slot jump and synchronous Stop checked against active handles and clock state. One shared clock and music instance; full real-time play reached the viewer results. Audit resize stress found no exceptions or stuck controls.
5. PASS: duplicate Theme devices flag and Fix assigns unused devices until unique. Actual flag frame and functional assertions checked.
6. PASS: complete version snapshot, modeled results and a real viewer card survived reload; reload-results.json and reload-saved frame inspected.
7. PASS: five held motif taps at two-second pace, plus five noneNamed and five allNamed completions, logged. How is selected by V.heard. Endpoint events start each completion; starting the next run intentionally cuts prior speech. Last event finishes. Folder first-tap welcome separately checked for all three folders after repair.
8. PASS: all seven finished WebPs inspected at final resolution and loaded in the tool. No people or lettering. Every evidence card names its source or identifies an invented/painted stimulus.

## Wave lessons
- PASS, Hint and voice: hints update synchronously on workspace switch; Read speaks the current hint; how selection uses V.heard; held-tap and endpoint logs checked. First input starts movement without waiting for speech.
- PASS, Focus and layout: no load autofocus. Source and motif buttons update in place; keyboard focus survives selection. Limit actions transfer focus when their control disables. Stable hint height. Dialog inputs have explicit names.
- PASS, Sizes: every required size, every mode, 375-wide iframe, grayscale, calm and keyboard frames checked. Audit found no small targets or clipped hints outside intentional modal coverage. Phone horizontal overflow=0.
- PASS, No giveaways: this is an expressive authoring task with explicitly disclosed deterministic readings, not a hidden-answer quiz. No unseen assessment answer is exposed by ids, badge position or meters.
- PASS, Honest numbers: model identity on screen; duration includes a separately stated count-in. Historical dates, units and invented voices labeled. Model recognition is not artistic quality.
- PASS, Standards: solo students generate from stimuli, compose form/devices, explain personal meaning, revise and preserve successive versions. Uses the dance family engine as specified; teaching actions are mapped in notes.
- PASS, Motion off: no infinite CSS animation remains; live dot stops. Dance timing continues with pose changes on counts. Audit calm and final calm-playing frame inspected.
- FAIL, Every short choice visible: saved motif choices and five source buttons now stay visible, including six saved motifs at 680 and phone width. Secondary parameter controls, Delete and compact Clear all still require scrolling. This strict simultaneous-control requirement is not fully met.
- PASS, Resize mid-animation: audit resize stress after state inputs and walk clicks reports no exceptions or disabled locks. Stage reprojects without discarding the running transport.
- PASS, Welcome after first tap: no welcomeAfter. All three folder first taps now speak welcomeFile immediately; choose speaks the relevant motif instruction. Three held-tap logs checked after repair.
- PASS, Unknown as unknown: viewer cards say they are watching until their dependency finishes; modeled readings reveal in phases, not before replay.
- PASS, One look, one meaning: D/V/P source badges and circle/triangle/square performer identities have consistent roles. Color never carries identity alone.
- PASS, Badge truth: version count, motif limit, selected slots, unsaved state and modeled recognition reflect their actual stored state. Functional limits and reload checked.
- PASS, Hint changes back: workspace hints recalculate on return; editing invalidates results and restores the editing instruction. Stop and disabled-limit actions give current next steps.
- PASS, No answer by copying: students choose movement, form and emphasis; model feedback comes after replay. The visible stimulus-to-motion proposals are teaching material, not a diagnosis puzzle answer key.

## Audit leads
One full audit completed, 16 leads. Scratch/audit/audit.md is retained. No second full audit was run. The audit used the prior bundle; fixes below were rebundled and checked with targeted shots only.

1. Motif-created scroll at 680: library moved out; all six options visible. Secondary parameters remain scrollable, acknowledged.
2. Motif-created scroll at 800/375: same repair; phone six-option frame checked. Secondary controls remain.
3. Motif-created scroll at 1000/1280: library moved out. Name, meaning and Delete can still scroll at restricted heights.
4. Motif-created scroll at 1366: library moved out and inspected; long meaning/Delete can still scroll with six motifs.
5. Motif-created scroll at 760: library moved out. Secondary editor remains a scroll region.
6. Structure-filled scroll at 680: entire library pinned, controls below it scroll; target-sized Repeat/Dancers and Empty remain reachable. Not claiming all parameters visible.
7. Structure-filled scroll at 800/375: same disposition. Compact phone frame inspected.
8. Viewer Clear all at 680/375: retained in the secondary version panel. Destructive housekeeping is below the main reading activity; accessible by scroll and keyboard.
9. Real viewer about field unnamed: fixed with explicit aria-label, targeted DOM check.
10. Real viewer remember field unnamed: fixed with explicit aria-label, targeted DOM check.
11. Real viewer dialog covers hint: intentional modal backdrop; the dialog has its own instruction and focus. Frame inspected at 680 and other audit sizes.
12. Real viewer state's Clear all scroll: same secondary-panel disposition as lead 8.
13. Change issue dialog covers hint: intentional modal backdrop with its own clear consequences, Cancel and Continue. All audit frames inspected.
14. Light pollution first-tap welcome missing: fixed; held first click logs welcomeFile spoken.
15. Food waste first-tap welcome missing: fixed; held first click logs welcomeFile spoken.
16. Colorado River first-tap welcome missing: fixed; held first click logs welcomeFile spoken.

Audit size, target, Motion off, resize, settled Enter, five-tap and quick-tap sections otherwise clean. Targeted checks had zero console errors. Two post-audit harness attempts failed due to an unsupported steps field and selector quoting; corrected to real held clicks and rerun successfully. These were harness errors, not silent passes.

## Frames looked at
Scratch paths below are relative to _scratch/choreography-for-a-cause/. Every saved PNG was inspected directly or on contact sheets. No extra full-size sweep after the single 28-frame mode/size pass.
- bar-frames: both finish references.
- first-frames: five initial frames, used to correct startup and source layout.
- functional-frames: model/transport run and reload-saved.
- full-frames: all 28 frames, four modes across seven required direct sizes.
- phone-frames: four actual iframe modes, latest six-motif libraries and final unobscured Structure stage checked.
- extra-frames: ten frames for grayscale, calm, keyboard, dialog, 96-count extreme, duplicate devices and real drag placement.
- targeted-frames: seven source, compact viewer, movement and allNamed frames after initial repairs.
- feel-frames: first dance, first readings, revision outcome.
- audit: all 44 PNGs across eleven contact sheets.
- last-frames: all eight final movement/layout/keyboard frames, including both six-motif libraries at 680 and 1366.
- pose-frames: all three 15-source pose grids, counts 1/4/8.
- post-audit-frames: three folder welcomes and named dialog.
- bar-comparison.png: completed scene beside Beat Lab.

## Art made
Seven image-tool paintings, all used: cc-glow, cc-stars, cc-bin, cc-fridge, cc-ring, cc-river, cc-studio. Total finished art 874.2 KiB; bundle 1345.1 KiB. Consistent painted editorial house style, no people or lettering. All raw originals retained. Processed only with art.py --rekey, inspected all finished WebPs. No redraws needed. Required generation credit added.

## Art still to paint
Owner requires painted dancers in the final tool. All 21 used pose entries in art/prompts.json have people:true, with three consistent badge identities, levels, mirrored variants and transition requirements. No people were generated. The kit figure is temporary and isolated behind createPerformer/paintPerformer for replacement without changing choreography timing. Final performer art quality remains unapproved.

## Engine changes wanted
Detailed in handoff.md: dance.floor.draw should support the stage backdrop; Dance.level needs native low variants for floor shapes; Dance.music needs instrument-specific gain and sustained pad duration. Local workarounds preserve shared files.

## Left open
- Strict simultaneous visibility of every secondary authoring control on compact screens is not achieved. Evidence text, long viewer readings and version history also scroll. Six saved motif choices and source buttons stay visible.
- Human headphone review of music balance, synthesized timbres and browser narration pacing remains. Muted Chrome verified timing and voice logs, not sound quality. No recordings were permitted.
- The open voice question leans toward a grown-up voice. Adding one to the shared bank is outside the allowed write scope; handoff records that decision. Current manifest is lively-host / Sadachbia, browser speech fallback.
- 96 dance counts plus count-in equal 60 seconds; spec wording qualified in notes and handoff.
- Painted dancer replacements and cold review remain. No second full audit after the final source/layout/accessibility corrections.
