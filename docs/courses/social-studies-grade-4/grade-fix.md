# Grade 4 social studies draft baseline repair

November 24, 2026. Internal runner handoff, not a teaching-readiness claim.

Reviewer first: examine the 58 retained template findings below, the six existing browser-check source rows, and the workload of the long assessment packets on days 102, 120, 131 and 159. The native lesson gate and print coverage remain unavailable in this environment.

## Gate evidence

| Check | Before | After |
|---|---:|---:|
| Unit-plan gate | 1 | 0 |
| Grade 4 ledger structural and citation problems | 0 | 0 |
| Scope and sequence portion of the native plan gate | 0 | 0 |
| Supplementary static plan diagnostic, including auxiliary gates, excluding known catalogue entries | 391 | 58 |
| Native full plan gate | unavailable | unavailable |
| Native lesson course gate | unavailable | unavailable |

Both native full checks stop at `ModuleNotFoundError: No module named 'markdown'`. A dependency installation did not complete; no environment or repository dependency files were changed.

The supplementary diagnostic in `_scratch/l87/tmp/social-studies-grade-4-grade-fix/static_plan.py` runs the actual plan checker with an import-only placeholder for the missing renderer. Its rendering function raises immediately if called. No rendering was called, and no checker function or result was suppressed. This is static evidence, not a native lesson or print pass. The before diagnostic printed 429 FAIL lines: 332 base findings plus 97 auxiliary findings. The after diagnostic prints 96: no auxiliary findings and 96 base findings. Both include 38 known missing section entries in data/units.csv, ignored as directed. The initial static run followed the first small content repairs, which did not affect these counted plan conditions.

The ledger check keeps the complete subject index when resolving grade 4 citations. Grade 4 has 1,822 rows, zero structural problems, zero unmatched citations and zero planned-only targets. Other grades' citation findings were not changed.

## Repairs

### Continuity

- Read the 160 day headers, goals, Tomorrow blocks and exit records in order. The end-of-course block closes the course rather than promising another day.
- Added the missing day 41 fresh-route and exit return on day 42. Day 41's Tomorrow block, day 42's classroom and home paths, and handbacks.csv now agree. Distribution occurs as Retrieval begins, without inserting another teaching block.
- Corrected six grade 4 ledger notes through ledger.py: conquest returns from day 65 on day 69; enslavement returns from grade 3; Congress returns from grade 3 day 28; purpose and passenger retain their prior learning; the scale-construction note now distinguishes teaching from the new day 16 retry.
- Changed day 65, day 69 and day 112 wording and relevant section explanations to name the review.

### Keys and case separation

- Read items.csv with the csv module one unit at a time, including course-level rows: 182 exit rows and 251 end rows, 433 total. Compared stems, answers, samples, look-fors and wrong responses using the given case evidence.
- Day 16's fresh scale construction repeated day 5's 392-kilometer practice. Replaced it with 168 kilometers on the same 4-centimeter/112-kilometer bar. Independently: 168 = 112 + 56, so the strip is 4 + 2 = 6 centimeters. The wrong response is now a 1.5-centimeter strip. Updated the CSV, wrong-answer explanation, day directions and section plan.
- Replaced eight vague timeline component keys with named dates and positions: Florida 1845, Iowa 1846, Texas 1845, Utah 1896; Maryland 1788, Ohio 1803, Arizona 1912, Montana 1889. Updated adult keys, section-plan copies and the component record. Saved skeletons remain runner snapshots.
- Changed duplicate generic task stems into source-specific directions. Simplified s07-A2 to one integrated importance explanation. These changes preserve the evidence and scoring demand.
- Documented same-day returns in the day 59 and day 106 response look-fors. Existing day narratives already provide the actual return slots.

Cold numerical anchors: unit 1 distances 200 kilometers, 90 kilometers/about 60 miles and 1,200 kilometers/about 750 miles; unit 4 timeline lengths 8 centimeters with offsets 2 and 7, and 20 centimeters with offsets 9.2 and 12.1; unit 6 spans 69, 83, 109 and 125 years; course check 1 distances 450 and 315 kilometers. The archaeology cases distinguish older years-ago dates from later dates and presence from a traced route. Source cases distinguish permission, intention, completed action, missing evidence and independent origins. The community and hazard cases require only details their supplied records support.

### Plan and day data

- Removed the stray `assess=end` on Respond day 59.
- Aligned section goals on days 42 and 102 with the written days and days.csv. Corrected US spelling in edited pages.
- Repaired goal-trace syntax, exact goal phrases and missing ids, including M2a/M2b. Kept practice evidence labeled as practice rather than inventing assessment scores.
- Corrected 22 opening records that had stored most of the whole day as the opening. Their real 40-minute teaching schedules were preserved; opens/opens_min now identify the actual first timed block.
- Added 96 local practice-versus-exit notes using the actual task rows. The auxiliary shape and one-ask gates are now clear.

### Other data

- Removed future-section material uses on days 119 and 120, restored real section-specific key/reference use days, named the missing map material and course-check bundles, and added missing teacher-reference rows.
- Replaced optional references to nonexistent unit 1 openers with the existing section plans and self-contained day pages.
- Normalized seven source rights labels without changing their stated rights or verification status; represented two mixed teaching/response bundles as packets with separate held sections.
- Left tools blank on days without tools. plan.py tables found no generated tables to change.

## Retained findings and template points

All 58 non-catalogue static findings are retained explicitly:

1. **47 practice-evidence trace references.** The trace validator accepts only exits or end items. These social studies days also gather evidence through source annotations, map construction, research, oral or written practice, and proposal drafts. Their narrow exits sample the learning; they do not repeat every larger classroom product. Reclassifying ungraded work solely to satisfy the trace would misstate the assessment. Inspect the exact retained rows in the appendix, especially the broad regional history goals.
2. **Seven exit-coverage findings.** Four require an exit/end row on Respond days 79, 103, 132 and 160 despite their assigned component retries. Three trace findings concern day 79 and the larger practice products on teaching days 125 and 126, whose separate exits sample another component. Do not add a second exit or disguise a retry as a summative item just for the gate.
3. **Four same-day handbacks.** Rows 283 and 287 to 289 return fresh evidence on days 132, 135 and 136 during the stated closing slots. The gate requires a strictly later day. Moving the return would contradict the actual lesson. Day 59 and day 106 same-day returns remain explicit in their item look-fors and day prose.

No checker source was edited. No subject outside grade 4 was repaired. No git command was used. This pass does not establish live source verification, rendered page fit, tested marking times or feasible classroom assessment workload.

## Existing browser-check sources

These statuses predate this pass and remain unchanged. Refused source pages were not fetched again or bypassed.

- 8B: https://wdfw.wa.gov/places-to-go/fishing-piers/elliott-bay
- s02-water: https://files.conagua.gob.mx/conagua/publicaciones/Publicaciones/EAM%202021.pdf
- s02-chapala-map: https://www.inegi.org.mx/contenidos/app/mexicocifras/datos_geograficos/14/14030.pdf
- s04-REC62: https://archives.nypl.org/mss/485
- s06-prescott: https://prescott-az.gov/planning-and-zoning/historic-preservation/
- C3-133-atlas: https://www.gnb.ca/content/dam/GNB3/t/dt-ct/rh-ra/docs/2020_County_Districts_Comtes_Districts.pdf

## Exact remaining static findings

```text
FAIL day 79: no exit question in items.csv
FAIL day 103: no exit question in items.csv
FAIL day 132: no exit question in items.csv
FAIL day 160: no exit question in items.csv
FAIL day 65: shows names s04-P65-8, which is neither an exit of day 65 nor an end-of-unit item of unit 4
FAIL day 66: shows names s04-P66-6, which is neither an exit of day 66 nor an end-of-unit item of unit 4
FAIL day 79: shows names no exit of the day; the exit ticket must check the goal
FAIL day 89: shows names s05-P89-5, which is neither an exit of day 89 nor an end-of-unit item of unit 5
FAIL day 89: shows names s05-P89-5, which is neither an exit of day 89 nor an end-of-unit item of unit 5
FAIL day 89: shows names s05-P89-5, which is neither an exit of day 89 nor an end-of-unit item of unit 5
FAIL day 122: shows names s06-P122-1, which is neither an exit of day 122 nor an end-of-unit item of unit 6
FAIL day 122: shows names s06-P122-1, which is neither an exit of day 122 nor an end-of-unit item of unit 6
FAIL day 123: shows names s06-P123-1, which is neither an exit of day 123 nor an end-of-unit item of unit 6
FAIL day 123: shows names s06-P123-1, which is neither an exit of day 123 nor an end-of-unit item of unit 6
FAIL day 125: shows names s06-X125a, which is neither an exit of day 125 nor an end-of-unit item of unit 6
FAIL day 125: shows names s06-X125a, which is neither an exit of day 125 nor an end-of-unit item of unit 6
FAIL day 125: shows names s06-X125a, which is neither an exit of day 125 nor an end-of-unit item of unit 6
FAIL day 125: shows names s06-X125a, which is neither an exit of day 125 nor an end-of-unit item of unit 6
FAIL day 125: shows names no exit of the day; the exit ticket must check the goal
FAIL day 126: shows names s06-X126a, which is neither an exit of day 126 nor an end-of-unit item of unit 6
FAIL day 126: shows names s06-X126a, which is neither an exit of day 126 nor an end-of-unit item of unit 6
FAIL day 126: shows names s06-X126a, which is neither an exit of day 126 nor an end-of-unit item of unit 6
FAIL day 126: shows names s06-X126a, which is neither an exit of day 126 nor an end-of-unit item of unit 6
FAIL day 126: shows names no exit of the day; the exit ticket must check the goal
FAIL day 127: shows names s06-P127-1, which is neither an exit of day 127 nor an end-of-unit item of unit 6
FAIL day 127: shows names s06-P127-2, which is neither an exit of day 127 nor an end-of-unit item of unit 6
FAIL day 127: shows names s06-X127b, which is neither an exit of day 127 nor an end-of-unit item of unit 6
FAIL day 132: shows names s06-P132-1, which is neither an exit of day 132 nor an end-of-unit item of unit 6
FAIL day 132: shows names s06-P132-2, which is neither an exit of day 132 nor an end-of-unit item of unit 6
FAIL day 132: shows names s06-P132-3, which is neither an exit of day 132 nor an end-of-unit item of unit 6
FAIL day 132: shows names s06-P132-4, which is neither an exit of day 132 nor an end-of-unit item of unit 6
FAIL day 142: shows names s07-P142, which is neither an exit of day 142 nor an end-of-unit item of unit 7
FAIL day 142: shows names s07-P142, which is neither an exit of day 142 nor an end-of-unit item of unit 7
FAIL day 142: shows names s07-P142, which is neither an exit of day 142 nor an end-of-unit item of unit 7
FAIL day 142: shows names s07-P142, which is neither an exit of day 142 nor an end-of-unit item of unit 7
FAIL day 142: shows names s07-P142, which is neither an exit of day 142 nor an end-of-unit item of unit 7
FAIL day 143: shows names s07-P143, which is neither an exit of day 143 nor an end-of-unit item of unit 7
FAIL day 144: shows names s07-P144, which is neither an exit of day 144 nor an end-of-unit item of unit 7
FAIL day 144: shows names s07-P144, which is neither an exit of day 144 nor an end-of-unit item of unit 7
FAIL day 145: shows names s07-P145, which is neither an exit of day 145 nor an end-of-unit item of unit 7
FAIL day 148: shows names s07-X148b, which is neither an exit of day 148 nor an end-of-unit item of unit 7
FAIL day 151: shows names s07-P151-E, which is neither an exit of day 151 nor an end-of-unit item of unit 7
FAIL day 151: shows names s07-P151-E, which is neither an exit of day 151 nor an end-of-unit item of unit 7
FAIL day 152: shows names s07-X152b, which is neither an exit of day 152 nor an end-of-unit item of unit 7
FAIL day 155: shows names s07-P155, which is neither an exit of day 155 nor an end-of-unit item of unit 7
FAIL day 155: shows names s07-X155b, which is neither an exit of day 155 nor an end-of-unit item of unit 7
FAIL day 155: shows names s07-X155b, which is neither an exit of day 155 nor an end-of-unit item of unit 7
FAIL day 156: shows names s07-P156, which is neither an exit of day 156 nor an end-of-unit item of unit 7
FAIL day 156: shows names s07-P156, which is neither an exit of day 156 nor an end-of-unit item of unit 7
FAIL day 160: shows names s07-R160-G, which is neither an exit of day 160 nor an end-of-unit item of unit 7
FAIL day 160: shows names s07-R160-P, which is neither an exit of day 160 nor an end-of-unit item of unit 7
FAIL day 160: shows names s07-R160-A, which is neither an exit of day 160 nor an end-of-unit item of unit 7
FAIL day 160: shows names s07-R160-C, which is neither an exit of day 160 nor an end-of-unit item of unit 7
FAIL day 160: shows names s07-R160-H, which is neither an exit of day 160 nor an end-of-unit item of unit 7
FAIL handbacks.csv row 283: to_day 132 is not later than from_day 132
FAIL handbacks.csv row 287: to_day 135 is not later than from_day 135
FAIL handbacks.csv row 288: to_day 136 is not later than from_day 136
FAIL handbacks.csv row 289: to_day 136 is not later than from_day 136
```
