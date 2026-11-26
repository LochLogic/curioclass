# Choreography for a Cause: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: choreography-for-a-cause

#### Built
Offline grades 9-12 choreography studio with three research folders, 15 source-to-movement proposals, editable eight-count motifs, four composition forms, devices, modeled audience readings, real viewer cards and eight saved versions. Uses kit:curio and kit:dance. Seven original paintings form the evidence and rehearsal space. Final bundle: 1,377,374 bytes, below 2 MB.

Build only. No commits, branch operations, shared-engine edits, recordings or polish round. All writes stayed in this tool and its Scratch folder. Commands used explicit time limits. Chrome ports 9980/9981 and host 8785 were used and closed; host.html was removed.

#### Numbers check
Scratch/check_numbers.py recomputed the examples and contrasts. Presence: A=96, B=16. Hidden and Glow size=2; Searching=.5. The example yields 0 of 4, then 4 of 4 after replacing both A slots with Glow. Contrast ratios: brand/paper 7.104, white/brand 7.828, ink/paper 15.438, muted/paper 6.422.

96 counts at 100 bpm take 57.6 seconds. Adding four count-in clicks makes exactly 60 seconds, not under 60 including the introduction. The UI, notes and handoff state this clarification. River arithmetic: 7.5+7.5=15 million acre-feet/year. One in three is 33.33%, an approximate movement analogy for the historical 31% food figure, not a restatement of it. Weight and dollars use separate labeled units rather than misleading equal bars. About 40 million is represented by 40 dots. Historical values and invented voices are labeled.

#### Feel check
Best moment: a real held-input session earned 0 of 4, revised the returning motif and earned 4 of 4 with two versions saved. The teacher still noticed weak contrast, making recognition a reason to examine the composition rather than a final artistic score. The result feels earned and specific to the student's arrangement.

Flat moment 1: generic A/B alternation initially made different stimuli feel too similar. Added source-specific pauses, sequential floor drops, accumulation, four-step sinking, converge/diverge pathways and continuous phrase transitions. Flat moment 2: selecting saved motifs required scrolling past parameters. Moved both complete libraries above the secondary editor, preserving selection and button identity.

Looked at Beat Lab and Snowy Mail Route reference frames. Scratch/bar-comparison.png puts the completed six-motif studio beside Beat Lab. The painted light, floor reflections and large moving ensemble give this tool a rich scene with a distinct quiet editorial character. The temporary articulated figures still lack the owner's intended painted finish; their replacement is explicitly pending. The play has a useful revision loop; real audience interpretation adds a reason to return beyond optimizing the model.

#### Done when
1. PASS: folder, stage, strip plus stage, and cards around the stage dominate their respective workspaces at 1366x768 and 680x425. Full and targeted frames inspected. Compact text and secondary controls scroll as noted below.
2. PASS: all 15 authored proposals sampled and visually checked at counts 1, 4 and 8. Final regression sampled 7,200 performer/device/count combinations without invalid positions. Source pauses checked explicitly. Motion off retains the same clock and count-step poses.
3. PASS: both exact Sources outcomes and teacher/stranger rule boundaries checked in functional.js; full student revision produced 0 then 4. Model reads source words, not edited prose. Notes and on-screen language identify it as a model.
4. PASS: transport replacement, immediate slot jump and synchronous Stop checked against active handles and clock state. One shared clock and music instance; full real-time play reached the viewer results. Audit resize stress found no exceptions or stuck controls.
5. PASS: duplicate Theme devices flag and Fix assigns unused devices until unique. Actual flag frame and functional assertions checked.
6. PASS: complete version snapshot, modeled results and a real viewer card survived reload; reload-results.json and reload-saved frame inspected.
7. PASS: five held motif taps at two-second pace, plus five noneNamed and five allNamed completions, logged. How is selected by V.heard. Endpoint events start each completion; starting the next run intentionally cuts prior speech. Last event finishes. Folder first-tap welcome separately checked for all three folders after repair.
8. PASS: all seven finished WebPs inspected at final resolution and loaded in the tool. No people or lettering. Every evidence card names its source or identifies an invented/painted stimulus.

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
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

#### Art made
Seven image-tool paintings, all used: cc-glow, cc-stars, cc-bin, cc-fridge, cc-ring, cc-river, cc-studio. Total finished art 874.2 KiB; bundle 1345.1 KiB. Consistent painted editorial house style, no people or lettering. All raw originals retained. Processed only with art.py --rekey, inspected all finished WebPs. No redraws needed. Required generation credit added.

#### Art still to paint
Owner requires painted dancers in the final tool. All 21 used pose entries in art/prompts.json have people:true, with three consistent badge identities, levels, mirrored variants and transition requirements. No people were generated. The kit figure is temporary and isolated behind createPerformer/paintPerformer for replacement without changing choreography timing. Final performer art quality remains unapproved.

#### Engine changes wanted
Detailed in handoff.md: dance.floor.draw should support the stage backdrop; Dance.level needs native low variants for floor shapes; Dance.music needs instrument-specific gain and sustained pad duration. Local workarounds preserve shared files.

#### Left open
- Strict simultaneous visibility of every secondary authoring control on compact screens is not achieved. Evidence text, long viewer readings and version history also scroll. Six saved motif choices and source buttons stay visible.
- Human headphone review of music balance, synthesized timbres and browser narration pacing remains. Muted Chrome verified timing and voice logs, not sound quality. No recordings were permitted.
- The open voice question leans toward a grown-up voice. Adding one to the shared bank is outside the allowed write scope; handoff records that decision. Current manifest is lively-host / Sadachbia, browser speech fallback.
- 96 dance counts plus count-in equal 60 seconds; spec wording qualified in notes and handoff.
- Painted dancer replacements and cold review remain. No second full audit after the final source/layout/accessibility corrections.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: choreography-for-a-cause

#### Played

Cold Grade 9-12 student path, through a finished viewer replay, before reading builder claims or source; then projection, extreme-state and adversarial checks. Rich studio, direct placement and synchronized phrases are strong. One pass, with targeted repair checks; no commits or shared-file edits.
Review ran 2026-11-05 to 2026-11-06 in S:\CurioClass-codex. Evidence paths below are relative to `_scratch/choreography-for-a-cause/`.

#### Findings fixed

- **blocker/general, Save version:** saving before Show viewers computed an unseen score. Save only completed readings; unknown is ?, never zero. Schema 2 migration removes unverifiable legacy model results while retaining movement, versions and typed notes. Actual reload checked.
- **blocker/general, form change:** Narrative to ABA could leave different A motifs. Normalize repeated-letter identity in ABA/Rondo.
- **blocker/general, library:** six old-issue motifs locked Make, selection and deletion. Old motifs remain gray and selectable for deletion, without allowing playback, editing or placement in the wrong issue.
- **blocker/general, version load:** a loaded dance could retain another issue's source card. Restore source, issue and reveal state together.
- **should fix/general, stale state:** revisions kept unrelated real readings; jump-then-edit changed the old slot. Clear current model/real readings on revision, keep snapshots intact, rebuild the selected slot's editor before jumping; stop old transport before Fix; recover focus at Narrative limits.
- **should fix/general, voice:** tuneHow waited behind eight counts and disappeared on the real path. Start it with Make; add an empty-library instruction; keep relevant hints during source selection/placement; avoid naming disabled controls. Manifest updated.
- **should fix/general, layout/access:** short editor choices and Delete hid below a scroll edge. Named editor pages expose complete groups with pinned transport. After audit, fit all six slots and all eight versions, repair compact sidebar/Clear all overflow, and explicitly name Name/What it shows fields. Full version metadata stays in accessible names and titles.
- **should fix/general, facts/meaning:** label chart bars; specify USDA's 2010 retail/consumer scope and Compact's Upper/Lower Basin use allocation. Student meaning starts blank, with a prompt rather than a copied answer.
- **should fix/family:dance, motion/art:** reservoir's final kneel rose. Correct local floor pose; verify descending sequence. Replace code figures with a painted three-person cast, including clear floor keys; improve joint overlaps and spacing. End dots now hold count eight.
- **polish/general, flat feedback:** a 4/4 buried useful criticism. Put conditional craft notes first, highlight them, disclose source-cue recognition and use a generic first-two-phrases note when holes mean there was no B. Keep the rich existing art and composition controls.

#### Findings left

- **blocker/general, prescribed model:** one Glow dome placed once in Rondo fills three A slots; B/C remain empty; Show viewers still yields 4/4 with no authored movement or meaning. This was actually run with input and a complete replay (`review-audit/state-same-picture-rondo-1366x768.png`). Editing all movement/text preserves the source recognition too. The spec explicitly requires this source-word model and same-motif extreme. CODEX-REVIEW section 3 forbids changing that rule. Honest labeling and stronger craft feedback do not fix mastery validity; this blocker is not release-cleared.

#### Break it

- **Recognition 0-4 and saved readings:** default/picture repetition is the cheapest winning path and still passes as above. The specified Hidden/Glow example recomputes exactly 0/4 then 4/4: A presence 96 versus B 16; sizes Hidden 2, Glow 2, Searching 0.5. Saving before replay now stores no score; changing a completed draft invalidates readings; older snapshots retain their own. No best-score leaderboard exists.
- **Form identity/variation check:** different A identities via form switching now normalize; duplicate devices trigger the warning. Fix supplies distinct devices and clears it, as prescribed. This is an authoring aid, not evidence that the student can invent variation; it grants no mastery award.
- **Teacher/ending checks:** same movement fires contrast criticism; two genuine feature differences clear it. A unique solo ending fires the ending note; three in unison clear it; three in canon do not. A Rondo with holes no longer claims a nonexistent B.
- **Counts/progress:** six slots times two repeats gives 96 dance counts, not an unbounded run. Stop/replay replaces transport; jump edits the selected slot. Final dots stay on eight. 5,280 source/device samples are finite; four reservoir heights strictly descend (`pure-checks-results.json`).
- **Limits/storage/reflection:** seventh motif and ninth retained version cannot exceed caps; deleting an old motif escapes the full-library dead end. Empty real-viewer fields are blocked; two question marks produce a note but no model score (`reflection-closeout-results.json`). Typed HTML displays literally. Clear all asks first; Cancel retains the note. Completed and legacy data survive actual reload without importing unearned legacy model scores.
- `functional-core-results.json`: 26 targeted checks passed. `prebreak-results.json` records original failures; `postbreak-results.json`, save-completed/reload-completed/reload-legacy results and storage-final-frames, plus post-audit/phone probes, record repairs. Accelerated endpoint checks supplement, rather than replace, the completed real-time replays.

#### Voice walk

Sound on, default settings, 0.12 s held clicks, 2 s gaps: open folder, Choose this issue, select card, Make, Structure, place A/B, Play dance, Viewers, Show viewers, wait through complete replay.
`voice-main-final-results.json` starts, in order: welcomeFile, motifHow, tuneHow, structHow, playHow, viewersHow, noneNamed, each once. Lines match their visible modes. Navigation/Play intentionally hush several long lines; logs verify starts/order and cancellation, not complete human audibility. No stale narration continues on another screen.

| Check | Spoken | Silent |
|---|---:|---:|
| Five Make actions, tuneHow | 1 | 4 |
| Five allNamed endpoint events | 5 | 0 |
| Five noneNamed endpoint events | 5 | 0 |
The empty-library side path speaks needMotifHow; Read speaks the current hint. Audit first-tap, five-held and quick-double checks are clean. All nine fixed strings match voice/lines.json. Muted Chrome cannot establish headphone timbre or music/narration balance; browser speech remains fallback and no recordings were made.

#### Facts checked

- **Light:** [Falchi et al. 2016, abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC4928945/) supports >80% of people globally and >99% in the US under light-polluted skies; Milky Way hidden from >1/3 of humanity and nearly 80% of North Americans. These are study estimates, not live measurements.
- **Food:** [USDA ERS EIB-121, Buzby/Wells/Hyman, 2014](https://www.ers.usda.gov/publications/43836) supports 2010 retail/consumer loss of 31%, 133 billion pounds, $161.6 billion at retail prices. One in three is an approximate movement analogy; three bodies are not exact percentages.
- **River users:** [Bureau of Reclamation, Colorado River Basin](https://www.usbr.gov/ColoradoRiverBasin/) gives municipal needs of 35-40 million people and also describes over 40 million; about 40 million is appropriately rounded.
- **Allocation:** [1922 Colorado River Compact, III(a)](https://www.usbr.gov/lc/region/pao/pdfiles/crcompct.pdf) apportions 7.5 million acre-feet of beneficial consumptive use annually to each Upper/Lower Basin, 15 million combined. It is not guaranteed flow or a complete account of rights.
- **Dance standards:** [NCAS Dance](https://www.nationalartsstandards.org/), checked against module 393 and concept 397: DA:Cr1 through stimuli/motif generation; Cr2 through form/relationships/devices; Cr3 through revision/versioning; Cn10 through students' own source connection. Activities offer practice; recognition does not assess these standards.
- **Music/timing/model:** original Lantern, per spec and track(): 100 bpm, 4/4, Am-F-C-G per eight counts, A4-C5-E5-C5 pluck, kicks 1/3, offbeat shaker. 96 × 0.6 = 57.6 s; four-count introduction adds 2.4 s, exactly 60 s total. Invented voices and painted stimuli are labeled; motif/viewer rules are tool proposals, not scientific audience predictions.

#### Sensitivity

Request a fresh sensitivity review of people/bodies: three individual older-teen/adult performers with different skin tones, builds and hair, no culture represented by one body; inspect anatomy in motion and accessible adaptation language. Floor poses are demonstrations, not physical requirements. No student must disclose personal trauma.
Review Colorado River framing, particularly Tribal rights and Mexico's share, which this narrow Compact card does not explain. The invented farmer is not testimony or the sole stakeholder. Astronomy-club and cafeteria voices are invented too. Notes explicitly preserve these boundaries; historical allocation must not imply present entitlement or guaranteed supply.

#### Flattest moment left

Once the fixed cue model is discovered, optimizing recognition becomes mechanical. The useful lift is immediate, visible craft criticism plus a real classmate's independent reading; the model still cannot judge the student's own meaning. The other flat moment, generic code bodies performing floor work, was replaced with painted, readable performers. Best moment: watching a source motif change roles across a synchronized form, then seeing the specific contrast/ending feedback. Compared with Beat Lab and Snowy Mail Route in `review-bar-comparison.png`; kept the painterly depth.

#### Graphics

Preserved all seven strong paintings: glow, stars, bin, fridge, reservoir ring, river and studio. Added cc-cast and cc-floor-cast with built-in imagegen, both people:true/drawn_by:codex, prompts and raw originals retained. Three neutral poses articulate through the existing engine; nine kneel/curl/lie keys make twelve source poses total. Twenty-one redundant old pose requests are explicitly superseded, not missing runtime art. No art remains to paint for this scope.
CAST_ART/CAST_REG and FLOOR_ART/FLOOR_RECTS isolate the replaceable figure skin. Engine timing, paths, devices and shape badges remain. Inspected final-size UI, cast contact sheet and 45 source-pose samples. Painted articulation is stylized, not motion capture.
Nine runtime images resolve; final bundle **1,782,285 bytes (1,740.51 KiB)**, below 2 MiB. Existing issue art was not reduced to clear a check.

#### Audit

One final audit completed, 40-minute ceiling, Chrome 9961 / host 8765: `review-audit/audit.md`, **13 leads**. Opened all 81 audit PNGs through labeled contact sheets, with native frames for findings; no runtime errors, initial-size target failures, endless calm motion, resize exceptions or controls left disabled.
Fixed eleven actionable rows: seven sidebar/eyebrow/Clear all overflow rows; two hidden-version rows; one hidden-six-slot row; one unnamed-meaning-field row. The two modal-covered-hint leads are intentional: each dialog supplies its own instruction. No second full audit.
Targeted post-audit frames confirm sidebar at 680/800/1000, all eight versions at 680/760/800/1000/1366 and 375 iframe, all six slots at 680 and 375, accessible field names, and final count dots. Phone probes show eight 84.25 × 44 version cells and six 52 × 44 slots; desktop probes confirm visible targets. Zero console errors in these repair shots.
All STANDARDS sizes were inspected: 680×425, 800×500, 1000×625, 1280×720, 1366×768, 1920×1080, 760×900 and 375×812 iframe. Keyboard-only creation/edit/play/Stop has visible focus; grayscale preserves identities. Motion off holds within a count and advances on the next at 100 bpm. Brand/paper contrast is 7.10:1; white/brand 7.83:1.
Wave lessons checked: hint/Read/state, focus/layout, sizes, source-model giveaways (FAIL above), honest assumptions, standards, Motion off, complete short choices, mid-action resize, immediate welcome, unknown shown unknown, distinct legends, truthful badges, reversible hints and no copied student meaning. Evidence includes keyboard-results, calm-results, voice logs, functional results and review-numbers.json. Test-harness timeouts, selector failures and empty probe returns were not counted as passes; bounded corrected runs supplied evidence.

#### Left open

- The prescribed scoring blocker requires a spec/owner decision; no unilateral assessment redesign or kit change. Do not treat 4/4 as a choreography grade or a cleared learning gate.
- Browser narration is the authorized fallback. No recordings, voice-bank edits, human headphone check, external publication or submission. Sensitivity judgment remains for the fresh reviewer.
- Unattended choices: honor painted dancers, use the minimal articulated cast plus necessary floor keys, retain prescribed model, and prioritize STANDARDS' visible short sets over the spec's sideways phone strip (overflow remains available).
- Limits used for substantive runs: bundle 120 s, drive batches 300 s, audit 2,400 s; original lightweight reads were not all wrapped, a procedural miss. Final static checks and port checks are in review-closeout.json. Only tool/Scratch were written; Chrome 9960/9961 and host 8765 are closed; host.html removed. Builder codex-report.md preserved as historical evidence.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Choreography for a Cause handoff

#### Implementation
src.html starts from the kit starter and loads kit:curio plus kit:dance. Its sections are styling, four permanent workspace shells, source card data, voice, persistence, authoring, performer adapter, source phrases, shared transport, viewer model and event wiring. Data stays in the single bundled HTML. No external requests or libraries are needed.

The open folder uses five evidence cards. The five source choices in Motifs stay visible in a left rail. Primary Make, Play and Stop controls sit outside the secondary editor. Structure has a pinned transport and six slots that fit at phone width, each at least 44 px wide. Viewers has four readings around the stage and a version panel. Compact fact folders scroll their evidence area so full source text remains accessible.

#### Movement and timing
Dance.floor uses stage projection. Its stage view ignores the backdrop option, so resizeStage clears decoration layers and inserts the studio painting, keeping the engine's floor projection. No shared file was changed. Floor contact is at a projected front edge of 88 percent, with performers at z 38. The painting is stretched to the real stage bounds to keep all floor edges visible.

motifPhrase makes eight one-count Dance.phrase steps and uses source-specific phrasing for the cards whose rule needs different dancer roles, pauses or a particular count. Pose edits switch to the student's chosen A/B shapes. Dynamics use Dance.dyn through the phrase engine. Devices change pose reach, pathway amplitude, sampled time or time direction. Low floor poses retain their native shape to avoid applying the kit's extra squat to an already grounded body.

compose caches per-slot phrases. One Dance.clock at 100 bpm drives all three performers, Lantern and the dots. Per-slot canon is sampled with two-count offsets inside each eight-count phrase, holding a delayed entry and truncating at the slot end so total dance counts stay exact. Slot dancer count wins over motif count. Empty slots are skipped. A slot tap replaces the old run synchronously without another count-in. stop drops the play handle, music output, clock and voice immediately.

#### Model and storage
model is a pure function over motifs, slots and issue. Presence sums eight times repeat times slot dancer count per motif id. The kid's size is absolute start/end level span plus pathway travel. The level pair counts as one contrast feature, and dancer comparison uses the actual slot count. Empty entries are skipped, so the first and second filled slots stand in for A and B if a strip contains holes. Ties remaining after the stated rules use first encountered motif.

Viewers reveal after their dependent slot: teacher after B, stranger after the last, friend after the last, kid after the last occurrence of its chosen motif. Cards explicitly identify the model. Devices and edited prose never change the source card's viewer words. Real viewer prose is escaped and saved locally. Conditional craft notes appear before recognition readings. If holes mean the first two played phrases are not A and B, the teacher's contrast note names the played phrases rather than inventing a B.

localStorage key curio-choreo-cause contains the current draft and up to eight immutable version snapshots with full motifs, slots, completed model results and real readings. Opening a version with unsaved work asks first. Changing issue keeps old motifs grayed, replaces the current strip and asks first. A six-motif limit applies across issues. Clear all confirms. All storage operations are caught; the hint reports inability to save. All eight versions fit in a fixed grid outside the notes scroller; full metadata remains in accessible names and titles. An unshown reading is marked ?, with a visible legend, never zero.

#### Owner's painted dancers decision
Three painted performers are live through createPerformer, paintedDancer and paintPerformer. CAST_ART and CAST_REG, plus FLOOR_ART and FLOOR_RECTS, are the swap boundary; preserve the Dance.play set/render interface, timing, floor registration, per-slot visibility and shape badges. art/prompts.json marks both atlases people:true. One neutral painted pose per individual supplies articulated pieces; kneel, curl and lie add nine floor keys. The 21 older pose requests are retained as superseded records. Movement is still interpolated by the dance engine.

Seven non-person paintings were made with the built-in image tool. Full prompts are in art/prompts.json, raw originals in art/raw, finished images in art/*.webp. No people or lettering appears in them. The larger issue images remain at 1200 pixels; all seven are used by the tool.

#### Open questions resolved
- Voice: the spec proposes adding a grown-up voice because the existing bank has no free one. Bank edits are outside this build's allowed folders, so the manifest retains the specified lively-host / Sadachbia while recording the desired future grown-up replacement here. No recordings were made, as required. Browser speech does not select Sadachbia by name and is a fallback, not the final voice.
- Timing clarification: 96 dance counts are 57.6 seconds. Four count-in clicks add 2.4 seconds, so the entire longest run is exactly 60 seconds, rather than under 60 including the count-in. UI and notes say this explicitly.
- Default dancer counts unspecified in several proposals use two, or one for an individual voice. Explicit three-dancer and two-dancer rules win. This makes the Sources example's B presence 16.

#### Engine changes wanted
- kit/dance.js, floor.draw: honor backdrop for stage and provide an option to suppress stage fill and curtains. resizeStage currently replaces only those decoration layers locally.
- kit/dance.js, level: add native low variants for floor shapes so applying low does not double-bend a sitting, lying or crouching dancer. safeLevel preserves native floor shapes locally.
- kit/dance.js, music: allow instrument-specific volume and long pad duration. Lantern currently repeats overlapping engine pad notes to hold its eight-count harmonies; a soft pluck uses the shared track volume.

#### Next
The cold review repairs below supersede the original build's open artwork and compact-editor limitations. No commit, branch change or shared-engine edit was made. Read codex-review.md for the final checks and remaining limitations.

#### Verification and compact layout limits
The cold review's single final full audit completed with 13 leads and no runtime, initial-size, resize or infinite calm-animation failures. Eleven actionable rows were fixed: compact sidebar overflow (seven rows), hidden version choices (two), hidden narrative slots (one), and the unnamed meaning field (one). Two leads intentionally report the modal backdrop covering the page hint; each modal provides its own instruction. Targeted checks followed these corrections; there was no second full audit. Evidence lives in _scratch/choreography-for-a-cause/review-audit/ and the post-audit frame folders. The builder's earlier audit is separate historical evidence.

The cold review replaced the scrolling parameter stacks with named editor pages. Both six-motif libraries and every short parameter group have dedicated views. Full evidence cards and long real-viewer notes still scroll at short heights and on phones. Clear all now stays beside Back to Structure, stacking below it at compact desktop widths. Six slots and all eight version buttons remain visible, with targets at least 44 px. This follows STANDARDS' visible-short-choices rule over the spec's sideways phone strip; overflow remains available if needed.

The modal backdrop intentionally covers the page hint while a dialog is open. The dialog supplies its own instruction. Both real-viewer fields and the Name/What it shows editor have explicit accessible names. First held taps on each of the three folders start welcomeFile immediately. The final Chrome instances and host are closed and host.html removed at review closeout.

Audio was exercised in muted Chrome, including narration logs, transport replacement and timing. Human headphone review of timbre, music balance and narration pacing remains open. Browser speech remains the fallback. Seven existing paintings were preserved, and the built-in image tool made two performer atlases during review, for nine runtime images. No voice recordings were made.


#### Cold review repairs (2026-11-05)
The painted cast is live. CAST_ART and CAST_REG plus paintedDancer are the replaceable skin adapter. cc-cast is one neutral T pose per performer, not a static replacement: clipped painted pieces follow Dance.dancer's projected joints on every render. The engine continues to own poses, paths, clocks, canon, devices and calm timing. Three shape badges preserve non-color identities. All people art is people:true. The 21 earlier unmade pose requests are retained as superseded records, not required runtime assets. Source image, prompt and contact sheet are retained.

Editors use an Edit selector to expose complete small groups without hiding short choice sets below a scroll edge. Libraries, Shape/Space/Meaning, Slot settings and Form checks retain the same authoring capabilities. The main transport stays pinned. Old-issue motifs remain gray and cannot be placed or edited, but can be selected in Your motifs and deleted through Meaning, preventing a full-library dead end.

Save version preserves only readings actually completed, never computes a score behind a skipped replay. Unwatched drafts say Viewers not shown. A revision clears current model and real readings; old snapshots retain their own readings. Loading a version restores its card, issue and reveal state. Switching ABA/Rondo normalizes repeated-letter motif identity. The viewer summary states that recognition reads source cues, not artistic quality, and that each motif keeps its source meaning after edits.

Slot changes while playing rebuild the selected slot's editor before restarting, so edits cannot target the previous slot. Fix variations stops the previous transport. Narrative add/remove recovers focus at its limits. End-of-play dots hold the final eighth count rather than wrapping to count one. The local low kneel now sits on the heels; the reservoir phrase descends through all four measured stages.

The first tuning line now starts with Make's immediate movement instead of waiting behind an eight-count take. Source selection and placement preserve still-relevant instructions. Voice manifest matches the fixed lines. No recordings were generated.

#### Sensitivity
Review the three painted individuals for respectful, natural representation and anatomical clarity in motion. They do not stand for cultures or a preferred dancer body. Source voices remain explicitly invented. River allocation uses Upper and Lower Basin names and beneficial use; teacher notes state that the card is not a full history of Tribal rights or Mexico's share. The water issue should not be read as solely a farmer's concern.

Floor artwork: FLOOR_ART and FLOOR_RECTS add nine key poses (kneel, curl and lie for each of the three people). Painted-upright pieces follow the projected joints; painted-floor key poses blend from the same joint angles and remain anchored to the engine floor. Motion off still jumps only on counts. The two atlases contain twelve source poses total, replacing the earlier request for 21 poses times identities times levels. Crouch, sit, traveling, asymmetry and devices continue through the articulated cast. The river convergence and split leave enough space to read each body.

Storage schema 2 records only completed replay readings. Schema 1 is accepted without losing motifs, versions or typed notes, but its unverified computed recognition entries are cleared and must be replayed. This prevents old shortcut results from surviving the save repair.

#### Left open after cold review
- Blocker, prescribed recognition model: one Glow dome placed once into Rondo fills the three A slots, leaves B/C empty and still earns 4/4 after replay. No original movement or meaning is required. The spec explicitly demands the source-word heuristic and same-motif extreme; replacing that model would contradict it. The UI now describes the limitation and foregrounds craft feedback, but this does not establish learning or clear the blocker. An owner/spec decision is needed before treating recognition as a success gate.
- Unattended decisions: use the owner's painted cast and minimal pose atlases; preserve the prescribed scoring model under CODEX-REVIEW section 3; prioritize the STANDARDS visible short-choice rule on phones. No external action or shared-kit change was made.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-06)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-06)
- 2026-11-25: handoff.md folded in (last changed 2026-11-06)
