# Market Day

## One idea
The child arrives at a Saturday market with five tokens and a bike with a flat tire, and at each stall decides whether it sells a good (you take it home) or a service (someone does it for you), hears the owner tell what they had to learn and where the thing came from, and buys or walks on, while a "gave up" shelf fills with what the tokens can no longer reach, so first graders feel that every choice has a benefit and a cost.

## Not like
- corner-store (2): making change at your own stand. Here choosing as a shopper, with no change to count.
- piggy-bank-planner (2, concept): saving over weeks. Here spending one day's tokens.
- teddy-bear-makers (1, concept, this batch): how one product is made and what it costs to make. Here what a shopper gives up, and who made or did each thing.
- community-helpers-village (1, concept, this batch): who keeps a town running. Here who sells what, and from how far.
- backpack-pack (K, spec): limited pockets force a choice of things. Here limited tokens across goods and services.

## Who and how
- Grade 1, Social Studies (Economics), module "Goods and Services". Standards: D2.Eco.2.K-2 (benefits and costs of personal decisions), D2.Eco.3.K-2 (skills and knowledge needed to produce goods and services), D2.Eco.4.K-2 (goods and services produced in the local community and in other communities).
- Driver: teacher on the projector with the class choosing each buy, or one child alone; every stall, choice and owner line is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Seven stalls, five tokens; a new market day starts with `New day`. tool.json `modes: ["Market", "My basket"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.
- Nothing is saved; `Print` prints My basket.
- Change from the idea card: no market family engine (it is built for supply and demand at grades 6-12); format stays a simple shop.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.2.K-2 (benefit) | Buy something and hear what it does for you (bread for lunch, a fixed tire to ride home) | the item in the basket with its benefit picture | 4 |
| D2.Eco.2.K-2 (cost) | Watch stalls you can no longer afford move to the "gave up" shelf | the gave-up shelf | 4 |
| D2.Eco.3.K-2 | Tap the owner to hear the skill and knowledge it took | the owner's skill picture | 3 |
| D2.Eco.4.K-2 | Hear where each thing came from: made here in town or far away, with a small map | the "from here" and "from far away" stamps | 5 |
| D2.Eco.3.K-2 (goods and services) | Sort each stall as a good or a service before buying | the bag and helping-hands mats | 2 |

## Screens and modes
Header (kit): title "Market Day"; `Market`, `My basket`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A sunny town square with seven striped stalls in a curve. The child's character (pick one of six looks first, a big picture choice) stands at the entrance with a pouch of five round tokens and a bike with a flat front tire. The welcome is queued (`welcomeAfter: true`): "It's market day! You have five tokens, and your bike has a flat tire. Tap a stall to walk over." First hint: "Tap a stall to walk over." The first tap walks the child to that stall and cuts the welcome.

**Market (focus: the open stall).** At 1366x768 the stall fills the center with its owner, the token pouch top right, the gave-up shelf along the bottom and the town square map small in the corner. At 680x425 the map folds away.
- At a stall, two big mats: "Good: you take it home" (a bag) and "Service: someone does it for you" (two helping hands). The owner says what they sell; the child taps a mat. Right: "Yes! Bread is a good. You take it home." Wrong: "Hmm. Can you put a haircut in a bag? Try the other one."
- Then the owner offers: `Buy` (shows the price as token pictures) or `Walk on`. Tapping the owner's face any time plays their skill line and their where-from line.
- Buy: tokens fly to the owner, the item (or a picture of the service done: a new haircut, a painted cheek, a fixed tire) goes to the basket, and its benefit plays. If any stall now costs more than the tokens left, it slides to the gave-up shelf with a soft sound and the line "You can't get the [thing] now. That's what you gave up."
- With zero tokens or nothing left affordable: "Your tokens are spent. Tap My basket."

**My basket (focus: two columns).** Left: "What I got" with benefit pictures. Right: "What I gave up" from the shelf. Below each item, a stamp: "From here" (the town) or "From far away" (a truck and a ship). The owner of the far-away thing explains it again on tap. At the end the bike: if the tire was fixed, the child rides home; if not, they walk the bike home ("That's okay. Next market day you might choose differently."). `New day` starts again with five tokens.

**Class mode.** Teacher notes: before each Buy, the class votes with thumbs.

## Content
Seven stalls (price in tokens, kind, skill line, where-from line, benefit line):
1. Bread, Mrs. Park's bakery cart (1, good). Skill: "I learned to mix and knead dough, and how long to bake it." From: "I bake it right here in town, early every morning." Benefit: "Bread for lunch!"
2. Apples, Mr. Silva's fruit stand (1, good). Skill: "I know how to pick apples that are ripe." From: "These grew at an orchard just outside town." Benefit: "A crunchy snack."
3. Bananas, Mr. Silva's fruit stand (1, good). Skill: "I know how to keep bananas from bruising." From: "Bananas need warm weather all year, so they grow far away, in places like Guatemala and Ecuador. They came by ship and truck." Benefit: "A sweet snack."
4. Honey, June's bee stand (2, good). Skill: "I learned how to care for bees and take honey without hurting them." From: "My bees made it from flowers in our town." Benefit: "Honey on your bread."
5. Haircut, Dre's barber chair (2, service). Skill: "I went to barber school and got a license to cut hair." From: "I do it right here, with my scissors and clippers." Benefit: "A fresh haircut."
6. Bike fix, Mr. Jonas's repair stand (2, service). Skill: "I learned how to patch a tube and pump a tire." From: "I fix it right here." Benefit: "Your tire is fixed. You can ride home!"
7. Face painting, Lia's paint table (1, service). Skill: "I practiced painting faces a lot, and I use paint that's safe for skin." From: "Right here at the market." Benefit: "A butterfly on your cheek!"
- All prices add to 10 tokens, so no child can buy everything with five.
- Teacher note: tokens stand for money; at a real market people pay with dollars and coins.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Buy` and `Walk on` show only after the good-or-service mat is tapped; the hint before then says "Tap the bag or the hands." and never names Buy.
- A stall on the gave-up shelf can be tapped to hear it, but not bought.
- Bananas and apples are one stand with two items; each is its own choice.
- With Motion off tokens and items appear in place without flying.

## Look
- Accent `--brand` #0f6b63 market teal (header, stall roofs' trim, the pouch); gold #f4c542 (tokens, the selected mat); paper #eef8f6; ink #062521; muted #4a5e5b. Scene: a sunny town square with striped stalls.
- Contrast (WCAG 2.1, computed): white on brand 6.36:1; brand on paper 5.87:1; ink on paper 14.98:1; muted on paper 6.37:1; ink on gold 9.98:1.
- Never color alone: mats have icons and words; prices show token pictures and a number.
- Different from this batch (brick orange, map navy, capsule slate, workshop raspberry).

## Art
- Local FLUX (`scripts/localart.py`): the town square with seven stalls (1, 16:9); each stall close-up, empty of people (6, 4:3); items and service results as stickers (bread, apples, bananas, honey jar, a fixed bike wheel, a butterfly face-paint mark, a haircut mirror) (7, 1:1); a small map of the town and of the Americas with a ship route (2).
- People art goes to Gemini (`people: true`): six child looks for the shopper (varied skin tones and hair, one with glasses, one in a hijab), each 3 poses (walking, holding the bag, riding or walking the bike); owners: Mrs. Park (a Korean American woman in her fifties), Mr. Silva (a Brazilian American man in his sixties), June (a white woman in her thirties in a bee veil pushed back), Dre (a Black man in his twenties), Mr. Jonas (a Lithuanian American man in his seventies), Lia (a Filipina American teen), each 3 poses (offering, explaining, thanking); "illustrated market stall owner <name> <pose>, soft gouache, plain white background, friendly face"; 3:4; cutout yes.
About 52 images. Drawn in code: tokens, mats, the gave-up shelf, stamps.

## Voice
Bank voice `upbeat-guide` as the narrator (unique in this batch); owners: Mrs. Park `warm-teacher`, Mr. Silva `knowing-guide`, June `soft-breath`, Dre `hero-coach`, Mr. Jonas `gravel-ranger`, Lia `big-sister` (each unique in this batch). `Curio.voice` with `scope: () => state.stall + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "It's market day! You have five tokens, and your bike has a flat tire. Tap a stall to walk over."
- event `offer`: the owner says what they sell.
- how `sort` (first stall only): "Is it a good you take home, or a service someone does for you? Tap the bag or the hands."
- event `sort-ok`, `sort-no`: the sort lines.
- how `buy` (first stall only): "Tap Buy to spend tokens, or Walk on to keep them."
- event `skill`, `from`: the owner's lines on face tap.
- event `benefit`: the benefit line.
- event `gave-up`: "You can't get the [thing] now. That's what you gave up." (once per thing).
- event, whole, `spent`: "Your tokens are spent. Tap My basket."
- event, whole, `home`: the ride-home or walk-home line.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (see the idea card change in Who and how). Tool-only code: stalls with a good-or-service sort, tokens, the gave-up shelf, the basket with stamps.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Good or service | Always tap the bag | Three of seven are services; the wrong tap asks a picture question and Buy waits for the right mat. |
| Good or service | Left mat is right | Mat order is the same each time on purpose (bag left, hands right) so the child learns them; the stall order is shuffled, so the answer isn't a pattern. |
| Gave up | Buy nothing | Allowed; then nothing goes to the shelf and My basket says "You kept your tokens. You gave up everything at the market." |
| Bike | Ignore the tire | Allowed; the ending shows walking home, honestly, with no scolding. |
There is no score; the lesson is in the basket.

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: look choice (spoken: "Tap the kid who looks most like you."), then `welcome` (queued; may be cut).
2. At a stall: `offer`, then `sort` (first stall). Mat tap: `sort-ok` or `sort-no`.
3. `buy` (first stall). Buy: `benefit`, then `gave-up` for each newly out-of-reach stall, one after another.
4. Tokens out or nothing affordable: `spent` (whole).
5. My basket: `home` (whole) after the columns show.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.2, 3 and 4 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Goods are things you can touch and take; services are work someone does for you | Federal Reserve Bank of St. Louis, Econ Lowdown, "Goods and Services" (K-2) | Council for Economic Education, Voluntary National Content Standards, Standard 1 | yes |
| Bananas grow in warm tropical places; the U.S. imports nearly all its bananas, mostly from Guatemala, Ecuador and other Latin American countries | USDA Economic Research Service, fruit import data | FAO, Banana Market Review | yes |
| Honey bees make honey from flower nectar | USDA Agricultural Research Service, honey bees | National Honey Board, how honey is made | yes |
| Barbers complete a barber program and need a state license | U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, Barbers | National Association of Barber Boards of America | yes |
| Bakers learn their skills mostly through on-the-job training | BLS, Occupational Outlook Handbook, Bakers | Retail Bakers of America, training | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-09): prices sum to 10; with 5 tokens there are 76 different baskets (including buying nothing) and none holds everything; the bike fix (2) fits in every budget at the start; the gave-up shelf rule moves exactly the stalls whose price is above the tokens left, and stalls already bought never go to the shelf; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the stall, pouch and shelf fit; at 680x425 the map folds.
2. Every stall sorts to good or service before Buy shows. (D2.Eco.3.K-2)
3. Owners tell their skill and where it came from on tap. (D2.Eco.3.K-2, D2.Eco.4.K-2)
4. Buying shows the benefit, and out-of-reach stalls move to the gave-up shelf. (D2.Eco.2.K-2)
5. My basket shows got and gave up with from-here and far-away stamps. (D2.Eco.4.K-2)
6. The bike ending matches whether the tire was fixed.
7. Buy is never named before the sort.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no flying tokens; no network requests.

## Open questions
- None for Cory.
