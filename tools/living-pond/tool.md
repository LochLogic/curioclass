# Living Pond: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: living-pond (Curiosity No. 13)

#### Built

An ecologist's study tank, with a living cut-away pond, specimen tray, strip-chart recorder, oxygen needle, thermometer, light readout, inherited shade strip, and Matter and Energy lenses. It opens running at two weeks per second. The engraved plate and Manual sit lower-left; Motion, Sound and Read have their own power panel.

Stocking, netting, feeding, bottom, decomposers, canopy and climate change the running model immediately. Ghost traces project an unchanged copy for 104 weeks. Eight device-local saved ponds support Open, Replay, Rename and confirmed Delete. Keyboard shortcuts and ordinary keyboard controls work. The Manual contains ten findings, the web, model explanation, dated pond log, sources and honesty notes.

Final offline bundle: **501,506 bytes**, about **0.50 MB**, 25 percent of the 2 MB goal. It contains its artwork and kit code. No runtime network request was observed. No commit, deployment or polish round was made. Authored files stayed in `tools/living-pond/` and `_scratch/living-pond/`. The existing `spec.md` modification was not edited by this build.

SHA-256: `dcf1b34276f813a245defd1b211b5ba1be2807e7d1eac952c2fafbf2edf44e54`.

#### The real material

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

#### Break the instrument

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

#### Voice walk

Selected bank: `gravel-ranger`, Algenib. No recording was made or bundled; the kit uses browser speech. This limitation is stated in the Manual.

The Curiosity brief's speech rule takes precedence over the spec's event narration: the first appropriate touch speaks **“Tap a creature to drop it in.”** once; later speech comes only from Read. Ecological events keep quiet sound cues and dated log entries. Read speaks the current calendar, oxygen, temperature, counts and latest log entry, including with Sound off.

Held Add, Food and Read at two-second spacing produced one hint and one Read entry in the kit log. Repeated-click and rapid-click audit checks were clean. No score, welcome lecture or automatic ecological speech was added. The final small copy fix makes singular turtle and heron counts grammatical.

#### Short test

Two independent real-time walks lasted **600.235 s** and **600.266 s**. The student path added fish and food, netted minnows, changed lenses, opened the Manual and saved. The adult path compared lenses, removed nymphs, used whole-run history, saved and used Read. Both reached about 1,204 simulated weeks. Both recorded **zero console exceptions and zero HTTP/HTTPS requests**. These were automated exploratory walks and my inspection, not tests with actual children.

- **Would a kid open it unassigned? YES, my judgment.** It starts alive, reacts immediately to stocking and feeding, and turns its first winter without a reading gate.
- **Would an adult play for fun? YES, my judgment.** Delayed cascades, shade selection, the unchanged ghost and saved histories leave room for experiments.
- **Is the real thing the interface? YES within the disclosed model.** Populations, oxygen, matter transfers and energy drive the visible tank and recorder. It does not claim to be measured field data.
- **Does it work without a score or finish? YES.** Neither walk needed one; the pond kept evolving after species disappeared.

Frame comparison, inspected beside the owner's studio reference:

![Living Pond beside Beat Lab](../../_scratch/living-pond/review-frames/comparison.png)

The shared confidence is a dense working surface and direct controls; this tool uses pond glass, field-station metal and chart paper, not Beat Lab's palette or layout.

#### Lesson creep check

The final `src.html` and voice lines contain no score, points, level, goal, sticker, badge, correct, wrong, try again, complete or well done. An innocuous “complete account” in an honesty note was changed to “full account.” No em dash occurs in the source. There is no Journal, quiz, finish screen, mode-pill header or toast system. Status text stays on the instrument rather than appearing as a timed award.

#### Done when

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

#### Audit leads

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

#### Frames looked at

All **85** frames indexed in `_scratch/living-pond/frames-index.json` were inspected through eight labelled contact pages, with critical frames also opened at full size. This includes the four required reference instruments, early failed frames, corrected wide/preview/phone frames, functional and voice paths, Matter, Energy, Net, grayscale, Manual, saves, winter, both long walks, and all 39 audit frames.

Also inspected: the comparison, final flow frame, final maximum-population frame, expanded ten-findings Manual frame, tracer-exit frame, generated raw atlas and keyed atlas. The early blank and overflowing frames are retained as failure evidence, not presented as final work. Final views are under `targeted-frames/`, `closeout-frames/`, `last-frames/`, `tracer-exit-retry/` and `review-frames/` in Scratch.

#### Art made

Generated a naturalistic gouache atlas with all **36** requested shore, bottom, ice, plant, creature, pose and prop subjects. No people, lettering or logos. The raw PNG, prompt and packed WebP are preserved. Bounded browser canvas packing removed the magenta key and spill without changing the drawn subjects; the normal `art.py --rekey` attempt failed because NumPy was absent.

The working water, tint, ice line, muck thickness, specimen positions, chart, needle, dots, tracking marks, energy widths and text are drawn in code. Dot samples and glyph multipliers are labelled; exact totals remain in the model. Shore plants and adult dragonflies are disclosed as scenery outside the matter ledger.

#### Engine changes wanted

See `handoff.md`: provide a supported Python environment for `scripts/art.py` rekeying, and extend `scripts/drive.py`'s fixed key map to letter/digit shortcuts. This build used its own bounded Scratch packing and CDP walk harnesses; no shared engine was changed.

#### Left open

- Historical numerical calibration is not fully reproduced. The source supplies formulas and claimed runs but no executable reference. Simultaneous conservative substeps are retained rather than tuning coefficients to force old outputs. The different snail range, oxygen/energy totals and decomposer recovery timing are reported explicitly.
- Ghost calculation does not reliably meet the under-5-ms requirement. It is finite and responsive but its first calculation can take 15–18 ms.
- Actual school Chromebook hardware performance remains unverified, despite a 60.0 fps desktop cap test.
- The gravel-ranger recording is absent; browser speech is the fallback. Pose and seasonal changes are immediate rather than a full crossfade/death-sinking animation system. Canopy and Year use native detented selectors rather than rotary knobs.
- Unattended choices: retained Canopy and Year; kept winterkill plain; used four shore variants in the atlas; kept all old achievement features out; used device-only saves; left any site card retirement or catalogue change to the owner because writes were restricted to this tool and Scratch.
- No new `plan.md` or site mapping was written; the tool is a Curiosity and this was Build only.

All owned Chrome ports **9980–9987** and host **8785** were closed at verification. No `host.html` was left in the tool folder. The report is the final build artifact; work stops here.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: living-pond

#### Played

Cold play preceded the builder's report, handoff, notes and source: desktop and 680 preview, adding, feeding, netting, all three lenses, Manual and saves. Anchor grade 5, then adult experimenter. Separate 600.141 s and 600.125 s walks recorded no console exceptions or HTTP/HTTPS requests. These are my automated exploratory walks and judgment, not research with children.
The tank is immediately inviting; the delayed collapse against its ghost is the strongest interaction. Work stayed in `S:\CurioClass-codex`, with authored writes only in this tool and its Scratch. No commits or shared-engine edits. Existing `spec.md` changes were left untouched.

#### Findings fixed

- **Blocker, real material:** food arrows pointed to generic positions and omitted links. Arrows now follow actual organism hitboxes, name their endpoints, distinguish absent kinds, include water/air recycling and the nymph-to-turtle link, and avoid implying that the visitor heron's body belongs to the matter pool. Algae and decomposer samples can be inspected too.
- **Should fix, access:** Life inspection lacked a keyboard equivalent; Enter now inspects the creature nearest the arrow-key pointer. Shortcuts no longer change the inert pond behind the Manual or saved-pond drawer. Native confirmation keeps its own keyboard handling.
- **Should fix, energy:** a negative grazer value looked like negative energy transfer. The ledger now says net production, labels negative values STORES USED, and suppresses the misleading negative percentage. Manual explains respiration, stored energy, and the energy imported by food/stocking.
- **Should fix, saving:** Open applied actions at the saved week after the chart snapshot. It now reconstructs that endpoint too; Open/Replay pools, week and marks match. New/Open clear transient selections, effects and fractional time accumulation.
- **Should fix, voice:** Read could announce spring and then quote an undated old ice event. Latest records now include their year and week.
- **Should fix, sources:** removed the stale CC BY 4.0 / blanket public-domain comment, qualified EPA reuse terms, named wildlife references and their rights, and made the model-only food web and warning thresholds explicit. No restricted source material was imported.
- **Polish, graphics and drama:** removed atlas padding at draw time, preserved creature proportions, kept snails on their stems/stones, uncovered the heron, and replaced repeated shore vignettes with a generated four-season panorama. The heron now visibly flies away when the model sends it off; Motion off skips that movement.
- **Should fix, audit-confirmed tray:** Net mode hid early removal controls at compact landscape widths. The tested 680, 760, 800 and 1000 layouts now keep every net-one/all control in the same row with its icon and at least a 44 px target. Phone scrolling remains as specified.
- **Should fix, contrast:** the ghost traces measured as low as 1.60:1 over the season bands. Kept their pale long-dashed style and raised their minimum calculated contrast to 3.30:1; hidden-trace labels retain full text contrast rather than being faded. Inspected the changed charts at 1366, 680 and 375.
- **Should fix, truthful control:** the decomposer button claimed Net 1 even though the model forbids netting specks. It now says Specks, announces the limitation and habitat switch, keeps readable text, and retains the worm icon. The offline file also carries the MIT notice and a CC BY 4.0 licence link.

#### Findings left

No known blocker or should-fix remains after the scoped corrections and rechecks. The following spec/evidence qualifications remain explicit.

- **Spec discrepancy:** own rerun gives year-10 snails 21.00–35.91, against the historical approximate 19–34. All six resident kinds persist and total matter is 742.0. Kept the specified coefficients and conservative rule rather than tuning to an unavailable historical executable; actual findings are disclosed.
- **Polish / evidence limits:** first ghost calculation measured 18.7 ms, with warm examples 4.5–6 ms, above the requested reliable 5 ms. No freeze was observed. Desktop timings do not establish 60 fps on a school Chromebook. The named ranger recording is absent; browser speech is the disclosed fallback.

#### Break it

No score, quiz, goal, finish gate or reward meter exists. Oxygen, biomass and energy are instrument measurements.

- Independently reran Starter, Empty, Some/Lots, all bottom, canopy and year extremes; 1,040-week heavy stocking/feeding stress stayed finite and nonnegative. Largest conservation residual was 6.55e-10 model units.
- At week 13, removing minnows raised floating algae to 439.96 and put snails below half their ghost in 17 weeks; heron and turtle left. Decomposers off put 92.07% of matter in muck after one year; restoring them then brought algae above 100 in 11 weeks.
- Lots gave winterkill conditions in year 2; Some retained minnows over ten winters. Sand shifted shade past one unit by year 3; gravel held 3.50. Year-10 heat/caught was 99.90%; algae caught 1.028% of sunlight and grazer net/algae net was 9.649%.
- 125 rapid held stocking taps reached 120 minnows; repeated shaker taps stopped at 30 food units that week. A real whole-pixel, jittered net swipe removed exactly six specimens. No exceptions. Drawn caps retain explicit multipliers.
- Open and Replay reproduced the saved week-17 pools and three action marks, including an addition at that exact week; the final chart count equalled the actual count. Blocked storage showed its failure and play continued. Empty pond remained finite for 104 weeks. Rename persisted; Cancel preserved a save; confirmed Delete returned focus to Close; the ninth save was refused. New/Cancel preserved pools, and New offered working Save, Starter and Empty choices. The test restored the original review-profile save fixtures.
- Adult walk exercised both ends of speed, feeder, bottom, decomposers, canopy and year; live resize checks preserved the running state. All lens and chart controls, Motion/Sound and Read were exercised. Calm tank pixels were identical between samples; grayscale retained dash/label distinctions.

Evidence: `review-save-controls.json`, `review-fresh-open.json`, `review-numbers.json`, `review-regressions.json`, `review-rapid.json`, `review-swipe.json`, `review-calm.json` and `review-live-*/results.json` in Scratch.

#### Voice walk

Held Add Minnow → Food → Read → Sound off → Read → Sound on, two-second gaps: one first-touch hint, two requested live reads, no automatic ecological narration. Read worked with Sound off. Both longer paths likewise spoke the hint only once. This follows the Curiosity brief's first hint / Read rule, which overrides the older event-narration list.

| Line | Kind | Expected | Logged |
|---|---|---:|---:|
| Tap a creature to drop it in. | first hint | 1 | 1 |
| Current calendar, oxygen, temperature and counts | Read | 2 | 2 |
| Dated latest record at a spring boundary | Read | 1 | 1 |

Browser speech was tested through the kit's start log in muted Chrome, not by claiming a bundled ranger performance. Voice evidence: `review-main-voice.json` and `review-dated-boundary.json`.

#### Facts checked

No measured ecological dataset is bundled or sampled. Numerical values are owner-supplied model parameters and this review's computed model outcomes, not field measurements. Sources and reuse terms are also in the Manual and `tool.draft.json`; source checks were made 2026-11-05.

| Fact / material | Named check and rights |
|---|---|
| Every starting pool, rate, refuge, shade inheritance and environmental formula | `018ace9b:tools/living-pond/spec.md`, owner-supplied illustrative model; documentation/content CC BY 4.0 under root LICENSE-CONTENT.md, code MIT under LICENSE (both read). Fresh conservation and scenario runs in `review-numbers.cjs`; total starts at 742, Empty at 470. |
| Matter cycling, food webs, chemical energy and respiration | [OpenStax Biology 2e 46.1–46.3](https://openstax.org/books/biology-2e/pages/46-2-energy-flow-through-ecosystems), current CC BY-NC-SA, reference only. Independently checked decay/oxygen and plant production against USGS and EPA below; no book text, images or data copied. Model energy percentages are calculations, not ecological constants. |
| Colder water holds more oxygen; decay consumes oxygen | [USGS Water Science School](https://www.usgs.gov/water-science-school/science/dissolved-oxygen-and-water), USGS-authored information US public domain; [USGS rights policy](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits). [California Water Boards table](https://www.waterboards.ca.gov/water_issues/programs/swamp/docs/cwt/guidance/3110en.pdf), reference only, independently gives 9.1 mg/L at sea level and 20 °C. The model fit gives 9.6, about 0.5 above that reference; disclosed, not presented as measured solubility. |
| Blooms can shade vegetation and lead to oxygen loss | [EPA, Effects on the Environment](https://www.epa.gov/nutrientpollution/effects-environment), with [document-specific reuse caveats](https://www.epa.gov/web-policies-and-procedures/epa-disclaimers). Reference only; no copied material. Independent mechanism check: USGS and Minnesota DNR. |
| Ice/light restriction and decay can cause winterkill | [Minnesota DNR](https://www.dnr.state.mn.us/areas/fisheries/waterville/winterkill.html), copyright DNR, reference only; independently [Connecticut DEEP Winter Fish Kills](https://portal.ct.gov/-/media/DEEP/fishing/general_information/WinterFishKillFactSheetpdf.pdf), reference only. The 3/2 mg/L thresholds are this model's choices, not universal tolerances. |
| Herons take fish in shallow water | [Cornell Lab](https://www.allaboutbirds.org/guide/great_blue_heron/lifehistory) and [Audubon](https://www.audubon.org/field-guide/bird/great-blue-heron), copyrighted references only. Their broader diets are not claimed to be simulated. |
| Painted turtles bask, eat varied food and overwinter in bottom mud | [Connecticut DEEP](https://portal.ct.gov/deep/wildlife/fact-sheets/painted-turtle) and [Missouri MDC](https://mdc.mo.gov/discover-nature/field-guide/western-painted-turtle), references only, no open reuse licence asserted or content copied. The 10 °C switch is a model parameter. |
| Aquatic nymph anatomy, hinged lip and small-animal prey | [British Dragonfly Society](https://british-dragonflies.org.uk/odonata/life-cycle-and-biology/), copyright BDS, and [Missouri MDC](https://mdc.mo.gov/discover-nature/field-guide/dragonfly-larvae), reference only. Six legs and lip match the atlas; BDS independently confirms snail and small-fish prey. |
| Historical papers | Holling 1959, Gillooly et al. 2001, Lindeman 1942, Endler 1980, Carpenter/Kitchell/Hodgson 1985 remain named provenance citations only. No paper data, prose or illustrations imported, and no fitted empirical coefficients claimed. |
| All painted art | Original OpenAI gpt-image illustrations edited for Curio Class, CC BY 4.0 under the repository content licence; no third-party wildlife images. The new built-in-imagegen prompt is saved in `art/prompts.json` and `review-shore-prompt.txt`; original in `art/raw/pond-shores-v2.png`, packed result `art/pond-shores-v2.webp`. Scenery is explicitly outside the matter pools. |

#### Short test

- Kid opening it unassigned: **YES, my judgment.** It starts alive and the first stocking/feeding action pays off without reading.
- Adult playing for fun: **YES, my judgment.** Counterfactual traces, delayed winter effects, inherited shade and replayed experiments support sustained investigation.
- Real thing as interface: **YES within the disclosed simulation.** Populations, matter transfers, oxygen and energy drive the tank and recorder. Connected food arrows and legible specimens make those relationships more central.
- No score or finish: **YES.** Extinction leaves a changing pond that can be restocked; no invented game layer was added.

![Living Pond beside Beat Lab, both reviewed](../../_scratch/living-pond/review-voice/comparison.png)
The studio reference has denser controls; the pond appropriately gives most of its area to moving organisms and water. Both expose the working material directly.

| Spec done-when | Result | Review evidence |
|---|---|---|
| 1. Running, immediate add, first ice | PASS | Held stocking responds; ice at week 41, about 20.5 seconds at Normal. |
| 2. Ten winters, matter, historical snail band | PARTIAL | Six resident kinds and 742 pass; measured 21.00–35.91 differs from the old approximate band. |
| 3. Minnow-removal cascade | PASS | 439.96 floating algae, half-ghost snails in 17 weeks, visitors leave. |
| 4. Decomposers off and recovery | PASS | 92.07% in muck, turtle leaves before resident extinction; early recovery in 11 weeks. |
| 5. Feeding and bottom | PASS | Year-2 Lots winterkill, Some survives, sand shifts, gravel stays 3.50. |
| 6. Tracer and full-year energy | PASS | Followed dot reached minnows; full-year heat/caught 99.90%. |
| 7. Canopy and year | PASS | Own 25/50%, Cold/Mild runs conserve matter; 50% and Cold lose nymphs, Mild has no ice. |
| 8. Tank and accessible main controls | PASS | Defaults at all eight sizes; compact Net correction re-shot at affected widths. |
| 9. Device saves and reconstruction | PASS | Exact Open/Replay and blocked storage checks; fresh-page check recorded separately. |
| 10. Caps, keyboard and Chromebook speed | PARTIAL | Capped real input and keyboard pass; no Chromebook hardware benchmark available. |
| 11. No game/lesson layer | PASS | Source/voice scan and visual review. |
| 12. Short test, comparison, offline and errors | PASS | Four judgments above, comparison, clean exploratory walks and scoped checks. |

#### Sensitivity

None requiring a cultural reviewer: no cultures, hard history, religion, human bodies or people images. Wildlife predation and winterkill remain plain ecological events, as the spec leans; no gore, moral blame or rewards.

#### Flattest moment left

A pond after every animal is lost has less visible motion. Its algae, oxygen and matter still run, and the tray can restock it. The cold build's abrupt disappearance/anonymous arrows were lifted with a visible departure and organism-connected web, without adding targets.

#### Graphics

Final desktop, 680 preview, 375 iframe, all lenses, net, caps, grayscale, calm, Manual and saves were inspected. A new four-season panoramic shore replaces conspicuous repetition; the existing 36-cell field-guide atlas stays. Native draw-time alpha trimming does not change the organisms' anatomy.
The normal `art.py --rekey` command failed because NumPy is absent. One bounded browser WebP-encoding retry succeeded after a file-origin canvas restriction. No software was installed; no shared script changed. Bundle size and audit frames: 745,839 bytes (728.4 KiB). The original 99 review frames were viewed through eleven labelled contact sheets, with critical states opened full size. Save/control-label/licence closeout frames were opened separately; all are indexed in review-frame-index.json. Early failed packing/host frames are retained as evidence, not described as final passes.

#### Audit

Completed exactly once, on the frozen pre-correction bundle, on Chrome 9951 and host 8755 with a 40-minute cap: **203 leads**, 42 frames, clean console/error rows, no stuck controls after resize, no infinite calm animation, and clean repeat/quick-tap voice checks.
Confirmed the compact Net overflow and corrected it; all 15 targets subsequently measured at least 44 px with zero overflow at 680, 760, 800 and 1000. Visual audit-frame review also corrected the compact muck anchor/leader line. Updated source drawers and fresh-page Open were rechecked; contrast changes were re-shot at 1366, 680 and 375. No second audit or full review was run.
Other leads were adjudicated on frames: the focusable pond canvas intentionally underlies its calendar, power and rim controls; the ledger passes pointer events through, so hit-testing falsely calls it covered; a first-run hint intentionally vanishes; phone TIME/LENS wrappers are zero-font but their native values/names remain readable; the phone tray intentionally scrolls; an open modal drawer makes the main tank inert; the hint is the required short first touch, not a lesson welcome. No kit header or extra instruction layer was added to satisfy those lesson-shaped leads.
Bundle SHA-256: `3c773bc4f9b317ce0eaafa64eea3683c5099ab46d8eb81d49aa33616b040d4d9`. Final manifest: `_scratch/living-pond/review-final-manifest.json`.

#### Left open

Historical calibration band, reliable 5 ms ghost budget, actual Chromebook benchmark and the absent ranger recording, as above. No deployment, site card retirement or new lesson plan was attempted. Unattended choices follow the brief: retain Canopy and Year, plain winterkill, original coefficients and device-only saves; no score, goal, quiz, kit header or finish screen. The only final lesson-creep word hits are two uses of level in the sea-level oxygen reference, a physical condition, not game progression; voice has none. Source has no em dashes. Owned Chrome/server cleanup: verified closed on 9950, 9951, 9953, 9954 and 8755..

Process note: the initial short document/metadata reads used tool-yield limits; explicit subprocess deadlines were added before play and used thereafter. Limits: 120 s bundles, 300 s drive batches, 2,400 s audit, 760 s for each real-time ten-minute walk. Scratch HTTP teardown logged connection resets after Chrome closed; instrument console checks were clean.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 0 (general 0, family 0), should fix 16 (general 7, family 9), polish accepted 22

### Refine: living-pond

Merged from refine/teaching.md, refine/play.md and refine/craft.md (round 1). Frame folders, all under
`S:/CurioClass-codex-scratch/living-pond/`: Teaching `teaching/frames/`, Play `play/shots/`, Craft `craft/`
(run1 to run4, z-*.png crops), shared audit `audit-r1/`. The short test passes in all three lenses; no score, goal,
level, sticker or finish screen was found. Integrator spot-checked items 1, 4, 5, 7 and 10 in src.html (cited lines
confirmed).

#### Blocker
None.

#### Should fix
1. **The pond's drama is silent: none of the spec's event lines exist.** src.html:622 (`L` holds only `hint`),
   voice/lines.json (one line), events written only by `logEvent` (src.html:375-524) into the Manual's pond log.
   Craft ran 136 weeks with the feeder on Lots: two freezes, a winterkill and "Heron flew off" were logged and the voice
   said only the hint (craft/run1/voice-events); Play saw the same at year 2 week 50, 0.6 mg/L (play/shots/feeder-lots.png).
   Fixed: add the spec's event lines as `V.say` events ("Ice. No new air gets in until spring.", "Oxygen's low. The
   minnows are gasping at the top.", a winterkill line, heron left, turtle left, "The snails are gone."), each at most
   once in 20 s, maxAge 4 s, with a `valid` that the event is still true; add them to voice/lines.json word for word.
   Plain statements of what happened, never praise. (family:curiosity)
2. **Seven controls are browser dropdowns, not instrument controls.** src.html:228, 230, 240-244 (Speed, Lens, Feeder,
   Bottom, Decomposers, Canopy, Year are native `<select>`). The bottom third reads as a settings form
   (audit-r1/size-1366x768.png, play/shots/*). CODEX-CURIOSITY "Real controls" and the spec ("Canopy dial", "Year
   dial", Decomposers `On` / `Off`) ask for dials and switches. Fixed: detented rotary switches with the value printed
   on them for speed, lens, feeder, bottom, canopy and year, a lever toggle for decomposers; arrow keys step each, each
   announces its value, a soft click on Sound; same values and keys (< >, L) as now. (family:curiosity)
3. **The Algae trace hides the cascade.** src.html:539 (`A:(s.p[1]+s.p[2])/5`), counts() at :762. Floating and stem
   algae are summed, so "net the minnows" reads as "algae up, snails down" with the cause invisible: stem algae fall
   from about 46 to 3.3 while the line climbs (teaching/frames/t-netminnows.png; Node: Af 245 to 440, As 45.7 to 3.3,
   snails 31.5 to 0). Fixed: show the two apart, either two algae traces (floating, on stems) with their own chips and
   end labels, or at least the stem share on the tray and in the counts. (family:curiosity)
4. **Snail and turtle food arrows start at the wrong algae.** src.html:1239-1248 (only floating clumps get hitboxes;
   the stem sprites at :1248 get none) and drawWeb (:1443-1492). The arrows run from a floating clump at the surface
   while the model and the Manual say snails and the turtle eat algae on stems (teaching/frames/t-turtle-inspect.png).
   Fixed: give the stem algae hitboxes (kind "stem algae") and draw the snail and turtle arrows from them. (family:curiosity)
5. **No first-run hint on screen below 900 px.** src.html:142 (`#hint{display:none}` under max-width 900). At 680x425,
   800x500, 760x900 and 375x812 the student gets no instruction before acting, and voice speaks only after a touch
   (audit-r1/size-680x425.png, size-760x900.png, size-375x812 (iframe host).png; play/shots/narrow-680-winter.png).
   Fixed: the one-line hint on the tank rim at every size (a short form such as "Tap a creature below" where room is
   tight). (general)
6. **The spoken hint arrives after the action it describes.** src.html:662-667 (`afterTouch`). If the first touch was
   a tray tap, the student hears "Tap a creature to drop it in." 1.4 s after doing it (craft/run1/voice-adds; audit
   held-click rows 6 to 13). Fixed: skip the line when the first touch was itself an Add or Food tap (its `valid`
   checks that nothing has been dropped yet); otherwise it stays as the spec says, once after the first touch.
   (family:curiosity)
7. **"Whole run" turns invisible when on.** src.html:42 and 85: `button[aria-pressed=true]` sets white text, then
   `.chartbar button` (same specificity, later) sets a transparent background, so the pressed label is white on cream
   paper (craft/z-whole.png, play/shots/year10-whole.png). Fixed: a pressed style for chart-bar buttons with its own
   dark fill (`#0b4f56` with white) or an inked underline. (general)
8. **The oxygen meter has no marks at 3 and 2.** src.html:1597-1619. Ticks only at 0, 5, 10, 15, 20; "3 gasp / 2 kill"
   is a loose 10 px caption in the corner, dropped entirely when the meter is under 120 px (680x425 frames). Fixed:
   a shaded red band 0 to 3 on the arc with labelled ticks at 3 "fish gasp" and 2 "winterkill", as the spec's
   readouts say, kept at short sizes. (general)
9. **The Energy ledger zeroes the moment the year ends.** src.html:531-535 (yearly reset), sync() :816-822. At week 51
   heat out is 102 percent of caught; one week later every line reads 0 and "0.0% OF SUN" (play/shots/energy-yr1.png);
   mid-year it reads 88 percent (teaching/frames/t-energy-y10.png). Thing to do 4 is "a whole year". `s.lastEnergy` is
   kept but never shown. Fixed: a "last year" line (or column) beside this year's, shown once a year has closed. (general)
10. **Following a matter dot is a long flat wait, and the keyboard can only follow muck.** src.html:1765 (Enter in
    Matter always `follow(14)`), `follow`/`updateTracker` :1092-1110. Play followed a dot from each of 8 pools for 52
    weeks: only animal-start dots touched an animal; the muck dot stayed "Muck" 26 weeks (play/shots/matter-follow.png).
    Fixed: Enter follows the dot nearest the arrow-key drop point (as Life does with `inspectCreature`), and the trip box
    shows how many weeks the dot has been where it is. Do not change the model's flows (see Settled calls). (general)
11. **The Manual reads as a model specification, above grade 5.** Manual `#manualbody` (src.html:259-306) and the Energy
    ledger labels. "a counterfactual, not a prediction after further changes", "flow-weighted probabilities",
    "outgoing flows share a proportional limit", "Caught is gross algae growth x 10", ledger "STORES USED", "GRAZERS NET"
    (teaching/frames/t-manual-found.png, t-energy-y10.png). Fixed: each section opens with a plain grade 5 paragraph
    ("the dashed line is the pond you didn't change", "kept in algae after they breathe", "plant eaters"), model detail
    below it for adults; ledger labels in plain words. Exact terms stay in the honesty paragraph. (general)
12. **The feeding entry hides the winterkills.** Manual "Food can slow the shade drift" (src.html:303). "With Some
    feeding, the average was 2.10" is true, but that pond had winterkill conditions in 6 of 10 winters and holds 0.86
    minnows by year 10 (Node; teaching/frames/t-feeder-some-y9.png, Y9 W49, 1.5 mg/L). Fixed: name the winterkills in
    the entry, or report a feeding level that keeps the school; numbers from the build's own runs. (family:curiosity)
13. **"Things people have found" lost their real-world sources.** Manual src.html:292-306. The spec asks each find "in
    this pond, with real-world sources" (Carpenter, Kitchell and Hodgson 1985 cascade; Minnesota DNR winterkill;
    Lindeman 1942 and OpenStax 46.2 energy shares; Endler 1980 shade drift; Cornell Lab heron; USGS oxygen). Fixed: one
    plain sentence per entry, "Real lakes do this too (source).", keeping "this is a model result". (family:curiosity)
14. **5-LS1-1 is not visible: nothing says algae are built from air and water.** Manual "Model and honesty"
    (src.html:281) and the algae inspect label. The pool is "Water & air" and also holds nutrients; a trip like "Muck >
    Decomposers > Water & air > Floating algae" lets a student conclude algae are built from rotted muck
    (teaching/frames/t-matter-trip.png). Fixed: the Manual and the algae inspect label say algae build their bodies from
    carbon dioxide (air) and water using sunlight, and that the nutrients from muck are a small share lumped into this
    pool. (family:curiosity)
15. **The shade drift has no history (MS-LS4-6).** Shade strip src.html:243, sync :808. Only the current AVG SHADE is
    shown; the drift over ten winters can only be seen by writing numbers down (teaching/frames/t-shade-y10.png).
    Fixed: an optional AVG SHADE trace on the recorder, a chip like the population chips, off by default, own dash and
    end label. (family:curiosity)
16. **Status grammar.** src.html:716: "The pond is full of minnow." / heron / turtle / snail. Fixed: plurals ("The pond
    is full of minnows.") or "No room for more minnows." (general)

#### Polish accepted
1. **Latest event on the tank.** A one-line monospace readout on the tank rim showing the newest pond-log line (from
   `logEvent`), so a student with Sound off still sees "Ice. New air is sealed out." or "Heron flew off." The Manual's
   pond log stays the record. (play/shots/feeder-lots.png) (general)
2. **Energy diagram labels.** drawEnergy src.html:1432-1441: small labels on the sun arrows, heat columns and "kept"
   arrow (Sun, Algae, Snails, Minnows, Decomposers); attribute an eater's heat to the eater, and give decomposers'
   breakdown of muck its own heat column (teaching/frames/t-energy-y10.png). (family:curiosity)
3. **Matter trip names the decomposers.** updateTracker src.html:434-441, 1098-1110: write the Muck to Water & air step
   as "Muck > broken down by decomposers > Water & air". (family:curiosity)
4. **Ghost lines easier to tell from real lines.** src.html:611, 1538: ghosts much paler (about 0.35 alpha) or thin
   dotted grey (play/shots/net-all-minnows.png). (general)
5. **Tray labels.** src.html:784: "36 · 1 = 1" becomes "36"; show "1 = N" only when N is above 1; no wrap in net mode
   (play/shots/net-swipe.png). Keep the "1 = N" key Done when 10 needs. (general)
6. **Winter looks like winter.** drawTank ice: a thicker ice sheet creeping from the edges, a darker, dimmer water column
   under ice, slower fish (play/shots/ice-winter.png). Motion off: no movement change needed beyond the colour. (general)
7. **Chart readable when projected.** End labels and legend larger at 1280 px wide and up; the dial's labels likewise. (general)
8. **Frame-rate headroom.** src.html:1781 redraws chart and oxygen canvases every frame: redraw them only on `advance()`
   or a change; skip the tank redraw with Motion off; compute the net swipe's ghost once at swipe end, not per scoop
   (src.html:1670-1677; 60 ms long task measured). At 4x CPU throttle Life at the limits dropped 15 of 180 frames
   (craft/throttle.py). (general)
9. **Sounds like water.** src.html:653-661: short filtered-noise bursts for splash, net swish and ice crackle in place
   of sine blips; keep the 150 ms spacing and Fast rule. (family:curiosity)
10. **Chart room at 680x425.** src.html:155-163: fold the legend into the plot's top margin at short heights so the trace
    gets more than about 35 px; keep "13.4 mg/L" off the dial's base line (craft/z-680chart.png). (general)
11. **New, then Save.** src.html:1083-1084, 955-968: after Save in the New dialog, go on to Starter or Empty (or label
    the button "Save only") (craft/run1/new-save). (general)
12. **Habitat panel closes on Escape and an outside tap** at short screens (src.html:943-946, 1725;
    craft/run2/habitat-680.png). (general)
13. **Station label clear of the cattails.** src.html:223, 1231: move "Living Pond / FIELD STATION / 13" left of the
    reeds or draw the reeds lower (craft/z-station.png, play/shots/tap-minnow.png). (general)
14. **Compact ledgers at short heights.** At 680x425 the Matter and Energy ledgers cover about 40 percent of the tank
    (craft/run2/matter-680.png): two lines there (IN POND and the trip; caught and heat out). (general)
15. **Turtles asleep apart.** src.html:1157-1159: spread the sleeping turtles or put extras on the log
    (play/shots/limits-fps.png). (general)
16. **Empty pond label.** src.html:1363: "NO TURTLE · NO HERON" when neither was ever there, not "walked off / flew off"
    (play/shots/empty-pond.png). (general)
17. **Manual "Muck can hold most of the matter":** say "20 clumps (100 units)" to match the chart. (family:curiosity)
18. **Food web arrows to Muck** for the turtle and heron (the model sends 30 percent there, src.html:449, 458). (family:curiosity)
19. **Run button's pressed state.** src.html:773-774: drop aria-pressed or use a plain label so a screen reader does not
    hear "Hold, pressed" for a running pond; avoid the Roman numeral glyph in the accessible name. (general)
20. **Calendar "Year 1" in monospace** like the other readouts (src.html:58). (family:curiosity)
21. **Replay restores the chart speed** it found when it ends (src.html:984). (general)
22. **Tank focus ring visible**: draw it inside the canvas edge (negative outline-offset or inset ring), since `.tank`
    clips the outside one (src.html:43, 50). (general)

#### Settled calls
- **Event lines stay.** CODEX-CURIOSITY says voice speaks the hint once and then only on Read; the spec lists event
  lines. They are readings of what happened (ice, low oxygen, a kind gone), not how lines, praise or goals, so the
  spec's lines are built (should fix 1). They must never coach or congratulate.
- **The hint is spoken after the first touch**, as the spec and BASELINE rule 16 say. Only the stale case (first touch
  was a stocking tap) changes (should fix 6). The audit's "welcome not heard" rows are not findings.
- **Play's "log right"** in the spec's Look means the wooden log on the right of the tank, not a pond-log strip. The
  pond log stays in the Manual; polish 1 adds only a one-line latest-event readout.
- **Do not change the model's flows** to make matter trips reach animals faster. The model is carried from git 018ace9b
  and Done when 6 passes (Teaching: a muck trip reached Minnow). Should fix 10 is about which dot is followed and
  showing the wait.
- **Manual numbers come from the build's own runs**, not the spec's summary numbers (for example muck 92.1 percent, 11
  weeks, 1.03 percent). Teaching recomputed every one in Node and they match; do not revert them.
- **Real controls (should fix 2)** keep the same values, keys and defaults; no new settings, no presets added.
- **Tag splits:** the hint below 900 px is general (Play), not family (Craft); the matter-follow item is general
  (Craft). Energy ledger reset is a should fix (Play), not polish (Teaching): it breaks thing to do 4.
- **Audit noise, not findings:** every `#pond` overlap row; "text under 10 px" on the TIME and LENS labels at 375
  (deliberately hidden, selects carry aria-labels); "keep region" for #ledger and for #run/#speed/#tray under the modal
  drawer; "hint out of view" at 1000 px and up in states (cleared by the first touch); the tray scrolling sideways at
  375 (the spec asks for a scrolling row).
- No score, goal, level, sticker or finish to add or remove; none of the fixes may add one.

#### To the spec's open questions
- **MS-LS4-6 reach.** Should fix 15 adds a shade trace so the trait change is shown as numbers over generations. If
  Cory does not want a seventh chart chip, the alternative is to drop the MS-LS4-6 reach (rule 2).
- **OpenStax licence.** The spec's Sources line says OpenStax Biology 2e is CC BY 4.0; Teaching found CC BY-NC-SA 4.0
  stated at the source (the Manual already says so). The tool cites it as a source only, no text or figures reused, so
  nothing in the tool changes; the spec line should be corrected.

#### Not taken
- Play 1's "log strip on the tank per spec Look": misread of the Look line; replaced by polish 1.
- Changing matter flow weights so more trips reach animals: model is fixed (Settled calls).
- Dropping MS-LS4-6 now: moved to open questions; the trace is the fix.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: living-pond (Curiosity No. 13), round 1

Cold Craft lens, 2026-11-06. Judged against docs/agents/CODEX-CURIOSITY.md, "Curiosities: the second shape" in
docs/VISION.md, "The look" in docs/CURIOSITIES.md, STANDARDS and BASELINE. Bundle `tools/living-pond/living-pond.html`
as built (not re-bundled). My frames and scripts: `S:/CurioClass-codex-scratch/living-pond/craft/` (run1 to run4,
shots1.json, shots2.json, throttle.py, throttle2.py, z-*.png crops). Shared audit: `S:/CurioClass-codex-scratch/living-pond/audit-r1/`.

Counts: blockers 0, should fix 7, polish 7, nit 4.

#### Contract (clean)

- One file, 745,839 bytes (0.75 MB), well under the 2 MB goal. Art is two packed WebP atlases.
- No network requests: `performance.getEntriesByType('resource')` is empty after load and a run (run1/perf-default).
  No fetch, XHR or remote src in the bundle. Manual source links open only on a click (target _blank).
- Console clean in every shot of mine (the only exceptions were from my own synthetic keydown dispatched on `window`,
  which has no `matches`; real keys target an element, re-run on `document.body` was clean).
- Kit used for voice, tones, Motion and Sound (`Curio.voice`, `Curio.tone`); no kit header or kit.css frame.
- No score, goal, level, sticker, badge, finish screen or toast. Lesson-creep grep on src.html: only hits are
  "level" inside honesty prose about oxygen levels. No em dashes in src.html, notes.md, tool.draft.json, lines.json or
  the bundle. "Curio Class" is never shortened.
- Matter stays exact: 742.0 in, 1269.7 against an expected 1269.7 after 1,050 key adds and a crash (run3), 744.0 after
  ten winters with one minnow added (run1/tenyears-whole).
- Storage blocked: Save shows "This browser can't save here. The pond keeps running." and the pond keeps running
  (run1/storage-blocked). The Saved drawer states "Saved ponds stay on this device. Nothing leaves it." (rule 7).
- Art: both `art:` tokens (pond-shores-v2, pond-specimens) have prompts.json entries, `people: false`, and no people
  are drawn.
- Lines: `allLines()` returns exactly the one line in voice/lines.json, word for word.

#### Findings

##### Should fix

1. **Controls are browser dropdowns, not real instrument controls.** src.html:228, 230, 240-244. Speed, Lens, Feeder,
   Bottom, Decomposers, Canopy and Year are seven native `<select>` boxes; at 1366x768 the habitat row is five
   200 px wide form fields (audit size-1366x768.png, run1 frames). The look rule (CURIOSITIES.md "Real controls",
   CODEX-CURIOSITY "The look") asks for knobs, faders, toggle switches and dials that turn and click with a small sound;
   the spec itself calls Canopy and Year "dials" and Decomposers an On/Off switch. Better: a three-detent rotary switch
   for speed, lens, feeder, bottom, canopy and year (arrow keys step it and it announces its value), a lever toggle for
   decomposers, each with a soft click on Sound. Span and Spire and Pocket Universe use zero selects. family:curiosity.

2. **None of the spec's event lines exist.** src.html:622 (`L` holds only `hint`), voice/lines.json (one line). The
   spec's Voice section lists event lines ("Ice. No new air gets in until spring.", "Oxygen's low. The minnows are
   gasping at the top.", winterkill, heron or turtle left, "The snails are gone."). I ran 136 weeks with the feeder on
   Lots: the pond log recorded two freezes, a winterkill and "Heron flew off", and the voice log shows only the hint
   (run1/voice-events). The winters and the heron are the tool's drama and a student looking at the tank hears none of
   it. Add them as `V.say` events with the spec's 20 s spacing and a `valid` that the event is still true. family:curiosity.

3. **No first-run hint on screen below 900 px wide.** src.html:142 (`#hint{display:none}` under max-width 900). At
   680x425 (the site preview), 800x500, 760x900 and 375x812 the instrument never shows "Tap a creature to drop it in.";
   only the voice says it, and only after a touch (audit size-680x425.png, size-760x900.png, size-375x812; confirmed in
   CSS). The brief's one quiet first-run hint must be on the instrument at every size. A short version on the tank
   rim ("Tap a creature below") would fit. family:curiosity.

4. **The hint is spoken after the action it describes.** src.html:662-667. `afterTouch()` queues "Tap a creature to
   drop it in." on the first action of any kind and hides the on-screen hint at the same moment. If that first action
   was a tray tap, the student hears the instruction for what they just did, while the screen no longer shows it.
   Seen in the audit's held-click table (rows 6 to 13: every Add and Food tap speaks it) and in run1/voice-adds (hint
   spoken 1.4 s after the first minnow drop). Give the line a `valid` that no specimen has been dropped yet, or skip it
   when the first touch was itself a stocking tap. family:curiosity.

5. **"Whole run" vanishes when switched on.** src.html:42 and 85. `button[aria-pressed=true]` sets white text and
   `.chartbar button` then sets a transparent background, so the pressed button is white on the cream chart paper.
   Seen in run1/tenyears-whole.png (crop z-whole.png): the label is nearly invisible exactly when the chart shows the
   whole run. Give the pressed state its own dark fill or an inked underline. general.

6. **The oxygen meter has no marks at 3 and 2.** src.html:1597-1619. The dial ticks only 0, 5, 10, 15, 20; "3 gasp"
   and "2 kill" are loose captions in the meter's top-left corner that point at nothing, and at short heights (w under
   120) they are dropped entirely (680x425 frames). The spec asks for marks at 3 "fish gasp" and 2 "winterkill" on the
   needle meter. Draw two red-zone ticks or a shaded 0 to 3 band on the arc, labelled there. general.

7. **Matter lens by keyboard can only follow the muck.** src.html:1765. Enter on the tank in Matter always calls
   `follow(14)` (Muck), whatever the drop point is on; the tank's label promises "Enter ... follows a dot in Matter". A
   keyboard user cannot follow a dot from algae, a minnow or water and air, which is Things to do item 3. Follow the
   dot nearest the arrow-key crosshair, as Life does with `inspectCreature`. general.

##### Polish

8. **Frame rate holds on a fast machine, thins under throttle.** Measured with rAF intervals at 1366x768 (run1, run3,
   run4, throttle.py and throttle2.py, CDP CPU throttling): Starter pond and add limits (80 algae clumps, 120 snails,
   120 minnows, 60 nymphs, 3 turtles, 2 herons, 240 specks) run a 16.7 ms median with no frame over 20 ms at 1x. At 4x
   CPU throttle (a fair modest-laptop stand-in) Matter and Energy hold 60 fps, Life at the limits drops 15 of 180 frames
   to 33 ms. At 6x every lens drops 40 to 55 percent of frames. The loop redraws the tank, chart and oxygen canvases on
   every frame (src.html:1781) though the chart and meter change once a model week; drawing those two only on
   `advance()` or a change, and skipping the tank redraw with Motion off, buys the headroom. A net swipe makes up to six
   ghost runs in one pointer move (src.html:1670-1677 into `act`): one 60 ms long task on this desktop, likely about
   200 ms on a Chromebook; compute the ghost once at the end of the swipe. Ghost runs themselves are 3 to 4 ms warm. general.

9. **Sounds are sine blips, not the spec's sounds.** src.html:653-661. Splash, net swish, flake ticks, heron plunk,
   turtle knock, ice crackle and crack are all `Curio.tone` sine beeps at different pitches. Short noise bursts
   (filtered white noise for splash, swish and crackle) would make the tank sound like water. family:curiosity.

10. **The strip chart is about 35 px tall at the 680x425 preview.** src.html:155-163. The short-screen layout gives the
    recorder 103 px and the legend bar keeps 44 px of it, so the plot has a 0 to 80 scale in about 35 px (audit
    size-680x425.png, crop z-680chart.png). At 680x425 the oxygen readout "13.4 mg/L" also sits on the dial's base
    line. Fold the legend into the plot's top margin at short heights so the trace gets the room. general.

11. **New, then Save, does not start a new pond.** src.html:1083-1084 and 955-968. The dialog asks "Save this pond
    before starting another?"; Save saves and opens the Saved ponds drawer, and the old pond keeps running, so the
    student has to press New again (run1/new-save: overlay "saves", week unchanged). Save then ask Starter or Empty,
    or label the button "Save only". general.

12. **The Habitat panel on short screens ignores Escape and outside taps.** src.html:943-946, 1725. At 680x425 the
    panel covers the whole tray and chart; Escape leaves it open (run2/habitat-680.png, `habitat-open` still true). Close
    it on Escape and on a tap outside, like the drawer. general.

13. **The "Living Pond / FIELD STATION / 13" label sits behind the right-hand cattails.** src.html:223 and 1231. At
    1366x768 and 1920x1080 the cattail sprite crosses "Pond" and "/ 13" (crop z-station.png). Move the label left of the
    reeds or draw the reeds lower. general.

14. **At 680x425 the Matter and Energy ledgers cover about 40 percent of the tank.** run2/matter-680.png. The tank is
    about 150 px tall there and the ledger box is about 90 px tall on its left third. A two-line compact ledger at short
    heights (IN POND and the trip) would leave the dots visible. general.

##### Nit

15. **Run's pressed state reads backwards.** src.html:773-774. While running the button says "Ⅱ Hold" with
    `aria-pressed=true`, so a screen reader hears "Hold, pressed" for a running pond, and the Roman numeral glyph may be
    read as "two". Use a plain label ("Running, press to hold") or drop aria-pressed. general.

16. **The calendar's "Year 1" is in Georgia serif.** src.html:58. The spec's calendar readout is monospace
    (`YEAR 3 · WEEK 22 · SUMMER`), like every other readout. family:curiosity.

17. **Replay leaves the speed on Fast.** src.html:984. After a replay ends the chart speed stays at 8 weeks a second.

18. **The tank's focus ring is clipped.** src.html:43 and 50. The canvas outline sits outside the canvas and `.tank`
    clips it; the only focus sign is the small yellow crosshair. A ring drawn inside the canvas edge when focused would
    be clearer. Focus rings elsewhere are visible (crops z-focus-tray.png, z-focus-footer.png, z-focus-power.png).

#### Access (checked)

- Every control is a real button, select or input with a 44 px target; tray buttons announce kind, count and the
  drawing multiplier ("Add Snail. 68 present. One drawing = 2."); net mode relabels them ("Net one ..."), and
  Decomposers explains it cannot be netted.
- Keys: Space, period, < >, 1 to 7, N, L, W, M and Escape all work; arrows move the drop point on the tank; Enter
  inspects in Life (see 7 for Matter). The drawer is modal, traps Tab, returns focus on close.
- Motion off (calm frame, run1/motion-off): swimming, arrivals and flight stop, counts still update.
- Colour is never the only signal on the chart: each line has its own dash and an end letter (A, S, M, N).

#### Standard voice check

Held clicks (0.12 s), Sound on, Motion on; logs from `__tool.vlog`.

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| "Tap a creature to drop it in." | how (first-run hint) | once, only while it still fits | once per load in 5 Add taps (run1/voice-adds), but stale after a tray tap (finding 4) |
| Read (calendar, oxygen, temperature, counts, latest log) | read | every press, Sound off too | 3 of 3, including one with Sound off; cut the hint as it should (run1/voice-read) |
| Ice, oxygen low, winterkill, heron left, turtle left, snails gone | event | each event, at most once in 20 s | 0 of 5 events over 136 weeks (finding 2) |
| First tap on Sound | none | nothing | nothing (audit row 2) |

Repeats, order and Read: clean. No line named a hidden control. Stale lines: only the hint after a stocking tap.

#### Short-test notes for the merge (Craft view only)

The real thing is the interface: the tank, chart and meter are drawn from the live model, painted art only places it.
What holds it back from the look of Beat Lab or Elements Inspector is finding 1: the lower third of the screen is a
row of web form dropdowns.

#### Audit pilot

- **Leads confirmed:** "hint out of view" at 680x425, 800x500, 760x900 and 375x812 (finding 3, CSS display:none);
  the held-click table's "spoken" column showing the hint after every Add and Food tap (finding 4).
- **Leads wrong (noise):** every `#pond` overlap row at every size and state (the tank is a full-screen stage with its
  calendar, power panel, transport and ledgers on top by design); "hint out of view" at 1000 px and up in the states
  (the hint hides after the first action by design); "text under 10 px" on the TIME and LENS labels at 375 (font-size 0
  hides the words on purpose, the selects carry aria-labels); "keep region" for #ledger (the ledger sits on the canvas)
  and for #run, #speed, #tray in manual and saved (a modal drawer); the tray cut short at 375 (the spec asks for a
  scrolling row); "welcome not heard" after a first tap on the tank, Run, Step and the tray (the hint is the welcome
  and it was spoken, as the same rows show).
- **What it missed:** the invisible pressed "Whole run" (5), the missing oxygen marks (6), the missing event lines (2),
  dropdowns in place of real controls (1), Matter keyboard following only muck (7), New then Save (11), Habitat
  ignoring Escape (12), the station label behind the cattails (13), the tiny chart at 680x425 (10), and frame times
  under throttle (8).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: living-pond (Curiosity No. 13), round 1

Cold Play lens, 2026-11-06. Played twice: as a grade 5 student alone at home, and as a teacher projecting it.
Bundle `tools/living-pond/living-pond.html` as built. My frames: `S:/CurioClass-codex-scratch/living-pond/play/shots/`
(scenario JS in `play/mk.py`, `play/mk2.py`). Shared audit: `S:/CurioClass-codex-scratch/living-pond/audit-r1/`.

#### Short test (Curiosity)

- Would a kid open it unassigned? Yes. It opens alive: heron in the shallows, minnows schooling, a turtle in the mud,
  a chart pen moving. One tap on Minnow drops one in and the count ticks (`tap-minnow.png`). Netting all the minnows
  and watching the snails crash and the heron leave is a real "whoa" (`net-all-minnows.png`).
- Would an adult play for fun? Yes. Ten winters at Fast draw a real predator-prey cycle on the chart (`year10-whole.png`);
  overfeeding gives a true winterkill in year 2 with the minnows crowding the surface (`feeder-lots.png`).
- Is the real thing the interface? Mostly. The tank and the chart are the interface. The bottom third is a row of
  web-form dropdowns (finding 5), and the winter drama is mostly invisible (finding 1).
- Does it work with no finish line? Yes. No score, goal, level, sticker, toast or finish screen found.

The short test passes. No blockers. The findings are about the drama reaching the student and the instrument feel.

#### Findings

1. **should fix** · family:curiosity · src.html:375 (`logEvent`), 622 (`L` holds only the hint), 1617 (dial)
   The pond's best moments happen silently. Ice, ice-out, "Heron flew off", "Turtle walked off", "Snails gone" and
   "Winterkill conditions" are written only to the pond log, which lives inside the Manual drawer. Nothing on the
   instrument says them: there is no log strip on the tank (spec Look: "log right"), none of the spec's event lines
   ("Ice. No new air gets in until spring.", "Oxygen's low. The minnows are gasping at the top.", winterkill, heron or
   turtle left, "The snails are gone.") is in `L` or voice/lines.json, and the oxygen dial has no 3 and 2 marks on its
   face, only "3 gasp / 2 kill" as corner text. In `feeder-lots.png` (year 2 week 50, 0.6 mg/L, winterkill logged) the
   only cues are a needle near 0 and fish at the top; a student who looked away misses what the spec calls the pond's
   best lesson. Better: a one-line latest-event readout on the tank rim, the spec's event lines (once per 20 s), and a
   red band from 0 to 3 on the dial face.

2. **should fix** · general · src.html:142 (`@media(max-width:900px) #hint{display:none}`)
   The only first-run instruction is hidden at every width under 900 px: 680x425, 760x900 (tablet portrait) and
   375x812. Voice speaks the hint only after the first touch (src.html:662), so a student on a tablet or a narrow
   Chromebook window gets no instruction at all before acting. Seen in `narrow-680-winter.png` and audit
   `size-680x425.png`, `size-760x900.png`, `size-375x812 (iframe host).png`. Better: keep the one-line hint on the
   tank rim at every size.

3. **should fix** · general · src.html:42, 86-87 (`#whole` pressed style)
   "Whole run" turns white on the cream chart paper when pressed: the toggle vanishes exactly when it is on, so a
   student cannot see it to turn it off. Seen in `year10-whole.png`, `feeder-lots.png`, `net-all-minnows.png`
   (zoom: `play/z-whole.png`).

4. **should fix** · general · src.html:531-535 (yearly reset), `sync()` Energy ledger
   Spec thing-to-do 4 is "leave the Energy lens on for a whole year". At week 51 the ledger reads caught 25,114 and
   heat out 25,674 (102 percent); one week later, the moment the year is done, every line drops to 0 and "0.0% OF SUN"
   (`energy-yr1.png`, year 2 week 00). `s.lastEnergy` is kept but never shown. Better: show last year's totals beside
   this year's, or hold last year's ledger until the new year has a few weeks of data.

5. **should fix** · family:curiosity · src.html:228-244
   Seven of the instrument's controls (speed, lens, feeder, bottom, decomposers, canopy, year) are native `<select>`
   dropdowns styled as form fields. On every frame the bottom third reads as a settings page, not a study tank, and
   each change is two clicks into an OS menu. The tray and Run feel like an instrument; these do not. Better: detented
   dials or toggle switches with the value printed on them (Craft owns the look rule; flagged here for feel).

6. **should fix** · family:curiosity · src.html:1092-1108 (`follow`, `updateTracker`); Enter on the tank in Matter
   Following a dot rarely tells the promised story (muck, water and air, algae, minnow, muck again). I followed one dot
   from each of 8 starting pools for 52 weeks: only dots that started in an animal ever touched an animal; water and
   air, floating algae, stem algae, muck and decomposers never reached one (for example "Water & air > Floating algae >
   Muck > Decomposers > Muck"). Enter in Matter always follows Muck, which stayed "Muck" for 26 weeks
   (`matter-follow.png`): a long flat wait for a keyboard student. Better: Enter picks the dot nearest the drop point,
   and the trip box says how long the dot has been where it is.

7. **should fix** · general · src.html:716
   Words do not match the state: "The pond is full of minnow.", "...of heron.", "...of turtle.", "...of snail."
   (checked by adding to each cap). Use plurals, or "No room for more minnows."

8. **should fix** · general · Manual drawer (src.html, `#manualbody`)
   A solo grade 5 student is sent to the Manual for every explanation, and it reads as a model specification:
   "counterfactual", "flow-weighted probabilities", "outgoing flows share a proportional limit", "Caught is gross algae
   growth x 10". The "Who eats whom" table is clear; most of the rest is not readable at the anchor grade. Better: a
   plain first paragraph per section at grade 5, with the model detail below it for adults.

9. **polish** · general · src.html:611, 1538 (chart dashes)
   The actual lines for snails, minnows and nymphs are already dashed, and ghosts are dashed [5,4] at 0.85 alpha, so the
   "dashed ghost of the untouched pond" is hard to tell from the real snail trace (`tap-minnow.png`,
   `net-all-minnows.png`). Better: ghosts far paler (about 0.35) or thin dotted grey.

10. **polish** · general · src.html:784
    Tray labels read "36 · 1 = 1", "71 · 1 = 2". A student cannot tell this means "36 here, one drawing stands for 2".
    In net mode it wraps to "1 =" over "1" (`net-swipe.png`). Better: "36 here", and the multiplier only when above 1.

11. **polish** · general · src.html:1157-1159
    Three turtles asleep in the mud are drawn 35 px apart with a 77 px sprite, so they pile on one another
    (`limits-fps.png`). Spread them, or put the extras on the log.

12. **polish** · general · src.html:1363
    On an Empty pond the tank reads "TURTLE WALKED OFF · HERON FLEW OFF" though neither was ever there
    (`empty-pond.png`). Better: "NO TURTLE · NO HERON".

13. **polish** · general · drawTank, ice
    Winter is the drama the spec promises ("ice creeps in from the edges with a crackle"), but under ice the water stays
    the same bright teal with a thin pale band at the top, and the fish swim as in spring (`ice-winter.png`). The
    backdrop carries the season, not the water. Better: a thicker ice sheet, a darker dimmer water column, slower fish.

14. **polish** · general (teacher projecting) · chart legend, end labels, meter text
    From the back of a room the chart's line keys and end labels ("A 36", 10 to 12 px monospace) and the dial's
    "3 gasp / 2 kill" (10 px) cannot be read. The tank projects well; the chart, which carries the story, does not.
    Better: larger end labels at 1280 px and up.

15. **nit** · general · `.station` title
    "Living Pond / FIELD STATION / 13" sits over the log and cattails at top right, so "FIELD STATION / 13" is half lost
    in the art (`size-1366x768.png`, `tap-minnow.png`).

Checked and fine: a tap on Minnow drops one the same frame; ice arrives at week 41 (about 20 s at Normal); the heron
flies off in winter and returns in spring; food arrows on inspect are clear and labelled, absent kinds dashed
(`inspect-key.png`); New offers Save first (`new-confirm.png`); 60 fps at every add limit at Fast (headless,
`limits-fps`); the matter total stays 742.0 over ten winters; calm mode keeps time (the tick ignores Motion; audit
"Motion off" clean).

Counts: blocker 0, should fix 8, polish 6, nit 1.

#### Audit pilot

- Leads confirmed: "hint out of view" at 680x425, 800x500, 760x900 and 375x812 (finding 2; a CSS rule, not a scroll).
  The 375x812 tray scrolls sideways with Decomposers, Food and Net out of view; the spec asks for a scrolling tray row
  there, so not reported.
- Leads wrong (noise): every `#pond` overlap row (the canvas fills the tank and controls sit on it by design);
  "text under 10 px 0.0px" on the TIME and LENS labels at 375 (deliberately font-size 0; the selects keep aria-labels);
  "keep region #ledger covered" (the ledger is an overlay on the canvas); "#run/#speed/#tray hidden" in manual and saved
  (the modal drawer makes main inert); "hint out of view" at 1000 px and up in states (the state's first touch had
  cleared it); "welcome not heard after first tap" (BASELINE rule 16).
- Missed by the audit: the invisible pressed "Whole run" toggle, the Energy ledger zeroing at year end, the status
  grammar, stacked turtles, the Empty pond's "walked off / flew off" label, the silent winterkill and missing event
  lines, the Matter trip that rarely reaches an animal, and the Manual's reading level.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: living-pond (Curiosity No. 13), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", not lesson norms.
Module: science-5-food-webs-and-matter-cycles (5-LS1-1, 5-LS2-1, 5-PS3-1); reaches 3-LS4-2, 3-LS4-3, MS-LS2-1,
MS-LS2-2, MS-LS2-3, MS-LS4-4, MS-LS4-6.

How I checked: the model script (src.html:342-600, which exports itself) run headless in Node for every Done-when
scenario and every "Things people have found" number (scratch: S:/CurioClass-codex-scratch/living-pond/teaching/sim.js,
sim2.js); the bundle driven with scripts/drive.py on port 9411 (frames in
S:/CurioClass-codex-scratch/living-pond/teaching/frames/); sources checked on the web.

Counts: blocker 0, should fix 7, polish 3, nit 2.

#### Findings

1. **should fix, family:curiosity.** Where: chart and tray counts (src.html:539 `A:(s.p[1]+s.p[2])/5`, counts() at
   :762). What: the Algae trace and count add floating and stem algae together, so the headline cascade (net the
   minnows, floating algae bloom, they shade the stem algae, the snails starve) shows on the recorder as "algae up,
   snails down", the opposite of what a grade 5 student expects, with the cause invisible. Stem algae drop from about
   46 to 3 units while the Algae line climbs; the only sign is the faint fade of the stem sprites. How seen:
   frames/t-netminnows.png (net all minnows at Y1 W13, run 45 weeks); Node run: Af 245 to 440, As 45.7 to 3.3, snails
   31.5 to 0. Better: two algae traces or chips (floating, on stems), or the stem share in the tray label.

2. **should fix, family:curiosity.** Where: drawWeb (src.html:1443-1492) and hitboxes (:1239-1246). What: only floating
   algae clumps are tappable as "algae", so the snail's and the turtle's food arrows start at a floating clump at the
   surface, while the model and the Manual's table say both eat algae on stems. It teaches the wrong link in the very
   chain finding 1 depends on. How seen: frames/t-turtle-inspect.png (turtle arrow from "Algae" at the surface); code.

3. **should fix, family:curiosity.** Where: Manual, "Food can slow the shade drift" (src.html:303). What: "With Some
   feeding, the average was 2.10" is true, but by then the Some pond has had winterkill conditions in 6 of 10 winters
   and holds 0.86 minnows; the entry presents it as green water hiding fish and never says the school was nearly wiped
   out each winter. A student who repeats the run sees Minnows 40 one week and near 1 the next and cannot square it with
   the entry. How seen: Node (winterkills 6, minnow count 0.86 at Y10 end); frames/t-feeder-some-y9.png (Y9 W49, O2
   1.5 mg/L, log "Winterkill conditions"). Better: name the winterkills in the entry, or use a feeding level that keeps
   the school.

4. **should fix, family:curiosity.** Where: Manual, "Things people have found" (src.html:292-306). What: the spec's
   Manual asks for each find "in this pond, with real-world sources" (Carpenter, Kitchell and Hodgson 1985 for the
   cascade; Minnesota DNR for winterkill; Lindeman 1942 and OpenStax 46.2 for the energy shares; Endler 1980 for the
   shade drift; Cornell Lab for the heron). The built entries keep only "this is a model result, not a measurement".
   Honest, but the student never learns that real lakes do the same thing, which is what turns a toy run into
   5-PS3-1 and MS-LS2-3 evidence. How seen: frames/t-manual-found.png; spec "The Manual". Better: one plain sentence
   per entry: "Real lakes do this too (source)."

5. **should fix, general.** Where: Manual throughout (src.html:259-306) and the Energy ledger. What: the language is
   pitched well above grade 5 (and hard for grades 6 to 8): "a counterfactual, not a prediction after further
   changes", "flow-weighted probabilities", "outgoing flows share a proportional limit when a pool is short", "Algae
   net production subtracts their respiration; grazer net production subtracts body maintenance from growth",
   "inherited shade shares drift", ledger "STORES USED", "GRAZERS NET". How seen: frames/t-manual-found.png,
   frames/t-energy-y10.png. Better: plain words ("the dashed line is the pond you didn't change"; "kept in algae after
   they breathe"; "plant eaters"), with the exact terms kept for the honesty paragraph.

6. **should fix, family:curiosity.** Where: Matter lens and Manual "Model and honesty" (src.html:281). What: 5-LS1-1
   asks students to argue that plants get their growing material chiefly from air and water, not soil. Here the pool
   is "Water & air", which the Manual says also holds the nutrients, and a muck dot's trip runs Muck, Water & air,
   Algae. Nothing on screen lets a student say "the algae's body came mostly from air and water, not from the mud";
   a student could as easily conclude the algae are built from rotted muck. How seen: Matter trips from
   frames/t-matter-trip.png run ("Muck > Decomposers > Water & air > Floating algae > Minnow > Muck"); Manual text.
   Better: in the Manual and the algae inspect label, say algae build from carbon dioxide (air) and water with sunlight,
   and that the nutrients from muck are a small share lumped into this pool. If that can't be shown honestly, 5-LS1-1
   is mentioned, not taught (rule 2).

7. **should fix, family:curiosity.** Where: shade strip (src.html:243, sync :808). What: MS-LS4-6 (a reach code) asks
   for a mathematical representation of a trait changing over generations. The tool shows only the current AVG SHADE;
   there is no history of it, so the drift the Manual describes over ten winters can only be seen by writing numbers
   down. How seen: frames/t-shade-y10.png (AVG SHADE 1.21, no record of earlier values; Whole run shows populations
   only). Better: an optional shade trace on the recorder (a chip like the population chips), or drop the MS-LS4-6
   reach. MS-LS4-4 and 3-LS4-2 are fine as they stand.

8. **polish, family:curiosity.** Where: updateTracker and the decomposer flows (src.html:434-441, 1098-1110). What: 80
   percent of what decomposers break down goes straight from Muck to Water & air (as their breath), so most trips read
   "Muck > Water & air" and skip the decomposers, the very role 5-LS2-1 names. How seen: three of four trips in the
   t-matter-trip run. Better: label that step "Muck > broken down by decomposers > Water & air".

9. **polish, family:curiosity.** Where: Energy ledger (sync, src.html:816-822). What: the ledger shows only the year so
   far and resets at week 0, so "heat out against caught" reads 88 percent at week 32 and only nears 100 in the last
   weeks; at Fast a student rarely sees the closed year. The model already keeps `lastEnergy`. How seen:
   frames/t-energy-y10.png (88.1 percent at Y10 W32); Node: last full year 99.9 percent. Better: a "last year" line.

10. **polish, family:curiosity.** Where: drawEnergy (src.html:1432-1441). What: the sunlight arrows, four heat columns
    and the green "kept" arrow carry no labels, and the heat columns are grouped by the pool the matter leaves, so an
    eater's digestive breathing is drawn on its prey's column and decomposers breaking down muck (the largest heat
    source) has no column at all. How seen: frames/t-energy-y10.png; code. Better: small labels (Sun, Algae, Snails,
    Minnows, Decomposers) and heat attributed to the eater.

11. **nit, family:curiosity.** Manual, "Muck can hold most of the matter": "algae above 100 units after 11 weeks" is
    true (Node: 11 weeks), but the chart and tray show clumps, so the student sees 20. Say "20 clumps (100 units)".

12. **nit, family:curiosity.** drawWeb gives the turtle and heron no arrow to Muck, though the model sends 30 percent
    of what they eat there (src.html:449, 458).

Nothing cultural, Native or hard-history: no sensitivity review needed. No giveaway concerns (no quiz or hidden
answer). No score, goal, level, sticker or finish screen found (lesson-creep grep on src.html: no hits beyond two uses
of "level" in oxygen prose).

#### Done when (the teaching-relevant ones, tested)

| # | Result | Evidence |
|---|---|---|
| 1 | PASS | Opens running; ice from week 41, about 19 s at Normal from week 3 (T < 4 for weeks 41 to 51). |
| 2 | PASS | Node, Starter 520 weeks: all six kinds kept, total 742.000 (drift 4e-12), year 10 snail counts 21 to 36 ("about 19 to 34"). |
| 3 | PASS | Net all minnows Y1 W13: floating algae 440 by W30, snails 4.7 vs ghost 9.5 by W30, heron off W15, turtle off W25. |
| 4 | PASS | Decomposers off: muck 92.1 percent at Y1 end; turtle walked off W33, before any kind went; back on, algae past 100 units in 11 weeks. |
| 5 | PASS (see finding 3) | Lots for two summers: winterkill Y2 W48, minnows gone W109. Some: minnows survive ten winters but with 6 winterkills, 0.86 left. Sand 3.50 to 2.27 by Y3 end; gravel 3.50 all ten years. |
| 6 | PASS (see finding 9) | Muck trip reaches Minnow; last full year heat 99.9 percent of caught; mid-year ledger 88 percent. |
| 7 | PASS | Canopy 25: all six kept; 50: nymphs gone Y3 W25; Cold: nymphs gone Y3 W43; Mild: no ice, all kept; each 742.00. |

#### Facts checked against a second source (13)

All Manual numbers recomputed in Node and matched: 1.03 percent caught, 9.65 percent grazers, nymph-netted snail peak
73.4 vs ghost 32.8, muck 92.1 percent, 11 weeks, shades 1.22 / 2.10 / 5.78, canopy and Year outcomes. External: OpenStax
Biology 2e licence is CC BY-NC-SA 4.0 at the source, as the Manual says (the spec's "CC BY 4.0" is out of date); USGS
confirms cold water holds more oxygen and decay uses it (no mg/L table there); oxygen fit 14.6 at 0 °C and 9.6 at
20 °C against the standard freshwater table 14.6 and 9.1 (Manual states the 0.5 gap); Minnesota DNR confirms ice,
low light and decay drive winterkill and uses 2.0 mg/L as its alert line; citations Lindeman 1942 Ecology 23(4),
Holling 1959 Can. Entomol. 91, Gillooly et al. 2001 Science 293, Endler 1980 Evolution 34(1), Carpenter, Kitchell
and Hodgson 1985 BioScience 35 all correct; heron sight-hunting in shallows, painted turtles overwintering in mud and
dragonfly nymphs' extendable lower lip and fish prey match the cited pages' known content. No readout found lying;
the Manual is careful to call its numbers model results and the pond made-up.

#### Frames looked at

Mine: t-default-2s, t-netminnows, t-turtle-inspect, t-energy-y1, t-energy-y10, t-manual-found, t-shade-y10,
t-feeder-some-y9, t-decomp-off, t-winterkill-lots, t-matter-trip (frames/ in my scratch). Audit: size-1366x768,
state-matter and state-energy at 1366x768.

#### Audit pilot

- Leads confirmed: none that bear on teaching.
- Leads wrong (for this lens): the #pond overlap rows at every size are the full-bleed canvas under its own overlays,
  noise as the brief warned; "hint out of view" at 1366x768 is wrong, the hint shows bottom-right of the transport in
  size-1366x768.png; the "welcome not heard" rows are the first-run hint being dismissed by the first action, which is
  the Curiosity design and BASELINE rule 16.
- Missed (outside its reach): all twelve findings above, chiefly the combined algae trace hiding the cascade, the food
  arrows from the wrong algae, and the confounded feeding entry.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: living-pond (Codex fix, round 1)

Evidence is relative to `_scratch/living-pond/`. All listed frames were opened and inspected. The source is an open-ended Curiosity; its numerical ecosystem was preserved.

#### Blocker
None in refine.md.

#### Should fix
1. FIXED: Six plain event readings now use V.say, current-state validity, four-second expiry and a per-line 20-second cooldown. `fix-before/before-events.png` and `before-events.json` show the old silence; `voice-ice.json`, `voice-low.json`, `voice-winterkill.json`, `voice-heron.json`, `voice-turtle.json`, `voice-snails.json` each show one matching spoken event at 1366x768. Seven fixed lines match allLines and voice/lines.json. Browser speech remains the recording fallback.
2. FIXED: All seven dropdowns became six detented rotary switches and one decomposer lever, preserving values, defaults and shortcuts. Arrow keys, Home/End and printed accessible value text work. `before-default.json`: 7 selects; `after-default.json`: 0. `fix-targeted/final-rotary-keys.png` and `switches-all-ends.json` cover all values and roles at 1366x768.
3. FIXED: Separate Floating and Stems traces, chips and end labels show the cascade. `fix-before/before-cascade.png` versus `fix-after/after-cascade.png`, both 1366x768; at the same week floating = 43.03 clumps, stems = 0.744 clumps. The populations did not change, only their recording.
4. FIXED: Four stem-algae hitboxes anchor the snail/turtle food routes. `fix-before/before-turtle.png` versus `fix-after/after-turtle.png` at 1366x768; before 0 stem anchors, after 4 (`after-turtle.json`). Stem algae can also be inspected.
5. FIXED: The rim hint stays visible before interaction at 680x425, 800x500, 760x900 and 375x812 in the iframe host. Matching `fix-before/before-hint-*.png`, `before-phone.png` and `fix-after/after-hint-*.png`, `fix-phone-closeout/final-phone.png`; computed display changed from none to block at each width.
6. FIXED: First Add or Food sets the stocking flag before the hint's validity is tested. `before-add-hint.json` records the old late spoken hint; `after-add-hint.json` and `voice-food-first.json` have empty voice logs after those first actions, at 1366x768. A first non-stocking touch still speaks the hint once.
7. FIXED: Whole run has its own dark pressed fill. Before: white on transparent; after: white on rgb(11,79,86), 9.26:1 nominal contrast. `fix-before/before-whole.png` versus `fix-after/after-whole.png`, 1366x768.
8. FIXED: The oxygen arc has a red 0 to 3 band, actual ticks at 2 and 3, and the labels fish gasp / winterkill at every width. `fix-before/before-hint-680.png` versus `fix-final/final-short-ledger.png` at 680x425; `fix-after/after-default.png` at 1366x768 and phone closeout show the same marks. The Manual identifies the thresholds as model choices.
9. FIXED: Energy shows the last closed year beside the current year. `fix-before/before-year-boundary.png` versus `fix-after/after-year-boundary.png`, 1366x768. At week 52 the previous caught = 25136.25 and heat = 25756.49 remain visible (102.5 percent), while the new year starts at zero.
10. FIXED: Matter Enter follows the dot nearest the arrow-key drop point and shows weeks in its current pool. Matching `before-matter-key.json` / `after-matter-key.json`: pool 14 (Muck) became pool 1 (the targeted Floating algae). `fix-after/after-short-matter.png` shows Muck, 4 weeks here at 680x425; `matter-direct-breakdown.json` records a trip reaching Snails and Minnow without changing flows. Netting a tracked turtle and a turtle walking away both reset the outside wait to 0 weeks (`tracker-exit-wait.json`).
11. FIXED: Recorder, Matter, Energy, food-web and honesty sections start with plain explanations; exact model terms are inside optional details. Energy labels now say Algae kept, Plant eaters kept and using stored food. `fix-before/before-manual.png`, `fix-after/after-manual.png`, and `fix-regressions/regression-energy.png`, all 1366x768.
12. FIXED: The feeding finding now states six winterkill winters and 0.86 remaining minnows. `before-feeding-shade.json` reproduces those values; `fix-targeted/final-manual-finds.png` shows the corrected entry at 1366x768. No false promise that Some preserves the school remains in this entry.
13. FIXED: Every one of the ten findings names real-world scientific context and distinguishes its own model result. The Manual and metadata name licences or reference-only copyright status. `before-manual.json` versus `after-manual.json`, plus `fix-targeted/final-manual-finds.png` at 1366x768. Source verification is recorded below.
14. FIXED: Both the honesty paragraph and visible/accessible algae inspection explain carbon dioxide and water, sunlight, and the small nutrient share combined into Water & air. `before-manual.json` lacks this explanation; `fix-targeted/final-algae-inspect.png` and `final-algae-inspect.json` show it at 1366x768.
15. FIXED: Optional Shade history is off by default, with its own dash, chip and end label, scaled separately from 0 to 7. `before-default.json` has no Shade key; `fix-targeted/final-shade-history.png` shows 523 stored samples from 3.50 to 1.21, with Whole run enabled, at 1366x768. Population calculations are unchanged.
16. FIXED: Full-capacity messages use plurals. `before-full-status.json`: The pond is full of minnow. `after-full-status.json`: No room for more minnows. Matching frames in fix-before and fix-after are 1366x768; the same map covers snails, herons, turtles and nymphs.

#### Polish accepted
1. FIXED: Latest log event is a quiet tank-rim readout; the full log stays in the Manual. `fix-after/after-events.png`, 1366x768, and `fix-final/final-short-ledger.png`, 680x425.
2. FIXED: Sun, kept food and named heat columns are labelled; fixed-adult heat belongs to the eater, and decomposition has its own column. `fix-targeted/final-heron-heat.png`, 1366x768; attribution numbers in `final-heron-heat.json`. Phone closeout separates the labels into three rows. Final eater metadata also attributes ordinary digestion to the eater, including fish-food heat. `energy-attribution-energy.json`: all respiration = 76.70810711193283, all named columns = 76.70810711193279; nymph digestion = 1.9511018345507336 and fish-food digestion = 2.8058484610706054 are included. Final frames: `fix-post-audit/final-energy-attribution-energy.png`, `fix-last-energy/energy-labels-*.png` and `fix-last-proof/clear-energy-labels-*.png`.
3. FIXED: A direct Muck-to-Water & air trip says broken down by decomposers. `matter-direct-breakdown.json` and `fix-final/matter-direct-breakdown.png`, 1366x768. Paths actually visiting the decomposer body pool retain that pool name.
4. FIXED: Ghost alpha is 0.35 with long dashes. `fix-after/after-cascade.png`, 1366x768; actual traces remain dark with distinct dashes.
5. FIXED: Counts omit 1 = 1, retain 1 = N only above one, and stay on one line in net mode. `fix-final/final-net-tray.png` and JSON: every count's scroll width equals its client width at 1366x768. Compact net layout is checked by the audit.
6. FIXED: Ice is thicker, edges extend inward, the water dims, and fish motion slows to 0.35 under ice. `fix-targeted/final-winter-three.png`, 1366x768. Colour changes remain when Motion is off.
7. FIXED: At 1280 and wider the legend is 13 px, chart end labels 12 px and meter labels 12 px, versus 10/11 px before. `fix-after/after-1280.png`, `after-default.png`, `after-1920.png`.
8. FIXED: Chart/meter rendering is cached until a change; Motion off skips idle tank drawing; a swipe builds one ghost on release. `performance-calm.json`: unchanged draw counts across 2 seconds. `performance-swipe.json`: six scoops, one ghost. Four-times CPU throttle: 180 frames, 1 above 25 ms, 59.67 fps (`fix-performance/throttle.json` and frame). This is a desktop test, not a Chromebook guarantee.
9. FIXED: Splash, net and ice use filtered noise buffers, retaining the 150 ms gate and Fast rule. `sound-buffer-evidence.json`: 0.13 s splash and 0.24 s ice, running AudioContext; `net-noise.json`: 0.18 s swish. No recorded audio or downloaded sound was added.
10. FIXED: At 680x425 the legend sits in the top plot margin, clear of the right end labels; 52 px of trace height remain. Oxygen value moved above the arc. `fix-before/before-hint-680.png` versus `fix-final/final-short-ledger.png`; `final-short-recorder.json` records the plot dimensions.
11. FIXED: The New dialog now labels its existing save action Save only. `fix-targeted/final-save-only.png`, 1366x768.
12. FIXED: Habitat closes on Escape and an outside tap at 680x425. `final-habitat-escape.json` and `final-habitat-outside.json` both report open false; matching fix-targeted frames were inspected.
13. FIXED: The station plate moved left of the right-hand reeds. `fix-after/after-default.png`, `after-hint-760.png` and phone closeout.
14. FIXED: At 680x425 Matter shows IN POND and trip; Energy shows caught and heat, with last-year values alongside. `fix-after/after-short-matter.png`, `fix-final/final-short-ledger.png`; Energy ledger is 38 px high, down from the tall six-line panel.
15. FIXED: Sleeping turtles are 95 px apart on the wide tank. `fix-targeted/final-winter-three.png` shows all three asleep without overlap at 1366x768. At 375x812 the three turtles are 87.6 px apart, each 77 px wide (`phone-three-asleep.json` and `fix-last-proof/phone-three-asleep.png`). The narrow arrangement keeps all three inside the tank.
16. FIXED: An unstocked Empty pond says NO TURTLE and NO HERON. `fix-after/after-empty.png`, 1366x768. Departures retain their actual walked/flew-off wording.
17. FIXED: The muck finding says 20 clumps (100 units). `fix-regressions/muck-finding-corrected.png` and JSON, 1366x768.
18. FIXED: Turtle and heron inspection both show arrows to Muck, matching the existing 30 percent transfers. `fix-after/after-turtle.png` and `after-heron.png`, 1366x768.
19. FIXED: Run/Hold has plain text and an action-specific accessible name, with no aria-pressed or Roman numeral. `fix-after/after-default.png` and source; keyboard focus frame confirms the controls remain reachable.
20. FIXED: Calendar Year uses Consolas/monospace. `fix-after/after-default.png`, 1366x768.
21. FIXED: Replay saves and restores its prior speed. `replay-restored.json`: restored Slow = 1, week 8, held; `fix-final/replay-restored.png`, 1366x768.
22. FIXED: Keyboard focus uses a 3 px inside outline. `focus-keyboard.json`: focus-visible true, offset -5 px; `fix-final/focus-keyboard.png`, 1366x768.

#### Settled calls
Applied all: event readings are factual, hint follows first non-stocking touch, the wooden log remains on the right, matter weights are unchanged, actual run numbers are preserved, switch values/defaults remain unchanged, shade history is optional, and no lesson structure was added. The Curiosity brief takes precedence over welcome/goal/score/finish audit conventions. No spec open question was changed. The old OpenStax licence error remains a spec-maintenance issue; the tool says current CC BY-NC-SA reference only.

#### Cheats tried
- Oxygen: rapid Food taps stop at 30 units per week; overfeeding still causes low oxygen and winterkill. No score or pass can be earned by tapping.
- Swept all seven switches through every detent: all values and accessible labels match, matter remains 742.0. The oxygen meter stays a numeric model output, not a success badge.
- Net swipe at the limit: six removals, one pre-change ghost. Additional contacts do not exceed the swipe cap.
- Matter: keyboard targeting chooses an actual drawn dot; changing the target does not change the conservative transfer weights. A direct muck trip reached Snails and Minnow and recorded the wait.
- Voice: repeated Ice requests inside the cooldown produce one spoken Ice line. A Heron line queued behind winterkill is dropped stale after the heron is present again (`voice-stale-dropped.json`), with an empty queue.

#### Voice walk
Held clicks used 0.12-second presses, with 2-second gaps. First Run: hint once. Natural model transitions were positioned immediately before the event, then advanced: ice at week 42, low oxygen at week 52, winterkill at week 101, heron departure at week 16, turtle departure at week 34, snails gone at week 69. Each matching event has one spoken log entry. First Add and Food produce no stale hint. Read retains the live calendar, oxygen, temperature, counts and dated latest log line; queued events cannot interrupt it. Files: fix-voice/*.png, voice-*.json, fix-final/voice-stale-dropped.png. No ranger clips were available; the existing offline browser voice supplies speech.

#### The real material
No ecological dataset was downloaded, sampled or added. Original model and prose: Curio Class revision 018ace9b, CC BY 4.0 content and MIT code under the repository licences. All seven daily transfers, rates and thresholds are illustrative model choices. `fix-model-parity.json`: 27 habitat combinations times 520 weeks, zero population/oxygen drift, largest conservation error 5.60e-11 units.

Source pages were checked 2026-11-06. They are references only; no third-party text, figures or datasets were bundled. Manual and tool.draft.json record the same source names and reuse terms.

- Photosynthesis and body material: [OpenStax 8.1](https://openstax.org/books/biology-2e/pages/8-1-overview-of-photosynthesis) and [31.1](https://openstax.org/books/biology-2e/pages/31-1-nutritional-requirements-of-plants), CC BY-NC-SA 4.0 as confirmed in its current Preface; independently checked against [NOAA Ocean Exploration](https://origin.oceanexplorer.noaa.gov/ocean-fact/photochemo/), public-domain federal text. NOAA independently verifies sunlight, carbon dioxide and water; OpenStax 31.1 supplies the small mineral share. These are original plain explanations, not copied passages.
- Decay, blooms, shade and oxygen: [USGS Dissolved Oxygen and Water](https://www.usgs.gov/water-science-school/science/dissolved-oxygen-and-water), public-domain federal text, and [EPA Nutrient Pollution](https://www.epa.gov/nutrientpollution/effects-environment), federal reference with document-specific third-party exceptions; no media reused.
- Winterkill: [Minnesota DNR](https://www.dnr.state.mn.us/areas/fisheries/waterville/winterkill.html), copyright Minnesota DNR, reference only; corroborated by USGS decay/oxygen guidance. The page initially returned 403, then loaded successfully. The 3 and 2 mg/L thresholds remain model settings, not universal tolerances.
- Food-web cascades and energy: [Carpenter, Kitchell and Hodgson 1985](https://doi.org/10.2307/1309989), copyright American Institute of Biological Sciences, and OpenStax Biology 2e 46.1-46.3, CC BY-NC-SA 4.0, reference only. Lindeman 1942 remains a copyrighted provenance citation; the percentages are recomputed model results, not copied data or universal energy rules.
- Inherited shade: [Endler 1980](https://doi.org/10.1111/j.1558-5646.1980.tb04790.x), copyright Society for the Study of Evolution, reference only; selection mechanism checked with OpenStax 19.3. Guppies are the source organism; this minnow model does not claim to reproduce their experiments.
- Heron hunting: [Cornell Lab](https://www.allaboutbirds.org/guide/great_blue_heron/lifehistory) and [Audubon](https://www.audubon.org/field-guide/bird/great-blue-heron), copyrighted references only. The feeding/shade numbers are this model's own results.
- Existing species art and other natural-history citations were retained. No new images, software or audio were downloaded.

#### Lesson creep check
`fix-creep.json` has two matches for level, both sea-level oxygen references. No goal, score, level progression, quiz, finish screen, kit header, praise, badge or sticker was introduced. There are no em dashes in src.html or the fixed voice lines.

#### Engine changes wanted
No shared engine change was needed. Existing handoff requests about art rekey dependencies and drive.py letter-key support remain unchanged. The fix uses the existing kit voice queue and local Web Audio.

#### Audit
The single audit finished successfully in 968 seconds (16 minutes 8 seconds), within the 2400-second limit. It reported 266 mechanical leads. All 42 audit frames were inspected through `fix-audit-contacts/` and compared with the targeted full-size frames. All 33 held-click rows had no errors and kept focus through Enter twice. Five-click and quick-tap probes were clean; resize stress found no exceptions or controls left disabled.

Every lead group is accounted for:
- Canvas overlaps: the instrument's controls and readouts intentionally sit over #pond, as the Settled calls say. No control-to-control overlap was reported.
- Phone TIME/LENS parent labels at 0 px: deliberately hidden; their rotary buttons have explicit accessible names and visible value text.
- Phone tray choices outside its scroll window: the specified scrolling specimen row; controls remain keyboard-reachable.
- Phone recorder choices outside #legend: confirmed and fixed. Seven 44 px keys now fit two rows with no horizontal overflow. `post-audit-phone-life.json`, `post-audit-phone-matter.json`, `post-audit-phone-energy.json` and `phone-shade-key.json` prove the bounds; `fix-last-proof/phone-shade-key.png` shows the optional shade line enabled.
- Ledger keep-region coverage: settled hit-test noise from noninteractive readouts over a canvas. The full-size frames show them plainly.
- Run/Speed/Tray hidden under Manual or Saved drawer: the intended modal/inert background, already settled.
- Hint out of view after interaction: the one-time hint has been dismissed, as intended.
- Welcome not heard/late: the Curiosity has a first-touch hint and factual event voice, not a lesson welcome. The accepted Add/Food suppression is separately verified. No welcome, goal, score or finish was added.

After the audit, its recorder-key lead and the manually confirmed heat-attribution/label lead received the scoped checks above, plus the two outside-tracker wait paths. No second full audit or lens pass was run. The final offline bundle is 744 KB, with clean scoped console logs and zero tool network requests. `fix-final-validation.json` records source/bundle hashes, the audited input hash, model parity, voice equality and closed ports. The full audit predates these scoped corrections; the report does not claim a second mechanical audit on them.

#### Frames and verification
Frames for the final scoped corrections are in fix-post-audit, fix-last-proof and fix-last-energy. Earlier before/after evidence is retained, including unsuccessful harness fixtures. A mistaken selector in one Manual fixture and a screenshot-result filename collision were corrected and rerun; they were harness errors, not tool exceptions. The original painted art is unchanged. Reference frames of Beat Lab, Elements Inspector, Span and Spire and Pocket Universe were opened; their lesson-shaped elements were not copied.

#### Left open
- Gravel-ranger recordings are not bundled; browser speech is the existing fallback.
- The historical claim that Some feeding keeps the school through ten winters is contradicted by the actual model. Per Settled calls, the fix reports winterkills instead of altering its flows.
- Four-times CPU performance was measured on this desktop, not on school Chromebook hardware.
- No questions were asked in this unattended run. Where there was a choice, the specified alternatives were used: retain the model; label Save only; use separate algae traces and an optional shade trace; use the settled factual event voice.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Living Pond build handoff

`src.html` contains the instrument CSS and markup, the conservative model, and the display and interaction controller in that order. `living-pond.html` is the generated offline bundle. No shared file was edited. There is no lesson sequence or achievement layer.

#### Model

The model uses sixteen matter pools plus fixed adult turtle mass. Seven daily substeps share a proportional outflow limiter. Minnow shade is eight matter pools. All population rates are deterministic. The tracer alone uses a seeded linear congruential draw to choose among actual transfers. Visual positions are deterministic seeded functions.

Habitat changes are applied immediately and recorded with the current week. A 104-week counterfactual is computed from the pre-change state. Saved ponds store the starting choice, action log and week. Open reconstructs silently; Replay applies the same marks at Fast. Storage calls are guarded.

Energy resets at the calendar boundary. `lastEnergy` supplies the last-year column beside the current year, including at week 0.

Decomposers Off freezes their activity and body pool; this hypothetical switch matches the brief's dormant specks and ensures that turning it back on can recover an early collapse. If algae have actually gone extinct, decomposers cannot create new algae; restocking is needed.

#### Art

One 6 × 6 atlas holds the 36 requested painted objects and places. Canvas crops its cells, and all live water, positions, tint, ice thickness, charts, dots, arrows, ledgers and gauges remain code. Raw generation is preserved in `art/raw/`. Prompts are in `art/prompts.json`.

The prescribed `scripts/art.py --rekey` command failed because the available Python lacks NumPy. `_scratch/living-pond/prepare_art.py` creates a browser canvas packing page; the assigned-port drive produces a keyed WebP data URI, and `assemble.py` saves it and assembles the source. This is deterministic packing, with no paid service or software installation.

#### Evidence

All build scripts, the historical specification, raw check results and frames are under `_scratch/living-pond/`. `model-results.json` records the ten-winter and intervention runs. `verify-model.js` checks conservation and finite values through every step; `verify_numbers.py` independently checks scenario thresholds and the seasonal calendar.

Browser evidence covers immediate input, tracer transfers, save/open, Replay equality, blocked storage, voice ordering, extreme populations, motion, grayscale and responsive layouts. The final mechanical audit is under `audit/`. Its leads are answered in `codex-report.md`.

#### Engine changes wanted

- `scripts/art.py` imports NumPy and SciPy for rekeying. Document or supply a supported interpreter for the build environment, so the normal art packing command works without installation.
- `scripts/drive.py`, key map in `main`: add arbitrary letter/digit shortcuts. Its current map raises KeyError for `l`, `n`, and `3`. This build's live-walk harness sends proper CDP key events without changing the shared script.
- No ecosystem engine promotion requested; this remains a tool-local model as the spec directs.

#### Known limits

The historical specification provides formulas and claimed outputs, but no executable reference implementation. The explicit simultaneous conservative flows do not reproduce every historical range exactly. The report gives actual outcomes rather than repeating unverified historical numbers. The first ghost can take more than the requested 5 ms. Desktop headless timings do not establish Chromebook performance.

The selected gravel-ranger recording is not bundled. The kit uses browser speech. The first hint speaks once after a touch unless that touch stocked or fed the pond. Per the settled Refine call, plain event readings describe ice, low oxygen, winterkill, departures and vanished snails. Each has a 20-second cooldown, a four-second expiry and a current-state validity check. Read speaks the live instrument.

OpenStax's current page licence differs from the old spec. It and EPA/DNR are references only, with no source text, figures or data copied into the instrument. The Manual records current terms and original model provenance. No measured ecological dataset is represented.

#### Cold review changes

Review evidence uses review-prefixed files in Scratch. The model coefficients and conservative transfer order are unchanged. Energy labels now distinguish net production and use of stores. Open reconstructs the final chart snapshot after actions at the saved week. New/Open clear transient selection and movement accumulators. Shortcuts respect the open drawer and native confirmation dialog.

Specimen cells are trimmed to alpha bounds in the browser and fitted without changing their aspect ratio. Food-web arrows anchor to current hitboxes, with missing kinds labelled absent; Life inspection is also available with Enter on the tank. The heron stands clear of the calendar. The new generated shore atlas has four full-width seasonal strips, drawn as a background, never as model data.

New shore prompt and original PNG are in art/prompts.json and art/raw/pond-shores-v2.png. The built-in imagegen skill produced it. scripts/art.py --rekey still fails at its NumPy import in the supplied interpreter; bounded browser canvas encoding supplies the WebP without touching shared code.

The review also dates the latest log entry in Read, animates model-driven heron departures using the existing flight pose (stationary with Motion off), and fits all Net controls at compact landscape widths without removing icons. This last layout correction was confirmed by the single review audit and re-shot at affected widths.

Ghost traces retain long dashes. The Refine fix uses 0.35 alpha to distinguish these projections from the actual pond. Actual traces keep their original colours and dash patterns, with separate stem algae and optional shade histories.

Hidden chart chips keep full label contrast and use strike-through to indicate hidden traces. In Net mode the decomposer key reads Specks and explains that they cannot be netted, rather than promising a Net 1 action. The bundled source includes its MIT notice and links the original content licence. Final save-control verification covered Rename, cancelled/confirmed Delete, the eight-save cap and all New choices, and restored the review-profile fixtures.

#### Refine fix implementation

Seven dropdowns were replaced locally by detented rotary switches and a decomposer lever. Their values, defaults and existing shortcuts are preserved. Arrow keys and Home/End operate the switches; accessible value text follows the printed value. No shared kit code changed.

Snapshots now record separate floating and stem algae counts and average minnow shade. The optional shade trace uses its own 0 to 7 scale. Matter Enter and pointer taps both choose the nearest visible dot. The trip records weeks in the current pool and names decomposers on the direct muck-to-water transfer. Transfer weights and population equations are unchanged.

Flow records carry the existing transfer kind and an eater attribution solely to label Energy heat at the breathing eater, including digestion by ordinary eaters and fixed adult turtles and herons. Decomposers have their own heat arrow. These metadata do not change transfer amounts. Charts and the oxygen meter redraw on state changes, rather than every animation frame. Motion off also suspends idle tank drawing. A swipe computes its unchanged ghost once on release or cancellation.

At phone width the seven recorder keys use short names in two rows, keeping Stems, Shade and Whole run visible. Their full values remain accessible. The tray retains its specified scrolling row. The final mechanical audit is run once; any corrections from its leads have scoped follow-up frames instead of another full audit.

Fix evidence is under `_scratch/living-pond/fix-before`, `fix-after`, `fix-targeted`, `fix-voice` and `fix-audit`. `fix-model-parity.json` compares 27 habitat combinations for 520 weeks each against the pre-fix source, with zero population or oxygen drift.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
