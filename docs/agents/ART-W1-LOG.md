# Wave 1 art log

Art for spec wave 1 of Curio Class, drawn 2026-10-27 before the builds. Cory approved drawing it now, knowing some of it will be redone once the tools exist.

Every picked image is "placed" with review "pending" in its prompts.json. Nothing has been marked ok. People images (any asset with "people": true, which includes the talking animal characters) were drawn with Codex only and all wait for Cory's review.

Sources: local FLUX = flux1-schnell on this PC (candidates c1-c8), Cloudflare = flux2-klein-4b (c9-c19), Codex = gpt-image-2 (c20 and up). "Round 2" means a second local try with an "sd" prompt fix.

Of the 75 wave 1 tools, 30 have art in prompts.json. Three more (art-style-match, art-through-time, world-music-map) use only public-domain works and have no prompts.json. The rest have no art or draw everything in code.

## Per tool

### biased-bot
- cafeteria-counter: placed, local FLUX c1.

### model-mechanic
- clearing-day: placed, local FLUX round 2 c1. Round 1 had a camera in frame or timestamp text.
- clearing-night: placed, local FLUX round 2 c2. Round 1 had fake timestamp text.

### internet-journey
- ij-dusk-town: placed, local FLUX c1.
- ij-server-hall: placed, local FLUX c2 (c3 had lettering).

### data-defenders
- dd-night-hallway: placed, local FLUX c2 (the others had fake sign lettering). The walls are warm orange rather than blue moonlight; the tool darkens it 40 percent, which helps.

### me-vs-the-counter
- gym-wall: placed, local FLUX c3.

### secret-keeper
- bunny, fern-fox, ollie-owl, gus-goose, rascal-raccoon, bear-grownup: people-pending, Codex. Bunny was drawn first and used as the style reference for the other five.
- pet-park: placed, local FLUX c3.

### spot-the-ai
- workshop: placed, local FLUX round 2 c1. Round 1 put objects on the bench the spec wants clear.

### input-or-output
- otter-call: people-pending, Codex.

### design-for-a-friend
- friend-lou: people-pending, Codex round 2 (c21). Round 1 on a green key lost part of the olive apron, so the key is now magenta.
- friend-ana: people-pending, Codex. Faint green wisps remain in her loose hair after despill.
- friend-kofi: people-pending, Codex round 2. Round 1 drew a white boy, which made all three friends white. The prompt now asks for a Black teen; the spec gives no appearance, so Cory may want to choose.
- All three have despill on.

### algorithm-audit
- board-rivera, board-bell, board-ortiz, parent-park: people-pending, Codex. Despill on all four (Ortiz had a green fringe in his hair). Rivera keeps a tiny green fleck at the top of her hair.

### code-kitchen
- diner-pass: placed, local FLUX c3 (c1 had a fridge logo, c2 a watermark). One pinned note has ruled lines; the image is used at 25 percent.

### data-policy-council
- All 6 members: people-pending, Codex.

### near-and-far
All 11 placed, local FLUX round 1.
- pine c2 (holes on), oak c3, barn c3, cow c2, post c3.
- mill c1 (holes on): a white tower mill with lattice sails, not on a wooden tower.
- hay c1: a loose golden pile more than a neat round bale.
- fox c2 (holes on, which fixed a pink gap between the legs).
- boat c1 (holes on), balloon c3 (holes on).
- hills c1 (despill on): a hairline warm edge along the top at full zoom.

### gallery-critique
- panel-okafor, panel-lindqvist, panel-santos: people-pending, Codex, despill on. Lindqvist keeps a tiny green fleck at the top of his hair.
- The three artworks are public-domain works (listed below).

### virtual-gallery
- 13 placed, local FLUX: window c1, creek c2, busstop c2, crows c3, tidepool c1, seeds c1, fireescape c3, rainglass c1, blockmap c1, tomatoes c1, teapot round 2 c3, laundromat round 2 c2, nightpool round 2 c1.
- bowl: placed, Codex c20. Local FLUX failed twice: the glossy glaze reflects the key color and the cutout ate half the bowl on green and on magenta. It looks more professional than a student piece.
- Problems: in round 1 FLUX signed most of the "student artworks" with a fake signature or date, and one candidate had a person. creek is 74 KB even at quality 36 (busy texture), over the 50 KB target. blockmap (54 KB) reads more like a paper diorama than a flat collage. tomatoes is 53 KB. fireescape is more a brick wall ledge than a fire escape.

### act-it-out
All 6 placed, local FLUX round 1.
- meadow-bridge c1, wide-river c1, veggie-garden c2, little-stage c1.
- cottage-kitchen c1: black range stove, but a modern fridge at the right.
- country-road c1. The other two had a child figure or a tiny person.

### director-s-chair
All 5 placed, local FLUX.
- greek-theatre: round 2 c3. In round 1 all three candidates had tiny figures in the seats or on the floor.
- noh-stage c2 (c1 had fake lettering).
- commedia-piazza c2 (c1 had a shop sign with text and a signature, c3 a tiny person).
- globe-playhouse c3 (c2 had modern cinema seats).
- box-set-study c3 (c1 and c2 had portraits with faces on the walls; c3 has one tiny framed picture with nothing you can make out).

### dance-pattern-puzzle
- festival-square: placed, local FLUX c1 (c2 and c3 had signatures).

### brand-builder
All 4 placed, local FLUX round 1.
- bb-storefront c1, bb-bag c2.
- bb-van c2 (c1 had a street sign with lettering, c3 a tiny person).
- bb-shirt c3 (c1 and c2 had a neck label).

### workplace-scenarios
All 8 placed, local FLUX.
- wp-car c1, wp-path c1, wp-lunch c1.
- wp-craft c1 (c2 had lettering).
- wp-field c1 (c2 had a signature).
- wp-staff c3 (c1 had a sign with a letter P, c2 lettering on a drawer).
- wp-gym: round 2 c1. Round 1 was sunny, not stormy. One tiny poster you cannot read remains on the wall.
- wp-pickup: round 2 c2. Round 1 had REC CENTER lettering and a car badge.
- FLUX added plain white signboards to most outdoor scenes. They are harmless but look a little odd.

### first-aid-responder
- fa-gym c1, fa-cafeteria c1, fa-shop c2 (c1 had WOOD TOOL lettering), fa-kitchen c1, fa-hallway c2: placed, local FLUX. FLUX kept adding a red cross emblem to walls and cabinets; those candidates were skipped.
- fa-field: placed, Cloudflare c10. Local round 1 gave an indoor court, painted yard numbers and a person; round 2 gave yard numbers and a cross on the cooler; Cloudflare c9 had lettering on the building.

### game-day-fuel
All 17 placed, local FLUX round 1, magenta key. Every cutout was checked against a dark background and is clean.
- strawberries c2, toast c2, eggs c1, bagel-pb c2, turkey c2, pbj c3, pasta c1, ricebowl c2, burrito c1, pizza c3, salmon c2, potato c2, salad c1, broccoli c1, fries c1.
- chicken-sandwich c2 (c1 had a white border frame).
- smoothie c2, despill on. FLUX painted the inside of the glass rim pink, a reflection of the key color. It reads as part of the glass.

### pressure-point
All 3 placed, local FLUX round 1.
- pp-bleachers c3 (dark blank scoreboard).
- pp-basement c2 (c1 had heart posters).
- pp-hallway c2 (a few faint marks on the bulletin papers that you cannot read).

### stress-toolkit
All 4 placed, local FLUX round 1.
- st-beach c2.
- st-forest c2: misty, but not clearly wet after rain.
- st-cabin c3. c2 had a lettered wooden sign and c1 a slumped bundle in the chair. c3 is plainer and dimmer than "snug".
- st-rooftop c1: dusk more than night. c2 had a signature.

### rules-referee
- locker-room: placed, local FLUX c3.

### captain-s-choices
- field-day c1 (c3 had a cooler with a label), field-night c3: placed, local FLUX round 1.
- bus: placed, local FLUX round 2 c1. In round 1, c1 and c3 had a person and c2 had lettering above the windshield. The round 2 interior is empty but more green-gray than yellow.

### keyword-fishing
- kf-lake-dock: placed, local FLUX c2 (open water across the middle).

### credit-card-builder
All 3 placed, local FLUX round 1.
- cc-snowy-owl c2 (c3 had a signature).
- cc-honeybee-sunflower c2 (c1 was a coneflower, not a sunflower).
- cc-moon-lake c2.

### fake-or-fact-lab
- ff-wood-frog: placed, local FLUX c1.
- ff-shark-street: placed, Cloudflare c9.
- ff-flooded-street: placed, Cloudflare c9.
- ff-library-front: placed, Cloudflare c10.
- Local rounds 1 and 2 kept adding shop signs with lettering, car brand badges, a passer-by, LIBRARY lettering or plaques covered in fake text. Cloudflare drew clean terraced streets that match each other. The library door has a few tiny paper notices you cannot read; the photo is 115 KB.

### research-quest
- rq-garden-bed c2 (c1 and c3 had signatures), rq-caterpillar c1: placed, local FLUX round 1.
- rq-garden-bloom c2: placed, local FLUX round 1 (c1 had a caption, c3 a lettered sign). The pink flowers look more like coneflowers than milkweed.
- rq-trail-map: placed, local FLUX round 2 c2. Round 1 gave square boxes or only 3 or 4 clearings. This one has five empty round clearings, a cabin, a small school and a flower garden, but no clear library or nature center, and the dotted trail has a loose end at the left. The builder should check that it fits the stops drawn in code.

## Public-domain works for the builder to fetch

These were not drawn or downloaded. They are left out of prompts.json, so the builder fetches them.

- near-and-far: Hogarth, Satire on False Perspective, The Met 365241.
- gallery-critique: AIC 20684, Met 11122, AIC 111442.
- art-style-match (18 works): Met 452111, 437881, 438376, 459084, 36490, 55433, 459095, 436528; AIC 93923, 120662, 22719, 16568, 153798, 81551, 27992, 122130, 28560, 80607.
- art-through-time (21 works): Met 544450, 246725, 247017, 662967, 39915, 39328, 438754, 449537, 435848, 356497, 312302, 436453, 437854, 291846, 438820, 435878; AIC 10926, 16571, 97439, 8991, 109819.
- world-music-map (8 instruments): Met 501374 saron, 500996 ud, 500750 sitar, 500712 tabla, 500576 koto, 501326 siku, 501474 bagpipe, 500616 erhu.

That is 51 works in all (1 + 3 + 18 + 21 + 8).

## Totals

- Tools with drawn art: 30. All are done.
- Assets: 128, all with a finished webp.
  - Local FLUX: 100 placed.
  - Cloudflare: 4 placed (fa-field, ff-shark-street, ff-flooded-street, ff-library-front), from 8 Cloudflare images drawn.
  - Codex: 24 placed. That is 23 people-pending plus the virtual-gallery bowl, from 26 Codex images drawn (including the Lou and Kofi redraws).
- Left "needed": none.
- No allowance was hit, for Codex or for Cloudflare.

## What is left

- Cory reviews all 128 placed assets, starting with the 23 people images: secret-keeper (6), input-or-output (1), design-for-a-friend (3), algorithm-audit (4), data-policy-council (6) and gallery-critique (3).
- Decisions for Cory: Kofi's appearance (the spec gives none), and whether to keep the small green flecks on Rivera, Lindqvist and Ana.
- Possible redraws once the tools are built: virtual-gallery creek (over the size budget), research-quest rq-trail-map (layout against the stops in code), captain-s-choices bus (not yellow), stress-toolkit st-rooftop (dusk, not night), data-defenders dd-night-hallway (warm, not moonlit).
- The builder fetches the 51 public-domain works above.
