# Boolean Builder

## One idea
Type a real database query and a live Venn diagram shades exactly the region it asks for, with every one of the 36 records drawn as a dot in its region, so you watch AND shrink the set, OR grow it, NOT carve a bite out of it, quotes pin a phrase, a star catch "treeline" by surprise, and a missing pair of parentheses quietly change what the database thinks you meant.

## Not like
- keyword-fishing (3-5, this group): every word must be on the page and the skill is which words to choose. Here operators, grouping, phrases and truncation are the subject, and the picture is set logic, not fish.
- fake-or-fact-lab (6-8, this group): judges whether a page can be trusted. Here every record is a sound study; the question is only whether your query finds the right ones.
- fair-use-court (9-12, this group): using sources legally. Nothing about permission here.
- api-playground (9-12 CS, wave 1): sends requests to made-up APIs and reads JSON. Here the query language is a library database's, and the response is a set you can see.
- decision-tree (6-8 CS, built) and flowchart-factory (6-8 CS, wave 1): logic as branching steps. Here logic is set membership, drawn as overlapping circles.
- Question Sharpener (ela 12, research family, not built): narrows a research question. Here the question is fixed and you narrow the search.

## Who and how
- Grades 9 to 12, library. Module: Databases and Advanced Search (Research), "Academic databases, Boolean search and primary sources".
- Topic line: "Boolean search with AND, OR, NOT and quotes".
- Driver: students on their own laptops; a teacher can project the Sandbox for a five-minute demo. 15 to 30 minutes.
- Standards: AASL.Curate (IV.A.2 identifying possible sources of information; IV.B.1 seeking a variety of sources). Math link: HSS-CP.A.1 (unions, intersections and complements of sets). CCSS ELA: W.9-10.8, W.11-12.8 (gather information from multiple sources, using advanced searches effectively).
- tool.json: driver "students", minutes "15-30", modes ["Sandbox", "Briefs"], grades_label "Grades 9-12". Kit starter plus `kit:theme-912`.

## Screens and modes
Kit frame on `kit:theme-912`. Header: title "Boolean Builder", small line "Lantern Index: urban heat collection"; mode buttons **Sandbox** (opens first) and **Briefs**; Motion, Sound, Read.

Top of the stage, full width: the **query bar**: a text field in the readout font, a row of insert buttons **AND**, **OR**, **NOT**, **( )**, **" "**, **\*** (each inserts at the caret), and **Clear**. Results update live as you type (300 ms after the last key) whenever the query parses; Enter does the same at once.
Under it, the **Query tree**: the parsed query drawn as a small tree (operator nodes, term leaves), each node labelled with its own count ("tree*: 11", "AND: 7"). This is where grouping becomes visible.
Focus (both modes): the Venn, the biggest block, in the center of the stage under the query bar; the query bar and tree above it stay compact (about a quarter of the stage height together), so every keystroke's effect lands in the middle of the screen.
Stage, main area: the **Venn**: up to three circles labelled with their terms in the set colors, inside a frame for the whole collection ("All 36 records"). Each region the query asks for is filled with the accent at 35% plus diagonal hatching. Every record is a dot placed in its region (records matching no circle sit in the frame outside the circles); dots in the result are filled, the rest are hollow rings. Hover, focus or tap a dot: its record card (title, year, abstract).
Panel: `#hint`; **Results: [n] of 36**; the result list (title, year, abstract, with every matched word underlined and bold); under the list, **How this database reads queries** (a fold-out with the rules in Content).

### Sandbox (opens first)
Starts with the query `heat` (20 results, one circle). Everything is free. Five **Try this** chips above the result list load a query: `heat AND island`, `"heat island"`, `tree OR trees`, `tree*`, `school* AND tree* OR shade`.

### Briefs (optional)
Four brief tabs, **Brief 1** to **Brief 4**, replace the Try this chips (each tab shows a check once met); the open brief's card shows a research need in one line, the number of key records, and live counts "Key records: [k] of [K] · Extras: [e]". Key records in the list and in the Venn get a small star (★ and the word "key" for screen readers). When every key record is in the results with no extras, the card shows "Brief met" with the query saved under it. Four briefs, any order; **Show a hint** gives one rule from Content per press (never the query).

## Content
Collection: Lantern Index, urban heat collection (all records made up). Search text is the title plus the abstract.

| # | Title | Year | Abstract |
|---|---|---|---|
| 1 | Street trees and summer heat in city neighborhoods | 2019 | Measured how much shade from trees lowered sidewalk temperatures on hot afternoons. |
| 2 | Cooling the urban heat island with green roofs | 2021 | Compared plant covered roofs with dark roofs over two summers. |
| 3 | The heat island effect in small towns | 2018 | Even towns of ten thousand people were warmer than nearby farmland at night. |
| 4 | Schoolyard shade and recess temperatures | 2022 | Tree shade kept playground surfaces cooler than open blacktop. |
| 5 | Heat waves on Pacific islands | 2020 | Ocean warming made island heat waves longer and more frequent. |
| 6 | Island birds and rising heat | 2017 | Seabirds on a small island nested later in hot years. |
| 7 | Pavement color and surface heat | 2019 | Light colored pavement stayed cooler than black asphalt in the sun. |
| 8 | Urban parks as cool spots | 2016 | Large city parks were cooler than surrounding streets on summer nights. |
| 9 | Planting trees in the urban heat island | 2023 | A tree planting program cooled the hottest blocks of one city. |
| 10 | Cooking with solar heat | 2015 | Students built solar ovens that reached cooking temperatures. |
| 11 | Who lives in the hottest city blocks | 2021 | Neighborhoods with fewer trees had higher heat exposure. |
| 12 | Tree roots and sidewalk cracks | 2018 | City trees can lift pavement as their roots grow. |
| 13 | Cool roofs in hot cities | 2020 | White roofs reflected sunlight and lowered indoor heat. |
| 14 | Heat island maps from satellites | 2022 | Satellite images showed the urban heat island across a whole city. |
| 15 | Treeline changes on mountains | 2019 | Warmer summers moved the treeline higher on two mountains. |
| 16 | Water fountains and splash pads on hot days | 2017 | Splash pads drew families to parks during heat waves. |
| 17 | Green schoolyards for cooler recess | 2024 | Schools that replaced blacktop with grass and trees measured cooler playgrounds. |
| 18 | Island cities and sea breezes | 2016 | Sea breezes cooled the edges of an island city but not its center. |
| 19 | Heat and student learning | 2020 | Test scores dropped on very hot school days in buildings without cooling. |
| 20 | Urban forests and air quality | 2018 | City trees removed some pollution from the air. |
| 21 | Night heat in the city | 2021 | The urban heat island was strongest after sunset. |
| 22 | Shade sails over playgrounds | 2023 | Fabric shade lowered slide temperatures at a school. |
| 23 | Cooling centers during heat waves | 2019 | Cities opened cooling centers for people without air conditioning. |
| 24 | Asphalt, concrete and grass compared | 2017 | Grass stayed far cooler than asphalt or concrete in the afternoon. |
| 25 | Heat island effect and energy use | 2022 | Hotter neighborhoods used more electricity for cooling. |
| 26 | Tree cover by neighborhood | 2020 | Some city neighborhoods had three times the tree cover of others. |
| 27 | Cookout safety on hot days | 2016 | Tips for grilling and food safety in summer heat. |
| 28 | Rooftop gardens in the city | 2021 | Gardens on roofs grew vegetables and cooled the buildings below. |
| 29 | Trees, shade and walking to school | 2024 | Students walked more on shaded routes. |
| 30 | Coastal cities and ocean heat | 2019 | Warm ocean water raised air temperatures in seaside cities. |
| 31 | The island of Maren: a travel guide | 2015 | Beaches, boats and summer weather on a made up island. |
| 32 | Measuring the heat island with student sensors | 2023 | Students placed temperature sensors around their town to map the heat island. |
| 33 | Wildfire smoke and city air | 2021 | Smoke from distant fires lowered air quality in cities. |
| 34 | Painting schoolyards with cool coatings | 2022 | A light coating cooled blacktop surfaces by several degrees. |
| 35 | Why cities are warmer than farms | 2017 | Buildings and pavement store heat and release it at night. |
| 36 | Trees and stormwater in cities | 2018 | Street trees soaked up rain and reduced flooding. |

How this database reads queries (the fold-out; the matching rules are this database's own, chosen to make each idea visible, and the fold-out says real databases differ):
- Words match whole words, any capitals. No automatic plurals: `tree` does not find "trees".
- `*` at the end of a word (3 or more letters first) finds every word that starts that way: `tree*` finds tree, trees and treeline.
- `"..."` finds the words side by side in that order. `*` works inside quotes too.
- `AND`, `OR`, `NOT` must be in capitals; a lowercase "and" is searched as a word (the tree marks it with "Did you mean AND?"). Two terms with nothing between them are joined by AND.
- This database does AND and NOT before OR, left to right. Other databases use other orders, so use parentheses to say what you mean.

Checked results (by script from the table; the build must match all):
- `heat` 20; `island` 11; `heat AND island` 9 (2, 3, 5, 6, 9, 14, 21, 25, 32); `"heat island"` 7 (2, 3, 9, 14, 21, 25, 32); `heat AND island NOT "heat island"` 2 (5, 6); `heat NOT island` 11.
- `tree` 4 (4, 9, 12, 26); `trees` 8; `tree OR trees` 10; `tree*` 11 (adds 15 treeline); `tree* NOT treeline` 10.
- `cool` 3; `cooling` 4; `cool*` 14; `coo*` 16 (adds 10 Cooking and 27 Cookout).
- `city` 12; `cities` 7; `cit*` 17; `cit* OR urban` 18.
- `school* AND (tree* OR shade)` 4 (4, 17, 22, 29); `school* AND tree* OR shade` 5 (1, 4, 17, 22, 29), read as `(school* AND tree*) OR shade`; `school* OR shade AND tree*` 7.
- `tree* AND heat` 3 (1, 9, 11); `(tree* OR shade) AND (cool* OR heat) AND (cit* OR urban)` 3 (1, 9, 11).
- `(roof* OR pavement OR asphalt OR blacktop) AND cool*` 8 (2, 4, 7, 13, 17, 24, 28, 34); `"heat wave*"` 3 (5, 16, 23).

Venn rule: if the query has 1 to 3 different terms, each term is a circle. Otherwise, if the top level is 1 to 3 groups joined by AND, OR or NOT and each group is one term or terms joined only by OR, each group is a circle labelled with its terms ("tree* OR shade"). Otherwise the Venn shows "Too many groups to draw. The results and tree still work." A region is filled when a record with exactly that circle membership would satisfy the query. Circles keep their set colors in order: first #5aa9ff, second #fbbf24, third #5fd39a.

Briefs (key records; the rule "every key record, no extras" is the tool's own):
1. "Trees or shade at school, for a proposal to your principal." Key 4, 17, 22, 29. One solution: `school* AND (tree* OR shade)`.
2. "How trees cool city streets." Key 1, 9, 11. Solutions: `tree* AND heat`, or `(tree* OR shade) AND (cool* OR heat) AND (cit* OR urban)`.
3. "The urban heat island, not hot tropical islands." Key 2, 3, 9, 14, 21, 25, 32. Solution: `"heat island"`.
4. "Cooler roofs, pavement and blacktop." Key 2, 4, 7, 13, 17, 24, 28, 34. Solution: `(roof* OR pavement OR asphalt OR blacktop) AND cool*`.
Hints, in order, per brief: 1 "Look at the tree. What did OR join?" then "Parentheses group the OR first." 2 "Which records talk about trees and heat together?" 3 "Island records about the Pacific have both words, but not side by side." 4 "Name the surfaces with OR, in a group, then add what they do."

## Interactions in detail
- Parse errors: the field outlines in `--warn` with a ✗ and a message under it ("A closing parenthesis is missing.", "AND needs a term on both sides.", "Put at least 3 letters before *."); the Venn and list keep the last good query, dimmed, labelled "Last working query".
- The Venn re-lays out when the circle count changes (fade 300 ms; instant with Motion off); dots slide between regions over 400 ms when terms change (instant with Motion off).
- Tapping a circle label puts its term at the caret; tapping a region shows "Records here: [n]" and their titles in a tooltip list.
- Empty query: one empty frame with all 36 hollow dots and "Type a search to start."
- Record cards never link out.
- Nothing plays on its own except short eases (300 to 400 ms); typing is never blocked by a running ease, which jumps to its end when a new query lands.
- Brief progress (which briefs are met, with their queries) saves in localStorage (`bb-briefs`, try/catch); **Clear briefs** (asks Yes / No) empties it. The Sandbox saves nothing.
- Keyboard: the query field first, then insert buttons, then the list, then the dots in record order. Visible focus. The tree and Venn have text equivalents for screen readers ("Region tree* and shade, not school*: 1 record, in results").
- Sizes: the query bar, tree and Venn visible without scrolling at 1280x720 and 1366x768 (the list scrolls in the panel); at 680x425 the tree collapses to one line of nested parentheses with counts; at 375 wide the Venn sits above the list at full width.

## Look
- Accent `--brand #e879f9` (orchid: the shaded regions, Search caret, focus of the query field, the header rule) with `--brand-ink #1c1203` for text on it, on `kit:theme-912` (dark).
- Set colors from the graphing family where they exist: first circle #5aa9ff, second #fbbf24, third #5fd39a; result regions are accent plus hatching, so shading never relies on color alone; filled vs hollow dots carry membership too. Errors use `--warn` with ✗.
- Neighbors: api-playground lemon #ffd75e, sorting-showdown lavender #c39bff, capture-the-flag pink #ff7ac8, data-policy-council navy (light theme); orchid sits between the pinks and lavenders and is new among 9-12 tools. Group siblings: keyword-fishing olive, credit-card-builder crimson, fake-or-fact-lab violet, research-quest teal and fair-use-review brass (light themes), enduring-questions lantern gold (dark), source-portfolio archive green (light): orchid stays apart from enduring-questions' gold on dark.
- Contrast: brand on paper (#0d1219) 7.64:1; brand on panel 7.03:1; brand on section bg 6.67:1; brand-ink on brand 7.50:1; ink on paper 15.96:1; muted on panel 8.13:1; set colors on the Venn bg (#0e1520): blue 7.46:1, amber 10.97:1, green 9.83:1; focus on panel 12.03:1; warn on section bg 9.90:1. All pass AA.

## Art
none: drawn in code. The whole tool is a diagram and its data: query bar, query tree, Venn circles, record dots, result list and preview.svg. Nothing on screen is a scene, place, creature or object a picture would show better; the records are text abstracts, never photos.

## Voice
Bank voice `curious-librarian` (Aoede), "Say curiously and warmly, like a friendly school librarian": a reference librarian at the database desk. No neighbor from `neighbors.py` (fair-use-review easy-coach, enduring-questions gravel-ranger, source-portfolio firm-captain) and no other spec in this batch uses it. `Curio.voice`, `scope: () => state.mode`. Narration is light: records and queries are on screen only. How lines are spoken the first time, then only update the hint; event lines play every time and are dropped when stale.
- w-sandbox (how; Sandbox welcome; stale once the query changes): "Type a search in the bar, or tap a Try this chip. The circles show which records it finds. Try AND, OR and NOT, and watch the shading."
- tree (how; the first query with two operators; stale on the next query change): "The tree under the bar shows how the database grouped your search. Type parentheses to change the grouping."
- star (how; the first star typed; stale on the next query change): "A star finds every word that starts that way. Tap a dot to check what else it caught."
- w-briefs (how; Briefs welcome; stale once the query changes): "Tap a brief tab, then type a search. Find every key record with no extras. Stars mark the key records."
- met (event; each time a brief is met; stale on brief change or query change): "Brief met. Every key record, nothing extra."

## Family engine
none

## Sources
- AASL, National School Library Standards (2018), Standards Framework for Learners: Curate IV.A.2 and IV.B.1. https://standards.aasl.org/framework/
- MIT Libraries, "Database Search Tips" guide: Boolean operators and search order (https://libguides.mit.edu/c.php?g=175963&p=1158594), plus its Phrases and Truncation pages. https://libguides.mit.edu/database-search
- Common Core State Standards, HSS-CP.A.1 (subsets of a sample space using unions, intersections and complements). https://www.thecorestandards.org/Math/Content/HSS/CP/
- All records and the Lantern Index are made up for Curio Class. The no-plurals rule, the 3-letter truncation minimum, the AND-before-OR order and the brief rule are the tool's own choices, said in the fold-out.
- Checks run 2026-10-29 (Python: whole-word match on title plus abstract, star as prefix, quotes as adjacent words, AND and NOT left to right before OR, juxtaposition as AND): all 26 checked results in Content match, count and record numbers (for example `heat AND island` 9, `"heat island"` 7, `tree*` 11, `coo*` 16, `school* AND tree* OR shade` 5 as 1, 4, 17, 22, 29, `school* OR shade AND tree*` 7); the five Try this chips give 9, 7, 10, 11 and 5; every brief solution returns exactly its key records; `heat AND island` misses brief 3 by 2 extras (5 and 6). Nothing needed fixing.

## Done when
1. Every checked result in Content matches the live count and record list exactly (`__tool.search(q)`).
2. `school* AND tree* OR shade` shows a tree grouping `(school* AND tree*) OR shade` and 5 results; adding parentheses around `tree* OR shade` gives 4 and the tree and Venn change to match.
3. The Venn follows the Venn rule: one to three circles for terms or OR groups; "Too many groups to draw" otherwise; every region's fill matches a hand check of the query on that membership; all 36 dots appear once.
4. Parse errors show their messages and keep the last good query dimmed; lowercase "and" gets the "Did you mean AND?" mark.
5. Each brief's listed solution meets it; `heat AND island` does not meet brief 3 (2 extras); the four brief tabs show their checks; progress survives a reload and Clear briefs (after Yes) empties it.
6. Focus: the Venn is the largest block, centered under the query bar, at 1280x720, 1366x768 and 1920x1080.
7. Tap while it plays: typing or tapping an insert button during a dot slide or circle fade takes effect at once, and the Venn jumps to the new query.
8. Query bar, tree and Venn visible without scrolling at every size in STANDARDS.md; 375 wide works in `drive.py --host`; dots reachable by keyboard with text equivalents.
9. Voice: welcome once per mode, how lines once, "Brief met" every time and dropped on brief change; no line names a disabled control; Read speaks the hint; console clean; no network requests; only "Curio Class".
