# Codex report: lunch-survey-cleanup

## Built
- Built Clean and Report from the kit starter using data-desk 1.1, without shared engine changes.
- Clean has nine immediate fixes, live comparisons, painted menu consequences, Chart, Rows, Days and grade splitting.
- Report has shuffled statements, five first-check matches, attributed corrections, draft invalidation and a local manager reply.
- Required metadata, notes, voice manifest, audit states, handoff, preview, dataset and generated bundle are present.
- Work stayed in the two authorized directories. No commits, branch operations or polish round.
- Commands used bounded child timeouts: bundle 120 s, drive batches 300 s, audit 2400 s, shorter checks 30 to 120 s.

## Numbers check
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

## Facts checked
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

## Break it
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

## Voice walk
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

## Feel check
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

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
- Opened every captured PNG: bar references, smoke/quick checks, full Clean/Report size matrices,
  targeted compact repairs, all view extremes, Motion off, grayscale, keyboard, voice and phone frames.
- Opened all 58 audit frames via 26 paired review pages: 51 unique images and seven byte-identical duplicates.
  `audit-review-manifest.json` records every original and its duplicate mapping.
- Opened all seven final repair frames, final hosted phone evidence, art contact sheets and `feel-compare.png`.
  Evidence stays under `_scratch/lunch-survey-cleanup/`; full size matrices were not repeated after small fixes.

## Art made
- Nine original image-tool assets: cafeteria, Reyes, two Marcus poses, paper, sticky notes, double cards/mouse and two meals.
- Three people assets have people: true. Warm painted style, code-only lettering, keyed cutouts and raw provenance retained.
- Marcus think was edited from the ask reference for identity; cutout fringes were despilled using the permitted rekey pipeline.
  Final-size/contact views were inspected. Fresh-agent representation review passed; owner's shipping contact-sheet review remains later.
- Finished art: 150,152 bytes = 146.63 KB. Voice files: 0 KB. Bundle: 467,052 bytes = 456.11 KB, below the 2 MB goal.
  Full-resolution raw source PNGs are build provenance and are not embedded in the delivered HTML.

## Art still to paint
None. No placeholders or failed image generations remain.

## Engine changes wanted
No data-desk changes. Optional safe relative JSON subpaths in `scripts/bundle_tool.py` are specified in handoff;
the loaded dataset currently lives at the tool root because the bundler accepts basename tokens only.

## Left open
- Browser speech fallback is verified, not a recorded performance in the planned bank voice. Recording was prohibited.
- Audit's 375px context was unavailable; separate hosted evidence covers it. Later cold review can rerun the audit.
- Approximate half-stage chart height is not met while all opening evidence and illustrated verdict remain visible;
  it is still the largest central component and the numbered focus requirement is met.
- Recommended fictional-data exception and grade-6 premise accepted; all ambiguity/layout/wording decisions are in handoff.
  Shared family documentation was not changed because it is outside the authorized write scope.
- All drive batches exited and closed their Chrome; the phone helper terminated/waited its owned server and removed host.html.
  No owned listener PID remains; the environment can expose port 8795 with PID 0, which was not treated as an owned process.
- No build-stopping issue remains. Build only; no commit and no polish round.
