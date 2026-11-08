# Misleading Charts handoff

## Structure
`src.html` starts from the kit starter. It contains the responsive desk, publication and correction styles, two sets of controls, six data sets, SVG rendering, and state transitions. The shared kit owns Motion, Sound, Read, chimes and voice queuing. No family engine applies because these charts must permit intentionally misleading geometry.

The panel precedes the stage in DOM order for keyboard navigation. Wide layouts show the original and correction beside each other. Short layouts use publication/correction tabs and move the privacy/reset footer under the stage. On a phone the desk and panel stack.

`chartConfig` describes the visible chart in model units. `compare` uses that model before pixel rounding. Screen pixels only annotate the ruler. `drawChart` lays out at actual pixel dimensions. The exact right axis on case 4 is 2/3 to 19/6. Case 6 compares first and last growth steps, rather than member totals, in its line view.

Only closed case ids are stored in `mc-closed`, inside try/catch. The kit's shared Motion setting is also stored. Notebook findings and Spin Room controls are not persisted. No network requests occur in the bundled tool.

## Decisions and contradictions
- Open question, fourteen paintings: accepted. Two desks, six blank publication props and six picture icons were made during this build, all with `people: false`.
- The brief requires the image tool; the older Art section names local FLUX. Followed the brief and used built-in OpenAI gpt-image, then the required `art.py --rekey` path. Added matching source credit.
- BUILD.md says not to draw or record; CODEX-BUILD.md and the user explicitly require painted art. Painted art was made; voice was authored, not recorded, as the build-only instruction says.
- The general Done when says every correction has lie factor 1.0, while its parenthetical allows "honest" for cases 2, 4 and 6. Used the specified contextual honest statements for those three. Rate correction uses rate for both picture and numerical comparisons, giving lie factor 1.0.
- Full year in case 2 contains ten school months. Labeled and explained this as the school year; did not invent summer values.
- The no-free-enumeration brief conflicts with a checker accepting any matching pair without evidence. Kept File it enabled when both choices are picked, but evaluate correctness only after diagnostic evidence. Each failed filing consumes its diagnostic proofs. Repeating an unrelated clue does not unlock another guess; the required diagnostic tools and ruler comparison must be used again. No score, attempt counter or new quiz was added.
- The six case numbers intrinsically match the listed trick-card order in the spec. Cards are unnumbered and displayed in a different order, removing that positional answer key.
- Baseline sliders use the full data set's minimum so moving a time window never leaves negative bar heights.
- A double-axis ruler only compares within the same quantity. Dividing wins by smoothies is not a meaningful relative change, so mixed-series picks ask for another point on the same line.
- Cases can contain secondary issues: case 2 also benefits from daily rates, and case 4 also has a nonzero baseline. The checker retains the spec's canonical technique for each case. The notes name this ambiguity; these are teaching cases, not a unique-classification test.
- Props fill the usable publication area, which can exceed the Art section's 55 percent of stage height. Readable charts and the explicit largest-item focus requirement take priority over that illustrative size suggestion. In the smallest robotics view the keyboard extends below the working paper area so its chart stays on a blank screen.
- Dense year labels stagger across rows. Compact gap annotations use "y" for years; the Notebook spells out the year gaps.
- Full-source robotics picture marks stay small to respect actual one-year spacing. Narrowing the time window lets the same painted robot appear larger without overlapping its neighbors.
- On a phone the controls precede the desk so the complete choice set and File it are initially visible. The chart is reached by scrolling. Disabled Spin Room controls have accessible descriptions and tooltip reasons; the longer reason text is visible in wide layouts.
- The standing rule against naming a disabled control takes priority over playing firstClue immediately after the first finding. It starts once both choices enable File it. The generic second-ruler line names bars, pictures and points so it fits all six cases.
- For the two line-based data sets, the first Draw as option is labeled "Lines". This describes the chart that the specification's honest spacing and separate-axis corrections preserve; its internal value remains `bars` for the common rendering path.
- Chart mark nodes retain their identity across redraws. Dense bar hit planes route pointer input to the closest center, and all marks have at least 44 px hit height. Enter and Space use the focused mark directly.
- The data sheet is a nonmodal dialog; the papers it covers are inert until it closes. On phones it is fixed within the viewport. Closing it restores the current ruling hint. Short-screen inspector notes sit above the chart so the live meter stays visible.

## Cold review decisions
- Reproduced a blocker in the existing filing design: held clicks through all choices, renewing the required ruler proof each time, close Case 3 without interpreting anything. The earlier report's proof gate does not prevent this. There is no score or saved best, but a Closed stamp is still a check result. Fully preventing enumeration requires a spec-level change to the fixed-answer interaction. Left open under CODEX-REVIEW.md's no-new-feature rule; not described as solved.
- Filed choices are now frozen and File it is genuinely disabled after acceptance, so a student cannot replace the accepted answers while retaining the printed correction.
- Fixed the two-axis meter's misleading honest result: it now names smoothies as its main comparison and reports the wins comparison separately, with the causation caution. Do not turn a one-series lie factor into an overall chart verdict.
- An evenly spaced robotics window is flagged only when its visible time intervals actually differ. Ruler rejects an unrelated endpoint pair instead of silently measuring the fixed first and last steps.
- Wrong-filing hints now name the required diagnostic tools, and the spoken retry line agrees. Stale ruler and wrong-answer speech retires when its step ends.
- The stamp and print effects now run together; one formerly canceled the other. Published text stays readable while its small dot blinks. Motion off removes both effects.
- Final audit fixes reserve a lower paper margin for the full-size stamp, move the compact baseline annotation above the plot, shorten wrong-ruling hints, and clear stray rulers after unrelated robotics picks. ResizeObserver now interrupts effects only for a real viewport resize, so revealing the correction does not cancel the print and stamp.
- On phones the data sheet makes its covered panel and case folders inert; header controls and Close remain reachable. Closing or resizing restores access. First-clue speech waits until the sheet closes.
- The audit completed once with 73 frames, clean repetition checks and clean resize stress. Its slider path had no outer return and stopped before the physical end: the configuration now returns its path and drags beyond the thumb center. Separate native-drag evidence supplements that audited snapshot. No second full audit.
- Redrew pic-laptop with rubber bumpers, beveled material, visible hinges and a clean magenta-keyed edge. First transparent edit was rejected because the shared keyer removed dark hinges. The second painting passed the required art.py --rekey route. No kit change.
- Corrected notes' standards claims: 2017 2-DA-08 is partial, 2-DA-09 should move to a modeling activity, and 6.SP.B.4 names display types absent here. Shared module metadata and spec are outside this review's write scope.
- The official 2026 CSTA PDF confirms DI-26 directly fits chart design; DC-23 has no sorting/grouping activity here and DI-25 is limited. Notes state those limits. Catalog scope should move unsupported full-coverage mappings rather than add thin activities to this tool.
- Unattended choices follow the brief: retain the canonical primary trick per case, browser narration and the complete illustrated set. No new topics, quizzes, accounts or recording workflow.

## Next step
Review findings, including the remaining enumeration blocker and curriculum mapping, before treating the tool as ready. No further review pass, recording workflow or publication is authorized by this run.

## Sensitivity
No people, religion, cultures, hard history, health, law or financial guidance. School names and publishers are invented. Case 5 challenges a stigmatizing school headline through equal-sized comparisons; the correction must never endorse the original claim.

## Engine changes wanted
None. No kit or shared files changed.

## Build evidence
All plans, input batches, generated-art paths, number checks, functional tests, frames and mechanical audit live under `_scratch/misleading-charts/`. `art/prompts.json` records every prompt and generated-art provenance. No commits or polish round were made. Read `codex-report.md` for the final validation record and remaining gaps.
