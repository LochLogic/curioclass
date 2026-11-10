# State Story Timeline

## One idea
The child taps their state and walks its story along a timeline of six to eight stops, starting with the Native nations whose homelands it is (named as nations, with their homes and ways of life) and running through newcomers, trails and railroads, statehood, hard times and today; at each stop they build questions about who made the change and who it affected, link cause cards to effect cards, and at three stops compare a kid's day then with their own, until a cause-and-effect chain across the whole line shows how one change led to the next and what was gained and lost, and for whom, so a fourth grader learns their state's history as a chain of choices by real people.

## Not like
- my-life-timeline (1, spec, same engine): one child's own life. Here a whole state across centuries.
- revolution-road (concept): national events from three viewpoints. Here one state's events.
- then-and-now-overlay (3, spec): one Main Street in sources. Here the state's whole story.
- settle-the-valley (4, spec): a made-up valley model. Here real state history.

## Who and how
- Grade 4, Social Studies (History), module "State History". Standards: D2.His.2.3-5 (compare life in specific historical time periods to life today), D2.His.3.3-5 (generate questions about individuals and groups who have shaped significant historical changes and continuities), D2.His.14.3-5 (explain probable causes and effects of events and developments).
- Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Family: timeline-maker (engine shared with my-life-timeline; no engine doc yet). The template mode becomes the extra, as the idea card asks: a solo child gets real, written state content by default.
- Scope (the idea card's "too big" flag): every state gets the same shape (six to eight stops, three kid-then cards, twelve cause and effect cards), written and source-checked one state at a time in waves; Nebraska is fully written here as the model and the first to ship (see Open questions). States not yet written show "Coming soon" and offer the teacher template.
- tool.json `modes: ["My state", "Teacher timeline"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.3.3-5 | At each stop, build one question from tiles about who made the change or who it affected (Who decided, Who was hurt, Who gained, Who kept doing) | the stop card with its people and the child's question | 3 |
| D2.His.14.3-5 | Drag cause cards onto the effect cards they led to, across stops | cords joining cards along the timeline | 4, 5 |
| D2.His.2.3-5 | At three stops, compare a kid's day then with the child's own (home, school or learning, chores, fun) | the two-column kid's day card | 6 |

## Screens and modes
Header (kit): title "State Story Timeline"; `My state`, `Teacher timeline`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A U.S. map. The welcome is queued (`welcomeAfter: true`): "Every state has a story. Tap your state to walk through it." First hint: "Tap your state." Written states open their timeline; others say "Your state's story is coming soon. Ask your teacher to make one with Teacher timeline."

**The timeline (focus: one stop at a time).** At 1366x768 the line runs across the bottom with the open stop card above; at 680x425 the line is a scrollable strip and the stop card fills the screen.
- The first stop is always the nations whose homelands the state is, with a map of their homelands, how they lived, and that these nations are still here today.
- Each stop card: a picture (public domain or illustrated), three short sentences, the people involved (named groups and named people where sources allow), and the question builder.

**Nebraska (the model, written in full).** Stops:
1. Homelands (before the 1800s): the Pawnee, Omaha, Ponca, Otoe-Missouria and Lakota nations, among others. Pawnee towns of earth lodges along the Platte and Loup rivers; farming corn, beans and squash in river valleys; summer and winter bison hunts.
2. Trails along the Platte (1840s to 1860s): hundreds of thousands of travelers on the Oregon, California and Mormon trails cross Nebraska along the Platte River, using its water and grass.
3. Treaties and land (1854): the Kansas-Nebraska Act opens the territory to settlers; in treaties that year and after, the Omaha, Otoe-Missouria and other nations give up most of their land for small reservations, often under pressure.
4. Homesteads and the railroad (1862 to 1867): the Homestead Act offers 160 acres to settlers who farm it for five years; the Union Pacific builds west along the Platte; Nebraska becomes a state on March 1, 1867.
5. Removal and Standing Bear (1874 to 1879): the Pawnee move to Indian Territory (today's Oklahoma) in 1874 to 1875; the Ponca are forced south in 1877; in 1879 Standing Bear wins a court ruling that a Native person is a person under U.S. law.
6. Dust and drought (1930s): years of drought and dust storms during the Great Depression; many farm families leave.
7. Today: center-pivot irrigation from the Ogallala Aquifer waters crops; the Omaha Tribe, Ponca Tribe of Nebraska (restored by Congress in 1990), Winnebago Tribe and Santee Sioux Nation have homelands and governments in Nebraska; Nebraska has the only one-chamber state legislature.
- Kid then cards at stops 1, 4 and 6: a Pawnee child in an earth lodge town (from the Pawnee Nation's published history; written with that source), a homesteader child in a sod house, a child during the dust storms.
- Cause and effect cards (12): trails need water and grass; travelers pass through Pawnee and Lakota lands and use up grass and game; the Kansas-Nebraska Act; treaties shrink homelands; the Homestead Act; the railroad brings settlers and ships crops; more settlers want more land; removal of the Pawnee and Ponca; Standing Bear's case; plowing the prairie and drought; dust storms; irrigation from the aquifer.

**Question builder.** Tiles: starters (Who decided, Who was hurt by, Who gained from, Who kept doing their ways during), a middle chosen from the stop's people and events. Example: "Who was hurt by the Homestead Act?" A narrator line answers briefly from the stop's sources.

**Cause and effect.** Cards collect under stops; the child drags a cause onto the effect it led to (for example "The railroad brought settlers" onto "More settlers wanted more land"). Wrong links: "Did this happen before or after? Did it lead to it?" The finished chain lights across the timeline. Narrator: "Each change led to the next. Some people gained, and some lost a great deal."

**Kid's day.** Four rows (home, learning, chores, fun) with picture choices for then; the child fills "me today".

**Teacher timeline (extra).** A blank timeline (the original template): add stops with a title, date, picture and text, and cause and effect cards; prints and saves in this browser only.

## Content
- Shared shape per state: six to eight stops, three kid-then cards, twelve cause and effect cards with a set chain, question tiles from each stop's people.
- Nebraska is written above. Each new state is written to the same rules (Build notes) and source-checked before it ships.

## Build notes
- Every state's first stop names its Native nations as nations, from that nation's own published history where it exists, plus a federal or state source; it says the nations are here today and names those with homelands or governments in the state.
- Treaties, removal and violence are told plainly in kid words, without graphic detail.
- Each state gets a fresh-agent sensitivity read before it ships.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Stops open in order; earlier stops can be reopened. Cause and effect cards appear only after their stop is read.
- Keyboard: arrow keys move along stops; Tab through tiles and cards.
- With Motion off cords appear without drawing.

## Look
- Accent `--brand` #5b3d8a timeline violet (header, the line, stop frames); gold #f4c542 (the open stop, a linked cord); paper #f5f2fa; ink #1a1030; muted #5a5466.
- Contrast (WCAG 2.1, computed): white on brand 8.47:1; brand on paper 7.65:1; ink on paper 16.34:1; muted on paper 6.55:1; ink on gold 11.12:1.
- Never color alone: stops carry dates and titles; cords carry arrows.
- Different from this batch (trade harbor teal, ship's log wood, article red, interest green).

## Art
- Public domain (Library of Congress, credited): for Nebraska, a Pawnee earth lodge photograph (William Henry Jackson, 1871), an Oregon Trail scene, an 1860s Union Pacific photograph, a sod house photograph (Solomon Butcher, Nebraska State Historical Society), a 1930s dust storm photograph (FSA). The build checks each item.
- People art goes to Gemini with `people: true`: the three kid-then cards (1 each), with the Pawnee child drawn from Pawnee Nation and museum references.
- Drawn in code: the timeline, stop cards, tiles, cords, maps.
About 8 images per state.

## Voice
Three bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `playful-friend` as the homesteader child; `big-sister` as the dust storm child. The Pawnee child's card is read by the narrator (see Open questions). `Curio.voice` with `scope: () => state.mode + ':' + state.state + ':' + state.stop`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each stop's text.
- how `ask`: "Build a question about who made this change or who it affected."
- event, whole, each answer line.
- how `link`: "Drag a cause onto what it led to."
- event, whole, `chain`.
- how `kid`: "Fill in your day next to theirs."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
timeline-maker (no engine doc; shared with my-life-timeline): the line, stops, cards and print. This tool adds per-state content files, the question builder and cause-and-effect cords.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Questions | Pick the first tiles | Any question is accepted, but the chain step needs each stop's cards, which open only after a question is built. |
| Cause and effect | Link cards at random | Only the set chain is accepted; a wrong link asks about order and cause. |
| Kid's day | Skip it | The print shows it blank, and the end line asks for it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each stop: text (whole), waits; `ask`; answer (whole).
2. `link`; after the chain: `chain` (whole).
3. Kid stops: `kid`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2, 3 and 14 (3-5) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Pawnee, Omaha, Ponca, Otoe-Missouria and Lakota homelands in Nebraska; Pawnee earth lodge towns on the Platte and Loup | History Nebraska, "Native Americans in Nebraska" | Pawnee Nation of Oklahoma, "History" | yes |
| Oregon, California and Mormon trails ran along the Platte | National Park Service, Oregon National Historic Trail | History Nebraska, "The Great Platte River Road" | yes |
| 1854 Kansas-Nebraska Act and the 1854 Omaha and Otoe-Missouria treaties | National Archives, Kansas-Nebraska Act | Oklahoma State University, Kappler's Indian Affairs: Laws and Treaties | yes |
| Homestead Act 1862; Union Pacific along the Platte; statehood March 1, 1867 | National Park Service, Homestead National Historical Park | Nebraska Secretary of State, "Nebraska statehood" | yes |
| Pawnee removal 1874-1875; Ponca removal 1877; Standing Bear ruling 1879 | History Nebraska, "Pawnee" and "Standing Bear" | National Park Service, "Standing Bear" | yes |
| Ponca Tribe of Nebraska restored by Congress in 1990; Omaha, Winnebago and Santee Sioux nations in Nebraska today | Ponca Tribe of Nebraska, "History" | Nebraska Commission on Indian Affairs, tribes in Nebraska | yes |
| Dust Bowl drought in the 1930s; center-pivot irrigation from the Ogallala Aquifer | National Drought Mitigation Center (University of Nebraska), "Dust Bowl" | USGS, "High Plains Aquifer" | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: treaties, removal and Native history. Each state's first stop names the nations whose homelands it is, from their own sources where possible, and says they are still here; removal is told plainly; a fresh-agent read is needed for every state before it ships.

Checks run (Python, scratchpad r8, 2026-11-09): Nebraska has seven stops in date order; the twelve cause and effect cards form one chain with no loops and every effect after its cause; three kid-then stops; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line and card fit; at 680x425 the card fills the screen.
2. Every written state's first stop names its nations and says they are here today.
3. Each stop accepts a built question and plays its answer. (D2.His.3.3-5)
4. Only the set cause-and-effect links are accepted. (D2.His.14.3-5)
5. The finished chain lights across the timeline. (D2.His.14.3-5)
6. Three kid's day cards fill and print. (D2.His.2.3-5)
7. Unwritten states say "coming soon" and offer Teacher timeline.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no drawn cords; no network requests.

## Open questions
- Scope: 50 written state timelines is a large job (default used: one shared shape, Nebraska written in full as the model and first to ship, other states written and source-checked in waves; unwritten states show "coming soon" and the teacher template).
- Sensitivity flag: Native history, treaties and removal in every state; the Pawnee child is read by the narrator, not a character voice (default used: nations' own published histories, fresh-agent read per state before it ships).
