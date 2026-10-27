# Ramp and Roof

## One idea
Every slope a building code cares about is a ratio (a ramp may rise at most 1 inch for every 12 it runs, a roof is
"6 in 12"), and that ratio is the tangent of one fixed angle; build a ramp or a roof to any size and the angle and
its sine, cosine and tangent stay put while the lengths change, so trig becomes the tool that turns a code rule
into a cut list.

## Not like
- shadow-measure (gr 10, this group): similar triangles from measured lengths, no angles named. Here every triangle is set by an angle and solved with sine, cosine and tangent.
- fire-lookout-triangles (gr 12 map): laws of sines and cosines, no right angles. Here right triangles only, and the goal is to build something that passes inspection.
- packaging-challenge (gr 10, this group): designs judged by material used. Here designs are judged by code rules (slope, rise, landings, roof pitch).
- ski-slope-designer (gr 8, graphing): slope as rise over run on a graph. Here slope becomes an angle, and the angle's ratios.
- optimization-workshop (gr 12 builder): calculus finds the best design. Here there is no best, only designs that pass or fail a rule.

## Who and how
- Grade 10, Geometry, module Right Triangle Trigonometry. Students drive, own laptops or pairs. 15 to 40 minutes.
- Topic line: "right triangle trigonometry".
- Standards (module): G-SRT.C (trig ratios from similarity; sine and cosine of complementary angles; solve right
  triangles in applied problems).
- CCSS clusters: Ratio lab serves G-SRT.C.6; the roof's ridge-angle readouts serve G-SRT.C.7; Ramp and Roof jobs
  serve G-SRT.C.8.
- tool.json: driver "students", minutes "15-40", modes ["Ratio lab", "Ramp", "Roof"], grades_label "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Ramp and Roof", subtitle "Build it to code with one angle." Modes `Ratio lab`,
`Ramp` (opens first), `Roof`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left (a to-scale elevation drawing on dark drafting paper, re-laid out per size), panel right (job
card, controls, readouts, `Inspect`). Under 1000 px wide the panel goes under the stage with controls first. Under
900 px tall the job card collapses to one line with `Job details`.

Every mode shows the same triangle readout block: angle θ, opposite, adjacent, hypotenuse, sin θ, cos θ, tan θ,
and for the other acute angle (90° − θ) its sine and cosine beside them.

### Ramp (builder)
- Job picker `R1` to `R4` and `My porch`. The stage shows the porch (its height is the job's rise), the ground, the
  lot line, and the ramp with its landings drawn as flat 60 in pads.
- Controls: `Runs` (1, 2, 3), `Run length` (slider and number box, 24 to 480 in, step 6 in; or drag the ramp's foot
  on the stage), `Turn back` (only with 2 runs: the second run folds back beside the first; a small plan view inset
  appears), `Width` (30 to 60 in, step 6), `Handrails` (on or off).
- `Inspect` runs the checks (Content) and lists each as a pass or fail line with a check or cross glyph and words.
  All pass: "Passes inspection." with the cut list: each run's surface length (the hypotenuse) and angle.
- `My porch`: a rise box (1 to 60 in); no lot line.
### Roof (builder)
- Job picker `F1` to `F5`. The stage shows the building's end wall, the rafters, the ridge, and the overhang.
- Controls: `Shed` or `Gable`, `Pitch` x in 12 (0.5 to 18, step 0.5), or an `Angle` box in degrees (typing an angle
  shows the exact pitch, 12 tan θ, to two decimals; the stage snaps the build to the nearest half inch of pitch and
  says so), `Overhang` (0 to 24 in, step 2).
- Readouts: run (half the width for a gable, the full width for a shed), rise, rafter length with overhang, roof
  angle θ, angle at the ridge between rafter and the vertical (90° − θ), and the line "sin θ = cos(90° − θ) = 0.4472".
- `Inspect` checks the job's rules.
### Ratio lab (explore)
- One right triangle. Drag the top corner to change the angle (1° to 89°, snaps to 0.5°), drag the far corner to
  change the size. The three side lengths change; sin, cos, tan don't, unless the angle moves.
- `Stamp` leaves a faint copy of the current triangle, nested at the same corner, and adds a row to a small table
  (size, opposite ÷ hypotenuse, adjacent ÷ hypotenuse, opposite ÷ adjacent). Rows with the same angle show the same
  three ratios. `Clear stamps`.

## Content
Rules (the class follows one code for every job; source lines in Sources):
- Ramp: running slope no steeper than 1:12; rise of one run at most 30 in; clear width at least 36 in; a 60 in
  landing at the bottom of each run (the porch is the top landing); a turn between runs needs a 60 by 60 in landing;
  handrails on any run that rises more than 6 in.
- Roof: asphalt shingles need a pitch of 2 in 12 or steeper.
On screen: "Ramp rules: 2010 ADA Standards, section 405. Shingle rule: International Residential Code R905.2.2.
Rules as of 2026."
Ramp jobs (rise, lot length, the passing build, recomputed):
- R1 Library side door: rise 6 in, lot 15 ft (180 in). One run of at least 72 in; length used 72 + 60 = 132 in.
  Handrails not required (6 in is not more than 6 in).
- R2 Porch: rise 24 in, lot 30 ft (360 in). One run of at least 288 in (24 ft); 288 + 60 = 348 in fits. Handrails
  required. Surface length 289.00 in, θ = 4.76°.
- R3 Community center: rise 36 in, lot 50 ft (600 in). One run fails (36 > 30). Two runs of 18 in, each at least
  216 in: 216 + 60 + 216 + 60 = 552 in fits. Surface length 216.75 in each.
- R4 Corner shop: rise 30 in, lot 20 ft (240 in). One run needs 360 + 60 = 420 in: too long. Two straight runs need
  480 in: too long. Two runs with `Turn back`, 180 in each: 180 + 60 = 240 in fits exactly; the bottom landing sits
  beside the porch.
At 1:12 every run has θ = 4.76°, sin θ = 0.0830, cos θ = 0.9965, tan θ = 0.0833.
Roof jobs:
- F1 Garden shed: shed roof, span 8 ft (run 96 in), pitch 4:12. Rise 32 in, rafter 101.19 in, θ = 18.43°, ridge
  angle 71.57°, sin θ = cos 71.57° = 0.3162.
- F2 Garage: gable, width 24 ft (run 144 in), pitch 6:12, overhang 12 in. Rise 72 in, rafter without overhang
  161.00 in, with overhang 174.41 in, θ = 26.57°, sin θ = 0.4472.
- F3 Mountain cabin: gable, width 20 ft (run 120 in), pitch 12:12. Rise 120 in, rafter 169.71 in, θ = 45°, ridge
  angle 45°, sin θ = cos θ = 0.7071.
- F4 Porch roof under a window: shed, run 96 in, rise at most 20 in, shingles. 2:12 (rise 16 in, θ = 9.46°) and
  2.5:12 (rise 20 in, θ = 11.77°) pass; 1.5:12 fails the shingle rule; 3:12 (rise 24 in) covers the window.
- F5 Architect's sketch: gable, width 28 ft (run 168 in), "about 30°, within 1°, on a half-inch pitch". 30° is
  6.93 in 12; 7:12 gives θ = 30.26° and passes, rise 98 in, rafter 194.49 in; 6.5:12 (28.44°) and 7.5:12 (32.01°)
  fail.

## Interactions in detail
- Slope check is exact: rise per run = rise ÷ runs as a fraction, and a run passes when run ≥ 12 × rise per run
  (inches, rational arithmetic, no rounding). The "1 : x" readout shows x = run ÷ rise per run to two decimals.
- Angles: θ = atan(rise ÷ run) for ramps, atan(pitch ÷ 12) for roofs, shown to two decimals; ratios to four
  decimals; lengths to two decimals of an inch. The rafter with overhang is (run + overhang) ÷ cos θ.
- Ramp lot check: straight length = runs × run + runs × 60 (one landing below each run); with `Turn back` (2 runs)
  footprint = run + 60. Fails name the number: "Needs 420 in, the lot has 240 in."
- Extremes: a run shorter than 12 × rise per run is drawn red-dashed with "too steep" text and its angle shown; the
  slider stops at 480 in. Pitch 0.5:12 draws an almost flat roof and fails the shingle rule. Pitch 18:12 gives
  θ = 56.31°. Ratio lab angles stop at 1° and 89°, so tan never blows up.
- Typing an angle in Roof: pitch = 12 tan θ shown exactly (two decimals); the build uses the nearest 0.5 pitch.
- Keyboard: every slider and number box works with arrows (Shift for ×4); the ramp foot and triangle corners are
  focusable handles with aria-valuetext ("run 288 inches, angle 4.76 degrees").
- Reset: each job keeps its last build for the page session; `Reset job` restores the job's start. Nothing is saved.
- `window.__tool = {state, setMode, job(id), set(name, value), inspect(), readouts()}`.

## Look
Accent `--brand #ff4d6d` (shingle red), `--brand-ink #10161f`. Stage drafting paper `#101823` with grid `#1d2a3a`;
structure lines `#e8edf3`; dimension lines and labels `#a6b3c4`; the ramp surface and rafters in the accent;
failed parts dashed `#ffb8a8` with words. Pass and fail lines always have a glyph and text.
Contrast (computed): brand on --panel 5.39:1, on --sec-bg 5.10:1, on drafting paper 5.55:1; brand-ink on brand
5.65:1; structure lines on paper 15.16:1; dimension labels 8.38:1. Redder than fire-lookout-triangles' flame
#ff6150 (gr 12) and launch-pad's coral #ff7a5c (gr 9); no grade 10 or 11 math tool is red.

## Art
none: drawn in code (porch, ramp, building, rafters, triangles, preview.svg).

## Voice
Bank voice `gentle-storyteller` (Vindemiatrix), style "gentle and warm, like a grandmother reading out the job
cards from her carpentry crew". Not used by any grade 9 to 11 math tool (function-family-reunion, gr 12, uses it).
`Curio.voice`, `scope: () => state.mode`.
- wRamp (how): "Here is a job card. Set the run, or drag the foot of the ramp. When it looks right, tap Inspect."
- wRoof (how): "Pick a pitch, so many inches up for every twelve across. Then tap Inspect."
- wLab (how): "Drag the top corner to change the angle, and the far corner to change the size. Watch the three ratios."
- sameRatio (how, first Stamp of a second size at the same angle): "A different size, the same three ratios. They belong to the angle."
- turnHint (how, first time R4 fails on length): "Too long for this lot. Try two runs, and tap Turn back."
- pass (event, Inspect passes; stale when the job changes): "That passes inspection. The cut list is ready."
- fail (event, Inspect fails; stale on any change): "Not yet. Read the lines with a cross."

## Family engine
none.

## Sources
- G-SRT.C text: Common Core State Standards for Mathematics, High School Geometry, Similarity, Right Triangles, and Trigonometry, https://www.thecorestandards.org/Math/Content/HSG/SRT/
- Ramp rules (405.2 slope 1:12, 405.5 width 36 in, 405.6 rise 30 in, 405.7 landings 60 in and 60 by 60 in at a turn, 405.8 handrails above 6 in rise): U.S. Department of Justice, 2010 ADA Standards for Accessible Design, https://www.ada.gov/law-and-regs/design-standards/2010-stds/ (read 2026-10-27).
- Shingle pitch 2 in 12 or steeper: International Code Council, International Residential Code 2021, R905.2.2, https://codes.iccsafe.org/content/IRC2021P2/chapter-9-roof-assemblies (the same rule in the 2012 to 2024 editions; local amendments can differ, said in teacher notes).
- Trig ratios and complements: OpenStax, Algebra and Trigonometry 2e, 7.2 "Right Triangle Trigonometry", https://openstax.org/books/algebra-and-trigonometry-2e/pages/7-2-right-triangle-trigonometry
- Every job's numbers were recomputed in Python (2026-10-27).

## Done when
1. R2 with one run of 288 in passes; 282 in fails slope ("needs at least 288 in"); with Handrails off it fails the handrail line.
2. R1 with 72 in passes with Handrails off.
3. R3 fails with one run (rise 36 > 30) and passes with two runs of 216 in (552 in used).
4. R4 fails straight with one or two runs and passes with two runs of 180 in and Turn back.
5. F2 at 6:12 with a 12 in overhang shows rise 72, rafter 174.41 in, θ 26.57°, sin θ = cos 63.43° = 0.4472.
6. F4 passes at 2 and 2.5, fails at 1.5 (shingles) and at 3 (window); F5 passes only at 7:12 (30.26°); typing 30 shows 6.93 in 12.
7. Ratio lab: stamping 30° at two sizes shows 0.5000, 0.8660, 0.5774 in both rows.
8. Keyboard alone completes R2; every size in STANDARDS.md keeps the drawing, the controls and Inspect visible without page scrolling.
9. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- Homes are not required to follow the ADA ramp rules; this tool uses them as the class code for every ramp, and
  the teacher notes say so. Fine?
