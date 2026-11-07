# Refine: Craft lens, microscope-bench (Curiosity No. 06), round 1

Cold lens. Read: REFINE.md, STANDARDS.md, BASELINE.md, CODEX-CURIOSITY.md, VISION.md (Curiosities), spec.md,
src.html, notes.md, material.json, art/manifest.json, art/prompts.json, voice/lines.json, audit-states.json and the
shared audit `S:/CurioClass-codex-scratch/microscope-bench/audit-r1/audit.md` with its frames. Own frames and logs in
`S:/CurioClass-codex-scratch/microscope-bench/craft/` (r1, r2, r4 subfolders), drive.py on port 9431, iframe host on
8873 (both stopped).

Counts: blockers 0, should fix 10, polish 5, nits 4.

## Contract (clean)

- One file, `microscope-bench.html` 1,361,131 bytes (1.3 MB), under the 2 MB goal. notes.md has the `Size:` line.
- No network requests: `performance.getEntriesByType('resource')` is empty after load and use (r1 perf shot). The
  Manual's source links are plain links the student may follow, never fetched.
- No console errors or exceptions in 17 driven shots (r1, r2, r4).
- Every `art:` token is a photograph listed in art/manifest.json with source, licence (CC BY or PD) and scale;
  prompts.json is empty with a reason ("No painted assets"). No people images.
- Words: no em dashes in src.html, notes.md, spec.md, voice/lines.json; "Curio Class" everywhere, never "Curio" alone.
- Privacy: "Your sketches stay on this device." on the sketchbook; a note saved, survived a reload in a fresh tab
  (r2 sb-write, sb-reload: `["craft test note"]`), save status "Saved on this device."
- Lesson creep grep (score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done,
  what is, collected): no hits in src.html.
- Keyboard: four dials are `role=slider` with aria-valuetext in units, arrows, Shift, Home and End; turret buttons,
  keys 1 to 4; eyepiece takes arrows and Enter; visible gold focus ring (r1 first-up.png). Plate and Manual lower-left,
  Motion, Sound, Read on their own POWER panel at 1366x768 and 375x812 (audit size-*.png).

## Findings

### Should fix

1. **Source photographs are too small for the objectives they are viewed through** (material.json assets;
   spec "Real material": base images up to 2400 px). onion-iodine is 85x80 px at 3.9 µm/px, leaf 64x132 px,
   leaf-detail 48x70, onion-detail 92x78, cheek 335x310 at 3.9 µm/px. At 40x (field 450 µm) the cheek shows about
   115 source pixels across the eyepiece, so it reads as out of focus while FOCUS says +0 µm (r2/cheek-40.png). The
   onion slide is one 0.4 mm square patch on empty glass (r2/onion-iodine.png). Total art is about 0.9 MB of the
   spec's 4 MB budget, so there is room for real, scannable fields. Better: larger sources per slide, or drop the
   40x/100x claim for slides that cannot carry it. family:curiosity.
2. **Journal-figure furniture is on the slides.** The blood smear is the source's 2x4 figure grid, with panel letters
   A to H and scale bars, mirrored by the optics (r4/blood-100-oil.png). The crane-fly wing keeps the plate's panel
   number "2" (art/wing.webp lower right; visible in the tray thumbnail, audit state-specimen-tray-1366x768.png).
   A microscope slide never has these. Crop or mask them out. family:curiosity.
3. **Cutouts show their edges.** At 10x the diatoms sit in pale yellow discs and the algal mat is a grey rectangle
   with hard edges (r4/sharp-10x.png, crop craft/pond10-crop.png); at 40x the diatom and rotifer photos are visible
   rectangles of a different backdrop (r1/first-down.png). It reads as pasted photos, not a wet mount. Feather or
   mask the cutouts into the glass tone. src.html:1083-1090. family:curiosity.
4. **Iodine shows no stain colour.** onion-iodine.webp is grey (enlarged: craft/onion-iodine-x4.png), so choosing
   Iodine swaps one grey field for another while the mount reads "iodine" and the drawer says "Lugol-stained"
   (src.html:1383). Spec palette and Done when 2 expect amber-brown. Teaching lens should confirm what the source is.
   family:curiosity.
5. **Frame times miss 60 fps when panning.** Measured with rAF in drive.py's headless Chrome (`--disable-gpu`, so a
   software-raster, pessimistic proxy for a modest laptop), 150 frames each, at 1366x768, canvas 430 px:
   4x pond sharp median 16.7 ms, p95 33.4 ms; 4x pond with the default +50 µm defocus median 33.3 ms, p95 50.0 ms;
   one `draw()` defocused at 4x 32.6 ms, iris at 20% 27.4 ms (r1 perf, r2 perf-4x). Causes in the code: `ctx.filter`
   blur and contrast are applied to every sprite's `drawImage` separately (src.html:1146, 1098), and every frame also
   redraws the glass locator and copies the view into the sketchbook preview even when the book is closed
   (1218-1220). Blur once (draw sprites to an offscreen layer, filter that), and skip the hidden preview. Done when 8
   is not shown. general.
6. **The first focus turn the "wrong" way does nothing.** The bench opens at 40x with focus +50 µm (src.html:992),
   already at the blur cap (1142). A first turn up, wheel up or drag up goes to +100 µm: the view is unchanged, but
   the hint vanishes and is not shown again (r1/first-up.png vs first-down.png). Half of first touches get no
   reaction, against Done when 1. Open at 4x (depth 55 µm) or uncap the blur so either direction changes the image.
   family:curiosity.
7. **The welcome names a control the student cannot reach.** A first tap on Specimen tray, Prepared slides,
   Prepare mount, Sketchbook or Manual opens a modal dialog and then speaks "Turn the focus knob." while the knob is
   inert behind the backdrop (audit "One held click" rows 0, 1, 2, 6, 20: spoken, heard; frame
   state-specimen-tray-1366x768.png). Give the welcome a `valid` check that no modal dialog is open. general.
8. **Lamp and Iris sliders are 26 px tall** (src.html:157; measured 286x26 at 1366x768, 23 px at 375 wide, 20 px in
   short windows). Under the 44 px target. general.
9. **At 375x812 the sketchbook is off screen.** The tray is a sideways strip (src.html:529) whose scrollWidth is
   962 px in a 343 px box; Place, Wash, the micrometer and Sketchbook start at x 641 with no cue beyond a clipped
   "Prepare mo" (r2/m375.png, m375-scroll; audit lead confirmed). On a phone there is no K key, so the sketchbook, a
   main feature, is effectively hidden. general.
10. **FIELD has no unit on a phone or a short window.** The unit lives in `small` ("mm diameter"), hidden at 375 wide
    (src.html:433) and under 530 px tall (384): the readout shows a bare "0.45" (r2/m375.png). The look rule is
    readouts with units: put "mm" in the value. family:curiosity.

### Polish

11. **Readouts are 10 px at 1366x768**: SCALE, STAGE X / Y, FOCUS, DEPTH, the mount line, the plate and the lens
    caption (src.html:172-177, 328-329; measured). Readouts are the point of a Curiosity; 12 px or more at the main
    size would read across a desk. general.
12. **The tray is three text buttons that open card dialogs** (src.html:561-563, 667-684; audit
    state-specimen-tray-1366x768.png, state-mount-preparation-1366x768.png). Spec Look asks for glass slides,
    dropper bottles and cover slips on the bench; the modal also hides the eyepiece while the mount is being made,
    so the student cannot see water, iodine or bubbles change the view as they choose. Better: a drawn tray beside
    the stage, or a non-modal drawer that leaves the eyepiece visible. family:curiosity.
13. **Read wording**: "Pond water, water, none, covered. 400 times." (src.html:1040-1042; r1 read-onion log, audit
    row 23). "none" has no noun. Better: "Pond water, wet mount, no stain, cover slip on." general.
14. **The same sprite repeats in the same pose** across the pond at 4x and 10x (r4/sharp-4x.png, sharp-10x.png).
    The Manual is honest about reuse; varied rotation and scale per copy would hide the stamp. family:curiosity.
15. **Blur is in device pixels, not field units** (src.html:1142-1147): a capped 24 px blur on a 430 px canvas and on
    a 1020 px one (DPR 2) look different, so the same focus state is blurrier on a small screen. Scale blur by canvas
    size. general.

### Nits

16. The crosshair "⊕" on the readout label sits on "MAG" (src.html:168; craft/mag-corner.png). general.
17. FOCUS reads "+0 µm" at best focus (src.html:1232). general.
18. After Sound is toggled the kit relabels it "🔇 Sound" or "🔔 Sound", while the tool resets Motion to plain text
    (r1 sound-motion log; src.html:1070). Reset Sound's label too. general.
19. Bare letter shortcuts E, R, X, K work wherever focus is outside a field (src.html:1713-1724); X washes the slide
    with no undo. Consider X only when the eyepiece or tray has focus. general.

## Standard voice check

Only one fixed line ("Turn the focus knob.", the first-run welcome) plus the dynamic Read. `allLines()` and
voice/lines.json match word for word. Status lines go to an aria-live region and are not voiced.

| line | kind | expected | spoken |
|---|---|---|---|
| Turn the focus knob. (tap on eyepiece, five held taps 2 s apart) | welcome / how | 1 | 1 (audit five-click rows clean; r1 first-wheelup log) |
| Turn the focus knob. (first touch is a focus turn) | welcome | cut at once | started, then hushed by the turn (r1 first-up, first-down) |
| Read (onion, iodine), five taps 0.3 s apart | read | 5 | 5, each current (r1 read-onion) |
| Sound as first tap | none | 0 | 0 (audit row 22) |
| Read as first tap | read only | Read text only | Read text only, no welcome (audit row 23) |

Stale lines: one found, finding 7 (welcome over a modal). Order: no line from an older action played after a newer one.

## Sensitivity

Nothing cultural, Native or hard-history. The blood smear comes from a malaria case; the Manual says so plainly.

## Audit pilot

- Leads confirmed: 375x812 tray cut short (finding 9); welcome "heard" after taps that open dialogs, which the audit
  logged as fine and is finding 7.
- Leads wrong: hint overlapping #view at every size (it is the designed quiet hint on the instrument); "hint out of
  view" in calibration, colony and sand states (correctly hidden after the first focus turn); keep regions covered in
  dialog states (expected for a modal; the modal itself is polish 12); manual overlap at 375 (not visible on its frame).
- Missed: figure letters, scale bars and cutout edges in the art (2, 3); low-resolution sources (1); grey iodine (4);
  frame times (5); first turn the wrong way (6); 26 px sliders, which its target check did not flag (8); FIELD with no
  unit (10).
