# Work Rate Crew build handoff

Build only. No commits, shared kit edits, deployment or polish round.

## Structure
src.html starts from the kit starter. Styles, semantic markup, bounded exact rational-expression parser and tool logic
are inline and readable. It uses kit:curio, kit:theme-912 and kit:graphing. The generated work-rate-crew.html is offline.
The five calls share stable crew buttons and one form. Mode changes do not rebuild controls under the pointer.
The public __tool API exposes state, setMode, call, assign, answer, audit, allLines and voice logs.
Scratch includes assembly sources, exact calculations, driven tests and screenshot evidence.

## Tricky parts
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

## Spec decisions and contradictions
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

## Sensitivity
Fictional mathematical workplace. No cultural, body, health, legal or historical claims; no people imagery.

## Engine changes wanted
No runtime engine changes. All work stayed inside this tool and its scratch directory.
Audit helper: scripts/audit_tool.py, PAGE_JS, replace its unconditional #hint lookup with
`const h = [...document.querySelectorAll('.hint')].find(vis) || document.getElementById('hint');`.
The tool uses one hint per mode with Curio.voice's documented custom read function. The helper currently measures the
hidden Calls hint in Quote sheet and Office audit, producing false out-of-view leads. The shared script was not edited.

## Art still to paint
None. Eight new assets generated; two props redrawn to remove green shadow artifacts. Existing dusk art preserved.

## Validation handoff
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
