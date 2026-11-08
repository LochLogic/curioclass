# Codex review: lunch-survey-cleanup


## Played

- Cold, as a grade 7 solo student, then as a teacher projecting the tool. Played before opening the builder's report, handoff, notes or source.
- Clean, all nine fixes, Chart/Rows/Days, grade splitting, gated Report, a flawed report, correction, Send, later drafts and a keyboard-only submission.
- Best moment: removing blanks visibly erases grade 6; restoring them changes whose lunch can make the menu. Kept the painted setting, trays, people, ghost bars and coverage evidence.
- Initial driver shot timed out; the required smaller retry opened. Subsequent batches completed within their limits.

## Findings fixed

- **Blocker, general, Report limits (`src.html:limits`)**: the two longest chips were true, so length guessing earned the limit match and 5/5. Reworded one false statement without changing its meaning. Longest and shortest strategies now fail in all 27 states.
- **Blocker, general, reason/counting alternatives**: a longest/middle/longest process-reason strategy selected all three truths and allowed 5/5 with correct other parts. Balanced reason alternatives to 76 characters and each state's three counting alternatives to equal lengths, preserving their meanings. All 27 states now lack a character-length ranking clue.
- **Blocker, general, later drafts (`createDraft`, `check`)**: unchanged Marcus-supplied reasons lost attribution and earned new first-check credit. Carry their provenance and explanations; exclude carried assistance from credit. Reproduced 5/5 before; now 3/5 with two visibly unscored Marcus fixes.
- **Should fix, family:data-desk, Days (`drawChart`)**: the caption claimed 118 filled answers after write-in removal left only 92. Captions now count retained blank/filled rows. Added audit states for this combination.
- **Should fix, general, Report layout (`fitReport`)**: trying all three fixes added enough comparison text to hide the last recommendation at 1366x768. Measure the full letter and use the existing Part/Fix tabs when needed; remeasure on resize. All choices remain available and keyboard focus survives.
- **Should fix, general, 680x425 Rows**: the cause note clipped into Report. Shorter equivalent text and compact card spacing clear the control, including compound comparisons; short report spacing also accommodates carried-credit text.
- **Should fix, general, voice**: rapid Check/Send or view changes could leave an obsolete instruction speaking. The kit's `now` option replaces obsolete speech and preserves Read priority. Identical view/mode taps preserve their still-valid instruction instead of cutting it.
- **Polish, general, post-check pause**: feedback became an undirected, mostly empty tabbed letter. Open the first mismatch, mark Part/Fix tabs and distinguish assisted/revised credit visually.
- **Polish, general, weakest art**: blank paper and generic sticky notes lacked teaching detail. Added precise survey marks over the painted page and readable code-drawn spelling labels. Kept every painting.
- Updated `notes.md`, `handoff.md`, `audit-states.json` and the generated bundle. Added three matching compact Fix-tab instructions to source and voice manifest (28 fixed lines).

## Findings left

- No confirmed blockers or should fixes remain. Planned voice recording and retained spec decisions are named under Left open.

## Break it

- **Comparison gate**: no-work Report remains locked. Repeating one fix does not count as comparing two. Mashing different fixes unlocks the intended exploration, but earns no report credit.
- **Verdict / Who's in / Days**: independently reconstructed all 412 raw rows and all 27 states, then compared the actual engine output. No mismatches. Add hunting can still discard 21 students; Add is an outcome, never a score, and the manager names that cost.
- **Three Part 1 checks**: tried position-only choices, outcome-only reasons, and longest/shortest strategies. Equal character lengths remove the former ranking clue in every state. Random guessing remains possible, with the first score frozen and no best-score reward. Wrong first choices remain charged to the frozen first score.
- **Part 2**: all three alternatives share the same V/T values, so copying the displayed numbers cannot distinguish them. Coverage/copy clauses have equal character lengths within each state. Correctness depends on coverage and copy handling, with shuffled placement.
- **Part 3**: all-chip and one-chip submissions fail; false humble-sounding claims fail. The former two-longest shortcut now fails in every state. At least two selected claims must all be true.
- **First score and later drafts**: repeated checks repair work without increasing the first score. A new draft retains Marcus attribution on unchanged supplied reasons, which stay unscored. A changed statement invalidates Send.
- **Recommendation / reply**: Part 4 is a recommendation, not a scored answer. The specified second check can supply answers and permit a guided Send; the report exposes that assistance rather than claiming independent mastery.
- Final gates: one true limit, all limits, edited Send and repeated-score checks reject their shortcuts; focused Fix 3 survives 1920-to-1366 resizing. Keyboard and held-click submissions reach the report.
- Evidence: `review-probes-before.json`, `review-probes-after.json`, `review-length-strategies.json`, `review-numbers.json`, `review-27-states.json`, held-click walks and keyboard evidence in Scratch.

## Voice walk

- Main path, Sound on, default Motion, held 0.12-second clicks at a 2-second pace: Drop blanks, Keep blanks, Keep spellings, Merge, Drop both, Drop extra, Report, reasons/counts/limits, Check twice, Part 4, recommendation, Send.
- Final spoken order: grade6Gone, tryTwo, flipAdd, ready, wReport, checkNext, checkMiss, checkFixed, sent. Opening Part 4 and sending make answerNext/sendNext obsolete, so they drop. State-changing actions interrupt prior events. The first fix legitimately skips wClean under BASELINE 16; Back to Clean and repeated Clean taps hear it once.
- Side path: early Report/notReady, Back/wClean, Days, Read, Rows, Chart, Sound off, Read, Sound on. Read speaks the current hint even with Sound off; obsolete view/welcome speech is replaced.
- Counts from five held actions: `days` how, expected 1, spoken 1 plus 4 silent; `checkOk` event, expected 5, spoken 5. First score stays 5 on the all-correct repeated-check path.
- Browser fallback dispatch/text was checked through `__tool.vlog`; this is not a claim to have listened to a recorded bank-voice performance.

## Facts checked

- **Fictional school, meal rule, characters, paper-page cause, taste test and trial month**: `spec.md`, Content. No claims about real schools, nutrition, real students or dietary groups are made.
- **412 rows / 391 students / 21 extra copies; grades 118/140/133; 61 nonrespondents; original row IDs, Days permutation and duplicate timestamps**: independently rebuilt the exact spec recipe; all 412 loaded rows agree field by field (`review_numbers.py`).
- **All 27 outcomes, least-picked Beef tacos, coverage and means**: independent reconstruction plus actual `DataTable` output. K/R/E = 53 vs 48, D/R/E = 27 vs 36, K/R/K = 54 vs 57, K/R/B = 52 vs 39. Answered mean = 844/273 = 3.091575; F/R/E = 3.667519; removing write-ins retains 92 filled guesses.
- **Remove, estimate or retain missing answers; duplicate clues and keeping one response**: Bakti Siregar, [Sampling and Survey Techniques, chapter 7](https://bookdown.org/dsciencelabs/sampling_and_survey_techniques/07-Data-Validation.html), opened live.
- **Systematic missingness can bias deletion; filled values are estimates rather than observed answers**: Hyun Kang (2013), [The prevention and handling of the missing data](https://pmc.ncbi.nlm.nih.gov/articles/PMC3668100/), opened live. The tool demonstrates its specific exclusion directly.
- **Standardizing variant strings requires choosing which meanings to merge**: [OpenRefine, Cell editing / Cluster and edit](https://openrefine.org/docs/manual/cellediting), opened live. The Merge reason states its assumption.
- **Unknown grade 6 Days, nonresponse preferences and future purchasing**: the fictional row recipe contains none of those observations; cleaned rows cannot establish them. Grade 6 lunch picks are available unless the working table removes them.
- **Standards DC-24 and DI-27**: [CSTA 2026 standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/) and [CSTA middle-school alignment](https://csteachers.org/codehs-ms_csta-standards-alignment/), opened live. Solo comparisons plus the process/evidence/limits report enact both skills.
- Teacher notes open with the required three sections and give practical home activities. Facts and intentional distractors were kept distinct.

## Sensitivity

- No cultural, religious, Indigenous, hard-history, body or health curriculum. Food preferences are not assigned to a language or ethnic group; retained the brief's grade 6 paper-form premise.
- Fresh visual review of Reyes and both Marcus poses: respectful, age-appropriate, consistent identity, no mocking or stereotyped details. All three assets have `people: true`. The later owner's people-art review remains a shipping step.

## Flattest moment left

- Reading the seven limits is still the slowest stretch. It serves the investigation; tabs and targeted feedback make correction easier without turning it into a different activity.

## Graphics

- Inspected all nine finished assets individually and in final-size scenes: cafeteria, Reyes, Marcus ask/think, three props and both trays. Cohesive painted style, plausible meals, no missing art tokens or placeholders.
- Added exact code detail to the weakest props; no image removed or simplified. Kept the menu-tray consequence, directional light, quiet status light and Motion-off behavior. Compared the finish with Beat Lab and Snowy Mail Route frames.
- Art: 150,152 bytes (146.6 KiB). Final bundle: 471,837 bytes (460.8 KiB), well below 2 MB.

## Audit

- Ran the review audit exactly once: completed in 26.4 minutes, 71 mechanical leads, all 76 PNGs opened individually. No console errors, exceptions, calm-loop activity or stuck controls.
- Confirmed the 680px retained-fill comparison overlapping Report and four rapid same-view/mode speech cuts. Fixed these and related compound cause spacing, then re-shot those layouts and voice paths.
- Remaining leads: native checkbox glyph inside its 44px label; visible SVG tspan/axis ownership; intentional phone scrolling below the fold; 15 welcome skips permitted by BASELINE 16; expected cause-note expansion with stable controls. Confirmed by frames, hit boxes and logs.
- The audit snapshot predates the scoped repairs. It was not rerun. Evidence: review-audit/audit.md, review-audit-viewed.json, audit-repair-quick-*.json and final scoped frames in Scratch.

## Left open

- The planned casual-peer bank voice has no authored clips in this build. Browser speech and line dispatch are verified; recording was outside this review's authorization.
- Retained the spec's recommended fictional-data exception and grade 6 premise; no shared family documentation, kit or scripts changed.
- Followed the spec-recommended options unattended, as noted above. No commits or shared-file edits. All writes stayed in the two authorized folders; all owned Chrome/server processes closed, ports 8765 and 9960 to 9967 bind freely, and host.html is absent. Final syntax, inline-resource, line-length and note/people checks pass.
