# Worksheets grade fit L22 (2026-11-20)

Task: later.csv row L22. The 27 sheets moved by L20 were read for their new grade or course: reading level, sentence
length, question demand, vocabulary, and whether the skills named in the I can line, the directions and the concept
row fit. Compared with the concept list row (docs/worksheets/social-studies.md) and the course (US History I is grade 11
per docs/courses/us-history-i/frame.md). Result: 26 fit, 1 fixed, 0 flagged.

| Sheet | Old to new | Verdict | What changed or why it fits |
|---|---|---|---|
| ss-1 #43 Who Leads Our Town? | G2 to G1 | fit | Short sentences, five picture-free choice items on literal recall, one short write. Passage already trimmed in L20. |
| ss-1 #48 Changemaker Timeline | G2 to G1 | fixed | Card text used Declaration of Independence, disasters, boycott, Nobel Peace Prize; the questions needed 1881 minus 1849 and a comparison of 1947 and 1955. Cards rewritten in plain words (years unchanged). Subtraction question replaced by "Who came right after Clara Barton?" {Jackie Robinson}; the closest-years question replaced by "Who came right before Malala Yousafzai?" {Rosa Parks}. Keys match the timeline order. |
| ss-3 #41 State History Timeline | G4 to G3 | fit | Ruler and scaled timeline, subtraction within 100, one choice, one short write. Dense for grade 3 but within reach with the sample-state scaffold. |
| ss-3 #47 Local, State or Federal? | G4 to G3 | fit | Three-level sort, concrete services, plain vocabulary. |
| ss-3 #51 What We Sell, What We Buy | G4 to G3 | fit | Map-grid arrows and goods, simple choice and write items. |
| ss-4 #48 Environment Shapes Life | G5 to G4 | fit | Region chart with clue bank, cause and effect from environment; reading level suits grade 4. |
| us-hist-1 #1 After the French and Indian War | civics G8 to US History I (G11) | fit | Map comparison and two adapted sources; at or below grade 11. |
| us-hist-1 #13 What to the Slave Is the Fourth of July? | same | fit | Primary source, audience, argument and tone. |
| us-hist-1 #14 Harriet Jacobs in Her Own Words | same | fit | Primary source, purpose and evidence. |
| us-hist-1 #20 Three Amendments, Three Promises | same | fit | Amendment text, chart, court cases. |
| us-hist-1 #23 Carnegie's Gospel of Wealth | US History II to I | fit | Two-source comparison; the Gilded Age row is in this course's concept list. |
| us-hist-hs #1 Who Is Missing From This Archive? | same course, renumbered | fit | Archive inventory; unchanged grade. |
| us-hist-hs #3 Harlem Renaissance Voices | same | fit | Poem and painting analysis. |
| us-hist-hs #9 Mobilizing the Home Front | same | fit | Data, graph and claims; arithmetic keys checked (6 million, 5.0 times, 38,100). |
| us-hist-hs #13 Brown v. Board and Mendez | same | fit | Court-opinion comparison. |
| us-hist-hs #22 Trace the Documentary's Sources | same | fit | Source tracing. |
| world-hist-7 #54 Greek City-States Map | G6 to G7 (World Geography and Ancient Civilizations II) | fit | Latitude and longitude plotting and geography reasoning suit grade 7. |
| world-hist-7 #57 Roman Republic Government | G6 to G7 | fit | Diagram, checks and balances, comparison with the US branches. |
| world-hist-hs #10 Procopius on Justinian and Theodora | G7 to World History I | fit | Two sources by one author, purpose and audience; suits high school. |
| world-hist-hs #16 Black Death Spread Map | G7 to World History I | fit | Plotting and trade-route reasoning; on the easy side for high school but the explain items carry the load. |
| world-geo-6 #52 Maya, Aztec, Inca Map | G7 to G6 | fit | Negative coordinates are grade 6 math; vocabulary (chinampas, terraces) is explained in the sheet; sentences short enough. |
| world-hist-hs #21 Zheng He and Columbus Compare | G7 to World History I | fit | Data comparison; keys checked (87, 100, 300, 59). |
| world-hist-2 #1 From Copernicus to Newton | World History I to II | fit | Timeline, matching authorities, explanation. |
| world-hist-2 #10 MAIN Causes of War | same | fit | Sort and argue. |
| world-hist-2 #15 The Great Depression Worldwide | same | fit | Data reading and graph; keys checked. |
| world-hist-2 #19 Wartime Deaths Data | same | fit | Percent calculations all re-checked against the table. |
| world-hist-2 #26 Winners and Losers of Globalization | same | fit | Evidence sort and weighing. |

## Checks

- `python -X utf8 scripts/worksheets.py`: 1008 built worksheets in 206 units, 0 problems.
- `python -X utf8 scripts/check_worksheets.py`: 7117 worksheets checked, 15 problems. All 15 are existing "module has 0 sheets, want at least 1" coverage gaps in other classes; none touch the 27 sheets read here or the edit.

## Could not settle

- Standards are not named on the sheets themselves (they come from the concept row's topic), so the standards check was against the row and the course frame only, not a standards crosswalk.
- ss-3 #41 (Ohio timeline, 10 events, Treaty of Greenville and removal of the Wyandot) is on the heavy side for grade 3 in sentence length. Left as is; a teacher read at the Desk could decide whether to shorten.
- The six us-hist-1 sheets were written for a grade 8 civics class and now sit in a grade 11 course. They are already document-analysis work, so no change, but the course frame may want stronger sourcing questions later (a scope call, not made here).
