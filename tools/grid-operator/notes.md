## What it teaches
Students test competing electricity fleets and use cost, reliability and fuel CO2 evidence to explain their tradeoffs. They distinguish megawatts of power from megawatt-hours of energy and see why demand must be met each hour.

## Key skills
- Read a supply stack against a changing demand line.
- Compare a paid-off fleet with the weekly cost of new capacity.
- Use stressful weather and outages to test a design.
- Explain storage losses and the difference between power and energy.
- Support a design choice with three separate measures.

## Support at home
- Talk about which household activities use electricity at the same time and which could happen at another hour.
- Discuss why a low-cost plan might still be a poor choice if it cannot keep lights on.
- Watch the weather together and predict how sunshine or still air could affect a city's power supply.

## A five-minute start
Save the base fleet as Plan A. Retire both coal units, save Plan B, then compare Spring and Heat wave. Ask students to explain the cost reduction and the shortage before building a replacement fleet.

## Modes
Plan sets the existing fleet, new capacity and battery charging policy. Nuclear additions use small modular reactor costs. Retire affects existing capacity only; new construction remains until removed with the minus stepper.

Run dispatches 168 one-hour intervals. Coal is committed for the week, with a 40 percent minimum. Spring has mild demand; Heat wave trips a fossil block from Wednesday 15:00 onward; Still winter week reduces combined cycle capacity to 70 percent on Wednesday and Thursday. Play starts immediately. Pause holds the current hour; Step hour pauses and advances once. Skip computes all remaining hours.

At the end of a week, Scorecard in the Run toolbar reopens the report. Replay or a new week restores Step hour.

Compare automatically runs all three weeks for each saved plan, with retained coal committed on. Weekly Run toggles are experiments and are not saved fleet settings. Load a saved plan to revise it. Four plans persist on this device only; Clear saved plans removes them. Reset retains saved plans.

## Talk questions
- What evidence makes a design reliable across all three weeks rather than just Spring?
- Which new capacity most changes the heat-wave shortage, and what does it cost?
- Why might storage reduce curtailment in Spring yet barely affect winter CO2?
- Why is cheapest per MWh served not enough to choose a fleet?
- Which omitted factors would matter before making a real energy decision?

## Good to know
This is an invented island grid with no imports, about half a million residents, and peak loads of 770, 1,000 and 900 MW. Forecasts are perfectly known. The three weeks are teaching scenarios, not measured city records.

Build inputs are 2022 dollars. Coal and gas fuel inputs are 2024 prices, while nuclear fuel uses the EIA Annual 2025 value. Costs compare designs, not bills. Capital uses the supplied 7 percent annuity factors over 30 years, or 15 years for batteries. Fixed upkeep applies to all retained and added capacity. The shared nuclear upkeep uses the AEO2023 large-reactor row even for new SMR builds, an explicit simplification retained from the spec.

Battery efficiency is 85 percent on charge, with loss counted when charging and one-to-one discharge. Each 100 MW block holds 400 MWh and begins every week half full. Default charging uses only the renewable portion of surplus. Gas charging is limited to spare combined cycle capacity from 00:00 through 05:00 and pays its fuel cost and emissions.

Wind and solar share counts accepted generation, including generation sent to storage. Battery discharge is not counted again as wind or solar. Initial half-full storage is an explicit model assumption. Zero service gives an undefined per-MWh value, shown as n/a, and cannot win lights-on challenges.

Fuel CO2 is not lifecycle emissions. Nuclear, wind, solar and battery discharge have zero direct fuel CO2 in this model. The omitted factors are power lines inside the city, start-up costs, ramp limits, spinning reserves, maintenance outages, water use, land use, mining and fuel supply chains, and emissions other than CO2 from burning fuel. Unserved energy is not assigned a dollar price.

## Sources
- [EIA AEO2023 technology costs, Table 1](https://www.eia.gov/outlooks/aeo/assumptions/pdf/elec_cost_perf.pdf): build and upkeep inputs, 2022 dollars.
- [EIA Electric Power Annual](https://www.eia.gov/electricity/annual/): heat rate and existing nuclear operating inputs.
- [EIA Annual Table 7.20](https://www.eia.gov/electricity/annual/html/epa_07_20.html): 2024 US natural-gas delivered price of $2.77 per MMBtu.
- [EIA Electric Power Monthly](https://www.eia.gov/electricity/monthly/): historical fuel prices and 2024 capacity factors.
- [EIA emissions coefficients](https://www.eia.gov/environment/emissions/co2_vol_mass.php): 116.65 pounds CO2 per MMBtu for natural gas.
- [EIA CO2 per kilowatthour FAQ](https://www.eia.gov/tools/faqs/faq.php?id=74&t=11): coal coefficient, 2.31 pounds per kWh.
- [FERC and NERC Elliott inquiry](https://www.ferc.gov/news-events/news/ferc-nerc-release-final-report-lessons-winter-storm-elliott): final report released November 7, 2023; context for cold-weather gas constraints.

Narration uses the browser fallback until firm-captain recordings are made in a later authorized workflow. No audio was recorded in this build.
