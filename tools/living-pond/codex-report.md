# Codex report: living-pond (Curiosity No. 13)

## Built

An ecologist's study tank, with a living cut-away pond, specimen tray, strip-chart recorder, oxygen needle, thermometer, light readout, inherited shade strip, and Matter and Energy lenses. It opens running at two weeks per second. The engraved plate and Manual sit lower-left; Motion, Sound and Read have their own power panel.

Stocking, netting, feeding, bottom, decomposers, canopy and climate change the running model immediately. Ghost traces project an unchanged copy for 104 weeks. Eight device-local saved ponds support Open, Replay, Rename and confirmed Delete. Keyboard shortcuts and ordinary keyboard controls work. The Manual contains ten findings, the web, model explanation, dated pond log, sources and honesty notes.

Final offline bundle: **501,506 bytes**, about **0.50 MB**, 25 percent of the 2 MB goal. It contains its artwork and kit code. No runtime network request was observed. No commit, deployment or polish round was made. Authored files stayed in `tools/living-pond/` and `_scratch/living-pond/`. The existing `spec.md` modification was not edited by this build.

SHA-256: `dcf1b34276f813a245defd1b211b5ba1be2807e7d1eac952c2fafbf2edf44e54`.

## The real material

There is **no measured population dataset** in this instrument. The material is the specified deterministic ecosystem model, with seven daily substeps per week, conservative transfers, nutrient-limited algae, type II feeding, oxygen, seasonal temperature and light, refuges, inheritance and sight-dependent predation. Its rates are illustrative model parameters, not measured minnow or pond estimates.

| Source | URL or identifier | Licence / use | Checked and sampling |
|---|---|---|---|
| Curio Class model | Repository `018ace9b:tools/living-pond/spec.md` | Owner-supplied model, implemented here | Every numerical coefficient and starting pool read; no dataset sampling |
| USGS, Dissolved Oxygen and Water | https://www.usgs.gov/water-science-school/science/dissolved-oxygen-and-water | USGS-authored information is US public domain; no third-party images copied | 2026-11-05; qualitative oxygen and decay checks; no numerical dataset downloaded |
| USGS, Copyrights and Credits | https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits | Explicit US public-domain policy, with exceptions for marked third-party content | 2026-11-05 |
| EPA, Nutrient Pollution: Effects | https://www.epa.gov/nutrientpollution/effects-environment | Reference only; no text, images or data reproduced | 2026-11-05; confirms bloom, shade and oxygen relationships |
| EPA terms | https://www.epa.gov/web-policies-and-procedures/epa-disclaimers | General terms permit noncommercial scientific and educational use, subject to document-specific exceptions | 2026-11-05; not represented as an unrestricted dataset licence |
| Minnesota DNR, Winterkill and Other Fish Kills | https://www.dnr.state.mn.us/areas/fisheries/waterville/winterkill.html | Reference only; no reusable licence established or material reproduced | 2026-11-05; independent winterkill mechanism check |
| OpenStax Biology 2e, 45.6 and 46.1–46.3 | https://openstax.org/books/biology-2e/pages/46-2-energy-flow-through-ecosystems | Current page states **CC BY-NC-SA**, rather than the old spec's CC BY 4.0; reference only, no text, figures or datasets reproduced | 2026-11-05; food webs and energy mechanisms checked |
| Holling 1959; Gillooly et al. 2001; Lindeman 1942; Endler 1980; Carpenter, Kitchell and Hodgson 1985 | Bibliographic provenance supplied in the original spec | Citations only; no paper text, figures or data bundled | Historical numerical claims were replaced by this build's computed results |
| Artwork | OpenAI gpt-image, this build | Original generated illustrations, edited for Curio Class | One packed 36-cell atlas; no third-party photographs |

Decay and oxygen mechanisms were cross-checked across USGS, EPA and DNR. The old DNR `/fish/winterkill.html` route was unavailable; the named agency's current winterkill page was used. No restricted source text or external numerical dataset was packed. Gathering consisted of bounded source checks; there were no bulk downloads. Source records are in `_scratch/living-pond/source-checks.json`; the historical spec, model implementation and reproducible assembly scripts are preserved there too.

The Manual labels every percentage and population finding as a result of this model. It does not repeat the old 477–509 algae, 95 percent muck, or 1.2 percent capture claims as if independently reproduced. The scalar coefficients, fixed adults, accelerated inheritance and one water-and-air pool are disclosed.

## Break the instrument

`verify-model.js` exercised Starter, Empty, all stocking limits, heavy feeding, removals, all new shade/climate extremes, and ten winters per case. Every checked weekly state remained finite and nonnegative. Maximum ledger residual across stress runs was **5.83 × 10^-11 units**. `verify_numbers.py` independently checked the ledger, intervention thresholds, energy ratios and ice calendar.

- Starter, 520 weeks: all six resident kinds persist; total 742.0000000000006. Year-10 snails: **21.00–35.91**; minnows: **12.20–44.89**. This does not exactly reproduce the old snail range.
- Minnows netted at week 13: floating algae peak **439.96**, snails fall below half their ghost after **17 weeks**, heron leaves at week 15 and turtle at week 25.
- Decomposers off from the start: muck holds **92.07 percent** after year 1; turtle leaves at week 33 before a resident kind is lost. On again at week 52: algae exceed 100 after **11 weeks**. Waiting until all algae are extinct requires restocking.
- Lots feeding: winterkill conditions at week **100**, year 2 week 48. Some feeding retains minnows through ten winters, despite later winterkill conditions.
- Sand: average shade **2.2674** by year 3 and **1.2163** by year 10. Gravel stays **3.5000**. Mud reaches **5.7837**.
- Nymphs netted at week 13: next-104-week snail peak **73.43**, against **32.79** unchanged.
- Year-10 caught sunlight: **1.028 percent**; plant eaters retain **9.649 percent** of algae's retained energy; heat out is **99.901 percent** of caught. The current-year ledger resets at the calendar boundary.

New-control runs, from Starter with the other defaults unchanged:

| Setting | Year-10 snail range | End average shade | Matter at 520 weeks | Resident outcome |
|---|---:|---:|---:|---|
| Canopy 25% | 18.75–45.10 | 1.6580 | 742.0 | All six persist |
| Canopy 50% | 7.84–23.50 | 1.8641 | 742.0 | Nymphs lost in year 3, at logged week 129 |
| Cold, −2 °C | 19.36–30.51 | 1.5314 | 742.0 | Nymphs lost in year 3, at logged week 147 |
| Mild, +2 °C | 15.37–33.88 | 1.1625 | 742.0 | All six persist; no ice |

Browser checks confirmed same-frame minnow addition, a 105-point ghost, a followed muck dot reaching snails and minnows, exact Open/Replay reconstruction, matching action marks, a fresh-page saved-pond load at week 17, the eight-save limit, Rename focus, confirmed Delete focus, and play with blocked storage. Real held inputs and whole-pixel jittered net drags were exercised. Resize checks had no exceptions. Drawer closure restores interaction with the tank.

A final boundary check confirmed that a followed minnow sample is marked “Taken out of pond” when netted, and a fixed turtle sample is marked “Walked out with turtle” when it leaves. Neither leaves a misleading ring floating in the water. The ledgers remain exact in both cases.

The maximum-population Matter frame measured **60.003 fps** over the final 120 frame intervals in desktop headless Chrome, with the model held at the add limits. This is a drawing test, not a school Chromebook hardware measurement. Ordinary live runs were about 58–60 fps. First ghost calculation measured about **15–18 ms**; warmed calculations were about **4–9 ms**, so the requested under-5-ms guarantee is not met.

## Voice walk

Selected bank: `gravel-ranger`, Algenib. No recording was made or bundled; the kit uses browser speech. This limitation is stated in the Manual.

The Curiosity brief's speech rule takes precedence over the spec's event narration: the first appropriate touch speaks **“Tap a creature to drop it in.”** once; later speech comes only from Read. Ecological events keep quiet sound cues and dated log entries. Read speaks the current calendar, oxygen, temperature, counts and latest log entry, including with Sound off.

Held Add, Food and Read at two-second spacing produced one hint and one Read entry in the kit log. Repeated-click and rapid-click audit checks were clean. No score, welcome lecture or automatic ecological speech was added. The final small copy fix makes singular turtle and heron counts grammatical.

## Short test

Two independent real-time walks lasted **600.235 s** and **600.266 s**. The student path added fish and food, netted minnows, changed lenses, opened the Manual and saved. The adult path compared lenses, removed nymphs, used whole-run history, saved and used Read. Both reached about 1,204 simulated weeks. Both recorded **zero console exceptions and zero HTTP/HTTPS requests**. These were automated exploratory walks and my inspection, not tests with actual children.

- **Would a kid open it unassigned? YES, my judgment.** It starts alive, reacts immediately to stocking and feeding, and turns its first winter without a reading gate.
- **Would an adult play for fun? YES, my judgment.** Delayed cascades, shade selection, the unchanged ghost and saved histories leave room for experiments.
- **Is the real thing the interface? YES within the disclosed model.** Populations, oxygen, matter transfers and energy drive the visible tank and recorder. It does not claim to be measured field data.
- **Does it work without a score or finish? YES.** Neither walk needed one; the pond kept evolving after species disappeared.

Frame comparison, inspected beside the owner's studio reference:

![Living Pond beside Beat Lab](../../_scratch/living-pond/review-frames/comparison.png)

The shared confidence is a dense working surface and direct controls; this tool uses pond glass, field-station metal and chart paper, not Beat Lab's palette or layout.

## Lesson creep check

The final `src.html` and voice lines contain no score, points, level, goal, sticker, badge, correct, wrong, try again, complete or well done. An innocuous “complete account” in an honesty note was changed to “full account.” No em dash occurs in the source. There is no Journal, quiz, finish screen, mode-pill header or toast system. Status text stays on the instrument rather than appearing as a timed award.

## Done when

| Spec item | Result | Evidence |
|---|---|---|
| 1. Running, immediate add, ice inside a minute | PASS | Same-frame count increase; normal ice begins at week 41, about 20.5 s |
| 2. Ten winters, 742.0, old snail range | FAIL | Six residents and matter pass; measured snails 21.00–35.91 differ from 19–34 |
| 3. Minnow removal cascade | PASS | Af 439.96; half-ghost snails at 17 weeks; heron and turtle leave |
| 4. Decomposers off and recovery | PASS | 92.07% muck, turtle first; early reactivation recovers algae above 100 |
| 5. Feeding and bottom | PASS | Year-2 winterkill with Lots; Some survives; sand drifts over one shade by year 3; gravel holds |
| 6. Tracer and energy | PASS | Browser trip reaches animals; full-year heat/caught 99.901% |
| 7. Canopy and Year | PASS | Live controls, conservative matter, ten-winter outcomes above and in Manual |
| 8. Largest tank and visible main controls | PASS | All required sizes inspected; 375 tray scrolls as specified; short landscape Habitat drawer preserves tank space |
| 9. Save, reload, Open, Replay, blocked storage | PASS | Equality checks, fresh load, matching marks, limit and storage-failure tests |
| 10. Caps, 60 fps on Chromebook, keyboard | FAIL | Caps, multiplier keys, keyboard and desktop 60 fps pass; Chromebook hardware not available to verify |
| 11. No achievement or lesson layer | PASS | Source/voice scan and interface inspection |
| 12. Short test, comparison, clean console, offline, punctuation | PASS | Both ten-minute walks, comparison frame, final clean drives and static scan |

## Audit leads

One full mechanical audit ran on **9981**, host **8785**, finishing with **242 leads** across repeated sizes and states. It was not rerun. Targeted post-fix checks are preserved separately.

- **Tank/overlay overlaps:** the keyboard-focusable canvas deliberately lies beneath its rim controls, calendar and readout overlays. These are siblings on one instrument, not intersecting control labels. The transparent hit-test of the Matter ledger is also reported as “covered” because it deliberately passes pointer events through.
- **Actual compact footer/light overlap:** fixed by assigning the footer its explicit fifth grid row. Final 680×425 and 800×500 frames show the meter and footer separately.
- **Phone shade text:** fixed with separate lines; final phone frame has no intersecting shade labels.
- **Manual links below 44 px:** fixed to measured **45.44 px** height. The long Manual body intentionally scrolls; its findings and references are not a short choice panel.
- **Tray overflow / moved controls:** the spec explicitly requests a scrolling phone tray, and Net adds removal controls. The focused Net control is now scrolled into view after the tray changes. Escape also puts the net down.
- **Hidden optional hint / zero-font label wrappers:** compact layouts omit the quiet hint and visual TIME/LENS wrapper words. Their native selectors have readable value text and explicit accessible names. The first-touch hint and Read remain available.
- **Drawer covers main controls / “left disabled” after resize:** intentional while a drawer is open. The main instrument is inert, focus stays in the drawer, and Close restores it; the final save-control test verifies both states. The pond model keeps running.
- **Welcome-premise leads:** a lesson-audit expectation. This Curiosity has zero lesson modes and only the brief's first-touch hint. Own held-input logs confirm the hint once and Read on demand.
- **Errors and stale controls:** final drives and both long walks have no console errors. The first build's global `location` function collision and sound argument warning were fixed before final checks. Intermediate driver connections had a cleanup interruption and a connection reset; isolated-port retries passed.

Independent contrast ratios: ink/paper **13.28:1**, muted/paper **6.33:1**, white/teal **6.31:1**, plate **6.34:1**; solid chart keys/lines **4.71–6.11:1**. Lines also have distinct dashes and labels. Grayscale and Motion off frames were inspected.

## Frames looked at

All **85** frames indexed in `_scratch/living-pond/frames-index.json` were inspected through eight labelled contact pages, with critical frames also opened at full size. This includes the four required reference instruments, early failed frames, corrected wide/preview/phone frames, functional and voice paths, Matter, Energy, Net, grayscale, Manual, saves, winter, both long walks, and all 39 audit frames.

Also inspected: the comparison, final flow frame, final maximum-population frame, expanded ten-findings Manual frame, tracer-exit frame, generated raw atlas and keyed atlas. The early blank and overflowing frames are retained as failure evidence, not presented as final work. Final views are under `targeted-frames/`, `closeout-frames/`, `last-frames/`, `tracer-exit-retry/` and `review-frames/` in Scratch.

## Art made

Generated a naturalistic gouache atlas with all **36** requested shore, bottom, ice, plant, creature, pose and prop subjects. No people, lettering or logos. The raw PNG, prompt and packed WebP are preserved. Bounded browser canvas packing removed the magenta key and spill without changing the drawn subjects; the normal `art.py --rekey` attempt failed because NumPy was absent.

The working water, tint, ice line, muck thickness, specimen positions, chart, needle, dots, tracking marks, energy widths and text are drawn in code. Dot samples and glyph multipliers are labelled; exact totals remain in the model. Shore plants and adult dragonflies are disclosed as scenery outside the matter ledger.

## Engine changes wanted

See `handoff.md`: provide a supported Python environment for `scripts/art.py` rekeying, and extend `scripts/drive.py`'s fixed key map to letter/digit shortcuts. This build used its own bounded Scratch packing and CDP walk harnesses; no shared engine was changed.

## Left open

- Historical numerical calibration is not fully reproduced. The source supplies formulas and claimed runs but no executable reference. Simultaneous conservative substeps are retained rather than tuning coefficients to force old outputs. The different snail range, oxygen/energy totals and decomposer recovery timing are reported explicitly.
- Ghost calculation does not reliably meet the under-5-ms requirement. It is finite and responsive but its first calculation can take 15–18 ms.
- Actual school Chromebook hardware performance remains unverified, despite a 60.0 fps desktop cap test.
- The gravel-ranger recording is absent; browser speech is the fallback. Pose and seasonal changes are immediate rather than a full crossfade/death-sinking animation system. Canopy and Year use native detented selectors rather than rotary knobs.
- Unattended choices: retained Canopy and Year; kept winterkill plain; used four shore variants in the atlas; kept all old achievement features out; used device-only saves; left any site card retirement or catalogue change to the owner because writes were restricted to this tool and Scratch.
- No new `plan.md` or site mapping was written; the tool is a Curiosity and this was Build only.

All owned Chrome ports **9980–9987** and host **8785** were closed at verification. No `host.html` was left in the tool folder. The report is the final build artifact; work stops here.
