# Pen Pal Parcels

## One idea
Three parcels arrive from pen pals in Ghana, Chile and Japan, and each one holds a thing made there that families here buy (shea butter for lotion, a bunch of grapes in our winter, a bike gear) plus a letter from a kid that says why their country makes and sells it, what they buy from us, and one real change happening where they live; the child pins each parcel on the globe, packs a reply with something made here that the pen pal's country buys, and watches lines fill the globe both ways, so a second grader learns that things in their own home connect them to faraway people and that countries trade to get what they can't make as well.

## Not like
- cocoa-chain (5, concept): a grade 5 supply chain from Ghana. Here no cocoa; three countries and trade both ways at grade 2.
- festival-parade (1, spec): festivals that traveled. Here goods that travel.
- day-in-the-life (3, concept, next batch): daily life in other countries compared. Here products and trade.
- piggy-bank-planner (2, spec, this batch): saving in one town. Here buying and selling between countries.
- three-towns (2, spec, this batch): where a breakfast comes from inside one country. Here between countries.

## Who and how
- Grade 2, Social Studies (Geography and Economics), module "Pen Pal Parcels". Standards: D2.Geo.10.K-2 (describe changes in the physical and cultural characteristics of various world regions), D2.Geo.11.K-2 (explain how the consumption of products connects people to distant places), D2.Eco.14.K-2 (describe why people in one country trade goods and services with people in other countries; moved here from piggy-bank-planner), D2.Eco.15.K-2 (describe products that are produced abroad and sold domestically and products that are produced domestically and sold abroad).
- Driver: teacher on the projector reading with the class, or one child alone; every letter, label and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parcels, three replies, a globe. Extra: kitchen hunt. tool.json `modes: ["Parcels", "Globe", "Kitchen hunt"]`, `minutes: "15-25"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Geo.11.K-2 | Open a parcel, see where its thing ends up in a home here, and pin the parcel's country on the globe | the thing in a kitchen or bathroom here; the pin and a line to the child's home | 2, 3 |
| D2.Eco.14.K-2 | Hear why that country makes and sells the thing, and tap the reason card that matches | the reason card: "It grows there", "Its season is our opposite", "Its factories make it well" | 4 |
| D2.Eco.15.K-2 | Pack a reply with something made here that the pen pal's country buys | the reply box and a line back from the U.S. to that country | 5 |
| D2.Geo.10.K-2 | Read the letter's "something changing here" part and sort it: a change to the land (physical) or a change to how people live (cultural) | the change card under a mountain icon or a people icon | 6 |

## Screens and modes
Header (kit): title "Pen Pal Parcels"; `Parcels`, `Globe`, `Kitchen hunt`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A front porch with a mailbox. The mail carrier, Ms. Pat, sets down three parcels with stamps from far away. The welcome is queued (`welcomeAfter: true`): "Three parcels came from far away, from your pen pals! Tap a parcel to open it." First hint: "Tap a parcel to open it." The first tap opens that parcel and cuts the welcome.

**Parcels (focus: the open parcel).** At 1366x768 the parcel's thing is at the left, the letter is center (with the pen pal's picture at the top), and three buttons sit under the letter: `Where does it go?`, `Why do they sell it?`, `What's changing?`. At 680x425 the thing sits above the letter.
- The letter is read by the pen pal in parts; each part plays when its button is tapped.
- Ghana parcel, from Ama, age 8, Tamale (northern Ghana):
  - Thing: a jar of shea butter. Where does it go: a lotion bottle and a bar of soap in a bathroom here ("Shea butter goes into lotion and soap your family might buy.").
  - Why they sell it: "Shea trees grow wild where I live. Women here gather the nuts and make the butter. Lots of countries buy it." Reason card: "It grows there."
  - What they buy from you: "We buy cars and trucks from your country."
  - What's changing: "Our capital city, Accra, is growing so fast! There are new buildings and roads everywhere." (cultural: how people live)
- Chile parcel, from Tomás, age 7, near Santiago:
  - Thing: a bunch of green grapes. Where does it go: a fruit bowl in a kitchen here, with snow outside the window.
  - Why they sell it: "When it's winter where you live, it's summer here! Our grapes are ripe when yours are not. Chile sends more grapes to other countries than any other country." Reason card: "Its season is our opposite."
  - What they buy from you: "We buy fuel for cars and machines from your country."
  - What's changing: "The glaciers on the mountains near my city are getting smaller every year." (physical: the land)
- Japan parcel, from Kenta, age 8, Sakai (near Osaka):
  - Thing: a bike gear. Where does it go: on a bike in a garage here.
  - Why they sell it: "My city has made bikes for a long, long time. Our factories make bike parts very well, and bike makers all over the world buy them." Reason card: "Its factories make it well."
  - What they buy from you: "We buy corn and soybeans from your country. Farms there grow lots of them."
  - What's changing: "There are fewer kids in Japan than before. My grandpa's old school closed because there weren't enough kids." (cultural)
- After the three buttons, the child taps the reason card (three cards shown) and the change sort (mountain or people). Wrong reason: the "why" part plays again. Wrong sort: "Is that a change to the land, or to how people live?"
- Then `Pack a reply`: six things made in the U.S. (cars and trucks, fuel, corn and soybeans, a movie, airplane parts, apples). The child drags the one the pen pal named into the reply box; a second right one counts as a bonus (all six are real U.S. exports, so any send is allowed, but the named one gets a star: "That's what Ama said they buy!"). The box is sealed and `Send` sends it.

**Globe (focus: the globe).** The globe turns to each country as its parcel is opened. A pin and a line come from the country to the child's home (a house icon in the U.S.); `Send` draws a line back. With three parcels done: six lines, three each way. The narrator: "Things in your home come from far away. And things made here go far away too. Countries trade so everyone can get things they can't make as well." Tapping a pin replays that pen pal's line.

**Kitchen hunt (focus: a checklist).** For home or class: "Look at labels in your kitchen. Find where things were made." Six picture rows (fruit, a can, a spice, a toy, a shirt, a shoe) with a country picker from a list of 20 countries. Nothing is saved after the page closes; `Print` prints the list.

## Content
- Three parcels as listed; three reason cards; six reply things; six change sort pairs (three letters, plus three practice cards in the review: "A new train line opened" cultural, "A river flooded its banks" physical, "Snow came early" physical).
- All three pen pals are made-up children in real places.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Pack a reply` shows only after the reason card and change sort are done. `Send` shows only after something is in the box.
- Keyboard: Tab through letter buttons; Tab to a reply thing, Enter to pick it up, Enter on the box to drop.
- With Motion off the globe jumps to each country and lines appear at once.

## Look
- Accent `--brand` #2b3f8c airmail indigo (header, parcel stamps, the globe's lines); gold #f4c542 (pins, the star, the lit button); paper #f0f2fa; ink #0b1230; muted #4f566b.
- Contrast (WCAG 2.1, computed): white on brand 9.58:1; brand on paper 8.57:1; ink on paper 16.43:1; muted on paper 6.53:1; ink on gold 11.29:1.
- Never color alone: lines carry arrows and labels ("to you", "from you"); the change sort uses icons and words.
- Different from this batch (piggy rose, storm teal, carousel red-brown, three towns olive).

## Art
- People art goes to Gemini with `people: true`: Ama, Tomás and Kenta (3 poses each: waving, holding the thing, pointing at their place; cutout yes; everyday clothes, drawn with respect, checked by a fresh-agent read); Ms. Pat the mail carrier (2 poses).
- Local FLUX (`scripts/localart.py`): the porch and mailbox (16:9); a shea tree with nuts and a jar of shea butter (2); grapes on the vine in a Chilean summer valley (1); a bike factory workbench with gears (1); Accra skyline with new buildings (1); Andes glacier near Santiago (1); a small closed school in Japan (1); the three "where it goes" home scenes (3); six reply things (6, 1:1, cutout yes).
- Drawn in code: the globe (continent outlines, pins, lines), letters, buttons, cards, the reply box, the hunt list.
About 30 images.

## Voice
Four bank voices, each unique in this batch: `upbeat-guide` as the narrator and Ms. Pat; `bright-teacher` as Ama; `easy-coach` as Tomás; `casual-peer` as Kenta. `Curio.voice` with `scope: () => state.mode + ':' + state.parcel + ':' + state.part`, `welcomeAfter: true`.
- how `welcome`: "Three parcels came from far away, from your pen pals! Tap a parcel to open it."
- event, whole, `hello`: each pen pal's greeting ("Hi! I'm Ama. I live in Tamale, in Ghana.").
- how `parts` (once): "Tap Where does it go, Why do they sell it, and What's changing."
- event, whole, each letter part.
- how `reason`: "Why do they sell it? Tap a card."
- how `sort`: "Is that a change to the land, or to how people live? Tap the mountain or the people."
- how `reply`: "Pack a reply. Drag something made here into the box."
- event `star`: "That's what [name] said they buy!"
- event, whole, `globe-done`: "Things in your home come from far away. And things made here go far away too. Countries trade so everyone can get things they can't make as well."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: letters in parts, reason and change sorts, the reply box, and the globe with pins and two-way lines.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reason | Tap any card | Each country's reason is different (grows, season, factories); a wrong tap replays the letter part. |
| Change sort | Guess | Two physical and four cultural across letters and practice, so one answer for all fails. |
| Reply | Send anything | Allowed (all are real exports), but the star comes only for the thing the pen pal named, and the hint asks "What did [name] say they buy?" |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a parcel: `hello` (whole), waits; `parts` (once).
2. Each button: its letter part (whole).
3. `reason`; tap; `sort`; tap.
4. `reply`; drop: `star` or a click; `Send`: the line draws.
5. Three parcels: `globe-done` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Geo.10, D2.Geo.11, D2.Eco.14 and D2.Eco.15 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Shea trees grow wild in the savanna of northern Ghana; women gather the nuts and make shea butter, which is sold abroad for lotions and soaps | Wikipedia, Shea butter (checked 2026-11-09) | Global Shea Alliance, "Shea industry" | yes |
| Chile is the world's largest exporter of table grapes, shipping mostly to North America and Europe during the northern winter | Wikipedia, Table grape (checked 2026-11-09) | USDA Foreign Agricultural Service, "Fresh apples, grapes, and pears: world markets and trade" | yes |
| Sakai, near Osaka, has a long bicycle-making history, and Japan is a major maker of bicycle parts | Sakai City, "Sakai Bicycle Museum" | Wikipedia, Sakai (checked 2026-11-09) | yes |
| U.S. exports to Ghana include vehicles; to Chile, refined fuel; to Japan, corn and soybeans | Observatory of Economic Complexity (OEC), U.S. exports by country | U.S. Census Bureau, Foreign Trade, exports by country | yes |
| Accra, Ghana's capital, is growing quickly | Ghana Statistical Service, 2021 Population and Housing Census | Wikipedia, Accra (checked 2026-11-09) | yes |
| Glaciers in Chile's central Andes are shrinking | NASA Earth Observatory, Andes glacier retreat | Wikipedia, Retreat of glaciers since 1850 (South America) | yes |
| Japan has fewer children than before, and many schools have closed | Wikipedia, Aging of Japan (checked 2026-11-09) | Japan Ministry of Education (MEXT), school closures data | yes |
| Countries trade because places differ in what they can grow or make well | Federal Reserve Bank of St. Louis, Econ Lowdown "Trade" (primary) | Council for Economic Education, "Why we trade" | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: three real countries with made-up child pen pals. Each place is shown through ordinary work and a real change, not poverty or crisis; Ghana is not shown through cocoa (cocoa-chain owns that). A fresh-agent read of the letters and art is needed before build.

Checks run (Python, scratchpad r4, 2026-11-09): each parcel has one reason, one named U.S. export, and one change; changes sort 1 physical, 2 cultural in letters, 2 physical, 1 cultural in practice; the three reason cards are all different; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 thing, letter and buttons fit; at 680x425 the thing sits above the letter.
2. Each parcel shows where its thing goes in a home here. (D2.Geo.11.K-2)
3. Each parcel pins its country with a line to the child's home. (D2.Geo.11.K-2)
4. Each parcel takes only its reason card. (D2.Eco.14.K-2)
5. Each reply sends a U.S. thing back with a line, starring the named one. (D2.Eco.15.K-2)
6. Each change sorts as land or people. (D2.Geo.10.K-2)
7. `Pack a reply` and `Send` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no globe spin; no network requests; Kitchen hunt keeps nothing after closing.

## Open questions
- None for Cory.
