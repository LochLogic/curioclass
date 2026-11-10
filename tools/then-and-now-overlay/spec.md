# Then-and-Now Overlay

## One idea
The child drags a fade slider over one real block of Main Street in Marshalltown, Iowa, to see it in the 1890s, in 1939 and today, built from public-domain sources (an 1894 Sanborn fire insurance map, the 1896 city directory, an 1868 bird's-eye view drawing, and a 1939 Farm Security Administration photograph), taps a building in each period to see what each kind of source says about it (the map tells what it was built of and used for, the directory tells who ran it, the photo shows what it looked like), finds the one spot where two sources don't agree, and lines up the street's changes with what was happening across the country at the same time, so a third grader learns that each kind of source answers a different question about the past.

## Not like
- then-and-now-flip (K, spec): picture pairs of everyday objects. Here one real street across three periods, read through real sources.
- capsule-from-1965 (1, spec): four made-up objects read for maker, date and place. Here real public-domain documents compared.
- state-story-timeline (4, concept): statewide events. Here one street beside national events.
- map-maker (3, spec, this batch): making a map. Here reading old maps as sources.

## Who and how
- Grade 3, Social Studies (History), module "Local History". Standards: D2.His.1.3-5 (create and use a chronological sequence of related events to compare developments that happened at the same time), D2.His.2.3-5 (compare life in specific historical time periods to life today), D2.His.9.3-5 (summarize how different kinds of historical sources are used to explain events in the past), D2.His.10.3-5 (compare information provided by different historical sources about the past).
- Driver: one child alone, or the teacher on the projector; `Read` reads every label and line (tool.json `driver: "either"`). Controls 44 px or more.
- Three periods on one slider, a same-time strip, a kid's-life compare. Extra: Your town (teacher template). tool.json `modes: ["Main Street", "Same time", "Kid's life", "Your town"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.
- The page names Marshalltown as a real place and credits every source item under the slider ("Library of Congress" and item numbers).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.9.3-5 | Tap a building in a period and open each source tab (Map, Directory, Picture); match each source to the question it answers: "What was it made of?", "Who ran it?", "What did it look like?" | the source tabs and the matched question cards | 2 |
| D2.His.10.3-5 | Find the building where the map and the directory (or the 1868 drawing and the 1894 map) disagree, and pick a reason they might | the two sources side by side with the difference lit | 3 |
| D2.His.1.3-5 | Drag street events and national events onto the same-time strip | the strip with two rows (Our street, Our country) and decade marks | 4 |
| D2.His.2.3-5 | Compare a kid's day on the street in the 1890s with today: getting there, buying things, light at night | the two-column kid's life card | 5 |

## Screens and modes
Header (kit): title "Then-and-Now Overlay"; `Main Street`, `Same time`, `Kid's life`, `Your town`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Today's Main Street block (an illustrated scene, made for this tool from the street's current layout) with a slider under it and three tabs: 1890s, 1939, Today. The welcome is queued (`welcomeAfter: true`): "This is Main Street in Marshalltown, Iowa, today. Drag the slider to go back in time." First hint: "Drag the slider to the left to go back in time."

**Main Street (focus: the street and the slider).** At 1366x768 the street fills the top two thirds and the source panel sits below; at 680x425 the source panel opens as a sheet over the street.
- The slider fades between three aligned layers:
  - 1890s: the 1894 Sanborn map sheet for this block, cropped and aligned to the street, with the 1868 bird's-eye view as a toggle (`Drawing`).
  - 1939: the FSA photograph of Main Street (Library of Congress, FSA/OWI collection, "Tallcorn, Main Street", September 1939, LC-USF33-003344-M2), placed so its buildings line up.
  - Today: the illustrated street.
- Six buildings on the block are tappable in every period (the build picks the six from the items below; see Build notes). Each opens the source panel with the sources that exist for that period:
  - Map tab (1890s): the Sanborn key decoded in plain words: pink means brick, yellow means wood frame, blue means stone; the label tells the use ("Hardware", "Drugs", "Livery").
  - Directory tab (1890s): the 1896 directory line for that address (business and owner's name).
  - Picture tab (1890s: the 1868 drawing; 1939: the photo; Today: the illustration).
- Matching: three question cards ("What was it made of?", "Who ran it?", "What did it look like?") are dragged to the tab that answers them, once per period. Wrong: "Does a [source] show that? Look again."
- Sources disagree: one building is marked by the build where two sources differ (for example the 1894 map labels a different business than the 1896 directory lists at that address, or the 1868 drawing shows an empty lot where the 1894 map shows a brick block). The child picks a reason from three: "Two years passed, and the shop changed" / "One source made a mistake" / "Both could be right at different times". The tool accepts the first and third and says: "Sources from different years can both be right. That's why historians check the date."

**Same time (focus: the strip).** Two rows across 1860 to today: Our street (top) and Our country (bottom). Eight event cards to drag:
- Street (from the sources): the 1868 drawing shows the young town; the 1894 map shows a brick Main Street and a livery stable; the Hotel Tallcorn on Main Street (opened 1928) towers over the street in the 1939 photo; cars park along the curb in 1939.
- Country: the first railroad across the country (1869); electric lights spread to towns (1880s to 1910s); cars replace horses for most families (1910s to 1920s); the Great Depression (1930s).
- When placed, lines join street and country events that fit together ("The livery stable rented horses. Once cars came, livery stables closed.").

**Kid's life (focus: two columns).** "A kid on Main Street in the 1890s" and "You today". Rows with picture choices: how you got to Main Street (walked or rode in a wagon / car or bus), where you bought candy (the general store or drugstore / a supermarket), light at night (gas or oil lamps, early electric / electric), what you'd see on the street (horses / cars). The 1890s column is filled from the sources by the child (each choice cites the source it came from); the Today column is the child's own.

**Your town (extra).** A teacher template: upload or paste links for up to three images per period (a map, a photo, a directory page) and up to six building spots; nothing leaves the page.

## Build notes
- The build confirms each item before use and records its catalog link in the tool's credits: the 1894 Sanborn map of Marshalltown (Library of Congress Sanborn Maps collection; reprint listings of the 1894 sheets confirm it exists), the 1868 bird's-eye view (Library of Congress, g4154m.pm002220), the 1939 FSA photo (LC-USF33-003344-M2), and the 1896 city directory (transcription on IAGenWeb Marshall County; the build checks a page image, if one exists, for the six addresses).
- The six buildings are the six on the photo's block that appear on the 1894 map and in the 1896 directory. The disagreement must be a real one found in these sources. If no real one is found, the drawing-versus-map difference is used instead.
- If any item can't be confirmed as public domain, the build stops and asks Cory (see Open questions).

## Content
- Three aligned period layers; six buildings with up to three sources each; three question cards; one disagreement; eight same-time cards; four kid's life rows.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The source panel's tabs show only the sources that exist for the chosen period. `Drawing` shows only in the 1890s.
- Keyboard: the slider moves by arrow keys in three steps and fine steps with Shift; Tab moves between buildings.
- With Motion off the slider snaps between periods instead of fading.

## Look
- Accent `--brand` #6b4a2b old print sepia (header, the slider, panel frames); gold #f4c542 (the selected building, the disagreement mark, matched cards); paper #f8f3ec; ink #22160b; muted #5f5548. The Sanborn colors stay as printed, always with their words.
- Contrast (WCAG 2.1, computed): white on brand 7.96:1; brand on paper 7.21:1; ink on paper 16.02:1; muted on paper 6.61:1; ink on gold 10.87:1.
- Never color alone: the Sanborn key is always shown in words.
- Different from this batch (day-in-the-life clay, promise navy, map-maker forest green, pool aqua).

## Art
- Public domain (Library of Congress, credited): the 1894 Sanborn sheet, the 1868 bird's-eye view, the 1939 FSA photo (3 images, cropped and aligned).
- Local FLUX (`scripts/localart.py`): today's street (1, matched to the photo's view, no real business signs or brand names); kid's life pictures (8, 1:1).
- Drawn in code: the slider, building hit areas, the source panel, cards, the same-time strip.
About 12 images. No people art (people in the 1939 photo are as photographed).

## Voice
Bank voice `wise-mentor` as the narrator (unique in this batch). `Curio.voice` with `scope: () => state.mode + ':' + state.period + ':' + state.building`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event `period`: "The 1890s." / "1939." / "Today."
- how `tap-building` (once): "Tap a building to see what the sources say."
- event, whole, each source's plain-words reading.
- how `match`: "Drag each question to the source that answers it."
- event, whole, `disagree`: "These two sources don't agree. Why might that be?" then the reply.
- how `same-time`: "Drag each event to its row and year."
- event, whole, each joining line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (the idea card names history-overlay, but no tool or engine exists for it and data/tools-concepts.csv lists this tool as family none). Tool-only code: aligned layers with a fade slider, building hit areas per period, the source panel, the strip.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Matching | Drag in order | Tab order differs per period, and periods lack some tabs. |
| Disagreement | Pick any reason | "One source made a mistake" gets a follow-up asking to check the dates; the lesson plays either way. |
| Same time | Drag by guess | Cards snap only within their decade and row; wrong drops name the date to look for. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Slider: `period`; `tap-building` (once).
2. Tap a building: a source reading (whole); `match`.
3. The marked building: `disagree` (whole).
4. Same time: `same-time`; drops; joining lines (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1, 2, 9 and 10 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| A Sanborn map of Marshalltown from 1894 exists (Library of Congress collection) | Hometown History Maps, reprint listing of "Sanborn Fire Insurance Map from Marshalltown, Marshall County, Iowa, 1894" | UC Berkeley Library, Union List of Sanborn Maps, Iowa | partly (build confirms on loc.gov) |
| The 1868 bird's-eye view of Marshalltown is in the Library of Congress | loc.gov item g4154m.pm002220 (search result, 2026-11-09) | Library of Congress Panoramic Maps collection | yes |
| An FSA/OWI photo "Tallcorn, Main Street, Marshalltown, Iowa" dates from September 1939 | Library of Congress FSA/OWI collection, LC-USF33-003344-M2 | NYPL and other FSA print listings | yes |
| The 1896 Marshalltown city directory is transcribed online | IAGenWeb Marshall County, "What's new" (complete upload noted October 11, 2020) | Library of Congress, U.S. City Directories on Microfilm, Iowa (Marshalltown 1891-1932) | yes |
| Sanborn map colors: pink brick, yellow frame (wood), blue stone | Library of Congress, "Sanborn Maps: Map key" | Penn State Libraries, Sanborn map key guide | yes |
| FSA/OWI photos and Sanborn maps published before 1930 are free to use | Library of Congress, FSA/OWI rights statement | Library of Congress, Sanborn Maps rights statement | yes |
| The transcontinental railroad was finished in 1869; cars replaced horses for most families by the 1920s; the Great Depression was in the 1930s | Library of Congress, "The Transcontinental Railroad" | Smithsonian National Museum of American History, "America on the Move" | yes |
Backed twice: 7. Cut: 0. The 1894 Sanborn existence rests on reprint and union listings; the build confirms the loc.gov item before use.

Checks run (Python, scratchpad r5, 2026-11-09): the slider's three stops map to 1894/1896 (1890s), 1939 and today; same-time cards sort into rows of four and four with decades 1860s to 1930s; 1896 minus 1894 is two years (the "two years passed" reason); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 street and panel fit; at 680x425 the panel opens as a sheet.
2. Question cards match only their source tabs in each period. (D2.His.9.3-5)
3. The disagreement shows two real sources side by side and plays the dates lesson. (D2.His.10.3-5)
4. Eight events land in their rows and decades. (D2.His.1.3-5)
5. The kid's life card fills from sources and the child. (D2.His.2.3-5)
6. Every public-domain item shows its credit.
7. `Drawing` is never named outside the 1890s.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the slider snaps; no network requests (images are stored with the tool).

## Open questions
- Marshalltown, Iowa as the built-in town (default used: Marshalltown, because an 1894 Sanborn map, an 1868 bird's-eye view, a 1939 FSA Main Street photo and the 1896 directory all exist); the build confirms each item and stops if one isn't public domain. Fallback town: Grundy Center, Iowa (a 1940 FSA Main Street photo exists).
