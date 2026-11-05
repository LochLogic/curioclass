# Biome Atlas handoff

Built by another chat, then cold-reviewed on 2026-11-03. No commits.

## Cold review, 2026-11-03

One review pass, no commits. Read codex-review.md for the final evidence and audit limits.
The old builder report describes the pre-review build. Preserve the rich landscape card set.
Cold review redrew ba-k-tropical-canopy using the built-in imagegen tool and its full prompt in art/prompts.json.
All twenty cutouts were re-exported at 1400 px and quality 72 from their raw paintings to repair full-screen softness.
The generated canopy raw file is art/raw/ba-k-tropical-canopy.png; no paid art.py generation was used.
Comparison results no longer shrink to a clipped row; Key uses a compact station summary.
Map Real biomes waits for each station's Reveal. The dry-month question outlines the whole year instead of the answer months.
Wrong-answer misses use their own spoken event and explanation, including at Dodge City.
Answer buttons are reused between questions; station changes hush stale speech; check feedback stays inside Key.
Recovery shows a progress edge, the next approximate stage and a specific same-climate completion result.

The single review audit completed with 57 leads. Its unchanged report is in _scratch/biome-atlas/review-audit/audit.md.
Post-audit corrections separate all-station chart labels, fit opened feedback on phones, preserve pin nodes and avoid cutting speech on repeated mode/empty Reset taps.
Welcome eligibility is checked before queuing so a completed Key gets its current Reveal instruction.
Plants sit above a measured caption band; tick labels use pixel spacing. Active climate labels and accessible chart values follow the shifted dot.
Focused rechecks only followed these corrections. No second full audit or new review round was run.

Source evidence is in _scratch/biome-atlas/review-ecoregions.json and review-numbers.json.
The UNEP-WCMC WWF point query confirmed the broad category for most stations, but contradicts Niamey's named ecoregion.
Kredarica's polygon is Dinaric Mountains mixed forests, not an elevation-resolved alpine tundra observation.
The spec's assignments remain unchanged, as required when a repair would change the spec. Notes disclose the limitation.

## Source map

src.html starts from the kit starter and uses kit:curio plus kit:theme-912.
Its sections are responsive styles, stable controls, climate calculations, a branching key, real-pixel SVG charts, succession stage data, layer rendering and event handlers.
stations.json preserves the spec's monthly inputs. world.json is the bundled land outline.
The hidden art bank holds the ten existing landscape cards. K holds the twenty new painted cutouts.
Curio.voice owns speech, Read, how-to deduplication and event logs.
window.__tool exposes state, calculations and interactions for review.

## Tricky parts

All calculations retain precision until display rounding. Southern stations reorder months only for plotting.
Wrong answers take a real branch and are checked after completion.
Each station has one saved record, including its comparison correctness and Reveal status.
At zero climate offsets the recovery destination is the real biome. Nonzero offsets use the key.
The timeline uses the larger source/destination span, 200 slider divisions, and an eight-second run.
Layer updates use CSS transitions; Motion off removes transitions without changing timeline duration.

## Open questions resolved

- Keep Dodge City as the sole intentional miss, following the spec's leaning.
- Teach only HS-LS2-6. Do not add HS-ESS2-4.
- Keep rounded succession timings, visibly labeled approximate.

## Engine changes wanted

Shared audit tooling only: scripts/audit_tool.py, MODES_JS.
Extend its selector with main .seg[aria-label="Mode"] button, preserving the existing header selectors.
The spec places mode tabs in the panel; header-only discovery misses them and cannot launch mode-specific control walks.
Explicit audit states and held-input tests cover the panel modes in this build. No shared file was changed.

## Review next

Cold review against spec.md and codex-report.md. Do not begin polish or deploy from this build.


## Build verification and boundaries

The ten original, unprefixed biome cards are retained. Twenty ba-k cutouts were generated during this build.
Bare soil, burned ground and scarred soil were each redrawn once. Raw originals and rejected first takes remain in art/raw.
The cutout ground strips use opacity for the spec's half and fifth descriptions; plant multipliers control height.
Short landscape layouts keep the main controls visible. Climate space remains in Read; Key and Change can hide that secondary inset in the shortest previews.
In Change, __tool.keyResult reports the live climate key. state.keyResult preserves the student's original prediction.
All 13 base results and 11 what-if results matched independent Python calculations.
Measured playback was about eight seconds for all ten biome stories.
Detailed screenshots and test JSON are in S:/CurioClass-codex/_scratch/biome-atlas.

## Source verification still open

The monthly station values and real-biome assignments come from spec.md.
An independent WWF ecoregion polygon point lookup was not completed: that dataset is not bundled in this worktree.
Do that source check in cold review. Do not treat the supplied ecoregion assignments as independently reverified here.
No network data was downloaded during Build.

## Numeric and audit recipe notes

The 8-year grassland span divided into 200 steps gives 0.04-year increments.
The approximate 0.3-year milestone lies between manual positions 0.28 and 0.32; Play crosses it continuously.
The spec's 200-step rule was retained.
The audit-state drag field requires a function body with an explicit return.
The initial audit recipes omitted it, so its named min/max snapshots stayed at zero offsets.
Those recipes are corrected for the next run. Separate real-drag and extrema frames cover the slider behavior.

## Additional audit helper change wanted

scripts/audit_tool.py, Audit.steps: require a drag result to be an array with at least two points.
Report an invalid drag recipe instead of silently converting an undefined result to an empty array.
No shared tooling was changed in this build.

## Evidence files

build-evidence.json records final bundle bytes and hashes, independent result checks, timing and viewport geometry.
audit-leads.md answers all 82 reported audit leads individually.
The full mechanical audit and all screenshot recipes remain in the supplied Scratch folder.
Change-mode T and P readouts track the active offsets; Read and Key retain the published station normals.
No commits or polish round were started.
