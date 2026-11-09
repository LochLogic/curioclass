# pH Mystery Liquids handoff

Build only, 2026-11-05. No commits, deployment or polish round.

## Structure
`src.html` follows the kit starter with curio.css, theme-912.css and Curio.voice. Its own CSS provides three responsive
layouts without scaling the entire scene. The instrument heights follow the bottle's 20 cm reference, while the
test beaker is deliberately enlarged as the teaching focus. Tests and shelf controls stay stable during updates.
Only case changes rebuild the case card and shelf. The notebook is an observation grid with its own scroll area.

The source contains LIQUIDS, the quadratic equilibrium calculation, the ion-threshold bulb model, the sample state,
the three case controllers and the graph renderer. `window.__tool` exposes the specified API plus pure model helpers,
allLines and vlog. Acid samples store integer milligrams, avoiding cumulative button-rounding errors.
Bench bottle hooks accept named liquid ids or A through G in LIQUIDS order. Soda hooks accept the three UI increments;
batch checks repeat those increments so their graph points match actual student actions.
The spill graph uses real viewport coordinates and redraws on resize. Bubbles never lock an input.
Glass and instrument art ignore pointer input. Bottle images sit behind the beaker, with readable code labels above
the glass. Hit-test-based keep-region checks can call these transparent, noninteractive art regions covered.
On phones the C1 labels fit the first viewport; C2 replaces the tray with the explanation after measurements.
Focus is captured before that layout change and deliberately transferred with preventScroll. A failed explanation
restores the tray and focuses Fresh sample. Secondary notes, the reference ladder and device controls may scroll.

Eighteen WebPs are referenced through art tokens. Seventeen new paintings were generated with the built-in image tool;
the existing prep-room painting is retained. Prompts and originals are preserved. Every asset has people:false.
The source is readable, not minified. The generated offline HTML is ignored by git. Metadata stays tool.draft.json.

## Case gates and adversarial choices
C1 checks identity and whether the actual observations distinguish that liquid from all other shelf candidates.
Correct labels without discriminating test evidence do not close the case. Wrong labels remain freely revisable as
the spec requests. New shelf clears labels, observations, evidence and C1 completion, and changes the seeded key.

C2 requires precise soda endpoints on fresh undiluted samples and meter readings of both fresh tenfold dilutions.
Overshooting the first usable endpoint does not earn the measurement. A wrong explanation clears the dilution
evidence, so pressing each answer in turn cannot close the case without a new experiment.

C3 requires the teacher report and a graph interval crossing the acid endpoint using the 0.001 g step.
A coarse sweep to excess soda cannot earn the reasoning gate. A wrong explanation requires Reset spill, another
teacher report and a new graph before another answer. These gates address the brief's explicit anti-cheat requirement.
Closed cases are progress acknowledgments, not grades, points or evidence of full standard mastery.

## Open questions settled
1. Keep the supplied HS-PS1-2 mapping as context, but explicitly document that the complete electron/periodic-trend
   standard is not taught. Do not claim full coverage. Changing the shared module is outside this build's write scope.
2. Keep the specified dark/dim/bright thresholds. Name them as a model on screen and explain the ion-mobility limit.
3. Keep 0.001 g as the finest step. The spill cannot land on pH 7 with those steps; its sharp jump is the point.
4. Use the image tool, as the user requires, in place of the older spec instruction to use local FLUX. No people
   are needed in this deserted room, so retain the spec's people-free scene rather than adding portraits.
5. Follow the precise spec chemistry rather than expanding to a full titration simulator. Teacher notes name the
   acetic acid/acetate and fixed-buffer limitations. "Harmless" is not presented as a real cleanup safety claim.
6. Use 84.007 g/mol for bicarbonate consistently. C3's unrounded need is 4.20035 g; the spec's 4.2004 g is rounded.
   This reproduces its pH 4.08 at 4.200 g. Displayed C2 reference amounts remain the requested rounded values.
7. The old Clemson food PDF URL redirects. The verified current table is
   https://www.clemson.edu/extension/food/_files/ph-of-common-foods-table.pdf . All five ranges match.
8. No audio was recorded, following CODEX-BUILD. The firm-captain/Alnilam bank is in lines.json; browser speech is
   used now. That fallback cannot guarantee the specific bank timbre.
9. The user says to stop when codex-report.md is written, while CODEX-BUILD asks for an early report. Keep interim
   evidence in Scratch and write the deliverable report only after checks, immediately before stopping.
10. Repeated dilution eventually makes the bare strong-acid formula predict an alkaline acid sample. Preserve all
    specified readings and include water autoionization at extreme strong-acid dilution. Weak quadratics are floored
    at neutral; those extremes are illustrative, not complete equilibrium calculations. This is documented in notes.

## Sensitivity
No people, bodies, cultural traditions, religion or hard history appear. Chemical handling safety is relevant.
Review the distinction between a teacher-gated virtual drill and instructions for responding to a real spill.

## Engine changes wanted
None. Shared kit, scripts and catalog files were not edited.

## Evidence and limits
Scratch is `S:/CurioClass-codex/_scratch/ph-mystery-liquids`. It contains independent number calculations, image
provenance, rendered frames, browser input walks, adversarial assertions and the single mechanical audit.
See codex-report.md for final results and every outstanding item. Chrome uses assigned ports and mute-audio.
The phone host uses 8795 and stops after its shots. All shell commands after the initial read setup use run.py limits.

Reference preparation accidentally regenerated the ignored bundle outputs for snowy-mail-route and beat-lab while
following CODEX-BUILD's reference instruction. This exceeded the user's narrower write boundary. No reference
sources were changed, and the generated outputs were left intact rather than making further out-of-scope changes.

## Cold review, 2026-11-07
Review commands use Chrome 9960, 9961, 9962, 9964 and 9966 and host 8765. Changes stay in this tool and its Scratch folder.
The beaker was repaired with built-in imagegen and processed with art.py --rekey. Its native alpha is preserved
by cutout:false plus native_alpha:true in prompts.json; it is still a transparent cutout asset.
The C2 comparison on the bench uses measured endpoints on a shared scale. It appears only after both measurements.
C2 retryNeeded requires Fresh sample on both bottles after a wrong explanation; stored diluted samples cannot
re-arm the explanation buttons. A vinegar-drops sample refuses later tests and soda until refreshed.
Acid-plus-soda conductivity retains sodium and counterions. Retained samples are explicitly named when reselected.
Wrong explanations now name the contradictory observation. Added next-action lines are in the voice manifest.
The spill's soda how-to stays valid after early additions so it can start at the normal two-second tap pace.
Full HS-PS1-2 mapping remains outside this tool's authorized write boundary. No new curriculum topic was added.

Additional cold-review repairs: the notebook no longer shrinks beneath its table; the desktop hint is sticky with
scroll padding. Litmus colors a masked paper overlay rather than the sample. Vinegar drops detect excess added
bicarbonate as well as the stock baking soda solution. Empty checks ask for missing labels. Voice phase changes
and successful/failed explanations hush obsolete instructions before starting the current line. The audit now
includes a full notebook, an active C2 explanation, the measured comparison and litmus-paper states.

## Unresolved cold-review blocker: C1 feedback
The independent reviewer swept every test without interpreting its values, then assigned labels using only the
right/wrong marks. This closes C1 in 14 checks. See Scratch/review-c1-sweep-results.json and its drive frame.
The spec explicitly requires individual correctness marks and free label revision. Removing those marks or adding
a reasoning gate would change the specified interaction; that change was not made in this scoped review.
Do not describe C1 completion as evidence of independent identification mastery.

The single final audit confirmed a partial inactive explanation set below the phone fold. On phones,
C2 now shows that set only when usable; the existing phase/focus transition is unchanged. Its portrait frames
also confirmed a stretched spill tray. The painted tray now keeps its native 500:202 aspect ratio.
Bench now follows the spec Content order, so its named bottles do not mirror the default C1 answer key.
Named bottle hooks are unchanged; the old A-G Bench aliases retain LIQUIDS order for compatibility.
The separate C1 feedback-elimination blocker remains, as documented above.

The single review audit finished with 56 leads. All 66 audit frames were inspected; confirmed repairs were re-shot
without a second full audit. Twelve targeted post-audit frames check the tray at all standard sizes, phone C2
ready/retry transitions and the Bench order. Final C2/C3 HTTP phone frames have no console errors. The source has
an inline empty favicon. Review Chrome/debug ports and host 8765 are closed; the temporary host was removed.
See codex-review.md for the cold review's findings, named sources, exploit outcomes and remaining blocker.
