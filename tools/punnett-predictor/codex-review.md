# Codex review: punnett-predictor

## Played

Cold Grade 9 solo walk, then projector-sized inspection, before opening the builder's report, handoff, notes or source.
Played Cross, both genes, meiosis, breeding and fit, a selected Mendel row and Try this total, then real fly data and chromosomes. Strong specimen bench; the linked-data reversal is the best moment.
Evidence lives in `_scratch/punnett-predictor/`: cold-frames, break-frames, focus-frames, recheck-frames, post-break-frames and phone-frames.

## Findings fixed

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

## Findings left

- Scope: full HS-LS3-2 is not taught here. Meiosis/recombination are; mutation and replication errors remain with Protein Factory, as the spec directs. Shared catalog/engine edits are outside authorization.
- Production: friendly-dad is declared and kept in the bank, but no recordings exist. Browser fallback timing was tested; the eventual recorded takes still need listening and timing review. Recording was prohibited by the brief.

## Break it

No score, best score, quiz, reflection gate or mastery badge exists. Fit is model compatibility, not a skill award; no new achievement layer was added.

- Test spam at N=10 for 3:1: five refusals. N=20: five valid fit events, no accumulated reward. Deterministic RR x RR plus Breed 1,000: nothing to test, no false success.
- Cheapest easy-parent route, repeated Breed to the cap, then a parent edit and Test: old fit gone, brood zero. Clear during the reveal stays empty; later callbacks cannot restore it.
- Real pointer sweep of Crossing over from 0 to 50 after breeding: brood and fit clear throughout, ending with four 25% predictions. No slider position earns a completion.
- Boundary checks: 19/20 for 3:1 and four equal types; 9/10 for 1:1; 79/80 for 9:3:3:1. All expected-count gates correct. At zero linkage no recombinant offspring occur.
- All 99 selectable crosses and all 51 linkage rates passed independent probability checks. 10,000 cap, 100 drawn specimens, seed-1 757/243, per-mode brood preservation and invalid seeds checked: 188 assertions.
- Clear repeats the seeded stream, so seed hunting is possible as exploration; notes explicitly say cherry-picking a fit is not evidence. There is no saved success to farm.
- Post-fix replay of all eleven cheat/voice/keyboard cases: zero tool errors. FitNo was also tested five times with a genuinely rare seed-22 brood (19 round, 1 wrinkled, chi-square 4.267).
- Final audit-repair replay: all six cheap routes retain those outcomes; the prefix probe matched 62 further frames. Native phone Breed and Try this total produced 1,000 and 1,064 offspring.

## Voice walk

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

## Facts checked

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

## Sensitivity

No culture-specific content, religion, hard history or human-body simulation. Peas and flies are the specimens. Home notes avoid inferring a person's genotype from appearance; retain that qualification in any later edit.

## Flattest moment left

After the first 100 specimens the tray stops gaining individual images while the tally and chart continue. This is the specified cap, honestly labeled; the student's brood and fit remain the grade-appropriate payoff.

## Graphics

All 20 finished images inspected at final sizes, and all referenced art loads. No people, missing art or placeholders. Two vestigial flies redrawn using built-in image generation and standard free rekey; no other illustration stripped or simplified.
Compared the final fly bench with Beat Lab; review-bar-comparison.png preserves both. Kept the dark naturalist workbench, large painted peas, textured trays, weighted square and chromosome colors/labels.
Art 367,370 bytes; final bundle 617,081 bytes, below 2 MB. Contrast: brand/panel 13.40:1, ink/panel 14.03:1, muted/panel 8.93:1, callout 8.48:1, selected ink/brand 15.11:1, control border 3.93:1.

## Audit

The single final audit completed within its 2,400-second limit, Chrome 9941 / host 8745. All 95 frames inspected. No exceptions, lost focus, infinite Motion-off activity or controls stuck after resize; five-click narration checks clean.
Its 112 leads: 89 geometry leads traced to covered content, touching labels, obsolete keep regions and scrollable supplemental content; confirmed obstructions repaired and re-shot. Also: 15 first-action welcome omissions allowed by STANDARDS/BASELINE 16; four intentional focusable static mini-square images; four quick-tap speech cuts fixed and rechecked. Native Tab proves access to supplemental Mendel content.
Audit keep regions now name the requested fit result and complete trait table plus action, rather than requiring the entire square and fit, or every supplemental card, simultaneously on a phone. Original audit bundle/states are frozen in Scratch; no second audit or review round.
Final SHA-256: `789212e31afb1d84b9ef2331911df0969346c8f71b2f0a871842252aa07805f5`; raw-byte receipt and targeted evidence in review-receipt.json and review-final-behavior-receipt.json.

## Left open

No unanswered questions: kept the supplied dataset, painted skins and meiosis-only scope; did not add nondisjunction or alter shared engines.
Missing genetics.js, probability.js and family documentation remain named in handoff.md; tool-local implementation is independently checked.
The report was staged in Scratch until delivery to honor the user's immediate stop-on-report rule. No commits. Initial document reads returned within one second before the explicit timeout wrapper was installed; later commands use bounded 30/120/300/2,400-second limits.
The builder's historical host-8775 cleanup note was labeled as historical and not refreshed: that port is outside this review's assigned scope.
Final cleanup: host.html absent and 8745 / 9940-9947 all closed. Drive and host children returned. Windows denied the CIM process inventory query; no unrelated process was killed. Port and permission evidence is in review-cleanup.json.
