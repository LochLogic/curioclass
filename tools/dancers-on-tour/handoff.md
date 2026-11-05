# Dancers on Tour: build handoff

## Structure
`src.html` starts from the kit starter. Styles and semantic controls come first, followed by original venue/piece data, model functions, the audience renderer, SVG plan, warm-up builder and event wiring. `window.__tool` exposes the model and voice log for checks. Temporary assembly fragments and scripts live in `_scratch/dancers-on-tour/`; `src.html` is the complete editable source.

Spread and swaps are per phrase. Front and Tempo apply to the venue. Formation coordinates are centered by the bounding box's depth before rotating by quarter turns. The safe margin measures centers. Sprinkler clearance is a separate park note. Settings and warm-ups persist per venue with guarded localStorage.

`formation`, `visibility`, `safety`, `metrics` and `notes` hold the rules. Visibility uses a segment projection and distance to the seat-target line; a blocker must be nearer. Seat eye heights follow the spec. The Safety light rates the whole piece, so changing phrase does not hide a jump risk elsewhere.

## Decisions and spec conflicts
- No explicit Open questions section exists in this spec. The owner overrides its original plan for code figures: keep the kit figure now, prepare painted replacements.
- The six venue and surface paintings were generated with the built-in image tool. No people were generated. Prompts, size and credit are in `art/prompts.json`; final WebPs were made only with `art.py --rekey`.
- Future dancers: 32 `people: true` cutouts, seven poses in four facings plus four eighth-turn arms-wide poses. `PAINTED_POSES` contains their `art:` tokens. `audienceRenderer.setup/resize/draw` is the replacement boundary. Replace kit actors there and preserve position, depth order, level and facing. The `snapshot()` hook exposes actual rendered actor coordinates and facings. Do not substitute a painted group for independent dancers. Future cutouts use magenta so green accents survive; none were generated in this build.
- Exact sample-seat positions were not supplied. Current model choices: gym/theater three rows at z -1.4, -2.7, -4 m and x -0.31w, 0, +0.31w. Park samples trace a front half circle, angles -68 to +68 degrees, x 7 sin(angle), z -1 - 4 cos(angle). These are model settings, not sourced venue facts. Plan chair icons are compressed below the front edge; explanatory text says so.
- The specified visibility rule is severe. Exhaustive discrete controls with these plausible samples found no whole-venue all-green solution, and no theater phrase solution with all nine seats for several formations. Raising the park Circle improves 0 to 1 visible sample seats at spread 1.0, rather than clearing every seat. Do not claim the theater's third note or the normal venueReady path passed. Model evidence is in Scratch `model.json`, `seat-search.json` and the report. The UI explicitly says all-green is not guaranteed. Fixing the content model needs an owner/spec decision, not an unreported relaxed threshold.
- The explicit safety formula contradicts Done when 4: gym jumps remain 2 points after all missing parts are supplied. A full gym warm-up therefore leaves medium risk. The gym's first note can pass with that warm-up while Safety stays amber. Followed the explicit points; documented on screen in the point breakdown and in notes.
- The safety formula does not include the warm-up's start order and minimum-duration checks at warm venues. The warm-up checklist still shows them. This distinction is intentional fidelity to the supplied rules.
- Fifteen minutes is a planning target. All six unique blocks total 18 minutes; overage is displayed, not silently removed.
- Above 15 minutes the timeline rescales its minute grid and shows a vertical 15-minute target marker. The total and overage remain explicit.
- Run uses four count-in beats, 32 piece counts and three one-count transitions, about 20.9 seconds at 100%. Tempo changes preserve the current count and apply immediately through the kit clock's pause/setBpm/seek/resume calls. Motion off keeps that duration and jumps to each formation.

## Voice
wise-mentor bank selection, Gacrux style, differs from Stage Blocker's firm-captain and Choreography Board's hero-coach. No audio was recorded in this build. Browser speech is the fallback. `Curio.voice` owns the queue; every fixed line is in `voice/lines.json`. Run hushes speech, has no welcome, and intercepts Read. Event validity uses the edit revision. Note acknowledgments use `V.heard` with a venue/note key so an unstarted queued acknowledgment is not marked heard.

## Verification and next work
See `codex-report.md` for completed checks and limitations. This is Build only, with no commits and no polish round. The next cold review should prioritize the content-model conflicts above, phone controls and small audience figures before aesthetic refinements.

The one full audit completed with 276 repetitive mechanical leads. Default sizes, reduced motion, resize safety and console/keyboard checks were clean. Scoped build repairs followed, with focused rechecks, not a second full audit:
- Scout rings clamp clear of captions; phone floor cards and Go to Adapt appear before the dossier after a tap.
- Section flex shrinking was removed so expanded rule text no longer paints over privacy text.
- Go to Adapt moves focus to Spread with preventScroll. Active venue/mode taps are idempotent, preserving a welcome during a double tap.
- Stop and live edits show the proper next action. Adapt instructions direct learners to the phrases with available swaps; stopped and running instructions differ.
- Quarter turns now agree between formation, arrow and audience actor. Right is Dance facing +90, left +270.
- Overlapping 46px transparent hit areas choose the nearest displayed dancer; visible circles and numbers shrink in dense plans, with at least 10.2px text. Keyboard inspection keeps each dancer's own id.
- Compact warm-up reorder controls come before its long checks, including all six selected blocks. The redundant Back to Adapt button was removed; the specified header Adapt button remains.
- Audit drag bodies now explicitly return their point arrays. The first audit's min/max fixtures stayed at default spread because the bodies returned undefined; separate real input tests and fixed-fixture tests verify 0.50 and 1.50. A max-duration warm-up fixture was added for the next audit.

The park sprinkler note samples formation positions, not swept transition paths. Compact/phone secondary explanations and warm-up checks may require scrolling. Do not describe the 276-lead audit as a clean post-repair audit.

## Engine changes wanted
None. The tool restyles the square floor's platform locally for the three surfaces; kit files were not changed.
