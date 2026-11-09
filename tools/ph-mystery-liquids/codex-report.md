# Codex report: ph-mystery-liquids
## Built
- Grade 10 chemistry, Cases and Bench, from the kit starter. Three cases, seven liquids, nine tray actions,
  keyboard and drag labels, an observation notebook, live indicator fills, fizz, bulb states and a responsive spill graph.
- Eighteen paintings load: seventeen made during this build and the existing prep room retained. No people.
- Offline HTML, draft stage built, teacher notes, voice manifest, audit states, source and handoff are present.
- No commits, deployment or polish round. Cwd was S:/CurioClass-codex throughout.

## Numbers check
- Independent script: _scratch/ph-mystery-liquids/check_numbers.py. Browser assertions: logic-results-final.json.
- Vinegar pH: 2.413155, 2.915338, 3.422241. HCl: 2.397940, 3.397940, 4.397940.
- Ammonia: 11.124723, 10.618424. Bicarbonate: 8.347217. Borax: 9.267606.
- At 84.007 g/mol, C2 needs 0.699442 g and 0.00336028 g; ratio 208.15. Requested displays round to 0.699 g,
  0.0034 g and approximately 208. Integer-milligram button endpoints are 0.700 g and 0.004 g.
- C3 needs 4.20035 g, which rounds to the spec's 4.2004 g. At 2.10, 3.78, 4.16 and 4.20 g, computed pH is
  0.300994, 0.999674, 2.017442 and 4.079217. At 4.201 g it is 8.35. No finer step was added.
- Contrast: brand/panel 6.96:1, brand/secondary 6.60:1, ink/brand 7.43:1, bottle label 16.63:1.
- At extreme dilution, the bare strong-acid formula would predict an alkaline acid. Water autoionization corrects
  that limit; weak quadratics are floored at neutral. All specified readings are unchanged, and notes state the limit.
- An initial test expected 65 graph points for a 64-point sequence. Corrected the test, then verified every point.
- Final functional/adversarial run: 100/100 assertions passed. CSS, focus and audit repairs received targeted checks.

## Facts checked
- Acetic Ka 1.8e-5, carbonic Ka1 4.3e-7 and Ka2 4.7e-11, boric Ka 5.4e-10:
  [OpenStax Chemistry 2e, Appendix H](https://openstax.org/books/chemistry-2e/pages/h-ionization-constants-of-weak-acids).
- Ammonia Kb 1.8e-5: [OpenStax Appendix I](https://openstax.org/books/chemistry-2e/pages/i-ionization-constants-of-weak-bases).
- pH/concentration, weak versus strong dissociation, acid-carbonate reaction and titration interpretation:
  [OpenStax 14.2](https://openstax.org/books/chemistry-2e/pages/14-2-ph-and-poh),
  [14.3](https://openstax.org/books/chemistry-2e/pages/14-3-relative-strengths-of-acids-and-bases),
  [14.7](https://openstax.org/books/chemistry-2e/pages/14-7-acid-base-titrations).
- Indicator bands use the spec's simplified boundaries: methyl orange 3.1/4.4, bromothymol blue 6.0/7.6,
  phenolphthalein 8.2/8.6 for clear/pale/pink, litmus 4.5/8.3. All fresh-liquid colors and each boundary tested.
  The named source is OpenStax 14.7's indicator figure. Color words accompany the drawings.
- Mobile ions produce electrical conduction: [OpenStax 11.2](https://openstax.org/books/chemistry-2e/pages/11-2-electrolytes).
  Exact bulb thresholds and stock concentrations are explicit instructional inputs, not measured real-product ratings.
- [EPA](https://www.epa.gov/acidrain/what-acid-rain) gives normal rain about pH 5.6 because of dissolved carbon dioxide.
  Applying 5.6 to this open distilled-water sample is the spec's model assumption, not a universal distilled-water value.
- Lime 2.00-2.35, lemon 2.00-2.60, vinegar 2.40-3.40, apple juice 3.35-4.00, tomato juice 4.10-4.60:
  [Clemson's current food table](https://www.clemson.edu/extension/food/_files/ph-of-common-foods-table.pdf).
  The old spec URL redirects. The current two-page table matches all five ranges and notes food variation.
- Goggles, reporting spills immediately, avoiding tasting and school safety rules:
  [ACS student code](https://institute.acs.org/acs-center/lab-safety/education-training/high-school-labs/student-lab-code-of-conduct.html).
  Never smelling is the supplied conservative classroom rule. The bleach warning is independently corroborated by
  [Health Canada](https://www.canada.ca/en/health-canada/services/home-safety/household-chemical-safety.html).
- Fixed buffer readings, escaping CO2, ignored volume change and residual-acid pH are explicitly simplified.
  The tool is not a full acetate-buffer titration or arbitrary-mixture simulator. Notes explain those limits.
- [NGSS HS-PS1-2](https://www.nextgenscience.org/sites/default/files/HSTopic.pdf): the required electron/periodic-trend explanation is not taught. The module mapping remains an owner issue;
  neither the UI nor the metadata claims full mastery of that standard.

## Break it
| Gate or display | Cheapest attack tried | Result and repair |
|---|---|---|
| C1 completion | Place the correct answer key without testing | Blocked. Each bottle needs uniquely discriminating evidence. |
| C1 evidence | Run one uninformative indicator on every bottle | Blocked. Remaining candidates are computed from actual observations. |
| C1 revision | Check wrong labels repeatedly, then place right labels | Revisions allowed as specified; no score or best record is awarded. Evidence still required. |
| New shelf | Reuse old labels and observations | Seed changes key; labels, observations, evidence and completion cleared. |
| Locked meter | Call the API directly in C1 | No pH or notebook leak; noMeter guide names available alternatives. |
| C2 soda endpoints | Dump 0.1 g into HCl and accept the overshoot | Blocked. Requires the first 0.001 g endpoint and a fresh undiluted sample. |
| C2 explanation | Click every option after one experiment | Wrong answer clears both dilution measurements. Cycling alone cannot pass. |
| C3 start | Press soda or call its API before reporting | No dose or graph point added. Teacher report required. |
| C3 graph gate | Sweep +0.1 g through the endpoint | No completion. Must record a 0.001 g crossing of the steep rise. |
| C3 explanation | Choose wrong, add one token step, then choose right | Blocked. Reset, report and rebuild the graph before retrying. |
| Readout | Twelve dilutions; repeated additions during fizz | Scientific notation fits; readings and total update synchronously. Another test clears fizz immediately. |
| Saved progress | Reload; Clear; deny all storage access | Reload preserves progress, Clear resets it, denied storage remains playable. |
- No points, grade, saved best score, percentage clue, answer-coded badge or answer-coded bottle attribute exists.
- Wrong-label speech initially replaced queued events. Each check now has a unique event key and a label-version
  validity guard. Two held checks 2 seconds apart both start their lines; moving a label invalidates stale feedback.

## Voice walk
- 120 ms held clicks at a 2-second pace. Main: wCases starts, opening C1 intentionally hushes that now-stale welcome,
  then c1, pickedHow, labelHow and solved start, in that order. The how lines start once. See voice-main.json.
- The main path uses actual Tab and Enter for all six labels and Check labels. It closes C1 and survives a reload.
- Side: wBench, pickedHow, Read, c2Tip, spillFirst, c3Soda and Read. Mode changes hush the old scope.
  Read speaks the current hint. See voice-side.json and voice-side-complete.json.
- wrong-voice.json confirms wrong:1 and wrong:2 both spoken. The earlier side attempt ended before queued feedback;
  the queue repair and longer targeted check supersede that failed check, not the whole side walk.
- The added fresh-sample hint after Vinegar drops was checked through a held Read action: spoken Read text matches
  the current hint exactly (flow/read-fresh-final).
- Bank firm-captain / Alnilam is specified, with all fixed lines in voice/lines.json. No recordings were made.
  Browser fallback cannot reproduce the selected bank's timbre reliably.

## Feel check
- Best moment: the initially identical acid readings give way to dramatically different soda endpoints, followed
  by two different dilution shifts. The steep spill-graph jump makes the final thousandth matter visibly.
- Flattest moment 1: the first compact layout hid labels. Reduced duplicate prose, kept all six labels in view,
  enlarged the visual priority of the beaker, and gave the phone a shorter bench with labels on the first screen.
- Flattest moment 2: repeated soda presses could feel like counter tapping. Each press now produces immediate
  sound, fizz or a graph point; coarse sweeping cannot complete the drill, and precision matters at the rise.
- Visual comparison: feel-comparison.jpg places the tool beside Snowy Mail Route. Both reference tools were opened.
  The painted lab has depth, reflected daylight, layered glass and tactile labels; it does not look plainer.
- Full-case functional paths and a real-input C1 student path were played. This is not a claim of a 25-minute
  classroom trial or of the separate ten-minute super-tool check.

## Done when
1. PASS: all specified fresh and diluted pH readings, independently recomputed and asserted.
2. PASS: each liquid's four indicator colors, words and all transition boundaries asserted.
3. PASS: vinegar/HCl dim, salt bright, distilled dark; all seven liquids tested.
4. PASS: C1 meter lock, correct closure, repeated wrong events and seeded New shelf verified.
5. PASS: 0.700/0.004 g button endpoints and 0.699/0.0034 g, approximately 208 reference card verified.
6. PASS: teacher gate and every specified C3 graph value verified, including the 4.200/4.201 g jump.
7. PASS: beaker is the central largest object at laptop and preview sizes; C3 tray and graph share the focus.
8. PASS: additions during fizz update in the same frame; a different test clears the old result immediately.
9. PASS: how lines once per load; appropriate per-mode guides; only noMeter names the locked meter.
10. PASS: real-input reload/Clear checks and denied-storage fallback.
11. PASS: eighteen images, zero people or painted lettering; labels and readings are code.
12. PASS with audit dispositions below: every required size, iframe phone, real keyboard and drag, clean tool console,
    offline resources and no em dashes. The outer test host alone requested a missing favicon; the tool did not.

## Wave lessons
- Hint/voice: PASS. Hint changes synchronously, Curio.voice handles heard state and Read, unique event keys preserve checks.
- Focus/layout: PASS. Stable controls, deliberate focus transfer for phone explanation phase, preventScroll on transfers.
- Sizes/targets: PASS after audit repair of the 40 px Cases button; main controls tested at every prescribed size.
- No giveaways: PASS. No score clues; parallel explanation lengths; observation and precision gates resist sweeping.
- Honest numbers: PASS. Ion thresholds, buffers, temperature and spill simplifications named; exact versus rounded amounts distinguished.
- Standards: FAIL for full HS-PS1-2 coverage in the supplied mapping. Notes explicitly identify the missing electron work.
- Motion off: PASS. No infinite animations remain; fizz keeps its one-second lifetime without motion.
- Short choice sets: PASS after compact and phone layout repairs; secondary Help/Clear and reference foods may scroll.
- Resize during action: PASS in audit; samples and graph history survive resize, no animation locks.
- Deferred welcome: PASS. No welcomeAfter; an action-specific guide supersedes the irrelevant welcome.
- Unknown stays unknown: PASS. Clear colorless bottles, Untested initial reading, blank notebook until a test.
- One style/meaning: PASS. Indicator color words and bulb words; status glyphs distinguish right and wrong labels.
- Honest badge: PASS. Closed means the task's evidence and explanation gates were met, not a grade.
- Hint reverses with state: PASS. Fresh sample, mode/case changes, reset spill and New shelf update immediately.
- No copying answer words: PASS. Observations give colors, amounts and pH; no reason is shown before an explanation.

## Audit leads
- The single audit completed within 40 minutes, with 108 leads. Original snapshot: Scratch/audit/audit.md.
- 1 small target: fixed Cases to 44 px minimum. Real keyboard-start shot measures 44 by 44 and opens C1.
- 49 overlap leads: native closed-details descendants had geometry despite not being painted. Explicitly hide those
  descendants when closed. The open-help frame shows normal scrolling flow, without overlapping the device controls.
- 32 fold leads: repaired 18 primary mobile controls. All six labels and Check/New shelf now fit the first phone view;
  C2's three choices fit when active; C3's teacher control and three choices fit. Fourteen Help/Clear leads are
  intentionally scrolling secondary controls, outside the experiment loop.
- 10 short-choice-panel leads list only Help/Clear, not an answer set. The actual label and explanation sets are all
  visible when used. The food ladder is passive reference material and may scroll.
- 5 keep-region leads: transparent beaker/rack hit tests are not an optical visibility test. Corrected layering keeps
  letters above glass and lets pointer input pass through art; native bottle-C selection was verified. The laptop
  notebook now fits (bottom 674.8 in a 720 px view). The phone notebook remains reachable by normal page scrolling,
  as the spec requires, rather than fully fitting the fixture's overly broad keep rectangle.
- 11 welcome leads: six initial bottle taps formerly named a disabled test; they now direct students to a case.
  Five mode/case/Clear taps correctly use their own contextual guide instead of a delayed old welcome. Main and side
  voice logs confirm the appropriate guides; there is no welcomeAfter.
- Audit Motion off, resized mid-action, repeated held input and quick taps are clean. No exceptions or stuck controls.
- Post-audit checks target the repairs only: post-audit/, layers/, phone/, flow/, ladder/, tag/ and lcd/. No second audit.
- Phone measurement completion transfers focus to choice-0 with scrollY 0; mode changes restore panel scroll to 0,
  and Clear returns focus to the first case. Original failed focus and queue checks are retained as historical evidence.
- Final tool console is clean. The early generic host's favicon 404 was outside the tool; the later host is clean.
- All Chrome/server processes started for the build were closed. Temporary tools/ph-mystery-liquids/host.html removed.

## Frames looked at
- bar/: Snowy Mail Route and Beat Lab. first/: laptop, preview, spill and Bench.
- late/: all seven desktop/preview sizes, C2 evidence, spill end, calm, grayscale and all five food paintings.
- phone/: bench first viewport and labels/notebook after scrolling. last/: completed C2 preview, spill preview,
  spill laptop, final laptop, extreme dilution and wrong-voice frame. Walk C1 and side frames also inspected.
- All 57 audit PNGs inspected on 15 contact sheets, with full-size frame checks for confirmed leads.
- Additional final frames: post-audit/ (six), layers/ (four), phone/phone-c1-final through phone-c3-final,
  flow/ (three), ladder/ladder-final, tag/extreme-tag-final and lcd/lcd-final. All were opened and inspected.

## Art made
- Seventeen new built-in image-tool paintings plus the retained prep room. Prompts, provenance and raw PNGs retained.
- Eighteen finished images total about 219.7 KiB. Voice recordings: 0 KiB. Final bundle: 411.4 KiB.
- No redraws; tester cutout was reprocessed to reduce key-color spill. Final images and contact sheet inspected.

## Art still to paint
None. No people assets are planned or missing.

## Engine changes wanted
None. Shared kit, scripts and catalog were not edited.

## Left open
- Complete HS-PS1-2 mapping needs an owner decision outside this tool's allowed write scope.
- Browser speech is the required unrecorded fallback; bank timbre needs a later recording stage.
- The deliberately simplified chemistry is documented, not claimed as real spill-cleanup guidance or complete equilibrium chemistry.
- Workflow exceptions: initial read-only bootstrap commands lacked explicit termination wrappers. Reference preparation
  regenerated ignored Snowy Mail Route and Beat Lab bundles outside the narrower write boundary; no reference source changed.
- No full audit rerun after narrow repairs, as CODEX-BUILD requests. Original audit and targeted repair evidence are retained.
