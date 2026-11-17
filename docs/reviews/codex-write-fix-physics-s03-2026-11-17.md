Updated only [physics/s03.md](docs/courses/physics/s03.md). Merged findings: five, with no duplicates.

1. Fixed item 1b: the final point requires both force and field directions to reverse, with both magnitudes unchanged.
2. Fixed item 1e: scoring requires a correct numerical field calculation, units, direction and specific comparison evidence. Rewrote the meeting sample.
3. Fixed error M: kept central-body transfer under M and appended Q for unchanged coefficients after unit changes. Updated diagnostics, repairs and response allocation.
4. Fixed the mission-history locator to printed page 165, retaining “Back to Earth.” Verified against the [source](https://www.nasa.gov/wp-content/uploads/2023/04/sp-4231.pdf).
5. Rejected the proposed day 40 reclassification within this file: UNIT-PLAN requires day kinds to come from days.csv and prohibits hand-editing the generated day list.

For the lead: the day 40 sequencing concern remains valid. Changing its kind requires a separately authorized days.csv correction and regeneration.

`python -X utf8 scripts/unitplan.py check physics` passed all ten plans, including s03.md. UTF-8, LF endings and absence of em dashes verified.
