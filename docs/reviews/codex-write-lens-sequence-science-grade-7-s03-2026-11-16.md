1. [Fields 4, 8 and day list] The generated list differs from days.csv on days 43, 55, 58, 59, 61 and 63 to 65: readiness minutes, image and gas evidence, prerequisite reuse and scoring dates disagree. | Teachers receive conflicting schedules and evidence requirements. | For the lead: reconcile these CSV rows with the plan’s stated corrections, then regenerate the day list; the fixer must not edit generated rows by hand.
2. [Field 8] Days 54, 63, 65 and 66 allocate all 50 minutes without accommodating the required two-minute card cleanup. | Following both instructions requires 52 minutes. | Reserve cleanup explicitly: day 54, shorten the unscored supporting prompt from ten to eight minutes; day 63, use 28 minutes revision plus two cleanup before the 20-minute item; day 65, shorten completeness checking from five to three; day 66, shorten anchor revision from 15 to 13. Refer the day 63 ledger adjustment to the lead.

Check: `unitplan.py check science-grade-7` passed s03.md with no failures or notes.

Count: 2 findings (lens sequence).

## Files changed outside the allowed set

- data/plans/unit-rejections.csv
