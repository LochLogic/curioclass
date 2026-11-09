# Codex review: ph-mystery-liquids
Held: C1's prescribed feedback still permits an elimination solve; the curriculum mapping also remains unresolved.
## Played
- Cold Grade 10 solo run before builder notes/source: C1 identification, C2 evidence and wrong choices, C3 reporting/graph and wrong choices, Bench. Tactile lab, strong central beaker; repeated dosing is the slow stretch.
- Also checked projector/preview use, the complete keyboard C1 path and every required size. Early harness-ID frames were invalidated and replaced.
## Findings fixed
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
## Findings left
- **blocker, general, C1 feedback:** a full test sweep followed solely by green/cross marks closes C1 in 14 checks without reading results (`review-c1-sweep-results.json`). The spec requires individual right/wrong marks and freely revisable labels. Removing that oracle or adding a reasoning gate would change the mandated interaction, so it stays flagged rather than silently changing the spec.
- **should fix, general, curriculum mapping:** full HS-PS1-2 electron/periodic-trend explanation is absent. Moving the shared module code exceeds the authorized folders; notes/handoff explicitly disclaim full coverage.
- **spec limitation:** fixed buffers, residual-acid pH during soda addition and extreme dilutions are instructional approximations. A full equilibrium titration would change the spec. Added an on-screen explanation of the omitted acetate buffering.
## Break it
- C1: exact answer key without tests fails; methyl orange on every bottle fails; discriminating observations plus correct labels pass. New shelf clears labels, evidence and completion. Locked pH meter gives no reading.
- C1's specified right/wrong revision remains an answer route after a full test sweep: 14 feedback checks closed it, including the final post-fix rerun. This unresolved blocker is distinct from the blocked no-test and copied-Bench-order routes; see Findings left.
- C2: 0.1 g dumped into HCl earns no endpoint; 0.003 g remains acidic and 0.004 g exhausts it. Vinegar's first milligram endpoint is 0.700 g, not 0.699 g.
- C2: clicking all explanations, re-reading retained dilutions after a wrong answer, and measuring a vinegar-treated sample cannot close the case after the repairs. Fresh experimental retries remain possible.
- C3: dosing before reporting changes neither dose nor graph. Coarse sweeping cannot close it. A wrong answer followed by a token dose/right choice fails; reset/report/new fine crossing is required.
- Progress is three case acknowledgments, with no points, percent, best score or reflection assuming an unmade mistake. Single-choice guessing still has ordinary chance; cycling cannot bypass experiments.
- Live fresh-liquid check: 47/47 pH, indicator and bulb assertions. Before/after exploit results and independent calculations are saved in Scratch.
## Voice walk
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
## Facts checked
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
## Sensitivity
- None culturally: no peoples, traditions, religion, bodies or hard history. The intentionally deserted lab needs no people assets. Safety review should preserve the distinction between virtual tests and real teacher-directed spill response.
## Flattest moment left
- The early coarse additions in C3 are still repetitive. Their quantity controls and the later precision crossing are specified; no shortcut/new mechanic was added. C2's measured comparison now makes its payoff more visible.
## Graphics
- All 18 assets inspected; no missing art tokens, people or painted lettering. Built-in imagegen repaired `art/raw/phm-beaker.png` and `art/phm-beaker.webp`, processed with art.py --rekey; full prompt in `art/prompts.json`. Other strong paintings retained. Final bundle 461,889 bytes, about 451 KiB, without recorded audio.
- All standard sizes inspected once, plus targeted repairs, grayscale, Motion off and 375-pixel iframe. Targeted notebook, 680x425 active choices, colored-paper/clear-liquid, native drag and denied-storage checks passed. Contrast: ink/brand 7.43:1, notebook text 11.13:1, bottle labels 16.63:1. Existing bar-tool frames inspected; `review-feel-comparison.jpg` preserves the comparison without rebuilding another tool.
## Audit
- One final audit completed within its 40-minute limit: `_scratch/ph-mystery-liquids/review-audit/audit.md`, 56 leads. Inspected all 66 audit frames, including ten full phone frames. Resize stress, Motion off, held/repeated/rapid inputs and focus checks completed without exceptions or stuck controls.
- Of 21 below-fold leads, 20 concern intentionally scrollable Model & safety notes/Clear; the remaining inactive phone explanation was fixed. All 12 short-panel warnings concern those secondary controls. Of ten keep-region leads, nine hit transparent noninteractive art and one is a reachable phone notebook. Two six-pixel overlaps are transparent bottle-hitbox tails, clear of bottle labels. Eleven welcome flags are direct first taps with their own current case/mode guidance, as BASELINE permits; no late welcome plays.
- The audit also exposed the distorted portrait tray; fixed and re-shot all seven standard desktops plus the phone. Post-audit evidence: `review-post-audit/` (12 frames), `review-bench-order-result.json`, `review-phone-retry-focus.json`. All tray ratios match 500:202; the 4.201 g endpoint remains pH 8.35. Phone ready/retry transitions and focus pass.
- Final 375-pixel HTTP iframe checks of C2/C3 have zero console errors (`review-http-final/`). Added an inline empty favicon to eliminate the incidental favicon request. Final JavaScript syntax, art references and number/contrast checks pass. No second full audit or polish round.
- Closed all used Chrome debug ports (9960, 9961, 9962, 9964, 9966), verified host 8765 stopped, and removed the temporary tool host. Cleanup evidence: `review-cleanup-results.json`. Scratch preserves failed attempts and verified replacements.
## Left open
- C1's feedback-oracle blocker needs a spec change. The authorized option was to preserve the explicitly required revision behavior and disclose the consequence. No request for an unattended answer was made.
- Unattended choices follow the spec: retain the named bulb thresholds, finest 0.001 g step, simplified chemistry and freely revisable per-bottle marks. Their limitations are explicit in notes/handoff; no new mechanism or topic was introduced.
- Shared curriculum mapping and the spec's simplified chemistry, as above. Browser narration uses fallback speech; firm-captain bank recordings remain a later recording-stage task.
- Some large browser batches failed at the driver/Chrome connection. One smaller numerical retry passed 47/47. Failed runs are retained and never counted as passes.
- Initial read-only bootstrap commands lacked explicit timeout wrappers. Subsequent bundle/drive/audit processes use the required bounds. No commits or intentional writes outside the two allowed folders.
