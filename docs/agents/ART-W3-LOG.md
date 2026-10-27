# Wave 3 art log

Art for spec wave 3 of Curio Class (9-12 science), drawn 2026-10-27 before the builds. A first art agent drew most of it and was stopped early; a second pass reviewed every picked image against its spec, redrew the weak ones and filled the three that were missing.

Every picked image is "placed" with review "pending" in its prompts.json. Nothing has been marked ok. No wave 3 asset shows people, so there are no people images to review.

Sources: local FLUX = flux1-schnell on this PC (candidates c1-c8). "Round 2" and "round 3" mean further local tries with an "sd" prompt fix. Every placed image is local FLUX, although the specs name Cloudflare (cfart.py); local went first, as in wave 2. The first agent drew a few Cloudflare candidates (c9, c10) for tree-of-life; none was used.

Of the 32 wave 3 tools, 10 have art in prompts.json. The other 22 specs say none or drawn in code. Each prompts.json sets its own "house_style" and "style" from the spec's Look.

## Per tool

### tree-of-life
- tol-chimp c2, tol-rhesus c2, tol-mouse c2, tol-dog c1, tol-horse c2, tol-hippo c2, tol-kangaroo c2, tol-chicken c3, tol-bullfrog c1, tol-wheat c1: placed, local FLUX round 1. Checked, kept. The kangaroo is slight, more wallaby than red kangaroo; the bullfrog is a bright yellow-green.
- tol-whale: placed, local FLUX round 2 c2. Kept. The whale is small in the frame.
- tol-fly: placed, local FLUX round 2 c3. Kept.
- tol-rattlesnake: placed, local FLUX round 3 c3 (new this pass). Rounds 1 and 2, and Cloudflare c9, gave bands or blotches, not diamonds. c3 has a striped head and a diamond-like chain of dark patches, but the diamonds are not crisp and the rattle is unclear. 16 KB.
- tol-tuna: placed, local FLUX round 3 c1 (new this pass). No candidate in three local rounds or Cloudflare drew the dark belly stripes of a skipjack; c1 is a clean generic tuna. 6 KB.
- tol-yeast: placed, local FLUX round 4 c3 (new this pass). Round 3 drew seed or egg piles (one with a cartoon face). Round 4 asks for a textbook microscope field: c3 shows translucent cells with small buds inside a glowing round field, on black rather than the slate of the others. 15 KB.
- All 512x512, 5 to 16 KB.

### reserve-designer
- rd-prairie-dog c1, rd-wood-frog c2, rd-ovenbird round 2 c1, rd-otter c2: placed, local FLUX. Checked, kept.
- rd-elk: placed, local FLUX round 2 c2 (redrawn this pass). The first pick (c1) had a faint signature in the grass at bottom right; round 2 c1 and c4 had signatures too. 27 KB.
- rd-bear: placed, local FLUX round 2 c4 (redrawn this pass). The first pick (c2) had a signature at bottom right; round 2 c1 had "2022" and c3 a signature. Three-quarter view rather than a strict side view. 32 KB.

### carrying-capacity
- cc-forest-edge: placed, local FLUX c2. Golden grass clearing before a spruce edge; few shrubs or saplings at the margin. Quality cut from 70 to 50 this pass: 149 KB down to 113 KB, still large (busy grass texture).
- cc-tundra-island: placed, local FLUX c2. Kept; 103 KB down to 74 KB at quality 50.

### mole-bakery
- mb-counter: placed, local FLUX round 2 c2. Kept. Reads more as a bakery kitchen than a shop counter, with no flour-dusted marble; it sits under a 70 percent overlay. 1280x731, 36 KB.

### ph-mystery-liquids
- phm-prep-room: placed, local FLUX c1. Kept. Shelves of plain bottles with blank labels, a puddle, daylight window. 1280x731, 26 KB.

### lake-commons
- lake-town: placed, local FLUX c2. Kept. Lake, docks, green floodplain and a few houses; the river mouth is not clear, and the code draws homes on top of houses already in the picture. 1600x914, 113 KB (over budget).

### biome-atlas
- tundra c2, boreal c2, deciduous c2, temperate-rain c2, mediterranean c1, dry-grass c1, desert c3, trop-savanna round 2 c1, trop-seasonal c2, trop-rain c2: placed, local FLUX. All checked, kept. trop-seasonal has many palms. All 720x411; deciduous 82 KB and boreal 62 KB are the heaviest.

### grid-operator
- control-room: placed, local FLUX round 3 c3 (redrawn this pass). Round 1 had lettering on the chart screens; the round 2 pick showed only a few glowing ribbons on a dark wall, not a wall of screens. Round 3 c3 is a curved video wall of line charts, desks and amber light; the charts have tiny tick marks but nothing readable. Shown at 15 percent. 23 KB.
- skyline: placed, local FLUX c1. Kept. 1600x400, 25 KB.

### up-the-watershed
- pasture round 2 c2, fields c1, construction c2, storm-drain round 2 c2, sewer c1, plant c1, geese c3, beach c1: placed, local FLUX. All checked, kept. Mixed look: geese and beach are photographic, the rest painterly. The drainage pipe in fields sticks out of the road bank oddly. 560x436, 11 to 41 KB.

### design-challenge-studio
- classroom c1, stream c1, rain-barrel c3: placed, local FLUX. Checked, kept.
- river: placed, local FLUX round 2 c2 (redrawn this pass). The first pick was a flat calm beige pond with a grass bank (4 KB). Round 2 c2 shows churning brown floodwater with branches and bare willows on the bank; round 2 c3 had a signature. 400x311, 10 KB.

## For the builder to fetch

- No wave 3 spec names a public-domain artwork. Nothing was fetched with pd_art.py.

## Totals

- Tools with drawn art: 10 of 32. All are done.
- Assets: 50, all placed with a finished webp, all local FLUX.
  - 7 drawn this pass: 3 that were missing (tol-rattlesnake, tol-tuna, tol-yeast) and 4 redraws (rd-elk, rd-bear, river, control-room), from 32 new local candidates.
  - 2 re-encoded smaller (cc-forest-edge, cc-tundra-island).
  - 41 kept from the first agent after review.
- People images: none.
- Left "needed": none.

## What is left

- Cory reviews all 50 placed assets.
- Possible redraws once the tools are built: tree-of-life tol-rattlesnake (diamonds not crisp), tol-tuna (no belly stripes, so not clearly a skipjack), tol-yeast (black field, not slate); carrying-capacity cc-forest-edge (113 KB, few shrubs) and lake-commons lake-town (113 KB, river mouth unclear); mole-bakery mb-counter (kitchen more than counter); up-the-watershed (photo and painting styles mixed across the eight cards).
- Cloudflare (cfart.py), as the specs name, could be tried for the tuna and the rattlesnake.
