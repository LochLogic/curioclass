Fixed: Unit 02 assessment 1. Calendar notes, scope and sequence, and day list now exclude days 18, 19 and 23 from scoring. Day 45 uses revised days 37 and 44 evidence and fresh items.

LEFT: Unit 03 sources 1. The [published alignment list](https://im.kendallhunt.com/HS/teachers/1/modeling_prompts/4/preparation.html) is verified and already recorded correctly in s03.md. The false source-map.csv record remains because that file is outside the edit whitelist.

Fixed: Unit 05 assessment 1. Days 66, 94, 98 and 100 remain practice. Calendar notes and scope and sequence now match field 5’s eligible revised records and fresh day 106 items. Day 105 is formative. Course days, boundaries and day kinds remain unchanged.

LEFT: A regeneration mistake required reconstructing exit and instrument rows in s02.md and s05.md. A person must compare those rows with their original versions.

`python -X utf8 scripts/plan.py check algebra-i`: PASS, 0 failures.

`python -X utf8 scripts/unitplan.py check algebra-i`: PASS, all seven unit plans.
