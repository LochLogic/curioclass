# The Shrinking Lake

## One idea
The child slides through sixty years of Lake Chad, where Chad, Cameroon, Niger and Nigeria meet, on real satellite images: open water of about 25,000 square kilometers in 1963 shrinks by roughly nine-tenths by the 1980s as drought hits and irrigation grows, while the people of the basin multiply; a herder, a farmer and a fisher explain how their lives moved with the water, and at four decision points the four countries choose to build dams and canals, share water rules or do nothing, with a modeled effect on cooperation and conflict; at the end a cause board separates natural causes from human ones, with the honest note that scientists weigh them differently and that the lake has partly recovered since the 1990s, so a sixth grader learns how long-term human change to the environment shapes where people compete or cooperate, and how moving populations change land use.

## Not like
- five-themes-field-trip (6, spec): one city, building a map. Here sixty years of one lake on a timeline.
- region-compare (6, spec): comparing regions in data. Here one place changing.
- hunter-to-farmer (6, spec): ancient farming. Here farming, herding and fishing today.
- settle-the-valley (4, spec): settlers changing a valley. Here four countries sharing a lake.

## Who and how
- Grade 6, Social Studies (Geography), module "The Shrinking Lake". Standards: D2.Geo.9.6-8 (evaluate the influences of long-term human-induced environmental change on spatial patterns of conflict and cooperation), D2.Geo.12.6-8 (explain how global changes in population distribution patterns affect changes in land use in particular places).
- Format: timeline. Driver: one child alone, or four students as the four countries (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- A decade slider from the 1960s to the 2020s, three people, four decision points, the cause board. Extra: Four countries (each student chooses for one country at each decision point). tool.json `modes: ["The lake", "Four countries"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.12.6-8 | Move the slider and turn on the population and land-use layers | the population counter; farm, pasture and fishing areas moving onto the old lakebed | 2 |
| D2.Geo.12.6-8 (people) | Follow the herder, farmer and fisher to where they moved | three paths on the map with each person's card | 3 |
| D2.Geo.9.6-8 | At four decision points choose a response for the countries and see the modeled effect on cooperation and conflict | the cooperation meter and its reason line; the Lake Chad Basin Commission card | 4 |
| D2.Geo.9.6-8 (causes) | Sort cause cards into Natural, Human or Both and read the scientists' disagreement | the cause board and the note | 5 |

## Screens and modes
Header (kit): title "The Shrinking Lake"; `The lake`, `Four countries`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A satellite view of Lake Chad in the 1960s: wide open water edged with marsh. Four border markers where Chad, Cameroon, Niger and Nigeria touch the shore. A decade slider at the bottom, set to 1963. The welcome is queued (`welcomeAfter: true`): "This is Lake Chad in 1963. Four countries share its shore, and millions of people depend on it. Drag the slider to watch sixty years go by." First hint: "Drag the decade slider."

**The slider (focus: the image and layers).** At 1366x768 the image fills the center with layers and people at the side; at 680x425 layers and people are tabs.
- Decades: 1963 (about 25,000 square kilometers of open water); 1973 (drought begins to shrink it); late 1980s (open water down to roughly a tenth of 1963, split into a northern and southern pool); 2000s and 2010s (partly recovered in places; the southern pool and wetlands larger); 2020s.
- Layers: open water; marsh and seasonal wetland; farmland and irrigation; pasture; fishing camps; a population counter for the basin (growing from roughly 10 million in the 1960s to over 40 million people today; figures given as estimates).
- Each decade's change shows on the map: farms and pasture following the water onto the old lakebed.

**Three people (D2.Geo.12.6-8).** Made for this game, built from real accounts:
- Hawa, a herder in Chad: her family's cattle followed the water south and onto the dry lakebed, where grass grew.
- Musa, a farmer in Niger: he planted on the newly dry soil and later used pumps to irrigate.
- Bello, a fisher in Nigeria: when the water left his village, he moved his boat and family to the islands farther in.
Each one's path appears on the map; the child reads where and why each moved.

**Decision points (D2.Geo.9.6-8).** Four moments, each with three choices and a modeled result (made for this game, with real history named beside it):
1. 1964: the four countries form the Lake Chad Basin Commission (real). Choice: share data and rules; each country for itself; build big dams upstream.
2. 1970s to 1980s: drought and dams on the rivers that feed the lake. Choice: limit new dams; keep building; share water by agreement.
3. 1990s to 2000s: farmers, herders and fishers crowd onto the shrinking shore and quarrel over land and water. Choice: shared grazing and fishing rules; let each group fight it out; move people away.
4. 2010s: armed conflict in the region (the Boko Haram insurgency) has forced millions from their homes, and the shrinking of fishing and farming work is one of several pressures researchers name. A long-discussed plan (Transaqua) would carry water from the Congo basin. Choice: work together on security and livelihoods; build the canal first; do nothing.
- The cooperation meter moves with each choice and a reason line says why ("Shared rules lowered quarrels over grazing"); the narrator always notes the real choices and that the model is a simplification.

**The cause board (the aha).** Cause cards to sort into Natural, Human or Both: less rain in the Sahel from the 1970s; irrigation pulling water from the rivers and lake; dams on rivers that feed the lake; more people needing water and land; a shallow lake that spreads and shrinks fast; a changing climate. Then the note: "Scientists don't fully agree. A 2001 study found drought was the main cause, with irrigation adding a large share in the driest years. Later satellite studies found the lake partly recovered since the 1990s, and groundwater rose." Narrator: "When the water changed, people moved, and that brought both quarrels and cooperation."

**The end.** The 1963 and today images side by side, the people's paths, the meter's record and the cause board. `Print` prints them.

**Four countries (extra).** Four students each choose for one country at each decision point; cooperation rises only when most agree.

## Content
- Six decade images, five layers, the population counter, three people with paths, four decision points with three choices each, the cause board with six cards and the note.
- Hawa, Musa and Bello and the cooperation model are made up and labeled; the images, areas, commission, conflict and studies are real.
- The conflict is named plainly, without images of violence, and with a teacher note.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The slider snaps to decades; layers toggle on and off.
- Decision points open as the slider passes them; each needs a choice before the slider moves on.
- Keyboard: Tab to the slider, layers, people and choices; arrows move the slider; Enter to choose.
- With Motion off images swap without fading and the counter jumps.

## Look
- Accent `--brand` #0f5f86 lake blue (header, slider, water layer); gold #f4c542 (the current decade, the chosen response); paper #eef5f9; ink #05202d; muted #4b5961.
- Contrast (WCAG 2.1, computed): white on brand 7.00:1; brand on paper 6.35:1; ink on paper 15.24:1; muted on paper 6.57:1; ink on gold 10.32:1.
- Never color alone: layers carry patterns (water plain, marsh dotted, farms striped, pasture hatched) and labels; the meter shows a number.
- Different from this batch (field trip teal, river green, museum terracotta, smoke slate).

## Art
- Public domain: NASA and USGS Landsat images of Lake Chad for 1963 (or the earliest available, 1972 to 1973 Landsat 1), 1987, 2001, and recent years (NASA Earth Observatory and USGS EarthExplorer), each with credit.
- People art goes to Gemini with `people: true`: Hawa with cattle, Musa in his field, Bello with his boat (3; cutout yes); dress from published photos of the region.
- Drawn in code: layers, paths, the counter, decision cards, the meter, the cause board.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `wise-mentor` as the three people's card reader (third person, read by one voice). `Curio.voice` with `scope: () => state.mode + ':' + state.decade + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each decade card.
- how `layers`: "Turn on a layer to see what changed."
- event, whole, each person's card.
- how `decide`: "Pick what the four countries do."
- event, whole, each decision result.
- how `causes`: "Sort each cause: natural, human or both."
- event, whole, the scientists' note.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the decade slider with image layers, people paths, decision points with a small cooperation model, the cause board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Slider | Jump to the end | Decision points must be answered in order; the slider stops at each. |
| Decisions | Always choose "do nothing" | The meter falls and the reason lines say why; the end shows the real choices beside the child's. |
| Causes | Put everything in Natural | Irrigation and dams in Natural play "Who built that?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Decade cards (whole), each waits.
2. `layers`; people cards (whole).
3. `decide`; results (whole).
4. `causes`; note (whole); `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.9.6-8 and D2.Geo.12.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Open water about 25,000 square kilometers in 1963; shrank by about nine-tenths by the 1980s | UNEP, Africa's Lakes / GRID (Lake Chad) | NASA Goddard (2001), "Lake Chad nearly vanished" | yes, figures given as "about" |
| Drought was the main cause with irrigation adding a large share in dry years | Coe and Foley, Journal of Geophysical Research (2001), summarized by NASA Goddard (2001) | UNEP Lake Chad assessments | yes, with differing weights, named in the note |
| The lake has partly recovered since the 1990s; groundwater rose | Pham-Duc et al., "The Lake Chad hydrology under current climate change," Scientific Reports (2020) | AFP Fact Check on the lake's size (2018 to 2019) | yes |
| The Lake Chad Basin Commission founded in 1964 by Chad, Cameroon, Niger and Nigeria | Lake Chad Basin Commission, "History" | Encyclopaedia Britannica, "Lake Chad" | yes |
| Basin population grew to tens of millions | Lake Chad Basin Commission | FAO, Lake Chad Basin profile | yes, as estimates |
| The Boko Haram conflict displaced millions in the basin; shrinking livelihoods named as one pressure | UN OCHA, Lake Chad Basin crisis overview | adelphi, "Shoring up stability" climate-security report (2019) | yes |
| The Transaqua inter-basin water transfer proposal | Lake Chad Basin Commission, Transaqua feasibility work | The New Humanitarian, reporting on Transaqua | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the region's armed conflict and displacement are named plainly with sources, without images of violence, and the lake is shown as one of several pressures, not the single cause. The three people are made up and drawn from real accounts. A fresh-agent read of the decision cards and people cards is needed before build.

Checks run (Python, scratchpad r11, 2026-11-09): 25,000 square kilometers shrinking by nine-tenths leaves about 2,500, matching the 1979 to 1986 range in published measurements (about 2,300 to 4,500); the four decision points fall in decade order (1964, 1970s to 80s, 1990s to 2000s, 2010s); each cause card has one right column; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 image with side panels; at 680x425 tabs.
2. The slider shows six decades with layers and the counter. (D2.Geo.12.6-8)
3. Three people's paths show where and why they moved. (D2.Geo.12.6-8)
4. Four decision points move the cooperation meter with reasons. (D2.Geo.9.6-8)
5. The cause board checks and shows the scientists' note. (D2.Geo.9.6-8)
6. Four countries mode takes four choices.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fading; no network requests.

## Open questions
- Sensitivity flag: armed conflict and displacement around the lake are named plainly (default used: sourced facts, no images of violence, the lake shown as one pressure among several, teacher note, fresh-agent read before build).
