# Codex report: line-leader-picker

## Built

- Three teacher-led K-2 modes, one offline HTML file, separate in-memory mode work, no student storage or network dependencies.
- Twenty animal classmates, two-step cards, calendar, leader spot, sticker stacks, dashed previous-month evidence, authorship stamp, three evidence checks, student-owned verdicts, summary and Bee's sick day.
- Started from kit/starter/src.html. Used Curio.voice, motion, tones, Read and Sound. No shared engine edits, git operations, commits, deployment or polish round.
- Hard limits: bundle 120 seconds, drive batches 300 seconds, audit 2400 seconds. Early read-only file reads used tool defaults before the deadline wrapper was established.

## Numbers check

- Scratch: prepare.py, numbers.json, number-details.py, model-tests.js and model-results.json.
- Twenty unique names, ABC order. A: Ant 20 and nineteen zeros, with or without Bee sick. B: twenty ones; with Bee sick: Ant 2, Bee 0, eighteen ones.
- D: 100,000 independently exercised sick months all gave twenty ones, and Bee never led on day 2. Seeded draws reproduce exactly.
- C: exact expected zeros 7.169718448; independent Python sample 7.16841; browser interpreter sample 7.16631. Actual counts drive Q2/Q3, including an injected all-one lucky case.
- Exact probability of three or more zeros: 0.999813723. Everyone once: 2.32019616e-8. Most turns 2: 12.135%; 3: 58.450%; 4: 24.303%.
- The spec's observed zero ranges and maximum of 8 are samples, not hard bounds. The Python sample reached 1 to 13 zeros; exact probability of a maximum above 8 is 3.95867621e-6. The tool does not impose those sample limits.
- Recomputed contrasts: green/white 6.529:1; ink/paper 14.321:1; muted/paper 5.878:1; Before/paper 6.648:1; red/white 5.406:1; ink/gold 8.495:1.

## Facts checked

| Student-facing fact | Named source and check |
|---|---|
| People choose rule steps; a machine follows them | Supplied spec, EK-ALG-IM-03 map; authored choices and either Who answer visibly establish this |
| One changed step changes outcomes | Supplied E1-ALG-IM-03 map; A-to-B interpreter and UI tests |
| Rules can include or leave out peers | Supplied E2-ALG-IM-03 map; actual count evidence and ungraded judgement |
| Pretend month is twenty school days, four weeks of five | Spec Content; calendar and count totals checked |
| Names, ABC order and shirt colors | Spec Content; uniqueness/order computation and art contact sheets |
| A has unequal access; B/C/D have the spec's same-chance property | Spec Check evidence table; Q1 is deliberately rule-level, separate from attendance outcomes |
| Left out and twice-while-none evidence | Spec Check evidence table; computed from the actual counts, never from a blanket C verdict |
| Bee absent only on day 2; B passes her turn; D retains her slip | Spec Rules table; independent reference outcomes, seeded UI and 100,000 D tests |
| Waiting animals feel left out | Fixed spec narration; imaginary characters only, no personal question or health claim |

- CSTA source attribution is the supplied 2026 CSTA PK-12 PDF, pages 44-45. I checked implementation against the local spec, not an independently fetched PDF. No new real-world claims were introduced.
- The fixed normal B/D Q1 explanations would misdescribe a sick month. Sick cases reuse the spec's Bee situation lines. On/off narration only describes the already specified pretend attendance switch.

## Break it

- Incomplete rule: Run, One day, To the end and New month cannot start. Step 2 appears only after step 1; changing step 1 clears it.
- Which step: clicking the unchanged first step did not clear the prompt or set a glow; clicking the changed second step did. No trial score or best score exists.
- Three checks: tried all No on a seeded C month whose evidence was all Yes. Counts stayed unchanged; each revealed actual evidence; a premature verdict could not be set.
- Verdict: Fair remained an accepted student call even with left-out friends. No correctness badge, points or stored achievement was earned by mashing thumbs or always choosing Fair.
- Lucky C: injected all-one counts produced [Yes, No, No], not an automatic unfair label.
- Pause then One day then To the end: one day, exactly one additional day, then exactly twenty total turns. Rapid mode changes left no late days in the old mode.
- Rapid friend taps: older unstarted count speech was dropped; the newest friend kept the highlight and queued count.
- A rapid Q2/Q3 path exposed the same-chance teaching line being replaced. Fixed its queue lifetime; the 2-second follow-up log records fSame spoken at 26073 ms.
- Final rechecks: editing a running rule cleared the month with no late day. Result controls retained focus while ignoring premature activation. Instruction-family switching correctly marked both changed instructions and accepted the changed second instruction; editing a partial month kept the completed twenty-turn Before and earned no false changed-step prompt.

## Voice walk

- Bank: friendly-dad, Achird; 155 prepared lines. All fixed narration and name/count parts are listed; no recording was made, as the Build brief requires. Runtime currently uses browser speech.
- Measured main path, with initial choices and Run held for 120 ms at a 2-second pace and the authorship answer after settling: First in line, step2, Goes to the back, runReady, machine, monthDone, everyone, who, whoMachine, another. First-action welcome was skipped as allowed; its premise remains in hint and Read.
- Side path: five first-step tile taps 2 seconds apart. All five tile names started. Step2 started once, then stayed silent when already heard; runReady started once in the main path.
- Change: welcome, changed tile, month result, compare. The fast path already used Run before chRun could start; that stale instruction was dropped. chWhich can likewise be skipped if the student answers immediately. Read retains the current actionable hint.
- Fair: mode welcome and rule line, whole result, evidence questions and Bee teaching. Bee B and Bee D situation lines started on their sick-day paths. The fixed C teaching now survives quick checks while that month remains current.
- Limitation: not every how-to line completed on the fast Change/Fair paths. Logs verify clip starts and queue behavior, not the quality of the eventual recorded bank voice. A recording and full listening pass remains open.

## Feel check

- Best moment: one changed card turns Ant's twenty-sticker tower into one sticker for each friend while the blue dashed old tower stays behind it.
- Flattest moment 1: a long repeated month could look like only a counter. Added the step lamps, moving leader, flying sticker, face-filled calendar and live Pause/One day/To the end controls, preserving the prescribed timing.
- Flattest moment 2: repeated fairness clicks could bury the idea in speech. Kept the chart evidence large, the judgement ungraded, the next question actionable, and fixed the C teaching line's queue lifetime.
- Played the whole Make path, Change comparison, C checks, B/D with Bee sick and summary. Later rounds make a real distinction between chance, inclusion and attendance. A class discussion can sustain ten minutes; repeated unexamined Run presses alone cannot.
- Compared with both bar tools. Side-by-side evidence: _scratch/line-leader-picker/feel-comparison.png. The painted room, animals and wood/brass desk have the intended visual weight; the code substitutes remain visibly simpler and are disclosed below.

## Done when

1. PASS: chart is the largest centered element at 1366x768 in all three modes; counts readable in inspected frames.
2. PASS with disclosed layout adjustment: full-screen controls fit; 680x425 uses four banks of five to preserve sixty-pixel targets. All eight standard-size default frames had no page scroll or undersized main target.
3. PASS: incomplete card cannot run; day 1 step 1 and step 2 lit in separate captured frames; Who and stamp tested.
4. PASS: A-to-B gave twenty ones over Ant 20/nineteen 0 Before outlines; unchanged-step cheat rejected and changed step glowed.
5. PASS: seeded C had Q1/Q2 Yes with zeros ringed; A Q1 No by rule; Bee B produced Bee 0/Ant 2; verdict stayed ungraded.
6. PASS: Pause/One day/To the end gave 1, then 2, then exactly 20 days; mid-run editing cleared immediately with no late day. First Make day uses its prescribed 1200 ms exception; later days use 450 ms.
7. PARTIAL: controls/questions have pictures and narration strings; runtime speech works, but recorded narration and the complete fast-path listening criterion remain open.
8. PASS: result is one narration sequence; Run and One day wait for it; no per-day speech during Run.
9. PASS for the measured main/five-tap paths: all tile events started, step2 and runReady each once. Fast Change instruction caveat is retained above.
10. PASS: Motion off had no running infinite animation; same normal first-day/later-day timings; Fair follows its explicit instant-calm exception.

## Wave lessons

| BUILD.md lesson | Result and evidence |
|---|---|
| Hint and voice | PARTIAL: actionable state hints/Read and once-only how lines; fast Change/Fair losses disclosed |
| Focus and layout | PASS after fixes: controls retain focus during result narration; Who/Close receive deliberate focus; keyboard order reaches the rule desk before classmates |
| Sizes | PASS: eight standard sizes, phone iframe, compact mode-specific frames; audit fixes below |
| No giveaways | PASS: no score, grading badge, predicted fairness label or right verdict; evidence is the lesson, not a hidden answer |
| Honest numbers | PASS: pretend twenty-day month, actual counts, explicit Before legend, rule-level Q1 |
| Standards | PASS: authored card, changed-step identification, three evidence checks and personal fairness call all performed solo |
| Motion off | PASS: no infinite animation; artwork remains visible; same normal day pacing |
| Short choice sets visible | PASS: all first/second-step options, four rule cards, checks and verdicts fit the inspected layouts |
| Resize during action | PASS in completed audit coverage: no exceptions or controls left disabled; later audit walk remains incomplete |
| Welcome not late | PASS: Curio.voice first-tap policy; main welcome skipped; mode welcomes cancel on mode changes |
| Unknown stays unknown | PASS: empty step 2 is ?, disabled Run; summary's untried rows stay ? |
| One look, one meaning | PASS: gold filled current stars, blue dashed Before, red dashed zero rings, count numerals |
| Badge says what is true | PASS: no success badge; stamp appears only after an authorship response; verdict belongs to student |
| Hint changes back | PASS: mode-local hint restored; running hint names the machine; Pause restores Run hint |
| No answer by copied words | PASS: changed-step prompt requires state-difference identification; checks require chart evidence |

## Audit leads

- **Audit not finished:** the single run hit the 2400-second cap. Saved audit.md has 288 mechanical leads, including repeated occurrences across sizes. Sizes, listed states, Motion off, resize coverage, and held-click walks for Make and Change completed. The Fair walk and automatic five-click/two-tap sections did not finish. No second audit was run.
- The timeout's taskkill was denied. The verified audit process and its own Chrome descendants were then terminated directly; final validation found no owned Chrome, host or audit process left.
- Fixed compact rule-card/count overlap and the sick-switch keep-region lead by giving its sixty-pixel cards a full sixty-pixel row. Rechecked at 680/800 with rectangle assertions.
- Fixed Close/Who-answer, Close/title and Close/table-heading overlap with reserved title space; contained the twenty class pictures. Rechecked Who and Summary, including all eight phone summary rows.
- Fixed focus falling to the page after To the end: aria-disabled enforces the result wait without physically disabling the focused element. The handler still refuses premature actions. Rechecked focus on #end and deliberate focus on the Who answer.
- Fixed the nine-pixel phone Bee caption with a clear picture, ten-pixel On/Off badge and spoken state. Fixed the phone's tallest-count circle spilling out of its gutter.
- Fixed additional inspected clipping: two-row full-screen verdict controls, phone check spacing, and short sick-row labels with a bed legend. Every visible phone verdict button now clears the hint band.
- Intentional icon controls account for zero-pixel text leads: their words are suppressed in compact layouts while visible 19-24 px glyphs, full accessible names and titles remain. The hidden long sick-row label similarly has a visible bed icon and legend.
- Phone classmate/count intersections are intentional transparent sixty-pixel hit regions around an unobscured count and portrait. They were not shrunk to satisfy box-overlap detection. The larger evidence-circle spill was a separate real issue and was fixed.
- Under-Summary hidden-box leads are expected overlay coverage. The chart reappears on Close. Summary is expressly an overlay in the spec.
- The two stale ready-line leads are retained as a voice-walk limitation: an action already taken invalidates its old instruction. The main measured path heard step2/runReady once; fast Change did not hear every how line.
- First-tap welcome leads for friends/tiles follow BASELINE 16 and this spec's explicit first-tap behavior. The premise remains in hint/Read and returns in the authorship answer. No late welcome was added.
- One day/To the end doing nothing on Change's completed starting month is an end boundary, not an extra day. Those controls are now marked unavailable at twenty days; Run/New month begin another month. Their active mid-month behavior passed direct tests.
- The initial full-size phone host made a favicon request that returned 404. The isolated host and tool now use an inline favicon; later phone and targeted batches had zero console errors, warnings or exceptions.
- Pre-fix frames/report remain intact. Targeted corrected evidence is in extra/, change-semantics/, final-checks/ and validation-manifest.json. The full size set and audit were not repeated.

## Frames looked at

- Bar: snowy-bar, beat-bar, and feel-comparison.
- Art: sheets 1-3, including the corrected object sheet at final asset sizes.
- Early: early-wide, early-compact; focused: compact-ready.
- Full size run: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and phone-make.
- Outcomes: month-A, changed-B, fair-C.
- Interactions: voice-main, voice-five-tiles, change-cheat, fair-cheats-C, bee-B, bee-D, rapid-mode, calm-day1, keyboard, grayscale.
- Extra: phone-make-final, phone-fair, compact-fair, compact-who, day1-step1, day1-step2; overlays: compact-who and stamp-final.
- Controls: pause-step-end and newest-friend. Final-checks: same-chance-final. Audit contact sheets and targeted corrected frames: all 73 audit PNGs reviewed in audit-sheet-1 through audit-sheet-7, with the 1366 Fair C frame also opened full size; fair-fixed-680/800, who-fixed, stamp-fixed, summary-fixed, wide-fair-controls-fixed, result-focus-fixed, edit-running-fixed, keyboard-from-load-fixed, phone-bee-fixed, phone-evidence-final, phone-summary-final, changed-instruction-identity and partial-month-keeps-before. Model-check was also opened.

## Art made

- 42 generated paintings: wall, 35 animal poses, Bee in bed, Turn Machine, three jars and tray. Final WebP total 635.37 KB; voice audio 0 KB; final bundle 1160.15 KB, below the 2 MB goal.
- Four object redraws removed unintended animal groups and cleaned the jar illustrations. Jar/tray key processing was corrected for transparent interiors and edge spill.
- Prompts, size settings, people flags, failed-asset notes and provenance are in art/prompts.json. Raw images are in art/raw; no downloaded artwork.

## Art still to paint

- Lion happy/waiting, Rabbit happy/waiting, Yak waiting. The image service rejected these outputs. Friendly SVG substitutes keep the tool usable; these five poses remain missing painted assets.
- No people were requested or generated in the final set; every prompt has people false.

## Engine changes wanted

None. Shared kit and scripts were left unchanged.

## Left open

- Five painted poses, recorded friendly-dad narration, and the full fast-path listening criterion above.
- CSTA PDF wording was attributed through the supplied local spec, not independently downloaded.
- Header and narrow-layout differences required by sixty-pixel targets are listed in handoff.md. The spec listed no open questions.
- The remaining Fair and automatic repeated-tap audit coverage is incomplete because of the cap. This build is not represented as a clean full audit. The bar tools were opened from their existing bundles to respect the write boundary.

Build only. No commit and no polish round.
