# Unit Sense
Renamed from: Unit Detective

## One idea
Every claim becomes a chain of numbers with their units, and you snap conversion cards onto it (each card is a
fraction equal to 1); units that appear on top and bottom strike out live, so a claim falls apart in plain sight
when the units left over are not the ones it says (miles is not miles per hour) or the number that comes out is
off by a factor you can name.

## Not like
- The rename: one of twelve "Detective" titles (overlap note). "Unit Sense" keeps the topic word and drops the detective framing; the case board stays.
- size-of-everything (gr 8): powers of ten across real sizes. Here the units are the subject, and each conversion is a card you place.
- model-my-world (gr 9, same group): writes equations for a situation. Here no equations: products of quantities and conversion factors.
- misleading-charts (6-8, CS): charts that mislead by design. Here the numbers and units themselves.
- health-claim-checker (9-12, health): source and evidence checks on health claims. Here only arithmetic with units decides.

## Who and how
- Grade 9, Algebra 1, Units and Quantities. Students drive; pairs work well. 15 to 30 minutes.
- Topic line: "units and dimensional analysis".
- Standards (module): N-Q.A (A.1 use units to understand problems and guide solutions, A.2 define appropriate quantities, A.3 choose a level of accuracy).
- CCSS cluster: N-Q.A in every mode; Report (precision) serves N-Q.A.3.
- tool.json: driver "students", minutes "15-30", modes ["Bench", "Case board"], grades_label "Grade 9".

## Screens and modes
Header: title "Unit Sense", subtitle "Let the units do the checking." Modes `Bench` (opens first), `Case board`.
Kit buttons.
The chain (both modes): a long fraction bar across the stage. Each quantity is a card with a number and units,
units on top or bottom. Conversion cards come from the card rack below the chain; each shows two equal quantities
as a fraction ("1.609344 km / 1 mi") and a `Flip` button turns it upside down. When the same unit sits on top and
bottom anywhere in the chain, both copies get a strike line and drop to the "cancelled" row over 300 ms (instant
with Motion off; adding, flipping or undoing a card during it finishes it at once). Live readout at the right end: the product of all numbers and the units left over ("7.4857 mi / h").
Panel: the target ("Units wanted: mi/h") with a units-match light (word "match" or "no match" plus a glyph),
`Clear chain`, `Undo`. Under 900 px tall the rack becomes a scrolling single row under the chain.

### Bench (explore)
Focus: the chain, center stage and full width, with its strike-outs and the live readout at its right end; the rack
under it, the target and match light in the panel.
Pick a starting quantity from a menu (Content: the quantity list) or type one ("65 mi/h"). Pick a target unit.
Add any cards from the full rack. No goal beyond reaching the target; a squared unit needs its card twice (the
tip says so the first time a ft² meets a yd card).

### Case board
Focus: with no case open, the cork board (art: cork-board) with its eight pinned case cards, each a painted picture
(Art) with the case's title in code on a paper label; once a case is open, the chain, center stage, with the claim
card a short strip above it (the case's painting cropped small at its left) and the rack under it. Steps 2 to 4 sit
in the panel. `Back to board` returns to the board.
Opening a case shows: the claim (a made-up post from a made-up
town account, or a documented real case, labeled), the facts given (their cards go on the chain), the target units,
and a rack limited to the cards the case needs plus two decoys. Steps:
1. Build the chain until the units match the target.
2. Compare (appears when the units match): the chain's result beside the claimed number, with the ratio between them
   ("the claim is 3.47 times the chain").
3. Verdict (its buttons are live once Compare shows): `Holds up` or `Falls apart`, and for Falls apart a reason chip: `Wrong time unit`, `A distance used
   as a speed`, `Linear factor on an area`, `Two unit systems mixed`, `Off by a power of ten`.
4. Report: a stepper chooses how many significant figures to report the result with. The tool marks it "fits the
   data" or "too precise: your least precise fact has 2 significant figures".
A solved case gets a stamp on the board ("Holds up" or "Falls apart", in words). Solved cases saved on this device
(localStorage `curio-unit-sense`, try/catch) with `Clear board`.

## Content
Conversion cards (exact unless marked): 1 mi = 1.609344 km; 1 mi = 5,280 ft; 1 km = 1,000 m; 1 ft = 12 in;
1 in = 2.54 cm; 1 yd = 3 ft; 1 m = 100 cm; 1 h = 60 min; 1 min = 60 s; 1 day = 24 h; 1 day = 86,400 s;
1 year = 365 days (a calendar year, labeled); 1 gal = 3.785411784 L; 1 L = 1,000 mL; 1 kg = 2.2046226 lb (rounded);
1 lbf = 4.4482216 N (rounded); 1 L of water ≈ 0.998 kg at 20 °C (measured, 3 significant figures);
speed of light 299,792.458 km/s (exact); speed of sound 343 m/s in air at 20 °C (3 significant figures).
Bench quantity list: 65 mi/h, 100 m in 9.58 s, 2 L, 1 day, 180 ft², 5 gal, 1 marathon (42.195 km).

Cases (claim; facts; target; chain result; verdict and reason):
1. Marathon post (made up): "Dana finished the city marathon in 3 hours 30 minutes, averaging 26 miles per hour!"
   Facts 26.2 mi, 3.5 h. Target mi/h. 26.2 / 3.5 = 7.49 mi/h; the claim is 3.47 times it. Falls apart: a distance used as a speed. Context
   line: the fastest marathon ever run averaged about 13.0 mi/h (42.195 km in 2:00:35).
2. Sunlight post (made up): "Light from the Sun reaches us in 8 seconds." Facts 149,597,870.7 km (1 au), speed of
   light. Target min. 499.0 s = 8.32 min. Falls apart: wrong time unit.
3. Mars Climate Orbiter (real, NASA, 1999): thruster pushes were recorded in pound-force seconds but read by the
   navigation software as newton seconds. Facts 1 lbf·s. Target N·s. 4.448 N·s. Falls apart: two unit systems
   mixed. The pushes were 4.45 times bigger than the navigators thought; the orbiter came within about 57 km of
   Mars instead of the planned 140 to 150 km and was lost.
4. Faucet post (made up): "A faucet dripping once a second wastes over 2,000 gallons a day." Facts 1 drip/s,
   0.25 mL per drip (USGS assumption). Target gal/day: 5.71 gal/day (and per year: 2,083 gal/year). Falls apart:
   wrong time unit (it is about 2,000 a year).
5. Carpet post (made up): "Our 12 ft by 15 ft classroom needs 60 square yards of carpet." Facts 12 ft, 15 ft.
   Target yd². 180 ft² × (1 yd / 3 ft)² = 20 yd². Falls apart: linear factor on an area.
6. Spin post (made up): "At the equator Earth's spin carries you at over 1,000 miles per hour." Facts equatorial
   circumference 40,075 km, one turn in 23.93 h. Target mi/h. 1,040.6 mi/h ("over 1,000" is 3.9 percent under).
   Holds up.
7. Water post (made up): "A gallon of water weighs about 8.3 pounds." Facts 1 gal, 0.998 kg/L. Target lb.
   8.33 lb (8.3287). Holds up.
8. Thunder post (made up): "Count the seconds between flash and bang, divide by 5, and you have the miles."
   Facts 5 s, 343 m/s. Target mi. 1.07 mi (the rule of thumb is 6.2 percent under). Holds up.

## Interactions in detail
- Units are tracked as a map of base-unit symbols to integer powers (mi: 1, h: −1). A unit cancels when top and
  bottom powers meet; ft² is ft with power 2, so one yd/ft card leaves "ft·... / yd" until a second is added.
- Numbers multiply in exact decimal where possible (cards are stored as fractions of integers, 1.609344 as
  1609344/10^6); the readout shows 5 significant figures with "≈" when rounded.
- A card that cancels nothing still joins the chain; its units pile up visibly ("mi·km/mi·h" style) and the
  match light stays "no match".
- Verdict checking: Holds up when the claim is within 10 percent of the chain result in the target units;
  otherwise Falls apart. (The three true claims are 0.3, 3.9 and 6.2 percent off; the five false ones are 77 percent
  or more off.) A claim worded "over" (case 6) is compared at its number. The right reason chip is the one in Content; a wrong chip answers with a hint ("Look at
  what the 26 measured. Was it a speed?") and lets them choose again. No points.
- Significant figures rule shown on screen: in a product or quotient, report no more significant figures than the
  least precise measured fact; exact definitions (60 s in a min, 2.54 cm in an inch) never limit it. Case 1's
  least precise fact is 3.5 h (2 figures): 7.5 mi/h. Case 2: 8.317 min allowed (constants are exact and 1 au is
  given to 10 figures), but the tip suggests "8.3 minutes is plenty for this claim".
- Undo removes the last card (`Undo` is disabled on an empty chain); `Clear chain` empties it. Opening another case keeps each case's chain this session.
- `window.__tool = {state, setMode, open(caseN), add(card, flipped), result()}`.

## Look
Accent `--brand #ff8f9e` (red pen rose), `--brand-ink #2a0a10`. The painted cork board (about `#6b5236` under the
lamp, dimmed to about `#2a2218` at the edges) behind paper labels `#f3ead8` with dark ink `#1c1203` (14:1; the labels
are opaque, so their text never sits on the painting), chain bar `#18202b`, unit chips `#e8edf3` on `#232d3b`, strike line `#ff8f9e` 3 px with the
chip moving to the cancelled row (position, not color, shows the cancel). Contrast (computed): brand on panel
7.97:1, on --sec-bg 7.56:1, brand-ink on brand 8.42:1.

## Art
Local FLUX (`scripts/localart.py`), all without people. One style: muted painted illustration in paper and cork tones,
soft desk-lamp light.
- cork-board: "A large cork bulletin board in a plain wooden frame, warm desk-lamp light, a few loose push pins in
  the corner, muted painted illustration"; 16:10; cutout no; people no; full-frame stage background of the Case board
  (cards, labels and stamps are placed on it in code).
- case-marathon: "A pair of worn running shoes resting on a painted finish line across a city street, scattered paper
  cups, morning light, muted painted illustration"; 4:3; cutout no; people no; case 1.
- case-sunlight: "The Sun rising over a calm ocean horizon with long golden rays across the water, muted painted
  illustration"; 4:3; cutout no; people no; case 2.
- case-orbiter: "A small gold-foil wrapped spacecraft with one long solar panel wing drifting toward a dusty red
  planet, black space with faint stars, muted painted illustration"; 4:3; cutout no; people no; case 3 (the real
  Mars Climate Orbiter, labeled "artist's painting").
- case-faucet: "A chrome kitchen faucet with a single water drop falling into a white sink, muted painted
  illustration"; 4:3; cutout no; people no; case 4.
- case-carpet: "An empty classroom with bare wooden floorboards and a rolled-up green carpet leaning by the wall,
  muted painted illustration"; 4:3; cutout no; people no; case 5.
- case-earth: "Planet Earth seen from space with the equator facing the viewer, blue oceans and white clouds, muted
  painted illustration"; 4:3; cutout no; people no; case 6.
- case-water: "A clear plastic gallon jug of water standing on an old metal kitchen scale with a plain round dial,
  muted painted illustration"; 4:3; cutout no; people no; case 7 (the dial face is blank; no reading is drawn).
- case-thunder: "A lightning bolt over flat farm fields at dusk with dark storm clouds and a lone barn far away, muted
  painted illustration"; 4:3; cutout no; people no; case 8.
The chain, cards in the rack, unit chips, strike lines, stamps, claim text and preview.svg are drawn in code (they
are the diagram, labels and controls).

## Voice
Bank voice `knowing-guide` (Sadaltager, "Say in a knowledgeable, friendly way, like a museum curator"). Not used by
math 9-12 neighbors, group siblings or the R02 batch. `Curio.voice`, `scope: () => state.mode + ':' + state.caseId`.
Claims, facts and tips are read on screen; Read speaks the hint.
- wBench (how, Bench welcome; stale on the first card added): "Pick a starting quantity and a target unit from the menus, then tap cards in the rack until the units match."
- wBoard (how, Case board welcome with no case open; stale when a case opens): "Tap a case card on the board to open it."
- wCase (how, the first case opened; stale on the first card added): "Tap cards in the rack to build the chain. Press Flip on a card to turn it over."
- flipTip (how, first card that cancels nothing; stale on Undo, Flip or the next card): "That card added units. Press Flip to turn it over, or press Undo."
- square (how, first squared unit meeting a single conversion card; stale when the square cancels): "Square feet need the card twice: once for each foot. Add the same card again."
- match (event, units match the target in a case; stale on any chain change): "The units match. Compare with the claim, then press Holds up or Falls apart."
- wrongReason (event, Falls apart with the wrong reason chip; stale on the next chip or case change): "Not that reason. Read the hint, then pick another reason."
- wrongVerdict (event, a wrong Holds up or Falls apart; stale on the next verdict or case change): "Look at the ratio again, then pick the other verdict."
- holds (event, correct Holds up; stale on case change): "It holds up. The units and the number agree. Now set the figures to report."
- falls (event, correct Falls apart with the right reason; stale on case change): "The claim falls apart. Now set the figures to report."
- solved (event, Report set to a precision that fits; stale on case change): "Case closed. Press Back to board for the next one."

## Family engine
none.

## Sources
- N-Q.A: Common Core State Standards for Mathematics, High School Number and Quantity, Quantities, https://www.thecorestandards.org/Math/Content/HSN/Q/
- Exact definitions (inch 2.54 cm, mile 1.609344 km, pound 0.45359237 kg, gallon 231 cubic inches = 3.785411784 L) and the pound-force (4.4482216152605 N): NIST Handbook 44 (2025), Appendix C, and NIST SP 811 (2008), Appendix B, https://www.nist.gov/pml/special-publication-811
- Speed of light 299,792,458 m/s (exact): NIST CODATA, https://physics.nist.gov/cgi-bin/cuu/Value?c
- Astronomical unit 149,597,870,700 m: IAU 2012 Resolution B2, https://www.iau.org/static/resolutions/IAU2012_English.pdf
- Marathon distance 42.195 km and the men's record 2:00:35 (Chicago, 2023): World Athletics competition rules and records page, https://worldathletics.org/records/by-discipline/road-running/marathon/outdoor/men
- Mars Climate Orbiter: NASA, "Mars Climate Orbiter Mishap Investigation Board Phase I Report" (November 10, 1999); summary at https://science.nasa.gov/mission/mars-climate-orbiter/
- Drip size 1/4 mL and drips per gallon: USGS Water Science School, "Drip Calculator", https://www.usgs.gov/special-topics/water-science-school/science/drip-calculator-how-much-water-does-a-leaking-faucet-waste
- Earth's equatorial radius 6,378.137 km and sidereal rotation 23.9345 h: NASA Earth Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
- Water density 0.998 g/mL at 20 °C: USGS, "Water Density", https://www.usgs.gov/special-topics/water-science-school/science/water-density
- Speed of sound 343 m/s at 20 °C: OpenStax, College Physics 2e, 17.2 "Speed of Sound", https://openstax.org/books/college-physics-2e/pages/17-2-speed-of-sound-frequency-and-wavelength; flash-to-bang 5 seconds per mile: National Weather Service, Lightning Safety, https://www.weather.gov/safety/lightning
- Significant figures in products and quotients: OpenStax, Chemistry 2e, 1.5 "Measurement Uncertainty, Accuracy, and Precision", https://openstax.org/books/chemistry-2e/pages/1-5-measurement-uncertainty-accuracy-and-precision
- Checks run (Python, 2026-10-29): case results 7.4857 mi/h (claim 3.47 times); 499.005 s = 8.3167 min; 4.4482 N·s;
  5.7061 gal/day and 2,082.7 gal/year; 60 ft·yd after one card, 20 yd² after two; 1,040.6 mi/h with the card's
  23.93 h; 8.3287 lb; 1.0657 mi. Fastest marathon 42.195 km in 2:00:35 is 13.05 mi/h. Fixes: case 6 had 1,040.4,
  which uses 23.9345 h, not the 23.93 h on the fact card; case 7 had 8.3304, which uses density 0.9982, not the card's
  0.998. The 5 percent Holds up band failed case 8 (the rule of thumb is 6.2 percent under), so the band is now
  10 percent: true claims are 0.3, 3.9 and 6.2 percent off, false ones 77 percent or more.

## Done when
1. Case 1 chain 26.2 mi / 3.5 h reads ≈ 7.4857 mi/h; Falls apart with "A distance used as a speed" is accepted; Report at 2 figures (7.5) "fits the data", at 5 figures "too precise".
2. Case 2 reaches min only with both the speed-of-light card and the min/s card flipped right: 8.3167 min.
3. Case 5: one yd/ft card gives 60 ft·yd, no match (the post's own mistake: it stopped there); the second card gives 20 yd²; Holds up is refused.
4. Case 4 gives 5.7061 gal/day; switching target to gal/year with the 365 days card gives ≈ 2,082.7.
5. Cases 6, 7, 8 accept Holds up (1,040.6 mi/h; 8.3287 lb; 1.0657 mi); Falls apart is refused with a hint.
6. Case 3 gives 4.4482 N·s, and its label says real, NASA, 1999; every made-up post is labeled made up.
7. A card that cancels nothing shows the extra units; Undo removes it; solved stamps survive a reload; `Clear board` works.
8. Focus: at 1366x768 and 1000x625 the chain is the largest thing on the stage in Bench and in an open case; the board with its eight painted cards fills the stage when no case is open.
9. Tap while it plays: adding, flipping or undoing a card during a strike-out shows the new chain and readout at once.
10. No voice line names a disabled control (Undo on an empty chain, the verdict buttons before the units match).
11. All sizes in STANDARDS.md keep the chain, rack and target visible; keyboard alone solves case 1; console clean, no network.

## Open questions
- Title: take "Unit Sense" (the overlap pass's suggestion, used here), or keep "Unit Detective"?
