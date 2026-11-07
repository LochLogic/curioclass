# Polish: microscope-bench (Codex fix, round 1)

The Curiosity brief governs. No lesson welcome, goal, score, quiz, level, finish or kit header was added. This pass is **not ready to clear the exit gate**: the coherent specimen blocker and steady-60-fps item remain open.

Evidence paths below are relative to `_scratch/microscope-bench/`. Screens were driven with `scripts/drive.py`. The principal frames are 1366×768; phone frames use a real 375×812 iframe. All commands from the repair runner have explicit child-process deadlines: reads 20 seconds, packing 120 seconds, drives 300 seconds, audit 2400 seconds. Initial brief reads completed immediately before the explicit process-killing wrapper was installed; those initial reads did not have explicit execution deadlines. No commits. `refine.md` and `refine/` untouched.

## Blocker

1. **NOT FIXED, partially repaired: photographic specimens.** Before: `fix-before-all/before-{pond,onion,root,blood,cheek,wing}.png` and `fix-before-extra/root-before-100.png`. After: `fix-material/`, `fix-controls/iodine.png`, `fix-final/root-final.png`.
   - a. Blood is now eight individual, physically scaled fields without the letters, gutters or source bars. Wing panel numeral and rotifer B are cut away. Paramecium Cy/Ma are alpha-masked, leaving disclosed gaps rather than reconstructed anatomy; focal-stack corner annotation masked. New blood assets are 138×82 px each, 0.17857 µm/px. Art furniture repair seen, but this does not supply a larger blood field.
   - b. Pond bodies use shaped alpha masks; yellow diatom disc and pale rectangular surrounds removed. Borders are feathered. The root close-ups have neutral surrounds masked. Finite root/onion/leaf fields still read as bounded photographic patches: not claiming the whole edge/background item cleared.
   - c. **Open.** CIL:43552 supplies a real 1280×1024 root field and a nonempty centre at low power. Other finite fields still lack the specified broad base plus 512 px detail coverage. No tissue was tiled or fabricated to fill the glass.
   - d. **Open.** Positions, rotation and modelled size vary, removing the near grid, but the pond still reuses four photographic individuals. No claim of new individuals or natural abundance.
   - e. Larger publisher cheek figure recovered (1967×1297 versus 1200×791), but nucleus detail is still inadequate. Source enlargement beyond about 2× is captioned SOURCE RESOLUTION LIMIT. Wing source bar retained at 2 mm / 206 px; 13.79 mm is crop width including background, not wing length. The species range is not used to rescale the photograph. **Fine wing hairs remain unresolved.**
   - f. Unstained onion LED cast corrected by per-channel white balance, explicitly stated. No grey image was tinted amber. Iodine is captioned MONOCHROME CAMERA. A colour CC BY onion candidate was found but has no defensible scale; it was not substituted. **Colour iodine remains open.**
   - g. Real meristem added, with four separate control close-ups inside it, transparently described as different preparations/stains. Base scale is an inference from nuclear widths cross-checked with the scaled control source, captioned BASE SCALE APPROXIMATE. Source has no pixel calibration. Metaphase note now describes the scattered squash spread. **The finite base remains small at 100× and is unsuitable for precise micrometry.**
   - h. **Open.** A larger Pocket MUSE brightfield panel remains too coarse. A sharp CC0 cheek photograph lacks scale. Do not claim a nucleus hunt or methylene-blue preparation is delivered.
2. **FIXED: first focus turn.** Opens at 10× objective, +50 µm. One downward coarse key reaches +0 µm, blur 0. Up changes blur from 9.345 to 12.373 px; no capped plateau. Real 12/40/50 px downward drags leave +38/+10/+0 µm; upward 12/40 px leave +62/+90 µm. Frames: `fix-controls/{focus-up,focus-down,drag-12,drag-40,drag12,drag40,drag50}.png`. Logarithmic field-scaled blur is explicitly a rendering approximation. Blur/diameter is 0.02279268 at every tested viewport, including 375 and 1920. Phone FOCUS is visible, 15 px high. The hint still leaves after the first focus action.

## Should fix

1. **FIXED: calibration without looking.** Counts open empty; Store disabled. Declared true model powers 3.9/9.8/41/98 differ from labels. Removed worked count. `fix-controls/calibration.png`, `evidence-calibration-cheats.json`: empty, zero, negative and >100 counts blocked; 10/41 stores 2.439024 µm/division. Original 42 px red cell × 5/28 µm/px = 7.5 µm. This is manual measurement, with no correctness score or automatic approval.
2. **FIXED: locator giveaways.** Locator paints only slide outline and current field circle. No photographic call remains in its draw function. `fix-material/pond.png` versus `fix-before-all/before-pond.png`.
3. **FIXED: focal planes.** `after-numbers.json`: pond/onion/root/blood offsets 0/+12/−18/+8 µm at 10×; onion wet/dry/uncovered references +12/+34/+52 µm. Objectives shift focus by only a few micrometres. Hair has a declared depth gradient of 15 µm per 100 µm along its real hair/grid photograph, using cached whole-photo blur textures, not an invented focal stack or new cuticle detail. Final `fix-hair-verified/hair-{minus,plus}.png` frames compare −20 and +20 µm. This model cannot reveal missing cuticle detail.
4. **FIXED: live mount tray.** Uses nonmodal `show()`. At 1366 its x range is 16–316; eyepiece is 431–841, with no intersection. Phone tray remains below the visible eyepiece. `fix-controls/mount.png`, `fix-sizes/phone-mount.png`. Preparation changes apply immediately; keyboard controls remain usable.
5. **NOT FIXED: steady 60 fps.** Removed per-sprite pond filtering; blur/contrast is applied once to a small offscreen layer. Locator updates only on geometric state changes; closed sketchbook preview is skipped. Same 1366×768 4× defocused pan proxy: median/p95 improved from **34.2/34.5 ms to 15.9/31.1 ms** (`perf-before.json`, `perf-after.json`). P95 still exceeds 16.7 ms. No physical Chromebook claim.
6. **FIXED: welcome over drawers.** Welcome has a validity predicate for open dialogs, and modal opening hushes prior speech. Every fresh held first click on Specimen tray, Prepared slides, Prepare mount, Sketchbook and Manual logs the hint as dropped/stale, not spoken. `evidence-voice-first-*.json`.
7. **FIXED: hidden phone shelf actions.** 375×812 shelf wraps into two rows: client/scroll width **343/343**, formerly **343/962**. Place, Wash, micrometer and Sketchbook have visible 44 px targets. `fix-sizes/size-375x812.png`, `size-375x812.json`.
8. **FIXED: phone units.** FIELD value contains “mm”; FOCUS value contains “µm”. `fix-sizes/size-375x812.png`; also checked at 680×425 and 800×500.
9. **FIXED: lamp and iris hit areas.** Both are **44 px** high at all eight tested sizes, formerly 23 at 375 and 26 at main size. `size-*.json`, `after-numbers.json`.
10. **FIXED: field-guide language and duplication.** Notes begin with ordinary identification and one detail. Source/motion caveats are on slide Manual pages. Colony and bubble notes also simplified. Status stays available to screen readers but is visually hidden. `material.json` note fields and `fix-targets-final/guide-final.png`, which visibly shows the plain two-sentence paramecium note.
11. **FIXED: Things people have found.** Restored eight matching entries: Hooke 1665, Leeuwenhoek letter 1676/publication 1677, rotifer wheel, red cell size, interphase, oil index, inversion and iris trade-off. Each has named linked references and licence status. Salt left out. The Hooke entry states the documented name/book/date without relying on the small-room anecdote.

## Polish accepted

1. **FIXED: Read wording.** Heard “Pond water, wet mount, no stain, cover slip on. 100 times. Field 1.84 millimetres.” Mount label matches. `evidence-voice-walk.json`.
2. **FIXED: pre-tap labels.** Tray uses Pond colony/fixed/darkfield/focal series and Blood smear/Giemsa. Motion note says cutouts rather than organism names. Source pages retain scientific names and published blood context. `fix-numbers/prepared.png`.
3. **FIXED: bubbles.** Dark 0.011 mm rims with a focus-dependent bright inner rim. `fix-controls/bubbles.png`.
4. **FIXED: teacher notes.** Names plant/animal cells, walls, nuclei and dividing chromosomes; nine focus photographs explained plainly in `notes.md`.
5. **FIXED: wandering.** Computed turns cover a wider irregular path, not the old ±0.23/0.13 mm loop. Sampled centre moves from (0.10,0.03) to (0.778,0.618) mm by 10 s, turns by 30 s, and reaches (−0.043,0.442) by 120 s. Motion off keeps pose byte-for-byte unchanged. `after-numbers.json`, `evidence-motion-frozen.json`.
6. **FIXED: main readout size.** Data rows, dial labels/outputs, optical label and lamp/iris labels compute at **12 px** at 1366×768. `after-numbers.json` and default frame. Compact layouts retain smaller, legible text.
7. **FIXED: plate wrap.** Second line begins “No. 06”, without a leading separator. Desktop and phone frames.
8. **FIXED: Sound label.** Remains plain “Sound” after two toggles. `evidence-voice-walk.json`.
9. **FIXED: modelling language.** Manual says aperture without oil is “modelled as 0.65”.
10. **FIXED: readout screws.** Corner marks moved above the text inset, including phone. Final phone frame and audit desktop frames.
11. **FIXED: repeated status prose.** `.status` is visually hidden with the screen-reader pattern; separate live region retained. Main frames show no duplicate turret/mount prose.

## Settled calls

All governing Curiosity calls applied: real photographic material only; no tinting, generated biology, abundance claim or lesson frame. The first-run hint still disappears. Calibration variation is small and declared. Locator remains. Only mount preparation became nonmodal. Manual, specimen tray and prepared-slide dialogs remain. No map/standard code changed. No extra omitted tray topics added. Existing turret, reticle, mirrored micrometer, iris/oil behavior, nine-plane colony and local sketchbook retained, with the required calibration/focus deviations described. Sensitivity wording retained. Bundle is 1,532,237 bytes (about 1.53 MB), below 2 MB; `notes.md` size updated.

## Cheats tried

- Click Store on empty counts: disabled, no stored calibration. Zero, negative and 101 counts also blocked.
- Enter 10/41 at 40×: stores 2.439024 µm/division, recovering 7.5 µm red-cell width. Arbitrary positive counts can still be stored intentionally, as on a manual instrument; there is no quiz to pass.
- Use locator to find specimens: no specimens are drawn on it.
- Use a first modal tap to trigger the focus instruction: five drawers all drop the stale instruction.
- Change to strong objective, pan to either stage limit, lamp/iris at zero or full, focus at 0 or 10 mm: no exceptions in eight combinations. Empty/dark glass is the expected optical state.

## Voice walk

Held clicks, 0.12 s, 2 s gaps. Focus knob first speaks the single hint once. Read interrupts it and reads current mount/MAG/FIELD; Sound off/on does not repeat it or add an icon to the label. Second Read repeats the current reading. Five separate first-drawer paths each drop the welcome. `allLines()` equals `voice/lines.json`: exactly one fixed line. Tests are muted; evidence is the kit's started/read log, not an acoustic recording.

## The real material

No generated micrographs. Canonical inventory: `art/manifest.json`, `material.json`, Manual source pages, and `tool.draft.json` sources. Static validation checks 35 assets, hashes, allowed rights and physical sampling with zero mismatches. Photographic bytes 1,027,388. Original files and packing scripts remain in Scratch. Pillow 13 in the Scratch virtual environment encoded the source crops; no system software was installed.

- **New meristem:** Shoba Shanti, CIL:43552, [Cell Image Library](https://www.cellimagelibrary.org/images/43552), DOI 10.7295/W9CIL43552. Archive states Public Domain; rechecked 2026-11-06. Existing raw 1280×1024 TIFF used whole, with border feathering. Approximate scale inference is explicitly marked; no precise measurement claim.
- **Larger cheek:** Liu et al., Pocket MUSE, [source article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7955119/), CC BY 4.0, publisher PNG fetched 2026-11-06. 1967×1297 figure, brightfield panel 8a only, 548×508 unannotated crop. Original 300 µm bar ratio gives 2.38 µm/px. Still insufficient for a clear nucleus.
- **Re-cut pond:** Kodama/Kitatani/Morita, Paramecium bursaria, DOI 10.1007/s00284-024-03793-8; Zeng et al., Adineta, DOI 10.3897/zookeys.941.50465; Sándor Bancsó, Pinnularia; Tee et al., freshwater mat. All CC BY 4.0. Existing raw downloads re-cut on 2026-11-06. Annotation/background alpha masks only; no inpainting. Scale bars retain original physical sampling.
- **Re-cut blood:** van Hellemond et al., [CDC Emerging Infectious Diseases figure](https://wwwnc.cdc.gov/eid/article/15/9/09-0358_article), Public Domain under CDC EID terms. Existing 600×254 raw figure split into eight 138×82 fields, 5 µm/28 px. No source letters/gutters/bars in the view.
- **Onion/leaf:** Ogasawara et al., DOI 10.1117/1.JBO.24.3.031007, and Christopher et al., DOI 10.1364/BOE.514653, CC BY 4.0. Existing raw fields retained, borders feathered; unstained LED cast corrected by channel gains. Lugol photo stays monochrome. No assumed amber colour.
- **Root close-ups:** Çavuşoğlu and Çavuşoğlu, DOI 10.1038/s41598-024-57762-z, CC BY 4.0. Original control panels retain 10 µm/35 px sampling; neutral surround alpha-masked. These are separate Feulgen preparations, not new cells manufactured in the acetocarmine field.
- **Wing:** Men/Starkevich/Saldaitis, DOI 10.3897/zookeys.1040.64376, CC BY 4.0. Full available 1512×1314 file checked, panel numeral removed. 2 mm/206 px scale retained; crop width not asserted as wing length. Higher-detail attempt did not yield an acceptable replacement.
- **Other retained material:** Vinocur hair CC BY 2.5; Kopczynski/St. John Bahamas sand CC BY 2.0; Xiao et al. multifocus supplement CC BY 4.0. Credits, exact URLs, scale derivation and original hashes remain in the manifest and Manual.
- **Rejected candidates:** Anonymous140209 colour iodine, CC BY 4.0, and Kyreb cheek, CC0, downloaded 2026-11-06 but lack a defensible scale. Never bundled. An attempted publisher wing URL returned an unrelated figure and was rejected. No downloaded executables. Gathering was bounded; no further photographs were sought after the curation pass.
- **Facts:** named paired references are attached to every restored Manual entry. Hooke: original Micrographia (PD) plus Marine Biological Laboratory (copyrighted factual reference); Leeuwenhoek: original Royal Society letter/DBNL archival letter (original PD, catalogue/edition reference only); rotifer: OpenStax Biology 2e (CC BY 4.0) plus source taxonomy; erythrocytes: OpenStax A&P (CC BY) plus Clinical Methods (copyrighted factual reference); cell cycle: OpenStax plus CIL; oil/inversion/iris: Nikon MicroscopyU and Rice/OpenStax, copyright reference only except OpenStax CC BY. Original paraphrases, no copied diagrams/text. Model offsets, power deviations, hair depth and compressed blur are declared Curio Class choices implemented in original MIT-licensed code.

## Engine changes wanted

None. All repairs are local. Model-comparison browser connections failed twice; no fresh model frame comparison or ten-minute short-test pass is claimed. The unresolved real-material blocker prevents claiming the adult-fun/real-material short test passes.

## Audit

The single audit **finished**, within its 2400 s limit: `fix-audit/audit.md`, **67 mechanical leads**. It found no runtime errors, no resize exceptions or stuck controls, and no continuing Motion-off animation. Ten repeated held-click controls and ten quick-tap controls were clean. No second audit was run.

Each lead class was checked:

- Eyepiece/hint overlap: intentional on-instrument hint, as explicitly settled in Refine.
- Hidden hints after focusing, colony and sand: expected first-action removal, not a missing lesson instruction.
- Manual, book, specimen/prepared dialog coverage and covered maker/power regions: expected modal backdrop. Nonmodal calibration/mount coverage of some knobs is expected; the live eyepiece remains visible.
- Phone Manual “Reading the instrument” / making-a-mount paragraph overlap: the paragraph belongs to a closed `details`; it is not painted. Native phone Manual frame inspected.
- 1000×625 Calibrate/footer overlap: **repaired and re-shot**. Compact readouts omit secondary rows; main controls remain visible. `compact-final.json`: Calibrate bottom **475**, footer top **545**, a **70 px gap**; `fix-targets-final/compact-final.png`.
- Phone micrometer and four mount legends under 10 px: **repaired to 10 px**. `phone-final.json`, `phone-mount-final.json` and their final frames.
- Empty calibration fields reported “no name”: visible `label for` associations already supplied native names; explicit matching `aria-label` values were also added. No fake default answer restored.
- Phone specimen dialog Place/Prepare buttons cut short: long provenance moved to the existing Manual source pages; tray uses a brief operational note. **Repaired and re-shot:** Place y=628–672 inside the dialog/window in `phone-tray-final.json` and `fix-targets-final/phone-tray-final.png`.
- Missing welcome on six drawer/calibration first taps: the intended valid-check result. This is a Curiosity with one optional hint, not a missing lesson premise. Sound/Read interruptions follow the kit rules.
- Root label now names both acetocarmine and separate Feulgen insets, matching the actual assembled preparation. Final root-label frame inspected.
- A follow-up showed the first hair gradient mapped the sharp portion outside the field; it was corrected to run along the hair in physical field units. Whole-photo blur textures avoid filter seams. Only the two affected hair frames were re-shot afterward.

Nine narrow post-audit shots logged **zero console/JavaScript errors** and **zero external resource requests**. The final two hair shots also logged zero errors. Earlier phone-host runs logged a missing browser favicon from the disposable HTTP wrapper, not an offline-tool request. The old wrapper was closed; later controlled-host checks returned no page errors. A connection-reset traceback while shutting down a request handler was host teardown, not a tool exception. All started task ports were checked and closed before completion.

The final bundle includes these narrow corrections made in response to audit leads; the audit itself describes the immediately preceding bundle. It is not represented as an audit of the later bytes.

## Frames looked at

Before/after main frames, phone/preview frames, all finite slide choices, mount/calibration/book/manual/prepared/specimen drawers, focus/drag/bubbles/iodine, ±20 µm hair, and the labelled contact sheets `fix-*-contact-*.jpg`. Principal data frames inspected at native size. Eight STANDARDS sizes checked once, with narrow follow-ups for changed layout. Audit frames reviewed as described above.

## Left open

- Blocker 1: broad, detailed slide coverage, new pond individuals, fine wing hairs, colour iodine at known scale, clear cheek nucleus. Source captions are honesty fallbacks, not a claim these are fixed.
- Should fix 5: 60 fps p95 requirement.
- No module-map changes; omitted salt/sugar/feather/methylene-blue stay omitted. No new feature or topic added to compensate.
- Full human ten-minute Curiosity comparison was not repeated; browser attempts to open prescribed models failed twice. No fabricated pass.
- Final narrow follow-ups completed; audit-led corrections are documented above. The two explicitly open Refine requirements remain open.

## Lesson creep check

`fix-validation.json` found only two whole-word hits: “Collected Letters” in an archival citation and JavaScript `Image.complete`. Both are legitimate, with no collection/progress system or finish state. No em dash or replacement character in `src.html`. The fixed voice list is unchanged and matches `allLines()`.

Cleanup: removed disposable `host.html` and the unused whole-figure `art/blood.webp`; the original source and before frames remain in Scratch. All 35 retained WebP files are manifested. Final connection check found no listener on 8715 or 9910–9917.
