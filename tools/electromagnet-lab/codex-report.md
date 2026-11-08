# Codex report: electromagnet-lab

## Built
Four complete modes: Coil, Static, Field and Notebook. Readable source, offline bundle, draft metadata, notes,
voice manifest, audit states, all 20 generated paintings and a handoff are present. Build only, with no commit.
The initial bundled version was 982 KB; redrawing cluttered art reduced the final size substantially.

## Numbers check
Scratch numbers.json enumerates all 192 coil combinations and 20 Static combinations before implementation.
model-checks.json independently verifies the 3/6/9 through 12/24/36 steel means, zero rounded non-steel counts,
0.6/1.2/1.8 amperes, and about 8 bits for 20 rubs at 2 cm. Field anchors are 86.48, 62.88 and 9.24 degrees at 6 cm.
40,000 independently sampled ratio sets confirm why the student's own means determine the nearest option.
Those samples use new seeds and pairs; they do not reproduce the spec's undocumented Monte Carlo percentages.
Spec conflicts: 36 is the maximum mean, while trials reach 40. The default 10-turn mean is 3, below its own ratio gate.
Done 1's required 4-times result at one battery is therefore impossible under the stated rules. The formula is retained.
Contrast on paper: ink 14.50, muted 5.62, brand 5.72, north 5.89, wire 5.63, ok 4.85, warn 6.03, focus 5.24 to 1.
White on brand is 6.34 to 1. Button outlines are 3.34 to 1 on paper. Lit rows have a bar and labels as well as color.

## Facts checked
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

## Break it
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

## Voice walk
The full student path used real held clicks at a 2-second pace, with the default Sound setting, then a Field/Notebook side path.
voice-walk.json includes zero console errors and zero HTTP requests. Read repeats the current hint; each mode welcome is reachable.
The main follow-up main-voice.json heard addQ, pickQ, keep, ready, claim, right and tested in order.
It caught test1 naming a temporarily aria-disabled Test through its needs guard. That unnecessary guard was removed.
The how-much instruction could still be dropped as stale before browser speech reached it on the fast path. Strict Done 10 is FAIL.
Right and tested events remain whole on the repaired main sequence. Instructions already acted upon may be cut; Read and mode changes hush.
Notebook's fair instruction was heard once, and right/caseDone events repeated for all three cases. Read intentionally interrupted the last cue.
The final manifest has 32 lines, including a guarded instruction for entering Field with the shared switch already on.
No Algenib recordings were made, as instructed. Browser speech timing and the specified performer's sound remain distinct.

## Feel check
Best moment: a large clip cluster leaps to the tip, hangs, then drops, and three measured means become a rising fair-test curve.
Flat moment 1: the first Static painting repeated apparatus behind the real simulation. It was redrawn as a quiet, textured worktop.
Flat moment 2: a finished Notebook miniature initially showed its first setup. It now finishes at 40 turns and 12 clips with power on,
or at the measured balloon gap or reversed compass result. Paper bits are irregularly scattered rather than a perfect grid.
Scratch feel-comparison.jpg places a lifting frame beside Snowy Mail Route. Both bar tools were bundled into Scratch and opened.
The workbench has richer materials and restrained Grade 8 feedback; it is not plainer than the finish reference.
I would keep exploring cores, weak fields and the notebook cases beyond ten minutes. Repeating an already tested easy turn set is flatter.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
First frames, all 11 size frames, four real iframe mode frames, real drag/keyboard frames, Static lift, zero gap,
the repaired maximum lift, all three fair Notebook results, and the workbench/bar comparison were opened.
All 74 audit PNGs were inspected in 20 numbered contact sheets, with suspect regions opened separately; audit-seen.json records them.
Final focused phone, dialog, compact Field, all four resize frames and the 760-wide Field frame were also opened and inspected.

## Art made
Twenty finished images, all people:false, generated with the built-in image tool and processed only with art.py --rekey.
Three paper scraps, the table, notebook and clip dish were redrawn. Final processed art: 339.12 KB. Recorded voice: 0 KB.
Final bundle: 768.26 KB, below the 2 MB goal. All paintings are used; no placeholder art remains.
The 32-line voice manifest uses provider Algenib and bank gravel-ranger; recording is deliberately deferred.

## Art still to paint
None. No people assets are required.

## Engine changes wanted
None. Shared files were left alone.

## Left open
The default 4-times spec contradiction, unequal supplied claim lengths, exact real-world force scaling and strict fast narration timing.
Recorded gravel-ranger narration remains for the owner's recording process. No school Chromebook or human audio assessment was performed.
The single audit completed. All started Chrome instances and the port 8785 server are closed; final-checks.json records cleanup.
Initial read-only commands used tool wait limits before the hard-deadline wrapper was introduced; subsequent build/check commands are bounded.
