# Lunch Survey Cleanup: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: lunch-survey-cleanup

#### Built
- Built Clean and Report from the kit starter using data-desk 1.1, without shared engine changes.
- Clean has nine immediate fixes, live comparisons, painted menu consequences, Chart, Rows, Days and grade splitting.
- Report has shuffled statements, five first-check matches, attributed corrections, draft invalidation and a local manager reply.
- Required metadata, notes, voice manifest, audit states, handoff, preview, dataset and generated bundle are present.
- Work stayed in the two authorized directories. No commits, branch operations or polish round.
- Commands used bounded child timeouts: bundle 120 s, drive batches 300 s, audit 2400 s, shorter checks 30 to 120 s.

#### Numbers check
- `build_data.py` independently rebuilt the exact recipe before implementation: 412 submissions, 391 unique students,
  grades 6/7/8 = 118/140/133, 21 extra copies, 452 school students and 61 nonrespondents.
- Paper rows are 295 to 412; all 118 have blank Days. There are exactly 21 adjacent identical copy pairs under 3 seconds.
  The last online timestamp is Monday 9:36:16. Original row numbers survive every transform.
- `check_model.js` passed 4,374 assertions, including all 27 states, 81 reply paths, 729 reason combinations and 3,456 limit sets.
  Independent Python expectations and actual source functions/engine tables were compared, not a second verdict lookup.
- K/R/E: 391 rows, 53 vs 48, Add. D/R/E: 273 rows, 27 vs 36, Not this time.
  K/R/K: 412 rows, 54 vs 57, Not this time. K/R/B: 370 rows, 52 vs 39, Add despite removing 21 students.
- Beef tacos is the least-picked menu item in every state; there are no ties. Four states say Add.
- K/R/E answered Days: 844 / 273 = 3.091575. F/R/E: (844 + 118 x 5) / 391 = 3.667519.
  Fill's mode is 5; the 5s are tagged as guesses. All state means are in `model-check.json`.
- Recomputed palette contrast: ink/paper 14.55, muted/paper 5.91, white/brand 6.50,
  ring/paper 4.60, focus/paper 5.32, border/paper 3.50. See `numeric-details.json` for every pair.
- Part 1 maximum length spread is 29.69 percent. Part 2 strings span 127 to 152 characters;
  the spec's prose calls this 11 percent, which does not follow the full range under the usual longest-relative measure (16.45 percent).
  Exact required Part 2 wording was retained; numbers are identical within each state's alternatives and placement is shuffled.

#### Facts checked
- Ridgeview, Marcus, Reyes, the 452 students, response counts, paper-page loss, missing laptops, duplicate timing,
  picks, Days values, menu rule, trial month and Friday taste test are fictional scenario facts from `spec.md`.
  They are not claims about real schools. All recipe-derived counts and displayed averages were independently recomputed.
- Removal can exclude a whole group when missingness is systematic: Kang H. (2013),
  [The prevention and handling of the missing data](https://pmc.ncbi.nlm.nih.gov/articles/PMC3668100/).
  Here the exclusion is also directly demonstrated by the row recipe; no grade-level food preference is generalized.
- Remove, fill or retain missing answers; detect rapid identical submissions; standardize labels:
  [Sampling and Survey Techniques, chapter 7](https://bookdown.org/dsciencelabs/sampling_and_survey_techniques/07-Data-Validation.html).
- A filled typical value is an estimate and supplies no observed answer: Kang 2013. The tool does not claim
  that all imputation is invalid or that leaving every blank is always best.
- Variant spellings can be merged before counting: [OpenRefine manual](https://openrefine.org/docs/manual/cellediting).
  Merge explicitly assumes the three strings mean one meal; the raw strings remain inspectable.
- Grade 6's actual Days, nonrespondents' preferences and future buying are unknown in this fictional dataset.
  Grade 6's lunch picks are unknown from the working table only after Drop blanks. Duplicate counts and grades 7/8 picks are known.
- Correct report reasons state each transform's actual effect and cost. Outcome-only and wrong-fact chips are intentional distractors.
- MS-DAT-DC-24 and MS-DAT-DI-27 checked against the
  [2026 CSTA standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/).
  The official DC-24 text uses singular "issue"; the spec notes the alternate plural wording. Both coded skills are enacted solo.
- Named sources were opened during the build. No medical, dietary-benefit, legal or real-student claims are taught.

#### Break it
- Report gate: direct no-work Check and Send calls fail. Mashing fixes unlocks comparison intentionally,
  but supplies no report credit; each tried alternative leaves live evidence.
- Verdict hunting: enumerated all 27 states. Add is not awarded as a score; Drop both can produce Add while losing students.
  Its explanation and manager reply expose that cost.
- Part 1: tried all reason combinations and all-outcome answers. Outcome-only reasons fail with an explanation.
  A longest-choice strategy originally passed the honest K/R/E path; reworded two false spelling reasons and retested.
  Neither shortest nor longest can pass all three rows in any state. Placement is shuffled per draft.
- Part 2: all three options contain the same V and T. Exhaustive checks require the correct coverage/copies clauses.
  The all-grades/once shortcut works only when that is actually the true statement.
- Part 3: pick-all, one true chip, humble-sounding false chips and every subset were tested.
  Only two or more selected chips, all true for the current fixes, earn the limit match.
- Score: repeated Check repairs wrong work on the second check but never increases the frozen first score.
  Marcus-supplied statements are labeled. Later student correction also retains the first score.
- Send: mismatch, post-check statement edit, stale revision and direct API attempts all block sending.
  Editing a recommendation does not falsify evidence; it is not a scored statement.
- New draft: several fix changes create exactly one next draft; changed reasons, coverage and limits clear,
  unchanged reasons/recommendation survive. Replaying makes a visibly labeled draft, not an improved historical score.
- Replies: all 81 recommendation/state paths follow ordered costs; K/R/E Add uses 53 to 48.
- Browser validation passed 76 assertions after the final repairs (`repair-adversarial.json`).
  Guessing remains possible at one first-check attempt; no skill check can prevent lucky guesses.

#### Voice walk
- Browser fallback only; 25 manifest lines match `allLines()` exactly. No recording or paid audio call was made.
- Held 0.12-second clicks at a two-second pace on the main path logged:
  grade6Gone, tryTwo, flipAdd, ready, wReport, checkMiss, checkFixed, answerNext, sent.
  wClean is skipped on a first fix as required by BASELINE 16; the premise stays in the manager note.
- The final Report wording repair was walked separately: wReport, checkNext, checkMiss, checkFixed, sent were spoken.
  answerNext became obsolete when Part 4 was selected; sendNext became obsolete at Send. Logs mark those as stale/newer,
  not a live instruction silently lost. Current guidance is visible immediately and Read speaks it.
- Side path: early Report speaks notReady; Back speaks wClean; Days updates the hint immediately;
  Read interrupts with the current Days instruction. Later Rows/Chart lines are dropped when newer input makes them stale.
- Five held taps did not repeat heard how lines. Mode changes hush speech. Whole event lines and revision predicates use the kit.
- Disabled-control repair: welcome names Parts 1 to 3, Check is named only when enabled,
  Part 4 is named before choosing, and Send is named only once enabled.
- Speech dispatch/order was inspected through `vlog`; muted Chrome means this is not a claim to have heard a recorded Zubenelgenubi performance.

#### Feel check
- Played through Clean, every view, a flawed report, correction and earned reply, including a complete keyboard-only send.
- Best moment: Drop blanks empties Grade 6; restoring those students and merging spellings changes the menu race,
  and the painted trays trade places. The reply then names the actual cost of the student's choices.
- Flattest moment 1: bare tally changes felt remote. Added the cafeteria setting, a lit painted menu/tray swap,
  ghost heights, leaf/least-picked labels and the student-coverage bars so each consequence has a visible place.
- Flattest moment 2: reporting felt like a long form. Used the manager's letter, Marcus's changed pose,
  compact Part/Fix tabs, attributed corrections and an earned reply that preserves the student's first attempt.
- Compared `feel-compare.png` beside Snowy Mail Route, and opened Beat Lab before building.
  The older-grade data work is denser, but has comparable illustrated context, immediate consequences and a specific payoff.
  Later drafts change coverage and costs in combination rather than adding an unrelated game.

#### Done when
1. PASS: chart is central and the largest single component, verdict above and Who's in below, all visible at 1366x768.
   Compact stage/panel remain side by side. Chart height is below the approximate 50-percent aspiration; see handoff.
2. PASS: all 27 outcomes and engine-table lengths agree; every view rebuilds synchronously from raw rows on a fix.
3. PASS: Drop blanks shows Grade 6 0/118, write-ins 27/53, grade6Gone once and tacos on the board; inspected compact frame.
4. PASS: tried-effect lines recompute with the other fixes; two per problem required; locked gate names/focuses Back to Clean.
5. PASS: 14 rows per page, stable original numbers, filled/merged/copy/dropped text tags; filters and paging exercised.
6. PASS: exhaustive reason/coverage/limits checks; first-check outcome explanation and second-check true reason verified.
7. PASS: frozen first score, attributed second-check fixes, invalidation and one next draft verified in browser.
8. PASS: 81 ordered reply paths; 53-to-48 best reply captured.
9. PASS: rapid taps during tray movement remain immediate; stale voice cancels; live controls alone are named;
   how lines use heard state and flips are delayed/capped at four. Motion-off has zero running infinite loops.
10. PASS: all nine finished assets embedded; people fully visible in normal strips/reply, compact folds intentional;
    no painted lettering, HTTP resource requests, tool console errors or exceptions in successful drive batches.

#### Wave lessons
- PASS Hint/voice: immediate hint and Read, heard-based how lines, no first-action wait; stale instructions documented above.
- PASS Focus/layout: persistent control DOM, no load autofocus; locked-report focus repaired; menu labels/badge separated.
- PASS Sizes: all seven STANDARDS sizes plus hosted 375x812 inspected; compact tabs keep active choice sets visible.
  Native checkbox glyphs are 17px inside clickable labels at least 44px tall; All was enlarged from 28 to 44px.
- PASS No giveaways: shuffled alternatives, longest/shortest cheat repaired, outcome-only explanation,
  shared numbers and false-limit traps. No reward for merely obtaining Add.
- PASS Honest numbers: unique students versus submissions, guessed 5s, blank-omitting mean, fixed chart domains and fictional labeling.
- PASS Standards: solo comparisons and cost reasons enact DC-24; checked process/evidence/limits report enacts DI-27.
- PASS Motion off: no running infinite loops; state changes and evidence remain available.
- PASS Short sets: all three current fixes, three current reasons, three counting statements and all seven limits visible;
  Part/Fix tabs separate groups instead of concealing options in scroll panels. The dataset table intentionally scrolls.
- PASS Resize mid-action: audit resized every state/action without exceptions or permanently disabled controls.
- PASS Welcome timing: no welcomeAfter; early action owns narration, premise remains visible, mode switches hush.
- PASS Unknown: missing Days stays blank or explicitly guessed; future buying and nonresponse remain unknown.
- PASS One look/meaning: striped extra copies, dashed previous heights, text-tagged fills and removed rows have distinct meanings.
- PASS Truthful badges: Add/Not/0 picks and trays derive from the same current table as the chart.
- PASS Hint restoration: view/mode/report state changes recompute the current hint; Read side path verified.
- PASS No word-copy shortcut: effect lines show numeric consequences; reasons require process/cost,
  coverage requires interpreting who remains, and limits require knowing what the data cannot say.

#### Audit leads
- Ran once, completed within 40 minutes (about 24 minutes), 113 mechanical leads; no audit exceptions.
  All leads are addressed below by repeated selector/cause; the original snapshot is preserved, not presented as a clean rerun.
- `#split-grade`/`#show-dropped` small glyphs: label hit areas are at least 44px; real label click verified.
- SVG tspan labels under `#chart`, and split-axis 0/20/40: ownership/box heuristic, not obscured text.
  Every affected size/split frame was inspected; labels are visible inside their chart SVG.
- Menu-list/badge overlaps at 1000,1280,1366,1920,760: fixed with separated wide geometry and compact list folding.
  Final 1366 geometry reports zero overlap; repaired initial/Add frames inspected.
- Grade6-removed cause/Report/progress overlaps: fixed shorter effect/cause layout. Final 680 frame has a 6px gap, zero overlap.
- `#filter-all` 28px: fixed to 44px. Table pager/row/pageno overlaps across sizes: same engine pager moved outside scrolling host.
  Final compact page 2 begins original row 309 with 14 rows; host bottom equals pager top, no covered rows.
- Report-ready disabled Check wording: fixed as described in Voice walk; final 25-line manifest and focused walk verified.
- Sent-report obsolete answerNext: answer was already selected; stale instruction correctly drops. New wording does not name disabled Send.
- `#to-report` lost focus: fixed to gate-back when locked; final browser focus assertion passes.
- First-action welcome misses on Show rows, fixes and views: permitted BASELINE 16; the action happens immediately.
  Read speaks current help; Sound deliberately cuts audio. Premise stays in note/notes.
- Two quick mode taps cut welcome: intentional scope hush, with current hint restored; no late welcome is queued.
- Other controls moved after note collapse, cause reveal, filter/view or mode changes: prescribed layout transitions,
  not replacement of the active button. Five-click runs and settled Enter-twice checks were clean apart from the repaired gate focus.
- Audit phone iframe/context and no-hint leads: harness could not enter its iframe. Separate correct hosted Clean,
  Report and Part 2 evidence checks succeeded at 375px, including a final post-repair frame, with zero errors.
- Motion, resize, report-locked and remaining state checks reported nothing new. No second audit was run.

#### Frames looked at
- Opened every captured PNG: bar references, smoke/quick checks, full Clean/Report size matrices,
  targeted compact repairs, all view extremes, Motion off, grayscale, keyboard, voice and phone frames.
- Opened all 58 audit frames via 26 paired review pages: 51 unique images and seven byte-identical duplicates.
  `audit-review-manifest.json` records every original and its duplicate mapping.
- Opened all seven final repair frames, final hosted phone evidence, art contact sheets and `feel-compare.png`.
  Evidence stays under `_scratch/lunch-survey-cleanup/`; full size matrices were not repeated after small fixes.

#### Art made
- Nine original image-tool assets: cafeteria, Reyes, two Marcus poses, paper, sticky notes, double cards/mouse and two meals.
- Three people assets have people: true. Warm painted style, code-only lettering, keyed cutouts and raw provenance retained.
- Marcus think was edited from the ask reference for identity; cutout fringes were despilled using the permitted rekey pipeline.
  Final-size/contact views were inspected. Fresh-agent representation review passed; owner's shipping contact-sheet review remains later.
- Finished art: 150,152 bytes = 146.63 KB. Voice files: 0 KB. Bundle: 467,052 bytes = 456.11 KB, below the 2 MB goal.
  Full-resolution raw source PNGs are build provenance and are not embedded in the delivered HTML.

#### Art still to paint
None. No placeholders or failed image generations remain.

#### Engine changes wanted
No data-desk changes. Optional safe relative JSON subpaths in `scripts/bundle_tool.py` are specified in handoff;
the loaded dataset currently lives at the tool root because the bundler accepts basename tokens only.

#### Left open
- Browser speech fallback is verified, not a recorded performance in the planned bank voice. Recording was prohibited.
- Audit's 375px context was unavailable; separate hosted evidence covers it. Later cold review can rerun the audit.
- Approximate half-stage chart height is not met while all opening evidence and illustrated verdict remain visible;
  it is still the largest central component and the numbered focus requirement is met.
- Recommended fictional-data exception and grade-6 premise accepted; all ambiguity/layout/wording decisions are in handoff.
  Shared family documentation was not changed because it is outside the authorized write scope.
- All drive batches exited and closed their Chrome; the phone helper terminated/waited its owned server and removed host.html.
  No owned listener PID remains; the environment can expose port 8795 with PID 0, which was not treated as an owned process.
- No build-stopping issue remains. Build only; no commit and no polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: lunch-survey-cleanup


#### Played

- Cold, as a grade 7 solo student, then as a teacher projecting the tool. Played before opening the builder's report, handoff, notes or source.
- Clean, all nine fixes, Chart/Rows/Days, grade splitting, gated Report, a flawed report, correction, Send, later drafts and a keyboard-only submission.
- Best moment: removing blanks visibly erases grade 6; restoring them changes whose lunch can make the menu. Kept the painted setting, trays, people, ghost bars and coverage evidence.
- Initial driver shot timed out; the required smaller retry opened. Subsequent batches completed within their limits.

#### Findings fixed

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

#### Findings left

- No confirmed blockers or should fixes remain. Planned voice recording and retained spec decisions are named under Left open.

#### Break it

- **Comparison gate**: no-work Report remains locked. Repeating one fix does not count as comparing two. Mashing different fixes unlocks the intended exploration, but earns no report credit.
- **Verdict / Who's in / Days**: independently reconstructed all 412 raw rows and all 27 states, then compared the actual engine output. No mismatches. Add hunting can still discard 21 students; Add is an outcome, never a score, and the manager names that cost.
- **Three Part 1 checks**: tried position-only choices, outcome-only reasons, and longest/shortest strategies. Equal character lengths remove the former ranking clue in every state. Random guessing remains possible, with the first score frozen and no best-score reward. Wrong first choices remain charged to the frozen first score.
- **Part 2**: all three alternatives share the same V/T values, so copying the displayed numbers cannot distinguish them. Coverage/copy clauses have equal character lengths within each state. Correctness depends on coverage and copy handling, with shuffled placement.
- **Part 3**: all-chip and one-chip submissions fail; false humble-sounding claims fail. The former two-longest shortcut now fails in every state. At least two selected claims must all be true.
- **First score and later drafts**: repeated checks repair work without increasing the first score. A new draft retains Marcus attribution on unchanged supplied reasons, which stay unscored. A changed statement invalidates Send.
- **Recommendation / reply**: Part 4 is a recommendation, not a scored answer. The specified second check can supply answers and permit a guided Send; the report exposes that assistance rather than claiming independent mastery.
- Final gates: one true limit, all limits, edited Send and repeated-score checks reject their shortcuts; focused Fix 3 survives 1920-to-1366 resizing. Keyboard and held-click submissions reach the report.
- Evidence: `review-probes-before.json`, `review-probes-after.json`, `review-length-strategies.json`, `review-numbers.json`, `review-27-states.json`, held-click walks and keyboard evidence in Scratch.

#### Voice walk

- Main path, Sound on, default Motion, held 0.12-second clicks at a 2-second pace: Drop blanks, Keep blanks, Keep spellings, Merge, Drop both, Drop extra, Report, reasons/counts/limits, Check twice, Part 4, recommendation, Send.
- Final spoken order: grade6Gone, tryTwo, flipAdd, ready, wReport, checkNext, checkMiss, checkFixed, sent. Opening Part 4 and sending make answerNext/sendNext obsolete, so they drop. State-changing actions interrupt prior events. The first fix legitimately skips wClean under BASELINE 16; Back to Clean and repeated Clean taps hear it once.
- Side path: early Report/notReady, Back/wClean, Days, Read, Rows, Chart, Sound off, Read, Sound on. Read speaks the current hint even with Sound off; obsolete view/welcome speech is replaced.
- Counts from five held actions: `days` how, expected 1, spoken 1 plus 4 silent; `checkOk` event, expected 5, spoken 5. First score stays 5 on the all-correct repeated-check path.
- Browser fallback dispatch/text was checked through `__tool.vlog`; this is not a claim to have listened to a recorded bank-voice performance.

#### Facts checked

- **Fictional school, meal rule, characters, paper-page cause, taste test and trial month**: `spec.md`, Content. No claims about real schools, nutrition, real students or dietary groups are made.
- **412 rows / 391 students / 21 extra copies; grades 118/140/133; 61 nonrespondents; original row IDs, Days permutation and duplicate timestamps**: independently rebuilt the exact spec recipe; all 412 loaded rows agree field by field (`review_numbers.py`).
- **All 27 outcomes, least-picked Beef tacos, coverage and means**: independent reconstruction plus actual `DataTable` output. K/R/E = 53 vs 48, D/R/E = 27 vs 36, K/R/K = 54 vs 57, K/R/B = 52 vs 39. Answered mean = 844/273 = 3.091575; F/R/E = 3.667519; removing write-ins retains 92 filled guesses.
- **Remove, estimate or retain missing answers; duplicate clues and keeping one response**: Bakti Siregar, [Sampling and Survey Techniques, chapter 7](https://bookdown.org/dsciencelabs/sampling_and_survey_techniques/07-Data-Validation.html), opened live.
- **Systematic missingness can bias deletion; filled values are estimates rather than observed answers**: Hyun Kang (2013), [The prevention and handling of the missing data](https://pmc.ncbi.nlm.nih.gov/articles/PMC3668100/), opened live. The tool demonstrates its specific exclusion directly.
- **Standardizing variant strings requires choosing which meanings to merge**: [OpenRefine, Cell editing / Cluster and edit](https://openrefine.org/docs/manual/cellediting), opened live. The Merge reason states its assumption.
- **Unknown grade 6 Days, nonresponse preferences and future purchasing**: the fictional row recipe contains none of those observations; cleaned rows cannot establish them. Grade 6 lunch picks are available unless the working table removes them.
- **Standards DC-24 and DI-27**: [CSTA 2026 standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/) and [CSTA middle-school alignment](https://csteachers.org/codehs-ms_csta-standards-alignment/), opened live. Solo comparisons plus the process/evidence/limits report enact both skills.
- Teacher notes open with the required three sections and give practical home activities. Facts and intentional distractors were kept distinct.

#### Sensitivity

- No cultural, religious, Indigenous, hard-history, body or health curriculum. Food preferences are not assigned to a language or ethnic group; retained the brief's grade 6 paper-form premise.
- Fresh visual review of Reyes and both Marcus poses: respectful, age-appropriate, consistent identity, no mocking or stereotyped details. All three assets have `people: true`. The later owner's people-art review remains a shipping step.

#### Flattest moment left

- Reading the seven limits is still the slowest stretch. It serves the investigation; tabs and targeted feedback make correction easier without turning it into a different activity.

#### Graphics

- Inspected all nine finished assets individually and in final-size scenes: cafeteria, Reyes, Marcus ask/think, three props and both trays. Cohesive painted style, plausible meals, no missing art tokens or placeholders.
- Added exact code detail to the weakest props; no image removed or simplified. Kept the menu-tray consequence, directional light, quiet status light and Motion-off behavior. Compared the finish with Beat Lab and Snowy Mail Route frames.
- Art: 150,152 bytes (146.6 KiB). Final bundle: 471,837 bytes (460.8 KiB), well below 2 MB.

#### Audit

- Ran the review audit exactly once: completed in 26.4 minutes, 71 mechanical leads, all 76 PNGs opened individually. No console errors, exceptions, calm-loop activity or stuck controls.
- Confirmed the 680px retained-fill comparison overlapping Report and four rapid same-view/mode speech cuts. Fixed these and related compound cause spacing, then re-shot those layouts and voice paths.
- Remaining leads: native checkbox glyph inside its 44px label; visible SVG tspan/axis ownership; intentional phone scrolling below the fold; 15 welcome skips permitted by BASELINE 16; expected cause-note expansion with stable controls. Confirmed by frames, hit boxes and logs.
- The audit snapshot predates the scoped repairs. It was not rerun. Evidence: review-audit/audit.md, review-audit-viewed.json, audit-repair-quick-*.json and final scoped frames in Scratch.

#### Left open

- The planned casual-peer bank voice has no authored clips in this build. Browser speech and line dispatch are verified; recording was outside this review's authorization.
- Retained the spec's recommended fictional-data exception and grade 6 premise; no shared family documentation, kit or scripts changed.
- Followed the spec-recommended options unattended, as noted above. No commits or shared-file edits. All writes stayed in the two authorized folders; all owned Chrome/server processes closed, ports 8765 and 9960 to 9967 bind freely, and host.html is absent. Final syntax, inline-resource, line-length and note/people checks pass.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Lunch Survey Cleanup handoff

#### Structure
`src.html` starts from the kit starter. Its CSS lays out a cafeteria workbench, a painted menu, cleaning cards and a letter.
The script holds the exact raw survey, kit voice lines, cleaning transforms, outcome summaries, chart annotations,
the engine row table, draft checks, replies and persistent control wiring. `survey.json` is loaded at bundle time.
`window.__tool` exposes the spec's inspection API. Its report pick indices refer to shuffled visible positions.
`DataTable`, `t.replace`, `t.count`, `t.crosstab`, `renderTable`, `Chart`, `barRects` and `scales` come from data-desk 1.1.
No kit or family file was changed. All counts and report truth come from rows, never a verdict lookup table.

#### Decisions and contradictions
- Accepted the recommended fictional-data exception to the family's public-data rule. Real private student rows are not used.
  The fictional school and survey are labeled on screen and in teacher notes. Any shared-family exception note is for the integrator.
- Kept the recommended sixth-grade paper-form premise. Did not restore the earlier English-learners premise.
- Followed the user's image request and CODEX-BUILD's generated-art instructions where BUILD says not to draw.
- The brief says to start codex-report.md early and also stop when it is written. The user's explicit stop condition wins:
  evidence stays in Scratch, and the completed report is created last.
- Three 140-pixel buttons cannot fit a 36-percent panel at 680 pixels. At widths up to 1100 or heights up to 740,
  problem tabs show one complete fix group. At 1366x768 and larger laptop layouts all three cards stay visible.
- Compact Report uses Part tabs, with Fix 1 to Fix 3 subtabs inside Part 1. All three reasons for the current fix are visible.
  The seven limits use two columns. These layout choices prevent short choice sets from disappearing into a scroll panel.
- After a check, Report uses the same tabs at every size so the explanatory feedback fits beside the selected statements.
  Before checking, the full two-column letter appears only when its measured content fits, including at 1366x768.
- At short preview heights the opening manager note uses its rule summary and opens fully over the stage on tap.
  The cafeteria header and Marcus fold. The Who's in evidence uses two columns of textual rows at these heights.
- On phones the controls come before the scene, and the page scrolls vertically. The tool remains a solo student tool.
  Report's compact evidence moves into Part 2 on phones, keeping the statement and its evidence together.
- The bundler only accepts json tokens with a basename. The requested data/survey.json is stored as the actually loaded
  survey.json at the tool root; the exact generated row recipe is unchanged.
- Cold review found that a longest/middle/longest length strategy still selected all three process reasons.
  Reason alternatives now have equal 76-character lengths, preserving their meanings. Counting alternatives likewise
  have equal lengths within each state, using equivalent grade and copies clauses, equal V/T and shuffled placement.
- The planned voice is casual-peer, Zubenelgenubi. No recording was authorized. Kit browser speech is the build fallback.
- STANDARDS forbids naming disabled controls. The Report welcome names Parts 1 to 3, followed by a Check instruction
  only when Check is enabled. After corrections, the Part 4 instruction names Part 4, followed by Send only when enabled.
- The menu item list folds at compact sizes; all menu names remain in the chart. On wide screens the menu, trays and
  badge have separate space. The chart remains the largest single central component, though below the spec's approximate
  half-stage-height aspiration while the opening note, verdict and all evidence are visible together.
- Effect comparisons list up to two removed grade groups, plus extra copies. The write-in subgroup remains in Who's in.
  This follows the spec's own Drop blanks effect example and prevents a fourth evidence clause overflowing short cards.
- Send to Ms. Reyes is a fictional local exchange. It draws a report and reply and makes no external transmission.

#### Tricky parts
- Cold review: unchanged assisted reason selections carry their supplied flag and explanation into later drafts.
  The first-check count excludes those carried answers; they remain visibly marked Marcus fixed.
- Cold review: the longest-limit shortcut is blocked by a natural, longer false statement about grades 7 and 8.
  Keep these alternatives meaningfully mixed in length when changing their wording.
- Cold review: Days captions count retained blanks/filled guesses, not a constant 118 when another fix removes rows.
- Cold review: a check opens the first mismatching Part/Fix and adds result marks to the tabs.
  Check and Send take over obsolete speech with the kit's now option, which preserves Read priority.
- Cold review: the letter measures its available height before using the wide layout. Trying all three alternatives
  can add enough comparison text to hide the recommendation, so overflow uses the existing Part/Fix tabs instead.
  Resize remeasures from the full layout; control elements and keyboard focus are preserved.
- The short preview lays out prop, title and Show rows above full-width details. Comparison clauses keep every number,
  use concise grade labels and separate Veg/Tacos lines, and retain the complete text for assistive reading and hover.
  This clears the confirmed Report-button overlap without shrinking targets or removing evidence/art.
- Repeating the same view or mode preserves its live how-to/welcome; a genuine change still drops obsolete speech.
- Compact Part 1 hints name the first unanswered Fix tab. These three instructions are in the 28-line voice manifest.
- Cold review: shortened the short-preview cause note so it clears the Report button in Rows view at 680x425.
- Cold review: painted paper has code-drawn survey marks, and the spelling detail uses readable sticky-note labels.
- A null fix keeps raw rows but does not count as tried. Each fix rebuilds from raw rows, so order does not destroy evidence.
- Who's in distinguishes unique students, removed students and extra submissions. It preserves raw write-in identity after Merge.
- Filled and merged tags use raw metadata. The Row column is the original 1 to 412, never a new index.
- All selected limits must be true and at least two must be selected. Check still permits one so students see that it is insufficient.
- First-check credit freezes per draft. Marcus repairs are separately marked and never improve that first score.
- Any report-statement edit invalidates Send. A changed cleaning fix creates one new draft after a check; later changes
  before the next check join that draft. Unchanged reason rows and the recommendation survive; coverage and limits clear.
- Buttons are not replaced on selection or checking. Send moves focus deliberately to its earned report with preventScroll.
- Flip voice waits 600 ms and is capped at four per page. It checks the revision and scope before speaking.
- Stale grade-six teaching stops if sixth graders are restored. Queued speech is dropped on mode or state changes.
- The existing engine pager is moved outside the scrolling table host, preserving its controller and keyboard buttons.
- Opening locked Report focuses its Back to Clean button. Phone mode switches scroll to the start of the new mode.

#### Sensitivity
No cultural, health, body or personal-data curriculum. Food preferences are not attributed to an ethnic or language group.
The manager and student are fictional. All three people assets have people: true. Their contact sheet is in Scratch.
A fresh-agent representation check passed: respectful, age-appropriate, consistent Marcus identity, plausible hands,
no stereotypes or mocking details. Small key fringes were subsequently despilled through the permitted rekey pipeline.
The owner's people contact sheet is retained for the later shipping review.

#### Engine changes wanted
None required in data-desk. Optional bundler improvement, outside this build's write scope:
`scripts/bundle_tool.py`, the json token substitution: allow safe relative subpaths such as json:data/survey,
resolve inside the tool root and reject traversal. This would let the source use the spec's data subfolder directly.

#### Evidence
All scripts, independent calculations, captured frames, voice logs and audit output live in `_scratch/lunch-survey-cleanup/`.
`model-check.json` records 27 states, 81 reply paths, 729 reason combinations and 3456 limit sets.
`browser-check-result.json` records actual engine-table and report-state assertions, including the first-score and Send cheats.
`numeric-details.json` records independently computed contrast, text lengths and shortest/longest strategy checks.
The report gives final frame, voice, audit and process-cleanup outcomes. No commit or polish round was performed.

##### Build audit (before cold review)
The build audit completed with 113 mechanical leads. All 58 frames were opened (51 unique; seven exact duplicates).
Focused repairs afterwards corrected menu/badge overlap, compact cause overflow, pager overlap, the 28px All target,
disabled-control voice wording and locked-report focus. Seven repair frames and 76 browser assertions passed.
SVG tspan ownership and 17px checkbox glyphs were false positives: labels remain visible and the clickable labels are 44px tall.
The audit's phone iframe lookup failed; separate hosted 375px Clean, Report and evidence frames were inspected successfully.
The audit was not rerun. Its snapshot and the later focused checks are intentionally retained separately in Scratch.

##### Cold review
The separate cold-review audit ran once and completed in 26.4 minutes: 71 leads, 76 individually viewed frames.
Scoped repairs fixed retained-fill comparison/cause overlap and repeated-tap speech cancellation.
Final checks covered equal-length reason/counting alternatives in all 27 states, keyboard submission, focused
1920-to-1366 resizing, score/Send gates and a fresh held-click voice path through Send. No second audit was run.
The compact comparison clears Report at 680x425 and 800x500; the worst compound cause clears it by 4px.
Final bundle: 471837 bytes; art: 150152 bytes. All owned review ports are closed and host.html is absent.
See codex-review.md for the findings, named sources, voice qualifications and retained spec decisions.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
