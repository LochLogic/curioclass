# Codex review: design-the-study

## Played

Cold Grade 12 play before reading the builder: initial rejection, paired placebo study, and Bench with a pin; also reviewed the 1920 projector view. The manuscript, lab and contribution reveal are strong; repeated waiting was flat. Release remains blocked by the spec conflicts below.

## Findings fixed

- should fix, general, voice: the two-second main path dropped Submit behind the longer Shuffle instruction. Shortened those prompts and let a new spoken step interrupt obsolete narration while preserving Read.
- blocker, general, Pilot: a paired 40-person Pilot was told to have everyone do both days, which it already did. Replaced that assumption with an uncertainty explanation.
- should fix, general, graphics: replaced the silhouette with the spec's revised editor portrait, generated using the built-in imagegen skill. Opening, letters and endings now use it.
- should fix, general, Bench: pinned-only histograms were called Current; labels now retain their pin numbers, means and SDs. Running studies display accumulating estimates rather than leaving old results onscreen.
- should fix, general, voice inventory: eight fixed Read hints were absent from allLines/lines.json; added them. All 26 strings match exactly.
- polish, general, phone: Clear wrapped onto a separate header row. Kept 44 px targets and fit the controls on one row, returning 48 px to the chart.
- should fix, facts: updated local AP notes/source credits to distinguish the legacy Unit 3 identifier from College Board's revised 2026-27 Unit 1 collecting-data content.
- should fix, general, audit: kept record-dialog instructions visible after a card is selected; rechecked all eight sizes. Compact pin captions/axes had squeezed plots and covered the footer hint; moved concise labels into the plots while retaining full accessible descriptions, and rechecked 680x425, 800x500 and 375x812. Rapid Run now preserves an identical how-to instead of cutting it. Empty-draft chart accessibility summaries also reset.

## Findings left

- blocker, Story, specification conflict: random order + placebo + Everyone knows + Computer publishes with a -15 ms expectation bar. Reproduced seed 1: count 0/1,000, Published, false claim that nobody knew. The explicit seven-letter specification omits this rejection. CODEX-REVIEW section 3 prohibits changing the spec; left for a spec decision.
- should fix, Story, same specification conflict: volunteers-only blinding with computer timing can be accepted with the prescribed claim that nobody knew. This acceptance wording also requires a spec correction.
- blocker, randomization analysis, source/spec conflict: unrestricted shuffles discard gamer blocks; independent sign flips discard the exactly half-each day order. Instrumenting the actual RNG found impossible assignments in 718/1,000 blocked shuffles and 861/1,000 paired flips (seed 2). Exact randomization inference must repeat the assignment scheme (Tang et al., 2009, section 3, https://pmc.ncbi.nlm.nih.gov/articles/PMC8318313/). The mandated algorithm and published example flag rates require a spec revision; teacher notes now disclose the limitation.
- should fix, catalog/spec: AP-STAT.U3 is legacy numbering. Current AP Unit 3 teaches proportions, not collecting data. Corrected local explanatory text; migrating the shared catalog identifier is outside the permitted write folders.

## Break it

- All 112 meaningful designs: recomputed estimates from individual records, checked exact bar sums, mix bars, sizes, fixed-seed shuffle replay and direct tail recount. All arithmetic checks pass; six unblinded placebo/computer designs escape the editor.
- Published/Pilot: tried the unblinded paired shortcut using real held clicks, before and after fixes. It still earns Published with expectation -15 ms. This is the named unresolved spec blocker, not a pass.
- Shuffle: five repeated clicks cannot fish for a smaller tail count; the same data keep the same 1,000 results. Submit is disabled before a shuffle, and editing invalidates the result/check.
- Bench: high Flagged share in a biased design is not treated as design quality; its histogram misses the true-effect line. All nine 400-study means pass the 1.5 ms tolerance; paired SD is 1.744 ms. Pins are comparisons, not a score, and their labels stay truthful without a current run.
- Rejection: repeated Submit returns the same named flaw; Revise alone cannot repair methods. Skip is the specified simulated Retracted outcome, not an external post.
- Saved outcomes: Published, Pilot and Retracted were reached; badges persisted into fresh tabs. Clear was tested with all three saved endings and a nonempty pin set: both arrays and localStorage were cleared.
- No slider, quiz, reflection gate, best score or quality meter exists. Selecting stronger methods directly is the intended open experiment, not a hidden-answer quiz.

## Voice walk

Held clicks, 0.12 s holds, two-second gaps, default Story: welcome, choose default chips, Run, Shuffle, Submit, Revise; Two groups; random assignment; placebo; double blind; computer, repeating Run/Shuffle/Submit after each revision; then Bench, Run, Pin.
- Spoken order: wStory, shuffle, submit, before, revise, choose, water, timer, stopwatch, published, wBench, pin. Every mode's how-to is heard once; old steps do not speak after a later state. Fast input and Read/Sound/mode-switch side path checked.
- Post-audit counts:

| Line / run | Kind | Expected | Spoken |
|---|---|---:|---:|
| Story welcome / main | welcome | 1 | 1 |
| Shuffle / main | how | 1 | 1 |
| Submit / main | how | 1 | 1 |
| Revise / main | how | 1 | 1 |
| Bench welcome / main | welcome | 1 | 1 |
| Shuffle / five Runs | how | 1 | 1 |
| Rejection / five Submits | event | 5 | 5 |
| Shuffle / rapid two Runs | how | 1, uncut | 1, uncut |

First-tap welcome cuts are allowed; subsequent row edits stop obsolete speech. Main path and repeat checks were rerun after the audit's rapid-Run repair.
- All 26 fixed lines match the manifest. Browser fallback only; no recorded news-reader clips or listening approval claimed.

## Facts checked

- AAP advice against youth energy drinks: AAP HealthyChildren, Mark Corkins, The Effects of Caffeine on Kids, current page checked 2026-11-08: https://www.healthychildren.org/English/healthy-living/nutrition/Pages/the-effects-of-caffeine-on-kids-a-parents-guide.aspx
- Random assignment, control, placebo and blinding: OpenStax Introductory Statistics 2e section 1.4: https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics
- Shuffle test: OpenIntro Statistics 4e, section 2.3, https://www.openintro.org/book/os/
- Standards: Common Core S-IC.B.3/.5/.6, https://www.thecorestandards.org/Math/Content/HSS/IC/ ; College Board AP Statistics 2026-27 Unit 1 collecting data, https://apcentral.collegeboard.org/courses/ap-statistics . The current official page confirms the legacy Unit 3 mapping is stale.
- Every reaction-time constant and all identities are fictional, from spec Content; not biological findings.
- Invented model checked independently: baseline 280, gamer -30, short sleep +25, person SD 20, true drink -10, expectation -15, practice -15, informed stopwatch -12, session SD 8 and stopwatch SD 30 ms (spec Content). 12,000 Python replicates reproduce means -39.986, -51.949, -37.004, +5.388, -24.877, -10.098, -9.967, -24.986 and -9.986 ms in table order. Paired SD 1.793 versus theory 1.789 ms.
- Exact group mix arithmetic: choose 40 = 20/20, gamer -12 and sleep 0; choose 20 = 11/9, gamer -10.30303 and sleep +1.26263; tired IDs 13 to 32 = gamer +18 and sleep +12.5. Blocked gamer mix is exactly 0. Bars sum to each observed estimate.
- Sign, mean difference, SD, two-sided absolute tail count and fewer-than-50 threshold match the stated fictional model and OpenIntro's general randomization logic; the restricted-assignment conflict above remains.

## Sensitivity

Adult-body/health context: preserve the explicit invented adult cohort and AAP advice. Gamer and short-sleeper offsets are invented, not claims about groups. Reviewer should check that the sole portrait depicts a credible older woman editor without caricature; people:true is set. No cultural or historical tradition is represented.

## Flattest moment left

The prescribed repeated Run, Shuffle, Submit revision cycle remains methodical. Accumulating Bench distributions and informative pin labels improve its previous dead wait.

## Graphics

Six assets checked at display size and as finished WebPs: editor, lab, can, water, stopwatch and reaction box. One editorial set, accurate unbranded objects, matching drink/placebo cans; no missing art tokens. Editor is the sole person and marked people:true.
- Replaced the obsolete portrait/silhouette with the spec's short dark hair, gray streaks, tortoiseshell glasses, blazer and blue pencil. Prompt: art/prompts.json; built-in imagegen; saved art/raw/editor-quill.png; processed with art.py --rekey only. Portrait is 100 px in the opening and 112 px in wide letters, responsive at small sizes.
- Art 131 KiB; final bundle 298,098 bytes (291 KiB). Preserved lab depth, paper texture, object detail, waterfall patterns and gentle LED motion. Contact sheet: _scratch/design-the-study/review-art-contact.png. Beat Lab comparison: review-bar-comparison.png in the same folder; the journal retains its own paper identity.

## Audit

Completed once last, 1,627.25 s (27.1 min), with the 40-minute bound: _scratch/design-the-study/review-audit/audit.md. Chrome 9941, host 8745. All 97 audit frames were inspected directly or in the 24 contact sheets, with native-size follow-up on leads.
- 16 leads: 13 allowed first-tap welcome skips (BASELINE rule 16), the record-dialog hint, the 680x425 pin/footer collision, and rapid Run cutting its how-to. All three real faults were fixed and scoped rechecks passed. The global hint intentionally stays inert behind a real modal; its persistent instruction is now inside that modal. No second audit or full review was run.
- Mechanical checks: all eight initial sizes clean; every listed state/mode, minimum/maximum cohort, all endings, inspector and three pins inspected. No console errors/exceptions, infinite calm animation, keyboard continuation loss or resize-stuck controls. Phone through the iframe host; grayscale and keyboard-only method/card navigation also checked.
- Wave lessons checked: immediate truthful hints/Read, stable focus and controls, 44 px targets, no concealed choice set, explicit unknowns, distinct chart styles, label/badge truth, hint restoration and no copied-word quiz. Mode/result reflow is intentional. The editor's false fairness claim and restricted-shuffle assumptions remain the explicitly named source/spec failures, not mechanical passes.
- Independent contrast: ink/panel 13.90, muted/section 5.84, brand/panel 5.95, brand/paper 5.49, white/brand 6.36, focus/panel 5.22; non-text border/section 3.88. Required notes headings are in order. Final scoped batches have zero browser errors; all started browsers/servers are closed and host.html removed.

## Left open

No new editor rule or null-model redesign added across an explicit spec conflict. Broad AP scope/generalization is discussed in notes but has no separate solo assessment; adding one would extend the specified activity. News-reader recordings remain absent; browser fallback is exercised, not listening-approved. No questions asked: retained news-reader, adult energy-drink context and the light manuscript theme as the brief leans. Wrote only the two permitted folders, no git commits; report assembled in Scratch and copied last to honor the stop instruction.
