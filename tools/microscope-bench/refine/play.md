# Play lens: microscope-bench (Curiosity No. 06), round 1

Cold Play lens, judged against CODEX-CURIOSITY.md, VISION.md "Curiosities: the second shape", the spec, STANDARDS,
BASELINE and POLISH. Played as a grade 6 student alone at home and as a teacher projecting at 1366x768.

My frames: `S:/CurioClass-codex-scratch/microscope-bench/play/f1/` (39 shots: every slide at 4x to 100x, oil, iris,
lamp, stage extremes, bubbles, dry mount, tray, mount drawer, sketchbook, calibration; zooms z01, z01b, z04, z14, z16,
z27; contact sheets sheetA to sheetD) and `.../play/f2/` (13 shots: first-focus drags, first key Up, tap at 10x and
40x, Read, motion at 0 s and 6 s, calm, rotifer hunt, 1280x720, dry mount; sheetE). Shared audit frames cited by name.

Counts: blocker 4, should fix 8, polish 5, nit 2.

## Short test (honest answers)

- **Would a kid open it unassigned?** For two minutes, yes: the bench looks like a real instrument and the first focus
  can land on a green paramecium. Then the material runs out (B1) and a dragged knob often shows nothing at all (B4).
- **Would an adult play for fun?** No, not today. An adult sees journal-figure crops pasted onto blank glass: hard
  rectangle edges, the same paramecium tiled across the slide, panel letters on the blood smear (B1, B2).
- **Is the real thing the interface?** The instrument is (turret, knobs, reticle, micrometer, iris, oil all behave).
  The specimens are not yet: they read as stickers on glass, not as a slide.
- **Does it work with no finish line?** Yes. No score, goal, level, finish or kit header slipped in. Nothing counts.

Two questions fail, so this is a blocker under CODEX-CURIOSITY.md. The fix is more and better real material, never a
game. What already works and should be kept: Bahamas sand at 4x (f1/24), the crane-fly wing at 4x (f1/22), the hair on
the counting grid (f1/20, f1/21), the nine-plane Volvox focal stack (audit state-colony-focused-680x425), and the
micrometer under the reticle with its mirrored digits (f1/29, f1/30). Those are the tone the rest should reach.

## Blockers

**B1. The slides are small photo tiles on empty glass, with their source backgrounds showing.** family:curiosity
- Where: `material.json` slides and assets; `src.html:1083-1105` (photograph, drawMaterial).
- What: almost every slide is one to four small crops floating in blank glass, drawn with hard rectangular edges and
  their own source backgrounds: diatoms sit on yellow discs, rotifers on grey rectangles, the paramecium on a pale
  rectangle (z01, z04). The pond reuses four individuals in a near grid (f1/04: six identical diatom discs, five
  identical paramecia). Physical sizes from material.json: onion field 425 µm (a 30 px square at 4x, f1/06), blood
  107x45 µm for the whole slide (a speck at 10x, f1/11), root tip four single cells of 60 to 80 µm (f1/15), the centre
  of the root tip at 100x is empty glass (f1/17), leaf 250x516 µm (f1/25). The spec's premise ("each slide is far
  bigger than the eyepiece... finding things is the activity", base images up to 2400 px) is inverted: the slide is
  mostly nothing and each find is one rectangle. Source images are 48 to 600 px; the bundle is 1.3 MB against a spec
  budget of about 4 MB, so there is room.
- How seen: f1/01, z01, f1/04, z04, f1/06, f1/11, f1/15, f1/16, f1/17, f1/25, f2/50 (rotifer at 40x: a grey strip).
- Better: fields that cover the slide (several real fields per slide, larger sources), source backgrounds masked or
  matched to the glass tone with feathered edges (the manifest already has `edgeFeatherOriginalPixels` and masks),
  and no visible repeats inside one field of view.

**B2. The blood smear is visibly a journal figure: panel letters A to H and panel gutters, upside down.** family:curiosity
- Where: `art/blood.webp`, slide `blood`.
- What: at 40x and 100x the "slide" is eight framed panels with bold letters (D, C, B, A read mirrored) and white
  gutters between them. A student sees a printed page, not blood.
- How seen: f1/12, f1/14, zoom z14.
- Better: crop single panels without letters or bars and lay them as separate fields, or find a fuller PD or CC BY
  smear. The paramecium crop (z01b) has a small dark mark near the centre that may also be a figure annotation;
  worth a check while at it.

**B3. The onion stain comparison runs backwards: unstained is deep navy, iodine is grey.** family:curiosity
- Where: `art/onion-clear.webp` (mean RGB 61,73,99), `art/onion-iodine.webp` (mean 178,178,178) and
  `onion-detail.webp` (126 grey); `src.html:678` (amber Iodine dropper).
- What: things-to-do 3 is "no stain, then iodine, compare". The student puts amber iodine on and the cells lose their
  colour. Unstained onion epidermis in brightfield is nearly colourless; iodine stains it yellow-brown. The view does
  not "really match" the mount (Done when 2). The iodine source is 85x80 px, so at 40x it is soft mush (f1/10).
- How seen: f1/07 against f1/09, f1/08 against f1/10; pixel means computed from the asset files.
- Teaching lens will likely want this too.

**B4. The first focus is a knife edge with no warmer or colder.** family:curiosity
- Where: `src.html:1141-1142` (blur capped at 24 px), `1312` (one coarse step per 7 px of drag), `dialDefs` coarse step.
- What: at 40x the depth estimate is 1.3 µm, so blur reaches its 24 px cap about 5 µm from focus. Everything from 50
  to 350 µm off looks identical. Only exactly 5.00 mm is sharp, which a drag hits only if it is 7 to 13 px long. A 12 px
  drag overshot to -50 µm and stayed blurry (f2/42); a 40 px drag went to -250 µm (f2/40); dragging or pressing Up
  first changes nothing visible (f2/41, f2/43). At 375 wide the FOCUS readout is hidden (`src.html:434`), so a phone
  user has no cue at all. The spec's first reaction ("the blur snaps sharp") fails for the most natural input, a drag.
- How seen: f2/40 to f2/43 with readout values logged; arrow key and wheel do land in one step (f1/01).
- Better: a blur that keeps growing with distance (no visible cap inside the coarse range), and start the first-run
  view at 10x where depth is 8.8 µm and a drag has room; or a coarse drag ratio that cannot skip the focus step on
  the first turn.

## Should fix

**S1. Every slide sits on the same focal plane, so focus is solved once, forever.** family:curiosity
- Where: `src.html:1002`, `1141-1147`.
- What: after the first turn, no slide, cover slip, dry mount or objective change ever needs focus again (except the
  colony). Removing the cover slip only adds 1.2 px blur, though the Manual says it "changes the focus model". Hair at
  -20 µm blurs evenly (f1/39): there is no surface to focus along, so things-to-do 7 cannot happen.
- Better: per-slide focal offsets (thickness, cover glass), and for thick specimens a depth range so focus slides
  through them, as the colony already does.

**S2. Calibration is pre-filled with the nominal answer.** family:curiosity
- Where: `src.html:1488-1490`.
- What: Calibrate opens with 10 and 40.0 at 40x, already reading 2.5 µm, the nominal value. Store gives "calibrated"
  with nothing read (f1/30). The reticle is drawn exactly nominal, so even an honest reading only reproduces nominal.
  The cheap path wins and the honest path finds nothing new.
- Better: start both fields empty; consider a small, stated per-objective deviation from nominal so calibrating
  finds something.

**S3. The glass locator gives away every find.** family:curiosity
- Where: `src.html:1107-1131`, line 1122 draws every fixed specimen into the locator.
- What: the locator shows the photos themselves, so "hunt the pond for the rotifer" is solved by looking at the map
  (f1/03, f1/01 locator). A real stage has vernier scales, not a minimap.
- Better: keep the slide outline and the field circle, drop the specimen thumbnails (or show only areas already
  passed over).

**S4. High power shows mush that looks like bad focus.** family:curiosity
- Where: wing (9.7 µm per source pixel), cheek (3.9), onion-iodine (3.9).
- What: wing at 40x is a featureless pale blur (f1/23); cheek at 40x is soft pink blobs while FOCUS reads +0 µm
  (f1/19). A student turns the focus knob looking for sharpness that is not in the photo. The Manual says so, but the
  student does not read the Manual between actions.
- Better: detail tiles at the places worth zooming to (the spec planned two to four per slide), or larger sources.

**S5. The mount drawer is a modal form that hides the eyepiece.** family:curiosity
- Where: `src.html:673-684`, `showModal` at 1464.
- What: water, dry, stain, cover slip and bubbles are eight buttons on a sheet that covers the view (f1/36). The
  student cannot watch a choice change the view, which is the whole point of making a mount. It reads as a settings
  form rather than a bench (the spec asked for drag or Enter with droppers).
- Better: a non-modal tray beside the eyepiece (as Calibrate already is), so each drop shows at once.

**S6. On the root tip, every cell is dividing.** family:curiosity
- Where: slide `root`, four objects, one per stage, each named on tap.
- What: the spec's hunt ("hunt for a cell caught in each stage") and its found-fact ("most cells are between
  divisions, so the dividing ones are rare finds") both need many interphase cells. Here there are exactly four cells
  and each is a different stage, so tapping all four is the whole activity (f1/15, f1/16). Teaching lens may flag the
  fact side.
- Better: full root-tip fields with mostly interphase cells, as in the source panels.

**S7. At 375 wide the tray shelf hides Sketchbook, Place, Wash and the micrometer.** general
- Where: `aside.tray` sideways scroll at phone width.
- What: four of seven tray controls are off to the right with no visible scroll cue; the Sketchbook, the only record,
  is the last one (audit size-375x812 (iframe host).png; audit lead confirmed on that frame).
- Better: wrap the shelf to two rows, or a visible edge fade and arrow.

**S8. "Things people have found" are mechanics notes, not finds.** family:curiosity
- Where: `src.html:747-754`.
- What: five lines about reticles and calibration factors. The spec's entries (Hooke's cells, Leeuwenhoek's
  animalcules, rotifer's name, red cell size, salt cubes, the root tip) are gone. This is the section that rewards a
  month of use; right now it rewards nothing.
- Better: entries tied to what the bench can actually show, each with its source, read after the find.

## Polish

**P1. Field notes lead with disclaimers.** family:curiosity. Tapping the paramecium gives "Motion follows a computed
path, not recorded swimming"; reused copies add "Reused photographic specimen" (f2/45). The find moment lands on a
caveat. Keep the name and one thing to notice; leave the honesty notes in the Manual. The note also shows twice, in
the bar and in the arm status (f2/45).

**P2. Read and the mount label say "Pond water, water, none, covered."** general. Aloud this is hard to follow (f2/46
log). The spec's model is "Onion skin, iodine, one hundred times, field one point eight millimetres". Better: "Pond
water, wet mount, no stain, cover slip on. 400 times. Field 0.45 millimetres."

**P3. The paramecium paces a small fixed loop.** family:curiosity. `pose()` (`src.html:1073-1077`): plus or minus
0.23 mm in x and 0.13 mm in y around home, top speed about 53 µm/s (0.23 mm x 0.23 rad/s), against about 1 mm/s for a
real one. After a minute it is predictable, and "follow it around the slide" is not possible. Better: wandering paths
across the slide, with turns.

**P4. Projected, the readouts are too small.** general. Data rows and the arm status are 11 px monospace
(`src.html:175`, `210`); from the back of a room only MAG and FIELD read. A larger readout card at 1366 and up would
serve the teacher.

**P5. The first-run hint speaks over a drawer.** family:curiosity. Opening the tray, prepared box or mount drawer as the
first action speaks "Turn the focus knob." while the modal covers the knobs (audit held-click table, rows 0 to 2). A
small thing, but the line names a control the student cannot see right then.

## Nit

**N1.** The maker's plate wraps so line two starts with a middle dot: "· No. 06 · Microscope Bench" (`src.html:233`,
`656`; every frame). Drop the leading dot when it wraps.

**N2.** The status line under the arm repeats the turret change in prose ("4 times objective. 40 times total. Field
4.50 millimetres.") right beside the readout that already says it (f1/03). Fine for screen readers; it could be
visually hidden.

## Cultural, Native or hard-history

Nothing cultural or Native. The blood smear is from a malaria patient; notes.md already says so and keeps it neutral.
No sensitivity review requested from this lens.

## Audit pilot

- **Leads confirmed:** 375x812 tray shelf cuts four of seven controls (S7).
- **Leads that were wrong or expected:** the hint overlapping `#view` at every size is the intended first-run hint on
  the instrument; "keep region covered" under Manual, tray, prepared box and mount are modal dialogs doing what modals
  do (the mount one is still a real problem, S5, but for feel, not overlap); the sketchbook at 1366 leaves the
  eyepiece visible as the spec asks (f1/37), and at 375 it shows the eyepiece in its corner as specified; "hint out of
  view" in the calibration, colony and sand states is the hint correctly gone after focus.
- **Clean rows cited, not re-shot:** Motion off, resize mid-action, five clicks and two quick taps per control.
- **What it missed:** everything above that needs eyes on the material or a real drag: the tile look and figure
  lettering (B1, B2), the reversed stain (B3), the focus knife edge and hidden FOCUS readout at 375 (B4), one focal
  plane for all slides (S1), the pre-filled calibration (S2), the locator giveaway (S3), mush at high power (S4).
