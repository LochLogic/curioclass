# Line Leader Picker: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: line-leader-picker

#### Built

- Three teacher-led K-2 modes, one offline HTML file, separate in-memory mode work, no student storage or network dependencies.
- Twenty animal classmates, two-step cards, calendar, leader spot, sticker stacks, dashed previous-month evidence, authorship stamp, three evidence checks, student-owned verdicts, summary and Bee's sick day.
- Started from kit/starter/src.html. Used Curio.voice, motion, tones, Read and Sound. No shared engine edits, git operations, commits, deployment or polish round.
- Hard limits: bundle 120 seconds, drive batches 300 seconds, audit 2400 seconds. Early read-only file reads used tool defaults before the deadline wrapper was established.

#### Numbers check

- Scratch: prepare.py, numbers.json, number-details.py, model-tests.js and model-results.json.
- Twenty unique names, ABC order. A: Ant 20 and nineteen zeros, with or without Bee sick. B: twenty ones; with Bee sick: Ant 2, Bee 0, eighteen ones.
- D: 100,000 independently exercised sick months all gave twenty ones, and Bee never led on day 2. Seeded draws reproduce exactly.
- C: exact expected zeros 7.169718448; independent Python sample 7.16841; browser interpreter sample 7.16631. Actual counts drive Q2/Q3, including an injected all-one lucky case.
- Exact probability of three or more zeros: 0.999813723. Everyone once: 2.32019616e-8. Most turns 2: 12.135%; 3: 58.450%; 4: 24.303%.
- The spec's observed zero ranges and maximum of 8 are samples, not hard bounds. The Python sample reached 1 to 13 zeros; exact probability of a maximum above 8 is 3.95867621e-6. The tool does not impose those sample limits.
- Recomputed contrasts: green/white 6.529:1; ink/paper 14.321:1; muted/paper 5.878:1; Before/paper 6.648:1; red/white 5.406:1; ink/gold 8.495:1.

#### Facts checked

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

#### Break it

- Incomplete rule: Run, One day, To the end and New month cannot start. Step 2 appears only after step 1; changing step 1 clears it.
- Which step: clicking the unchanged first step did not clear the prompt or set a glow; clicking the changed second step did. No trial score or best score exists.
- Three checks: tried all No on a seeded C month whose evidence was all Yes. Counts stayed unchanged; each revealed actual evidence; a premature verdict could not be set.
- Verdict: Fair remained an accepted student call even with left-out friends. No correctness badge, points or stored achievement was earned by mashing thumbs or always choosing Fair.
- Lucky C: injected all-one counts produced [Yes, No, No], not an automatic unfair label.
- Pause then One day then To the end: one day, exactly one additional day, then exactly twenty total turns. Rapid mode changes left no late days in the old mode.
- Rapid friend taps: older unstarted count speech was dropped; the newest friend kept the highlight and queued count.
- A rapid Q2/Q3 path exposed the same-chance teaching line being replaced. Fixed its queue lifetime; the 2-second follow-up log records fSame spoken at 26073 ms.
- Final rechecks: editing a running rule cleared the month with no late day. Result controls retained focus while ignoring premature activation. Instruction-family switching correctly marked both changed instructions and accepted the changed second instruction; editing a partial month kept the completed twenty-turn Before and earned no false changed-step prompt.

#### Voice walk

- Bank: friendly-dad, Achird; 155 prepared lines. All fixed narration and name/count parts are listed; no recording was made, as the Build brief requires. Runtime currently uses browser speech.
- Measured main path, with initial choices and Run held for 120 ms at a 2-second pace and the authorship answer after settling: First in line, step2, Goes to the back, runReady, machine, monthDone, everyone, who, whoMachine, another. First-action welcome was skipped as allowed; its premise remains in hint and Read.
- Side path: five first-step tile taps 2 seconds apart. All five tile names started. Step2 started once, then stayed silent when already heard; runReady started once in the main path.
- Change: welcome, changed tile, month result, compare. The fast path already used Run before chRun could start; that stale instruction was dropped. chWhich can likewise be skipped if the student answers immediately. Read retains the current actionable hint.
- Fair: mode welcome and rule line, whole result, evidence questions and Bee teaching. Bee B and Bee D situation lines started on their sick-day paths. The fixed C teaching now survives quick checks while that month remains current.
- Limitation: not every how-to line completed on the fast Change/Fair paths. Logs verify clip starts and queue behavior, not the quality of the eventual recorded bank voice. A recording and full listening pass remains open.

#### Feel check

- Best moment: one changed card turns Ant's twenty-sticker tower into one sticker for each friend while the blue dashed old tower stays behind it.
- Flattest moment 1: a long repeated month could look like only a counter. Added the step lamps, moving leader, flying sticker, face-filled calendar and live Pause/One day/To the end controls, preserving the prescribed timing.
- Flattest moment 2: repeated fairness clicks could bury the idea in speech. Kept the chart evidence large, the judgement ungraded, the next question actionable, and fixed the C teaching line's queue lifetime.
- Played the whole Make path, Change comparison, C checks, B/D with Bee sick and summary. Later rounds make a real distinction between chance, inclusion and attendance. A class discussion can sustain ten minutes; repeated unexamined Run presses alone cannot.
- Compared with both bar tools. Side-by-side evidence: _scratch/line-leader-picker/feel-comparison.png. The painted room, animals and wood/brass desk have the intended visual weight; the code substitutes remain visibly simpler and are disclosed below.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

- Bar: snowy-bar, beat-bar, and feel-comparison.
- Art: sheets 1-3, including the corrected object sheet at final asset sizes.
- Early: early-wide, early-compact; focused: compact-ready.
- Full size run: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and phone-make.
- Outcomes: month-A, changed-B, fair-C.
- Interactions: voice-main, voice-five-tiles, change-cheat, fair-cheats-C, bee-B, bee-D, rapid-mode, calm-day1, keyboard, grayscale.
- Extra: phone-make-final, phone-fair, compact-fair, compact-who, day1-step1, day1-step2; overlays: compact-who and stamp-final.
- Controls: pause-step-end and newest-friend. Final-checks: same-chance-final. Audit contact sheets and targeted corrected frames: all 73 audit PNGs reviewed in audit-sheet-1 through audit-sheet-7, with the 1366 Fair C frame also opened full size; fair-fixed-680/800, who-fixed, stamp-fixed, summary-fixed, wide-fair-controls-fixed, result-focus-fixed, edit-running-fixed, keyboard-from-load-fixed, phone-bee-fixed, phone-evidence-final, phone-summary-final, changed-instruction-identity and partial-month-keeps-before. Model-check was also opened.

#### Art made

- 42 generated paintings: wall, 35 animal poses, Bee in bed, Turn Machine, three jars and tray. Final WebP total 635.37 KB; voice audio 0 KB; final bundle 1160.15 KB, below the 2 MB goal.
- Four object redraws removed unintended animal groups and cleaned the jar illustrations. Jar/tray key processing was corrected for transparent interiors and edge spill.
- Prompts, size settings, people flags, failed-asset notes and provenance are in art/prompts.json. Raw images are in art/raw; no downloaded artwork.

#### Art still to paint

- Lion happy/waiting, Rabbit happy/waiting, Yak waiting. The image service rejected these outputs. Friendly SVG substitutes keep the tool usable; these five poses remain missing painted assets.
- No people were requested or generated in the final set; every prompt has people false.

#### Engine changes wanted

None. Shared kit and scripts were left unchanged.

#### Left open

- Five painted poses, recorded friendly-dad narration, and the full fast-path listening criterion above.
- CSTA PDF wording was attributed through the supplied local spec, not independently downloaded.
- Header and narrow-layout differences required by sixty-pixel targets are listed in handoff.md. The spec listed no open questions.
- The remaining Fair and automatic repeated-tap audit coverage is incomplete because of the cap. This build is not represented as a clean full audit. The bar tools were opened from their existing bundles to respect the write boundary.

Build only. No commit and no polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: line-leader-picker
#### Played
Verified S:\CurioClass-codex. Cold K-2 student and teacher-projector play preceded the builder's report, handoff, notes and source. Played all three modes, every rule, both authorship answers, wrong checks, Bee absent and summary. The twenty-sticker tower becoming twenty shared turns is the strong moment; the warm classroom and cast stay.
#### Findings fixed
- Should fix, general, art/src: five missing paintings used visibly flatter SVG substitutes. Generated both Lion poses, both Rabbit poses and Yak waiting; replaced all five fallbacks and corrected their inventory.
- Should fix, general, src/voice: Bee lines asserted a previous normal month, a name returning on day two, or an assigned turn in a random draw. Narration now describes the actual rule and one-day absence without those assumptions; sick C explicitly limits the day's equal chance to present friends.
- Should fix, general, src/voice: next actions and the same-chance distinction could disappear behind old feedback. Shortened ready lines; prioritized instructions and teaching; scoped pending feedback to its response and month.
- Should fix, general, src: friend-count speech and flying stickers could outlive their month. Added generation/count checks and canceled transient visuals on stop.
- Should fix, general, src/audit states: switching away during result speech could lose the authorship/check prompt. Completed, unfinished results now resume on return; held-click recheck opened Who correctly.
- Should fix, general, src: One day and resumed modes could name Pause when Run was visible. Hints immediately name the available controls.
- Should fix, general, src/voice: the third question said twice while its calculation included three or more. Screen, summary and narration now consistently mean extra turns.
- Should fix, general, src/voice: fixed result hints were missing from the narration bank. Added all nineteen zero-count hints and the everyone hint; all 178 prepared strings match allLines.
- Should fix, general, src: summary left covered friend buttons in keyboard navigation. The chart is inert while summary is open.
- Should fix, general, src: at 760x900 the On/Off badge covered Bee's caption. Gave the badge its own grid row, preserving the painted bed and full caption; both states re-shot with zero overlap.
- Polish, general, src: new stickers were repeatedly rebuilt and lost their pop after 75 ms. Stable unchanged stacks and per-column timers let the full pop land, lifting the fast month's flattest moment.
- Polish, general, src: changed-step feedback now points to Before and now without awarding a mastery chime after option cycling.
#### Findings left
- Should fix, spec conflict, Art/Rule D: the required jar-empty painting contains two slips, while the interpreter correctly has zero names after twenty draws. Retained the explicitly specified painting; see Left open.
- No other confirmed blocker or should-fix left after the scoped rechecks. This is not a final recorded-voice approval.
#### Break it
- Empty/one-step card: tried running early; no day or score can be earned. Step 1 changes clear step 2.
- Changed-step check: unchanged first step leaves the question open; changed second step exposes the causal evidence. Cycling choices produces an explanation, no points, saved best or mastery award.
- Three fairness checks: premature Q3/verdict changes nothing. Tried all Yes, all No, and wrong answers followed by both verdicts. Actual evidence remains true; neither fairness opinion is graded.
- Chance check follows the rule; left-out and extra-turn checks use actual counts. Injected lucky C gives Yes/No/No, rather than a blanket unfair result. Re-rolling cannot manufacture a grade because none exists.
- Run/Pause/One day/rapid End: exactly twenty total turns at the end; one-step and pause behavior stay bounded. Mid-run edits/mode changes cancel old work. Returning during a result restores the missing end prompt.
- Independent reference: A gives Ant 20/nineteen 0; B gives twenty 1s; sick B gives Ant 2/Bee 0/eighteen 1s. Python tested 20,000 D months; browser tested 4,000 D months without a failure.
- No reflection presumes a student's mistake. Both Who answers teach human authorship; the changed-step response identifies evidence; fairness calls remain the student's.
#### Voice walk
Held clicks, 120 ms presses, two-second action gaps, default rules and Sound on; waits only for a month/result to finish. Motion-on recheck and a separate Motion-off path.
- Make: tile0, step2, runReady, tile2, machine, monthDone, Ant, most20, zero19, who, whoMachine.
- Change: wChange, chRun, tile3, monthDone, everyone, chCompare, chWhich, chSame, chYes.
- Fair: wFair, rule A/result, fChecks, q1, q2, fVerdict, fair, fNext; B/result and q0; C/result and fSame; D/result; sick B/result and fBeeB; notFair; fSummary.
- Side paths: sick D heard fChecks, q0 and corrected fBeeD; Sound-off Read spoke the hint twice across a mode switch; interrupted result returned to Who. Targeted C heard fSame once without a cut, then fVerdict, fair, fNext and fSummary.

| Line/kind | Expected | Spoken |
|---|---:|---:|
| Tile names, events, five taps | 5 | 5 |
| step2, how, five tile taps | 1 | 1 |
| runReady / chRun / fChecks, how, main walk | 1 each | 1 each |
| fSame, once-only teaching, C recheck | 1 | 1 |
| Fair / Not fair, events, main walk | 4 / 1 | 4 / 1 |
| fSummary, how, main walk | 1 | 1 |

The final sick-C branch also spoke q1CSick once, uncut: present friends share the chance; Bee was away on day two. Completed actions can supersede their old instruction; another was canceled by the immediate mode switch. The current hint and Read retain it. No late welcome was added; BASELINE 16 allows the first-tap welcome cut. Logs establish starts and state agreement, not the quality of unrecorded bank audio.
#### Facts checked
- People create algorithms, changing a step changes outcomes, and rules affect peers: [CSTA 2026 PK-12 Standards](https://csteachers.org/2026-csta-pk-12-computer-science-standards/), printed pp. 44-45, EK/E1/E2-ALG-IM-03. Read the live PDF directly, including the line-leader example and grade 2 design-fix boundary.
- Twenty named animal friends, ABC order, four five-day weeks and one pretend twenty-day month: spec Content and Screens; recomputed totals and interpreter conservation. These are model assumptions, not calendar or biology claims.
- Rules A/B/C/D, Bee absent only on day two, rotation passing Bee, retained jar names and actual check criteria: spec Rules and Check evidence tables; independent Python plus actual browser interpreter checks. Absence carries no health guidance.
- Normal C expected zero turns: 20 times (19/20)^20 = 7.169718448. All once: 20!/20^20 = 2.3201961595e-8. Exact occupancy calculation gives maxima 2/3/4 at 12.135%/58.450%/24.303%; three or more zeros 0.999813723. Spec sample ranges are not hard limits. Derivations and seed checks are in Scratch.
- Contrast: [W3C WCAG 2.2, Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); recomputed white/green 6.53, ink/paper 14.32, muted/paper 5.88, Before/paper 6.65 and white/red 5.41. Grayscale retains counts, outlines, icons and labels.
- Teacher notes open with the three required sections; home activities practice these rules without purchases or a screen. All three standard codes map to an action the child actually takes.
#### Sensitivity
No cultural, Native, religious or hard-history content; no real people's bodies. The animal cast replaces a real class roster. Waiting poses are gentle, not mocking; Bee's absence is not a child's fault. Fair and Not fair remain equally available opinions. A later sensitivity lens can check those emotional cues; there are no human people assets to flag.
#### Flattest moment left
Repeated Run presses without discussing the chart remain repetitive. This is a teacher-led comparison tool: the stronger path is changing a step and checking Bee's different situation. No out-of-spec challenge ladder or score was added.
#### Graphics
All 47 planned paintings inspected at their displayed scale; five added with built-in image generation, full prompts/provenance preserved, keyed/resized only with art.py --rekey. Consistent storybook light, clothes and ground line; no human figures. Art 705.03 KB; bundle 1241.77 KB. Classroom depth, brass/wood machine, shaded objects, idle lamps and Before outlines retained. Compared with the existing Snowy Mail Route bundle. Art contact sheet and all viewed frames are in Scratch.
New files: art/lion-happy.webp, art/lion-waiting.webp, art/rabbit-happy.webp, art/rabbit-waiting.webp and art/yak-waiting.webp. Exact successful built-in prompts are in [art/prompts.json](art/prompts.json), review_prompt fields; source PNGs remain in art/raw.
#### Audit
**Audit not finished:** ran once with --port 9961, --host-port 8765 and the 2400-second cap. Partial review-audit/audit.md has 183 leads. Sizes/states/Motion off and Make/Change one-click/Enter walks completed. Fair walk, automatic five-click/two-tap tables and automatic resize stress did not finish or were not reached. No full-audit PASS is claimed.
First-screen sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 iframe. Opened all 76 saved size/state/Motion-off frames; also inspected cold play, corrected main/side paths, phone/compact checks, keyboard and grayscale shots.
Intentional leads: suppressed text around visible icon glyphs; transparent sixty-pixel phone hit areas overlapping their readable counts/Before counts; expected overlay coverage. Do not shrink the targets or remove art to clear those flags.
Confirmed audit fault fixed: Bee caption, On and Off at 760x900. Welcome-skip leads on tiles/friends comply with BASELINE 16; the premise stays reachable and human authorship is spoken again. Re-shot only affected states. Manual normal/Fair mid-run resizes between 1366x768 and 760x900 completed twenty days with no error or lock. The Bee D phone-size selector was normalized for the next audit; its extra phone state was not part of this capped run.
Final evidence: review-walk-release/, post-audit-checks/, review-resize/ and review-validation.json in Scratch. Corrected main path, sick-C sentence and early-run attempts passed; zero browser errors in targeted drive batches. All test Chrome/host ports closed, no host.html left. Audit and final bundle hashes are preserved separately.
#### Left open
- Jar-empty/two-slip specification conflicts with the exact empty state. A spec change or an additional true-empty illustration should settle that; no rule or shared-kit change was improvised.
- Friendly-dad recordings were not made, as instructed. Browser narration is functional; recording quality and final clip timing remain for the recording workflow.
- Kept four banks of five in the narrow preview: twenty sixty-pixel K-2 targets cannot fit two banks of ten beside controls in 680 pixels. STANDARDS overrides that spec layout.
- No questions were asked in this unattended run. Early quick read-only commands used tool defaults before the explicit deadline wrapper; bundle/drive/audit runs had explicit 120/300/2400-second caps. Authored files stayed in the tool/Scratch scope; no git commits or shared-kit edits.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 12 (general 12, family 0), polish accepted 9
Traced to spec: blockers 0, should fix 6

### Refine: line-leader-picker

Lenses: refine/teaching.md, refine/play.md, refine/craft.md. Shared audit: S:/CurioClass-codex-scratch/line-leader-picker/audit-r1.
No sensitivity review needed (no cultural, Native or hard-history content; all three lenses agree).
Integrator spot-checked in src.html: check() order (1323-1342), recordSummary at month end (1239, 1355-1359),
choose() in the Which step state (1043-1049) and on a re-tap (1051-1069), friendTap beeSick (1253-1255), L.fSummary (617).
All four lens claims held.

#### Blocker
None.

#### Should fix
1. **Is It Fair?, check feedback plays after the next question and is then dropped.** src.html:1334-1340, `check()`.
   On a first answer the next question's how line is spoken `now:true`, then "The chart agrees." / "Look at the chart
   again." plus the evidence line is queued behind it; the next thumb tap (about 3.5 s later, a child answering the
   question just heard) drops it. Seen: play/out2/fair-A-flow vlog (all three feedback pairs dropped on rule A);
   craft/frames/v4-checkx5 (q1C dropped, "agree" heard after Q2's question); teaching shots2.json t-check-order.
   A pre-reader hears three questions and no answers, and "The chart agrees" lands on the wrong question. Fixed:
   feedback (agree/look + evidence) speaks first, the next question waits for it; a later thumb never drops feedback
   for an earlier check that has not started. Re-run the voice check on a three-answer chain at 3.5 s and 6 s. (general) (build)
2. **Is It Fair?, Our chart answers the checks before the child does.** src.html:1239, 1355-1370. `recordSummary()` runs
   at month end and fills Q1 to Q3 from the data, so opening Our chart right after a rule card shows Yes/Yes/Yes with
   every thumb untouched; Q1 (a rule fact the chart cannot show) is handed over outright. Toggling Bee also records a
   row for a rule nobody checked. Seen: teaching frames/t-summary-before-checks.png; play out2/fair-summary-after.
   Fixed: a cell shows "?" until that check is answered on that rule (then the data's yes/no, as now); a row appears
   only once its first check is answered. Spec said "yes / no icons from the data" with no timing. (general) (spec)
3. **Is It Fair?, a pre-reader cannot see a mismatch, or which verdict they picked.** src.html:1313-1319, CSS .verdict,
   247. The tapped thumb gets the same pressed ring whether it matches the data or not; the only sign is 12 px "× No"
   text, hidden at 680x425 and narrower. Fair / Not fair set aria-pressed but have no pressed style, so after a
   verdict nothing visible changes but the hint. Seen: play out2/fair-A-flow.png. Spec promises "evidence on the chart
   for each check" (rings on zero columns, tallest marked) for pre-readers. Fixed: after each check the chart evidence
   draws (zero rings for Q2, tallest marked plus rings for Q3, the rule card's step pictures highlighted for Q1) and a
   small picture yes/no mark shows by the chip at every size (not a right/wrong mark); verdict buttons get a clear
   pressed look. (general) (build)
4. **Is It Fair?, thumbs mean two things.** src.html:854-855, 861-862. Checks use thumbs up = yes, thumbs down = no;
   the verdict uses thumbs up = Fair. For rule A the matching answers are down, up, up ("yes, a friend was left out")
   beside a thumbs-up Fair button. A K-2 child reads thumbs up as "good", which blurs the line between the chart's
   facts and the child's own fairness call. Seen: teaching frames/t-bee-sick-B-checks.png. Fixed: the checks use
   yes / no pictures (a check mark and a cross, or a nodding and a shaking head, each with its word as the accessible
   name), thumbs stay only on the verdict; update fChecks ("Tap yes or no for each question.") and the q0 to q2 how
   lines to name the new pictures, in voice/lines.json too. (general) (spec)
5. **Is It Fair?, a Q1 mismatch says "Look at the chart again."** src.html:1340 (same agree/look choice for checks 0
   to 2). Q1 is the rule's own fact (spec, Check evidence); for rule C the chart shows 3 stickers beside 0, which
   supports the "no" a child just gave, so sending them back to the chart teaches the opposite of fSame. Fixed: a Q1
   mismatch gets its own line, "Think about the rule, not this month's stickers.", then the q1 rule line; add it to
   L, allLines() and voice/lines.json. (general) (spec)
6. **Is It Fair?, the Q2 evidence line names "that friend".** src.html:1329. Q2 with any zero speaks `left` ("That
   friend waited all month and never led. Being left out feels sad."), the classmate-tap line; no friend is selected
   and rule C usually has 5 to 10 at zero, rule A nineteen. Seen: craft/frames/f1-fair-full (evidence "9 left out"),
   teaching t-fair-C-all-thumbs log. Fixed: Q2 speaks the count line that already exists (`zeroOne` / `zeroN`, "Nine
   friends never got a turn.") then "Being left out feels sad." as its own clip; `left` stays for the classmate tap.
   The spec gave Q1 and Q3 evidence lines but none for Q2. (general) (spec)
7. **Change a Step, Which step: the old tile is called unchanged.** src.html:1043-1047. After "Which step made the
   month change?", tapping the Before tile in the changed slot ("Stays at the front") gets chSame, "That step stayed
   the same.", which is false. Seen: teaching t-which-old-tile log. The spec says the prompt accepts a changed
   *step*. Fixed: judge by slot: any tile in a changed slot gets chYes and the glow on the new tile; only a tile in
   an unchanged slot gets chSame. (general) (build)
8. **Change a Step and Make a Rule, re-tapping the chosen tile wipes the month and changes nothing.** src.html:1051-1069,
   `choose()`. The Change mode opens with "Stays at the front" pressed; tapping it (to hear it, or because it glows)
   turns Ant's 20 into Before outlines with `changed: []`, Run replays the same month and no compare line or Which
   step follows. In Make a Rule it silently clears a finished month. Seen: play out1/change-same-tile.png. Fixed: a
   tap on the tile already chosen only speaks its name (event line, every time); in Change a Step add "That step is
   the same. Tap the other picture to change it." once as a how line (in L, allLines(), lines.json); the month and
   Before are untouched. Spec said any tile tap changes the rule and clears the month. (general) (spec)
9. **Is It Fair? and classmate taps, Bee's sick line claims a cause it did not have.** src.html:1253-1255. With Bee
   sick, tapping Bee at 0 always adds beeSick before `left`, under every rule; under rule A (Ant 20, everyone 0) and
   often rule C, Bee's 0 has nothing to do with the sick day, and E2 is about telling the rule's effect from the
   situation's. Seen: teaching t-bee-sick-A log. Fixed: add beeSick only when the sick day changed Bee's count (Bee 0
   in the sick month and Bee would have led in the same month without the sick day; in practice rule B, and rule C
   only if the day-2 draw was Bee). Spec told the build to add it for any Bee 0 in a sick month. (general) (spec)
10. **Is It Fair?, New month (or re-tapping a card) erases the class's verdict.** src.html:1034, 1239, 1355-1358.
    clearMonth sets verdict null and recordSummary overwrites the row, so Our chart loses a call already made. Seen:
    teaching t-newmonth-wipes-call (C verdict false, then null). notes.md says Our chart keeps "the class's own calls
    for this page load". Fixed: the summary keeps the last verdict per rule row until a new verdict is given for that
    row; the checks on screen reset as now. Notes then stay true. (general) (build)
11. **Our chart, the line says "Tap Close" over a bare ×, and asks to pick before any rule has a row.** L.fSummary
    src.html:617, src.html:894. The spec line has no "Tap Close"; the build added it, and the button shows only "×".
    Opened before any rule is tried it asks "Which one would you pick for our class?" over a table of "?". Seen:
    audit-r1/state-summary-1366x768.png; play finding 4; craft finding 9. Fixed: "Tap the X to go back to the rule
    cards." (and give the × a visible "Close" label at 1366 and up), and speak fSummary only once at least two rows
    have a verdict; before that, a short how line "Check a rule card first. Its row fills in here." Update lines.json.
    (general) (build)
12. **Compact sizes, the gold stars shrink to 7 to 8 px specks.** src.html:229, 348. At 680x425, 800x500 and 375 wide
    the chart reads as faces plus numbers; a 2-star column is two dots in a corner, and Ant's 20 Before outlines
    become a hatched bar. Seen: craft/zoom-fairc-680.png (from audit-r1/state-fair-c-680x425.png),
    craft/zoom-changed-375.png. The chart is the focus of the tool and the 16:10 preview. Fixed: in the 10x2 and 5x4
    banks the star stack uses the cell width the count does not (or stars as short rows of at least 12 px), so each
    sticker reads; check 680x425, 800x500, 375x812. (general) (build)

#### Polish accepted
1. **Step 2 tap: tile name first, then "Tap Run".** src.html:1074-1076. Now the how line plays `now` and the tile
   name after it (play out1/make-d-end, craft v2-step2x5). Speak the tile name first, then runReady / chRun queued.
   Keep Done when 9 (runReady once). (general)
2. **Q3 has one wording everywhere.** Chip (src.html:846) "Extra turns while a friend got none?", voice and hint
   "Did someone lead more than once while a friend got none?", Our chart column "Extra / none?" (527). Use the spoken
   question on the chip (wrapped) and the Q3 picture with a short "Led more, one none?" or the picture only in the
   summary header. (general)
3. **The name slip lands beside the jar, not over Week 1.** src.html:57 (.slip left 145 top 30) covers day squares 1-2
   for the whole month (play out1/make-d-day1.png, make-d-day8.png). Place it by the jar or the Leader spot, never over
   a calendar day. (general)
4. **Projector reading size.** At 1920x1080 rule card names stay 12 px, check questions 14 px, evidence 12 px
   (audit-r1/state-fair-c-1920x1080.png). Scale .rule-pick, .check h2, .evidence and .verdict button in the 1600 px
   media query. (general)
5. **Fair mode hint does not name the hidden Turn Machine.** src.html:1285 sets hint('machine') while the machine is
   hidden. Keep the current hint, or a fair line naming the rule card. (general)
6. **Bee's sick day shows on the chart.** src.html:984 shows Bee in bed only while exactly 2 days are done; in a
   finished sick month Bee's column looks like any other zero. Add a small bed mark on Bee's column (or Bee's class
   row cutout) whenever the sick switch is on. The spec already promises "Bee in bed on day 2". (general)
7. **The Who question comes back if closed unanswered.** src.html:1227-1233, 1274. Closing with × loses the only EK
   moment for the page load. Offer it again after the next finished month until answered. (general)
8. **Rule B's Q1 line answers Q1.** L.q1B (638) "Everyone gets a turn, one after another." is the turn-for-everyone
   idea fSame separates from same chance. Use "Every friend comes to the front in turn, so everyone has the same
   chance." in L and lines.json. (general)
9. **Cheap nits taken:** remove the unreachable lines tie11 to tie20, most1 and zero20 from L and voice/lines.json
   (craft finding 7, read from resultParts 1203-1211); add `title` tooltips to the icon-only Fair, Not fair, Our chart
   and New month buttons at short sizes (spec asked for them); make Run's top gradient stop dark enough for 4.5:1 with
   white 15 px bold text (now 4.40:1 at the top, src.html:124). (general)

#### Settled calls
- Audit "overlap" rows at 375x812 (count over classmate button) are by design; "text under 10 px" rows on icon-only
  buttons are font-size 0 with names intact. Do not change (Play and Craft agree).
- "Welcome not heard" after a first tile or classmate tap, and a mode welcome cut by a quick second tap: BASELINE 16;
  the premise stays in the hint and Read. Do not change.
- "has not led yet" 4 of 5 at a 2 s pace is the newer tap dropping the older tap's tail, as the spec asks; 5 of 5 at 4 s.
- Q2 line wording: Teaching called it polish, Craft should fix. Settled should fix (item 6): the spoken line is false
  about the screen.
- Thumbs (item 4): settled from the spec's own aim (facts on the chart, verdict the child's) and BASELINE 2; the checks
  change pictures, nothing about what is taught. Verdict stays thumbs plus the cross on Not fair.
- Our chart (item 2): it still shows the data's yes/no once answered; it never shows right/wrong marks for answers and
  never marks the verdict (E2 Done when).
- No score, points or right/wrong marks anywhere in Is It Fair?; the picture yes/no by a chip (item 3) shows the
  chart's fact, not whether the child was right.
- Contract, keyboard, focus, 60 px targets, Motion off pacing, lines table vs lines.json, art tokens: clean (Craft). Leave.

#### To the spec's open questions
- None for Cory. For the spec owner: spec.md should be updated to match items 2, 4, 5, 6, 8 and 9 (summary fills from
  answers, yes/no check pictures, Q1 mismatch line, Q2 count line, re-tap of the chosen tile, beeSick only when the sick
  day caused the zero). Codex does not edit spec.md.

#### Not taken
- Day-by-day readout in Is It Fair? ("Day 2: Bee away, Cat led..."): the bed mark (polish 6) covers the teacher's need
  without bringing back the day strip the spec removed for this mode.
- Distinct first-in-line step icons at 680x425 (play nit 10): the voice names each card and the rule cards carry their
  letter; an art redraw for a nit is not worth it now.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: line-leader-picker (round 1)

Cold Craft lens, 2026-11-06. Bundle `tools/line-leader-picker/line-leader-picker.html` as built (not re-bundled).
Shared audit: `S:/CurioClass-codex-scratch/line-leader-picker/audit-r1/audit.md`. My frames and logs:
`S:/CurioClass-codex-scratch/line-leader-picker/craft/frames/` (shots in `craft/shots.json`, Chrome port 9883, held
clicks 0.12 s, Sound on).

Counts: blocker 0, should fix 3, polish 3, nit 4.

#### Findings

1. **Is It Fair?, check answers: the feedback for an answer plays after the next question, so it reads as the
   answer to the wrong question.** `src.html:1334-1340`: on the first answer to each chip, `V.how(next, {now: true})`
   speaks the next question ("Was any friend left out? Tap thumbs up for yes, or thumbs down for no.") first, and
   only then the feedback for the question just answered ("The chart agrees." + evidence line). A pre-reader hears
   "Was any friend left out? ... The chart agrees." and takes "agrees" as the verdict on Q2. With a 6 s tap pace the
   first answer's evidence line was then dropped (`q1C ... dropped, newer`). Seen: `craft/frames/v4-checkx5` log
   (16114 q1 how spoken, 21497 agree, 22249 q1C dropped). Better: feedback first (event, now), then the next
   question queued behind it. **should fix**, general.

2. **Is It Fair?, Q2 evidence line names "that friend" when several friends are left out and none is selected.**
   `src.html:1329`: Q2 with any zero uses the `left` line, "That friend waited all month and never led. Being left
   out feels sad." It is the classmate-tap line; after a Q2 answer no friend is picked, and in rule C usually 5 to 10
   friends are at 0 (my seeded run: 9 left out, `craft/frames/f1-fair-full`, evidence "Yes: 9 left out"). The spoken
   line does not match the screen. Better: a Q2 line built from the count ("n friends never got a turn", which
   already exists as `zeroN`/`zeroOne`), and keep `left` for the classmate tap. **should fix**, general.

3. **Compact layouts: the gold stars, the focus of the tool, shrink to 7 to 8 px specks.** `src.html:229` (`.star
   {width:8px}` at short heights), `src.html:348` (7 px at under 600 wide), stack columns 15 to 17 px wide. At
   680x425, 800x500 and 375 wide the sticker chart reads as faces plus numbers; a 2-star column is two dots in the
   corner of the cell (zoomed: `craft/zoom-fairc-680.png`, from `audit-r1/state-fair-c-680x425.png`;
   `craft/zoom-changed-375.png`, Ant's 20 Before outlines are a hatched bar). The preview must be readable and
   inviting (STANDARDS, Sizes); here the "chart shows at a glance" idea is lost in the 16:10 preview. Better: in the
   5x4 and 10x2 banks, give the stack the width the count number does not use (or stars as a short row of 12 px
   stars), so each sticker is visible. **should fix**, general.

4. **Q3 has three different wordings.** On the chip: "Extra turns while a friend got none?" (`src.html:846`); spoken
   and in the hint: "Did someone lead more than once while a friend got none?" (`L.q2`); in Our chart: "Extra /
   none?" (`src.html:527`). The spec's wording is the spoken one. Anything shown twice should match (POLISH);
   "Extra turns" is also vaguer for grade 2. Better: the chip heading uses the spoken question (or a shortened form
   with the same words), the summary column "Led twice, one none?" or the picture only. **polish**, general.

5. **Make a Rule / Change a Step: the tile's own name plays after "Tap Run".** `src.html:1074-1076`: when step 2 is
   chosen and `runReady`/`chRun` is not yet heard, the how line is spoken now and the tile's name is queued behind
   it, so the student hears "Tap Run to play our month." then "The leader stays at the front." about 2 s after the
   tap (`craft/frames/v2-step2x5` log: tap at about 3.8 s, runReady 4012, tile2 6093). If they tap Run straight
   away, the tile name starts after the month is already playing. Order should follow the action: tile name first,
   then the how line. **polish**, general.

6. **Is It Fair?, the hint names the Turn Machine while it is hidden.** `src.html:1285`: `fairRule` sets
   `hint('machine')` ("The Turn Machine does just what our card says.") for the 1.5 s month, but the machine art and
   rule card are hidden in this mode. Better: a fair-mode line ("Rule C is playing its month.") or keep the previous
   hint. **polish**, general.

7. **Lines that can never play are in `voice/lines.json`.** `tie11` to `tie20` (two friends with 11 or more turns
   need 22 or more days), `most1` (`resultParts` returns "everyone" first when the top count is 1) and `zero20`
   (someone always leads): 12 clips the voice step would record for nothing. Checked by reading `resultParts`
   (`src.html:1203-1211`). **nit**, general.

8. **Short layouts: Fair, Not fair, Our chart and New month are icon-only with no tooltip.** At 680x425 to 1000x625
   (`src.html:249-251`) the text is set to `font-size:0`; the accessible names survive, but there is no `title`, and
   the spec asked for labels as tooltips. The icons themselves render (`audit-r1/state-fair-c-680x425.png`).
   **nit**, general.

9. **Our chart: the voice says "Tap Close" but the control is a bare "×".** `L.fSummary` (`src.html:617`). A
   pre-reader hears a word that is not on screen. Better: "Tap the X to go back to the rule cards." **nit**, general.

10. **Run button text contrast at the top of its gradient is 4.40:1** (white on `#33884f`, 15 px bold, not large
    text); 6.53:1 at the bottom. `src.html:124`. Average passes; a flat `#1d6b3a` or a darker top stop removes the
    doubt. **nit**, general.

#### Contract and access (clean)

- One file, 1,271,577 bytes (under the 2 MB goal). No `http` URL, `fetch` or XHR in the bundle; Resource Timing
  listed 0 entries after a full Make month and a Fair month (`p2-fairframes`, `f1-fair-full`). No console errors or
  exceptions in any of my 14 shots or in the audit. Kit used (`Curio.voice`, `Curio.tone`, motion, header buttons).
- Frame times at 1366x768 (headless, GPU off): a Make run, 300 frames, median 16.7 ms, max 16.8 ms, none over 33 ms;
  a Fair month's sticker pops, 150 frames, max 16.7 ms.
- Keyboard: Tab order is mode buttons, Motion, Sound, Read, step tiles, run buttons, then the 20 classmates (panel
  before the long list). Enter on a step-1 tile then Tab and Enter on a step-2 tile builds the rule; focus stays on
  the tile through the step-2 rebuild; focus ring 4 px solid (`k1-tab`). Escape closes both overlays. Who overlay
  takes focus on its first button; Our chart makes the chart inert and focuses Close.
- Targets: 60 px on tiles, run buttons, classmates, thumbs and verdicts; kit header buttons 44 px (audit clean).
- Color never alone: zero columns have a dashed ring and the waiting pose; Not fair has thumb plus cross; Before is
  dashed and has its count.
- Motion off: no fly-star, arrive or pop classes ever applied; day 1 about 1220 ms, then 454 to 469 ms per day, same
  as Motion on (`m1-calm-run`). Lamps' breathing loop stops under `.calm`.
- Lines: every value in the line table (including the 19 generated `monthZeroN` hints) is in `voice/lines.json`
  word for word and the reverse; no duplicates.
- Art: all 47 `art:` tokens have a prompts.json entry, none unused; all are animals or objects, `people:false` is
  correct.
- Words: no em dashes in src, notes, spec or lines; "Curio Class" only in full. Nothing is stored; notes say so.

#### Standard voice check

Sound on, Motion on, held clicks. Logs in each shot's output (`craft/frames/*.png` named as below).

| Line | Kind | Expected | Spoken | Run |
|---|---|---|---|---|
| tile0 / tile1 (step 1 tiles) | event | 5 | 5 | v1, tiles 2.5 s apart |
| step2 | how | 1 | 1 (then dropped 1, silent 3) | v1 |
| tile2 / tile3 (step 2 tiles) | event | 5 | 5 (first one late, finding 5) | v2 |
| runReady | how | 1 | 1 (then dropped 1, silent 3) | v2 |
| friend name + "led one time." | event | 5 | 5 and 5 | v3, 4 s apart |
| agree (Q1 re-answered) | event | 5 | 5 | v4, 6 s apart |
| q1C evidence | event | 5 | 4 (first dropped behind the next question, finding 1) | v4 |
| q1 (next question) | how | 1 | 1, then silent | v4 |

- Stale lines (v5, taps 0.2 s apart through tile, tile, Run, classmate, Change mode, Make mode, New month): every
  older line dropped or cut by hush; the last spoken line ("The Turn Machine does just what our card says.") fits the
  running month; final hint "Tap Pause, One day, or To the end." Clean.
- First tap: stage tap gets the welcome at once (v7); a key (Tab) gets the welcome (v8); tiles, classmates, mode
  buttons, Read and Sound as in the audit table. Tile and classmate first taps skip the welcome (BASELINE 16); the
  premise stays in the hint and Read and returns in the Who answer lines. Not reported.
- Read (v6): Read during a tile line cuts it and speaks the hint; Read with Sound off still reads; a mode change 0.5 s
  after Read starts the Change welcome at once. Clean.
- Order (v9): lines followed the taps; classmate taps 0.6 s apart drop the older classmate's unstarted count (as the
  spec asks); the only order fault is the tile name behind its how line (finding 5) and check feedback behind the
  next question (finding 1).
- Done when 8 (no per-day line during a run) and 9 (five tile taps 2 s apart, step2 and runReady once) hold.

#### Audit pilot

- Leads confirmed: none of the audit's leads became a finding.
- Leads wrong: "text under 10 px" on Motion, Sound, Read and on Fair, Not fair, Our chart, New month at short sizes
  (the icons render through `::first-letter`; names are intact; only the missing tooltip is a nit, finding 8). The
  375 "overlap" rows (count over classmate button) are by design: the classmate button fills the cell and the count
  sits in its padding, readable on the frame. "Welcome not heard" after tile and classmate first taps and the mode
  welcome cut by a second quick tap are BASELINE 16 cases, not reportable. The classmate "has not led yet" lost 1 of 5
  at a 2 s pace is the newer tap of the same friend replacing it (spec: newer drops older); at 4 s all 5 played.
- Missed by the audit: the stars shrinking to specks in the compact charts (finding 3; it checks text, not drawn
  marks), the check feedback playing after the next question (finding 1; its walk taps each control once, not an
  answer sequence), the Q2 line's wording against the state (finding 2), the three Q3 wordings (finding 4) and the
  unreachable recorded lines (finding 7).

Nothing here is cultural, Native or hard history; no sensitivity review needed from this lens.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: line-leader-picker (round 1)

Played twice: as a K-2 child alone at home (Sound on, nothing read), and as a teacher projecting at 1366x768 and
1920x1080. My frames and logs: `S:/CurioClass-codex-scratch/line-leader-picker/play/out1/` and `out2/` (drive.py,
held clicks, port 9880). Shared audit frames used: `audit-r1/size-1366x768.png`, `state-who-*`, `state-changed-*`,
`state-fair-c-*` (1366, 1920, 680), `state-bee-b-1366x768.png`, `state-summary-1366x768.png`, `state-changed-375x812.png`,
`state-who-680x425.png`.

Overall: the core loop lands. The droopy sitting pose on 19 friends after rule A is the strongest moment in the tool,
the Before outlines in Change a Step read at a glance, and a solo K child gets a clear first instruction. The
problems are in Is It Fair?, where the grade 2 feedback is mostly unheard and unseen, and one easy trap in Change a Step.

#### Should fix

1. **Is It Fair?: the check feedback is dropped at a normal tapping pace** (src.html:1333-1340, `check()`).
   On the first rule, each thumb tap speaks the next question's how line first (`now:true`), then queues
   "The chart agrees." / "Look at the chart again." plus the evidence line. That question line takes about 3.5 s, so
   the next thumb tap (a child answering a question they just heard) drops the queued feedback. Rule A with taps
   3.5 s apart (`out2/fair-A-flow.png`, vlog): "Look at the chart again." + "Only the friend at the front can lead..."
   dropped, "The chart agrees." + "That friend waited all month and never led..." dropped, "Look at the chart again." +
   "One friend led more than once..." dropped by the verdict tap. Same in `fair-bee-C` (q1CSick never heard). The
   child hears three questions and no answers: the evidence lines are the teaching of E2, and the "left" feelings
   line is lost too. Better: speak the feedback first and let the next question wait for it (or speak the next question
   only after the feedback ends), and do not let a later thumb drop a feedback line that has not started on the first
   pass. Tag: general (event line lost behind a how line on rapid answer flows).

2. **Is It Fair?: a pre-reader cannot see that the chart disagreed, or which verdict they picked**
   (src.html:1313, 1318-1319, CSS .verdict). The tapped thumb gets the same blue pressed ring whether it matches the
   data or not; the only sign is 12 px text "× No" under it (hidden entirely at 680x425 and narrower, src.html:247).
   With the spoken "Look at the chart again." dropped (finding 1), a mismatch is invisible to a grade 2 non-reader
   (`out2/fair-A-flow.png`: thumb up on Q1 for rule A, evidence "× No"). Separately, Fair / Not fair have no pressed
   style at all: after tapping Not fair nothing on screen changes except the hint (same frame). Better: show the
   evidence as a picture next to the thumbs (a small check or look-again mark, not right/wrong scoring), and give the
   verdict buttons a pressed look. Tag: general. Level stays should fix since the spec
   promises "evidence on the chart for each check" to pre-readers.

3. **Change a Step: tapping the already chosen tile wipes last month and changes nothing** (src.html:1051-1069,
   `choose()`). The mode opens with "Stays at the front" pressed; a child who taps it (natural: to hear it, or because
   it glows green) turns Ant's 20 stars into Before outlines, clears the chart, and is told "Tap Run to play our
   month." with `changed: []`. Running replays the identical month, then no compare line and no "Which step" question
   arrive (`out1/change-same-tile.png`). The same tap in Make a Rule silently clears a finished month. Better: a tap on
   the tile that is already chosen only speaks its name (and in Change a Step, says "That step is the same. Tap the
   other picture to change it."), and never moves the month to Before. Tag: general.

4. **Our chart hint names a control that is not on screen** (src.html L.fSummary, overlay `.close`). The hint and voice
   say "Tap Close to return to the rule cards." but the button is a bare "×" (`audit-r1/state-summary-1366x768.png`).
   A child who cannot read cannot find "Close". Better: "Tap the X to go back to the rule cards." or a visible "Close"
   label on the button. Also: opened before any rule is tried, the summary asks "Which one would you pick for our
   class?" over a table of only "?" (same frame); ask that only once at least two rules have rows. Tag: general.

#### Polish

5. **Step 2 tap: the instruction plays before the confirmation** (src.html:1074-1076). Tapping a step 2 tile speaks
   "Tap Run to play our month." first and the tile's own name after it (`out1/make-d-end` vlog: 2131 ms "Tap Run...",
   4276 ms "The name stays out of the jar."). The child hears the next action, then the echo of what they tapped,
   and the Run instruction is buried. Better: tile name, then "Tap Run...". Tag: general.

6. **The name slip pops up over Week 1, far from the jar** (src.html:57, `.slip {left:145px; top:30px}`). In jar rules
   the slip always lands on day squares 1-2, covering day 1's face for the whole month while the jar sits at the far
   right (`out1/make-d-day1.png`, `make-d-day8.png`). Better: place it beside the jar (or the Leader spot) so the
   draw reads as coming out of the jar, and never over a calendar day. Tag: general.

7. **The third question reads differently on screen and in the voice** (src.html:846 vs L.q2). Chip: "Extra turns while
   a friend got none?"; hint and voice: "Did someone lead more than once while a friend got none?"; summary column:
   "Extra / none?" (`audit-r1/state-fair-c-1366x768.png`, `state-summary-1366x768.png`). POLISH: anything shown twice
   matches. Use one wording (the spoken one is clearer for grade 2); "Extra / none?" is cryptic as a header. Tag: general.

8. **Our chart fills in the answers before the child checks** (src.html:1239, `recordSummary()` at finish). As soon as
   a month ends, its Q1-Q3 row shows ✓/× from the data, so opening Our chart answers the three checks, including Q1,
   which is not visible on the chart itself. Toggling Bee also records a row for a rule nobody looked at
   (`out2/fair-summary-after`: "A · Bee sick" filled with no checks answered). Better: fill a cell once the child has
   answered that check. Tag: general.

9. **Projector reading size** (`audit-r1/state-fair-c-1920x1080.png`). At 1920x1080 the rule card names stay 12 px,
   the check questions 14 px and the evidence 12 px while the chart grows huge; from the back of a room the rule cards
   are unreadable. The 1600 px media query scales the chart and hint but not `.rule-pick`, `.check h2`, `.evidence`
   or `.verdict button`. Tag: general.

#### Nit

10. The first-in-line step icons (dots, ring, curl arrow, door bracket) are hard to tell apart at 680x425 rule cards
    (`audit-r1/state-fair-c-680x425.png`: A and B look the same). The voice covers it; a bigger difference in the
    arrow would help. Tag: general.

#### Checked and fine

- First screen (solo K): hint says what to do, Run stays disabled until both steps, first tile tap speaks its name
  (welcome skip is rule 16, not reported). Who overlay appears once and both answers land on "people made the rule".
- Motion off keeps time: 20 days took 8.7 s after the Run tap (1200 ms + 19 x 450 ms expected 9.75 s from the tap)
  (`make-calm-run`).
- Month result lines play whole and say the right thing (rule C: "Some friends led three times each. Nine friends
  never got a turn."; rule D: "Everyone got one turn."). Bee sick rule B gives Ant 2, Bee 0 with the ring.
- Changing both steps in Change a Step says "Two steps changed" and accepts either tile (`out1/change-both`).
- No console errors in any of my shots. Depth: rules C and D give a new month each time; Change a Step chains
  (each run becomes the new Before). Enough for a K-2 tool used across a few sessions.

#### Audit pilot

- Leads confirmed: none that matter for play. The 375x812 friend/count "overlaps" are by design (count sits in the
  button's corner, `state-changed-375x812.png` reads fine); the "text under 10 px" rows are icon-only buttons with
  font-size 0 (intended compact layout).
- Leads wrong: the "welcome not heard" rows for friend and tile first taps are BASELINE rule 16, the premise stays in
  the hint. The "has not led yet" 4 of 5 at a 2 s pace is the newer tap dropping the older one's tail, as the spec asks.
- Missed: finding 1 (feedback dropped behind the next question; its 2 s pace test only covered single controls, not a
  three-answer chain), finding 3 (re-tapping the chosen tile), findings 2 and 7 (visual and wording, out of its scope).

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: line-leader-picker (round 1)

Cold Teaching lens, 2026-11-06. Read spec.md, src.html, notes.md, BASELINE, REFINE and the shared audit
(S:/CurioClass-codex-scratch/line-leader-picker/audit-r1). My frames and logs:
S:/CurioClass-codex-scratch/line-leader-picker/teaching/frames (shots.json, shots2.json beside them).

Summary: no blockers. The core works: Run stays disabled until both steps are chosen, day 1 lights step 1 then
step 2, the Who overlay stamps "Made by our class", the stays-to-back change gives twenty 1s over Before outlines,
rule C shows Q1 yes and Q2 yes with the fSame line, Bee sick under B gives Bee 0 and Ant 2 (leaders 0,2,3,...,19,0,
confirmed in t-bee-sick-B-checks), verdicts are never marked. Recomputed: 20 x (19/20)^20 = 7.17. The problems are
in the Is It Fair? check flow and a few lines that say something false or misleading.

#### Findings

1. **Is It Fair?, Our chart (src.html:1239, 1355-1370).** The summary records Q1, Q2 and Q3 at month end, before
   any check is answered, so opening Our chart right after a rule card shows "Yes / Yes / Yes" for that rule while
   all three thumbs are still untouched. Q1 (a rule-level fact the chart cannot show) is handed over outright.
   Seen: frames/t-summary-before-checks.png (checks [null,null,null], row C all Yes). Better: fill a cell only once
   that check is answered ("?" until then). Level: should fix. Tag: general.

2. **Is It Fair?, thumbs mean two things (src.html:854-855, 861-862).** The three checks use thumbs up for "yes" and
   thumbs down for "no", and the verdict uses thumbs up for Fair and thumbs down for Not fair. For rule A the
   matching check answers are down, up, up (yes, a friend was left out), then the class is asked for a thumbs
   verdict. A K-2 child reads thumbs up as "good"; "thumbs up, yes a friend was left out" fights that, and it blurs
   the line the tool wants kept between the chart's facts and the student's own fairness call. Seen:
   frames/t-bee-sick-B-checks.png (three thumbs-up checks beside a thumbs-up Fair button). Better: yes / no
   pictures for the checks (check mark and cross, or a nodding and a shaking head), thumbs only for the verdict.
   Level: should fix. Tag: general.

3. **Is It Fair?, Q1 mismatch says "Look at the chart again." (src.html:1340).** Every check answer that does not
   match gets that line. But Q1 is the rule's own fact (spec: "Q1 is the rule's own fact"); for rule C the chart
   shows 3 stickers beside 0, which supports the "no" a child just gave. Sending them back to the chart for Q1
   teaches the opposite of fSame. Seen in code: the agree/look choice is the same for checks 0 to 2. Better: for Q1
   a mismatch line about the rule ("Think about the rule, not this month's stickers."), then the q1 rule line.
   Level: should fix. Tag: general.

4. **Is It Fair?, feedback arrives after the next question (src.html:1334-1340).** Answering a check speaks the next
   question first (now:true), then "The chart agrees." plus the evidence line for the check just answered. Log with
   9 s gaps (t-check-order, shots2.json): after Q1 the order is "Was any friend left out? ..." then "The chart
   agrees. Only the friend at the front can lead...". After Q3 the verdict prompt plays before Q3's feedback
   (t-fair-C-all-thumbs). A pre-reader hears the answer to question 1 while looking at question 2. Better: feedback
   first, then the next question. Level: should fix. Tag: general.

5. **Change a Step, Which step: the old tile is called unchanged (src.html:1043-1047, L.chSame line 636).** After
   "Which step made the month change? Tap that step.", tapping "Stays at the front" (the Before step, in the
   changed slot) gets "That step stayed the same. Look for the step you changed." That is false: it is the very
   step that changed. Seen: t-which-old-tile log (tile-2 tap). Also, while the question is open every tile tap is
   captured as an answer, so a child cannot try another change until they find the pressed new tile. Better: judge
   by slot (any tile in a changed slot is right: "Yes, step 2 changed from stays at the front to goes to the
   back"), or give the old tile a line saying it was the Before step. Level: should fix. Tag: general.

6. **Is It Fair?, Bee's sick line implies a cause it did not have (src.html:1253-1256).** With Bee sick, tapping Bee
   at 0 always says "Bee was home sick on day two." then the left-out line, under every rule. Under rule A (Ant 20,
   everyone else 0) and often under rule C, Bee's 0 has nothing to do with the sick day. Seen: t-bee-sick-A log
   ("Bee. never led this month. Bee was home sick on day two. That friend waited all month..." with Ant 20).
   E2-ALG-IM-03 is about telling the rule's effect from the situation's effect, so the line should not blur them.
   Better: play beeSick only when the sick day changed Bee's count (rule B), or under A say Bee would not have led
   under this rule even at school. Level: should fix. Tag: general.

7. **Is It Fair?, New month erases the class's call (src.html:1034, 1239, 1355-1358); notes.md "Modes".** New month
   on a draw rule (and re-tapping any rule card) clears the verdict and overwrites the summary row, so Our chart
   loses the call the class already made. Seen: t-newmonth-wipes-call (summary C verdict false, then null after New
   month). notes.md says Our chart "records the outcomes and the class's own calls for this page load", which is
   not true after a New month. Better: keep the last verdict per rule (or show the old call beside "new month"),
   and make notes match. Level: should fix. Tag: general.

8. **Is It Fair?, the sick day is not visible on the chart (src.html:984; day strip hidden at 951).** Bee in bed
   shows only while exactly 2 days are done; the fair month runs at 75 ms a day, and in a finished month Bee's
   column looks like any left-out column. With the day strip hidden, a teacher cannot point at why Ant has 2 and
   Bee 0 (the turn passed on day 2, Ant led again on day 20). Seen: frames/t-bee-sick-B-checks.png (no bed mark, no
   day record). Better: a small bed mark on Bee's column in sick months and a one-line day readout ("Day 2: Bee
   away, Cat led. Day 20: Ant again."). Level: polish. Tag: general.

9. **Make a Rule, Who closed unanswered never returns (src.html:1227-1233, 1274).** Close (x) dismisses the only
   EK-ALG-IM-03 question for the whole page load (whoShown stays true). A teacher who closes it by accident loses
   the stamp moment. Better: offer it again after the next month until it is answered. Level: polish. Tag: general.

10. **Is It Fair?, Q2 evidence line is singular (src.html:1329, L.left).** The Q2 detail is always "That friend
    waited all month and never led...", even for rule A with 19 friends at 0. Seen: t-fair-C-all-thumbs log (rule
    A, Q2). Better: a Q2 line with the count ("Nineteen friends never led."), keeping "Being left out feels sad."
    Level: polish. Tag: general.

11. **Is It Fair?, rule B's Q1 line answers a different question (L.q1B, line 638).** Q1 asks "Same chance for
    every friend?" and rule B's line is "Everyone gets a turn, one after another." That is the turn-for-everyone
    idea the tool separates from same chance (fSame). Better: "Every friend's place comes to the front in turn, so
    everyone has the same chance." Level: polish. Tag: general.

12. **Our chart column "Extra / none?" (src.html:527).** Cryptic for grade 2 next to the spoken "Did someone lead
    more than once while a friend got none?". Better: the same star-star-bar-empty picture used on the check, or
    "Extra turns?". Level: nit. Tag: general.

Standards: EK (choose two steps, Who question, stamp), E1 (change a step, Before outlines, Which step) and E2 (three
checks, own verdict, Bee's sick day) are each exercised by something the student does and sees; no code is only
mentioned. Findings 1 to 7 weaken E1 and E2 delivery. Teacher notes: What it teaches, Key skills and Support at home
are true of this tool and doable tonight; nothing sensitive for rule 8. Nothing cultural, Native or hard history: no
sensitivity review needed.

#### Audit pilot

- Leads confirmed: none in the Teaching lens's scope (its rows are layout and voice timing; Play and Craft own the
  375x812 count and face overlaps and the 0 px header text).
- Leads wrong or excused: "welcome not heard after a first tile or friend tap" is excused by BASELINE rule 16; the
  premise stays on the rule card's job line and returns in the Who line.
- What it missed: the summary giveaway before any check (1), the thumbs double meaning (2), Q1 "look at the chart"
  (3), feedback after the next question (4; its walk has no answer sequence), the false "stayed the same" line (5),
  Bee's sick line under rule A (6) and New month erasing the call (7). All are states or words it cannot judge.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: line-leader-picker (Codex fix, round 1)

The user's Curiosity brief takes precedence over the legacy lesson spec and Refine. The workbench has no kit header, grade tags, forced quiz, answer gate, score, level or finish screen. The existing evidence questions are optional observations in any order; both fairness opinions are independent and ungraded. After the first quiet hint, speech is requested with Read. The exact automatic-narration requests below are left explicitly NOT FIXED instead of claiming a lesson-style pass.

Evidence paths below are relative to `_scratch/line-leader-picker/`. Named JSON files in that Scratch root record the numbers or Read log for the corresponding frames. Original source is preserved as `src-before.html`; Refine was not edited.

#### Blocker
None in Refine.

#### Should fix
1. **NOT FIXED as prescribed: automatic three-answer narration chain.** Reproduced dropped feedback and evidence at both 3.5 s and 6 s in `before-voice-3.5.json` / `before-voice-6.json`. The Curiosity replacement removes automatic questions and answer grading. Repeated held-click chains at both paces have zero automatic speech entries, with observations `[false,true,true]` and matching facts. See `after-chain-3.5.json`, `after-chain-6.json` and their frames in `after-break-frames/`. Read speaks the current evidence. No automatic chain is claimed.
2. **FIXED: premature Our chart facts.** Before: C had `[true,true,true]` with all observations null. After: summaries is `{}` before any inspection, and the first inspection records `[true,null,null]`. See `before-summary.json`, `after-summary.json` and `after-functional-frames/after-summary.png`. A freely chosen fairness call may create a row with unknown facts, since Curiosity calls do not require the observations.
3. **FIXED: visible evidence and chosen verdict.** Q1 highlights both step pictures on the selected rule; Q2 rings empty columns; Q3 also marks the tallest counts. Each inspected chip has a 24 × 24 px yes/no fact mark. Both verdicts have a blue outline and white inset when pressed. See `after-functional-frames/after-rule-read.png`, `after-sizes-frames/after-fair-680.png`, and final re-shots `after-compact-frames/final-fair-680.png` / `final-fair-375.png`. The marks show facts, never correctness grades.
4. **FIXED: two meanings for thumbs.** Evidence controls now use check/cross pictures with Yes/No accessible names; thumbs remain only on fairness opinions. fChecks and q0/q1/q2 name the new controls, with the bank matching runtime. Compare `before-frames/before-mismatch.png` with `after-compact-frames/final-fair-680.png`; see `validation.json`.
5. **FIXED: Q1 points to the rule.** A mismatch readout says “Think about the rule, not this month's stickers.” followed by the rule line. `before-rule-mismatch.json` captured the old chart instruction. `after-rule-read.json` records the new exact Read sequence; the rule's step pictures are highlighted in its frame at 1366 × 768.
6. **FIXED: Q2 names the actual count.** Seed 7 has six empty columns. Read requests “Six friends never got a turn.”, then “Being left out feels sad.”, then the separate same-chance explanation for C. `after-count-read.json` and `after-functional-frames/after-count-read.png` prove it. The singular classmate line remains only in classmate readouts.
7. **FIXED: the old tile identifies the changed slot.** Before: tapping old Stays at the front left `which:true`, glow 0. After: glow 2 marks the new Goes to the back tile, the twenty counts remain 1, and the optional inspection ends. See `before-old-tile.json`, `after-old-tile.json` and their 1366 × 768 frames. Any first inspection can leave the comparison prompt; there is no correct-answer gate.
8. **FIXED: selected tile re-taps preserve the month.** Before: both modes lost all days and counts. After: Change retains Ant 20 and no new Before; Make retains all twenty days. Five further step-1 re-taps also retain twenty days. See `before-retap.json`, `after-retap.json`, `final-state-patterns.json` and their frames. Tile names remain available through Read; an unchanged Change tile adds the specified same-step explanation.
9. **FIXED: Bee's absence has a counterfactual test.** The same uniform day-2 draw is compared with the all-present jar. Bee's absence sentence is included only when Bee has zero turns and would otherwise have led. A omits it, B includes it, and C follows the paired draw. `after-bee.json` records A/B/C/D. `after-model.json` checks 1,000 paired C months: zero mismatches, 15 affected zeros and 382 unaffected zeros. Counts and the persistent bed mark are visible in `after-functional-frames/after-bee.png`.
10. **FIXED: saved calls survive new months.** A saved false verdict remains false after New month and the next inspection. Additional card re-taps, attendance switches and mode round trips preserve healthy false and sick true independently. See `before-verdict.json`, `after-verdict.json`, `final-state-patterns.json` and the summary frames.
11. **FIXED: summary wording and Close label.** An empty board uses “Check a rule card first. Its row fills in here.”; the invitation appears only after two rows have a verdict. The return instruction names X, and Close is visible at 1366 and above. See `after-summary-empty.json`, `final-summary-two.json`, `after-functional-frames/after-summary-empty.png` and `after-values-frames/final-summary-two.png`.
12. **FIXED: compact stickers are readable.** Before: 680 stars were 8 × 4.39 px, 800 stars 8 × 6.25 px, phone stars 7 × 4.39 px. After: both gold and all twenty dashed Before stickers are 12 × 12 px at 680 × 425, 800 × 500 and 375 × 812. Dense short cells reserve space for the count instead of drawing stars through it. See `before-stars-680.json`, `before-stars-800.json`, `before-phone-fixed.json`, `after-fair-375.json`, `final-before-680.json`, `final-before-800.json`, `final-before-375.json`, and the matching final frames in `after-values-frames/`.

#### Polish accepted
1. **NOT FIXED as automatic speech; Read order FIXED.** The tile name precedes Tap Run in `after-tile-read.json`: “The leader goes to the back of the line. Tap Run to play our month.” No automatic how-to queue is retained, following the Curiosity voice rule.
2. **FIXED: Q3 wording.** The chip uses the full spoken question. Our chart uses the same picture with “Led more, one none?”. See `after-compact-frames/final-fair-375.png` and `after-values-frames/final-summary-two.png`.
3. **FIXED: name slip placement.** The slip is positioned inside the jar scene. At 1366 × 768 its rectangle has zero intersections with all twenty calendar squares. See `after-jar-slip.json` and its frame in `after-break-frames/`.
4. **FIXED: projector type.** At 1920 × 1080, rule names are 18 px, questions 20 px, evidence 17 px, verdicts 19 px. See `after-projector.json` and `after-functional-frames/after-projector.png`.
5. **FIXED: Fair hint names visible material.** Fair uses fChecks while its month runs, rather than naming the hidden machine. See `after-break-frames/after-model.png` and `after-model.json`.
6. **FIXED: Bee's bed remains visible.** The bed mark is tied to the switch, rather than exactly two completed days. All four finished-rule tests have `bed:true` in `after-bee.json`.
7. **NOT FIXED: re-offer the Who quiz.** The forced Who overlay was removed under the Curiosity brief. Its explanation is in the Manual and the authored rule card stamps without an answer. `after-retap.json` and `after-make-calm.json` show no Who overlay after finished months. Reintroducing an unanswered quiz would violate the user's instruction.
8. **FIXED: Rule B's explanation.** `final-B-read.json` records “Every friend comes to the front in turn, so everyone has the same chance.” at the B rule inspection.
9. **FIXED: accepted nits.** tie11 through tie20, most1 and zero20 were removed. All four compact utilities have title labels. Run's darker gradient top gives 5.218:1 white-text contrast, formerly 4.40:1. See `validation.json`; final compact geometry records every utility visible and tappable.

#### Settled calls
- Designed count/classmate overlap and icon-only font-size-zero controls remain intentional; the animal cast and all 47 existing paintings were kept.
- The older welcome-cut cases are superseded by one quiet first hint and explicit Read. No welcome screen or new welcome requirement was added.
- Classmate narration is now its current readout plus Read; there is no queued tail to race a later tap.
- Q2 uses the actual zero-count sequence, as settled in should fix 6.
- Thumbs remain on verdicts; observation controls and fact markers use yes/no pictures.
- Our chart displays data facts, never right/wrong marks for observations or verdicts. Unknown cells stay unknown until inspected in that recorded month. The previous recorded month stays until replaced.
- Keyboard focus, Motion off, sixty-pixel controls and the offline bundle were rechecked. The header-only audit discovery limitation is documented below rather than restoring a kit header.

#### Cheats tried
- All No on C still shows the actual Yes/Yes/Yes facts, empty columns and tallest counts; it earns no score or pass.
- Fair before inspecting any question is allowed and ungraded. Q3 can be inspected first. `after-free-explore.json` records all three evidence controls enabled independently.
- A's deliberately inaccurate first Yes records the data's No without awarding anything. `final-summary-two.json` keeps the student's Fair opinion distinct from that fact.
- Repeating selected step 1 five times preserves the twenty-day result. Card re-taps, switching Bee twice, and mode round trips preserve the separate saved calls. `final-state-patterns.json`.
- Interpreter stress: 6,000 A/B/D months with/without absence and 1,000 C counterfactual pairs, zero mismatches. `after-model.json`. Independent Python sampling and occupancy arithmetic agree in `validation.json`.

#### Voice walk
- Read log requests, each once at its relevant inspection: Q1 rule correction plus C rule line; six-friend count plus feelings plus same-chance line; chosen tile name then Run; B's equal-chance line; two-row summary invitation and X return instruction. Evidence: `after-rule-read.json`, `after-count-read.json`, `after-tile-read.json`, `final-B-read.json`, `final-summary-two.json`.
- Held-click chains at 3.5 s and 6 s have zero automatic question or feedback entries. This proves the Curiosity replacement, not the Refine's requested automatic chain.
- `voice/lines.json` equals allLines(): 165 unique lines. Browser voice is the current fallback; missing recorded clips were reported by the bundler and no recorded-take quality claim is made.

#### Engine changes wanted
`scripts/audit_tool.py`, MODES_JS: add `nav .workstations button` to its header-only mode selectors. The current audit cannot automatically discover these Curiosity workstations. Both other workstations have explicit audit states; its automatic per-mode control walk remains limited. No shared script or kit file was edited.

#### Audit
The single full audit completed within its 2,400-second limit, with 71 inspected frames and 267 mechanical leads. Report: `fix-audit/audit.md`; every bullet has a disposition in `audit-disposition.md`. No full audit was repeated. The final bundle differs from the audit snapshot only by the scoped geometry/accessibility repairs below; both hashes are recorded in `final-validation.json`.

- **FIXED: 1000 × 625 New month clipping.** The short side panel now reserves 264 px. New month ends at x=995 within the 1000 px viewport. `flow-fair-1000.json` and `after-flow-frames/flow-fair-1000.png`.
- **FIXED: marks touching wrapped headings at 760 and 375.** Marks now live in the diagram row, with enough row height to contain them. All three heading/mark intersections are zero at 680, 800, 760, 1000, 1366, 1920 and 375. All markers remain 24 × 24 px; all tested controls are visible, at least 60 px and tappable. `flow-fair-*.json` and `after-flow-frames/`.
- **FIXED: projector Bee caption/On-Off overlap.** The switch uses separate grid rows for state and caption. Intersection is zero for both On and Off at 1920 × 1080. Main projector type remains 18/20/17/19 px. `audit-fixed-bee-False.json`, `audit-fixed-bee-True.json` and matching `after-audit-frames/` images.
- **FIXED: Manual close/heading overlap and covered keyboard targets.** A sixty-pixel title row gives zero close/heading intersection at 680, 1366 and 375. The open drawer makes the workbench inert and keeps Tab inside; Escape restores the workbench and focus to Manual. `audit-fixed-manual-*.json` and the Manual frames in `after-audit-frames/`.
- **Intentional: compact count/button overlap.** The readout belongs inside the large classmate hit area; count text and the painted classmate remain visually separate. This is the settled compact-bank pattern, including the blue Before numbers.
- **Intentional: font-size-zero utilities.** Their visible icons, accessible names and title labels remain. **Intentional: Manual covering #board.** The requested drawer covers the workbench while open; closing restores it.
- **Settled: three first-hint cuts on quick mode taps.** BASELINE 16 permits these. There are no mode welcomes or automatic question chains to restore.
- The 29-control single-click/keyboard walk had no console errors or lost-focus failures. Ten repeated-input checks passed. Final resize stress had no exceptions or controls left disabled; Motion off had no endless animation.
- After the audit, only affected geometry was re-shot: `after-audit-frames/` and `after-flow-frames/`. An intermediate phone placement still overlapped Q3 by 48 square pixels; the structural diagram-row repair reduced it to zero. Gold and Before stickers remain 12 × 12 px at all three named compact sizes, including a full twenty-star phone column.
- `final-validation.json` records all final assertions, source/bundle hashes, unchanged Refine hash, and closed ports 9910, 9911 and 8715. No commits were made. Generated host.html was removed.

#### The real material
- Curio Class, Line Leader Picker, `tools/line-leader-picker/spec.md`: authored fictional animal class, twenty-day model and four rule definitions. Content CC BY 4.0, as stated in the original tool's licence header. Interpreter `src.html`: MIT. Named in the Manual and tool.draft.json.
- Existing illustration collection: “Illustrations generated with OpenAI gpt-image, edited for Curio Class”; supplied Curio Class content, CC BY 4.0. No art downloaded, regenerated or removed. Jar paintings are explicitly schematic; chart counts are exact.
- No empirical dataset, new real-world fact, quoted standards text or outside download was added. No data-gathering time was used. Model results were checked against the independent MIT Python implementation in `validate.py`: expected C zeros 7.169718448, sample mean 7.171 over 10,000 months. The browser interpreter gave 7.14 over a separate 1,000 seeds. These are model checks, not two empirical sources.
- Runtime network resource list is empty in `final-state-patterns.json`. The bundle is 1,252,995 bytes and self-contained. Source licence references were checked in the existing local files on 2026-11-06.

#### Curiosity decisions and limits
- No unattended question was sent. The brief determined the choices: explicit Read, optional evidence, no quiz gate, wooden instrument controls, Manual and engraved plate, no invented catalogue number.
- The legacy spec and concepts file have no Line Leader Curiosity entry or plate number. `curiosity:true`, `plate:null`; the visible plate omits an unassigned number. The owner must assign that metadata later.
- Lesson-creep search: “sticker” names turn-count marks and animation helpers, never rewards. “grade” occurs only in the Manual's statement that observations are not graded. No goal, score, level, badge, finish screen or quiz was added. Program step numbers are the two executable instructions, not lesson progress.

#### Short test
- Would a kid open it without an assignment? Plausible from the animal cast and immediate rule changes; not independently validated in this fix.
- Would an adult play for fun? Uncertain. The replacement/rotation comparisons and counterfactuals are interesting, but the supplied four-rule scope is limited.
- Is the real material the interface? Yes: the executable rules, actual turn counts and Before outlines are the working material.
- Does it work without a score or finish line? Yes. No answer or verdict is required to continue exploring.
- No new ten-minute human-play validation or owner desk-review approval is claimed. The four reference instruments were opened and used; their frames are in `after-break-frames-contact.jpg`.

#### Frames looked at
All before and targeted-after PNGs were inspected directly or in the contact sheets for `before-frames`, `after-functional-frames`, `after-sizes-frames`, `after-break-frames` and `after-compact-frames`; successful phone reproduction is in `before-phone-frames/`. Final values, all 71 audit frames, and all scoped repair frames were inspected in their contact sheets and selected full frames. The current final chart/evidence frames are in `after-flow-frames/`. An initial phone harness lookup used the outer window incorrectly; its successful re-run supplied the phone numbers above. Initial host favicon 404s were harness-only and corrected for subsequent drives.

#### Left open
- The exact automatic narration chain, automatic tile/how queue, and returning Who quiz are intentionally not implemented; the Curiosity brief wins.
- The Curiosity plate number and concept entry are absent from the supplied spec. No number was invented.
- Recorded narration remains absent; Read uses browser voice. No recording or installation was attempted.
- The audit engine still discovers modes through header selectors. Explicit workstation states and targeted drives cover the other workstations; a full automatic per-mode control walk is not claimed.
- A new ten-minute human-play appeal check was not validated; the short-test answers above state that limit.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: Line Leader Picker

#### Structure
src.html has tool-local wooden controls, the classroom chart, two-step rule desk, optional evidence cards, Our chart and the lower-left Manual. kit/curio.js supplies Motion, Sound and Read. There is no kit stylesheet or header. Workstations keep independent state for this page load.

drawDay is the single interpreter. Counts, stickers and evidence use its generated days. A coupled all-present day-2 draw records whether Bee's absence changed her turn. Before is captured only on a genuine edit of a finished month. Re-tapping a selected instruction preserves the month and Before.

The optional comparison inspection judges a changed slot, so either old or new tile identifies it. Any first inspection leaves that state; there is no required correct path. Evidence cards and both fairness opinions are independent controls available after a month appears. A fact mark always describes evidence, never the tapped answer's correctness. recordSummary preserves an old verdict when the current month has no new verdict. Sick and healthy rows use separate keys.

#### Voice
Curio.voice owns Read and its log. The first quiet hint may speak once. Later interactions update readParts and the readout, without queuing automatic questions or lessons. Read speaks the parts in order: tile name before Run, Q1 about the rule, Q2's actual zero count before the feelings line. voice/lines.json equals allLines(). Browser narration is the current fallback; recordings remain the owner's later workflow.

Automatic three-answer narration and the unanswered Who quiz from the older review are superseded by the user's Curiosity instruction. polish.md records those departures. No kit engine changes were needed.

#### Layout
Original paintings, palette, calendar and all 20 classmates remain. Compact ordinary cells retain large classmates beside 12-pixel sticker rows. Cells with more than six current or Before stickers use the full cell width for short rows. layoutStars recalculates columns on resize. Dashed blue outlines remain distinguishable from gold fills at shared coordinates.

The name slip belongs to the jar scene, never the calendar. Bee's bed mark persists while the sick switch is on. Our chart has a visible Close label at 1366 and above. The lower-left Manual has a sixty-pixel target.

#### Sources and metadata
Manual and tool.draft.json name the authored Curio Class model (CC BY 4.0), interpreter (MIT) and existing illustration credit. No outside data or quoted standards wording was imported. Scratch contains independent arithmetic and runtime evidence. The old spec has no Curiosity number or concept entry; plate is null instead of an invented catalogue number.

#### Sensitivity
Imaginary animals only. Bee's one-day absence has no medical claim. Waiting poses show an outcome, never a judgement about a child. Both fairness opinions remain available and ungraded.

#### Engine changes wanted
Shared kit, docs and audit scripts were untouched. Audit compatibility wanted: scripts/audit_tool.py, MODES_JS, include `nav .workstations button` alongside the current header-only selectors. A Curiosity has no kit header, so the current selector misses its workstations. Explicit audit states cover both other workstations in this fix; the automatic per-mode control walk remains limited to the initial workstation.

#### Validation
See polish.md for before/after evidence and the single final audit. Prior build and cold-review reports remain historical. Refine and its lens files were not edited.

#### Final geometry and audit disposition
The single full audit completed with 71 frames. The four confirmed geometry causes were repaired and re-shot, with no second full audit. See polish.md and _scratch/line-leader-picker/audit-disposition.md. Source and audit-snapshot hashes differ explicitly in final-validation.json.

Fact marks are part of the diagram row, whose minimum height contains a 24-pixel marker. This avoids dependence on a heading's wrapped height. Short layouts reserve a 264-pixel side panel. Compact transport and chart utilities sit on the wooden rail. In a dense cell under 68 pixels high, four grid positions reserve room for the count and small portrait; twenty 12-pixel stars remain visible.

The Manual reserves a sixty-pixel title row. It makes the workbench inert while open, contains Tab focus, and restores focus on Escape or Close. The projector sick switch separates its On/Off state and caption in a two-row grid. These are tool-local repairs.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
