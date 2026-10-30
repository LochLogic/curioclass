# Source Portfolio

## One idea
Build a six-source portfolio for a contested question, "Should the Millbrook Dam come down?", from a shelf of thirteen source cards, and watch four gauges (range of views, kinds of sources, real corroboration, expert standing) while a citation web shows which agreements are independent and which are four pages echoing one press release.

## Not like
- Boolean Builder (library 9-12, wave 2): finds records with search logic. Here the sources are already found; the skill is choosing a balanced set and judging how they depend on each other.
- fake-or-fact-lab (6-8 library, wave 1): lateral reading to decide whether one page is trustworthy. Here every card is what it says it is; the question is how the set works together.
- Research Notebook (ela 9, this group): notes and a cited paragraph from a fixed shelf. Here nothing is written; the product is the set itself.
- Source Mixer (ela 11, this group): weighs four given sources inside one answer. Here the student chooses which sources make the set at all.
- Enduring Questions (library 9-12, this group): expert positions on the lasting issue behind a question. Here the experts appear only as authors and citers of sources.
- missing-voices-archive (social 9-12, not specced): finds who an archive leaves out. Here missing views show on the views wheel, but the whole portfolio, not one archive, is the subject.
- Source Sorter (ela 6), research family, not specced: sorts single sources by credibility. Here grade 9-12 adds origins, echoes and how experts cite a source.

## Who and how
- Library, grades 9-12, module Source Portfolio: "Curating sources across views".
- Topic line: "building a balanced set of sources".
- Standards: AASL.Curate, D1.5.9-12, D3.1.9-12, D3.2.9-12.
- Driver: students on their own laptops or in pairs; works projected for a whole-class build. 20 to 35 minutes.
- tool.json: driver "students", minutes "20-35", modes [] (pure explore), grades_label "Grades 9-12". Kit starter, own light `:root`.

## Screens and modes
Kit frame. Header: "Source Portfolio", small line "Should the Millbrook Dam come down?"; Motion, Sound, Read. Two views as a segmented control, **Shelf** and **Citation web**, plus a **Background** button (the Elwha card, Content).

A slim painted banner of the dam the question is about (art sp-millbrook-dam) runs above both views, the question in code across its blank sky.

**Shelf.** Focus: the card grid, the biggest, central block, with the portfolio and gauges beside it in the panel so each Add shows its effect at once. A grid of 13 source cards like library catalog cards. Each card front shows its title, maker, kind (as a stamp: STUDY, DATA, NEWS, PRESS RELEASE, BLOG, REPORT, MEMO, PREPRINT, WEB PAGE, PAMPHLET, NEWSLETTER) and the view it comes from (a colored tab with the view's word). Tap a card to flip it: the back lists **Origin** (who first produced the information), **Authority** (who wrote it and what they know), **Context** (when, for whom, why), **Structure** (what kind of document, reviewed or not), **Cites** and **Cited by** (card numbers), and **Speaks to** (the key claims, each with its side). Badges on the back: **Peer reviewed**, **Government report**, **Cited by an expert source**, **Preprint**, **Correction notice**, **Paid for by an interested party**. **Add to portfolio** on both faces.

**The portfolio** (panel, top): six slots like folder pockets. Each filled slot shows the card's number, title and view tab, with **Remove**. Under the slots, four **gauges**, each a short bar with a goal tick, its count and a one-line reason:
- **Range of views**: distinct views in the portfolio (goal 4).
- **Kinds of sources**: distinct kinds (goal 3).
- **Corroboration**: key claims covered by at least two independent origins, on either side (goal 4 of 4); its line reads "[n] of 4 claims checked by two independent origins"; tap to see the claim list with origins and their sides.
- **Expert standing**: sources experts value (goal 2).
Under the gauges, **Echo check** lines ("Cards 3, 4 and 5 all trace to card 2's press release. They count as one origin.").

**Citation web.** Focus: the web itself, filling the stage. The 13 cards as nodes (number and view color), arrows from citer to cited, and shaded hulls around sources that share an origin, each hull labeled ("One origin: Hartwell Engineering cost study"). Cards in the portfolio are drawn with a thick ring. Four **claim filters** above the web (Salmon, Sediment, Power, Cost): choosing one lights only sources that speak to it, with + or - marks for side. Tap a node to open its card back in a side drawer.

**Views wheel** (in the panel, below the gauges): seven slices, one per view, filled when the portfolio holds a source from that view, so a missing view is a visible gap.

Panel also holds `#hint` and **Clear portfolio** (asks Yes / No).

## Content
Everything about Millbrook is made up for Curio Class, said on the shelf ("Millbrook, its dam and every source here are made up for this tool. The Background card is real."). No real organization, person or study is named on a card.

The question: "Should the Millbrook Dam come down?" The dam (made up) was built in 1931 on the Sable River, makes a little hydropower, holds Millbrook Lake, and needs repairs.

Key claims: K1 "Salmon would return above the dam." K2 "Sediment behind the dam would harm the river below." K3 "The power the dam makes matters to the region." K4 "Removing the dam would cost about $40 million."

Views (seven, each with a color and word): Tribal fisheries, Lake homeowners, Utility, River scientists, History, Town budget, Recreation. News and government are kinds, not views; their cards carry the view of the people they mainly quote or serve, said on the card.

The shelf (number, title, maker, kind, view; origin; badges; cites; speaks to):
1. "Return of the Run: Salmon Habitat Above Small Dams," two State University biologists, STUDY in a journal, River scientists. Origin: own field surveys and published results from the Elwha River. Peer reviewed. Cites 9. Speaks to K1 + (habitat is there), K2 - (staged release kept sediment manageable on the Elwha).
2. "Removal Would Destroy Our Lake," Friends of Millbrook Lake, PRESS RELEASE, Lake homeowners. Origin: Friends of Millbrook Lake (K2) and card 6 (K4). Advocacy group (no badge). Cites 6. Speaks to K2 + ("toxic mud"), K4 + ("$40 million").
3. "Residents Fear Losing the Lake," Millbrook Gazette, NEWS, Lake homeowners (quotes residents). Origin: card 2. Cites 2. Speaks to K2 +, K4 +.
4. "Save Our Lake!," Lakeside Living blog, BLOG, Lake homeowners. Origin: card 2 (paragraphs copied, credited as "a press release"). Cites 2. Speaks to K2 +, K4 +.
5. "Dam Fight Splits Millbrook," Valley News Online (a neighboring town's site), NEWS, Lake homeowners. Origin: card 3. Cites 3. Speaks to K4 +.
6. "Millbrook Dam: Repair and Removal Options," Hartwell Engineering, REPORT, Utility. Origin: own estimate. Paid for by an interested party (commissioned by Sable Valley Power). Cited by 2 and 7 only. Speaks to K4 + ($40 million to remove, $18 million to repair).
7. "Clean Power from Millbrook," Sable Valley Power, WEB PAGE, Utility. Origin: utility's own records (K3) and card 6 (K4). Cites 6. Speaks to K3 + ("about 6 percent of our supply"), K4 +.
8. "Small Hydropower in Our State," State Energy Office, REPORT, Utility (serves power planning). Origin: state records. Government report. Speaks to K3 + (Millbrook dam about 6 percent of Sable Valley Power's supply; replaceable with other sources).
9. "Fish Counts Below Millbrook Dam, 2015-2025," Upriver Nation Fisheries Department (a made-up tribal government), DATA, Tribal fisheries. Origin: own counts. Cited by an expert source (card 1). Speaks to K1 + (salmon gather below the dam each fall).
10. "The Dam That Built Millbrook," Millbrook Historical Society, PAMPHLET, History. Origin: town records. Speaks to none of K1 to K4 (why the dam and lake matter to the town's story).
11. "Sediment Behind Millbrook Dam: A First Screening," State University geologists, PREPRINT, River scientists. Origin: own samples. Preprint (not yet peer reviewed); Correction notice ("Table 2 units corrected; conclusions unchanged"). Speaks to K2 - (mostly sand and gravel; contaminants low in most samples).
12. "A Free River for Paddlers," Sable River Paddlers Club, NEWSLETTER, Recreation. Origin: card 1. Cites 1. Speaks to K1 +.
13. "Repair or Removal: What Millbrook Would Pay," Millbrook town engineer, MEMO, Town budget. Origin: own estimate. Government report. Speaks to K4 + ($34 million to $42 million to remove, most of it eligible for state and federal river grants; repair paid mostly by the town).

Independent origins per claim (the rule: sources share an origin when one repeats or copies another, or both repeat a third; a cited source that adds its own data is still its own origin):
- K1: origin 1 (cards 1, 12), origin 9 (card 9).
- K2: origin Friends of Millbrook Lake (cards 2, 3, 4), origin 1 (card 1), origin 11 (card 11).
- K3: origin 7 (card 7), origin 8 (card 8).
- K4: origin 6 (cards 2, 3, 4, 5, 6, 7), origin 13 (card 13).
Valued by experts (Expert standing): 1 (peer reviewed), 8 and 13 (government reports), 9 (cited by a peer-reviewed study). Card 11 shows "Not yet reviewed" and does not count, but its correction notice line says "A public correction is a sign the authors check their work." Card 6 shows "Paid for by Sable Valley Power; cited only by the utility and groups repeating it."

Exactly four six-card portfolios meet every goal (checked by script): 1, 2, 7, 8, 9, 13 (five views, six kinds, 4 of 4 claims, 4 valued), the same with card 3 or card 4 in place of card 2, and 1, 7, 8, 9, 11, 13. The tool never names one. 1,048 of the 1,716 possible portfolios meet at least three of the four goals.

Background card (real; Content checked in Sources): "On the Elwha River in Washington, two dams, the Elwha Dam (1913) and the Glines Canyon Dam (1927), were taken down between September 2011 and 2014, the largest dam removal in United States history until the Klamath River dams came down in 2024. The Lower Elwha Klallam Tribe had pressed for removal for decades. Scientists have tracked salmon returning upstream since." Source line on the card.

## Interactions in detail
- Adding: a seventh card asks which slot to replace. The same card can't be added twice. A card's front shows "In portfolio" when added.
- Gauges update at once; with Motion on, bars ease over 200 ms. Each gauge's line names the reason ("3 views: add a view the wheel shows empty"; "Cost is backed by one origin only: cards 2 and 7 both repeat card 6").
- Echo check appears when two or more portfolio cards share an origin, naming the cards and the origin card.
- Citation web: laid out once from fixed positions (no physics), so it is the same every time; arrows are drawn in SVG; hulls are rounded shapes around shared-origin groups. With Motion off, filters change instantly.
- Background opens a dialog with the painted river (art sp-elwha-river) above the card's text; Escape closes.
- Nothing plays on its own except 200 ms gauge eases; a tap during an ease is taken at once.
- Store: the portfolio saves to localStorage `sp-portfolio` (try/catch); Clear portfolio (after Yes) empties it.
- Keyboard: view control, card grid (arrow keys; Enter flips; A adds), then the panel. The citation web has a text equivalent: a list of each card with "cites" and "cited by" and its origin group.
- Sizes: at 1366x768 and 1280x720 the grid shows 13 cards in 5 columns and the panel holds slots, gauges and wheel. At 680x425 cards show 4 columns with the back as a drawer, and the wheel folds under a **Views** button. At 760 and 375 wide, the portfolio slots become a sticky strip of six numbered pockets at the top, gauges follow the grid, and the web shows as its text list with a **Show web** toggle.

## Look
- Accent `--brand #17693c` (archive green). Own light `:root`, a manila folder desk: `--paper #f3ead6`, `--panel #fffdf7`, `--ink #231d12`, `--muted #5e5442`, `--line #d9cba8`, accent `--brand #17693c` (archive green: gauges, Add, slot edges), `--btn #17693c` with `--head-ink #ffffff`, `--focus #1d4ed8`. Slot pockets `#e9d9b0`. Echo lines in `#9a3412` with the word "Echo" and a two-ring icon.
- View colors (tab and node, always with the view's word): Tribal fisheries `#0f766e`, Lake homeowners `#1d4ed8`, Utility `#a16207`, River scientists `#6d28d9`, History `#57534e`, Town budget `#be185d`, Recreation `#17693c` with a dashed outline to tell it from the brand.
- Kind stamps look rubber-stamped (rotated 2 degrees, single color ink); catalog cards have a punched hole at the bottom.
- Neighbors: boolean-builder orchid on dark; fair-use-review brass on light; fake-or-fact-lab purple; research-quest teal. Group siblings: Research Notebook fountain-pen blue, Portrait in Four Media coral, Source Mixer cyan, Question Sharpener violet, Enduring Questions lantern gold. Green on manila is new among library tools.
- Contrast (WCAG 2.1): white on brand 6.73:1; brand on paper 5.62:1, on panel 6.61:1, on slot manila 4.81:1; ink on paper 13.97:1, on manila 11.96:1; muted on paper 6.22:1, on panel 7.31:1; focus on panel 6.59:1, on paper 5.60:1; echo on panel 7.18:1. View colors on panel: 5.38, 6.59, 4.84, 6.98, 7.5, 5.94, 6.61. All pass AA.

## Art
Local FLUX (`scripts/localart.py`); no people. The tool is mostly diagram and data (catalog cards, stamps, pockets, gauges, views wheel, citation web, all in code), so only the two places it is about are painted, in one style: soft daylit painted landscape.
- sp-millbrook-dam: a small old concrete dam across a river in a wooded valley, a calm lake behind it with a few houses and docks on the far shore, the river running on below the dam, a wide plain sky across the top, soft daylight, painted landscape; 4:1; cutout no; people no; the banner above both views and the backdrop of preview.svg, the question in code across the sky. A lake behind a dam in daylight, so it does not repeat keyword-fishing's misty lake from a dock.
- sp-elwha-river: a wild river running fast and clear through a deep forested canyon, gravel bars and young alder trees along the banks, a broken concrete wall remnant on one bank, painted landscape; 16:9; cutout no; people no; the Background dialog about the real Elwha River (a painting, not a photo of the place, so no caption claims an exact view).
That is 2 images, none with people.

## Voice
Bank voice `firm-captain` (Alnilam), "Say firmly but kindly, like a ship captain giving clear directions": a river pilot keeping the set on course. No neighbor from `neighbors.py` (research family: research-notebook calm-professor, portrait-in-four-media knowing-guide, source-mixer news-reader, question-sharpener big-sister; same subject: boolean-builder curious-librarian, fair-use-review easy-coach, enduring-questions gravel-ranger; credit-card-builder bright-teacher) and no other spec in this batch uses it. `Curio.voice`, scope the view, `welcomeAfter: true`. How lines are spoken the first time, then only update the hint; event lines play every time and are dropped when stale.
- w-shelf (how; Shelf welcome; stale once a card is added): "Tap a card to flip it and see where its facts come from. Then press Add to portfolio to fill your six pockets."
- gauge (how; the first time a gauge is under its goal after 3 cards; stale once that gauge moves): "Check the gauges. Each one tells you what the set still needs."
- echo (event; each new echo found; stale if the portfolio changes first): "Those cards share one origin. They count once."
- wheel (how; the first time 6 cards fill only 3 views or fewer; stale once a view is added): "The wheel shows views you haven't heard from. Tap Remove on a card, then add one from an empty view."
- w-web (how; Citation web welcome; stale once a node or filter is tapped): "Arrows show who cites whom. Shaded groups share one origin. Tap a claim filter or a card to look closer."
- full (event; each time all four gauges reach their goals; stale when the portfolio changes): "All four gauges are full. That's a balanced set."

## Family engine
research (`kit/research.js`), described in full in Question Sharpener's spec. This tool uses: Source (13 cards with origin, authority, context, structure, cites and claim sides), Shelf (card grid and flip), Conflicts and corroboration (`R.web`: origin groups and independent origins per claim), and Store (`sp-portfolio`). The gauges, wheel and citation web drawing are this tool's own.

## Sources
- Elwha River: Elwha Dam completed 1913, Glines Canyon Dam 1927; removal began September 2011 and was complete in 2014; the largest dam removal in US history at the time: U.S. Geological Survey, "Elwha River Restoration," https://www.usgs.gov/centers/pcmsc/science/elwha-river-restoration and USGS news, September 2011; National Park Service, "Elwha River Restoration," https://www.nps.gov/olym/learn/nature/elwha-ecosystem-restoration.htm
- Klamath River dams removed in 2024, now the largest dam removal in US history: Engineering News-Record, 2024 coverage of the Klamath River Renewal Corporation project; Klamath River Renewal Corporation, https://klamathrenewal.org
- Lower Elwha Klallam Tribe's long push for removal: National Park Service, Elwha pages above.
- Kinds of sources, origin, authority, structure, context and corroboration: C3 Framework for Social Studies State Standards, D1.5.9-12, D3.1.9-12, D3.2.9-12, https://www.socialstudies.org/standards/c3
- AASL National School Library Standards (2018), shared foundation Curate, https://standards.aasl.org/framework/
- Millbrook and all 13 cards are written for Curio Class.
- Checks run 2026-10-29 (Python, all 1,716 six-card portfolios, origins per claim as in Content): 1, 2, 7, 8, 9, 13 gives 5 views, 6 kinds, 4 of 4, 4 valued; 2, 3, 4, 5, 6, 7 gives 2 views, 0 of 4, 0 valued; swapping 13 in for 5 gives 1 of 4 (and 3 views); exactly four portfolios meet every goal. Fixed: Content said "many others" reach full marks; it is four. Note: the Corroboration gauge counts a claim when two independent origins speak to it on either side (card 1 and the lake group disagree on sediment, yet K2 counts); if it counted only agreeing origins, just one portfolio (1, 7, 8, 9, 11, 13, with no lake homeowner voice) could fill every gauge. Left as written; see Open questions.

## Done when
1. The portfolio 1, 2, 7, 8, 9, 13 shows Range 5 (goal 4), Kinds 6 (goal 3), Corroboration 4 of 4, Expert standing 4 (goal 2), and the full line plays.
2. The portfolio 2, 3, 4, 5, 6, 7 shows Range 2, Corroboration 0 of 4 (K1 none; K2 one origin; K3 only origin 7; K4 only origin 6), and an Echo check naming cards 2 to 7 and their origins.
3. Swapping card 13 into that portfolio for card 5 makes K4 corroborated (origins 6 and 13): Corroboration 1 of 4.
4. Card 11 never counts toward Expert standing; its back shows Preprint and Correction notice; card 6 shows "Paid for by Sable Valley Power".
5. The citation web draws the arrows in Content (2 to 6, 3 to 2, 4 to 2, 5 to 3, 7 to 6, 1 to 9, 12 to 1) and hulls for the Friends of Millbrook Lake group and the Hartwell group; the claim filter Cost lights cards 2, 3, 4, 5, 6, 7, 13.
6. The views wheel fills one slice per view and leaves the rest visibly empty with their names.
7. Focus: in Shelf the card grid is the largest, central block with the slots and gauges visible beside it; in Citation web the web fills the stage; checked at 1280x720, 1366x768 and 1920x1080.
8. Tap while it plays: an Add or Remove during a gauge ease is taken at once and the gauges show the new values.
9. The dam banner and the Elwha painting load, show no person and no fake lettering; the question text is code over the banner's sky.
10. Reload keeps the portfolio; Clear portfolio (after Yes) empties it; no network requests; console clean.
11. At every size in STANDARDS.md the six slots and the gauges are visible without scrolling the page; 375 wide works in `drive.py --host`.
12. Voice: welcome once per view, how lines once, "Those cards share one origin" every time a new echo appears; no line names a disabled control; only "Curio Class" appears.

## Open questions
- [source-portfolio] The tribal view comes from a made-up tribal government (Upriver Nation Fisheries Department) beside a real background card about the Lower Elwha Klallam Tribe. OK, or should a Native educator review the card first, or the view be framed only through the real Elwha example?
- [source-portfolio] D1.5, D3.1 and D3.2 are 9-12 social studies standards on a library tool. Keep the four-code standards line as the module has it?
- [source-portfolio] The Corroboration gauge counts a claim as corroborated when two independent origins speak to it, even when they disagree (card 1 says the sediment is manageable, the lake group says it would harm the river). Strictly, corroboration means agreeing. Keep the gauge as is (and its reason line says "checked by two independent origins"), rename it "Cross-checked claims" (the One idea says "real corroboration"), or count only agreeing origins, which leaves one full-marks set with no lake homeowner voice?
