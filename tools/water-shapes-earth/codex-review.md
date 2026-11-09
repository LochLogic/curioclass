# Codex review: water-shapes-earth
## Played
Confirmed S:\CurioClass-codex. Played as a solo Grade 9 student before reading builder notes/source, then checked the projection view.
All three benches: Plan, Run, Skip, Graph, Conclude, Compare and lab book, with held clicks and Sound on. The split is the best payoff.
## Findings fixed
- Blocker, general, Stream Table: no-transport sand still built a delta and a silt cloud. Deposits now require transported grains; only mixed includes suspended fines.
- Should fix, general, narration: Graph speech delayed or suppressed Conclude on the main path. Step switches hush old-screen speech; completed runs queue the next-action line.
- Should fix, general, lab book: a first tap could speak the freezer welcome over the book. It now speaks the book instruction, hushes stale speech, and makes the background inert until Close.
- Should fix, general, calm stream: grain positions still interpolated with Motion off. They now stay still until completion or a requested group preview; run timing is unchanged.
- Should fix, general, stacked Plan: the bench put every dropdown below the phone fold. The editable table now precedes the still bench; Run retains the large scene.
- Should fix, general, Compare: explanations repeated general facts instead of the actual manipulated variable. It now names a controlled pair, changed settings, means and mechanism.
- Should fix, general, storage: Run saved automatically before any storage notice. The lab-book button now says On this device.
- Should fix, general, completion: finishRun now rejects stopped/invalidated runs, preventing stale completion from entering the book.
- Polish, general, graphics: replaced the green-fringed jar, neutralized residual tint in its SVG presentation, and anchored it on the scale.
- Polish, general, graphics: shaded and textured the flat delta; put its low-contrast labels on a dark field plate.
- Should fix, general, compact stream: audit frames confirmed crowding captions and a slope card under group buttons. Captions now have a 15 px minimum line step; the compact slope card sits at lower left.
- Polish, general, claim input: added explicit aria-labelledby alongside the existing native label association.
- Should fix, general, scientific scope: notes now distinguish ideal pore saturation, invented rates, CO2-only temperature effects and simplified grain cutoffs from field measurements.
## Findings left
Should fix, spec source conflict: 32 mm pebbles at 1.50 m/s is not a verified rounding of Hjulström's table. Constants stay because the brief prohibits spec changes; teacher notes disclose the difference.
Browser narration remains the existing fallback; no recordings were commissioned.
## Break it
- Fairness: identical groups in every bench remain repeats, never Fair; two changed variables remain confounded. Real Run/Compare clicks confirm no causal endorsement.
- Crack gauge: all fills, rocks, liquids and cycle limits tested. Zero/oil stay zero, width stops at 1.00 mm, break cycles match the model.
- Mass readout: all water/rock/temperature combinations at minimum, eight and maximum weeks match the invented-rate calculation.
- Stream meter: all slope/flow/sediment combinations checked; low/0.25% moves nothing, medium/4% moves sand/gravel, flood/4% moves pebbles.
- Low-flow sand now has neither a delta nor silt. Mixed flood still produces sorted deposits. Grain movement uses trial 1, as its visible readout does.
- Noise: 318 numerical cases and 6,360 seeded noisy trials pass their baseline bounds; reseeding cannot set a score because no score or best record exists.
- Empty claim + Compare intentionally opens a worked example; it never marks the claim correct. Identical tests explicitly reject changed-cause inference.
- Repeated Run resets the experiment. Editing mid-run cancels and invalidates it; Skip after cancellation cannot save it. Group preview and mode change act immediately.
## Voice walk
Main path at default settings, held 120 ms clicks, 2 s spacing: Run, Skip, Graph, Conclude, Compare; repeat in Dissolve and Stream Table.
Spoken order after fixes: break, Graph how-to, Conclude how-to, Dissolve how-to, finished how-to, Stream how-to.
First Run suppresses the Freeze welcome as BASELINE 16 permits; its instructions remain in the hint/Read. The side path hears that welcome too.
Later Graph/Conclude visits stay silent. Old-screen speech stops on a step change. Read speaks the current hint and a mode switch releases it immediately.
| Line | Kind | Expected | Observed |
|---|---|---|---|
| fair | event | 5 repeated Runs | 5 starts |
| graph | how | once | 1 |
| conclude | how | once | 1 |
| dissolve, stream | mode how | once each | 1 each |
| finished | how | once | 1 |
| break | event | 2 completed runs | 2 starts |
| book | how | once over 5 opens | 1 |
| Read with Sound off | forced read | current hint | 1 |
The log verifies starts, cuts and ordering, not a human listening judgment or the gravel-ranger timbre. No fixed-line wording changed.
Final modal tests hear the book instruction first, block covered Run/mode controls and restore focus on Close. A natural Freeze-Thaw run reaches Run complete without Skip.
## Facts checked
- Ice expands about 9%: [USGS Water Density](https://www.usgs.gov/water-science-school/science/water-density). Spec density inputs independently give 1.090651 volume ratio and 0.916883 critical fill.
- Ideal 91.7% pore-fill argument: [FHWA-HRT-06-117, chapter 2](https://www.fhwa.dot.gov/publications/research/infrastructure/pavements/pccp/06117/02.cfm); not a universal rock threshold. Fagerlund's work concerns critical saturation of concrete.
- Crack rates/break cycle checks are explicitly invented spec constants: granite/sandstone/shale split at 50/20/13 cycles at full fill; sandstone 95% gives 0.795181 mm at 40 cycles.
- Normal rain about pH 5.6 due to CO2: [USGS pH and Water](https://www.usgs.gov/water-science-school/science/ph-and-water).
- CO2-bearing water dissolves carbonate into dissolved calcium/bicarbonate: [USGS WRIR 02-4045, table 3](https://pubs.usgs.gov/wri/wri024045/htms/table3.htm).
- Dissolution helps form caves/sinkholes: [USGS Natural Holes](https://eros.usgs.gov/earthshots/natural-holes); the tool does not say every sinkhole has this cause.
- Calcite limestone/marble and marble's recrystallized texture: [USGS recognition guide](https://pubs.usgs.gov/gip/acidrain/4.html). Granite's tiny rate and marble's 0.8 factor are lab assumptions.
- Gas solubility generally decreases as temperature rises: [OpenStax Chemistry 2e, 11.3](https://openstax.org/books/chemistry-2e/pages/11-3-solubility). The 1.2/1.5 loss multipliers are invented, not measured temperature laws.
- Dissolve arithmetic: 8-week cold CO2 limestone 15.20 g, granite 19.984 g; maximum modeled loss 7.20 g. Independent Python and browser checks agree.
- Manning relationship: [USGS WSP 2175](https://pubs.usgs.gov/wsp/wsp2175/wsp2175_vol2.pdf). Depth approximates hydraulic radius for a wide channel; n = 0.03 is the chosen model constant.
- All 12 speeds recomputed: medium/4% 0.904806, flood/1% 0.941036, flood/4% 1.882072 m/s.
- Grain thresholds/order: [Hjulström (1935), table 7 and figures 17-18](https://paleoarchive.com/literature/Hjulstrom1935-MorphologicalActivityRiversRiverFyris.pdf), printed pp. 295-298, downloaded and visually inspected. 8 mm: 0.81 m/s; 30 mm: 2.18-2.21 m/s. Exact tool cutoffs are model choices, not verified measurements for all three specified sizes.
- Already-suspended fines versus erosion from the bed are distinguished. Mixed material's cloud does not claim cohesive clay erodes at every speed.
- Water about 1,000 kg/m3 versus air about 1.2: [NASA Glenn atmosphere model](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/earth-atmosphere-equation-metric/); ratio 833.33, stated about 830 near sea level.
- Numerical rates/noise are simulation definitions. HS-ESS2-5 is practiced through manipulating one variable, repeated trials and evidence-based explanations, rather than a score.
## Sensitivity
None: material-property investigations, no cultural identities, hard history, religion or bodies. All 13 images contain no people; an unoccupied scientific bench fits this spec.
## Flattest moment left
Granite barely changes in Dissolve. That quiet control is scientifically useful; the readable scale and trial dots carry the difference. Compare was the flatter avoidable moment and is now plan-specific.
## Graphics
Inspected all 13 finished assets at output size and their scenes; replaced ws-jar via the built-in imagegen skill and art.py --rekey.
Kept the painted freezer, mineral textures, warm lab, glass, balance, tray and stone cutouts. Delta gains shading, deposition ridges and grain texture.
Compared with the existing Snowy Mail Route and Beat Lab bar frames. No simplification or new topic was introduced.
Art 419.18 KiB; bundle 674.61 KiB. The SVG neutralizes key tint on colorless glass; text/readouts remain in code.
## Audit
One full audit completed, exit 0, within its 40 minute cap, Chrome 9941 and host 8745. All 97 generated frames inspected, with full-size confirmation of the compact stream leads.
17 leads disposed: five caption/slope overlap rows fixed; one native-label false lead hardened with explicit ARIA; four region/scroller rows intentional; seven welcome omissions/cuts allowed by BASELINE 16.
The scene-region samples hit intentional group controls over an empty corner. Four-group phone scrolling is the spec's internal table scroller, with no page-wide overflow.
No runtime errors, lost focus, resize exceptions, stuck controls or infinite CSS animations. All repeated-click checks clean.
Wave lessons checked independently: current hint/Read, stable controls, 44 px targets, empty data shown unknown, group letters alongside colors, honest model labels, no scored giveaways, and controlled-investigation standards coverage.
The audit did not detect the book's wrong-screen speech or continuous SVG grain travel with Motion off; this review fixed both.
Final affected frames re-shot at every implicated size, all inspected, zero console errors. Claim association verified at all eight sizes; stream spacing/card at 680, 800, 1000 and 1366.
Main-path and modal voice checks re-run; Copy table and Clear both succeed. Motion-off stream stays static while its 15-second run remains active. No second full audit.
## Left open
- Browser fallback cannot guarantee the specified gravel-ranger timbre; recordings remain a later pipeline step.
- Spec conflict: replacing the 1.50 m/s pebble cutoff with the original table's approximately 2.2 m/s for 30 mm would prevent the specified 1.88 m/s flood from moving those pebbles. Resolve size/cutoff/outcome together in the spec; no unauthorized substitute made.
- No unattended questions: kept invented rates as the spec leans toward, and preserved Motion-off timing under STANDARDS rather than the spec's instant-run wording.
- Phone Plan prioritizes editable controls before the still bench. The full illustrated Run remains unchanged in focus.
- No commits; changes confined to the named tool and Scratch.
