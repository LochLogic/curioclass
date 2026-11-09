# Codex report: punnett-predictor

## Built
Built only in the authorized tool and Scratch folders from S:\CurioClass-codex. No git commits, no polish round.
Three working modes, 20 painted assets, the kit frame and voice queue, graphing Plane, seeded gamete sampling, interruptible breeding and meiosis, seven historical datasets and linked flies.
Genetics and probability engines are absent, so exact model functions live in src.html. Shared files were not changed.

## Numbers check
Evidence: calc_spec.py, numbers.json and model-tests.cjs in Scratch.
Seven chi-squares: .262880, .014999, .390743, .063506, .450575, .349650, .606516. Their rounded spec values all match.
Two-gene total 556, chi-square .470023981. Fly total 2300, chi-square 1002.646957, recombinant fraction .17.
SD at n=1000 is .013693064; exact probability outside [.70,.80] is .000228222. Seeded 20,000-run checks reject 5.365% at n=1000 and 5.095% at n=100.
Critical values from scipy agree with NIST. Minimum fair samples: 20 for 3:1 and four equal types, 10 for 1:1, 80 for 9:3:3:1. Play lasts 18 s.
No conflicting numerical answers. Displayed percentages are rounded; calculations use unrounded probabilities.

## Facts checked
- One allele per parent, two divisions after one DNA copy, haploid products, homologs versus sister chromatids: OpenStax Biology 2e 11.1, https://openstax.org/books/biology-2e/pages/11-1-the-process-of-meiosis (opened during build).
- Independent assortment, linkage, recombination, map units and the 50% limit: OpenStax Biology 2e 13.1, https://openstax.org/books/biology-2e/pages/13-1-chromosomal-theory-and-genetic-linkage (opened during build).
- Complete dominance and squares: OpenStax Biology 2e chapter 12, https://openstax.org/books/biology-2e/pages/12-introduction, as named in spec; exhaustive model checks cover all selectable crosses.
- Historical seven traits and counts: Mendel (1866), spec transcription, http://www.mendelweb.org/Mendel.html. Live source timed out; counts retained exactly and arithmetic checked. This is a provenance limitation.
- Fly labels and counts 965, 944, 206, 185: spec attribution to Campbell Biology 12th ed. 15.3. Edition unavailable; labeled Morgan-style, not original Morgan observations. B/b and V/v are simplified classroom symbols.
- Chi-square cutoffs and upper-tail interpretation: NIST table, https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm (opened during build).
- Sample spread, expected counts, ratios, df and fit status: independent Python/scipy computations and Node assertions above. A fit is compatibility, not proof or a claim of causation.
- Many-gene/environment and multiple-crossover model limits: OpenStax chapters 12-13 and the spec's required limits line, shown in the tool and notes.
- Parent pea pictures, four fly looks and seven trait forms checked visually against spec descriptions. All art contains no people.

## Break it
No points, best scores, completion badges or reflection gates are implemented. The fit is a statistical readout, not an earned achievement.
Tried testing 0, 10 and 19 offspring for a 3:1 prediction: refused; n=20 allowed. Tested 79/80 for 9:3:3:1 and 10 for 1:1. Tried deterministic RR x RR: nothing to test, no false success.
Tried preserving a favorable fit while changing parents, seed, gene count, trait, linkage model or crossing over: brood and fit reset. Mode switches preserve each mode's own brood, not a mixed sample.
Tried sweeping crossing over: prediction changes and brood clears on every move. At zero no recombinant offspring occur; at 50 all four probabilities are .25. There is no persistent reward to farm.
Tried repeated Breed while a tally runs, Clear during tally, parent edit during tally and modes during tally: no stale count restoration. Cap remains 10,000; only first 100 images are drawn.
Model evidence: 11 groups passed, including 81 two-gene crosses, 18 one-gene crosses, all 51 linkage rates, seed reproducibility and cap tests. Browser evidence: 35 passing assertions, no tool console errors.
Invalid seeds (negative, fractional, empty and above uint32) are rejected. Opening the linked model clears the independent brood; reopening that unchanged model preserves it. Male meiosis offers no female crossover slider. Zero-recombination headers visibly say 0%.

## Voice walk
Main held-click path at 2 s pace heard welcomeCross, openSquare, breedHow, fitYes, welcomeMendel, welcomeLinked. Welcome cuts on active input are expected.
An initial queued settle line was lost behind breedHow. Fixed it to start at the event; the focused rewalk heard openSquare, breedHow, settle, fitYes in order.
Five repeated open/close actions: openSquare once and breedHow once. Five fit tests: fitYes started five times. Slider side path heard crossing once across repeated arrow moves.
Keyboard-only main path opened meiosis, reached step 6, escaped and bred 1,000. Read uses the current hint via the kit.
Voice files declare friendly-dad; no recording was made, per Build brief. Browser speech fallback is in use. Long lines can be interrupted by later meaningful actions; recordings still need a cold voice review.

## Feel check
Best moment: the tray becomes 100 individual specimens while the Converge line settles near .75, then the fly data break the independent model.
Two flattest moments: sparse early tray and tiny compact meiosis labels. Added a breathing painted specimen in the empty tray and changed the filled tray to 20 columns by 5 rows; enlarged compact chromosome allele labels.
Compared first-wide and voice-fix with bar-beat and bar-snow, then inspected feel-comparison.jpg with final fly art beside Beat Lab. This keeps the serious grade 9 workbench while giving specimens real light, texture and shape. The larger square and neutral-wing redraws carry the visual identity.
The later session changes the explanation: one gene, two independently assorting genes, historical samples, then an independent model that fails for linked genes. The student's own brood and fit are the payoff; there is no artificial score.

## Done when
1. PASS: 2 by 2 predicts 3:1 and 4 by 4 predicts 9:3:3:1. Exhaustive parental-pair tests and painted square frames.
2. PASS: four haploid products per parent; product links return focus to the matching header. Browser assertion and keyboard path.
3. PASS: seed 1 gives 757 round and 243 wrinkled, share .757. Converge targets .75 and its reveal follows displayed N through resize and cancellation.
4. PASS: all seven rows, both painted forms and rounded chi-squares match; two-gene statistic displays .470. Numbers script, browser and Mendel frames.
5. PASS: independent-model fly chi-square 1002.6; 17 gives 41.5/41.5/8.5/8.5; 50 gives 25 each. Exact tests and linked frames. Wording says rare by chance, not impossible.
6. PASS: any expected count below 5 blocks fit; deterministic cross says nothing to test. Boundary and cheat tests.
7. PASS: at 1366x768 and 680x425, Cross/Linked squares or chromosomes dominate; Mendel's table dominates. Inspected audit and post-fix frames.
8. PASS: Next, Back and Close cancel Play synchronously; Clear cancels tally immediately. Browser assertions and native input frames.
9. PASS: native keyboard path, all-size audit plus targeted fixes; 375-wide 4 by 4 fits. Phone Breed/Clear/Test dock and tablet Clear are visible and usable.
10. PASS on required held-click walks: how lines once per five repeated actions; fitYes five starts per five tests. Rapid replacement can interrupt a how line; Read remains available (audit disposition below).
11. PASS: 20 images decode, no people, self-contained bundle, no automatic external URLs, no em dashes. Receipt plus browser frames. Citation links in documentation are not runtime fetches.

## Wave lessons
1. Hint and voice: PASS on required main/side paths; hints update synchronously, Read speaks them, V.heard controls how lines. Lost settle fixed and rewalked. Quick replacement limitation below.
2. Focus and layout: PASS: no autofocus on load; native keyboard path and audit focus checks. Meiosis returns to its header. Hint reserved; overlap fixes inspected.
3. Sizes: PASS: all STANDARDS sizes audited once; phone independently hosted and native tapped. Targets at least 44 px; compact and tablet controls rechecked.
4. No giveaways: PASS, not a hidden-answer game. Sweeping sliders changes an explicitly visible model and clears its sample. No badges or saved score.
5. Honest numbers: PASS: expected model, N, percentages, df and compatibility limits are shown. Linked weights, repeated male headers and zero-probability columns are explicit.
6. Standards: FAIL for full HS-LS3-2 coverage: meiosis is taught; replication errors/mutations intentionally remain in Protein Factory, per spec's leaning. Family doc/engines are missing. Other specified inheritance/probability activities work.
7. Motion off: PASS: no running animations in calm frame; specimens and chromosomes remain readable; Play keeps six three-second beats.
8. Short choices visible: PASS after sticky control and phone dock fixes; all parent choices and 16 square cells fit. Historical seven-row table remains the dominant selectable region.
9. Resize mid-animation: PASS: audit stress clean, plus targeted tally/Converge resize tests preserve progress and controls.
10. No late welcome: PASS: mode-local welcome, no welcomeAfter. First meaningful action can replace welcome per BASELINE 16.
11. Unknown as unknown: PASS: empty brood has an instruction and 0 offspring, not fabricated observations; prediction and real data are labeled separately.
12. One look, one meaning: PASS: specimen art consistently encodes phenotype; parental and recombinant combinations are named; muted zero columns explicitly state 0%.
13. Badge truth: PASS: no achievement badge; fit is compatibility and no-test reasons remain explicit. Labels follow current model.
14. Hint restores with state: PASS: mode/parent/seed/slider/reset/close updates tested; Clear restores empty-brood hint and cancels old work.
15. No copying answer words: PASS, not a diagnosis quiz. Probability and data remain visible working instruments, not a rewarded answer-selection gate.

## Audit leads
One final audit ran once, finished within 40 minutes, exit 0, 78 frames, 8 declared states, 44 leads. Evidence is Scratch audit/audit.md and audit-contacts-final/manifest.json.
It audited a pre-fix snapshot. Do not call the final artifact audit-clean. Final changes have targeted functional/layout evidence, not a second full audit.
- Empty tray instruction/total overlaps at 680, 800, 1000: FIXED, hide first-100 badge while empty; post-frames.
- Test cut short in Cross at 680 and 1000, Linked at 760, and two-genes/two-orientations/linked-data/linked-chromosome at 800, 1280, 1366, 760: FIXED, Test moved above tray; sticky controls and targeted frames.
- Thousand state breed region covered at 680 and 1000, six/five controls offscreen: FIXED, sticky Breed/Seed/Test, deliberate result reveal, phone dock. Tablet Clear wrapping discovered and fixed with nowrap compact controls; final tablet-frames verify all controls uncovered.
- Linked testcross phase text overlaps at 760 in Linked, linked-data and linked-chromosome: FIXED, phase text does not wrap mid-genotype; inspected targeted 760 frame.
- Meiosis-last Play/prediction overlap at 680: FIXED, prediction detail hidden while meiosis is open; compact last-step frame.
- Chromosome B/V and b/v overlaps at 680 and 800: FIXED, separate allele baselines, enlarged compact text; targeted linked frames.
- Phone iframe context and missing-hint leads: AUDIT LIMITATION, not a tool missing hint. Independently drove same-origin host at 375, native taps, all three modes, Read and phone action reveals; input/post/tail frames.
- Fourteen first-tap welcomes not heard and three rapid mode welcome cuts: EXPECTED under BASELINE 16, active input replaces welcome. Premise and current instructions remain in hint/Read; no late queued welcome.
- Rapid repeated Open how line cut: LEFT OPEN for cold voice review. A replacement view can interrupt the once-per-mode line; normal 2-second held-click main path hears it, and Read speaks current instructions. Do not count rapid taps as a fully heard walk.
- Linked-header rebuilt/focus-kept rows: expected model/view transition; Close has focus in the view and product links return to header. Functional and keyboard checks.
- Sound initial width movement: FIXED by starting with the same bell label used by kit toggle.
- Five-click narration checks, Motion off and resize stress were clean in the audit. No tool exceptions or stuck controls.
Audit snapshot SHA256: 33b2dafa711e9a1132efd919cb8181e6b31523af0753844c96f9e3a1c14d9d76.
Final bundle SHA256: f13dd98cc888eaa620d5e384ef21097e9d1f5b546e33182804df61683f1e849f.

## Frames looked at
All 126 PNGs: first-frames (5), target-frames (10), input-frames (10), last-frames (4), audit (78), post-frames (11), tail-frames (6), tablet-frames (2).
All audit PNGs inspected through ten contact sheets with manifest; targeted screenshots individually inspected. Also art sheets, final-size cutouts and final feel-comparison.jpg.
Includes both bar tools, grayscale, Motion off, keyboard, every audit state, 375-wide modes, compact chromosomes, last meiosis step, native phone actions and tablet Clear.
Final source differs after screenshots only by readable HTML paragraph reflow; final receipt verifies the bundled source.
Contrast calculations: brand/panel 13.40:1, ink/panel 14.03:1, muted/panel 8.93:1, selected ink/brand 15.11:1, muted/data card 7.75:1, control border/button 3.93:1.

## Art made
20 final images, 22 generated candidates. The two normal-wing flies were redrawn once to remove pink key spill. Both old candidates are preserved in Scratch. Finished cutouts were made only with art.py --rekey.
Art 370,222 bytes (361.5 KB); bundle 615,331 bytes (600.9 KB), below 2 MB goal. Recorded voice 0 bytes; 28 declared browser-fallback lines. All art assets have people:false.
Four peas, ten plant forms, four flies, wooden seed tray and culture plate. Raw sources and prompts are preserved; illustration credit is in tool.draft.json.

## Art still to paint
None. No people are needed for this specimen-based scene.

## Engine changes wanted
See handoff.md. Missing genetics.js, probability.js and family documentation remain shared-work requests. Existing kit files were untouched.

## Left open
MendelWeb live verification timed out. Campbell edition attribution is unverified. HS-LS3-2 is intentionally taught only for meiosis, with mutation/replication errors left to Protein Factory.
Missing family engines/documentation are worked around locally, not added to shared files. Browser fallback voice needs a cold review when friendly-dad recordings exist. Rapid Open interruption remains as described above.
Cleanup FAIL: all Chrome ports 9970-9977 are closed and host.html is removed, but host 8775 still responds. Windows denied taskkill for exact matched own drive.py host processes, PIDs 15364, 44808, 35032, 19084 at inspection. No unrelated process was killed. Scratch native-host-close.json and validation-receipt.json preserve evidence. This was a runtime permission denial, not automatic approval-review rejection.
No questions were left pending in this unattended run. All spec open-question choices and conflicts are documented in handoff.md. Report drafted in Scratch until delivery to honor the user's immediate stop-on-report instruction, which overrides the brief's early-report location rule.
