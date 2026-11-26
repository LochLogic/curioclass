# pH Mystery Liquids: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: ph-mystery-liquids
#### Built
- Grade 10 chemistry, Cases and Bench, from the kit starter. Three cases, seven liquids, nine tray actions,
  keyboard and drag labels, an observation notebook, live indicator fills, fizz, bulb states and a responsive spill graph.
- Eighteen paintings load: seventeen made during this build and the existing prep room retained. No people.
- Offline HTML, draft stage built, teacher notes, voice manifest, audit states, source and handoff are present.
- No commits, deployment or polish round. Cwd was S:/CurioClass-codex throughout.

#### Numbers check
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

#### Facts checked
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

#### Break it
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

#### Voice walk
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

#### Feel check
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

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
- bar/: Snowy Mail Route and Beat Lab. first/: laptop, preview, spill and Bench.
- late/: all seven desktop/preview sizes, C2 evidence, spill end, calm, grayscale and all five food paintings.
- phone/: bench first viewport and labels/notebook after scrolling. last/: completed C2 preview, spill preview,
  spill laptop, final laptop, extreme dilution and wrong-voice frame. Walk C1 and side frames also inspected.
- All 57 audit PNGs inspected on 15 contact sheets, with full-size frame checks for confirmed leads.
- Additional final frames: post-audit/ (six), layers/ (four), phone/phone-c1-final through phone-c3-final,
  flow/ (three), ladder/ladder-final, tag/extreme-tag-final and lcd/lcd-final. All were opened and inspected.

#### Art made
- Seventeen new built-in image-tool paintings plus the retained prep room. Prompts, provenance and raw PNGs retained.
- Eighteen finished images total about 219.7 KiB. Voice recordings: 0 KiB. Final bundle: 411.4 KiB.
- No redraws; tester cutout was reprocessed to reduce key-color spill. Final images and contact sheet inspected.

#### Art still to paint
None. No people assets are planned or missing.

#### Engine changes wanted
None. Shared kit, scripts and catalog were not edited.

#### Left open
- Complete HS-PS1-2 mapping needs an owner decision outside this tool's allowed write scope.
- Browser speech is the required unrecorded fallback; bank timbre needs a later recording stage.
- The deliberately simplified chemistry is documented, not claimed as real spill-cleanup guidance or complete equilibrium chemistry.
- Workflow exceptions: initial read-only bootstrap commands lacked explicit termination wrappers. Reference preparation
  regenerated ignored Snowy Mail Route and Beat Lab bundles outside the narrower write boundary; no reference source changed.
- No full audit rerun after narrow repairs, as CODEX-BUILD requests. Original audit and targeted repair evidence are retained.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: ph-mystery-liquids
Held: C1's prescribed feedback still permits an elimination solve; the curriculum mapping also remains unresolved.
#### Played
- Cold Grade 10 solo run before builder notes/source: C1 identification, C2 evidence and wrong choices, C3 reporting/graph and wrong choices, Bench. Tactile lab, strong central beaker; repeated dosing is the slow stretch.
- Also checked projector/preview use, the complete keyboard C1 path and every required size. Early harness-ID frames were invalidated and replaced.
#### Findings fixed
- **blocker, general, C2:** retained dilutions could re-enable successive explanation guesses without fresh experiments. Added a per-bottle fresh-sample requirement after an incorrect explanation. Original exploit passes before and fails after.
- **blocker, general, C2:** a vinegar-treated dilution counted as fresh evidence. Reacted samples now require Fresh sample before further tests, dilution or soda; altered readings cannot enter the gate.
- **should fix, general, Bench:** neutralized vinegar still read dim and fresh. Conductivity now retains sodium/counterions, result context says soda-treated, and reselecting a sample states its prior treatment.
- **should fix, general, Litmus paper:** the liquid turned red/blue while the paper stayed white. Color now belongs to the paper; the liquid stays clear.
- **should fix, general, wrong paths:** feedback merely demanded repetition. Each explanation now names the contradictory observation. Empty-label checks no longer claim that nonexistent labels are crossed.
- **should fix, general, voice:** dilution, label selection and overshoot instructions had silent-only text. Added manifest-backed guidance. Teacher reporting, phase changes, label placement and closure stop stale speech; completed-case events start immediately.
- **should fix, general, notebook/layout:** a populated table painted past its shrunken notebook, and keyboard navigation scrolled the hint away. Prevented notebook shrinking/overflow and kept the desktop hint visible with scroll padding.
- **should fix, general, status:** ready C2 choices still said to gather evidence; solved C3 choices still appeared enabled. Both now match their actual state.
- **should fix, general, phone/portrait:** inactive C2 explanations were partly below the phone fold and the spill tray stretched vertically. Hide future explanations until the existing ready phase; preserve the painted tray's 500:202 ratio. Ready choices and failed-answer Fresh sample focus still work.
- **should fix, general, C1 giveaway:** Bench's named bottle order mirrored the default identification key. Bench now follows the spec's Content order. Copying it cannot close C1; the separate correctness-feedback exploit remains below.
- **polish, general, C2:** lifted the flat text-only payoff with paired bars of the student's measured soda additions on one scale. No answer sentence is supplied by the graphic.
- **polish, general, art/motion:** repaired green/magenta beaker fringes with imagegen, preserving glass shape and native alpha. Calm fizz is scattered in place, with its original one-second lifetime.
#### Findings left
- **blocker, general, C1 feedback:** a full test sweep followed solely by green/cross marks closes C1 in 14 checks without reading results (`review-c1-sweep-results.json`). The spec requires individual right/wrong marks and freely revisable labels. Removing that oracle or adding a reasoning gate would change the mandated interaction, so it stays flagged rather than silently changing the spec.
- **should fix, general, curriculum mapping:** full HS-PS1-2 electron/periodic-trend explanation is absent. Moving the shared module code exceeds the authorized folders; notes/handoff explicitly disclaim full coverage.
- **spec limitation:** fixed buffers, residual-acid pH during soda addition and extreme dilutions are instructional approximations. A full equilibrium titration would change the spec. Added an on-screen explanation of the omitted acetate buffering.
#### Break it
- C1: exact answer key without tests fails; methyl orange on every bottle fails; discriminating observations plus correct labels pass. New shelf clears labels, evidence and completion. Locked pH meter gives no reading.
- C1's specified right/wrong revision remains an answer route after a full test sweep: 14 feedback checks closed it, including the final post-fix rerun. This unresolved blocker is distinct from the blocked no-test and copied-Bench-order routes; see Findings left.
- C2: 0.1 g dumped into HCl earns no endpoint; 0.003 g remains acidic and 0.004 g exhausts it. Vinegar's first milligram endpoint is 0.700 g, not 0.699 g.
- C2: clicking all explanations, re-reading retained dilutions after a wrong answer, and measuring a vinegar-treated sample cannot close the case after the repairs. Fresh experimental retries remain possible.
- C3: dosing before reporting changes neither dose nor graph. Coarse sweeping cannot close it. A wrong answer followed by a token dose/right choice fails; reset/report/new fine crossing is required.
- Progress is three case acknowledgments, with no points, percent, best score or reflection assuming an unmade mistake. Single-choice guessing still has ordinary chance; cycling cannot bypass experiments.
- Live fresh-liquid check: 47/47 pH, indicator and bulb assertions. Before/after exploit results and independent calculations are saved in Scratch.
#### Voice walk
- Held 120 ms inputs, two-second pace, default Sound on, in two bounded main-path segments. Main paths used the default OS motion setting; the separate repeat/Read walk explicitly used Motion on.
- C1: c1, labelHow, pickedHow, afterDrops, attachLabel, solved, wBench. First tap opened C1 directly, legitimately skipping wCases. C1 also closed through real Tab/Enter only.
- C2/C3: wCases, c2Tip, pickedHow, diluteHow, freshHow, diluteMeter, explainHow, c2Solved, spillFirst, c3Soda, spillFine, c3Explain, c3Solved, wBench, in that order. Each started once; old lines stopped on the student's relevant next action.
- Side: blank Check gives missingLabels; one intentionally wrong label gives five wrong events from five checks. Read twice, including with Sound off, matches the current hint. All three walks: zero console errors and exact allLines/manifest agreement.
| Line | Kind | Expected | Heard |
|---|---|---:|---:|
| c1 / c2Tip / spillFirst / c3Soda / wBench | how or welcome | 1 per applicable walk | 1 each |
| labelHow / pickedHow / freshHow | how | 1 per applicable walk | 1 each |
| wrong | event | 5 repeated checks | 5 |
| solved / c2Solved / c3Solved | event | 1 on each closure | 1 each |
| Read | read | 2 side actions | 2 |
#### Facts checked
- pH definition, neutral 7 at 25 degrees C and strong-acid dilution: [OpenStax Chemistry 2e 14.2](https://openstax.org/books/chemistry-2e/pages/14-2-ph-and-poh).
- Partial versus full ionization and changing weak-acid ionization on dilution: [OpenStax 14.3](https://openstax.org/books/chemistry-2e/pages/14-3-relative-strengths-of-acids-and-bases).
- Acetic Ka 1.8e-5, carbonic Ka values 4.3e-7/4.7e-11 and boric Ka 5.4e-10: [OpenStax Appendix H](https://openstax.org/books/chemistry-2e/pages/h-ionization-constants-of-weak-acids). Ammonia Kb 1.8e-5: [Appendix I](https://openstax.org/books/chemistry-2e/pages/i-ionization-constants-of-weak-bases).
- Independently recomputed: vinegar 2.413/2.915/3.422; HCl 2.398/3.398/4.398; ammonia 11.125/10.618; bicarbonate 8.347; borax 9.268. Stock concentrations and fixed-buffer behavior are explicit spec inputs, not measured products.
- Indicator color transitions and titration limits: [OpenStax 14.7](https://openstax.org/books/chemistry-2e/pages/14-7-acid-base-titrations). The spec's discrete bands and pale-pink category are simplified representations, not precise laboratory calibration.
- Paper rather than solution changes in a litmus-paper test: [Royal Society of Chemistry](https://edu.rsc.org/experiments/acid-or-alkali-acidic-or-alkaline-a-litmus-paper-test/1708.article).
- Mobile ions conduct and remain as dissolved salts after neutralization: [OpenStax 11.2](https://openstax.org/books/chemistry-2e/pages/11-2-electrolytes). Exact bulb cutoffs are declared model choices; neutralized vinegar now reads bright.
- Acid plus bicarbonate makes salt, water and carbon dioxide: [OpenStax 18.6](https://openstax.org/books/chemistry-2e/pages/18-6-occurrence-preparation-and-properties-of-carbonates). Added soda remaining in a sample also fizzes with vinegar drops.
- Molar mass 84.007 g/mol: [NIH PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/sodium_bicarbonate). Independent stoichiometry: C2 0.699442282/0.00336028 g, ratio 208.15. C3 requires 4.20035 g; modeled pH at 2.10/3.78/4.16/4.20/4.201 g is 0.301/1.000/2.017/4.079/8.35. Rounded 4.2004 g does not mean that 4.200 g is neutral.
- Water/CO2: [US EPA](https://www.epa.gov/acidrain/what-acid-rain) supports about 5.6 for normal rain. Its application to this open distilled-water sample is a model assumption, not a universal water value.
- All five food ranges match [Clemson's current table](https://www.clemson.edu/extension/food/_files/ph-of-common-foods-table.pdf): lime 2.00-2.35, lemon 2.00-2.60, vinegar 2.40-3.40, apple juice 3.35-4.00, tomato juice 4.10-4.60. Variation is stated.
- Goggles, authorized work and immediate spill reporting: [ACS student laboratory code](https://institute.acs.org/acs-center/lab-safety/education-training/high-school-labs/student-lab-code-of-conduct.html). Never tasting/smelling is the spec's conservative rule. No real cleanup or harmless-spill claim is made.
- Bleach incompatibility with acids/ammonia: [Health Canada](https://www.canada.ca/en/health-canada/services/home-safety/household-chemical-safety.html). The shelf contains no bleach.
- Full standard requires electron states and periodic trends: [NGSS HS-PS1-2](https://www.nextgenscience.org/search-standards?keys=HS-PS1-2); this tool does not teach those parts.
#### Sensitivity
- None culturally: no peoples, traditions, religion, bodies or hard history. The intentionally deserted lab needs no people assets. Safety review should preserve the distinction between virtual tests and real teacher-directed spill response.
#### Flattest moment left
- The early coarse additions in C3 are still repetitive. Their quantity controls and the later precision crossing are specified; no shortcut/new mechanic was added. C2's measured comparison now makes its payoff more visible.
#### Graphics
- All 18 assets inspected; no missing art tokens, people or painted lettering. Built-in imagegen repaired `art/raw/phm-beaker.png` and `art/phm-beaker.webp`, processed with art.py --rekey; full prompt in `art/prompts.json`. Other strong paintings retained. Final bundle 461,889 bytes, about 451 KiB, without recorded audio.
- All standard sizes inspected once, plus targeted repairs, grayscale, Motion off and 375-pixel iframe. Targeted notebook, 680x425 active choices, colored-paper/clear-liquid, native drag and denied-storage checks passed. Contrast: ink/brand 7.43:1, notebook text 11.13:1, bottle labels 16.63:1. Existing bar-tool frames inspected; `review-feel-comparison.jpg` preserves the comparison without rebuilding another tool.
#### Audit
- One final audit completed within its 40-minute limit: `_scratch/ph-mystery-liquids/review-audit/audit.md`, 56 leads. Inspected all 66 audit frames, including ten full phone frames. Resize stress, Motion off, held/repeated/rapid inputs and focus checks completed without exceptions or stuck controls.
- Of 21 below-fold leads, 20 concern intentionally scrollable Model & safety notes/Clear; the remaining inactive phone explanation was fixed. All 12 short-panel warnings concern those secondary controls. Of ten keep-region leads, nine hit transparent noninteractive art and one is a reachable phone notebook. Two six-pixel overlaps are transparent bottle-hitbox tails, clear of bottle labels. Eleven welcome flags are direct first taps with their own current case/mode guidance, as BASELINE permits; no late welcome plays.
- The audit also exposed the distorted portrait tray; fixed and re-shot all seven standard desktops plus the phone. Post-audit evidence: `review-post-audit/` (12 frames), `review-bench-order-result.json`, `review-phone-retry-focus.json`. All tray ratios match 500:202; the 4.201 g endpoint remains pH 8.35. Phone ready/retry transitions and focus pass.
- Final 375-pixel HTTP iframe checks of C2/C3 have zero console errors (`review-http-final/`). Added an inline empty favicon to eliminate the incidental favicon request. Final JavaScript syntax, art references and number/contrast checks pass. No second full audit or polish round.
- Closed all used Chrome debug ports (9960, 9961, 9962, 9964, 9966), verified host 8765 stopped, and removed the temporary tool host. Cleanup evidence: `review-cleanup-results.json`. Scratch preserves failed attempts and verified replacements.
#### Left open
- C1's feedback-oracle blocker needs a spec change. The authorized option was to preserve the explicitly required revision behavior and disclose the consequence. No request for an unattended answer was made.
- Unattended choices follow the spec: retain the named bulb thresholds, finest 0.001 g step, simplified chemistry and freely revisable per-bottle marks. Their limitations are explicit in notes/handoff; no new mechanism or topic was introduced.
- Shared curriculum mapping and the spec's simplified chemistry, as above. Browser narration uses fallback speech; firm-captain bank recordings remain a later recording-stage task.
- Some large browser batches failed at the driver/Chrome connection. One smaller numerical retry passed 47/47. Failed runs are retained and never counted as passes.
- Initial read-only bootstrap commands lacked explicit timeout wrappers. Subsequent bundle/drive/audit processes use the required bounds. No commits or intentional writes outside the two allowed folders.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### pH Mystery Liquids handoff

Build only, 2026-11-05. No commits, deployment or polish round.

#### Structure
`src.html` follows the kit starter with curio.css, theme-912.css and Curio.voice. Its own CSS provides three responsive
layouts without scaling the entire scene. The instrument heights follow the bottle's 20 cm reference, while the
test beaker is deliberately enlarged as the teaching focus. Tests and shelf controls stay stable during updates.
Only case changes rebuild the case card and shelf. The notebook is an observation grid with its own scroll area.

The source contains LIQUIDS, the quadratic equilibrium calculation, the ion-threshold bulb model, the sample state,
the three case controllers and the graph renderer. `window.__tool` exposes the specified API plus pure model helpers,
allLines and vlog. Acid samples store integer milligrams, avoiding cumulative button-rounding errors.
Bench bottle hooks accept named liquid ids or A through G in LIQUIDS order. Soda hooks accept the three UI increments;
batch checks repeat those increments so their graph points match actual student actions.
The spill graph uses real viewport coordinates and redraws on resize. Bubbles never lock an input.
Glass and instrument art ignore pointer input. Bottle images sit behind the beaker, with readable code labels above
the glass. Hit-test-based keep-region checks can call these transparent, noninteractive art regions covered.
On phones the C1 labels fit the first viewport; C2 replaces the tray with the explanation after measurements.
Focus is captured before that layout change and deliberately transferred with preventScroll. A failed explanation
restores the tray and focuses Fresh sample. Secondary notes, the reference ladder and device controls may scroll.

Eighteen WebPs are referenced through art tokens. Seventeen new paintings were generated with the built-in image tool;
the existing prep-room painting is retained. Prompts and originals are preserved. Every asset has people:false.
The source is readable, not minified. The generated offline HTML is ignored by git. Metadata stays tool.draft.json.

#### Case gates and adversarial choices
C1 checks identity and whether the actual observations distinguish that liquid from all other shelf candidates.
Correct labels without discriminating test evidence do not close the case. Wrong labels remain freely revisable as
the spec requests. New shelf clears labels, observations, evidence and C1 completion, and changes the seeded key.

C2 requires precise soda endpoints on fresh undiluted samples and meter readings of both fresh tenfold dilutions.
Overshooting the first usable endpoint does not earn the measurement. A wrong explanation clears the dilution
evidence, so pressing each answer in turn cannot close the case without a new experiment.

C3 requires the teacher report and a graph interval crossing the acid endpoint using the 0.001 g step.
A coarse sweep to excess soda cannot earn the reasoning gate. A wrong explanation requires Reset spill, another
teacher report and a new graph before another answer. These gates address the brief's explicit anti-cheat requirement.
Closed cases are progress acknowledgments, not grades, points or evidence of full standard mastery.

#### Open questions settled
1. Keep the supplied HS-PS1-2 mapping as context, but explicitly document that the complete electron/periodic-trend
   standard is not taught. Do not claim full coverage. Changing the shared module is outside this build's write scope.
2. Keep the specified dark/dim/bright thresholds. Name them as a model on screen and explain the ion-mobility limit.
3. Keep 0.001 g as the finest step. The spill cannot land on pH 7 with those steps; its sharp jump is the point.
4. Use the image tool, as the user requires, in place of the older spec instruction to use local FLUX. No people
   are needed in this deserted room, so retain the spec's people-free scene rather than adding portraits.
5. Follow the precise spec chemistry rather than expanding to a full titration simulator. Teacher notes name the
   acetic acid/acetate and fixed-buffer limitations. "Harmless" is not presented as a real cleanup safety claim.
6. Use 84.007 g/mol for bicarbonate consistently. C3's unrounded need is 4.20035 g; the spec's 4.2004 g is rounded.
   This reproduces its pH 4.08 at 4.200 g. Displayed C2 reference amounts remain the requested rounded values.
7. The old Clemson food PDF URL redirects. The verified current table is
   https://www.clemson.edu/extension/food/_files/ph-of-common-foods-table.pdf . All five ranges match.
8. No audio was recorded, following CODEX-BUILD. The firm-captain/Alnilam bank is in lines.json; browser speech is
   used now. That fallback cannot guarantee the specific bank timbre.
9. The user says to stop when codex-report.md is written, while CODEX-BUILD asks for an early report. Keep interim
   evidence in Scratch and write the deliverable report only after checks, immediately before stopping.
10. Repeated dilution eventually makes the bare strong-acid formula predict an alkaline acid sample. Preserve all
    specified readings and include water autoionization at extreme strong-acid dilution. Weak quadratics are floored
    at neutral; those extremes are illustrative, not complete equilibrium calculations. This is documented in notes.

#### Sensitivity
No people, bodies, cultural traditions, religion or hard history appear. Chemical handling safety is relevant.
Review the distinction between a teacher-gated virtual drill and instructions for responding to a real spill.

#### Engine changes wanted
None. Shared kit, scripts and catalog files were not edited.

#### Evidence and limits
Scratch is `S:/CurioClass-codex/_scratch/ph-mystery-liquids`. It contains independent number calculations, image
provenance, rendered frames, browser input walks, adversarial assertions and the single mechanical audit.
See codex-report.md for final results and every outstanding item. Chrome uses assigned ports and mute-audio.
The phone host uses 8795 and stops after its shots. All shell commands after the initial read setup use run.py limits.

Reference preparation accidentally regenerated the ignored bundle outputs for snowy-mail-route and beat-lab while
following CODEX-BUILD's reference instruction. This exceeded the user's narrower write boundary. No reference
sources were changed, and the generated outputs were left intact rather than making further out-of-scope changes.

#### Cold review, 2026-11-07
Review commands use Chrome 9960, 9961, 9962, 9964 and 9966 and host 8765. Changes stay in this tool and its Scratch folder.
The beaker was repaired with built-in imagegen and processed with art.py --rekey. Its native alpha is preserved
by cutout:false plus native_alpha:true in prompts.json; it is still a transparent cutout asset.
The C2 comparison on the bench uses measured endpoints on a shared scale. It appears only after both measurements.
C2 retryNeeded requires Fresh sample on both bottles after a wrong explanation; stored diluted samples cannot
re-arm the explanation buttons. A vinegar-drops sample refuses later tests and soda until refreshed.
Acid-plus-soda conductivity retains sodium and counterions. Retained samples are explicitly named when reselected.
Wrong explanations now name the contradictory observation. Added next-action lines are in the voice manifest.
The spill's soda how-to stays valid after early additions so it can start at the normal two-second tap pace.
Full HS-PS1-2 mapping remains outside this tool's authorized write boundary. No new curriculum topic was added.

Additional cold-review repairs: the notebook no longer shrinks beneath its table; the desktop hint is sticky with
scroll padding. Litmus colors a masked paper overlay rather than the sample. Vinegar drops detect excess added
bicarbonate as well as the stock baking soda solution. Empty checks ask for missing labels. Voice phase changes
and successful/failed explanations hush obsolete instructions before starting the current line. The audit now
includes a full notebook, an active C2 explanation, the measured comparison and litmus-paper states.

#### Unresolved cold-review blocker: C1 feedback
The independent reviewer swept every test without interpreting its values, then assigned labels using only the
right/wrong marks. This closes C1 in 14 checks. See Scratch/review-c1-sweep-results.json and its drive frame.
The spec explicitly requires individual correctness marks and free label revision. Removing those marks or adding
a reasoning gate would change the specified interaction; that change was not made in this scoped review.
Do not describe C1 completion as evidence of independent identification mastery.

The single final audit confirmed a partial inactive explanation set below the phone fold. On phones,
C2 now shows that set only when usable; the existing phase/focus transition is unchanged. Its portrait frames
also confirmed a stretched spill tray. The painted tray now keeps its native 500:202 aspect ratio.
Bench now follows the spec Content order, so its named bottles do not mirror the default C1 answer key.
Named bottle hooks are unchanged; the old A-G Bench aliases retain LIQUIDS order for compatibility.
The separate C1 feedback-elimination blocker remains, as documented above.

The single review audit finished with 56 leads. All 66 audit frames were inspected; confirmed repairs were re-shot
without a second full audit. Twelve targeted post-audit frames check the tray at all standard sizes, phone C2
ready/retry transitions and the Bench order. Final C2/C3 HTTP phone frames have no console errors. The source has
an inline empty favicon. Review Chrome/debug ports and host 8765 are closed; the temporary host was removed.
See codex-review.md for the cold review's findings, named sources, exploit outcomes and remaining blocker.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
