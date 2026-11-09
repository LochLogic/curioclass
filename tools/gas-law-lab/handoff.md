# Gas Law Lab build handoff

## Structure

`src.html` starts from the kit starter and uses `kit:curio` and `kit:theme-912`. Constants and the SI model come first,
then measurement/progress logic, the tool-local particle picture, responsive SVG apparatus/graph renderers and input
wiring. `__tool` exposes the specified API plus pure model/regression helpers and voice logs. Art tokens resolve to
all 11 generated WebP assets. Prompts and raw art are in `art/`; generated images are credited in tool.draft.json.

## Tricky parts

- Physical units are SI internally, with volume displayed in mL or L and pressure in kPa. Use the exact weight increment.
- Guided sets require four distinct bath settings and use true temperatures to reject repeated-temperature and insufficient-span shortcuts; noisy readings are
  fitted without rounding. A set must keep one fixed recipe, and B changes exactly one factor. Stop rows do not qualify.
- Deleting current-set data invalidates its comparison; unrelated bench rows leave guided fits intact, and deleting B retains valid A.
  Clear resets the comparison. Every Record still saves a row, including a non-qualifying bench row.
- A gas-only change leaves the slope unchanged. The result card reports that case accurately.
- Can input is limited at the current gas temperature, then its bath is limited to the last safe whole degree.
- Graph axes must stay at T (°C) and V (mL) for guided completion. Bench supports all specified axis combinations.
- The short layout moves Real lab and Start again into the tab rail. Long notebook tables may scroll; primary controls stay put.
- The browser voice is the kit fallback. `voice/lines.json` specifies bank bright-teacher and voice Autonoe; no audio was recorded in Build.

## Spec decisions and contradictions

- Open question: retain HS-PS3-2. Do not add an unrequested state standard; the gas laws lead into the particle/weight energy representation.
- The spec requests a new `docs/families/particles.md`, but the authorized write roots exclude docs. It was not written.
- `kit/particles.js` and its family doc are absent. The particle picture is implemented locally, not in kit. See Engine changes wanted.
- The spec says every second line has a different slope even if only the gas changes. Ideal gas theory says otherwise;
  recommend changing amount or weights and show a same-slope gas comparison honestly.
- The spec names local FLUX; the user's image-tool requirement wins. OpenAI gpt-image made all assets, with no people.
- Transparent glass had key-color artifacts on its first pass. It was regenerated with alpha, preserved through art.py --rekey.
- The build brief asks for an early codex-report.md while the user explicitly says to stop when it is written. The report
  was assembled in Scratch and copied to the tool only after the checks, so the user's stop boundary is respected.
- The spec's “R exact” is a rounded decimal representation of the exact N_A k product. The specified decimal is used consistently.

## Sensitivity

No cultural, historical, bodily or people content. Model equipment is not a real apparatus safety certification.

## Engine changes wanted

- `kit/particles.js`, new `Box` API: implement the family API listed in spec.md, including walls, heat-bath collisions,
  species, counts, still frames and picture-only hit counting. It does not exist in this checkout, so a faithful reuse
  is impossible. Promote only after the family has the required finished uses, per BASELINE rule 13.
  Required methods: `addSpecies`, `add`, `remove`, `setT`, `setWall`, `hits`, `meanKE`, `speedHist`, `count`, `frame`,
  `still`, `dissolve`; options include shape, dimensions, seed, bathCoupling, attract and zones. Sibling-only attraction
  and dissolving behavior was not added to this gas-law tool.
- `docs/families/particles.md`: document the actual promoted API and sibling contracts. This build has no authority to write docs.

## Next work

Read codex-report.md for the original build and codex-review.md for the cold review. No git operation was performed.
Voice recording is still deferred; the review tested browser speech fallback timing, not the final Autonoe recordings.

## Cold review repairs

- Clamp amount to the destination apparatus limit when switching from Can to Piston (0.0200 to 0.0100 mol).
- Graph crossings now use the selected x-axis unit, including kelvin. Celsius is no longer printed on every crossing.
- Experiment controls precede notebook row deletes in DOM order; explicit grid positions preserve the visual layout.
- Deleting an unrelated bench row preserves guided fits; deleting a B row preserves the valid A fit.
- The guided welcome specifies a total 60-degree span. Both the screen hint and Read remain available.
- Reversing compression or leaving the piston stop hushes the corresponding active line when its claim stops fitting.
- A queued zero-crossing event also checks the actual fit, selected axes and visible notebook, so Read cannot delay it into a different graph.
- Motion off synchronizes the rendered piston volume, preventing a stale position when Motion resumes after a temperature change.
- Balloon width reserves room for the largest allowed volume before applying cube-root scaling. This preserves area proportional
  to volume to the two-thirds power at narrow portrait widths, rather than flattening growth against a pixel cap.
- At laptop widths the result card leaves the lines' common crossing visible. It labels the real-gas extrapolation limit.
- gl-can was redrawn with the built-in OpenAI image tool and processed by art.py --rekey with its alpha preserved.
  Raw replacement: art/raw/gl-can.png. The full replacement prompt is in art/prompts.json; the old asset is in Scratch.
- Final audit: `_scratch/gas-law-lab/review-audit/audit.md`, one complete run, 19 leads. The early Fit instruction and
  compact can-caption overlap are fixed; focused checks are in `review-audit-fixes/`. Other leads are permitted first-tap
  welcome skips, recorded-data row scrolling, and the runner's iframe-context lookup gap. Hosted phone checks remain independent.

## Validation and test environment

The original build audit is in `_scratch/gas-law-lab/audit/audit.md`; its 94 original leads are mapped to fixes or deliberate
tradeoffs in codex-report.md. Focused post-fix checks and `FINAL_VALIDATION.json` are in Scratch. The compact Notebook
table intentionally scrolls to data rows; Clear is always in its toolbar and Delete stays at the table edge.

The LibreOffice Python launcher left host child processes after the parent exited. Final cleanup matched only the
exact `scripts/drive.py gas-law-lab --host 8785` command, checked it again before stopping it, and verified that ports
9980, 9981 and 8785 were closed. No unrelated Python or Chrome process was targeted. `host.html` is removed.

The cold review's final validation is `_scratch/gas-law-lab/REVIEW_FINAL_VALIDATION.json`; final file hashes are in
`review-static.json`. Exact-command and workspace checks closed the three review host children on 8765; connection
refusal confirmed closure of 9960, 9961 and 8765. The final balloon frame check confirms the expected 1.233259 width
ratio from sea level to 5,000 m at 760 wide, as well as at 680 and 1366.
