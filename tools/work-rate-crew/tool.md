# Work Rate Crew: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: work-rate-crew

#### Built
Build only, in S:\CurioClass-codex. Writes confined to tools/work-rate-crew and _scratch/work-rate-crew.
No commits, shared file changes, deployment or polish round. Draft stage is built.
Three modes: five dispatch calls, the rational rewrite quote sheet, and four practice-sheet audits.
Crew taps place painted gear on the street immediately. Textured paint bands meet across the actual house cutout.
Later calls introduce price/deadline comparisons, an unknown crew, a delayed start and two possible roots.
Verified jobs earn device-local board stamps. Deadline trials produce a comparison ledger before the final quote.
Source is readable: 1,450 lines, longest line 150 characters. Offline bundle: 696,056 bytes, about 696 KB or 680 KiB.
Build manifest and exact file hashes: _scratch/work-rate-crew/build-manifest.json.

#### Numbers check
Independently recomputed before building with Fraction; repeated with Sympy in spec-verification.json.
- Ana + Ben: 5/12 house/hour; 12/5 hours = 2.4 hours = 2 h 24 min. Five hours means 25/12 houses, uncapped.
- Deadline: AB 12/5 h, $336, yes; AC 3 h, $360, yes; BC 4 h, $320, no; ABC 2 h, $340, yes.
- Dee takes 12 h alone. Late-start finish is 14/5 h after 8:00, or 10:48.
- Sprayer roots: 6 and 4/5. The latter gives -6/5 h for the sprayer. Valid times: brush 6 h, sprayer 4 h.
- Quote identity simplifies to zero. T(12)=3; T(0.5)=4/9; T(60)=15/4; T<2 exactly for 0<x<4; T<4 for x>0.
- Audit solution sets: empty, empty, {1/2}, {3}. Sheet 3 root 1 is undefined; sheet 4 original sides both equal 3/2.
- Actual contrast: brand/panel 10.90, brand/secondary 10.59, brand ink/brand 11.52, paper ink 14.99.
  First two differ from the spec's ratios because actual panel colors differ; all remain above AA.
- Paint is one second per modeled hour, capped at four seconds. Motion-off run measured 2407.7 ms for 2.4 h.

#### Facts checked
- Combined constant work rates and reciprocal-time modeling: supplied OpenStax Intermediate Algebra 2e, 7.5.
- Original-domain restrictions and substitution for extraneous roots: supplied OpenStax 7.4.
- Rational rewriting and addition: supplied CCSS HSA A-APR.D.6 and D.7; equation checking: A-REI.A.2.
- Every displayed job number, cost and worksheet answer: independent exact computations above.
- Names, company, jobs, rates and prices are fictional and labeled made-up company. Constant rates are stated.
- Quote graph and paint readouts derive from the same exact rates as the checks. Names accompany crew colors.
- Device-only progress statement matches localStorage; no analytics or network code added.
No current market-price, professional painting, safety or cultural claims are taught.

#### Break it
Browser functional checks: 195/195 in functional-final-results.json, before the added proof gate.
Strengthened audit checks: 22/22 in proof-final-results.json and again post-proof-results.json.
- Rate: tried copied sums, averages, integers, +0 shortcuts and wrong fractions. Only a combined single fraction passes;
  unknown crew calls require the symbolic combined fraction.
- Equation: tried identities, known-root-only equations, added roots, domain holes at solutions and code strings.
  Rejected. No eval. Reduced polynomial comparison plus five exact probes accepts equivalent equations.
- Solve: tried 5 h, negative/empty/nonfinite inputs, wrong units and near values. Five is refused as a solution.
  An uncredited five-hour simulation caps the wall at one and reports 25/12 houses.
- Stamps: Paint before verification and repeated Paint cannot earn completion. Crew changes invalidate calculations.
  Both roots and matching reasons are required for the sprayer; calling 4/5 a denominator-zero root fails.
- Deadline: cheapest choice alone cannot pass; all three pair trials must be checked and painted, then cost and pair filed.
  AC at exactly 3 h passes; BC's cheaper $320 quote fails the deadline.
- Quote: swept all 120 slider values and tried sign/verdict choices. Sweeping cannot complete the rewrite or proof.
  Wrong q/r and missing or wrong threshold/sign fail. Exact 4, -16 and positive-remainder reasoning pass.
- Audit: verdict guessing initially passed valid-only sheets. Fixed by requiring substitution evidence for every root.
  Retested every verdict combination with empty proof, wrong denominator, wrong order and wrong equal values: fail.
  Correct zero-denominator expressions or exact equal-side values pass. Revealed substitution is an intentional worked check.
- Persistence: reload retains verified completion; Clear removes it. Malformed storage is guarded with try/catch.
- Interruptions: crew/call/mode/Paint changes cancel old runs immediately. Held crew interruption leaves new state, zero paint.
The public test API is not a security boundary; normal UI paths enforce the learning gates.

#### Voice walk
Curio.voice, 18 fixed lines, lively-host metadata. Runtime inventory matches voice/lines.json exactly.
No audio recorded, as instructed. Required Chrome driver muted audio: logs verify scheduling, not audible voice quality.
Held-click main walk at about 2 s pace: assign -> rate -> solve -> paint -> done, all started as spoken.
Intervening state changes cancel obsolete instructions. Welcome is stale on first crew assignment by spec.
Side walk: wQuote -> wAudit -> audit. Queued quote-reason line dropped on leaving Quote sheet, correctly stale.
Read speaks the current mode's visible hint through the custom read function. Hints change synchronously with state.
Audit found invalid Paint/repeated empty Clear cutting welcome. Fixed; both quick-tap rechecks preserve wCalls.
Rapidly assigning then unassigning a crew cancels its obsolete assignment instruction, intentionally.
Full logs and keyboard/storage results: walk-results.json. Rechecks: post-quick-paint.json and post-quick-clear.json.

#### Feel check
Played the five-call calculation path and all audits; held main and side walks exercised actual controls.
Best moment: gold and blue fronts meet on textured siding at 2.40 h, matching the prediction and earning the job.
Flattest moment 1: assigning crews initially felt like editing numbers. Added on-site gear, named pills, status and tones.
Flattest moment 2: deadline repeated forms crowded the board. Trials now build an earned ledger for the final choice;
short layouts put time, cost and deadline side by side, preserving the house and the next instruction.
Compared bar-comparison.png against Beat Lab; also opened Snowy Mail Route before building. The rich place and
simulation payoff retain a restrained Grade 11 workplace tone. No confetti or unrelated game mechanics.

#### Done when
1. PASS: 5/12, 12/5, 2.4 and 2 h 24 min accepted; 5 refused; verified run ends at exactly one. Functional checks and frames.
2. PASS: AC exactly 3 h qualifies; AB $336 wins; BC fails; all-pair and optional ABC tests passed.
3. PASS: late equation and equivalents pass; 14/5 and 10:48 accepted. Functional checks.
4. PASS: both 6 and 4/5 required; second root needs negative time. Wrong reason and incomplete root tests fail.
5. PASS: q=4, r=-16; x=12 reads 3; 120-value sweep stays below 4; real drag reaches x=60, T=15/4.
6. PASS: all four audit verdicts and denominator/equal-side evidence checked; proof gate passes 22/22 probes.
7. PASS: 1366x768 and 1000x625 frames inspected: house, graph and worksheet dominate their respective modes.
8. PASS: live controls cancel painting; resize stress has no exception or locked controls. Held interruption inspected.
9. PASS: multiply bands retain siding; every crew color has a named pill. Mid-paint and grayscale frames inspected.
10. PASS for exercised paths: reload/Clear, keyboard Enter and slider arrows, all standard sizes, 375 iframe host,
    clean console/no tool network. Final keyboard check: focus Paint, completed true, painted 1.
    Full audit predates final repairs; this does not claim a clean final full audit.

#### Wave lessons
- Hint and voice: PASS, current hints, Read, held walks and quick-action repairs; stale-context cancellations above.
- Focus and layout: PASS, no load focus; stable controls; Enter advance preserves focus on Paint/root controls without scroll.
- Sizes: PASS in inspected matrix and affected reshoots; header targets at least 44 px; smallest hints visible after repair.
- No giveaways: PASS for UI cheats tested, including equation shortcuts, slider sweeping and empty audit proof.
- Honest numbers: PASS, fictional constant rates stated; house cap separated from uncapped readout; fractions retained.
- Standards: PASS, students add rational rates, rewrite q+r/b, solve rational equations and test roots in the original.
- Motion off: PASS, measured duration retained with calm progress bar; audit reports no endless animation.
- Short choices visible: PASS, crews/root verdicts in view; final deadline phone and 680/800 frames inspected.
- Resize mid-animation: PASS, audit stress clean; simulation state independent of layout.
- Welcome after first tap: PASS with spec stale rule; assignment instruction replaces welcome, no late welcome queued.
- Unknown shown unknown: PASS, unassigned rate is ? + ?; unknown duration remains x rather than a revealed answer.
- One look, one meaning: PASS, consistent crew colors with names; grayscale frame inspected.
- Badge says truth: PASS, assigned/verified/done distinct; unverified simulations cannot earn a stamp.
- Reversible hint: PASS, crew/mode changes restore the relevant step and instruction immediately.
- No answer by copying words: PASS for completion gates; combine original rates and supply typed proof/equation.

#### Audit leads
Single audit finished within 40 minutes: 53 leads, 73 PNGs, no runtime exceptions, resize locks or endless calm motion.
audit/audit.md and audit/host/tool.html preserve the pre-repair snapshot. No second full audit was run.
All 53 leads are covered below; counts match the report's grouped lead lines.
| Leads | Disposition |
| --- | --- |
| 2 small header targets | Fixed Calls and Read to at least 44x44; final 680 metrics confirm. |
| 8 answer-name leads | Existing labels supplemented with step-specific aria-label; targeted metrics confirm. |
| 10 small footer-stamp leads | Fixed 9 px to 10 px at 760 and 375; inspected post frames. |
| 3 phone title/picker overlaps | Replaced padded title bounds with available width; default/deadline/sprayer checked. |
| 3 Quote under2-name leads | Added explicit threshold name; shared rendering covers mode/min/max. |
| 1 cost-name lead | Added explicit cost name; final deadline metrics confirm. |
| 1 after-paint stamp lead | Same 10 px footer rule, including Job done. |
| 5 hidden Calls-hint leads in other modes | Helper false positives: hidden #hint selected. Visible hints and Read work; handoff requests helper fix. |
| 1 deadline hint/footer overlap | Three-column short form; final 680 hint ends y355, before footer y373. |
| 4 deadline crew/footer overlaps | Compact cards; final 800 Cy ends y388, before footer y445. |
| 2 deadline Clear below-fold leads | Phone/760 form compacted; controls and Clear visible in inspected host frames. |
| 7 sprayer overlap/covered-hint leads | Horizontal verdict/reason rows, compact crew/readout; 800 frame has hint/results above footer. |
| 2 first-crew welcome leads | Intentional stale-on-assignment rule; first action speaks its own instruction. |
| 2 quick crew how-line cuts | Unassignment invalidates instruction; hint returns to assign crews. |
| 2 quick Paint/Clear welcome cuts | Fixed invalid Paint/unchanged empty Clear; quick logs show welcome with no cut. |
Five-repeat tests clean. Sound-off intentionally hushes narration. Read repeats the current hint on demand.
Targeted repairs checked afterward; final bundle differs from audit bundle, with both hashes in build-manifest.json.

#### Frames looked at
Full mode/size matrix shot once: 24 frames, including actual 375x812 iframe through host 8795. All inspected.
Affected layouts reshot locally. Earlier failed frames preserved; they do not represent final layout.
Inspected main/side walk frames and 8 special frames: grayscale, Motion off, interruption and quote extremes.
Inspected all 73 audit PNGs through 19 indexed contact pages; critical leads also opened full size.
Inspected all 12 post-audit frames and final four: deadline 680/800, keyboard completion and quote 680.
Evidence remains under _scratch/work-rate-crew; audit-contact-index.json maps audit contact pages.
Art contact sheet and Beat Lab comparison opened at final verification. Browser batches reported zero shot errors.

#### Art made
Eight new OpenAI gpt-image illustrations: street, cutout house, roller, brushes, ladder, can, sprayer and legal-pad paper.
Warm painted style, detailed clapboards, worn tools, afternoon light. No people; each asset has people:false.
New WebP art 319,430 bytes (319 KB); all nine preserved WebPs 352,702 bytes (353 KB). Voice assets 0 KB.
Bundle 696 KB against 2,000 KB goal. Existing unused dusk art preserved; not loaded by the tool.
Can and sprayer redrawn once each to remove green shadow artifacts. Final cutouts/contact sheet inspected.
Full prompts/provenance in art/prompts.json. Art processed only with scripts/art.py --rekey per asset.

#### Art still to paint
None. All eight specified assets present; no placeholders or people silhouettes.

#### Engine changes wanted
No runtime engine changes. Kit Curio.voice and graphing Plane/fn/label/trace used without shared edits.
Audit helper PAGE_JS should select the visible .hint instead of unconditional hidden Calls #hint.
Exact proposed lookup is in handoff.md. Shared script left untouched.

#### Left open
Cold reviewer should run a full audit on the final bundle; this build ran the mechanical audit only once.
Audio listening quality/bank-voice identity unassessed; browser fallback used because recording forbidden.
No unattended question sent. BASELINE w2-05 settles the open audit question in favor of labeled practice sheets.
Spec's 'never faster than fastest crew alone' comparison is reversed; implemented correct T<4 behavior.
Five-hour contradiction resolved as refused solution but allowed uncredited simulation.
Symbolic single-fraction rates used for unknown-time calls. Decisions also recorded in handoff.md.
All started Chrome instances/server stopped; ports 9990, 9991 and 8795 closed, host.html removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: work-rate-crew
#### Played
- Cold play as a grade 11 solo student before reading builder notes: Calls 1-5, Quote sheet and Office audit. Rich house scene; typed algebra is appropriately demanding.
#### Findings fixed
- Blocker, general, audit: revealing substitution let copied text earn a filing. Worked examples remain available but cannot earn independent credit for that sheet during the page visit.
- Blocker, general, Calls: an estimate exposed the exact finish clock. Later copying it now completes worked practice without an independent job stamp.
- Blocker, general, sprayer: 36 verdict/reason combinations could be tried without doing the domain check. Typed sprayer times are now required as evidence.
- Blocker, general, rate: 0.25+1/x slipped through the slash-count test. The outer expression must now be a single fraction.
- Should fix, general: editing quote answers or audit evidence left success true. Both invalidate immediately on input.
- Should fix, general, voice: late crew used the on-time result. Added an accurate late result and a next-pair how-to. Rewrite completion stops obsolete welcome speech.
- Should fix, general, craft: Motion-off late-start clock used elapsed hours; it now shows the same clock-time convention as Motion on.
- Should fix, general, teaching: changed nonexistent largest allowed time to strict upper bound; corrected teacher-note positive remainder wording.
- Should fix, general, layouts: compact root and audit controls/hints crowded the footer. Removed redundant feedback and compacted the affected forms.
- Polish, general: replaced the green-fringed ladder, preserved house/street; independent audit now leaves a filing seal on its worksheet.
#### Findings left
- Validation gap, should fix, general: complete mode/size, resize-stress and automatic voice coverage remain unverified because the final audit failed before its first result. The brief explicitly requires stopping after an unfinished audit.
- No new topics or kit edits. Equation checking remains solution-equivalence checking as specified; it cannot certify how a student derived an equivalent equation.
#### Break it
- 66/66 focused browser assertions passed: blank/wrong rates, unfinished symbolic sums, identities, wrong/extra equation roots, wrong times, incomplete root lists, 36 verdict/reason combinations, slider sweep, wrong rewrite/boundary, every empty-proof audit verdict combination, copied substitution, edited results and switching sheets after help.
- All deadline pairs recomputed and painted. Exactly 3 h qualified; the $320 late pair was refused as cheapest; Ana+Ben at $336 filed successfully.
- Device-local completion survived a fresh page; Clear board removed it. Keyboard Tab/Enter assigned both crews with visible retained focus.
#### Voice walk
- Held main path, 0.12-second presses and 2-second gaps, with a stage tap while paint finishes: assign, rate, solve, paint, done, wQuote, quote, wAudit. Each mode's how-to started once and matched the visible hint.
- Extra audit event expected 5, spoken 5. Main how-to keys expected 1 each, spoken 1 each. Late event expected 1, spoken 1; on-time event absent on that late trial.
- Side path: Quote -> Read -> Audit -> Sound off -> Read -> Calls -> Sound on. Read worked while sound was off; mode changes released it; queue empty afterward.
- Chrome was muted as required. Browser speech fallback is bundled; this checks speech scheduling, not the recorded bank voice's audible quality.
#### Facts checked
- Fictional rates/prices, verified with Fraction and the work-rate rule in [OpenStax 7.5](https://openstax.org/books/intermediate-algebra-2e/pages/7-5-solve-applications-with-rational-equations): AB 5/12 house/h, 12/5 h, $336; AC 1/3, 3 h, $360; BC 1/4, 4 h, $320, late; ABC 1/2, 2 h, $340. Five hours gives 25/12 houses.
- OpenStax Intermediate Algebra 2e 7.5: combine constant work rates, not times; late start gives 14/5 h after 8:00, 10:48; Dee takes 12 h alone.
- OpenStax 7.4 and 7.5: sprayer algebra roots 6 and 4/5, second implies -6/5 h for sprayer and fails the story rather than the equation.
- Common Core HSA-APR.D.6: 4x/(x+4)=4-16/(x+4); x>0 gives T<4 and T<2 iff x<4. At x=1/2,12,60: 4/9,3,15/4 h.
- [OpenStax 7.4](https://openstax.org/books/intermediate-algebra-2e/pages/7-4-solve-rational-equations): audit sheets 1-2 have no solution, sheet 3 only 1/2, sheet 4 has 3. Zero denominators excluded in originals; valid sides equal -1 and 3/2 respectively.
- [Common Core HSA-APR.D.6/D.7](https://www.thecorestandards.org/Math/Content/HSA/APR/) and [HSA-REI.A.2](https://www.thecorestandards.org/Math/Content/HSA/REI/) checked live: rational rewriting/addition and solving with original-domain checks are practiced.
#### Sensitivity
- None: fictional company and algebra practice, no cultural, historical, religious or body content. Spec explicitly uses named crews and gear rather than portraits.
#### Flattest moment left
- The audit's text-only filing was the flattest payoff; the result now lands as a seal on the actual worksheet.
- Comparing three deadline pairs still repeats calculation and painting. It is justified by distinct costs and the earned comparison ledger; no extra mode added.
#### Graphics
- All eight loaded art assets inspected at use sizes; original unused dusk image also inspected and preserved. One coherent painted set; no people or stereotypes.
- Ladder redrawn with built-in imagegen from the existing asset; magenta-key prompt and provenance in art/prompts.json, raw PNG and processed wrc-gear-ladder.webp saved inside the tool.
- House, street, paper, multiply paint bands, siding detail and restrained grade 11 presentation preserved. Bundle 701,107 bytes, about 685 KiB.
#### Audit
- Audit not finished. One invocation, 40-minute command ceiling, Chrome 9941, host 8745. CDP Tab.send timed out while enabling a domain on the first size, before audit.md or any size frame existed. There were no partial leads to fix. Not rerun, as the brief requires.
- Manual evidence: cold mode frames at 1366; affected root layouts at 680/800/1000 and 375 iframe; audit seals at 680/1366/375; grayscale, Motion off, keyboard, deadline ledger and voice paths. All inspected. Final 680 root hint ends y358.5 and audit hint y364, above footer y373.
- Latest full matrix at 1280/1920/760, complete mode/size coverage and resize stress are not claimed. Focused browser batches were clean except one wrapper favicon 404, corrected in the scratch host; the tool itself has a data favicon.
#### Left open
- No unattended questions asked. Retained the Office audit per BASELINE w2-05.
- Kept required worked-substitution help and estimate simulation, but labeled their later verification as worked practice without independent credit. Help history lasts for the page visit; this is a learning gate, not a tamper-resistant assessment.
- Accepted solution-equivalent equations, including x=12 for the new-hire equation, per the spec; no claim that the comparator proves a student's derivation. APR.D.7 is exercised through the spec's addition task, not a separate assessment of all four rational operations.
- No shared files changed or git commits made. Bundle/drive/audit limits were 120/300/2400 seconds. Two initial read-only commands lacked an explicit wrapper; subsequent commands were bounded. All started Chrome/server ports were closed, and host.html removed before finalization.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Work Rate Crew build handoff

Build only. No commits, shared kit edits, deployment or polish round.

#### Structure
src.html starts from the kit starter. Styles, semantic markup, bounded exact rational-expression parser and tool logic
are inline and readable. It uses kit:curio, kit:theme-912 and kit:graphing. The generated work-rate-crew.html is offline.
The five calls share stable crew buttons and one form. Mode changes do not rebuild controls under the pointer.
The public __tool API exposes state, setMode, call, assign, answer, audit, allLines and voice logs.
Scratch includes assembly sources, exact calculations, driven tests and screenshot evidence.

#### Tricky parts
Exact fractions use BigInt. Equations are parsed without eval, reduced as rational polynomials, compared symbolically,
and probed at five values. Identities, extra polynomial roots and domain holes at actual roots are rejected.
Five-hour estimates can be simulated without being accepted or saved. Verified completion requires checked rate,
equation when applicable, solution and both root reasons when applicable, followed by the paint run.
The house mask and multiply bands preserve siding texture. Alpha-column mass maps work fractions to band widths.
Cancellation tokens stop stale animation callbacks after a crew, call, Paint or mode action.
Deadline trials stay in memory across pair changes. Finished calls alone are saved on this device.
After all pairs are tested, the comparison ledger replaces the crew list while the cheapest quote is filed.
Audit verdicts also need substitution evidence: a zero denominator for an extraneous root or the exact common value
of the original sides for a valid root. Evidence follows root order, separated by semicolons. This closes verdict guessing.

#### Spec decisions and contradictions
- The open question about practice sheets is settled by BASELINE.md, w2-05: keep the extraneous-roots audit inside the
  story as the crew lead's checking sheets. All four are implemented and explicitly labeled practice sheets.
- The spec's comparison to hole-hunter says combined work is 'never faster than the fastest crew alone'. This is
  reversed. Positive combined rates are faster than either crew alone; the quote graph remains below Ana's four hours.
- Call 1 asks both to refuse 5 as an answer and to show its uncapped five-hour work. Check time refuses 5, while Paint
  tests it without saving completion and reports 25/12 houses. The wall stops full at the true finish.
- Call 3 and 5 rate sums contain x. Students combine the symbolic terms into one rational fraction before Equation.
- The spec says local FLUX; this build uses the image tool required by the user and CODEX-BUILD.md. No people were
  needed because this scene expressly keeps crew members as names and gear.
- The brief says start the report at first bundle but also stop when it is written. The report was scaffolded early,
  completed as evidence arrived, then finalized after the single audit.
- No questions were sent during this unattended session. The specified lively-host voice is metadata; the explicit
  instruction not to record means runtime uses kit browser speech fallback rather than recorded Sadachbia clips.

#### Sensitivity
Fictional mathematical workplace. No cultural, body, health, legal or historical claims; no people imagery.

#### Engine changes wanted
No runtime engine changes. All work stayed inside this tool and its scratch directory.
Audit helper: scripts/audit_tool.py, PAGE_JS, replace its unconditional #hint lookup with
`const h = [...document.querySelectorAll('.hint')].find(vis) || document.getElementById('hint');`.
The tool uses one hint per mode with Curio.voice's documented custom read function. The helper currently measures the
hidden Calls hint in Quote sheet and Office audit, producing false out-of-view leads. The shared script was not edited.

#### Art still to paint
None. Eight new assets generated; two props redrawn to remove green shadow artifacts. Existing dusk art preserved.

#### Validation handoff
Cold review, 2026-11-07: see codex-review.md for the independent review and final audit disposition.
The review separates revealed worked examples from independent credit: auditHelp and callHelp survive control resets
for the page visit. Clear board removes saved jobs, but does not erase already revealed answers during that visit.
An estimate reaching completion reveals the finish clock, so later verification is worked practice without a job stamp.
The sprayer fit check now also requires the calculated sprayer times, 4; -1.2, to prevent verdict/reason enumeration.
oneFraction checks the outer expression shape as well as exact value, rejecting 0.25+1/x as an unfinished sum.
Quote reasoning and audit filings invalidate immediately when their input changes. Successful independent audits put
a filing seal on the worksheet; worked examples receive a separate label. The original substitution remains available.
Voice lines include a late-deadline event and next-pair instruction. Rewrite success hushes its obsolete welcome.
Motion-off late-start runs keep the 8:00 clock convention. The ladder was redrawn on a magenta key with clean gaps.
The review's numeric checks and 66 focused browser assertions are under _scratch/work-rate-crew.
Final review audit did not finish: the first size's CDP domain-enable call timed out before audit.md could be saved.
No partial leads were produced. The audit's host/tool.html preserves the attempted bundle. Per the one-audit rule,
it was not rerun. Manual affected-state frames and voice logs passed; a complete mode/size and resize audit remains
unverified. The review browser and host ports were confirmed closed. Do not describe this as a clean final full audit.

The paragraphs below record the earlier builder validation, not the cold review's evidence.
Exact Fraction and Sympy calculations agree with every job, audit and quote-sheet result. Browser functional checks
passed 195/195. The strengthened audit-evidence gate separately passed 22/22, including a post-audit repeat.
The full size matrix ran once. The single mechanical audit finished with 53 leads and no runtime or resize exceptions.
Its saved bundle is the pre-repair snapshot. Targeted repairs then covered header targets, accessible names, stamps,
phone call-title bounds, short-screen deadline forms and root controls, and invalid-action narration cuts.
All 73 audit PNGs were inspected through indexed contact pages, with critical leads opened full size.
The final four-frame check confirms 680/800 deadline hints, 680 quote instructions and keyboard completion.
Do not describe the final bundle as having a clean full audit: only targeted checks followed the repairs.
Scratch/build-manifest.json records both bundle hashes. The cold review should run its own complete audit.
Chrome audio was muted by the required driver. Voice logs verify scheduling, not listening quality or a recorded voice.
The first crew action replaces the now-stale welcome with its own assignment instruction as the spec requires.
Rapidly unassigning that same crew cancels its stale assignment line. Unchanged empty Paint/Clear actions preserve welcome.
All started Chrome instances and the host server were closed. No host.html remains.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
