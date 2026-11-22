# Finish fix: science-grade-2 (COURSE-RUN stage 7, 2026-11-22)

One fix pass over the eleven finish reports. Each report now ends with "Fixes applied (2026-11-22)", one line per finding.

## Counts per report

| Report | Applied | Rejected | Left |
|---|---|---|---|
| answer-key checks | 6 (plus M57b) | 1 (B58b alternative) | 4 minor notes (no change asked) |
| answer-key u01 | 7 | 0 | 1 |
| answer-key u02 | 5 | 0 | 1 (record C, lead's call) |
| answer-key u03 | 6 (plus printing) | 0 | 0 |
| answer-key u04 | 8 | 0 | 2 (E17 tag fits; picture watch) |
| answer-key u05 | 7 | 0 | 0 |
| answer-key u06 | 8 | 0 | 0 |
| answer-key u07 | 4 | 0 | 0 |
| safety | 25 | 0 | 2 (sand data sheet; unit sheet links) |
| sensitivity | 9 (M1 to M3, L1 to L6) | 0 | 2 (For Cory) |
| cold read | 10, 3 of them in part | 0 | 4 (parts of 7, 8, 10; 13) plus the known gaps |

US spelling: 139 replacements (color, gray, mold, neighbor, labeled, modeled, modeling, recognizable, practice) across the course's pages and days.csv, errors.csv, handbacks.csv and parts.csv. items.csv had none. A rescan finds none left.

## Safety page

courses/science-grade-2/safety.md, 889 words. It covers the stop rule, eye protection with ratings (splash goggles marked Z87 and D3; impact marked Z87), hand washing, allergies (plants, foods, stings, mold, latex), plants, soil and mold, outdoor looks and adult ratios, heat and lamps, electricity, magnets (none used), small parts and string, glass and sharp edges, and clean-up. Each rule names its days. DEFAULTS.md has a line naming the page. Sources U17 to U19 (two association pages and one state education department page) were opened and marked checked: 2026-11-22.

## Gates

- plan.py check science-grade-2: 17 FAIL before the rights fix, 17 FAIL after it (16 FAIL before this pass).
  - 16 are the known "section N.N not in data/units.csv" lines.
  - 1 is new: "s02-E11 and s02-E12 use the same numbers". They are one assessment case on the day 25 packet, and E12's stem now states its data, as the u02 reader asked. Left as a template point.
- lesson.py check (course lines): 0 FAIL and 20 NOTE, both before and after.
- Gate note for the lead: the whole-repo runs of plan.py check and lesson.py check crash on science-grade-1 ("TypeError: keywords must be strings", plan.py line 1020). That course is not mine, so I did not touch it. I ran plan.py with `check science-grade-2`, and lesson.py through a small wrapper (in my tmp folder) that keeps only science-grade-2 day files. Both run the same checks.

## For Cory

1. Mount St. Helens on day 12. The teacher line now answers "yes, some people were" hurt, with no number. Options:
   - (a) Keep it with no number. My pick.
   - (b) State the death count once the browser check on U21 confirms it.
   - (c) Drop the line.
2. Grounding for the M2 and L2 wording (a child telling a real disaster story; the family sit-out). Options:
   - (a) Keep the wording as written. My pick.
   - (b) Ground it on the four refused pages (Red Cross, SAMHSA, Head Start family engagement, USDA food stigma) after a browser read.
3. Day 46 argument table (cold read 8). Options:
   - (a) Keep four records with ten points and the scribe limit. My pick.
   - (b) Cut to three records and turn the say items into pair talk. This changes unit 4's scored design.
4. Day 45 minutes (cold read 13): the day runs 38 minutes against a scope of 35. Options:
   - (a) Set the scope to 38, inside the course's 35 to 40 frame. My pick.
   - (b) Trim a block from day 45.

## For the lead: sweep

- UK spellings across all seven units and days.csv (day stage, plan stage). Worth a scan in sister courses.
- Soil source mismatch: materials.csv "untreated soil (household stand-ins)" against unit 5's sterilized soil (plan stage).
- Outdoor looks had no second adult or site sweep (unit plan stage, units 1 and 7).
- Unit 6 scored only the jay case, so pollination was unscored (unit plan stage). Day 62 was typed Fluency but teaches (plan stage).
- Hand washing deferred with no time on days 50 to 55 (day stage).
- Ledger: if the ledger records unit 6's scored evidence, s06-E11 is now scored and s06-E8 is unscored practice. If it records day kinds, day 62 is now Application. I ran no ledger command.

## Left

- Cold read 7 (other 4.1 exits): each already asks a spoken reason.
- Cold read 10 (day 10 minutes): 37 is inside the frame.
- Known gaps: APPROACH-SCIENCE.md, the course family note and the supplies list are listed by the rubric and not built here.
- u01 finding 8: the day 10 retry packet against the unit plan line is the lead's to reconcile.
- u02 record C: a design choice for the lead.
- Safety: one sand data sheet (lead). The unit sheets do not link the safety page, because they are child pages.

## Browser check

- https://www.britannica.com/place/Mount-Saint-Helens (403): sources.csv U21. Fact: people died in the 1980 eruption, behind the day 12 teacher line "yes, some people were". I tried USGS pages U16 and U20, and neither states it.
- From the sensitivity report, no course fact rests on these:
  - https://www.redcross.org/get-help/how-to-prepare-for-emergencies/disaster-and-children.html
  - https://www.samhsa.gov/find-help/disaster-distress-helpline/disaster-types/children-youth
  - https://eclkc.ohs.acf.hhs.gov/family-engagement/article/head-start-parent-family-community-engagement-framework
  - https://www.fns.usda.gov/cn/school-meals-stigma
