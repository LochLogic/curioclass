# Answer-key read: social-studies-grade-4, unit 1

Job 017, kit 14. Assigned date: 2026-11-25. Work performed: 2026-11-26.

## Verdict

**Fail as a completed cold answer-key read.** Ten content faults were fixed, but Record A still needs a two-item split beyond the final edit whitelist, and my initial extraction exposed answer guidance before the independent solutions were recorded.

## Scope and counts

Read all **41** exit/end records for days 1 to 16: **15 exits, 19 day-15 assessment records, 7 day-16 retries, and 0 readiness items**. The 19 include two records scored from existing work, s01-A4b and s01-A4c-interpretation, which ask for no additional student response. Read all **90** associated wrong-answer rows. Day 1 and day 12 retrieval are not readiness items in items.csv.

Faults by kind: **key 5; off-goal 2; rule4 2; key-on-child-page 1; two-asks 1; ambiguous 0; needs-info 0**. Ten fixed; one split left. Eight item rows changed, plus diagnostic-only repairs for s01-A2b and s01-X13. No ids or assigned days were changed, no new items were added, and rows outside unit 1 were preserved.

## What I studied

- `docs/pipeline/briefs/sensitivity-read.md`, sections 1 to 3, answer-key instructions: solve, compare, check standards, report limits.
- `docs/courses/social-studies-grade-4/DEFAULTS.md` and `docs/pipeline/briefs/section-write.md`, rule 8: 40-minute days, 350 student words per page, sentences of at most 15 words, turns counted per child.
- `items.csv`, initially restricted to assessment records, and the held exit, assessment and retry cards: computed the answers and read the SVG positions and lengths.
- `days.csv`, `parts.csv`, section plans u01-1 through u01-4 field 3, and unit plan s01 field 5: compared the requested work with the goals and standards.
- The unit's teaching masters, student portions of d001 through d016, teacher keys, record sheet, wrongs and handbacks: checked case separation, scoring, print forms, routing, turns and scale.
- The exact source URLs listed below, opened after the solution record: checked the factual premises rather than marking them from search summaries.

Before opening the teacher key pieces, the file inventory listed `key-01.md` through `key-16.md`, and the assessment inventory listed all 41 item ids. Those teacher pieces print the answers to their day's items. The solution record is `_scratch/l87/tmp/social-studies-grade-4-key-u1/solutions-before-keys.md`; the revised-item record is `revised-solutions-before-keys.md` in that same folder.

## Own errors and cold-solve limit

My first extraction excluded the answer column but accidentally included `steps` and `samples`. Both contain answer guidance. The extraction included all 41 records, so I cannot certify any of them as an uncontaminated cold solve. I stopped that extraction pattern, used a strict stem-only field list, recorded all 41 answers and methods before opening full answer fields and teacher pieces, and disclosed the exposure rather than calling the read cold. No later agreement with the keys repairs that process error. A new reader must perform the required cold read.

No arithmetic or coordinate error was found in my recorded solutions. The narrower disagreements below concern what the item actually asks versus what its key scores. My initial s01-A3a response located both cultural features relative to the street; the key required an unrequested lake relationship. That was a key/stem mismatch, not a mistaken map reading.

## Faults

| Item | Kind | What was wrong | Fix or exact remaining action | Stage that made it |
|---|---|---|---|---|
| s01-P16-1 | two-asks | ?Repair Record A using its key and north arrow.? The printed record requires both a symbol correction and a direction correction. Teacher-only wording to score one privately assigned component does not split the printed asks. | **Left.** Retain s01-P16-1 for ?Repair the dashed-line label using Record A's key.? Key: river. Add s01-P16-1-direction for ?Repair the page-right label using Record A's north arrow.? Key: west. Give each its own print line, teacher key, wrongs and handback entry; route the new id in day 16's shows. | section plan |
| s01-A2a | rule4 | ?seven indexed places? adds United States, Mexico and Nunavut to the four reserved locations. These appeared in teaching, and the ledger explicitly says Nunavut is not a fresh check. | Restored the unit plan's four held places, Manitoba, Oaxaca, Jamaica and Kansas. Updated the item, key, response table and record count to four. Marked e-g supplement as unscored reference. | section plan, retained by data |
| s01-P16-2 | rule4 | ?168 kilometers using the review bar? reuses the 4-centimeter/112-kilometer practice bar and its half value, 56. | New held bar: 6 centimeters represents 104 kilometers. New construction: 156 kilometers, so 9 centimeters. Updated item, samples, wrong-answer explanation, printed bar and teacher key. | section plan |
| s01-X1 | off-goal | ?Write a supporting question? does not show the assigned D1.1 importance criterion. | Now ?Why might the two readers ask different map questions?? The key explains their different purposes and information needs. | section plan |
| s01-A4c | off-goal | ?Describe another reader's different question and needed map? can name a reader and map without explaining why the question matters, the assigned D1.1 criterion. | Now ?Explain why another reader would need C or D for a different question.? Key and wrong-answer note require the answer's benefit for that reader. | unit plan |
| s01-A2b-province | key-on-child-page | Child card: ?Division reference: provinces are major divisions of Canada.? The item asks for that definition, and the key repeats it. | Removed the child-facing answer sentence. The definition remains in teacher-only key-15.md, already named in Before class. New stem: ?Explain why Manitoba is a province rather than a country.? Child applies the legend and country boundary. | data |
| s01-A2d | key | Stem asks how Card H identifies a Native nation today, but the key also requires distinguishing it from a state or independent country and begins ?Yes? without a yes/no question. | Key now scores the named nation and its present government evidence. No separate unasked comparison. L is diagnosed only if volunteered. | data |
| s01-A3a | key | ?Use E to locate the library and park? allows several mapped relationships, but the look-fors specifically require the park/lake relationship. | New single relationship task explicitly names library, park and lake. Key accepts northwest or west for the library and the supported park/lake relationship. | data |
| s01-A2c | key | Plot-K item includes sample and wrong row ?L: 110 degrees west, 30 degrees north,? carried from the separate reading item. | Removed that wrong row, added an observable misplaced-K response with x rather than inferring a cause, and replaced the unrelated sample. | data |
| s01-A2b | key | Wrong-answer note still says to score ?the two definitions separately? on the chain item after county/province were split into other ids. | Note now scores the four chain blanks only and sends definitions to their own item ids. | data |
| s01-X13 | key | Wrong-answer note refers to crediting Z, which belongs to the separate s01-X13b item. | Note now scores Y here and explicitly leaves Z to s01-X13b. P requires an explicit reference-line explanation. | data |

The final edit whitelist permits unit rows of items.csv/wrongs.csv, shared/key pieces and this report. It excludes handbacks.csv and days.csv. I did not partly create a split that would lack the required routing, or edit those excluded tables. This is a scope conflict to settle with Cory or the lead, not a template exception.

## Recorded answers and methods before full key comparison

These are the initial records, preserved even where an item was later changed. All matched the mathematical/geographic substance of the full answers; alternative supported wording was accepted. The exposure limitation above applies throughout.

| Item | My recorded answer | Method |
|---|---|---|
| s01-X1 | Which details help someone walk to school, and which help someone compare countries? | Compare the two stated purposes and form a supporting question. |
| s01-X2 | Lake Winnipeg, feature 2: its enclosed hatched shape matches the lake legend. | Match the pattern, then use the index. |
| s01-X3 | Sierra Madre Occidental at 1; Mojave Desert at 2. | Index and range/desert patterns. |
| s01-X4 | Canadian Shield: North America; Amazon Basin: South America. | Match regions to labeled continent outlines. |
| s01-X5 | 200 kilometers. | Segment 50 SVG units / bar 20 = 2.5; 2.5 x 80 = 200. |
| s01-X6 | 90 kilometers, about 60 miles. | 60+30 and 40+20. |
| s01-X7 | The town view supports local routes with streets and library; Colorado locates Denver; the continent view locates Colorado but omits local streets. | Compare visible and omitted detail. |
| s01-X8 | Seattle town view: it shows the garden, hall and shoreline route. | Compare the requested walk with visible features. |
| s01-X9 | Prince Edward Island is a province within Canada: the inset is hatched. | Apply the printed legend. |
| s01-X10 | Sonora at S; Barbados at B. | Follow the index to the main map and Caribbean inset. |
| s01-X11 | Tucson city, Pima County, Arizona state, United States country, North America continent. | Read containment from inner to outer. |
| s01-X12 | X at 40N/120W. | Intersect latitude row and longitude column. |
| s01-X13 | 20 degrees north, 90 degrees west. | Y is at x335/y155, the 90W column and 20N row. |
| s01-X13b | Z at 60N/130W. | Intersect top latitude row and second longitude column. |
| s01-X14 | Walking Map helps follow paths near the pond; Region Map locates the park relative to town. Neither measures distances. | Use one feature from each map and an explicit limit. |
| s01-A1a | 1 Mackenzie River; 2 Great Slave Lake; 3 Arctic Ocean; 4 Appalachian Mountains; 5 Chihuahuan Desert. | Match numbered geographic positions and patterns to the unordered index. |
| s01-A1b | The solid line at 1 is the river; dotted lines are boundaries. | Match C legend patterns. |
| s01-A1c | P is west of Q. | North points page-right; page-up is west. |
| s01-A1d | 1200 kilometers, about 750 miles. | Segment 30/bar20 = 1.5; 800+400 and 500+250. |
| s01-A2a | a Manitoba, province; b Oaxaca, state; c Jamaica, country; d Kansas, state; e United States, country; f Mexico, country; g Nunavut, territory. | Read both D sheets, index and political-division patterns. |
| s01-A2a-outline | Trace Canada national boundary. | Follow the outer country outline, including islands rather than Manitoba only. |
| s01-A2b | Madison city, Dane County, Wisconsin state, United States country, North America continent. | Apply inset containment. |
| s01-A2b-county | Dane County is a division inside Wisconsin state that contains Madison. | Use this inset, without generalizing all countries. |
| s01-A2b-province | A province is a major division within Canada. | Apply supplied division reference. |
| s01-A2c | K at 50N/100W. | Intersect second row and fourth column. |
| s01-A2c-read | 30 degrees north, 110 degrees west. | L at x171/y95.3 matches row and column. |
| s01-A2d | Chickasaw Nation has elected officials and a supreme court today, evidence of its own government. | Use Card H present-day institutions. |
| s01-A3a | Library northwest of park; library north of Street, park south of Street. | Read E with north up and feature positions. |
| s01-A3b | Madison is in southern Wisconsin, within North America. | Follow the point in F and Wisconsin shape in G. |
| s01-A3c | F spans Wisconsin for statewide deliveries; it omits local streets and individual addresses. | Match map extent to the task. |
| s01-A4a | C shows physical features and D political locations; together they help a visitor locate landforms and jurisdictions. They omit current road or travel conditions. | Support one claim with one visible feature from each map and a limit. |
| s01-A4b | No separate response: score the reasoning in A4a once. | Inspect evidence-to-claim links in the submitted response. |
| s01-A4c | A river researcher asks where the Mackenzie runs and needs C rather than D. | State a distinct reader purpose and appropriate map. |
| s01-A4c-interpretation | No separate response: the visitor and river researcher need different map information. | Compare A4a and A4c without rescoring the same criterion. |
| s01-P16-1 | Dashed line means river; page-right is west. | Use legend and rotate directions with south pointing up. |
| s01-P16-2 | A strip 1.5 times the 112-kilometer bar, 6 centimeters at actual size. | 168 = 112+56; source bar is 4 centimeters. |
| s01-P16-3 | Yucat?n is a state within Mexico. | Reverse the false containment and use hatch legend. |
| s01-P16-4 | Native nations can govern themselves within the United States today. | Replace the false outside-only statement with the supplied reference. |
| s01-P16-5 | Equator north/south is latitude; prime meridian east/west is longitude. | Correct both swapped headings. |
| s01-P16-6 | The wider view omits Oak Street. | Compare visible detail instead of assuming complete coverage. |
| s01-P16-7 | V shows stalls beside a well, locating the market water source. | Add the missing V evidence to the given access-and-water claim. |

## Revised items solved again

The revised-item solutions were recorded before writing the revised keys. The purely diagnostic repairs did not change the student task.

| Item | New independent solution and method |
|---|---|
| s01-X1 | Walking to school needs local route details; comparing countries needs country locations. Explain why the two purposes require different information. |
| s01-A2a | a Manitoba province; b Oaxaca state; c Jamaica country; d Kansas state. Read a-d and the map key; e-g is not assessed. |
| s01-A2d | Chickasaw Nation has elected officials and a supreme court today. Those institutions establish the present government evidence asked for. |
| s01-A3a | Library northwest/west of park; park beside Lake Monona. Read the north-up map, not an assumed real library position. |
| s01-A2b-province | D shades Manitoba as a province inside Canada. A province is a division of that country. |
| s01-P16-2 | 156 = 104 + 52; a whole 6-centimeter bar plus half, 3 centimeters, gives a 9-centimeter strip. SVG bar spans 60 of 80 units on an 8-centimeter-wide diagram. |
| s01-A4c | A landform researcher needs C to locate the Chihuahuan Desert for comparing physical regions. This gives another reader, a supported question/map and why the answer matters. |

## Rule 4 and case distinctions

Read the teaching masters as well as the held cards. Held maps and invented situations remain withheld until their check. The revised scale values are absent from teaching masters. The three repeated political entries are no longer scored.

Filtered ledger commands used `python -X utf8 scripts/ledger.py show social-studies --before social-studies-grade-4 --term "<word>"`, never the whole ledger. Terms searched: Madison, Winnipeg, Mojave, Denver, Seattle, Shield, Amazon, Mackenzie, Appalachian, Chickasaw, Sonora, Tucson, Potawatomi, Prince Edward, Manitoba, Yucat, park, Barbados, Oaxaca, Great Slave, Market Maps and 168.

Lower-grade hits judged distinct: Denver's earlier city-dot/capital and founding cases are not this invented library/river three-view comparison; Chickasaw homeland/removal cards are not the new present-government card. Appalachian appears as a prior term, not a reused assessment case. Lower-grade Amazon compass work is flagged below because the ledger does not specify whether it used the same basin representation. Generic continental outlines, compass conventions, vocabulary definitions and grid margin labels are common map references, not themselves a held case. The map-specific feature combinations, coordinate pairs, invented locations and measurement data are the case comparisons.

A1a's name bank supplies the unfamiliar names but does not pair a name with a printed feature number; students still read C and its legend. I accepted this supported map-labeling task rather than making it recall of five untaught place names. The matching work is narrow and does not alone establish all of MA.4.T1.1; the other components assess key use, orientation and measurement.

## Facts and safety

Opened the source-of-record URLs below. Their corresponding sources.csv rows already carry `checked: 2026-11-25`; I did not edit sources.csv. Opens were performed on 2026-11-26, and were not backdated. Parsed geographic source records, rather than relying on a search summary. Downloads and selected records are retained in this job's scratch folder in source-evidence.json.

| Facts checked | Source row and page opened | Result |
|---|---|---|
| Lake Winnipeg and Great Slave Lake names/categories | 1C / 15C2: [lake records](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_lakes.geojson), and [15C2 ZIP](https://naciscdn.org/naturalearth/50m/physical/ne_50m_lakes.zip) | Lake records present. |
| Hudson Bay and Arctic Ocean categories and geometry | 2H / 15O: [marine records](https://naciscdn.org/naturalearth/50m/physical/ne_50m_geography_marine_polys.zip) | Bay and ocean records present. |
| Sierra Madre Occidental, Canadian Shield, Amazon Basin, Appalachian Mountains, Chihuahuan Desert | 3G / 15C3: [landform records](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_geography_regions_polys.geojson), [15C3 ZIP](https://naciscdn.org/naturalearth/50m/physical/ne_50m_geography_regions_polys.zip) | Names and physical categories present. |
| Mojave broad location | 3D: [park desert page](https://home.nps.gov/lake/learn/nature/deserts.htm) | Describes southern Nevada and southeastern California; source uses the spelling Mohave. No exact desert border is asserted. |
| Shield in North America; Amazon basin's South American position | 4S: [archived Shield page](https://epe.lac-bac.gc.ca/100/205/301/statcan/canada_e-book-ef/05-01-21/142.206.72.67/01/01a/01a_002a_e.htm?nodisclaimer=1); 4B: [basin map](https://storage.googleapis.com/fao-aquastat.appspot.com/PDF/MAPS/amazon-map_detailed.pdf) | Continent/region premises supported. |
| Map/ground distance and extent/detail selection | 5S: [map scale](https://www.ga.gov.au/scientific-topics/national-location-information/topographic-maps/what-is-map-scale) | Supports concept; classroom distances and conversion pairs are invented approximations. Recomputed all item arithmetic independently. |
| Denver, Seattle and Madison representative city locations; states and continent context | 7C / 15G: [place records](https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2025_Gazetteer/2025_Gaz_place_national.zip); 7N / 15C0: [country records](https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip); 9G / 15D: [division records](https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_1_states_provinces.zip) | Read the CO Denver, WA Seattle and WI Madison records and state/continent fields. |
| South Platte River in Denver | 7R: [river trail page](https://denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Parks-Recreation/Planning-Design-Construction-Community-Engagement/Park-Facility-Projects/South-Platte-River-Trail-Improvements) | Page places the river through Denver. Local streets and library pin are invented. |
| Prince Edward Island/Manitoba provinces; Sonora/Oaxaca/Yucat?n states; Kansas state; Nunavut territory | 9C: [Canadian divisions](https://www.canada.ca/en/intergovernmental-affairs/services/provinces-territories.html); 9G / 10M / 11G / 15D / 16P: [division records](https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_1_states_provinces.zip) | Read categories and parent countries. Nunavut is now unscored reference only. |
| Barbados and Jamaica country status | 10G: [country records](https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip) | Sovereign-country records present. |
| Tucson/Pima/Arizona and Madison/Dane/Wisconsin | 11P: [Pima County](https://www.pima.gov/about-pima-county); 15M: [Dane municipalities](https://www.danecounty.gov/municipalities); 11G / 15D division records | County/city and enclosing state premises supported. |
| Lake Monona relationship to Madison | 15LC: [city park page](https://www.cityofmadison.com/parks/find-a-park/olbrich) | Real lake/city premise supported. Assessment library, park and street are invented, not claims about that actual park. |
| Chickasaw Nation government today; Native self-government in the United States | 15H: [nation government](https://www.chickasaw.net/Our-Nation/Government.aspx); 11B / 12D: [government reference](https://www.bia.gov/frequently-asked-questions) | Present institutions and self-government premise supported. |
| Latitude and longitude zero lines/directions | 12A: [latitude](https://oceanservice.noaa.gov/facts/latitude.html); 12B: [longitude](https://oceanservice.noaa.gov/facts/longitude.html) | Definitions supported; read every held plotted/read intersection from its SVG coordinates. |

Judged rather than independently field-verified: all invented roads, gardens, halls, libraries, parks, markets, claims and walking situations; schematic distance approximations; broad locator placement and relative positions. These are classroom representations, not actual navigation routes. I did not certify every coastline vertex or physical print registration. No item requires a child to disclose home, money, religion or family facts, to speak publicly, or to enact a historical harm. Naming a Native nation remains specific and in the present, without equating a nation with a state or an independent country.

### Browser check

- Source **8B**, [Elliott Bay](https://wdfw.wa.gov/places-to-go/fishing-piers/elliott-bay). File: `courses/social-studies-grade-4/u01-2/exit-08.md`, also embedded in `d008.md`; item s01-X8. Fact: Elliott Bay adjoins Seattle's waterfront. The existing source row records a 403 and the one alternate, `https://www.seattle.gov/documents/Departments/Waterfront/2026_WFS_ProjectBrochure_Map_ENGLISH.pdf`, also 403. Neither was retried or fetched by another route. Keep browser check; the lead must open it in a real browser.

## Section-plan field 3 lines now stale

The data job's writer owns these synchronizations; section plans were not edited.

- `u01-1.md`, E1 / s01-X1: old ?Write a supporting question about their different map needs? and its sample. Replace with the revised purpose/importance explanation and answer.
- `u01-3.md`, Q2 component shapes and reserved index: seven places, including United States, Mexico and Nunavut, must become the four reserved a-d places. Country/territory supplement is reference only.
- `u01-3.md`, Q2 A2b description: the province item now applies the term to Manitoba and its country boundary, not a copied definition.
- `u01-4.md`, Q4 A4c shape, and `u01-1.md` Q4 other-reader shape: include why the answer matters to the other reader, not naming a different reader/question/map alone.
- `u01-4.md`, s01-P16-2: old 168 kilometers, 112-kilometer review bar and 6-centimeter answer. Replace with 156 kilometers, new 104-kilometer/6-centimeter bar and 9-centimeter answer.
- `u01-2.md`, Q3 A3a shape/key: explicitly name the library/park/lake relationship required by the revised stem.

No other field 3 exit stem differs from the final items.csv. A2d's existing plan calls for the nation evidence; the removed extra data look-for no longer imposes an unstated second answer. Diagnostic-only changes do not require new plan stems.

Other required owner sync: `d015.md` embeds the older seven-row response table even though Before class names the separate assessment form. The edited `assessment.md` is the current four-row form. Its province reference has been removed and the new stems are current there; the day file's item placeholders resolve new stems but its static e-g rows remain. `d010.md` still tells students to write categories for X10, although items.csv and the current held master score locations only. Both day files are outside this job's final shared-piece edit boundary. The ledger's old reserved-scale value also needs its script-owned update before a later writer relies on it.

## Length, turns and marking scale

All 41 original item stems and every revised stem have no sentence over 15 words, retaining normal punctuation. The shared response form supplies short directions and space for the mapped relationships. The final course gate verified printed sides. The revised assessment is two pages, with 97 and 170 extracted words, and retry-2 is one page with 33 words. I rendered those PDFs to PNGs and visually inspected all three pages: no clipping or overlap, the four-row table and revised prompts are present, and the new bar is labeled 104 kilometers. Intermediate renderings remain in this job folder. Other course pages were checked by the gate, not visually certified by this read.

The record and teacher keys use **shown, shown with help, not yet seen**, with no total. Two partner turns of 45 seconds take 90 seconds across simultaneous pairs; three cycles take 4.5 minutes. Six individual hearings at 45 seconds take 4.5 minutes inside a named five-minute slot, with paper evidence collected from everyone else. Day 16 has four sequential five-minute groups, each with at most two 45-second explanations, within its 20-minute allocation. No uncounted whole-class oral queue was found.

## Could not settle

1. This read's cold-solve requirement needs a new reader because of my extraction error.
2. Record A's split requires permission for the handbacks/days routing excluded by the final whitelist. The exact proposed split is in the faults table. It is not called fixed.
3. The lower-grade ledger's ?Amazon? compass case does not identify river versus basin or its artwork. Current X4 uses the physical Amazon Basin/Canadian Shield continent case. I cannot certify that distinction from the filtered ledger text alone; I did not open lower-grade course files outside this job's read scope. Lead should settle whether the reserved basin is sufficiently distinct or needs a replacement.
4. Source 8B remains the browser check listed above.

## Gate evidence

Final complete course gate **exited 0**: **0 failing findings; 94 new note lines**. It reports **330 current failing lines** against the existing baseline; these are retained course debt, not a clean-course result. The baseline is from e91338bbf and the current head is 2e2883ac7, so committed changes since that baseline also appear as notes. Lesson failing lines in the comparison fell from 182 to 180. No new FAIL line was printed.

The first literal `python -X utf8 scripts/gate.py --course social-studies-grade-4` attempt failed because the launcher reported a directory as sys.executable. The actual executable was `C:/Program Files/LibreOffice/program/python-core-3.12.14/bin/python.exe`. Preflight attempts then identified missing Markdown and pypdf dependencies, installed only under this job's scratch/deps folder. A full pre-edit launch was started before content edits, but later print attempts produced no PDFs and that incomplete run was stopped. It is not treated as a passing pre-edit result. The existing stored course baseline was retained; no manual baseline was requested or created.

The final run used that actual executable, scratch/deps on PYTHONPATH, and the job-local `sitecustomize.py` launch compatibility hook. That hook adds only an isolated browser profile, a hidden window and --no-sandbox to the local HTML print process in this managed environment. It does not replace or disable a gate, assertion, content rule, page count, or baseline comparison. Every one of the 12 course gates ran. No shared script was edited.

Final invocation, after setting PYTHONPATH to this job folder and its deps folder:

```powershell
& 'C:/Program Files/LibreOffice/program/python-core-3.12.14/bin/python.exe' -X utf8 scripts/gate.py --course social-studies-grade-4
```

Printed new lines, including the complete comparison's notes that the console abbreviated:

```text
== lesson-social-studies-grade-4 (92 new line(s), 0 failing); failing lines fell 182 -> 180
  note courses/social-studies-grade-4/u01-1/d001.md: teacher 467 words, student 181 words (109 frame, 72 questions), 40 min, 2 side(s), at home 96 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/d002.md: teacher 509 words, student 181 words (104 frame, 77 questions), 40 min, 2 side(s), at home 98 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/d003.md: teacher 570 words, student 226 words (166 frame, 60 questions), 40 min, 2 side(s), at home 98 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/d004.md: teacher 497 words, student 167 words (119 frame, 48 questions), 40 min, 2 side(s), at home 84 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/exit-01.md: blank, 40 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/exit-02.md: blank, 47 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/exit-03.md: blank, 48 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/exit-04.md: blank, 47 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/family.md: family, 256 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/four-part-map-card.md: blank, 42 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/key-01.md: opener, 271 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/key-02.md: opener, 282 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/key-03.md: opener, 213 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/key-04.md: opener, 216 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/landform-cards.md: blank, 105 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/maps-a-b.md: blank, 53 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/mountain-belts.md: blank, 48 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/opener.md: opener, 477 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/practice-water.md: blank, 43 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/question-board.md: blank, 53 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/question-strips.md: blank, 68 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/record.md: record, 144 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-1/silhouette-cards.md: blank, 17 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/symbol-arrow-slips.md: blank, 67 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-1/trail-map.md: blank, 52 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/boulder-windows.md: blank, 103 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/d005.md: teacher 445 words, student 124 words (53 frame, 71 questions), 40 min, 2 side(s), at home 92 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/d006.md: teacher 410 words, student 110 words (49 frame, 61 questions), 40 min, 2 side(s), at home 79 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/d007.md: teacher 482 words, student 228 words (168 frame, 60 questions), 40 min, 2 side(s), at home 73 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/d008.md: teacher 499 words, student 254 words (211 frame, 43 questions), 40 min, 2 side(s), at home 76 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/exit-05.md: blank, 32 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/exit-06.md: blank, 27 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/exit-07.md: blank, 56 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/exit-08.md: blank, 63 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/key-05.md: opener, 252 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/key-06.md: opener, 169 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/key-07.md: opener, 251 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/key-08.md: opener, 194 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/opener.md: opener, 443 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-2/practice-bar.md: blank, 24 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/prepared-strips.md: blank, 70 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/table-repairs.md: blank, 99 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-2/weather-inventory.md: blank, 89 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/canada-trails.md: blank, 105 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/containment-government.md: blank, 146 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/d009.md: teacher 429 words, student 188 words (153 frame, 35 questions), 40 min, 2 side(s), at home 69 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-3/d010.md: teacher 450 words, student 244 words (190 frame, 54 questions), 40 min, 2 side(s), at home 76 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-3/d011.md: teacher 510 words, student 288 words (219 frame, 69 questions), 40 min, 2 side(s), at home 73 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-3/exit-09.md: blank, 42 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/exit-10.md: blank, 38 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/exit-11.md: blank, 98 words, student page 2 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/key-09.md: opener, 195 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-3/key-10.md: opener, 241 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-3/key-11.md: opener, 270 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-3/mexico-caribbean-trails.md: blank, 89 words, student page 2 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-3/opener.md: opener, 436 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-c.md: blank, 43 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-d.md: blank, 39 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-e-f-g.md: blank, 49 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-grid.md: blank, 22 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-inset-card.md: blank, 71 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-location-index.md: blank, 47 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment-measurement.md: blank, 24 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/assessment.md: blank, 233 words, student page 2 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/claim-reference.md: blank, 51 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/d012.md: teacher 464 words, student 202 words (161 frame, 41 questions), 40 min, 2 side(s), at home 72 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/d013.md: teacher 439 words, student 119 words (68 frame, 51 questions), 40 min, 2 side(s), at home 70 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/d014.md: teacher 425 words, student 152 words (111 frame, 41 questions), 40 min, 2 side(s), at home 75 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/d015.md: teacher 486 words, student 230 words (43 frame, 187 questions), 40 min, 2 side(s), at home 38 words, 45 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/d016.md: teacher 442 words, student 49 words (29 frame, 20 questions), 40 min, 1 side(s), at home 88 words, 35 min, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/evidence-critiques.md: blank, 98 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/exit-12.md: blank, 31 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/exit-13.md: blank, 36 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/exit-14.md: blank, 46 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/key-12.md: opener, 217 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/key-13.md: opener, 240 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/key-14.md: opener, 228 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/key-15.md: opener, 669 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/key-16.md: opener, 308 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/numbered-stars.md: blank, 71 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/opener.md: opener, 481 words, 0 failure(s)
  note courses/social-studies-grade-4/u01-4/response-comparisons.md: blank, 226 words, student page 2 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-1.md: blank, 25 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-2.md: blank, 12 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-3.md: blank, 31 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-4.md: blank, 33 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-5.md: blank, 26 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-6.md: blank, 27 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/retry-7.md: blank, 44 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/routes-and-headings.md: blank, 79 words, student page 1 side(s), 0 failure(s)
  note courses/social-studies-grade-4/u01-4/zero-line-reference.md: blank, 67 words, student page 1 side(s), 0 failure(s)
  note lesson_course: 192 failure(s) in 160 day(s), 127 in day files
== plan-social-studies-grade-4 (2 new line(s), 0 failing)
  note note day 11: the goal piece "Native nations are nations too" is shown by no exit of the day, only by s01-A2d; does the exit check the goal?
  note social-studies-grade-4: 1254 items and 1487 wrong answers checked, 58 failure(s)
gate social-studies-grade-4 against its baseline: 0 failing finding(s), 94 new note line(s)
```


## Files changed

- Unit 1 rows only in `data/plans/social-studies-grade-4/items.csv` and `wrongs.csv`, through rows.py, full ids and composite wrong-row keys, dry-run first.
- `u01-1/exit-01.md`, `u01-1/key-01.md`, `u01-1/record.md`.
- `u01-4/assessment.md`, `assessment-inset-card.md`, `assessment-location-index.md`, `key-15.md`, `retry-2.md`, `key-16.md`.
- This report. Helper scripts, receipts, source evidence and solution records remain only in `_scratch/l87/tmp/social-studies-grade-4-key-u1/`.

No extra empty folder was observed. No shared script, source row, section plan, unit plan, handbacks row or day file was edited.
