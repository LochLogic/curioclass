# Suburb Boom

## One idea
The student watches metro Detroit grow from 1940 to today on real aerial photographs, a decade at a time, as four policies arrive and decide who can buy where and what gets built: the 1930s federal lending map that marked Black and immigrant neighborhoods "hazardous", federal home loan rules that insured new suburbs but not older mixed streets, the interstate routes that cut through the Black Bottom and Paradise Valley neighborhoods, and large-lot zoning in the new suburbs; farms turn into subdivisions, streetcars stop, creeks and wetlands are paved, and in 2014 and 2021 floods fill the freeways and basements built where water used to sit; beside the map two made-up families with the same income, one white and one Black, follow the choices each was allowed; then the student changes one policy card (route the highway elsewhere, drop the lending map, allow apartments, keep a wetland) and replays, with the result labeled as a what-if, and at the end compares a then-and-now map of home values and who lives where, so an eleventh grader learns how human and physical systems shape each other, how settlement changed the land and its people, and how economic and political decisions shaped city, suburb and rural patterns.

## Not like
- climate-on-the-move (10, spec): climate moving people. Here policy moving people.
- layers-and-scales (9, spec): reading thematic maps. Here one metro changing by decade.
- who-decides (12, concept): present-day local action. Here eighty years of decisions.
- expansion-map (8, spec): a nation's borders. Here one region's streets.

## Who and how
- Grade 11, Social Studies (U.S. History and Geography), module "Suburb Boom". Standards: D2.Geo.4.9-12 (analyze relationships and interactions within and between human and physical systems to explain reciprocal influences that occur among them), D2.Geo.6.9-12 (evaluate the impact of human settlement activities on the environmental and cultural characteristics of specific places and regions), D2.Geo.8.9-12 (evaluate the impact of economic activities and political decisions on spatial patterns within and among urban, suburban, and rural regions).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Nine decade steps (1940 to 2020), four policy cards, the families panel, one what-if replay, the then-and-now map and the write-up. Extra: Second metro (the same steps for a second city, chosen at build). tool.json `modes: ["Metro Detroit", "Second metro"]`, `minutes: "35-45"`, `grades_label: "Grade 11"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.6.9-12 | Step the decades and mark what settlement changed on the land and in the neighborhoods | the aerial photos with overlays; the change marks | 2 |
| D2.Geo.8.9-12 | Play each policy card, follow the two families, then change one card and replay | the policy shelf; the families panel; the what-if map | 3 |
| D2.Geo.4.9-12 | Trace the wetland thread from paving to flooding and explain the loop | the creek and wetland layer; the 2014 and 2021 flood maps | 4 |

## Screens and modes
Header (kit): title "Suburb Boom"; `Metro Detroit`, `Second metro`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** An aerial photograph of Detroit's northwest edge around 1940: farms, a creek, a streetcar line, a few streets. Below, a policy shelf with four cards face down. A decade dial reads 1940. The welcome is queued (`welcomeAfter: true`): "This is farmland now. In twenty years it won't be. Four decisions will shape what comes, and who gets to live here. Turn the first card." First hint: "Tap the first policy card."

**Decades (focus: the map).** At 1366x768 the aerial fills the left with the families panel and shelf right; at 680x425 the panel and shelf are sheets. Each step swaps in the real aerial for that decade (or the nearest year) with drawn overlays the student can switch on: subdivisions, highways, streetcar lines, creeks and wetlands, the lending map grades.
- The lending map (1939): neighborhoods graded A to D; D, outlined in red and called "hazardous", included most Black neighborhoods.
- Federal home loans (from 1934): insured mortgages in new, all-white subdivisions; the 1938 underwriting manual recommended racial covenants. In 1941 a developer built a half-mile wall along Birwood Street to separate a new white subdivision from a Black neighborhood so the loans would be approved.
- Covenants: Shelley v. Kraemer (1948), a case joined with a Detroit case, ruled courts couldn't enforce them; other barriers stayed.
- Streetcars: the last Detroit streetcar line closed in 1956.
- Highways: the Federal-Aid Highway Act (1956); I-375 and the Chrysler Freeway (I-75) through Black Bottom and Paradise Valley, clearing homes, churches and businesses around 1959 to 1964.
- Zoning: large-lot rules in new suburbs that excluded apartments.
- The Fair Housing Act (April 1968).
- Detroit's population peaked near 1.85 million in 1950 and was about 639,000 in 2020, while the suburbs grew.
- After each step the student marks one change to the land and one to who lives there.

**Families panel (D2.Geo.8.9-12).** Two made-up families with the same income, labeled "made for this tool": at each decade they see the same house ads and a card shows which they could buy, whether the loan would be insured, and where each family ends up. Real figures sit behind each card.

**What-if (D2.Geo.8.9-12).** The student flips one card (route the highway elsewhere, drop the lending map, allow apartments, keep a wetland) and replays from that decade; the map shows a modeled result in a dashed outline, labeled "a what-if, not what happened".

**The wetland thread (D2.Geo.4.9-12).** A creek layer shows streams buried in pipes and wetlands paved from 1950 on; then the August 11, 2014 storm and the June 26, 2021 storm, when water filled freeways and basements across the metro. The student traces the loop: building changed the land, and the land pushed back on the people.

**The end (the aha).** A then-and-now map of home values and who lives where, beside the 1939 lending grades. The write-up: "Settlement changed the land by ___. Decisions about ___ shaped who lives where. The land pushed back when ___." Narrator: "The lines on the 1939 map were drawn in an office. Eighty years later you can still see them from the air." `Print` prints the maps and the write-up.

**Second metro (extra).** The same decade steps for a second metro, chosen at build where aerials and lending maps exist.

## Content
- Nine decade aerials (USGS and local archives), overlays, four policy cards with real dates and rules, two labeled made-up families, the what-if model with its rules stated, flood maps, the then-and-now map.
- Policies, places, dates and figures are real and sourced; the families are made up and labeled.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Decades step forward only after each step's two marks; any past decade can be revisited.
- The what-if opens after 1970 is reached.
- Keyboard: Tab to the dial, the overlays, the shelf, the panel and the marks; arrow keys step decades; Enter flips and marks.
- With Motion off decades swap without a fade and floods appear at full extent.

## Look
- Accent `--brand` #3f6324 suburb green (header, the dial, the shelf); gold #f4c542 (the card in play, a marked change); paper #f3f6ee; ink #132008; muted #535a4b.
- Contrast (WCAG 2.1, computed): white on brand 6.95:1; brand on paper 6.36:1; ink on paper 15.53:1; muted on paper 6.56:1; ink on gold 10.43:1.
- Never color alone: lending grades carry letters and patterns as well as color; overlays carry labels; what-ifs use dashed lines and a label.
- Different from this batch (gilded bronze, archive teal, decade violet, press red).

## Art
- Public domain aerial photographs (USGS EarthExplorer single frames, frame ids and years checked at build); the 1939 lending map redrawn in code from the National Archives original (Record Group 195), with Mapping Inequality (University of Richmond) cited for the digitized boundaries, license checked at build; the Birwood wall from the Library of Congress (1941, Farm Security Administration). Each with credit.
- People (illustrated) for the two made-up families, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Drawn in code: overlays, the dial, the cards.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator and hints; `big-sister` as the families panel reader. `Curio.voice` with `scope: () => state.mode + ':' + state.decade + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each policy card.
- event, whole, each decade summary.
- how `mark`: "Mark one change to the land and one to who lives here."
- event, whole, each families card.
- how `whatif`: "Flip one card and replay."
- how `wetland`: "Trace the creek from paving to flooding."
- how `write`: "Write how the land and the decisions shaped each other."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the decade dial with aerials and overlays, the policy shelf, the families panel, the what-if model, the flood layer.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Decade marks | Tap any spot | Each mark must sit on a changed area and name the change. |
| What-if | Flip a card and skip the replay | The replay must reach 2020 before the end opens. |
| Write-up | Only describe the floods | It needs the land, a decision and the push-back. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Policy card (whole), waits; decade summary (whole); `mark`; families card (whole).
2. `whatif`.
3. `wetland`.
4. `write`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.4.9-12, D2.Geo.6.9-12 and D2.Geo.8.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The 1939 Detroit lending map and its grades | National Archives, Record Group 195, HOLC City Survey Files | Mapping Inequality, University of Richmond | yes |
| Federal home loans from 1934; the 1938 manual recommended covenants | Federal Housing Administration, Underwriting Manual (1938) | Rothstein, "The Color of Law" (Liveright, 2017) | yes |
| The Birwood wall (1941) | Library of Congress, FSA/OWI photograph (1941) | Sugrue, "The Origins of the Urban Crisis" (Princeton, 1996) | yes |
| Shelley v. Kraemer (1948) with the Detroit case McGhee v. Sipes | Shelley v. Kraemer, 334 U.S. 1 (1948) | Sugrue (1996) | yes |
| Detroit's last streetcar line closed in 1956 | Detroit Historical Society | Detroit Department of Transportation history | yes |
| I-375 and I-75 through Black Bottom and Paradise Valley | Detroit Historical Society, "Black Bottom" | Michigan Department of Transportation, I-375 project history | yes |
| Detroit about 1.85 million (1950) and about 639,000 (2020) | U.S. Census Bureau, 1950 Census | U.S. Census Bureau, 2020 Census | yes |
| The August 11, 2014 and June 26, 2021 floods | National Weather Service, Detroit/Pontiac office event summaries | Michigan State Police, emergency declarations | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: redlining, racial covenants, the Birwood wall and the clearing of Black neighborhoods are named plainly; the two families are made up and labeled, and their cards use real rules, never stereotypes. A fresh-agent read is needed before build.

Checks run (Python, scratchpad r20, 2026-11-09): nine decade steps 1940 to 2020; Detroit's 2020 population is about 35 percent of its 1950 peak; the Fair Housing Act came 34 years after federal home loans began; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 aerial, panel and shelf; at 680x425 sheets.
2. Each decade has a land change and a people change marked. (D2.Geo.6.9-12)
3. The families panel and one what-if replay show how decisions shaped where people lived. (D2.Geo.8.9-12)
4. The wetland thread links paving to the 2014 and 2021 floods. (D2.Geo.4.9-12)
5. Lending grades carry letters and patterns, not color alone.
6. What-if results are dashed and labeled.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fades; no network requests.

## Open questions
- Sensitivity flag: redlining, covenants and the clearing of Black neighborhoods (default used: named plainly, made-up families labeled with real rules behind them, no stereotypes, fresh-agent read before build).
- The idea card flags a data source (default used: metro Detroit, lending map redrawn from the National Archives original, Mapping Inequality license checked at build).
