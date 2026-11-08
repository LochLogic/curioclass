## What it teaches

Students plan controlled investigations and use repeated-trial evidence to explain how water breaks, dissolves and moves Earth materials. They connect each measured change to expansion on freezing, dissolved carbon dioxide or the force of moving water.

## Key skills

- Change one variable while holding the others constant.
- Compare three trial results with a group mean.
- Distinguish model assumptions from measured natural rates.
- Support a claim with numbers and a property of water.

## Support at home

- After rain, look from a safe path for sand collected where runoff slowed. Ask why it collected there.
- Look for cracks in exposed rocks or pavement. Discuss how trapped water could expand when frozen, without assuming every crack has that cause.
- Notice a smooth river stone and discuss how moving water can carry and sort rock pieces. No collecting or entering water is needed.

## A 5-minute start

1. Turn Noise off and press Run in Freeze-Thaw. Groups differ only in crack fill.
2. Watch C split. Compare its gauge with A and B, then open Graph.
3. Open Conclude, write a claim, and press Compare. The model answer uses the plan that was actually run.
4. Return to Plan and use vegetable oil as a control liquid. Keep every other variable the same.

## The three benches

Freeze-Thaw: sandstone starts at fills 50%, 95% and 100%, over 40 cycles. Each cycle takes a quarter second; trials stop when added crack width reaches 1.00 mm. Default no-noise results: 0.00 mm, 0.80 mm and a split at cycle 20. The last gauge records the split threshold, not continued widening after failure.

Dissolve: each chip starts at 20.0 g. Compare distilled, rainwater and CO2-rich water. Calcite is the main mineral in limestone and marble. Cold water holds more dissolved CO2 in this model, increasing loss for rainwater and CO2-rich water. Granite barely changes. The Conclude card connects dissolved calcium and bicarbonate to caves and sinkholes.

Stream Table: compare slope, flow depth and sediment. Manning's equation uses roughness n = 0.03 and hydraulic radius approximated by depth in a wide channel. Water speeds are in meters per second. Sand, gravel and pebbles need about 0.20, 0.80 and 1.50 m/s to begin moving. Mixed sediment shows the largest transported grains settling closest to the mouth, followed by smaller grains and a silt cloud in still water.

## Talk about it

- Why is a nearly full crack different from a half-full one?
- Which pair of groups can support a causal claim? Which cannot?
- Why can a chip lose mass without disappearing as visible crumbs?
- How can two streams with different slopes have similar speeds?
- Which result would you repeat with Noise off before making a claim?

## Good to know

This tool supports HS-ESS2-5 through students' own controlled investigations, repeated measurements and explanations of water's properties. It is an educational model, not a prediction of weathering times in nature.

Freeze and dissolve rates are invented, ordered lab rates. Expansion uses the rounded critical fill 0.917. Real frost damage also involves ice lenses drawing in water; that mechanism is outside this model. Oil produces no widening in this model. Rock saturation is simplified to a single crack's fill.

Noise multiplies each trial's model rate by a seeded normal factor with standard deviation 5%, clipped to ±10%. Run again creates a new seed. A frozen block's final width is capped at the split threshold. Dissolve noise applies to mass loss, so remaining mass is not varied by an arbitrary percentage of 20 g.

The fair-test checker compares every pair of groups. Identical groups are labeled as the same test, not as a one-variable comparison. Run remains available for unfair plans and records their fairness in the lab book.

Motion off removes movement but preserves run timing under the standing Curio Class standard. Skip to end is always available while running. Space starts a run outside text fields and controls. Tab navigates controls; Enter opens plan dropdowns. Graph arrows move between Run, Graph and Conclude. All controls remain live during playback.

Completed plans and results save only on this device, with try/catch storage fallback. Claims remain in the open session only, including the session-claim column in Copy table. Clear lab book removes saved entries. Copy table is a local clipboard convenience. No network requests or analytics are made.

The requested gravel-ranger voice is specified in voice/lines.json. Build does not record narration; the kit uses browser speech until recordings are supplied.

## Sources and model constants

- USGS Water Science School, [Water Density](https://www.usgs.gov/water-science-school/science/water-density): ice is less dense than water and expands about 9% on freezing. The spec's density inputs 0.9998 / 0.9167 give the model volume ratio 1.09065.
- Fagerlund (1977), Materials and Structures 10:217: critical degree of saturation and frost damage.
  [FHWA-HRT-06-117, chapter 2](https://www.fhwa.dot.gov/publications/research/infrastructure/pavements/pccp/06117/02.cfm)
  explains the ideal 91.7% pore-fill argument. It is not a universal threshold for natural rocks.
- USGS, [pH and Water](https://www.usgs.gov/water-science-school/science/ph-and-water), and Sinkholes: rain pH about 5.6, carbonate dissolution and karst.
- OpenStax Chemistry 2e, 11.3 Solubility: gas solubility decreases as temperature rises.
- USGS Water-Supply Paper 2175 (1982): Manning flow relationship.
- Hjulström (1935), Bulletin of the Geological Institute of Uppsala 25:221: grain thresholds, rounded here.
- NASA Glenn Research Center, Earth Atmosphere Model: air density about 1.2 kg/m³. Water / air ≈ 833.

The exact rock rates, temperature multipliers and grain thresholds are teaching-model assumptions, not measured universal constants.
Hjulström separates erosion from continued transport: fine silt and clay already in suspension can remain aloft at low speeds;
this tool does not model lifting cohesive clay from the bed. Mixed sediment includes that pre-suspended fine material.
The 0.20, 0.80 and 1.50 m/s cutoffs are the spec's rounded choices, not exact values established by the original curve.
The [original Hjulström paper](https://paleoarchive.com/literature/Hjulstrom1935-MorphologicalActivityRiversRiverFyris.pdf),
table 7 on page 295, lists 0.81 m/s for 8 mm grains but 2.18-2.21 m/s for 30 mm grains.
Its page 296 describes a broad, preliminary erosion zone, with depth and grain-size qualifications.
The spec's 1.50 m/s cutoff for 32 mm pebbles is therefore a chosen teaching threshold, not a verified rounding of that table.
It remains unchanged here because changing it would change the specified stream outcomes.
The cold-water multiplier isolates CO2 solubility; real dissolution also depends on reaction kinetics, water chemistry and exposed area.
The oil control means no modeled widening, rather than a measured prediction for every vegetable-oil mixture.

Compare names a pair that changes exactly one variable and connects its actual means to that variable.
Identical tests are repeats, not evidence of a changed cause; a confounded plan never receives a causal endorsement.
There is no score or automatic judgment of the student's claim. Compare is a worked example, available with an empty claim.
