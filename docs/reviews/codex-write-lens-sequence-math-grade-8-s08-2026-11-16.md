Gate: `python -X utf8 scripts/unitplan.py check math-grade-8` passes s08.md without notes.

1. [Field 2; day list, day 141] Field 2 teaches expression estimation on day 140, but day 141’s generated note introduces it on a fluency day | The calendar contradicts the teaching sequence and fluency designation | For the lead: change days.csv day 141 to rehearse expression estimation already taught on day 140, then regenerate the day list.
2. [Field 3; day list, day 153] Day 153 allocates zero major-work minutes despite requiring five minutes of previously taught 8.EE.C.7 practice | The stated cluster allocation omits required major work | For the lead: allocate five major minutes on day 153 in days.csv and regenerate; update field 3 from 550/800, 68.75 percent, to 555/800, 69.375 percent.

Count: 2 findings (lens sequence).

## Files changed outside the allowed set

- docs/COURSES-STATUS.md
