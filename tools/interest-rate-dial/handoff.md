# Handoff: interest-rate-dial

Build and cold review. No commits or deployment.

## Source layout
`src.html` starts from the kit starter. Tool CSS re-lays the four cards and dial at actual pixel sizes. The JS contains the models, six round records, voice table, render functions and input handlers. No family engine exists for money. `window.__tool` exposes the state and model for reproducible review.

Scratch holds the original build assembly parts and scripts. The reviewed `src.html` is authoritative; running the old assemble.py would overwrite review fixes. Images use only art tokens. No runtime files or network are needed after bundling.

## Tricky parts
- Card interest, payment and balance round monthly with ties to even, matching the spec's Python table. `cents()` rounds the exact floating-point value using BigInt. Do not replace it with Math.round without repeating the number check.
- Keisha's signed annual rate is separate from base. Pin stores both Luis plans to keep comparisons fair.
- Predict uses separate round state; Street survives mode switches. The reveal is scored once. A new round drops queued, unstarted narration.
- Number tweens last 400 ms. A new change during one jumps to the target. The dial sweep is 1.2 seconds, with unchanged pacing when Motion is off.
- Cafe narration limits count actual starts in V.log, with validity checked at playback; muted or stale queued lines use no allowance. Shop again hushes a statement that no longer fits.
- Native modal close callbacks use restoreModal to protect the current hint and focus. The final reveal closes More before opening the recap; Escape can return to the recap button. Keep these ownership checks when changing dialog behavior.
- Contact sheets and source evidence are in `_scratch/interest-rate-dial/`.

## Open questions and contradictions resolved
- Followed the named art list: 16 assets (1 backdrop, 12 people poses, 2 shops, 1 car). The spec says 17 but names only 16.
- The user's explicit image-tool instruction and the newer Codex people permission take precedence over the older Gemini-only language. All 12 people assets have `people: true` and use reference images to retain each neighbor's identity.
- The open question leans toward a fresh stereotype review and an owner contact sheet. Both sheets are prepared. The fresh agent passed all 12 poses under BASELINE rule 11; evidence is in Scratch's record-review.md. Owner review remains for shipping, outside this build.
- No voice was recorded, following CODEX-BUILD's explicit no-record instruction. `wise-mentor` is selected in lines.json; browser fallback cannot reproduce its recorded timbre.
- The source section's 14.3-point margin is above prime, while this fictional tool adds 14 to its own base. Kept the specified formulas and explicit made-up-add-ons caption. Do not describe the tool base as the actual Fed target.
- The segment suggestions total 25-35 minutes, while the required metadata says 20-35. Kept the explicitly required metadata; segment times are flexible suggestions.
- The opening description says Luis's balance swells, but the specified minimum repays some principal every month. Followed the formula: rate increases raise total interest and payoff time, not the initial $1,500 balance.
- Build/check commands use explicit bounded timeouts. Initial read-only probes returned immediately before that wrapper was established. Reference tools were bundled into Scratch to respect the write boundary.

## Sensitivity
The four neighbors are fictional Japanese American, Black, Latino and South Asian adults in varied roles. Luis's debt comes from a car repair, not carelessness. Review the people together for stereotypes, respectful worry expressions, hands and full-body framing. No cultural practices or eligibility claims are taught.

## Engine changes wanted
None. All work is tool-local.

## Next phase
The cold review is recorded in codex-review.md. Do not infer authorization to publish or start another polish round from this handoff.

## Cold review changes, 2026-11-07
- Final worked answers stay visible until See your recap. recapHow names that control, then endLine is queued only with the open recap.
- The recap asks how signing changes Keisha's situation, without assuming the final case was signed.
- Wrong calls retain the student's choice beside the correct outcome. Reveal cards have a brass outline.
- The context card names the Fed target range's upper bound, monthly/no-new-charge/no-fee assumptions and Priya's later principal repayment.
- Closed cafe redrawn with the built-in image tool using the open cafe as reference. Same facade, blank sign and framing; brown paper and stacked furniture show the state. Open cafe also redrawn against green to preserve its burgundy awning while cleaning magenta edging. Both raw outputs and prompts remain in art/.
- Retained the spec's ties-to-even money convention. Independent decimal half-up results differ by cents, not months or decisions; do not treat these fictional totals as bank payoff quotes.
- Audit end-recap now presses See your recap explicitly; wrong-reveal covers feedback at every size.
- Do not run Scratch assemble.py over this reviewed source: it holds the earlier build parts.

- Further cold findings: guard late modal-close restoration by mode/round/phase, hush dialog Read on close, label revealed ladders Start to result, cancel the live sweep frame when Motion is turned off, and use the existing dense sidebar through 850 px height.
- Cold checks: all 15 detents match the specified monthly convention; 11 cheap six-round strategies failed to reach 24/24; cap is two cafeYes/two cafeNo starts; five separate signing events spoke; Home/End and jittered pointer drag reach the correct limits. No shared scripts were edited.

- Final voice edge fix: a cafe verdict reversal hushes only an already-playing opposite cafe event, then queues the matching event. It uses V.playing text, preserves the two-start limits and does not cut Read. The full voice main path and reversal are rechecked after the single audit.

## Cold audit coverage
The single final audit completed on Chrome 9941 / host 8745 within 40 minutes. Its 31 leads are classified in codex-review.md. All seven non-phone sizes, Motion off, focus, repeat inputs and resize stress completed. The audit's own phone host returned 404 and no iframe context, so the separate drive.py host route supplied eight phone states with real held clicks. All eight are 375 px wide with 44 px minimum targets and no console errors.

## Audit harness change wanted
In scripts/audit_tool.py, Audit.size, save a frame and the host response status when iframe context is missing before returning the lead. This run's failed phone route produced no diagnostic screenshot. Investigate the host's 404 separately; its cause is unconfirmed. No shared script was changed here.
