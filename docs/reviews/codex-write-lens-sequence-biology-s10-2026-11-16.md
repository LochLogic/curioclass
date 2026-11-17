1. [Field 8 and day 153] The tool schedule omits day 153, but the timing table requires 24 minutes of digital file revision | Required revision work conflicts with the listed tool days | Add day 153 to field 8's tool allocation; ask the lead to align days.csv and regenerate its tables.
2. [Day list, day 143] A Fluency day introduces cell entry, formulas and a multistep procedure | First instruction is classified as practice | For the lead: change day 143 to Understanding in days.csv and regenerate the header and day list, giving five understanding days and one fluency day.
3. [Field 4] Readiness response specifies an affected group without the whole-class threshold | It omits UNIT-PLAN rule 6's response when more than a third miss an item | Specify whole-class repair above that threshold and small-group repair otherwise, within the existing ten minutes.

Gate: `python -X utf8 scripts/unitplan.py check biology` passed, including s10.md.
Count: 3 findings (lens sequence).
