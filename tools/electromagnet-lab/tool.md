# Electromagnet Lab: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: electromagnet-lab

#### Built
Four complete modes: Coil, Static, Field and Notebook. Readable source, offline bundle, draft metadata, notes,
voice manifest, audit states, all 20 generated paintings and a handoff are present. Build only, with no commit.
The initial bundled version was 982 KB; redrawing cluttered art reduced the final size substantially.

#### Numbers check
Scratch numbers.json enumerates all 192 coil combinations and 20 Static combinations before implementation.
model-checks.json independently verifies the 3/6/9 through 12/24/36 steel means, zero rounded non-steel counts,
0.6/1.2/1.8 amperes, and about 8 bits for 20 rubs at 2 cm. Field anchors are 86.48, 62.88 and 9.24 degrees at 6 cm.
40,000 independently sampled ratio sets confirm why the student's own means determine the nearest option.
Those samples use new seeds and pairs; they do not reproduce the spec's undocumented Monte Carlo percentages.
Spec conflicts: 36 is the maximum mean, while trials reach 40. The default 10-turn mean is 3, below its own ratio gate.
Done 1's required 4-times result at one battery is therefore impossible under the stated rules. The formula is retained.
Contrast on paper: ink 14.50, muted 5.62, brand 5.72, north 5.89, wire 5.63, ok 4.85, warn 6.03, focus 5.24 to 1.
White on brand is 6.34 to 1. Button outlines are 3.34 to 1 on paper. Lit rows have a bar and labels as well as color.

#### Facts checked
- Turns and current increase a coil's field; current reversal reverses its direction: OpenStax College Physics 2e 22.9.
  https://openstax.org/books/college-physics-2e/pages/22-9-magnetic-fields-produced-by-currents-amperes-law
- A steel core strengthens the electromagnet; wood and aluminum are not ferromagnetic cores: OpenStax 22.2.
  Non-steel coils still make fields. Their zero clip counts here are a model threshold, not an absent field.
  https://openstax.org/books/college-physics-2e/pages/22-2-ferromagnets-and-electromagnets
- Steel can retain some magnetization, and a lifting electromagnet can release steel when current stops: OpenStax 22.2.
  The one-in-three remaining clip is a declared model choice, not a measured frequency.
- A compass indicates magnetic-field direction and filings show its shape: OpenStax 22.3 and NOAA NCEI geomagnetism FAQ.
  https://openstax.org/books/college-physics-2e/pages/22-3-magnetic-fields-and-magnetic-field-lines
  https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions
- The modeled alkaline AA cell is nominally 1.5 volts: Energizer E91 datasheet. Series voltages and current: OpenStax 21.2.
  https://energizer.com/apac/australia/wp-content/uploads/sites/3/2024/05/e91_max_na_AA.pdf
  https://openstax.org/books/college-physics-2e/pages/21-2-electromotive-force-terminal-voltage
- Low-resistance coils heat, and other nearby magnetic material can confound a compass test: OpenStax 21.2 and 22.2.
  Notes say to switch off between real tests and explain the model's omitted unpowered-nail effect.
- Rubbing transfers charge and charged objects polarize neutral objects: OpenStax 18.1 and 18.2.
  https://openstax.org/books/college-physics-2e/pages/18-1-static-electricity-and-charge-conservation-of-charge
  https://openstax.org/books/college-physics-2e/pages/18-2-conductors-and-insulators
- Electric force depends on charge and distance: OpenStax 18.3. Magnetic dipole pull fades with distance: OpenStax magnetism chapters.
  https://openstax.org/books/college-physics-2e/pages/18-3-coulombs-law
- Charging can saturate: Matsusaka et al., Chemical Engineering Science 65, 5781-5807, DOI 10.1016/j.ces.2010.07.005.
  Its review is not an empirical validation of this particular balloon curve. The exact curve and gap factors are model choices.
- Counts, noise ranges, 2.5 ohm resistor, simplified clip proportionality and the fixed Notebook examples come from spec Content.
  All numerical outputs are recomputed from those rules. The bench says MODEL and notes distinguish field from lifting force.
- Fair-variable questions and qualitative non-contact field evidence map to NGSS MS-PS2-3 and MS-PS2-5.
  https://www.nextgenscience.org/topic-arrangement/msforces-and-interactions

#### Break it
checks.json records 31 successful functional and cheap-cheat checks; claims-checks.json adds 58 option and ratio checks.
field-checks.json adds 19 checks, including the rapid-toggle exploit after its repair. These are mechanical evidence, not mastery claims.
- Mash Test on one value: one row is replaced, never three different fair values. A running Test cannot start duplicate trials.
- Change two settings: the row cannot join the old fair set. Zero sets, too few values and three of four cores cannot unlock a claim.
- Rubbing with three values: blocked. Four values including 40 with sufficient signal: opens.
- Guess all claims or ratio options in turn: only the first pick is retained. A wrong first pick remains fixed, not right.
- Always pick 2 times: fails the 4-times pair and both distance families. Every correct ratio is the nearest to the actual means.
- Read a hidden meter: no strength or charge meter exists. The ammeter shows current, not the quiz answer.
- Drop arrows, sprinkle or flip with power off: no checklist credit. Rapid on/off before a visible turn earns no turn check.
  The repaired gate reads the displayed needle. A real turn, off check and 120-degree flip are required.
- Fresh filings after reversal: exact same seeded shape; the compass reverses. Unlock also needs the earlier sprinkle.
- Overlap the coil or place unlimited arrows: compass stays outside it; oldest arrows leave after 40.
- Try every Notebook option: first pick retained. Run is three seconds; Next acts immediately and cancels it.
- Change a setting mid-test or switch modes: no partial row is logged. A negative first-frame timestamp was found and clamped.
- Reload: saved measurements return, first choices reset as the spec requires. There is no saved grade or best score to fake.

#### Voice walk
The full student path used real held clicks at a 2-second pace, with the default Sound setting, then a Field/Notebook side path.
voice-walk.json includes zero console errors and zero HTTP requests. Read repeats the current hint; each mode welcome is reachable.
The main follow-up main-voice.json heard addQ, pickQ, keep, ready, claim, right and tested in order.
It caught test1 naming a temporarily aria-disabled Test through its needs guard. That unnecessary guard was removed.
The how-much instruction could still be dropped as stale before browser speech reached it on the fast path. Strict Done 10 is FAIL.
Right and tested events remain whole on the repaired main sequence. Instructions already acted upon may be cut; Read and mode changes hush.
Notebook's fair instruction was heard once, and right/caseDone events repeated for all three cases. Read intentionally interrupted the last cue.
The final manifest has 32 lines, including a guarded instruction for entering Field with the shared switch already on.
No Algenib recordings were made, as instructed. Browser speech timing and the specified performer's sound remain distinct.

#### Feel check
Best moment: a large clip cluster leaps to the tip, hangs, then drops, and three measured means become a rising fair-test curve.
Flat moment 1: the first Static painting repeated apparatus behind the real simulation. It was redrawn as a quiet, textured worktop.
Flat moment 2: a finished Notebook miniature initially showed its first setup. It now finishes at 40 turns and 12 clips with power on,
or at the measured balloon gap or reversed compass result. Paper bits are irregularly scattered rather than a perfect grid.
Scratch feel-comparison.jpg places a lifting frame beside Snowy Mail Route. Both bar tools were bundled into Scratch and opened.
The workbench has richer materials and restrained Grade 8 feedback; it is not plainer than the finish reference.
I would keep exploring cores, weak fields and the notebook cases beyond ten minutes. Repeating an already tested easy turn set is flatter.

#### Done when
1. FAIL as written: compare and rising three-row chart work; default eligible pair is 20 to 40, about 2 times. Two batteries enable 4 times.
2. PASS: confounded rows do not light with the old set; zeros cannot offer Answer. checks.json.
3. PASS: all 24 direction-option cases checked; Core requires four cores. claims-checks.json.
4. PASS: four ratio families use nearest actual ratio; weak pairs show too small. claims-checks.json and model-checks.json.
5. PASS: Balloon compare adds Rubbing and Gap; four rubbing values include 40; a captured lift shows bits crossing the gap.
6. PASS: off/on/off/flip gates, fresh identical filings and one-try reason checked. field-checks.json.
7. PASS: three one-try cases; fair results 6 and 12 clips, about 8 bits at 2 cm, north then about 45 degrees. checks.json.
8. PASS: edits and mode switches abort without a row; drag, keyboard and Next case work without waiting.
9. PASS with documented compact folding: settings/Test/board fit the main laptop sizes; short landscapes remain side by side.
10. FAIL in strict fast speech timing: how-much may go stale before being spoken. Hints and Read stay correct; privacy is under the table.
11. PASS in completed checks: no people, no HTTP requests, no current tool console errors. Earlier SVG timing errors were fixed.

#### Wave lessons
- Hint and voice: FAIL for strict fast narration. Contextual hints, stale guards and once-only how lines work; how-much remains open.
- Focus and layout: PASS in checked paths. Focus is not taken on load; stable setting buttons survive redraws; dialogs restore focus without scrolling.
- Sizes: PASS for primary controls after compact Field repair. Results navigation follows the controls and can be below the phone fold.
- No giveaways: PASS for sweeps and first-answer retention; no hidden strength badge. Exact spec wording is retained despite unequal sentence lengths.
- Honest numbers: PASS. MODEL is visible, current is on-only and all physical simplifications are explicit in notes.
- Standards: PASS. Solo students ask questions, build fair repeated sets, compare ratios and investigate non-contact evidence in both force types.
- Motion off: PASS in the audit. No infinite calm animation; durations remain 3.6, 4.5 and 3 seconds.
- Short choices: PASS in inspected frames. All options are available together before a pick; unrelated distractors fold after the one allowed answer.
- Resize mid-animation: PASS. Seven focused checks preserve all four modes and finish Coil, Static and Notebook runs across a resize.
- Welcome delay: PASS. No welcomeAfter. First tap acts immediately; welcome content stays in hint and Read.
- Unknowns and meanings: PASS. No measured point before a test; trial ticks and dots differ; off arrows stay gray and on arrows teal.
- True badges and restored hints: PASS. First wrong picks remain fixed. Warm, test and mode hints update with the state.
- No word-copy answer: PASS. Class data names settings, not supported claims. Student means determine the quantitative answer.

#### Audit leads
One audit completed within its 40-minute cap. Its original 48 leads remain in Scratch/audit/audit.md, grouped here without deletion.
- Six compact Class-data/hint overlap or covered-region leads: fixed by reserving adjacent space. Post-frames confirm both controls.
  These cover 680 and 800 base overlap/coverage (four), Static overlap (one), and coil-after-test overlap (one).
- Six zero-size header-font leads at 760 and 375: fixed with real readable 10 px words; focused phone frames confirm.
- Three dialog Close/title or label overlaps: fixed with reserved title width; final Class-data and Real-one dialogs inspected.
- Two short Field hint coverage/out-of-view leads: fixed by folding shared settings into Coil settings and shortening the checklist.
- Nine results-fold leads: intentional reading scroll, eight Older/Newer/Chart/Clear findings at 760 plus records at 375.
  The primary settings, question board and Test remain above the fold; results follow them on the stacked layouts.
- Three hint-covered leads behind Class-data, Real-one and Clear dialogs: intentional modal coverage, with focus restored on close.
- Three Notebook fair-how drops: the automatic state has already run the fair animation, making the queued instruction stale.
  The real held-click side walk heard that instruction once; all three fair-result events were heard. No forced stale replay was added.
- Nine welcome leads: four first Group clicks and Test skip the welcome, and four quick mode double taps hush it.
  BASELINE decision 16 permits first-action interruption. The premise and next action remain visible and available through Read.
- Three no-change clicks: compass click focuses the drag/keyboard target; an off flip has no powered field; clearing empty paper is inert.
  Real dragging, arrow movement, A/drop, powered flipping and clearing populated paper all change their intended state.
- Four resize-disabled leads: audit anchors predated the header-width repair made during that run, hitting adjacent mode buttons.
  Focused current-coordinate held clicks preserve each mode and its control set at 1366 to 760 and back, with no errors.
  The additional three mid-animation resize checks also pass. This targeted replay is resize-checks.json, not a second audit.
Ten five-click/2-second checks were clean; six quick-tap checks were clean besides the four welcome interruptions above.
No tool console errors or real focus loss were found. A server teardown connection reset is harness noise.
The audit's initial phone copy predates repairs. Focused phone/dialog/compact frames use the final bundle; original leads are retained.

#### Frames looked at
First frames, all 11 size frames, four real iframe mode frames, real drag/keyboard frames, Static lift, zero gap,
the repaired maximum lift, all three fair Notebook results, and the workbench/bar comparison were opened.
All 74 audit PNGs were inspected in 20 numbered contact sheets, with suspect regions opened separately; audit-seen.json records them.
Final focused phone, dialog, compact Field, all four resize frames and the 760-wide Field frame were also opened and inspected.

#### Art made
Twenty finished images, all people:false, generated with the built-in image tool and processed only with art.py --rekey.
Three paper scraps, the table, notebook and clip dish were redrawn. Final processed art: 339.12 KB. Recorded voice: 0 KB.
Final bundle: 768.26 KB, below the 2 MB goal. All paintings are used; no placeholder art remains.
The 32-line voice manifest uses provider Algenib and bank gravel-ranger; recording is deliberately deferred.

#### Art still to paint
None. No people assets are required.

#### Engine changes wanted
None. Shared files were left alone.

#### Left open
The default 4-times spec contradiction, unequal supplied claim lengths, exact real-world force scaling and strict fast narration timing.
Recorded gravel-ranger narration remains for the owner's recording process. No school Chromebook or human audio assessment was performed.
The single audit completed. All started Chrome instances and the port 8785 server are closed; final-checks.json records cleanup.
Initial read-only commands used tool wait limits before the hard-deadline wrapper was introduced; subsequent build/check commands are bounded.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: electromagnet-lab
#### Played
Cold Grade 8 solo walk through Coil, Static, Field and all Notebook cases before reading the builder's files; then a projector-sized teacher walk. The tactile bench and clip lift are strong.
Played the two finish references from their existing bundles. Kept the rich apparatus, palette, exploratory choices and measured-data payoff.
#### Findings fixed
- Blocker, general, Notebook: longest option solved all three cases. Balanced distractor lengths and varied the supported answer's length rank; retained each misconception and every supported claim.
- Blocker, general, Field: a flip plus core change could earn the reversal check. The observation now requires unchanged position, power and coil settings, then expires when the displayed needle settles.
- Blocker, general, Field: following Flip before the first sprinkle stranded the comparison. Each powered sample now records its polarity; sample, new flip, sample recovers without free credit.
- Should fix, general, chart: equally spaced 0/5/10/20/40 rubs distorted the curve. Numeric axes now use numerical distances; Core remains categorical.
- Should fix, general, mode entry: Static inherited Coil's folded class card while its welcome named hidden rows. Bench entry exposes its comparison and restores a matching hint.
- Should fix, general, voice: Notebook referred to an absent chart; queued how lines outlived their actions, and result speech could miss the next case. Shortened results, guarded stale lines and stop only obsolete instructions.
- Should fix, general, Field question: warming could replace the hint while Switch was hidden. Kept Switch available, retained the question hint and restored it after power changes.
- Should fix, general, weak Field setup: an insufficient reversal repeated the same instruction. Added visible, narrated stronger-setup guidance for both full and compact controls.
- Should fix, general, shared settings: Field could speak Coil's hidden Answer/Test instruction. Bench-specific ready hints now stay in their bench.
- Polish, general, Notebook: the three-second demonstration was flat. Its live labels now change from 20 turns/6 clips to 40/12, and show 20 rubs/2 cm/about 8 bits.
- Polish, general, art: replaced the flat Notebook compass circle with the existing painted brass compass, dial ticks, shadow and centered needle. Corrected Field face alignment and rekeyed green spill/loop holes.
- Polish, general: singular clip/bit captions now agree with a count of one.
#### Findings left
No confirmed tool blocker or should fix remains, but independent mechanical verification is incomplete. This is not a full audit pass. The supplied default 4-times example also conflicts with its minimum-count rule.
#### Break it
- All six fair sets: repeated one setting only replaces a row; one value cannot unlock. Trying every claim and ratio option retains the first pick and its correction status.
- Confounded rows do not join the old set. Zero-spread sets stay blocked. Core needs four cores; Rubbing needs four values including 40 and enough signal.
- Constant "2 times" fails the stronger Turns/Batteries ratios and gap questions. Answers use the nearest option to the actual measured means; no strength/charge meter or supported-answer label appears before the pick.
- Notebook longest-answer sweep: originally 3/3 supported; now 1/3, with the first two explicitly corrected. No fixed length rank solves the three cases. Trying every option cannot repair the first choice.
- Field button sweep, off flips, arbitrary arrows and rapid on/off do not earn observations. The compass cannot overlap the coil; arrows cap at 40.
- Reversal plus a core change or a move cannot earn check 4. A new real flip at a held stronger setup can. Weak reversal gives a recovery instruction.
- Sprinkling twice at one polarity cannot unlock; a fresh opposite-polarity sample can. Fresh before/after patterns match; the first filings answer stays final.
- Setting/mode changes abort trials without logging partial rows. The real five-tap Test mash yields one row. Calm trials still take about 3.6 seconds, with no infinite animation.
- Keyboard-only entry and compass arrows work. Read works with Sound off; mode change releases Read. Five fair-run result events repeat without repeating their how-to.
- Evidence: review-before-*.json, review-after-*.json, review-guards-*.json, review-weak-*.json and review-last-*.json in Scratch. Scenario fixtures are distinguished from real held-click walks.
#### Voice walk
Held clicks, 120 ms presses, two-second action gaps, default Sound on, real jittered compass drag; trial animations finish before the next test setting.
Coil: addQ, pickQ, test1, keep, ready, claim, right, howMuch, tested. The first row tap may skip the welcome under baseline 16.
Static: wStatic; compare, add Rubbing, select it, test. Shared addQ/pickQ/keep instructions stay silent after their first hearing.
Field: wField, item1, fieldOn, item2, fieldOff, item3, fieldFlip, item4, fieldSprinkle, filings, right, fieldExplore.
Notebook: wNote, first answer result, fair, caseDone; subsequent answer results and caseDone events repeat, with fair silent after its first hearing.
Side paths: weak full/compact setup recovery, Read with Sound off, five fair reruns and rapid toggles. Full logs, cuts and counts are saved, not inferred from queued lines.
The final main walk (review-voice-release.json) has zero console errors, zero HTTP requests and no cut result events. Actioned how-to lines may be cut; none is falsely marked spoken while merely queued.

| Lines | Kind | Expected | Spoken |
|---|---|---:|---:|
| addQ, pickQ, test1, keep, claim, howMuch, fair | how | 1 each | 1 each |
| wStatic, wField, wNote; wCoil first-tap skip | welcome | 1 / 1 / 1 / 0 | 1 / 1 / 1 / 0 |
| fieldOn, fieldOff, fieldFlip, fieldSprinkle, filings, fieldExplore | how | 1 each | 1 each |
| ready, tested; item1 through item4 | event | 1 each | 1 each |
| right / wrong / caseDone in the main walk | event | 4 / 1 / 3 | 4 / 1 / 3 |
| caseDone in five fair reruns | event | 5 | 5 |
#### Facts checked
- Turns/current strengthen a fixed-geometry coil; current reversal reverses its field: [OpenStax 22.9](https://openstax.org/books/college-physics-2e/pages/22-9-magnetic-fields-produced-by-currents-amperes-law).
- Steel strengthens a coil; wood/aluminum do not do the same; an air-core coil still has a field; steel may retain magnetism; nearby scissors confound an on-only test; scrap cranes use electromagnets: [OpenStax 22.2](https://openstax.org/books/college-physics-2e/pages/22-2-ferromagnets-and-electromagnets).
- Compass direction, field-line shape and non-contact magnetic evidence: [OpenStax 22.3](https://openstax.org/books/college-physics-2e/pages/22-3-magnetic-fields-and-magnetic-field-lines); magnetic versus true north: [NOAA NCEI](https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions).
- AA nominal 1.5 V: [Energizer E91](https://energizer.com/eu/spain/wp-content/uploads/sites/9/2024/05/e91_max_na_AA.pdf). Series cells/current/internal resistance: [OpenStax 21.2](https://openstax.org/books/college-physics-2e/pages/21-2-electromotive-force-terminal-voltage); heating at high current: OpenStax 22.2/22.9.
- Rubbing transfers charge: [OpenStax 18.1](https://openstax.org/books/college-physics-2e/pages/18-1-static-electricity-and-charge-conservation-of-charge); neutral-paper polarization: [18.2](https://openstax.org/books/college-physics-2e/pages/18-2-conductors-and-insulators); charge/distance dependence: [18.3](https://openstax.org/books/college-physics-2e/pages/18-3-coulombs-law).
- Saturation model form: Matsusaka et al., CES 65 (2010), DOI 10.1016/j.ces.2010.07.005, corroborated by [Matsusaka, KONA 29 (2011), equation 12](https://www.jstage.jst.go.jp/article/kona/29/0/29_2011007/_pdf/-char/en). Neither source validates this balloon's numerical parameters.
- Exact counts, 2.5 ohms, gap factors, noise and idealized Earth/pole units are declared spec model choices. Independent Python enumerated 192 coil and 20 static settings: current 0.6/1.2/1.8 A, maximum mean 36, non-steel mean at most 0.36, class counts 6/24/0/5, fair Notebook 6/12/about 7.8 bits.
- Runtime means match all 212 independently computed settings. All 24 claim branches and 16 ratio branches pass; too-small ratio guesses and a three-core set with a genuine signal stay blocked. Numeric chart positions are measured, not assumed.
- Small-magnet home precaution: [U.S. CPSC](https://www.cpsc.gov/safety-education/neighborhood-safety-network/toolkits/child-safety). Notes distinguish real heating, remanence, field strength and simplified clip counts.
- Student-question/fair-set work teaches [MS-PS2-3](https://www.nextgenscience.org/pe/ms-ps2-3-motion-and-stability-forces-and-interactions); off/on/flip, gaps and flawed-test evaluation teach [MS-PS2-5](https://www.nextgenscience.org/pe/ms-ps2-5-motion-and-stability-forces-and-interactions).
#### Sensitivity
None: no people, cultural, religious, historical or body content. All 20 assets are marked people:false and visually checked.
#### Flattest moment left
Retesting an already understood easy Turns set is routine. The weak-field recovery, changed quantities and richer Notebook compass improve the original weakest demonstration without adding topics or scoring.
#### Graphics
All 20 paintings checked in scene and on a new contact sheet. No new painting needed; one cutout reprocessed, precise compass drawing upgraded. Art 339.05 KB; bundle 781.90 KB; no recordings.
Phone controls fit with zero horizontal overflow; compact Notebook and Field question frames retain readable evidence and an accessible Switch. Grayscale and Motion off checked.
Independent contrast on paper: ink 14.50:1, muted 5.62:1, brand 5.72:1, ok 4.85:1, focus 5.24:1; white on brand 6.34:1. Labels and marked corrections remain useful in grayscale.
Compared the workbench with Snowy Mail Route and Beat Lab. Kept its richer, age-appropriate laboratory finish.
#### Audit
Audit not finished. The one run had a 40-minute process-tree cap, but exited on its own 60-second CDP domain-enable timeout in the initial size stage. No audit.md or PNGs were produced, so there were no partial leads to fix.
Did not rerun it, following the incomplete-audit stop rule. Failure receipt: _scratch/electromagnet-lab/review-audit-failure.md; artifact hashes and cleanup: review-closeout.json. No claim of all-size, resize or mechanical-audit clearance is made.
Direct review frames cover 680x425, 1366x768 and real 375x812 iframe states. Fresh 800x500, 1000x625, 1280x720, 1920x1080 and 760-wide audit checks remain unverified. The 37 focused frames were inspected in ten contact sheets, with phone/compact/main-path frames opened separately.
#### Left open
- Done when 1 is impossible as written: at one battery, 10 turns averages 3 clips, below the ratio gate's minimum 4. The eligible default comparison is 20 to 40, about 2 times; two batteries permit 10 to 40, about 4 times. Kept the formula and spec untouched.
- Algenib/gravel-ranger recordings remain absent, as in the build. Verified browser-speech starts and timing through the muted Chrome log; no human listening or physical school-device test was claimed.
- Unattended choice: applied the explicit no-giveaway/length rules to distractor phrasing while preserving the supported claims and misconceptions. The early review draft lived in Scratch so writing codex-review.md remains the final action.
- The first read-only document command used a tool wait limit; subsequent shell commands used explicit hard process deadlines.
- Only tools/electromagnet-lab/ and _scratch/electromagnet-lab/ were intentionally written. No git commits or shared-source changes. No tool-folder host.html. Every assigned Chrome/host port was closed at closeout; Windows denied the extra process-command-line inventory, so no claim of an OS-wide process inventory is made.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Electromagnet Lab handoff

Build only. No commit, deployment or separate polish round. The final build report is codex-report.md.

#### Structure

src.html starts from kit/starter/src.html. The order is responsive layout, stable controls, content and state,
fair-test model and actions, DOM rendering, workbench drawing, Field and Notebook, then input bindings.
The kit owns Motion, Sound, Read, tones and the narration queue. No family engine applies.
All moving scientific geometry and the chart are SVG. Twenty generated illustrations are embedded by the bundler.
The standalone file is electromagnet-lab.html. No data file or outside library is loaded by the tool.

#### State and gates

Only completed rows are saved in guarded localStorage curio-emlab. Their means are recomputed on loading.
Each row is unique by bench and settings. Retests replace it. A setting change or mode change cancels an active test.
Boards start empty and can only gain a question through differences between class-data rows.
Fair rows match every other current setting. Minimum values and a non-flat spread are independent gates.
First claim and ratio picks are retained. A displayed correction never converts the first answer to a right answer.
The spec's tested, fixed and found, fixed labels mean corrected evidence, not independent mastery.
Claim evidence is frozen after the first pick, except that a too-small ratio can receive a stronger fair set.
Core and Rubbing go directly from their claim to the tested mark. They have no ratio task.

Field has two point poles, a one-unit north Earth field and an exclusion zone around the coil.
Compass movement uses pointer capture or half-centimeter arrow-key steps. A drops an arrow, capped at 40.
Checklist turns use the displayed needle angle after its 0.3-second ease. Instant on/off tapping cannot claim a turn.
Fresh filings use fixed seeded positions and the coil component, so reversing polarity preserves their shape exactly.
The student must sprinkle before a flip and again after a completed turn to unlock the direction question.
Notebook fair runs last three seconds. Next case is live during a run, which cancels rather than silently finishing.

#### Art and voice

All 20 specified paintings were generated individually with the built-in image tool during the build.
Every asset has people:false and drawn_by:codex. The manifest has full prompts and the common painted-realism style.
Five first candidates were redrawn: three paper scraps came back as scenes; the table and notebook had distracting apparatus.
The clip dish was redrawn to neutral frosted glass after key removal tinted the transparent glass.
Raw originals are in art/raw and final WebP files are in art. Only art.py --rekey was used for processing.
Art previews, contact sheets and discarded build evidence stay in Scratch.

voice/lines.json declares provider voice Algenib, bank gravel-ranger and the warm shop-teacher direction.
No audio was recorded in Build.
Curio.voice currently falls back to browser speech, so a browser voice is not the specified recorded performer.
How-to lines are once per page load; events use unique queue keys. Read speaks the current hint and the initial data summary.

#### Settled choices and contradictions

The spec lists no Open questions. No user questions were asked in this unattended build.

- The user's image-tool instruction supersedes the spec's older Local FLUX route. No people are needed in this scene.
- The seven-line preview mistakenly counted 21 images. The full spec lists 20, all present and used.
- The maximum model mean is 36, while the required noise formula allows a trial of 40. The formula and 40-clip dish win.
- Done when 1 requests 4 times from 10, 20 and 40 turns at one battery. Its 10-turn mean is 3, below its own ratio gate of 4.
  That setup can compare 20 to 40, about 2 times. At two batteries the 10-to-40 comparison is eligible and gives about 4 times.
- Magnetic field scales with turns and current. Actual lifting force and clip count need not. The spec's linear count rule is
  retained as a labeled model; notes explicitly distinguish the physical field relation from this teaching approximation.
- The field's shape would not stay identical if the one-unit Earth component were also used for filings on reversal.
  Filings show the coil component, while the compass includes Earth. This follows the spec's intended shape/direction lesson.
- Full class rows, comparison chips, board and controls cannot all remain open in the short previews. After two inline rows
  are selected they fold to the compare strip and a Class data button. Full rows remain available in that dialog.
  At short landscape sizes the Class data button shares the hint row and the board uses four columns, preserving 44 px targets.
- Answer cards temporarily fold the settings. After a first pick, unrelated distractors fold away and the chosen and supported
  answer remain. This keeps every available choice visible before the first pick and the correction visible afterward.
- At 760 wide the stage stays at 16:10 and is centered narrower than the page so the controls fit the same viewport.
  At 375 wide the stage fills the width. The results table follows the controls and can require page scrolling on a phone.
- Cold review retained the supported claims and rewrote distractors with the same misconceptions and comparable lengths.
  The original longest-answer shortcut solved all three Notebook cases. It no longer does; first answers still remain final.
- The brief asks for an early tool report, while the user says to stop as soon as it is written. An early report draft was kept
  in Scratch and the tool report is written only as the final build action.

#### Evidence

Scratch is S:/CurioClass-codex/_scratch/electromagnet-lab. numbers.json enumerates all 192 coil settings and 20 Static settings.
model-checks.json independently checks numerical anchors, 40,000 ratio sets and palette contrast.
checks.json records the full functional and cheat walk. claims-checks.json tests every direction option, Core's four-value gate,
and the four ratio families. field-checks.json includes the rapid-toggle attempt and observed needle-turn checks.
The initial oversized drive expression exceeded its internal 60-second evaluation cap. The bounded CDP runner launches the
scenario and polls small results instead. Subsequent scripted checks complete; this does not modify the shared driver.
size-frames contains the one full size pass. phone-frames covers the real 375 px iframe and other work states.
input-frames checks real jittered dragging and keyboard movement. Voice and final audit evidence are in Scratch too.
Build and check commands run from the authorized root with deadlines. Chrome uses only assigned ports, with muted audio.
The iframe server uses 8785 and is stopped after its shots. No host.html is created inside the tool folder.

#### Sensitivity

No cultural, religious, historical or body content. No people appear in the illustrations.
Science and electrical heating claims are sourced in notes.md. This is an on-screen lab, not instructions for wiring a real coil.

#### Engine changes wanted

None. No shared kit, engine, documentation or other tool was edited.

#### Left open

Recorded Algenib narration remains for the owner's recording pipeline, as requested by Build only.
The default 4-times numerical example needs a future spec correction. The spec file was left unchanged.
The build's fast-voice failure was repaired in cold review; the held-click walk now hears the how-much instruction,
all mode welcomes after the permitted first-tap skip, and all three fair-result events. Review evidence supersedes the build timing note.
Desktop headless checks do not establish actual school-device performance or human audio quality.

#### Cold review repairs

The review first played the bundle without reading this handoff or the build report. Its evidence has the review-
prefix in Scratch. The new review report is the current disposition; codex-report.md preserves the original build evidence.
Coil and Static expose their comparison on entry. Their numeric chart axes use actual distances between settings.
The six supported claims are unchanged. Distractor wording balances lengths while preserving the original wrong ideas.
Results are brief enough for two-second input. Obsolete how-to lines stop when their action is taken; results stay whole.
The Field switch stays available during its question, and warming does not replace the question's instruction.
A filings sample records its polarity. A later opposite-polarity sample unlocks the question, even after an early flip.
The fourth checklist item now expires its observation after the displayed needle settles. Changing the core, position,
power or other coil settings cancels that observation. A small real turn gets a stronger-setup cue, with a compact version.
Notebook's fair runs show both settings and the changing counts. Case 3 uses the painted brass compass, dial ticks,
glass and metal highlights, and a centered needle instead of the plain circle. The same alignment fixes the Field compass.
The existing compass painting was rekeyed with despill and handle-hole removal. No new paintings or recordings were needed.
The review uses only Chrome 9960 through 9967 and the temporary host on 8765. Shared kit and scripts are unchanged.
The single independent review audit exited on its internal 60-second CDP domain-enable timeout before making
audit.md or any frames. It was not rerun under the incomplete-audit stop rule. Review audit coverage of 800x500,
1000x625, 1280x720, 1920x1080 and 760 wide remains unverified; earlier builder evidence is not a substitute.
The review directly inspected 680x425, 1366x768 and a real 375x812 iframe. The failure receipt and closeout hashes
are in Scratch/review-audit-failure.md and Scratch/review-closeout.json. All assigned ports were closed at closeout.

#### Initial audit repairs

The audit was run once. Its original leads are retained, with dispositions in the report.
The compact Class data button now sits beside a narrower hint. Mobile header controls keep readable words at 10 px.
Dialog titles reserve space for Close. Header button widths are stable when Sound changes.
Short Field previews fold the shared controls into Coil settings and show four compact checklist labels.
The dialog uses fresh button clones with shared state and guarded focus restoration. A held-click check changed batteries to 3.
Closing it restores the relevant Field instruction. Full laptop layouts retain all three setting rows.
Answer cards fold unrelated controls until their one allowed choice is made; the filings result has Back to paper.
The paper and notebook fill the workspace when results are hidden. Scene captions have light plaques for contrast.
Post-frames, post-phone-frames, last-phone-frame and dialog-frames verify the affected states without a second full audit.
The audit's initial phone copy predates these repairs; the focused phone checks use the final source and bundle.
All 48 original audit leads are answered in the report. All 74 audit PNGs were inspected in 20 numbered contact sheets.
Seven focused resize checks preserve all four modes and complete Coil, Static and Notebook animations across resizing.
Original resize leads used header coordinates from before its width repair; fresh held clicks use each current button's position.
All started Chrome instances and the port 8785 server are closed. final-checks.json records cleanup and artifact integrity.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
