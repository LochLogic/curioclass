# Codex report: microscope-bench (Curiosity No. 06)

## Built

Second build, Cory's decision of 2026-11-05. The bench now contains its real material: **27 licensed photographic crops and focal planes, 13 source groups, ten photographic slide choices and the exact stage micrometer**. It opens on a blurry pond assemblage at 400× total magnification. One coarse focus detent reveals the photographed material and starts the computed swimming paths. There is no welcome screen or lesson sequence.

Changed from the first build: installed the physically scaled photographs; built the specimen tray, prepared-slide box and preparation drawer; connected actual unstained and Lugol-stained onion fields, water/dry mounting, cover slips, modelled air bubbles and fixed source preparations; added swimming photographic sprites, nine measured colony depth planes, photograph hit regions and the glass locator. CIL:43552 was retrieved this time but still rejected for missing digital calibration; an independently scaled, licensed root-tip source is used instead. Unsupported specimens have no empty or coming-soon slots.

Kept the working first-build instrument, exact ruler and reticle, focus/stage controls, four objectives, lamp, iris, oil model, keyboard access, local sketchbook and printing. The engraved Curio Class Curiosities / No. 06 / Microscope Bench plate and Manual remain lower-left. Motion, Sound and Read occupy their own power panel. The final corrections fix compact-tray clipping, cross-box stale selection, a sticky footer intercepting the lower slide at 800×500, locator stroke thickness, reticle-number contrast and long-note PDF clipping. Static locator photographs are cached; material geometry and physical sampling are unchanged.

The offline file is **1,355,958 bytes (1.356 MB)**, below the 2 MB goal and 6 MB ceiling. Photographic WebP files total 913,352 bytes before base64 embedding. `notes.md` records the size. The larger seven-line opening budget proved unnecessary.

All authored changes are confined to `tools/microscope-bench/` and `_scratch/microscope-bench/`. `codex-report-1.md` is retained untouched; its SHA-256 is `e0ac32dfcf21e140aa4be2060bb03b649b38e65714c4847012f80ffb03052191`. No commits, publishing, shared-engine changes or polish round. The final report was deferred until all work was checked because the owner's stop-on-report instruction takes precedence over an early report scaffold.

## The real material

Sources were checked individually for PD or CC BY rights. NIH/PMC hosting was not treated as a public-domain grant. The author licences govern those photographs. The manifest contains each crop's source and binary URLs, credit, licence link, fetched UTC time, original and packed SHA-256, dimensions, original/preserved physical sampling, crop rectangle, resampling and mask information. Source magnification is supplementary; **objective power alone was never used to invent digital µm/pixel**.

Network gathering began 2026-11-05 at 23:42:14 UTC. The initial accepted photographic package was packed by 00:18 UTC. The last three bounded pond-source attempts, near 00:29 UTC, returned 403 and were omitted. Gathering stayed within the owner's 75-minute cap. Subsequent local cropping, bar measurement and rendering checks were build work. Raw downloads and scripts remain in Scratch, and only accepted WebP material is shipped.

| Material / source group | Rights, credit and source URL | Fetch date and scale / sampling |
|---|---|---|
| Characterization of Crystals in Ciliate Paramecium bursaria, Fig. 1a centre | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Yuuki Kodama, Ayasa Kitatani, Yuriko Morita. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11246328/) | 2026-11-05 UTC. 20 µm bar = approximately 69 pixels in the downloaded figure. |
| Adineta beysunae (10.3897-zookeys.941.50465) Figure 3.jpg | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Zeng Y, Wei N, Wang Q, Iakovenko NS, Li Y, Yang Y (2020). [Source](https://commons.wikimedia.org/wiki/File:Adineta_beysunae_(10.3897-zookeys.941.50465)_Figure_3.jpg) | 2026-11-05 UTC. Photographic panel B only. Vertical 50 µm bar = approximately 538 original pixels. Drawing A excluded. |
| Bancsó 2021 Fig 7-8 Pinnularia viridis.jpg | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Sándor Bancsó. [Source](https://commons.wikimedia.org/wiki/File:Bancs%C3%B3_2021_Fig_7-8_Pinnularia_viridis.jpg) | 2026-11-05 UTC. 20 µm bar = approximately 165 pixels in the downloaded 1280 px thumbnail. Scale measured after thumbnail resampling. |
| 41396 2020 676 Fig4b.jpg | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). H. S. Tee, D. Waite, L. Payne, M. Middleditch, S. Wood, K. M. Handley. [Source](https://commons.wikimedia.org/wiki/File:41396_2020_676_Fig4b.jpg) | 2026-11-05 UTC. Lower-right panel: 20 µm bar = approximately 89 pixels. One unlabelled filament crop. |
| Hemocytometer grid with human hair 100x.jpg | [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/). Jeffrey M. Vinocur. [Source](https://commons.wikimedia.org/wiki/File:Hemocytometer_grid_with_human_hair_100x.jpg) | 2026-11-05 UTC. Known-size object: central haemocytometer fine squares, 50 µm, approximately 50 px. Inferred standard Neubauer grid pitch, not a camera calibration. Both axes agree within about 2%. |
| Marine biogenous aragonite sand (modern; sandy beach at French Bay, San Salvador Island, Bahamas) (48739969587).jpg | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/). Sara Beth Kopczynski, shared by James St. John. [Source](https://commons.wikimedia.org/wiki/File:Marine_biogenous_aragonite_sand_(modern%3B_sandy_beach_at_French_Bay,_San_Salvador_Island,_Bahamas)_(48739969587).jpg) | 2026-11-06 UTC. 2 mm white bar = approximately 280 pixels. Reflected-light source; not transmitted-light sand. |
| Tipula dechangensis (10.3897-zookeys.1040.64376) Figures 1, 2.jpg | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Men Q-L, Starkevich P, Saldaitis A (2021). [Source](https://commons.wikimedia.org/wiki/File:Tipula_dechangensis_(10.3897-zookeys.1040.64376)_Figures_1,_2.jpg) | 2026-11-06 UTC. Photographic wing panel 2 only. 2.0 mm bar = approximately 206 pixels. Specimen is a crane fly, not a housefly. |
| Mobile-phone-based Rheinberg microscope with an LED array, Fig. 9a | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Yuma Ogasawara, Ryo Sugimoto, Ryoji Maruyama, Hidenobu Arimoto, Yosuke Tamada, Wataru Watanabe. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC6975239/) | 2026-11-05 UTC. 100 µm bar = approximately 47 pixels. Brightfield panel a only. |
| Low-cost 3D-printed lenses for brightfield and fluorescence microscopy, Figs. 5C, 5E, 6D and 6F | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Jay Christopher, Liam M Rooney, Mark Donnachie, Deepak Uttamchandani, Gail McConnell, Ralf Bauer. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11019669/) | 2026-11-06 UTC. Fig. 5: 250 µm bar ≈64 px; Fig. 6: 50 µm bar ≈76 px. Unlabelled crops strictly within commercial-lens lower-left halves. Onion uses Lugol iodine; Hosta epidermis is a water mount. |
| Pocket MUSE, Fig. 8a brightfield only | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Yehe Liu, Andrew M. Rollins, Richard M. Levenson, Farzad Fereidouni, Michael W. Jenkins. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC7955119/) | 2026-11-06 UTC. 300 µm bar = approximately 77 pixels at downloaded 1200 px figure width. Original CytoStain and propidium iodide preparation; no fluorescent panel reproduced. |
| Exogenous application of mycotoxin fusaric acid, Fig. 4, control root-tip mitosis | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kürşat Çavuşoğlu, Dilek Çavuşoğlu. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC10960845/) | 2026-11-05 UTC. 10 µm bar = approximately 35 pixels. Four control fields; Feulgen staining, original photographic panels a–d. |
| Human Plasmodium knowlesi Infection, Fig. 1 | [Public domain](https://wwwnc.cdc.gov/eid/page/copyright-and-disclaimers). J. J. van Hellemond and coauthors; CDC Emerging Infectious Diseases (2009). [Source](https://wwwnc.cdc.gov/eid/article/15/9/09-0358_article) | 2026-11-05 UTC. Caption: 5 µm bar, approximately 28 pixels in this 600 px figure. Eight Giemsa-stained blood fields with malaria parasites. The uninfected cell near source x105,y50 spans about 42 pixels, independently approximately 7.5 µm. |
| High-contrast multifocus microscopy with a single camera and z-splitter prism, Supplement 1, Fig. S9b | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Sheng Xiao, Howard Gritton, Hua-an Tseng, Dana Zemel, Xue Han, Jerome Mertz (2020). [Source](https://doi.org/10.6084/m9.figshare.12964487.v3) | 2026-11-05 UTC. 100 µm bar = approximately 98 pixels in extracted PDF JPEG. Nine simultaneous focal planes spaced 25 µm, +100 to -100 µm. Fixed Volvox in Eukitt; darkfield, original ImageJ green-fire-blue lookup table retained. Same registered crop for every plane. |

The pond deliberately reuses four source specimens in a larger assemblage of 22 photographic instances. They retain their source dimensions; counts, positions and swimming trajectories are model parameters, not measurements of a natural pond. Rotifers, diatoms and filament patches remain still photographs. No cilia, cells, grains, wing veins or other anatomy were painted or generated. Photograph edges, source sampling and finite coverage remain visible. Original in-photo abbreviations and panel letters are retained where removing them would require inventing anatomy.

The colony is a fixed Volvox preparation from a CC BY supplement, not living fluorescence. Nine registered source views are spaced 25 µm apart, from +100 to −100 µm; focus blends neighboring planes, with computed blur outside the measured span. Its original darkfield and ImageJ pseudocolour remain declared in the eyepiece caption and Manual. The source PDF, metadata and extracted JPEG are preserved. Other defocus is computed. Sand retains its reflected-light capture. The wing is a crane fly. Hair uses an inferred standard haemocytometer pitch, with that uncertainty stated. Root-tip fields are separate Feulgen control-cell photographs, not a continuous invented tissue map. Blood is a Giemsa-stained malaria sample, not a normal-blood atlas. The cheek smear retains CytoStain and propidium iodide; it is never labelled methylene blue.

Water, cover glass, bubbles, iris and oil alter a declared optical model. They do not change the original photographic chemistry. Iodine selects genuine Lugol-stained onion fields from another preparation, rather than claiming a registered before/after experiment. Prepared slides keep their original stain and medium. The Manual names these limits and every source.

Independent factual checks and rights status, also recorded in the Manual and `tool.draft.json`:

- [Nikon objective properties](https://www.microscopyu.com/microscopy-basics/properties-of-microscope-objectives) and [Rice microscope measurement](https://www.ruf.rice.edu/~bioslabs/methods/microscopy/measuring.html): field, magnification and measurement relationships. Copyrighted factual references; no illustrations or prose passages reproduced.
- [Nikon depth of field](https://www.microscopyu.com/microscopy-basics/depth-of-field-and-depth-of-focus): the implemented wave-optical term. FN 18, eyepiece 10×, apertures, reference focus and oil index are explicit model assumptions, not source-camera measurements.
- [Nikon reticle calibration](https://www.microscopyu.com/tutorials/reticlecalibration), Rice and [Merck calibration](https://www.merckmillipore.com/Web-IN-Site/en_US/-/EUR/ShowDocument-Pronet?id=201605.071): independent dimensional/calibration references. Copyrighted reference material only. The exact 1 mm / 100-interval calibration slide is original code.
- [Clinical Methods: peripheral blood smear](https://www.ncbi.nlm.nih.gov/books/NBK263/) and [OpenStax erythrocytes](https://openstax.org/books/anatomy-and-physiology/pages/18-3-erythrocytes): independent textbook comparison, about 7–8 µm. No reproduced diagrams or text passages.
- [ZEISS haemocytometer guide](https://asset-downloads.zeiss.com/catalogs/download/mic/96e9e3a7-f2fd-4989-94e3-d12412701623/EN_wp_How-to-Use-a-Hemocytometer.pdf) and [Marienfeld counting grids](https://www.marienfeld-superior.com/counting-grids.html): 0.05 mm fine squares. Copyrighted factual references only.
- [Nikon specimen contrast](https://www.microscopyu.com/techniques/phase-contrast/specimen-contrast-in-optical-microscopy), together with the independent Rice operating/calibration reference, informs the declared iris approximation. Biological identities and original preparations are attributed to the source authors rather than claimed as independently authenticated specimens.

Reproducibility: `curate2.py`, `accepted-cuts.json`, `pack2.py`, `pack-results.json`, `catalog2.py` and `provenance2.py` hold the cut list, Chrome WebP conversion, scale factors and source chain. The independently inspected 250 µm bars in the exact low-power onion/leaf figure span 64 pixels (`scale-probe2.json` and `scale-bar-detail.png`). Repacking all material starts by running `curate2.py` to restore the complete settings list; later packing used small correction batches while retaining the combined results.

Rejected material is preserved as research evidence, not shipped: unscaled CIL:43552 despite a stated 40× objective, ambiguous numerical scale labels without a drawn span, internally implausible source bars that would require guessing a correction, unscaled crystal/feather/cheek photographs, and NC/ND/SA-only material. The specification's curation fallback is used for salt, sugar, feather and the methylene-blue preparation.

## Break the instrument

`checks2-final.json` passes the complete functional run. `target-final2.json`, `last2/result.json`, `print-final2/result.json` and `depth-recheck2/result.json` record focused corrections. Tests used actual held mouse clicks, whole-pixel stage drags and keyboard input; direct state setup was used only to prepare photographic/checking states and timing loops.

- The initial +50 µm defocus becomes 0 with one coarse ArrowDown and the hint disappears. Coarse 0–10 mm, fine −50 to +50 µm, stage axes −10 to +10 mm, and lamp/iris 0–100 all reached their ends through real keys without exceptions or nonfinite values.
- Fields independently match 18/objective: 4.50, 1.80, 0.45 and 0.18 mm. Nominal reticle factors are 25, 10, 2.5 and 1 µm/division. Fifty rapid stage keys finish at 2.50 mm. A rightward real drag increases slide X while the image transforms in the opposite direction.
- Dry 100× is dimmer and softer; adding oil changes the estimated depth from 1.3018 to 0.53328 µm. These are model values. Lamp zero and a fully closed iris intentionally darken the field; the iris-zero centre pixel was [0,0,0,255]. Controls remain usable. Washing leaves empty glass and halts specimen motion.
- Keyboard Enter selects a tray item and Enter on the eyepiece mounts it. Every offered photographic mount decoded, produced a distinct field and retained its source sampling. Iodine, none, wet/dry, cover removal/replacement and careless/gentle cover handling were exercised. Prepared source preparations remain fixed.
- Every one of the nine measured colony planes produced a distinct rendered hash. The initial two-minute depth leg actually remained on root tip because the lower colony card was intercepted by a sticky footer. That failure was found in the state trace, fixed, and followed by a separate 120-second real-input walk at 800×500. The retry asserts the colony was selected/mounted and visits every 25 µm plane from −100 to +100.
- Motion off leaves the swimming clock exactly unchanged. After its one pending redraw, idle rendering stops; the final idle test had zero continuing renders. Resuming does not apply accumulated hidden time.
- Calibration rejects zero counts and stores factors separately per objective. A valid 100 µm / 100-reticle-interval calibration gives 1 µm/division at 100× objective. The blood source has a 42-pixel uninfected red cell and a 28-pixel 5 µm bar: 42 × 5 / 28 = **7.5 µm**, or 7.5 calibrated reticle divisions and about 18 rendered pixels. This agrees with the independent 7–8 µm textbook range within 20%, allowing source endpoint uncertainty. It is a dimensional check, not clinical validation.
- A keyboard stroke, label, note and 400× magnification survived reload. The first long-note PDF exposed modal clipping; normal document flow now prints the full 3,064-character test note across two pages. PDF extraction confirms all 38 repeated phrases and its final marker, and both pages were inspected in Chrome's PDF viewer. No bench controls print.
- At 1366×768 with fourfold CPU throttling, the expanded pond initially averaged 59 fps. Static locator-photo caching removed the repeated work. The longer 300-frame samples were pond **60.002 fps**, hair **59.603 fps**, sand **59.603 fps**, with 95th-percentile intervals of 16.7–16.8 ms. This is a desktop performance proxy, not a physical Chromebook benchmark.
- No runtime exceptions or automatic external HTTP/HTTPS requests occurred in the functional, focused or timed exploration runs. No remote image, font or library is required by the instrument.

All command batches have wall-clock stoppers: bundle at most 120 seconds, normal browser/check batches under five minutes, exploration in two-minute phases, and the single mechanical audit capped at 25 minutes. Helpers close their owned muted Chrome profiles and local host. An initial read-only brief/memory pass used yield limits rather than a wall-clock stopper; that process deviation is retained here instead of claiming every opening read was bounded.

## Voice walk

The specified bank remains `science-narrator`, quietly styled, with the browser-voice fallback and no recorded clips. The sole fixed line is Turn the focus knob. A real focus change hushes it and makes it obsolete. Read announces the current mount, total magnification and field, without inventing an untapped feature name.

The audit's held-click walks at a two-second pace, repeated clicks and quick taps were clean. Non-focus first actions can hear the single hint; Sound off cuts it, Read avoids adding it, and turning focus first suppresses it. The functional walk pressed Read twice with a two-second gap and recorded the current readouts in `__tool.vlog`. Chrome was muted throughout as required. Queue/timing behaviour was checked; human voice quality and a recorded narrator performance are not claimed.

## Short test

The scripted operator exploration lasted **600.5 active seconds**, using student-oriented focus/chasing/preparation and adult-oriented depth/calibration/recording perspectives. It used real input and unhurried pauses, with observations of the resulting frames. It is not a sixth-grader/adult participant study or a month-long follow-up. It found the lower-card selection failure described above; after correction, the successful 120-second depth retry brings observed exploration above twelve minutes. Subsequent print and selection fixes received focused verification rather than restarting a polish round.

| Question | Honest assessment |
|---|---|
| Would a kid open it unassigned? | Likely yes: focus reveals real photographed life and moving specimens can leave the field. The knobs and supplied glass offer immediate things to handle. Some photo edges and small source fields limit the illusion. |
| Would an adult play for fun? | Yes in operator review: chasing, calibrating against real bars and passing through measured colony depth are satisfying. Repeated pond individuals and a finite library will become recognizable. |
| Is the real thing the interface? | Yes: the photographs, physical sampling, inverted stage, reticle and focus carry the activity. No answer panel stands between the user and the material. The Manual distinguishes source data from optical/motion approximations. |
| Does it work without score or finish? | Yes. Nothing evaluates, awards, unlocks, counts discoveries or ends the exploration. The user's sketchbook is the only record. |

The reference tools were opened and used: Beat Lab playback (confirmed with the actual icon Play control), Elements Inspector on iron, and both Span and Spire / Pocket Universe Manual drawers. Their instrument confidence and family controls informed this bench, without importing lesson headers, missions or palettes.

| Microscope Bench | Elements Inspector |
|---|---|
| ![Microscope bench with real material](../../_scratch/microscope-bench/last2/bench-final.png) | ![Elements Inspector on iron](../../_scratch/microscope-bench/models-2/elements.png) |

## Lesson creep check

The final source/voice search covers score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done, what is and collected. The only remaining hit is JavaScript's `im.complete` image-loading property, not visible UI or a completion state. The earlier descriptive word points was changed to details. No score, goal, level, collection count, mode pills, kit header, quiz, reward or finish screen was introduced.

## Done when

| Spec item | Result and evidence |
|---|---|
| 1. Blurry pond and first focus reaction | **PASS.** Opens directly on real pond photographs at +50 µm; one real coarse detent sharpens them and starts paths. |
| 2. Every offered specimen/preparation matches real material | **PASS under the stated curation fallback.** Ten photographic slides and the ruler are usable; unsupported materials are absent. Original stains/contrast, different onion preparations and model-only mounting effects are declared. |
| 3. Licensed manifest and Manual inventory | **PASS.** All 27 photographic assets have permitted rights, source/credit, physical sampling and hashes; all source groups appear in the Manual and metadata. |
| 4. Calibrated cheek or red-cell size within 20% | **PASS.** Independently barred blood source gives 7.5 µm and agrees with both textbook references; calibration uses the exact ruler. |
| 5. Inversion and dry immersion softness/dimming | **PASS.** Real drag/key checks and oil-model checks recorded. |
| 6. No questions or premature added feature names | **PASS for the interface.** Inspection below 40× says Look closer; names require inspection at 40× or higher. Existing abbreviated source annotations/panel letters are photographic data, not added prompts, and remain a disclosed limit. |
| 7. Private book, persistence and print | **PASS.** Stroke/label/note/MAG reload checks; full long-note PDF verified after clipping correction. Privacy is stated on screen. |
| 8. Keyboard/value access and Chromebook 60 fps | **FAIL as a literal hardware acceptance claim.** Keyboard/value access passes and the fourfold CPU desktop proxy runs about 60 fps; no physical Chromebook or separately specified school hardware profile was available. |
| 9. Responsive layout, plate/Manual, AA, frozen swimmers | **PASS.** Every STANDARDS size checked; final 375×812 has zero horizontal document overflow, plate/Manual bottom at 810 px, and a 286 px ocular. It is smaller than the suggested 340 px so working controls fit. Motion freeze is measured. |
| 10. Offline and short test with comparison | **PASS for the operator test.** No automatic external requests; twelve-plus minutes including the corrected depth leg, with comparison above. No human study claim. |
| 11. No lesson/game layer | **PASS.** Source/voice search and visual inspection; no evaluative or progress layer. |

## Audit leads

One full audit finished: `_scratch/microscope-bench/audit2/audit.md`, **65 leads**, not a claimed clean audit. Repeated held clicks, quick taps, mid-action resizing and Motion off were clean.

The leads are accounted for by the intentional one-time focus hint overlapping the optical field; native modal drawers/backdrops covering inert underlying keep regions; the specified horizontally scrolling phone shelf; and a collapsed-details paragraph/summary rectangle that does not paint an overlap in the inspected Manual. Active drawer controls fit their scrollable drawers. Source links are deliberate outbound actions only.

Visual/state-trace findings fixed during this build: compact micrometer text clipping; cross-box stale description/selection; the 800×500 sticky footer intercepting the colony card; thick adaptive locator outline; reticle-number contrast; UTF-8 JSON reading; and long-note modal print clipping. After the single audit, the print document, selection guard, locator outline and number halos were corrected and checked with focused browser/PDF runs. The full audit was not repeated after those changes.

Contrast ratios: cream/bench **7.18:1**, readout **11.56:1**, slide-tray text **10.91:1**, Manual links **7.32:1**. The grayscale frame was inspected. Disabled preparation controls retain their original-source explanation. The permanent instrument controls, plate and Manual remain in view; the phone slide shelf scrolls intentionally.

## Frames looked at

Viewed the model references, raw candidate figures and scale evidence, first second-build frames, all 24 `frames2/` frames, all 24 `frames2-final/` frames, all 24 audit frames, seven exploration frames, every `target-final2/` frame, the print layout, final correction/PDF frames and the corrected depth frames. Review sheets preserve original frame pixel dimensions; phone, source crops and final correction views were also inspected individually. Preliminary phone shots whose outer host was only 768 px tall were superseded by the isolated full 375×812 captures, rather than used to claim a visible plate.

Evidence: `checks2-final.json`, `target-final2.json`, `print-final2/result.json`, `depth-recheck2/result.json`, `last2/result.json`, `validation2.json`, `audit2/audit.md` and `review-sheets2/`. Final offline HTML SHA-256: `f6517e7cdb752246d3cfb269c92d7809a1802ce6e4b47d8fc5bc2b4186854b6d`.

## Art made

Original code draws the bench, enamel instrument, glass, knurled knobs, stage scales, reticle, preparation bottles and modelled air boundaries. No AI bitmap art was made. The 27 photographic assets are cropped/resampled WebP reproductions under their recorded licences, not generated specimens. Total photo bytes: 913,352; final offline file: 1,355,958 bytes. `art/prompts.json` explains why there are no painted assets.

## Engine changes wanted

No shared changes. The existing guarded localStorage adapter is retained because this checkout's kit exports no save/load API. It reports storage failure visibly. Any future shared persistence work should follow the three-tool rule; it is not required by this build.

## Left open

- Qualifying physically calibrated salt, sugar, feather and methylene-blue cheek material were not found within the bounded curation pass. They are omitted using the spec's explicit fallback. The prepared cheek photograph uses its real, different stain.
- Resolved hair cuticle, wing interior microhairs and beating rotifer cilia are not fabricated. Source sampling/still photographs limit those experiences. Broader contiguous biological fields would deepen the finite library, but no empty data slots are shipped.
- The pond reuses individuals and its paths are simulated. Biological names/preparations come from source authors; no independent specimen authentication or ecological abundance claim is made. Source annotation abbreviations remain visible.
- A physical school Chromebook benchmark and human grade-6/adult follow-up remain unperformed. Browser voice quality was not assessed with unmuted audio. The phone ocular remains below the suggested 340 px.
- The explicit owner choices taken unattended: preserve the first report; use genuinely barred/known-object scale rather than objective-only estimates; choose curated omissions over invented material; keep source contrast/preparations honest; use an actual fixed-colony depth series and computed still-sprite motion; retain browser speech fallback. The 75-minute gathering cap superseded 45 minutes. No permission questions were asked.

This report closes Build only. No polish round, commit or release action follows it.
