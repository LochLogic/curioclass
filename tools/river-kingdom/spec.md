# River Kingdom

## One idea
The child runs a farming kingdom twice, first on the Nile, whose flood rises on a steady schedule each late summer and drains before planting, then on the Tigris and Euphrates, whose floods come hard in spring just as the grain ripens; each year they assign workers to canals, dikes, granaries and scribes and settle disputes from a case pile by carving a rule in stone, and the same tools lead to different results: Egypt's steady river suits one ruler over a long valley, while Mesopotamia's risky rivers bring walled city-states, strict water laws, constant repair and fields slowly turning salty, until the child's carved laws are laid beside real ones from Hammurabi's code, so a sixth grader learns how each river shaped its people's land, work and government.

## Not like
- hunter-to-farmer (6, spec): the start of farming. Here two early kingdoms built on farming.
- museum-label-writer (6, spec): how writing began. Here what scribes and laws were for.
- tenochtitlan-builder (7, concept): engineering a lake city. Here two river valleys.
- rome-republic-to-empire (6, spec): a government changing over a century. Here how a river shapes a government.

## Who and how
- Grade 6, Social Studies (World History, Geography and Civics), module "Mesopotamia and Egypt". Standards: D2.His.1.6-8 (analyze connections among events and developments in broader historical contexts), D2.Geo.4.6-8 (explain how cultural patterns and economic decisions influence environments and the daily lives of people in both nearby and distant places), D2.Civ.5.6-8 (explain the origins, functions, and structure of government with reference to the U.S. Constitution, state constitutions, and selected other systems of government).
- Format: tycoon. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Two valleys, ten years each, then the compare board and the laws wall. Extra: "What if the Nile failed?" (a run of low floods, as happened at times in Egypt's history). tool.json `modes: ["Two rivers", "Low Nile"]`, `minutes: "30-40"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.4.6-8 | Each year assign ten worker teams to canals, dikes, drainage or fallow, granaries and scribes | harvest, granary, the salt meter, dike strength, and how villagers' days change | 2 |
| D2.Civ.5.6-8 | Settle cases by carving a rule; see who makes rules in each valley (a pharaoh's officials, a city's king and temple) | the case pile, the child's stone, and the government chart for each valley | 3 |
| D2.Civ.5.6-8 (real laws) | Lay the child's laws beside real laws from Hammurabi's code and mark what matches | the laws wall | 4 |
| D2.His.1.6-8 | Fill the compare board and link each valley's choices to its river and to the wider Near East | the compare board and its map | 5 |

## Screens and modes
Header (kit): title "River Kingdom"; `Two rivers`, `Low Nile`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two river valleys side by side: the long, narrow Nile with desert on both sides, and the wide plain between the Tigris and Euphrates, sealed with a clay seal until the Nile is played. A season wheel for each (Egypt: flood, growing, harvest; Mesopotamia: plow and sow in autumn, grow over winter, harvest and flood in spring). The welcome is queued (`welcomeAfter: true`): "You'll rule two farming kingdoms, one on each river. Start on the Nile. Drag your worker teams to jobs, then tap Run the year." First hint: "Drag a worker team to a job."

**A year (focus: the valley and the job board).** At 1366x768 the valley fills the top with meters at the side and the job board below; at 680x425 the job board is a drawer.
- Ten worker teams; jobs: Dig canals (spread water farther), Build and repair dikes, Drain and rest fields (fallow), Fill granaries, Train scribes (records of fields, grain and taxes).
- Nile rules: the flood comes each late summer and drains by autumn, leaving fresh silt; the flood height varies (a high or low year about one in five, read from the nilometer); canals and granaries pay off steadily; fields don't turn salty because the flood washes salt away.
- Tigris and Euphrates rules: the spring flood comes as the grain ripens; unless dikes are kept strong, a big flood about one year in three breaks through; canal water left standing in hot fields leaves salt behind, so without drainage and fallow the salt meter rises, wheat yields fall and the child must switch to barley, which stands more salt.
- Meters: Harvest, Granary, Salt (Mesopotamia only), Dikes, Scribes (records), People's days (a villager card that says how the year went).
- The case pile: one or two disputes a year, e.g. "My neighbor didn't repair his dike, and the flood ruined my field." "A man opened his ditch and forgot to close it; my barley drowned." "Who owns the new land the flood left?" The child picks a rule from three tiles and it is carved on the kingdom's stone.

**Who makes the rules.** A government chart for each valley: Egypt, one pharaoh over the whole valley, officials and scribes counting fields and taxes, a single system along one river road; Mesopotamia, many walled city-states (Ur, Uruk, Lagash, Umma), each with a king and temple, sometimes fighting over water, later united under kings like Hammurabi of Babylon. A real case card: around 2500 BCE, Lagash and Umma fought for generations over a strip of farmland and its canals.

**The laws wall (the aha).** The child's carved laws appear beside real ones from Hammurabi's code (about 1750 BCE), in plain words: if a man is too lazy to keep his dike strong and a break floods the fields, he must repay the grain lost (law 53); if a man opens his ditch carelessly and floods his neighbor's field, he pays for the neighbor's loss (law 55). The child marks Same idea, Different, or Stricter. Narrator: "A risky river made water rules matter. Hammurabi carved them in stone so everyone could know them."

**The compare board.** Rows the child fills from tiles: When the flood comes; How safe it is; Salt; Who rules; How many states; What laws stress. A small map links both valleys to the wider Near East (trade in timber, stone and metals neither valley had). Narrator: "Two rivers, the same tools, two different kingdoms."

**Low Nile (extra).** Three low floods in a row; the granaries the child filled decide whether villages go hungry, and the narrator notes that low floods at times weakened Egypt's rulers.

**The end.** Both valleys' ten-year lines, the stone of laws, the laws wall and the compare board. `Print` prints them.

## Content
- Two valleys' rules (made for this game, tuned to the history below), ten years each, about 15 case cards, the government charts, the Lagash and Umma card, two Hammurabi laws in plain words (with the full translation a tap away), the compare board.
- The kingdoms the child runs are made for this game and labeled; the rivers, seasons, salt, barley, city-states, pharaohs and laws are real.
- The comparison is a simplification, and a note says so: Egypt had hard years and Mesopotamia had long peaceful stretches.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Teams drag or tap-then-place; the board always totals ten.
- A case must be settled before `Run the year`.
- Keyboard: Tab to teams, jobs and case tiles; arrows move teams; Enter to place or carve.
- With Motion off the flood rises without animation and the meters jump.

## Look
- Accent `--brand` #2f6b2f river-field green (header, jobs, the stone frame); gold #f4c542 (grain in the granary, the chosen tile); paper #f1f6ef; ink #0c200c; muted #4f5a4d.
- Contrast (WCAG 2.1, computed): white on brand 6.43:1; brand on paper 5.87:1; ink on paper 15.62:1; muted on paper 6.61:1; ink on gold 10.52:1.
- Never color alone: the salt meter shows white crystals and a number; flood years carry a wave icon and words.
- Different from this batch (field trip teal, museum terracotta, smoke slate, lake blue).

## Art
- Public domain (Met Open Access, ids checked at build for the open-access flag): an Egyptian model of a granary or of farmers (Middle Kingdom); a Mesopotamian clay tablet of field or grain records; a cast or photo of the Code of Hammurabi stele (Louvre photo with a public-domain or open license). Each with credit.
- Local FLUX (`scripts/localart.py`): the Nile valley across three seasons (3, 16:9); the Mesopotamian plain across three seasons (3, 16:9); a salty field and a barley field (2, 1:1).
- People art goes to Gemini with `people: true`: an Egyptian scribe, a Mesopotamian farmer, villagers for the day cards (4; cutout yes).
- Drawn in code: the job board, meters, stone, laws wall, compare board, the Near East map.
About 15 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `firm-captain` as the overseer who reports each year and reads cases. `Curio.voice` with `scope: () => state.mode + ':' + state.valley + ':' + state.year + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `assign`: "Drag your worker teams to jobs, then tap Run the year."
- event, whole, each year's report.
- how `case`: "Pick a rule to settle this case."
- event, whole, floods, breaks and salt warnings.
- how `wall`: "Mark each pair: same idea, different or stricter."
- how `compare`: "Fill each row of the compare board."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: two rule sets in a small table, the job board, meters with the salt build-up, the case pile and stone, the laws wall and the compare board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Mesopotamia | Copy the Nile plan | Without dikes a big flood breaks through and without drainage the salt meter climbs; the overseer names why. |
| Cases | Pick any rule | Every rule is carved; the laws wall shows how it compares to Hammurabi's, which is the lesson. |
| Compare | Fill both columns the same | Each cell checks; "When the flood comes" with the same answer plays "Look at the season wheels." |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `assign`.
2. Yearly report (whole), waits; `case`; events (whole).
3. Second valley, same.
4. `wall`; `compare`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.6-8, D2.Geo.4.6-8 and D2.Civ.5.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The Nile flood came each late summer on a steady schedule, measured by nilometers | Encyclopaedia Britannica, "Nile River" and "Nilometer" | Met Heilbrunn Timeline, "Egypt in the Predynastic and Early Dynastic periods" | yes |
| Mesopotamian floods came in spring near harvest and could be violent | Encyclopaedia Britannica, "Mesopotamia: the land" | University of Chicago Oriental Institute (ISAC), "Mesopotamian agriculture" | yes |
| Irrigation salted southern Mesopotamian fields; farmers shifted from wheat to barley | Jacobsen and Adams, "Salt and Silt in Ancient Mesopotamian Agriculture," Science (1958) | Encyclopaedia Britannica, "Salinization" | yes |
| City-states such as Ur, Uruk, Lagash and Umma; the Lagash and Umma border war over farmland and canals | Met Heilbrunn Timeline, "Early Dynastic Sumer" | Louvre, "Stele of the Vultures" | yes |
| Hammurabi's code, about 1750 BCE; laws 53 and 55 on dikes and ditches | Yale Avalon Project, "The Code of Hammurabi" (L. W. King translation) | Louvre, "Law Code of Hammurabi" | yes |
| Egypt unified under one king around 3100 BCE; low floods at times weakened rulers | Met Heilbrunn Timeline, "Egypt: Early Dynastic" and "First Intermediate Period" | Encyclopaedia Britannica, "Ancient Egypt" | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-09): the job board totals ten teams in every year; a one-in-three big flood gives about three breaks in ten years without dikes; Hammurabi (about 1750 BCE) comes after Egypt's unification (about 3100 BCE) and the Lagash and Umma war (about 2500 BCE); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 valley and job board fit; at 680x425 the board is a drawer.
2. Each valley's year runs by its own river rules; salt builds only in Mesopotamia. (D2.Geo.4.6-8)
3. Cases are carved on the stone; each valley's chart shows who rules. (D2.Civ.5.6-8)
4. The laws wall pairs the child's laws with laws 53 and 55. (D2.Civ.5.6-8)
5. The compare board checks and the Near East map links both valleys. (D2.His.1.6-8)
6. Low Nile runs three low floods.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animated floods; no network requests.

## Open questions
- Sensitivity flag: the two-river comparison is simplified (default used: a note on the board says Egypt had hard years and Mesopotamia long calm ones; fresh-agent read for accuracy before build).
