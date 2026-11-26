# Punnett Predictor: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: punnett-predictor

#### Built
Built only in the authorized tool and Scratch folders from S:\CurioClass-codex. No git commits, no polish round.
Three working modes, 20 painted assets, the kit frame and voice queue, graphing Plane, seeded gamete sampling, interruptible breeding and meiosis, seven historical datasets and linked flies.
Genetics and probability engines are absent, so exact model functions live in src.html. Shared files were not changed.

#### Numbers check
Evidence: calc_spec.py, numbers.json and model-tests.cjs in Scratch.
Seven chi-squares: .262880, .014999, .390743, .063506, .450575, .349650, .606516. Their rounded spec values all match.
Two-gene total 556, chi-square .470023981. Fly total 2300, chi-square 1002.646957, recombinant fraction .17.
SD at n=1000 is .013693064; exact probability outside [.70,.80] is .000228222. Seeded 20,000-run checks reject 5.365% at n=1000 and 5.095% at n=100.
Critical values from scipy agree with NIST. Minimum fair samples: 20 for 3:1 and four equal types, 10 for 1:1, 80 for 9:3:3:1. Play lasts 18 s.
No conflicting numerical answers. Displayed percentages are rounded; calculations use unrounded probabilities.

#### Facts checked
- One allele per parent, two divisions after one DNA copy, haploid products, homologs versus sister chromatids: OpenStax Biology 2e 11.1, https://openstax.org/books/biology-2e/pages/11-1-the-process-of-meiosis (opened during build).
- Independent assortment, linkage, recombination, map units and the 50% limit: OpenStax Biology 2e 13.1, https://openstax.org/books/biology-2e/pages/13-1-chromosomal-theory-and-genetic-linkage (opened during build).
- Complete dominance and squares: OpenStax Biology 2e chapter 12, https://openstax.org/books/biology-2e/pages/12-introduction, as named in spec; exhaustive model checks cover all selectable crosses.
- Historical seven traits and counts: Mendel (1866), spec transcription, http://www.mendelweb.org/Mendel.html. Live source timed out; counts retained exactly and arithmetic checked. This is a provenance limitation.
- Fly labels and counts 965, 944, 206, 185: spec attribution to Campbell Biology 12th ed. 15.3. Edition unavailable; labeled Morgan-style, not original Morgan observations. B/b and V/v are simplified classroom symbols.
- Chi-square cutoffs and upper-tail interpretation: NIST table, https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm (opened during build).
- Sample spread, expected counts, ratios, df and fit status: independent Python/scipy computations and Node assertions above. A fit is compatibility, not proof or a claim of causation.
- Many-gene/environment and multiple-crossover model limits: OpenStax chapters 12-13 and the spec's required limits line, shown in the tool and notes.
- Parent pea pictures, four fly looks and seven trait forms checked visually against spec descriptions. All art contains no people.

#### Break it
No points, best scores, completion badges or reflection gates are implemented. The fit is a statistical readout, not an earned achievement.
Tried testing 0, 10 and 19 offspring for a 3:1 prediction: refused; n=20 allowed. Tested 79/80 for 9:3:3:1 and 10 for 1:1. Tried deterministic RR x RR: nothing to test, no false success.
Tried preserving a favorable fit while changing parents, seed, gene count, trait, linkage model or crossing over: brood and fit reset. Mode switches preserve each mode's own brood, not a mixed sample.
Tried sweeping crossing over: prediction changes and brood clears on every move. At zero no recombinant offspring occur; at 50 all four probabilities are .25. There is no persistent reward to farm.
Tried repeated Breed while a tally runs, Clear during tally, parent edit during tally and modes during tally: no stale count restoration. Cap remains 10,000; only first 100 images are drawn.
Model evidence: 11 groups passed, including 81 two-gene crosses, 18 one-gene crosses, all 51 linkage rates, seed reproducibility and cap tests. Browser evidence: 35 passing assertions, no tool console errors.
Invalid seeds (negative, fractional, empty and above uint32) are rejected. Opening the linked model clears the independent brood; reopening that unchanged model preserves it. Male meiosis offers no female crossover slider. Zero-recombination headers visibly say 0%.

#### Voice walk
Main held-click path at 2 s pace heard welcomeCross, openSquare, breedHow, fitYes, welcomeMendel, welcomeLinked. Welcome cuts on active input are expected.
An initial queued settle line was lost behind breedHow. Fixed it to start at the event; the focused rewalk heard openSquare, breedHow, settle, fitYes in order.
Five repeated open/close actions: openSquare once and breedHow once. Five fit tests: fitYes started five times. Slider side path heard crossing once across repeated arrow moves.
Keyboard-only main path opened meiosis, reached step 6, escaped and bred 1,000. Read uses the current hint via the kit.
Voice files declare friendly-dad; no recording was made, per Build brief. Browser speech fallback is in use. Long lines can be interrupted by later meaningful actions; recordings still need a cold voice review.

#### Feel check
Best moment: the tray becomes 100 individual specimens while the Converge line settles near .75, then the fly data break the independent model.
Two flattest moments: sparse early tray and tiny compact meiosis labels. Added a breathing painted specimen in the empty tray and changed the filled tray to 20 columns by 5 rows; enlarged compact chromosome allele labels.
Compared first-wide and voice-fix with bar-beat and bar-snow, then inspected feel-comparison.jpg with final fly art beside Beat Lab. This keeps the serious grade 9 workbench while giving specimens real light, texture and shape. The larger square and neutral-wing redraws carry the visual identity.
The later session changes the explanation: one gene, two independently assorting genes, historical samples, then an independent model that fails for linked genes. The student's own brood and fit are the payoff; there is no artificial score.

#### Done when
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

#### Wave lessons
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

#### Audit leads
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

#### Frames looked at
All 126 PNGs: first-frames (5), target-frames (10), input-frames (10), last-frames (4), audit (78), post-frames (11), tail-frames (6), tablet-frames (2).
All audit PNGs inspected through ten contact sheets with manifest; targeted screenshots individually inspected. Also art sheets, final-size cutouts and final feel-comparison.jpg.
Includes both bar tools, grayscale, Motion off, keyboard, every audit state, 375-wide modes, compact chromosomes, last meiosis step, native phone actions and tablet Clear.
Final source differs after screenshots only by readable HTML paragraph reflow; final receipt verifies the bundled source.
Contrast calculations: brand/panel 13.40:1, ink/panel 14.03:1, muted/panel 8.93:1, selected ink/brand 15.11:1, muted/data card 7.75:1, control border/button 3.93:1.

#### Art made
20 final images, 22 generated candidates. The two normal-wing flies were redrawn once to remove pink key spill. Both old candidates are preserved in Scratch. Finished cutouts were made only with art.py --rekey.
Art 370,222 bytes (361.5 KB); bundle 615,331 bytes (600.9 KB), below 2 MB goal. Recorded voice 0 bytes; 28 declared browser-fallback lines. All art assets have people:false.
Four peas, ten plant forms, four flies, wooden seed tray and culture plate. Raw sources and prompts are preserved; illustration credit is in tool.draft.json.

#### Art still to paint
None. No people are needed for this specimen-based scene.

#### Engine changes wanted
See handoff.md. Missing genetics.js, probability.js and family documentation remain shared-work requests. Existing kit files were untouched.

#### Left open
MendelWeb live verification timed out. Campbell edition attribution is unverified. HS-LS3-2 is intentionally taught only for meiosis, with mutation/replication errors left to Protein Factory.
Missing family engines/documentation are worked around locally, not added to shared files. Browser fallback voice needs a cold review when friendly-dad recordings exist. Rapid Open interruption remains as described above.
Cleanup FAIL: all Chrome ports 9970-9977 are closed and host.html is removed, but host 8775 still responds. Windows denied taskkill for exact matched own drive.py host processes, PIDs 15364, 44808, 35032, 19084 at inspection. No unrelated process was killed. Scratch native-host-close.json and validation-receipt.json preserve evidence. This was a runtime permission denial, not automatic approval-review rejection.
No questions were left pending in this unattended run. All spec open-question choices and conflicts are documented in handoff.md. Report drafted in Scratch until delivery to honor the user's immediate stop-on-report instruction, which overrides the brief's early-report location rule.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: punnett-predictor

#### Played

Cold Grade 9 solo walk, then projector-sized inspection, before opening the builder's report, handoff, notes or source.
Played Cross, both genes, meiosis, breeding and fit, a selected Mendel row and Try this total, then real fly data and chromosomes. Strong specimen bench; the linked-data reversal is the best moment.
Evidence lives in `_scratch/punnett-predictor/`: cold-frames, break-frames, focus-frames, recheck-frames, post-break-frames and phone-frames.

#### Findings fixed

- Blocker, family:genetics, breeder: the one-second reveal interpolated final phenotype totals and left final fractions visible beside partial N. It now reveals actual sampled prefixes, matching counts, fractions and specimen count. The thousand voice event waits for displayed N.
- Should fix, general, compact meiosis: the last-step chromosome art shrank to tiny marks at 680x425. Consolidated its controls and reserved 90 pixels for the scientific drawing; rechecked 680 and 800.
- Should fix, general, Play: automatic steps left the opening hint at the final products. Hints now follow each step and name the gamete links at the end, with unchanged 18-second pacing in Motion off.
- Should fix, general, Mendel bars: the legend relied on color. Added O/E labels, retained both colors and all art, and checked grayscale.
- Should fix, family:genetics, art: both vestigial flies had pink fringes and weak wing stubs. Redrew both from their corresponding normal-wing references, keyed through art.py, and aligned displayed body sizes.
- Should fix, general, voice/access: row selection used an undeclared variable Read hint. Replaced it with a fixed declared how line that starts at selection; the mini-square cells now have keyboard focus and probability labels.
- Should fix, general, phone Mendel: its hint named Try this total while the button was below the page fold. The action now occupies the bottom dock; the seven-row table stays intact. Status also follows the current brood after an interrupted reveal or mode switch.
- Should fix, general, final audit: fixed controls covered results at 680/800/1000 and content at 375. Put desktop results in their own scroller and phone content above the dock. All seven desktop sizes and phone native actions rechecked; full scientific panels remain available.
- Should fix, family:genetics, final audit: compact B/V label boxes touched. Separated their baselines without reducing letters or chromosomes; checked first and final products at 680/800.
- Should fix, general, final audit: two quick taps hushed three mode welcomes and the meiosis how line. Repeated taps now preserve the current panel and speech; all four cases produce one uninterrupted line.
- Polish, family:genetics, flattest moment: Mendel's near-identical bars offered little payoff. Selecting a row now exposes its actual departure from the predicted count, with immediate specimen feedback. Try this total stays above the detail.
- Polish, general: fit copy now states the upper-tail assumption and Motion visibly says its preference stays on device. Sources resolve the previously unchecked datasets.
- Verification caught a first-frame timestamp before the animation start; clamped progress to zero and rechecked 63 frames, with no mismatch or exception.
- The phone recheck caught natural panel growth and a hidden Close at the products step. Explicit square height and a compact scientific-panel grid fixed both; no specimen art was removed.

#### Findings left

- Scope: full HS-LS3-2 is not taught here. Meiosis/recombination are; mutation and replication errors remain with Protein Factory, as the spec directs. Shared catalog/engine edits are outside authorization.
- Production: friendly-dad is declared and kept in the bank, but no recordings exist. Browser fallback timing was tested; the eventual recorded takes still need listening and timing review. Recording was prohibited by the brief.

#### Break it

No score, best score, quiz, reflection gate or mastery badge exists. Fit is model compatibility, not a skill award; no new achievement layer was added.

- Test spam at N=10 for 3:1: five refusals. N=20: five valid fit events, no accumulated reward. Deterministic RR x RR plus Breed 1,000: nothing to test, no false success.
- Cheapest easy-parent route, repeated Breed to the cap, then a parent edit and Test: old fit gone, brood zero. Clear during the reveal stays empty; later callbacks cannot restore it.
- Real pointer sweep of Crossing over from 0 to 50 after breeding: brood and fit clear throughout, ending with four 25% predictions. No slider position earns a completion.
- Boundary checks: 19/20 for 3:1 and four equal types; 9/10 for 1:1; 79/80 for 9:3:3:1. All expected-count gates correct. At zero linkage no recombinant offspring occur.
- All 99 selectable crosses and all 51 linkage rates passed independent probability checks. 10,000 cap, 100 drawn specimens, seed-1 757/243, per-mode brood preservation and invalid seeds checked: 188 assertions.
- Clear repeats the seeded stream, so seed hunting is possible as exploration; notes explicitly say cherry-picking a fit is not evidence. There is no saved success to farm.
- Post-fix replay of all eleven cheat/voice/keyboard cases: zero tool errors. FitNo was also tested five times with a genuinely rare seed-22 brood (19 round, 1 wrinkled, chi-square 4.267).
- Final audit-repair replay: all six cheap routes retain those outcomes; the prefix probe matched 62 further frames. Native phone Breed and Try this total produced 1,000 and 1,064 offspring.

#### Voice walk

Held clicks 0.12 s, default settings, two-second gaps: choose parents, Open the square, five Nexts, Close, Breed 1,000, Test, Mendel, select row, Try this total, Test, Linked genes, Show real data, Chromosome view.
Heard in order: welcomeCross, openSquare, breedHow, settle, fitYes, welcomeMendel, mendelSelected, settle for the new brood, fitYes, welcomeLinked, fitNo. Reopening meiosis keeps openSquare silent because already heard.
Each mode's how-to starts on the main path. Main recheck has no exceptions. Side walk confirms Read interrupts speech, mode change releases Read, and Read works with Sound off.
These are actual line starts in the fallback voice log; later meaningful actions may interrupt stale speech. Quick repetition of the same action now leaves its line whole. Recorded friendly-dad takes remain absent.

| Line | Kind | Expected in five actions | Observed |
|---|---|---|---|
| openSquare / breedHow | how | 1 / 1 | 1 / 1 |
| fitYes / needMore | event | 5 / 5 | 5 / 5 |
| fitNo | event | 5 | 5 |
| mendelSelected | how | 1 | 1 |

#### Facts checked

Checked live 2026-11-08; arithmetic independently recomputed in review_numbers.py and review-numbers.json.

- All seven trait counts/dominance pairs and two-gene counts: [Mendel's primary text, Brown-hosted MendelWeb translation](https://cs.brown.edu/people/rblumber/MendelWeb/Mendel.html). The original MendelWeb host timed out; its mirror resolves verification.
- Seven totals 7,324 / 8,023 / 929 / 1,181 / 580 / 858 / 1,064; ratios 2.96 / 3.01 / 3.15 / 2.95 / 2.82 / 3.14 / 2.84; chi-squares .26 / .01 / .39 / .06 / .45 / .35 / .61: computation against Mendel counts, all below the df=1 cutoff.
- Two genes: total 556; expected 312.75, 104.25, 104.25, 34.75; chi-square .470024: same primary text and independent Pearson calculation.
- Four fly counts 965 gray normal, 944 black vestigial, 206 gray vestigial, 185 black normal: [OpenStax Biology 2e 13.1, Figure 13.3](https://openstax.org/books/biology-2e/pages/13-1-chromosomal-theory-and-genetic-linkage). Total 2,300, recombinants 391/2,300=.17, independent-model chi-square 1002.646957 independently checked. Campbell edition itself remains unchecked; the dataset is verified.
- One allele per parent, genotype versus look, complete dominance, 3:1 and 9:3:3:1, gamete headers: [OpenStax 12.2](https://openstax.org/books/biology-2e/pages/12-2-characteristics-and-traits) and [12.3](https://openstax.org/books/biology-2e/pages/12-3-laws-of-inheritance). Row deviations use N times .75, not rounded ratios.
- DNA copies before two divisions; homologs then sisters separate; haploid products need not all differ; plant gametes form later: [OpenStax 11.1](https://openstax.org/books/biology-2e/pages/11-1-the-process-of-meiosis). Both independent orientations and linked chromatid continuity inspected.
- Nonsister crossing over, linkage, approximate map units and 50% recombinant limit: OpenStax 13.1 above. At d=17, .415/.415/.085/.085; at 0, .5/.5/0/0; at 50, .25 each. Slider means recombinant gamete percentage, not percentage of meioses crossing over.
- df=positive predicted classes minus one, upper-tail 5% values 3.841/5.991/7.815, rare rejection under a true model: [NIST e-Handbook 1.3.6.7.4](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3674.htm). UI uses specified rounded cutoffs. Expected counts at least 5 and minimum N=10 are explicit tool assumptions, not a mastery test.
- At N=1,000 and p=.75, SD=sqrt(.75*.25/1000)=.013693. This supports the stated usual .70 to .80 range; no guarantee is made.
- Many-gene/environment limits: [NIH NHGRI Polygenic Trait](https://www.genome.gov/genetics-glossary/Polygenic-Trait) and [Phenotype](https://www.genome.gov/genetics-glossary/Phenotype). Simplified fly symbols are identified in notes; own diagrams/art do not imply a human identity model.

#### Sensitivity

No culture-specific content, religion, hard history or human-body simulation. Peas and flies are the specimens. Home notes avoid inferring a person's genotype from appearance; retain that qualification in any later edit.

#### Flattest moment left

After the first 100 specimens the tray stops gaining individual images while the tally and chart continue. This is the specified cap, honestly labeled; the student's brood and fit remain the grade-appropriate payoff.

#### Graphics

All 20 finished images inspected at final sizes, and all referenced art loads. No people, missing art or placeholders. Two vestigial flies redrawn using built-in image generation and standard free rekey; no other illustration stripped or simplified.
Compared the final fly bench with Beat Lab; review-bar-comparison.png preserves both. Kept the dark naturalist workbench, large painted peas, textured trays, weighted square and chromosome colors/labels.
Art 367,370 bytes; final bundle 617,081 bytes, below 2 MB. Contrast: brand/panel 13.40:1, ink/panel 14.03:1, muted/panel 8.93:1, callout 8.48:1, selected ink/brand 15.11:1, control border 3.93:1.

#### Audit

The single final audit completed within its 2,400-second limit, Chrome 9941 / host 8745. All 95 frames inspected. No exceptions, lost focus, infinite Motion-off activity or controls stuck after resize; five-click narration checks clean.
Its 112 leads: 89 geometry leads traced to covered content, touching labels, obsolete keep regions and scrollable supplemental content; confirmed obstructions repaired and re-shot. Also: 15 first-action welcome omissions allowed by STANDARDS/BASELINE 16; four intentional focusable static mini-square images; four quick-tap speech cuts fixed and rechecked. Native Tab proves access to supplemental Mendel content.
Audit keep regions now name the requested fit result and complete trait table plus action, rather than requiring the entire square and fit, or every supplemental card, simultaneously on a phone. Original audit bundle/states are frozen in Scratch; no second audit or review round.
Final SHA-256: `789212e31afb1d84b9ef2331911df0969346c8f71b2f0a871842252aa07805f5`; raw-byte receipt and targeted evidence in review-receipt.json and review-final-behavior-receipt.json.

#### Left open

No unanswered questions: kept the supplied dataset, painted skins and meiosis-only scope; did not add nondisjunction or alter shared engines.
Missing genetics.js, probability.js and family documentation remain named in handoff.md; tool-local implementation is independently checked.
The report was staged in Scratch until delivery to honor the user's immediate stop-on-report rule. No commits. Initial document reads returned within one second before the explicit timeout wrapper was installed; later commands use bounded 30/120/300/2,400-second limits.
The builder's historical host-8775 cleanup note was labeled as historical and not refreshed: that port is outside this review's assigned scope.
Final cleanup: host.html absent and 8745 / 9940-9947 all closed. Drive and host children returned. Windows denied the CIM process inventory query; no unrelated process was killed. Port and permission evidence is in review-cleanup.json.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Punnett Predictor build handoff

#### Structure
src.html starts from the kit starter. Its own CSS lays out a naturalist's bench without scaling the whole scene. Curio Class kit handles motion, sound and narration. The graphing family Plane draws Converge with log10-transformed horizontal coordinates. Tool-local functions implement exact gamete probabilities, seeded sampling, phenotype classification and chi-square.

State holds separate Cross and Linked broods. The seeded stream belongs to its brood. Model edits clear the affected brood. The animation changes displayed counts only; the final sample is committed immediately. Play owns one cancellable timeout. Mode changes and parent changes stop it synchronously.

Opening female linked meiosis switches from the independent model once and clears that obsolete brood. Reopening the same model preserves its brood. Male-header meiosis explains its identical bv products without exposing the female crossing-over slider.

Converge uses a clip rectangle tied to the currently displayed offspring count during a large batch. Resize rebuilds that rectangle from the same progress state. Desktop controls sit outside the results scroller. On phones Breed, Clear and Test remain in a dock; the main content scrolls above the hint and dock. Explicit actions reveal their requested tray, fit card or meiosis view without taking focus on load.

#### Open questions resolved
- Keep meiosis-only scope. No nondisjunction step was added. Notes explicitly limit HS-LS3-2 coverage and point to Protein Factory for mutations.
- Keep the supplied Campbell-style fly counts. The edition was not available to verify. Label them Morgan-style, retain their exact values and document that attribution remains open; do not substitute a different dataset.
- Use painted pea and fly cutouts. All 20 spec assets are generated in this build; none contains people.

#### Spec conflicts and decisions
- The spec requests local FLUX, while the build brief and user require the image tool. Used the built-in image tool, with individual prompts and OpenAI credit.
- genetics.js, probability.js and docs/families/genetics.md are absent. Built the specified mechanics locally inside this tool without writing shared files. No protein or creature API was invented.
- A testcross has four female gamete types and one male type. The requested 4 × 4 display repeats bv male headers and labels that repetition. After linkage is enabled, female columns are weighted rather than falsely implying equiprobable cells.
- Female fly headers print their probabilities. Zero-probability columns keep their genotype labels but mute their specimen pictures; they are possibilities of the independent model, not possible offspring at zero recombination.
- Rr × Rr has a 25% chance per displayed box and 50% aggregate Rr probability. Accessible cell labels state both, resolving the spec's ambiguous 'Rr, round, 1 in 2' cell example.
- Four meiotic products need not have different genotypes. Two unlinked genes can orient two ways, but one meiosis uses only one. Both alternatives are shown at line-up; products show one possible orientation.
- Crossing-over slider d is recombinant gamete percentage. A crossover involves two of four chromatids. Text does not equate d with percentage of meioses experiencing an exchange.
- The requested fitYes voice overclaimed that chance explains the result. Wording now says compatible, not proof. fitNo uses rare rather than impossible.
- Motion off preserves the six three-second Play beats. This follows STANDARDS and POLISH timing rules where the spec's phrase 'off with Motion off' could suggest skipping playback time.

#### Art review
The two full-wing fly assets were redrawn once because the first magenta key tinted their wings pink. The selected redraws use a green key, neutral wings and the standard pipeline's despill option. First candidates remain in Scratch. All images were inspected, including the finished 240-pixel cutouts.

#### Sensitivity
This is organismal inheritance using peas and flies. No human traits or bodies are modeled. Family notes avoid inferring a person's genotype from appearance or presenting one-gene examples as a model for human identity.

#### Engine changes wanted
- Missing kit/genetics.js and docs/families/genetics.md: add the spec's Gene, Genotype, gametes, cross, breed, phenotype, chiSquare, Punnett, Meiosis and Skins API when shared code is commissioned. Promote tested mechanics after three real tools need them, per BASELINE rule 13.
- Missing kit/probability.js: a standard seeded Rand and Converge wrapper would remove the local implementation. This build uses its own explicitly documented Mulberry32 stream, so its seed-1 result cannot promise identity with a future family engine.
- No existing shared file was changed.

#### Review next
Cold review should inspect phenotype art fidelity, linked-chromatid continuity, compact layouts and voice with the final friendly-dad recordings. This run is Build only.

#### Cold review repairs, 2026-11-08
- The tally animation now reveals actual prefix counts and fractions, rather than interpolating the final ratio. Its tray reveal and thousand-event voice follow displayed N. Clear, model edits, repeat Breed and mode changes still cancel synchronously.
- Mendel row selection shows expected dominant count and observed departure, labels bars O/E for grayscale, gives immediate specimen feedback, and uses a fixed recorded-line-ready hint. Try this total stays above the detailed result.
- Short landscape meiosis puts Back/Next/Play and Close in one row, reserving at least 90 pixels for chromosomes. Automatic Play now updates the hint at each step and at the products.
- The 375-pixel Mendel view gives Try this total the existing bottom action dock; all seven trait choices remain visible. Stopping a reveal or changing modes refreshes the status for the actual brood.
- Both vestigial flies were redrawn with neutral edges and explicit curled stubs, using the corresponding normal-wing fly as a reference. A display scale aligns body sizes. Original art is preserved only in Scratch; finished WebP files use art.py --rekey.
- Motion states on screen that its preference stays on device. Fit text now explicitly describes the upper tail under the model.
- Primary Mendel counts were verified through Brown University's MendelWeb mirror. OpenStax 13.1 Figure 13.3 independently confirms all four fly counts, resolving dataset verification without substituting data. The Campbell edition itself remains unchecked.
- No new topic, nondisjunction step, score or mastery gate was added. Shared engine work and full HS-LS3-2 coverage remain outside this tool's authorized scope.
- The single final audit completed with 112 mechanical leads. Confirmed layout issues were repaired: results no longer pass beneath Breed/Seed, phone content has a bounded scroll area, and compact linked-allele labels no longer touch. Phone meiosis keeps Close and the step controls together, with the scientific scene filling the remaining space.
- Repeated taps on the current mode or already-open parent panel preserve narration instead of hushing it. Switching modes and closing still interrupt normally.
- Audit keep regions now identify the requested fit result and the complete Mendel trait table plus action. Supplemental cards and keyboard-inspectable mini-square content remain available by scrolling.
- Targeted post-audit evidence: 12 desktop layout states, 13 phone states, the main voice path, all six cheap routes, four quick-tap regressions and 62 actual-prefix animation frames passed. All resulting frames inspected. Scratch review-final-behavior-receipt.json and review-receipt.json record the final behavior and raw bundle hash.
- Review host.html is absent and ports 8745 / 9940-9947 are closed. Windows denied the CIM process inventory query; the port checks and exact permission error are preserved in Scratch review-cleanup.json.

#### Prior build test-process cleanup limitation (historical)
This is the builder's recorded result, not refreshed in the cold review: those ports are outside the review's assigned 9940-9947 and 8745.
Chrome debugging ports 9970 through 9977 are closed and host.html is removed. The local test host on 8775 still responds. Windows denied termination of the exact matched `python -X utf8 -u scripts/drive.py punnett-predictor --host 8775` processes (PIDs 15364, 44808, 35032, 19084 at inspection). No unrelated process was terminated. Scratch native-host-close.json records the matched commands and Access denied results; validation-receipt.json records the live port. This is a runtime permission limitation, not an approval-review rejection.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
