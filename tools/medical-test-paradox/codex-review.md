# Codex review: medical-test-paradox
## Played
Cold Grade 10 play of all four modes preceded reading the builder's report, handoff, notes or source.
Played as a solo student and checked the projected explanation. The 90 versus 891 reveal is strong; retained it.
Evidence: Scratch review-cold, review-break-before, review-rerun, review-sizes, review-phone and review-extremes.

## Findings fixed
- Blocker, general, Town mode return: Table exposed 9.17% beside an active prediction. Abandoning a prediction
  now returns Town to Ready with unknown results. Real held-click reproduction changed from revealed/predict to hidden/ready.
- Should fix, general, Table voice: correct-match results were once-only how lines. They are now events, spoken 5/5.
- Blocker, general, Table retries: cycling targets after an answer-giving hint could trigger ordinary success feedback.
  Track assisted questions and label those matches as worked examples. Unassisted matching retains its own feedback.
- Should fix, general, stopped runs: an old animation-frame callback rewrote Stopped as an active town count.
  Added a cancellation check after yielding; stopped chart and status now agree under changed settings.
- Should fix, family:probability, Chances: the leaves lacked the specified joint products. Both positive leaves
  now show their whole-town products separately from the conditional test rates.
- Should fix, general, compact Table: overlap, Reset and Glossary fell below the phone/short-window panel.
  Kept six questions visible and placed all three controls in a fixed row; formula details can scroll separately.
- Should fix, general, voice inventory: added fixed Read-only hints, glossary lines and assisted-match feedback; 23 lines total.
- Should fix, general, portrait Town prediction: result card was clipped at 760x900. Reduced only that state's
  town band to 80px, preserving the painting, grid and visible prediction controls; affected layout rechecked.
- Should fix, general, Glossary: its first action hint was silent. It now speaks once on opening with a modal-open
  validity check, preserving Read interruption, close, focus return and silent repeats.
- Polish, general, Second test: lifted the flattest scene with solid/dashed positive routes and shaded leaf cards,
  retaining all branches and counts. Leaf-number contrast is at least 8.62:1. Checked all eight STANDARDS sizes.
- Polish, general, art: replaced green-fringed coin and cassette using built-in imagegen edits and art.py --rekey.
  Preserved genuine alpha instead of applying a second chroma key. Prompt set is art/prompts.json.

## Findings left
No known in-scope blocker or should fix remains. Audit leads and spec-level limits are explicitly answered below.
Spec-level dependencies and production voice limitation are named under Left open.

## Break it
- Town prediction: real end-to-end slider sweep leaves percent and counts unknown; no reward appears.
  Repeated reveal after changing the hidden slider cannot alter the locked prediction. Mode-return answer leak fixed and rerun.
- Seven Cases: untouched 50% guesses reveal all answers, including accidental closeness in C4. No score, best,
  completion gate or mastery claim exists; the voice describes numerical closeness only. C1-C7 recomputed independently.
- Table: tried every target in sequence, five wrong matches and five right matches, real drag and keyboard selection.
  Wrong feedback deliberately supplies the relevant fraction, as the spec requires. After that hint, brute force
  produces worked-example feedback. It cannot obtain an unassisted match for that question; no score or mastery gate exists.
- Fraction/readouts: Positive gives 90/981; Has it gives 90/100; addition gives 991/10,000 = 0.0991.
  The denominator visibly changes. Equivalent numeric pairs are accepted without relying on hidden IDs.
- Random/convergence: same seed 12345 repeats, 12346 differs; seed 4 at the rare extreme gives explicit 0/0.
  100 C1 towns pooled to 9.14153% versus 9.17431% expected, in 1.69 seconds. No score rewards a lucky run.
  Interrupted beats recompute immediately; stopped partial charts retain their original expected reference.
- Extremes: N=1,000/100,000, p=0.1%/50%, catches=50%/100%, clears=50%/99.9%; no console errors or undefined arithmetic.
  100,000 uses ten-person squares. Motion off has zero infinite animations; grayscale retains fill/outline and plus signals.
- Keyboard-only C1 reaches the reveal with visible focus. Stable Table buttons retain focus and support matching.

## Voice walk
Default settings, Sound on, real 120 ms held clicks at two-second gaps: stage, Test everyone, Lock in guess,
Positives only, Table, Has it, Positive, Second test, Chances, Cases, Coin, Show answer.
Started in order: wTown, predictHow, positivesHow, surprise, wTable, afterTable, wSecond, wCases, coin.
All required mode how-to lines started once. Later input appropriately cut lines whose state ended.
Side path covered Sound off, Read, Sound on, Counts/Chances, case change and Reset. Read spoke the current hint.
| Line | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| Required welcomes/how-to lines | instruction | once each | once each |
| rightQuestion, repeated matches | event | 5 | 5 |
| wrongQuestion, repeated mismatches | event | 5 | 5 |
| workedQuestion, assisted retries | event | 5 | 5 |
Narration uses the browser fallback. This verifies scheduling and visible-state agreement, not an authored Aoede recording.

## Facts checked
Checked live on 2026-11-08, plus independent Python fixtures in Scratch review_numbers.py:
- Sensitivity TP/(TP+FN), specificity TN/(TN+FP), PPV TP/(TP+FP), NPV TN/(TN+FN), and prevalence:
  [FDA diagnostic-test guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/statistical-guidance-reporting-results-studies-evaluating-diagnostic-tests-guidance-industry-and-fda)
  and [Shreffler/Huecker, StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK557491/). NCBI direct access hit a browser check; indexed text corroborated it.
- False positive/negative meanings and prevalence-dependent predictive value: the same FDA guidance and StatPearls.
- Original teaching inputs 1%, 90%, 9% false-positive rate and natural-frequency explanation:
  [Gigerenzer et al., original paper, introduction and Figures 2-3](https://journals.sagepub.com/doi/10.1111/j.1539-6053.2008.00033.x).
- Better physician interpretation with counts, scoped to the reported examples:
  [Association for Psychological Science, 2008 release](https://www.psychologicalscience.org/news/releases/just-a-numbers-game-making-sense-of-health-statistics.html).
- Credit year 2007, five authors, 8(2):53-96: [PubMed record 26161749](https://pubmed.ncbi.nlm.nih.gov/26161749/). DOI's 2008 does not change the publication year.
- C1 TP/FN/FP/TN 90/10/891/9009; PPV 9.17%, NPV 99.89%, union .0991. C2 81.08%, C3 9.02%,
  C4 81 and 80.19 (display 80.2), 50.25%; C5 90.91%, C6 100%, C7 1%: Python applied to the spec's fictional inputs.
- Conditional fractions, union-minus-overlap, path multiplication and independence:
  [Common Core HSS-CP A.1-A.5, B.6-B.8](https://www.thecorestandards.org/Math/Content/HSS/CP/).
  Conditional independence is explicitly a model assumption, not a claim that real repeat tests have independent errors.
- Coin test: equal positive rates with/without the condition leave its probability unchanged; same FDA guidance and direct algebra.
  Fictional condition and perfect-test case remain explicitly fictional/what-if, not clinical performance claims.

## Sensitivity
People's bodies: a fresh sensitivity reviewer should check fictional-versus-personal medical interpretation,
the shorthand Well for absence of this condition, neutral false-alarm language and the repeat-test assumption.
The historical example originally involved breast screening; this adaptation names its source without implying
these are current clinical screening rates. Abstract chart glyphs are not demographic portraits.
All five paintings were visually checked and contain no people; their people flags are false. Empty scenes follow the spec.

## Flattest moment left
The 100-town curve often settles quickly and becomes visually quiet. Retained its honest scale and pooled calculation;
making it dramatic by exaggerating variation would weaken the lesson. The repeat tree received the visual lift.

## Graphics
All five finished assets opened at native size and seen in the tool. Town, clinic and laboratory paintings kept.
Coin and cassette edited with built-in imagegen, raw PNGs in art/raw and final assets in art/coin-flip.webp and art/test-strip.webp.
All art shares pastel directional light; precise population, table, tree and convergence diagrams remain in code.
Independent contrast: accent/stage 5.62:1, button ink/accent 5.52:1, ink/panel 13.11:1, muted/panel 7.25:1;
accent/result 4.73:1 and slate icons/light canvas 4.77:1, using the lightest gradient stops. Scratch review-contrast.json.
Compared with Beat Lab and Snowy Mail Route frames. Numerical instrument detail is preserved, with no added game layer.
Final bundle 798.4 KB; five assets total 245.0 KB. No placeholders or automatic network requests.

## Audit
Completed once within the 40-minute cap on port 9951, host 8755. All 113 frames inspected on 19 labeled sheets;
the 760x900 failure was also opened individually. Frozen input and SHA-256: Scratch review-audit-input.html/json.
Seven leads answered: one portrait prediction-card overlap fixed; three missing-welcome flags checked against
BASELINE rule 16; three pristine Reset no-ops (Table, Second test, Cases) are intentional and retain keyboard focus.
Test everyone and Positives only speak their own fitting instructions. Glossary now speaks its own action hint once;
the Town welcome remains available through the restored hint and Read after closing it. No late welcome was added.
Resize stress, settled-focus/Enter tests, Motion off, five-click repeats and quick-tap checks completed cleanly.
Post-audit rechecks passed: 18 inspected frames cover the fixes, all six matching cheats, affected tree sizes and main-path voice.
No second full audit or review round. All task Chrome/server processes closed; temporary host.html removed.

## Left open
- kit/probability.js and docs/families/probability.md are absent. Local mechanics remain; fixing the shared kit
  would violate this review's write boundary. Existing exact engine requests remain in handoff.md.
- Module B.9 counting is not taught, as the spec explicitly states. Move that catalog claim elsewhere; no new counting feature added.
- No recordings made: the Build rules prohibit recording audio. curious-librarian/Aoede remains production metadata.
- STANDARDS wins the calm-mode timing contradiction: motion stops, instructional beat durations remain.
- No unattended questions were left pending; spec/baseline choices were taken and documented. No commits.
- Procedure: initial document reads lacked a process timeout; bundle, drive, art and audit commands used explicit caps.
