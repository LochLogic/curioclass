# Ocean Conveyor

## One idea
On a model globe with a heating slider (more sun at the equator, less at the poles), a spin switch (on by default) and a dye dropper, the student turns spin off and watches warm air rise at the equator and flow straight toward the poles, then turns spin on and sees the flow bend into three bands of wind in each hemisphere (trade winds, westerlies, polar easterlies); dye dropped in the oceans traces the wind-driven gyres and the Gulf Stream carrying warm water north; cooling and salting North Atlantic water makes it sink and starts the slow deep conveyor, shown on a side-view slice; at the end a climate panel pairs two coastal towns at about the same latitude, Plymouth in southwest England and Cartwright on the coast of Labrador, whose January temperatures differ by about 21 degrees Celsius, and the student explains the gap with the model, so a sixth grader learns how unequal heating and Earth's rotation cause patterns of air and ocean circulation that shape regional climates.

## Not like
- raindrop-s-journey (6, concept): one water molecule's path through the water cycle. Here whole-planet flows.
- climate-postcards (3, spec): describing climates from data. Here what causes the differences.
- feedback-loop-builder (9, spec): climate feedbacks. Here circulation itself.
- biome-atlas (12, spec): biomes from climate. Here where the climate comes from.

## Who and how
- Grade 6, Science, module "Climate and Ocean Circulation". Standard: MS-ESS2-6 (develop and use a model to describe how unequal heating and rotation of the Earth cause patterns of atmospheric and oceanic circulation that determine regional climates).
- Format: simulator. Driver: one student alone, or a teacher leading the class (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- The globe with heating slider, spin switch and dye dropper; the side-view slice; four steps (heat, spin, dye, sink); the climate panel with one city pair. Extra: What if (a slower spin, or North Atlantic water that stops sinking). tool.json `modes: ["Globe", "What if"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS2-6 (unequal heating) | Move the heating slider with spin off | air rising at the equator, sinking at the poles | 2 |
| MS-ESS2-6 (rotation) | Turn spin on and drop dye | wind bands bending; ocean gyres | 3 |
| MS-ESS2-6 (regional climate) | Sink cold salty water, then explain the city pair | the conveyor on the slice; the climate panel | 4 |

## Screens and modes
Header (kit): title "Ocean Conveyor"; `Globe`, `What if`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A globe on a stand, the sun to one side. Three controls: the heating slider, the spin switch (on), the dye dropper. The welcome is queued (`welcomeAfter: true`): "The sun warms Earth unevenly. Watch what that does to the air and the sea. Turn the spin switch off first." First hint: "Tap the spin switch to turn it off."

**Step 1, heat (focus: the air).** At 1366x768 the globe fills the left with the side-view slice right; at 680x425 the slice is a sheet. Spin off, the student drags the heating slider up; arrows show warm air rising at the equator, flowing toward the poles high up, sinking and coming back near the ground. A thermometer at the equator and at a pole shows the gap.

**Step 2, spin (focus: the wind bands).** Spin on: the same arrows bend. In each hemisphere three bands appear with names: trade winds from 0 to 30 degrees, westerlies from 30 to 60, polar easterlies from 60 to 90. A note: "Spin doesn't push the air. It turns the ground under it, so the path looks bent."

**Step 3, dye (focus: the ocean).** The student drops dye in the North Atlantic and the North Pacific. Winds drag the surface water into big loops (gyres). The Gulf Stream and North Atlantic Current carry warm water toward northwest Europe; the Labrador Current carries cold water south along Canada.

**Step 4, sink (the deep conveyor).** Near Greenland the student taps `Cool` and `Add salt` (salt is left behind as sea ice freezes). The water gets denser and sinks on the slice, flows south along the bottom and rises far away. A note: "One trip around the deep conveyor takes about a thousand years."

**The climate panel (the aha).** Two postcards: Plymouth, England (about 50 degrees north) and Cartwright, Labrador (about 54 degrees north). January averages about 7 degrees Celsius and about minus 14. The student picks the reasons from the model (the warm current and the westerlies blowing off it; the cold current and winds off the land) and writes one sentence. Narrator: "Same distance from the equator, very different winters. The sea and the wind carry the difference."

**The end.** The globe with all four steps on, the slice and the explanation. `Print` prints them.

**What if (extra).** Slow the spin (wider bands) or stop the sinking (the North Atlantic current weakens and Plymouth's postcard cools). A note says this is a model, not a forecast.

## Content
- A simple circulation model (three cells per hemisphere), wind bands, five gyres, the Gulf Stream and Labrador Current, the sinking switch, one city pair with 1991-2020 January normals, the explanation card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each step unlocks the next control; earlier controls stay live.
- Keyboard: Tab to the slider, spin switch, dropper, `Cool`, `Add salt`, the postcards and the reasons; Enter acts, arrows move the slider.
- With Motion off arrows and dye show as still paths and the globe doesn't turn.

## Look
- Accent `--brand` #0b5a7a current blue (header, current arrows, the slice frame); gold #f4c542 (warm water, the control in use); paper #eef6f9; ink #06202b; muted #4a5b63.
- Contrast (WCAG 2.1, computed): white on brand 7.61:1; brand on paper 6.96:1; ink on paper 15.36:1; muted on paper 6.46:1; ink on gold 10.34:1.
- Never color alone: warm and cold currents carry "warm" and "cold" labels and different arrow styles.
- Different from this batch (schoolyard brick, cell green, strata plum, magma red).

## Art
- Local FLUX (`scripts/localart.py`): a Plymouth harbor postcard in January (1, 4:3), a Cartwright coast postcard in January (1, 4:3).
- Drawn in code: the globe, wind arrows, gyres, dye, the slice, thermometers.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `news-reader` as the weather desk on the climate panel; `calm-professor` as the model guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `heat`: "Drag the heating slider up."
- how `spin`: "Tap the spin switch to turn it on."
- how `dye`: "Tap the dropper, then tap the ocean."
- how `sink`: "Tap Cool, then Add salt."
- event, whole, each step's result.
- how `explain`: "Pick the reasons, then write one sentence."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the circulation model, gyres, the slice. City normals sit in a marked block `/* OCEAN-CONVEYOR DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Steps | Skip to the climate panel | The panel opens only after all four steps run. |
| Reasons | Pick "Plymouth is farther south" | It's farther south by only about 3 degrees; the card shows the latitudes and asks again. |
| Sentence | Copy a reason | The sentence needs a current and a wind. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `heat`.
2. Step result (whole), waits. `spin`; `dye`; `sink`.
3. `explain`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS2-6 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Three circulation cells and wind bands at 0, 30 and 60 degrees | NOAA National Weather Service JetStream, "Global Circulations" | UCAR Center for Science Education, "Global Atmospheric Circulation" | yes |
| Wind drives surface gyres; the Gulf Stream carries warm water north | NOAA Ocean Service, "Ocean Currents" | NASA Earth Observatory, "Ocean Motion" | yes |
| Cold, salty North Atlantic water sinks and drives a deep conveyor taking about 1,000 years | NOAA Ocean Service, "The Global Conveyor Belt" | Woods Hole Oceanographic Institution, "Ocean Circulation" | yes |
| Plymouth January mean about 7 C (1991-2020) | Met Office, UK climate averages, Plymouth Mountbatten | NOAA NCEI, WMO 1991-2020 climate normals | yes |
| Cartwright January mean about minus 14 C (1991-2020) | Environment and Climate Change Canada, Canadian Climate Normals | NOAA NCEI, WMO 1991-2020 climate normals | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-10): Cartwright is 3.3 degrees farther north than Plymouth; a 7 C and minus 14 C pair is a 21 degree gap; three 30-degree bands make 90; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 globe and slice; at 680x425 sheet.
2. Unequal heating with spin off shows rising and sinking air. (MS-ESS2-6)
3. Spin on bends winds into bands and dye shows gyres. (MS-ESS2-6)
4. The conveyor sinks on the slice and the city pair is explained with a current and a wind. (MS-ESS2-6)
5. The city normals match the cited 1991-2020 records within 1 degree.
6. The model and What if notes say it is a model, not a forecast.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still paths; no network requests.

## Open questions
- The idea card flags a data source (default used: Met Office and Environment and Climate Change Canada 1991-2020 January normals for Plymouth and Cartwright, checked before build; values shown rounded to whole degrees).
