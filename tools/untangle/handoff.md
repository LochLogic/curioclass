# Untangle build handoff

Build only. No commits, deployment, shelf edits, or polish round.

`src.html` is the canonical readable source. `untangle.html` is the generated, offline game.
The game uses the shared Recess stylesheet and a tool-local snapshot of the shared Recess script; it has no classroom header, voice, lesson cards or standards UI.
All 20 First Skies and the exact 550-record ladder are embedded, with a worker-generated daily sky.

## Rebuild

Run from `S:\CurioClass-codex`:

```powershell
$env:CURIO_DRAFT=1
python _scratch/untangle/review_run.py 120 python scripts/bundle_tool.py untangle
```

The standard shared bundler now works directly. `lib/recess.min.js` is a readable snapshot of `kit/recess.js`,
with only its header's inline script/link example comment replaced. The original header both closes the inline
script and triggers stylesheet substitution. No executable shell code was changed. The source uses `lib:recess`
so this workaround survives bundling and does not depend on a Scratch-only postprocessor. Do not overwrite it
with an unsanitized copy. No shared kit or bundler file was edited.

The older Scratch `bundle.py` adapter is build history; do not use it for the reviewed source.

`_scratch/untangle/assemble.py` was the build-time assembler. It refreshes script sections from the build-time
Scratch modules, so do not use it after editing the canonical source unless those modules are synchronized.

## Evidence

- `../../_scratch/untangle/checks.json`: 1,799 assertions, both required hashes, all 1,140 required layouts.
- `../../_scratch/untangle/solutions.csv`: every stated crossing count, computed count, pace and witness move count.
- `../../_scratch/untangle/independent-results.json`: separate Python geometry and constructive planarity checks.
- `../../_scratch/untangle/compact-checks.json`: all 570 skies solved in the 680x425 preview's 484x401 field.
- `../../_scratch/untangle/additional-geometry-final.json`: 5,130 shape/mirror checks at nine final field sizes.
- `../../_scratch/untangle/daily-checks.json`: 55 dates, deterministic generation, both required field sizes.
- `../../_scratch/untangle/play/results.json`: real pointer, keyboard, touch and offline play.
- `../../_scratch/untangle/play/extra-results.json`: score tiers, best preservation, clearance slide and restart races.
- `../../_scratch/untangle/art-checks.json`: all 23 backdrop darkness checks and painted glint registration.
- `../../_scratch/untangle/audit/audit.md`: the one complete mechanical audit, including its raw leads.
- `../../_scratch/untangle/final/`: targeted checks after compact-layout and pointer-focus fixes, plus comparison frames.

## Implementation choices

- The spec's packed X values count non-shared line intersections including exact touches and overlaps.
  This interpretation matches every record and both hashes; runtime trouble follows the separate 7 px/4 degree rules.
- A drop shorter than 4 px returns to its lift position. It cannot accumulate free movement or a zero-move best.
- The 680x425 preview uses a compact control rail to preserve actual pixel clearance. The specified laptop and
  390x844 phone arrangements retain their top shell controls and bottom strip.
- Transparent generated paintings are resized without chroma-keying or trimming their coordinate canvas.
  First Skies painted cut-outs fit their guide bounds; glints use the painted gold sprite registered at the exact guide coordinates.
- Asset filenames use lowercase `sky-l01` through `sky-l20`, matching the bundler's lowercase token grammar.
- The move pace is verified reachable. Neither the spec nor this build claims an exact global minimum.
- There is no opponent, losing state, or pass-and-play mode in this game's spec.
- Cold review: Undo now settles a pending slide and checks for a solve before removing history. This prevents a
  rapid Undo from minting a lower score while putting a crossing back into an already solved sky.
- Cold review: `revealLanded` and `settleReveal` preserve the painted reveal and daily beams on resize or a
  motion-mode change during the glide. The motion callback ignores unrelated shell repaints.
- Cold review: drops that reduce crossings get a brief geometric gold halo; Calm keeps the still appearance.
- Cold review: the effectively empty notes file has been restored with game-specific grown-up guidance.
- Cold review: saving initials focuses the shell's Next button; Next preserves keyboard focus on the new sky.
  Tool-local adapters also name the shell's modal cards and keep Tab inside them. No executable shell code changed.
- Cold review: the desktop Worlds overview reserves extra header/footer space when sizing tiles, so its Back
  button stays fully visible in the 1000x625 preview. Phone and short-landscape overrides keep their layouts.

## Engine changes wanted

- `kit/recess.js`, header: escape or remove literal `<script>`/`</script>` and `<link>` examples in the header comment.
  `bundle_tool.py` currently interprets those examples as tokens and produces invalid inline JavaScript.
- `kit/recess.css`, `.rc-arr`: use a 44 px minimum height for initials arrows. This game supplies a local style override.
- `kit/recess.css`, phone toolbar: allow the title and four-digit total to fit beside five controls at 375 px.
  This game supplies local font and spacing overrides.
- `kit/recess.js`, `card` and `initials`: label the dialog from its heading, contain Tab inside it, and move
  focus to Next after saving removes the initials form. This game supplies tool-local accessibility adapters.

## Left open

The requested three-child playtest, ages 8 to 13, was unavailable in this unattended session. The 30 to 90 second
human median and enjoyment/stall criteria are not claimed. All automated play and geometry evidence is separate.
The owner's decision on the visual bar remains the owner's decision; the painted look board and final frames are provided.
