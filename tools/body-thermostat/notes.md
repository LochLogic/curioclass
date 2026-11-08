## What it teaches

Students conduct controlled model experiments to explain how negative feedback maintains core temperature.
They use paired temperature traces to separate the effects of sweating, skin vessels, shivering and a changing set point.

## Key skills

- Change one variable while holding the others steady.
- Read temperature and time from a graph.
- Compare evidence with and without a response.
- Explain a difference between current temperature and the target temperature.
- Recognize what a model leaves out.

## Support at home

- Talk about why the same air feels different when you rest or walk. Use ordinary observations, without testing extreme heat or cold.
- Notice why damp clothes feel different from dry clothes, and connect that to evaporation.
- Ask your child to describe a thermostat's sensor, target and response using your home's familiar controls.

## A 5-minute start

Choose Shorts, Run and Play in Lab. Pause after a few simulated minutes and identify the responses.
In Experiment, run a trial, switch Sweating off, and run another. Press Compare and explain why the traces separate.
Use Fever starts in Fever mode to distinguish a higher target from colder surroundings.

## Modes

- Lab: steer a live model. Reset clears its temperature trace. At 5 min/s, one simulated hour takes 12 real seconds.
- Experiment: each Run trial freezes its starting conditions, computes up to 60 minutes, and reveals the trace over two seconds.
  Select any two trial numbers, then Compare. A dashed second trace remains identifiable in grayscale.
  The notebook is page-only and disappears on reload. Interrupted reveals still retain the complete computed row.
- Fever: holds the environmental conditions from Lab. Fever starts raises the target to 38.5°C; Fever breaks returns it to 37°C.
  Returning to Lab restores a 37°C target. Fever remembers its own target.

## Talk questions

What changed between your trials? What did you hold constant?
Why does a body at 37°C shiver when the target becomes 38.5°C?
Can the air deliver heat to the body instead of taking heat away?
What can this model explain, and what would require a real investigation?

## Good to know

This teaches HS-LS1-3 through the student's own paired investigation. It models a 60 kg body, not an individual person.
Its gains, insulation, wind factors and activity heat rates are model assumptions. It omits breathing losses, sunshine,
hands and feet and changing water supply. No model output predicts how long a person can safely stay in a setting.
The simulation stops at 35 or 40°C; those are model stop limits, not instructions to wait for those temperatures in real life.
CDC lists 103°F or higher as one heat stroke sign, alongside other symptoms; a temperature alone is not a diagnosis.
The help messages distinguish model limits from diagnosis. Suspected heat stroke requires emergency care and immediate cooling; hypothermia needs urgent medical help (CDC). This is not a complete first-aid lesson.
Content about bodies and fever needs the sensitivity review described in handoff.md.

## Sources

- NIH MedlinePlus, Body temperature norms: https://medlineplus.gov/ency/article/001982.htm
- CDC, Definitions of Signs, Symptoms, and Conditions of Ill Travelers:
  https://www.cdc.gov/port-health/php/definitions-symptoms-reportable-illness/
- CDC, Preventing Hypothermia: https://www.cdc.gov/winter-weather/prevention/index.html
- CDC, Heat Related Illnesses: https://www.cdc.gov/extreme-heat/media/pdf/Heat_Related_Illness.pdf
- OpenStax Anatomy and Physiology 2e 24.6, Energy and Heat Balance (source consulted for facts):
  https://openstax.org/books/anatomy-and-physiology-2e/pages/24-6-energy-and-heat-balance
- Source cross-check for fever's raised target: NCBI Bookshelf, StatPearls, Physiology, Fever,
  https://www.ncbi.nlm.nih.gov/books/NBK562334/
- ASHRAE Handbook Fundamentals (2021), ch. 9:
  https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch09/F21_Ch09_si.aspx
  The chapter lists body specific heat as 3490 J/(kg K), while this tool follows the spec's 3470 as a model constant.
  The chapter rounds evaporation heat at 30°C to 2.43 million J/kg; the spec uses 2.426 million.
- 2024 Adult Compendium of Physical Activities, https://pacompendium.com, provenance cited by the spec.
  Its current running table lists general jogging at 7.5 MET and running at 6 to 6.3 mph at 9.3 MET.
  The spec uses 7 and 9.8; this tool keeps its prescribed activity watts as model assumptions, not measured teen values.

## Media

Illustrations generated with OpenAI gpt-image, edited for Curio Class. Eight assets, no people in painted art.
Fixed narration text is prepared for soft-breath. No audio was recorded during this build; browser speech is the current fallback.

## Cold review changes

Run trial pauses the separate live clock; recorded trials retain their original conditions.
The comparison caption gives the temperature difference at the last time both trials reached.
Identical and multiple-change comparisons still identify their limitations. A stopped trial shows CDC-based safety context.
