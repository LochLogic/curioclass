# Codex report: work-rate-crew

## Built
Build only, in S:\CurioClass-codex. Writes confined to tools/work-rate-crew and _scratch/work-rate-crew.
No commits, shared file changes, deployment or polish round. Draft stage is built.
Three modes: five dispatch calls, the rational rewrite quote sheet, and four practice-sheet audits.
Crew taps place painted gear on the street immediately. Textured paint bands meet across the actual house cutout.
Later calls introduce price/deadline comparisons, an unknown crew, a delayed start and two possible roots.
Verified jobs earn device-local board stamps. Deadline trials produce a comparison ledger before the final quote.
Source is readable: 1,450 lines, longest line 150 characters. Offline bundle: 696,056 bytes, about 696 KB or 680 KiB.
Build manifest and exact file hashes: _scratch/work-rate-crew/build-manifest.json.

## Numbers check
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

## Facts checked
- Combined constant work rates and reciprocal-time modeling: supplied OpenStax Intermediate Algebra 2e, 7.5.
- Original-domain restrictions and substitution for extraneous roots: supplied OpenStax 7.4.
- Rational rewriting and addition: supplied CCSS HSA A-APR.D.6 and D.7; equation checking: A-REI.A.2.
- Every displayed job number, cost and worksheet answer: independent exact computations above.
- Names, company, jobs, rates and prices are fictional and labeled made-up company. Constant rates are stated.
- Quote graph and paint readouts derive from the same exact rates as the checks. Names accompany crew colors.
- Device-only progress statement matches localStorage; no analytics or network code added.
No current market-price, professional painting, safety or cultural claims are taught.

## Break it
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

## Voice walk
Curio.voice, 18 fixed lines, lively-host metadata. Runtime inventory matches voice/lines.json exactly.
No audio recorded, as instructed. Required Chrome driver muted audio: logs verify scheduling, not audible voice quality.
Held-click main walk at about 2 s pace: assign -> rate -> solve -> paint -> done, all started as spoken.
Intervening state changes cancel obsolete instructions. Welcome is stale on first crew assignment by spec.
Side walk: wQuote -> wAudit -> audit. Queued quote-reason line dropped on leaving Quote sheet, correctly stale.
Read speaks the current mode's visible hint through the custom read function. Hints change synchronously with state.
Audit found invalid Paint/repeated empty Clear cutting welcome. Fixed; both quick-tap rechecks preserve wCalls.
Rapidly assigning then unassigning a crew cancels its obsolete assignment instruction, intentionally.
Full logs and keyboard/storage results: walk-results.json. Rechecks: post-quick-paint.json and post-quick-clear.json.

## Feel check
Played the five-call calculation path and all audits; held main and side walks exercised actual controls.
Best moment: gold and blue fronts meet on textured siding at 2.40 h, matching the prediction and earning the job.
Flattest moment 1: assigning crews initially felt like editing numbers. Added on-site gear, named pills, status and tones.
Flattest moment 2: deadline repeated forms crowded the board. Trials now build an earned ledger for the final choice;
short layouts put time, cost and deadline side by side, preserving the house and the next instruction.
Compared bar-comparison.png against Beat Lab; also opened Snowy Mail Route before building. The rich place and
simulation payoff retain a restrained Grade 11 workplace tone. No confetti or unrelated game mechanics.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
Full mode/size matrix shot once: 24 frames, including actual 375x812 iframe through host 8795. All inspected.
Affected layouts reshot locally. Earlier failed frames preserved; they do not represent final layout.
Inspected main/side walk frames and 8 special frames: grayscale, Motion off, interruption and quote extremes.
Inspected all 73 audit PNGs through 19 indexed contact pages; critical leads also opened full size.
Inspected all 12 post-audit frames and final four: deadline 680/800, keyboard completion and quote 680.
Evidence remains under _scratch/work-rate-crew; audit-contact-index.json maps audit contact pages.
Art contact sheet and Beat Lab comparison opened at final verification. Browser batches reported zero shot errors.

## Art made
Eight new OpenAI gpt-image illustrations: street, cutout house, roller, brushes, ladder, can, sprayer and legal-pad paper.
Warm painted style, detailed clapboards, worn tools, afternoon light. No people; each asset has people:false.
New WebP art 319,430 bytes (319 KB); all nine preserved WebPs 352,702 bytes (353 KB). Voice assets 0 KB.
Bundle 696 KB against 2,000 KB goal. Existing unused dusk art preserved; not loaded by the tool.
Can and sprayer redrawn once each to remove green shadow artifacts. Final cutouts/contact sheet inspected.
Full prompts/provenance in art/prompts.json. Art processed only with scripts/art.py --rekey per asset.

## Art still to paint
None. All eight specified assets present; no placeholders or people silhouettes.

## Engine changes wanted
No runtime engine changes. Kit Curio.voice and graphing Plane/fn/label/trace used without shared edits.
Audit helper PAGE_JS should select the visible .hint instead of unconditional hidden Calls #hint.
Exact proposed lookup is in handoff.md. Shared script left untouched.

## Left open
Cold reviewer should run a full audit on the final bundle; this build ran the mechanical audit only once.
Audio listening quality/bank-voice identity unassessed; browser fallback used because recording forbidden.
No unattended question sent. BASELINE w2-05 settles the open audit question in favor of labeled practice sheets.
Spec's 'never faster than fastest crew alone' comparison is reversed; implemented correct T<4 behavior.
Five-hour contradiction resolved as refused solution but allowed uncredited simulation.
Symbolic single-fraction rates used for unknown-time calls. Decisions also recorded in handoff.md.
All started Chrome instances/server stopped; ports 9990, 9991 and 8795 closed, host.html removed.
