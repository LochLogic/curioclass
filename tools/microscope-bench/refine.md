ROUND 2 (exit check 2026-11-06): Blocker 1 open (slides still specks and small patches on bare glass: c; four reused pond individuals: d; wing, cheek and iodine sources too coarse, no colour iodine, no cheek nucleus: e, f, h; root meristem a small patch at 100x: c, g); Should fix 5 open (pan p95 31 ms)
Counts: blockers 2 (general 0, family 2), should fix 11 (general 5, family 6), polish accepted 11

# Refine: microscope-bench

Merged from refine/teaching.md, refine/play.md and refine/craft.md (no sensitivity.md; all three lenses agree none is
needed). Judged against CODEX-CURIOSITY.md, BASELINE.md and spec.md. Integrator spot-checks: src.html 992 (opens at
40x, coarse 5.05), 1083-1090 (photograph draws each crop as a hard rectangle), 1141-1142 (blur capped at 24 px),
1312 (one coarse step per 7 px of drag), 1488-1489 (calibration fields filled with the nominal answer), 1122 (locator
draws every fixed specimen); material.json asset sizes (onion-iodine 85x80, leaf 64x132, leaf-detail 48x70, root
tiles 210 to 290 px); frames play/f1/z14.png (mirrored panel letters A to D and gutters on the blood smear) and
teaching/f1/pond-para-400.png (yellow vignette disc round the diatom, pale rectangle round the paramecium). All
confirmed. Lens frames live under `S:/CurioClass-codex-scratch/microscope-bench/` (teaching/, play/, craft/).

## Blocker

1. **Re-source and re-cut the specimens: the slides are journal-figure crops pasted on blank glass.** material.json
   slides and assets, art/*.webp, src.html:1083-1105 (photograph, drawMaterial). All three lenses found this from
   different sides; it is one fix. The instrument is right; the real material is not yet the interface, so the short
   test fails ("would an adult play for fun": no) and Done when 2 and 6 fail. What fixed looks like, part by part:
   a. **Figure furniture off every slide.** Blood is the whole EID figure: panel letters A to H (mirrored), white
      gutters, eight 5 µm bars (play/f1/z14.png, craft/r4/blood-100-oil.png, teaching/f1/blood-1000.png). Paramecium
      carries the source labels "Cy" and "Ma" (Kodama Fig. 1a), which also names a cell part before any tap (Done
      when 6). Wing keeps panel "2", rotifer keeps "B", a colony plane keeps a corner numeral. Crop inside each panel
      or mask from the source pixels; lay the blood out as eight separate fields spread across the glass.
   b. **No hard tile edges or source halos.** Diatoms sit in yellow vignette discs, the paramecium on a pale
      rectangle, the mat and rotifer on grey rectangles (teaching/f1/pond-diatom-400.png, play/f1/z01.png, z04.png,
      craft/pond10-crop.png). Mask or match each source background to the glass tone with feathered edges (the
      manifest already has `edgeFeatherOriginalPixels` and masks).
   c. **Slides that cover the glass, not specks on it.** Onion is one 425 µm patch (play/f1/06), the whole blood
      slide is 107x45 µm (play/f1/11), the root tip's centre at 100x is empty glass (play/f1/17). Spec "Real
      material": one base image up to 2400 px per slide plus two to four 512 px detail tiles at the places worth
      zooming to. Art is about 0.9 MB of the spec's 4 MB budget, so there is room; update the `Size:` line in
      notes.md if the bundle passes 2 MB.
   d. **No visible repeats.** The pond stamps the same paramecium and diatom in a near grid (play/f1/04, craft
      r4/sharp-4x.png). Use more individuals, and vary rotation and scale per copy (Craft 14 folded in here).
   e. **Sources fine enough for the objective that views them.** Wing 9.7 µm/px, sand 7.1, cheek, iodine onion and
      leaf 3.9, against about 0.9 µm per screen pixel at 400x: soft mush while FOCUS reads +0 µm
      (teaching/f1/wing-400.png, cheek-400.png, play/f1/19, 23, craft/r2/cheek-40.png). Things to do 4 (find a
      nucleus) and 9 (fine wing hairs) cannot be done. Re-source first; where a slide still upscales past about 2x,
      show an on-instrument caption in the style of the existing "REFLECTED-LIGHT SOURCE" one ("SOURCE RESOLUTION
      LIMIT"). Re-measure the wing scale on the full-resolution file (ZooKeys 1040 gives 14.3 to 16.8 mm; the tile is
      13.8 mm, measured on a thumbnail).
   f. **Iodine that looks like iodine.** Unstained onion is deep navy (Ogasawara Fig. 9a, RGB LED lighting, mean RGB
      61,73,99); the "iodine" field is a grey 85x80 px patch (mean 178,178,178), so the amber dropper turns cells
      grey (play/f1/07 vs 09, 08 vs 10, teaching/f1/onion-iodine-400.png, craft/onion-iodine-x4.png). Find a colour
      Lugol onion field (PD, CC0 or CC BY) and a near-colourless unstained one; correcting the LED cast is allowed if
      the slide's Manual page says so. Never tint the grey photo amber (that is painting data). If no colour source
      exists, caption the view on the instrument ("MONOCHROME CAMERA").
   g. **A root tip that is a meristem, not four cells.** Today four isolated dividing cells, one per phase, on empty
      glass (teaching/f1/root-40.png, root-100.png, play/f1/15, 16). There is nothing to hunt (Things to do 13), and
      the spec's fact "most cells are between divisions" is inverted. Use a real meristem field with many interphase
      cells; the spec names CIL:43552 (onion root tip, Cell Image Library, public domain, doi 10.7295/W9CIL43552).
      The build rejected it for missing pixel calibration (art/manifest.json exclusions); the spec allows scale from
      "a known-size object in frame", so set it from cell or nucleus widths cross-checked against the Çavuşoğlu Fig. 4
      10 µm bar, say so on the slide's Manual page, and keep the four Çavuşoğlu figures as close-ups placed inside the
      field. Rewrite the metaphase note to describe what root1 shows (a scattered squash spread, not a plate).
   h. **A cheek field that shows nuclei** (teaching/f1/cheek-400.png: pale pink smudges). Pocket MUSE Fig. 8a is too
      coarse; find a PD or CC BY cheek field (CDC PHIL Public Domain or Cell Image Library PD/CC BY first) that
      resolves a nucleus at 400x.
   (family:curiosity)

2. **The first focus turn often changes nothing.** src.html:992 (opens at 40x, +50 µm), 1141-1142 (blur capped at
   24 px), 1312 (7 px of drag per 50 µm coarse step). At 40x depth is 1.3 µm, so blur hits its cap about 5 µm from
   focus: everything from 50 to 350 µm off looks the same. A first turn up (wheel, key or drag) goes to +100 µm with
   no visible change and the hint is gone (craft/r1/first-up.png vs first-down.png); a 12 px drag overshoots to
   -50 µm, a 40 px drag to -250 µm (play/f2/40 to 43). At 375 wide the FOCUS readout is hidden (src.html:434), so a
   phone user has no cue. Done when 1 fails for half of first touches. Fixed: open at 10x (or 4x) per the Manual's
   own "scan at low power" (Teaching P1); make blur keep growing visibly across the whole coarse range (no cap reached
   inside it), and compute it in field units scaled to canvas size so a 430 px and a 1020 px canvas match (Craft 15);
   a first drag of any natural length in either direction must visibly change the view and the toward-focus
   direction must reach sharp. Show FOCUS at 375 wide. (family:curiosity)

## Should fix

1. **Calibration is passed without looking.** src.html:1182 (reticle at exactly nominal), 1488-1489 (count fields
   filled with 10 and the nominal answer), Manual near 721 (gives the 4x answer). One tap on Store turns "nominal"
   into "calibrated" with the same number (play/f1/30, teaching/f1/micro-40-ret.png). Fixed: empty count fields; give
   each objective a small, realistic true magnification that differs from nominal (for example 3.9x, 9.8x, 41x, 98x)
   and say so in the Manual's honesty notes; describe the method in the Manual without the worked count. Done when 4
   still holds (a red cell measures 7.5 µm; keep it within 20 percent after the change). (family:curiosity)
2. **The glass locator gives away every find.** src.html:1107-1131, line 1122 draws every fixed specimen into the
   locator, so "hunt the pond for the rotifer" is solved by the map (play/f1/03). Spec: "nothing is centred for you.
   Finding things is the activity." Keep the slide outline and the field circle; drop the specimen thumbnails.
   (family:curiosity)
3. **Every slide sits on one focal plane.** src.html:1002, 1141-1147. After the first turn no slide, mount or
   objective change ever needs focus again (except the colony); removing the cover slip only adds 1.2 px blur though
   the Manual says it changes the focus model; hair at -20 µm blurs evenly (play/f1/39), so Things to do 7 (focus
   along the hair) cannot happen. Fixed: per-slide focal offsets (prepared slide, wet mount, dry mount, cover slip on
   or off), and a depth range for thick specimens such as the hair so focus slides through them, as the colony does.
   (family:curiosity)
4. **The mount drawer is a modal form that hides the eyepiece.** src.html:673-684, showModal at 1464 (play/f1/36,
   audit state-mount-preparation-1366x768.png). The student cannot watch water, iodine, cover slip or bubbles change
   the view, which is the point of making a mount; spec Controls ask for drag or Enter with droppers on the bench.
   Make it a non-modal tray beside the eyepiece (as Calibrate already is) so each choice shows at once. (Play S5 and
   Craft 12 merged; family:curiosity)
5. **Panning misses 60 fps.** Headless software-raster proxy at 1366x768: 4x pond defocused median 33.3 ms, p95
   50.0 ms; sharp p95 33.4 ms (craft r1/r2 perf). Causes: `ctx.filter` blur and contrast applied per sprite
   (src.html:1146, 1098); the locator and the sketchbook preview are redrawn every frame even when the book is closed
   (1218-1220). Blur once on an offscreen layer and skip the hidden preview. Done when 8. (general)
6. **The welcome speaks over a modal.** A first tap on Specimen tray, Prepared slides, Prepare mount, Sketchbook or
   Manual opens a dialog and then speaks "Turn the focus knob." while the knob is behind the backdrop (audit "One held
   click" rows 0, 1, 2, 6, 20; state-specimen-tray-1366x768.png). Give the welcome a `valid` check that no modal is
   open. (Craft 7 and Play P5 merged; general)
7. **At 375x812 the tray shelf hides Place, Wash, the micrometer and the Sketchbook.** src.html:529; scrollWidth
   962 px in a 343 px box, no cue beyond a clipped "Prepare mo" (craft/r2/m375.png, audit size-375x812). On a phone
   there is no K key, so the only record is hidden. Wrap to two rows or add a visible edge fade and arrow. (general)
8. **Readouts lose their units on a phone.** FIELD's unit lives in a `small` hidden at 375 wide (src.html:433) and
   under 530 px tall (384), so it shows a bare "0.45" (craft/r2/m375.png). Put "mm" in the value. (FOCUS at 375 is
   in Blocker 2.) (family:curiosity)
9. **Lamp and Iris sliders are 26 px tall** (src.html:157; 23 px at 375 wide, 20 px in short windows). Raise the hit
   area to 44 px. (general)
10. **Field-guide notes are written for a microscopist and lead with caveats.** material.json `note` fields,
    src.html:1426-1436. Jargon ("Green endosymbiotic algae fill this photographed ciliate", "pennate diatom",
    "bdelloid rotifer", "Microcoleus-dominated freshwater mat", "erythrocytes", "Biogenic aragonite"), and the find
    lands on "Motion follows a computed path" or "Reused photographic patch" (play/f2/45). The note also shows twice
    (bar and arm status). Open with one plain sentence a grade 6 student reads ("A paramecium: one cell that swims.
    The green dots are algae living inside it."), then one real detail; provenance and honesty lines stay on the
    slide's Manual page. (Teaching S6 and Play P1 merged; general)
11. **"Things people have found" lost every spec entry.** src.html:747-754 holds five instrument notes. Restore the
    spec's entries that match slides that exist (Hooke 1665, Leeuwenhoek 1676, the rotifer's wheel, red cell 7 to
    8 µm, root-tip cells mostly between divisions, oil about 1.52, the flipped image, the iris trade-off), each with
    its source. Leave out salt (not in the tray). (Teaching S7 and Play S8 merged; family:curiosity)

## Polish accepted

1. **Read wording.** src.html:1040-1042: "Pond water, water, none, covered." becomes "Pond water, wet mount, no
   stain, cover slip on. 400 times. Field 0.45 millimetres." Same on the mount label. (general)
2. **No names before a tap on tray cards or in the Manual's motion note.** "fixed Volvox colony", "malaria parasites"
   on cards; paramecium and rotifer in the motion note (Manual 735-736). Keep the slide's own label as a real slide
   would carry it ("Pond colony, fixed, focal series", "Blood smear, Giemsa"); organisms are named in the field guide
   and on the source pages. Done when 6. (family:curiosity)
3. **Air bubbles as thick dark rings.** src.html:1100-1103 draws thin 1 px circles, one off the specimen
   (teaching/f1/bubbles-100.png). Spec: "thick black rings that are not cells": thick dark rim, bright centre that
   changes with focus. (general)
4. **notes.md teacher sections in plain words.** "What it teaches" never says "cells"; "Key skills" says "nine
   registered planes of a fixed pond colony". Say it plainly (see teaching.md P5), true of this tool. (general)
5. **The paramecium wanders.** `pose()` src.html:1073-1077 paces a plus or minus 0.23 x 0.13 mm loop at about
   53 µm/s. Give it wandering paths with turns across the slide so Things to do 1 ("follow it around the slide")
   works. Motion off still rests it in place. (family:curiosity)
6. **Larger readouts at the main size.** Rows are 10 to 11 px at 1366x768 (src.html:172-177, 175, 210, 328-329);
   12 px or more so they read across a desk and from a projector. (general)
7. **Plate wrap.** When the maker's plate wraps, line two starts "· No. 06" (src.html:233, 656). Drop the leading
   dot on wrap. (nit, family:curiosity)
8. **Sound label.** After toggling, the kit relabels "🔇 Sound" / "🔔 Sound" while Motion is reset to plain text
   (src.html:1070). Reset Sound's label too. (nit, general)
9. **"Modelled as".** Manual 711-712: the 0.65 aperture for 100x without oil is a modelling choice; say "modelled
   as". (nit, general)
10. **Crosshair on MAG.** The "⊕" on the readout card sits on "MAG" (src.html:168, craft/mag-corner.png). Move it
    clear. (nit, general)
11. **Status line repeats the readout.** The arm status repeats the turret change in prose beside the readout
    (play/f1/03). Keep it for screen readers, hide it visually. (nit, general)

## Settled calls

- **The specimen fix is real material only.** All three lenses converge on the photos; Blocker 1 is one coherent
  re-source and re-cut. Nothing is painted, tinted or redrawn as data (CODEX-CURIOSITY "Never paint data"). Where a
  source cannot be found, the honest fallback is an on-instrument caption or leaving the piece out, never a fake.
- **Severity of the iodine and root-tip items.** Play called iodine a blocker, Teaching and Craft a should-fix;
  Teaching called the root tip a should-fix. Both sit inside Blocker 1 because Done when 2 fails on them and they are
  the same fix (better sources).
- **The resolution caption is a fallback, not the fix.** Teaching proposed it first; Play and Craft wanted larger
  sources. Re-source first, caption only what still upscales past about 2x.
- **The first-run hint still goes after the first action** (CODEX-CURIOSITY). Fix the reaction to the first turn
  (Blocker 2), not the hint's lifetime.
- **Calibration deviation is small, real and stated**, not a puzzle: it is there so calibrating finds something, as
  on a real bench.
- **Locator:** keep the slide outline and field circle; it is the thumbnails that give finds away.
- **Modals:** the Manual, specimen tray and prepared-slide box may stay dialogs; only the mount must be non-modal.
- **Audit leads that were wrong** (Play and Craft agree): the hint overlapping #view is the designed hint on the
  instrument; "hint out of view" after focus is correct; covered regions under dialogs are expected.
- **Prepared slide labels** may name the slide the way a real slide label does; organism and disease names wait for
  a tap.
- **Bundle size:** going past the 2 MB goal for real, scannable sources is allowed by the spec (about 4 MB, 6 MB
  ceiling) with the `Size:` line updated.
- **Sensitivity:** none needed (all three lenses). The blood smear is a published malaria case, labelled neutrally;
  keep notes.md's line.
- **Do not change:** the turret, knobs, reticle, micrometer with mirrored digits, iris, oil model, the nine-plane
  Volvox focal stack, sand and wing at 4x, the hair on the counting grid, the keyboard model, the sketchbook save.

## To the spec's open questions

- **MS-LS1-2 claim.** Teaching S3: no ordinary interphase cell shows a clear nucleus today, and MS-LS1-3 is not
  exercised (the spec already says so). Should the map list MS-LS1-1 only, adding MS-LS1-2 once a cheek or onion
  field really shows a nucleus (Blocker 1h)? Codex does not change the map.
- **CIL:43552 scale.** May a root-tip field be scaled from a known-size object (cell or nucleus widths cross-checked
  against a second scaled source) when the archive gives no pixel size? Blocker 1g leans yes, under the spec's
  "a known-size object in frame".
- **Tray items left out by the curation fallback** (salt, sugar, feather, methylene-blue cheek): Things to do 4, 6
  and 8 cannot be done. Re-try sourcing in this pass, or trim the spec's Things to do?

## Not taken

- Craft 17, FOCUS reads "+0 µm" at best focus: the spec asks for a signed whole number.
- Craft 19, X washes with no undo and bare letter keys work outside fields: the spec names key X for wash; scoping
  keys is a design change for a later round.
- Teaching N1 as a separate item: folded into Blocker 1e (re-measure the wing on the full file).
- Craft 14 and 15 as separate polish: folded into Blocker 1d and Blocker 2.
- Teaching P1 as separate polish: folded into Blocker 2 (open at low power).

## Exit check (2026-11-06)

Scoped cold check of the fixed bundle (1,532,237 bytes). Fresh audit in
`S:/CurioClass-codex-scratch/microscope-bench/exit/audit-r2/`; my frames in `.../exit/shots/` (contact sheet
`contact.jpg`, 16 shots at 1366x768, zero console errors). Blockers 1 of 2 fixed, should-fix 10 of 11 fixed: 11 of 13 overall.

### Blockers

1. **Open (partly fixed).** Repaired: a (blood split into eight fields, no letters, gutters or bars; Cy/Ma, panel 2,
   B and corner numeral masked) and b for the pond bodies (no yellow disc or pale rectangle in pond-40.png). Still
   open, seen on my frames: c, blood-10.png shows eight dark specks on an empty 1.84 mm field and blood-100.png
   (oil, centred) is empty glass with one small patch in the corner (each field is 138x82 px at 0.18 um/px, about
   25x15 um); root-10.png shows the CIL meristem as a small square patch in the middle of empty glass, so there is
   still little to hunt (g partly: real meristem and honest BASE SCALE APPROXIMATE caption added, metaphase note
   rewritten). d, material.json pond reuses four photographed individuals 22 times (rotation and size now vary).
   e, wing-40.png is grey mush under a SOURCE RESOLUTION LIMIT caption; the caption is the settled fallback, but the
   re-source did not land and Things to do 9 still cannot be done. f, onion-iodine-40.png is a hard-edged grey
   square with MONOCHROME CAMERA (honest, not tinted, but iodine still does not look like iodine; colour source not
   found). h, cheek-40.png: pink smudges, no nucleus, captioned. Codex's polish.md agrees all of these are open.
2. **Fixed.** Opens at 10x, +50 um (default.png, blur 9.3 px, visibly soft). Blur curve at 10x from my js run:
   +-50 um 9.3, +-150 um 14.2, +-250 um 16.6, +-350 um 18.2 px, so it keeps growing with no cap inside the coarse
   range; field-scaled per polish.md. FOCUS with units visible at 375 (audit size-375x812 frame). Drag numbers taken
   from polish.md (+38/+10/+0 for 12/40/50 px down), not re-driven.

### Should fix

1. Fixed. Calibrate at 40x opens with both counts empty (cal-40 js: "" and ""); true powers 3.9/9.8/41/98 at
   src.html:935 and stated in the Manual (767).
2. Fixed. Locator shows outline and field circle only (pond-40.png, locator thumbnails gone).
3. Fixed. Per-slide offsets and mount offsets at src.html:938-941 (pond 0, onion +12, hair -15, wet/dry/cover terms).
   Hair depth gradient taken from polish.md frames, not re-shot.
4. Fixed. Mount drawer opens non-modal (`mount-drawer:false` for :modal); locator-mount.png shows the tray at the
   left with the eyepiece in full view.
5. **Open.** Codex's own proxy: p95 31.1 ms against 16.7 ms (median 15.9). Not re-measured; Codex states it open.
6. Fixed. Welcome has `valid: no dialog open` (src.html:994); audit rows 0, 1, 2, 6, 19, 20 show it dropped on a
   modal first tap, and heard on every non-modal first tap.
7. Fixed. Audit 375x812 frame: shelf wraps; polish.md 343/343 scroll width.
8. Fixed. FIELD and FOCUS carry units in the value at 375 (audit frame).
9. Fixed. Lamp and Iris 44 px (polish.md size json; audit found no small-target lead on them).
10. Fixed. Notes open plainly ("A paramecium: one cell that swims. ..."), caveats moved to slide descriptions and
    Manual pages (material.json).
11. Fixed. Eight entries restored with sources (polish.md; spot-checked Manual text for oil and iris entries via
    grep only).

### Polish (bulk spot-check)

Read wording heard in the audit row 23 ("Pond water, wet mount, no stain, cover slip on. 100 times. Field 1.84");
Sound label plain; tray labels neutral; plate wrap and readout size look right on default.png. Others taken from
polish.md. Polish never blocks.

### Regressions

None found. Default screen, each specimen once (pond, onion, cheek, wing, root, blood, leaf), mount tray and
calibration drawer all render with zero console errors or exceptions. The audit's resize-mid-action and held-click
passes are clean. The only audit leads are the designed hint over the eyepiece, hint gone after focus, and covered
regions under dialogs, all settled calls.

### Gate

1. Done when: **fails** on 2 and 6 for the material (Blocker 1), and 8 (60 fps, Should fix 5).
2. Codes: no map change; the MS-LS1-2 question to Cory stays open (no nucleus is resolved yet, Blocker 1h).
3. Solo defaults: pass (opens at 10x, first turn changes the view, calibration empty, locator gives nothing away).
4. Sensitivity: not required (all three lenses); pass.
5. No blocker or should-fix open: **fails** (Blocker 1, Should fix 5).
6. Bundle: pass, 1.53 MB under the 2 MB goal, no console errors, no network requests in my shots or the audit.
7. Voice counts: pass, one fixed line, spoken once, dropped under a modal, Read and Sound behave (audit tables).

Verdict: ROUND 2. Blocker 1 is a sourcing problem, not a code one; if round 2 cannot find broader real fields, the
honest move named in Settled calls (leave the piece out or trim the spec's Things to do) needs Cory's call.

## Audit pilot

- Leads confirmed: none were real defects this round.
- Leads wrong: 57 leads, all expected: hint/eyepiece overlap at every size (settled), "hint out of view" after
  focus (settled), keep regions covered under dialogs (settled), welcome "not heard" on modal first taps (that is
  Should fix 6 working as intended; the audit text still frames it as a missing premise, which does not apply to a
  Curiosity).
- What it missed: everything that kept this tool in round 2. It cannot see that slides are specks on empty glass,
  that sources are too coarse, or that panning misses 60 fps; those needed frames at each objective and a perf probe.
