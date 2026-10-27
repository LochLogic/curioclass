# Wave 2 art log

Art for spec wave 2 of Curio Class (9-12 math, CTE and computer science), drawn 2026-10-27 before the builds. Cory approved drawing it now, knowing some of it will be redone once the tools exist.

Every picked image is "placed" with review "pending" in its prompts.json. Nothing has been marked ok. The one people image was drawn with Codex only and waits for Cory's review.

Sources: local FLUX = flux1-schnell on this PC (candidates c1-c8), Cloudflare = flux2-klein-4b (c9-c19), Codex = gpt-image-2 (c20 and up). "Round 2" means a second local try with an "sd" prompt fix. Local FLUX went first for every scene and object, as the brief asked, even where a spec named Cloudflare.

Of the 58 wave 2 tools, 11 have art in prompts.json. The other 47 specs say none or drawn in code. Folders keep their old ids (renames proposed in BATCH-W2-LOG.md are not applied here). Each prompts.json sets its own "house_style" and "style" from the spec's Look, in place of the K-5 storybook style.

## Per tool

### launch-pad
- lp-field-dusk: placed, local FLUX c2. Soccer field with goals, coral sunset glow at the horizon, dark navy sky. c1 had numbers painted in the sky; c3 had yard tick marks. 1600x914, 13 KB.

### work-rate-crew
- wrc-house-dusk: placed, local FLUX c2. Left half fresh sage, right half dark old paint with peeling strips, two ladders, drop cloths, buckets. A city skyline sits behind the fence; the right half reads more brown than faded gray. 1600x914, 33 KB.

### shadow-measure
- sm-schoolyard: placed, local FLUX c1. Pale blue sky over a low red brick school, blank walls, grass strip in front. A power pylon and a lamp post stand at the left, and a tree at the right edge. 1600x914, 40 KB.

### packaging-challenge
- pc-kraft: placed, local FLUX c1. Fine vertical fluting on pale kraft. It is lighter than the spec's accent #c08a2a and gets slightly darker toward the right edge, so a plain tile may show a seam: the builder may want to tint it or mirror-tile it. 512x512, 3 KB.

### rigid-motion-twins
- rmt-sandstone: placed, local FLUX round 2 c3. Round 1 gave flat cream slabs with no ripples. Round 2 c1 and c2 looked like wood grain; c3 has real ripple marks but reads as rippled sand more than stone, and the ripples bunch toward the left and middle (choose the crop with care). Paler and yellower than the spec's average #c9a57a. 1280x731, 94 KB (busy texture).

### image-transformer
- imt-lighthouse: placed, local FLUX c2 (c1 had a tiny person on the rocks). 800x622, 47 KB.
- imt-balloon: placed, Cloudflare c10. Every local candidate in rounds 1 and 2 had people in the basket. Cloudflare drew an empty basket; red, yellow and blue stripes over green hills. 800x622, 24 KB.
- imt-fox: placed, local FLUX c2, facing left as the spec asks. 800x622, 25 KB.
- All three come out 800x622 (FLUX frames are 1152x896, a bit wider than 4:3 tall). The spec places the picture on a 4 by 3 box, so the builder should crop to 800x600 or stretch slightly.

### fire-lookout-triangles
- flt-lookout-dusk: placed, local FLUX c2. Lookout cabin on a rocky summit, blue hazy ridges, an orange band at the horizon, one thin smoke column far away on a ridge. c1 had the smoke coming out of the cabin's own chimney; c3 had a signature. The cabin sits on a short wooden tower base. 1280x731, 15 KB.

### design-the-study
- editor-quill: people-pending, Codex c20. Dr. Mara Quill, silver bun, reading glasses on a beaded chain, navy cardigan, blue pencil over a manuscript of plain gray lines. Green key with despill; checked on dark and on the paper color, clean edge. The teal bit beside her right temple is a bead on the glasses chain. The figure is cut at the bottom edge (chest up, as asked). 360x354, 22 KB.

### courtroom-statistics
- courtroom-empty: placed, local FLUX round 2 c1. All three round 1 candidates had a US flag (c1 also had framed portraits, c2 a seal). Round 2 describes a plain oak-paneled wall instead. The bench is low and there is no clear witness stand; benches, wainscot and tall daylight windows are there. 1280x731, 32 KB.

### fair-dice-investigation
- cafe-after-hours: placed, local FLUX c3. Shelves of game boxes with blank faces, green felt table, scattered dice, one hanging lamp, dark windows. Less noir than asked (soft olive walls); the tool dims it anyway. c1 had marks like lettering on boxes; c2 had books, not games. 1280x731, 23 KB.

### computing-team-stories
- cts-game-studio: placed, local FLUX c2. Two desks, dark blank monitors, sketchbooks with doodled creatures, a controller, two lamps. Daylight-warm more than dusk. 960x549, 13 KB.
- cts-health-office: placed, local FLUX c2. Town map on a corkboard with colored pins, laptop with a dark screen, a white cooler box. The map has a few tiny marks you cannot read; c3 had "Clinic" on the cooler. 960x549, 11 KB.
- cts-river-lab: placed, local FLUX c1. Server rack with lights, a small mountain river valley model, a tied stack of old logbooks. The desk monitor has an all-in-one shape with a plain dot under the screen (no logo); Cory may find it too close to a known brand's look. c2 had a signature. 960x549, 15 KB.
- cts-newsroom: placed, Cloudflare c9. Night, three dark monitors, a map with roads only, a mug, a desk radio. Local round 1 had a fruit logo on a laptop and lettering on the map; round 2 had "NIS" on a map and tiny words on a map under the desk. The radio looks more like a desk phone than a police scanner. 960x549, 16 KB.
- cts-limb-lab: placed, local FLUX round 2 c1. Robotic hand on paper, small white 3D printer, cutters and red wire, a pencil sketch of a hand. Round 1 c2 had lettering on the printer base, and the other two had no printer. The printer has a tiny blue display with nothing readable. 960x549, 14 KB.

## For the builder to fetch

- No wave 2 spec names a public-domain artwork, from The Met, the Art Institute of Chicago, NASA, the Library of Congress, NOAA or anywhere else. Nothing was fetched with pd_art.py.
- catalog-column-rules needs a Seattle Public Library data pull (data, not art), as its spec says.

## Totals

- Tools with drawn art: 11 of 58. All are done.
- Assets: 17, all with a finished webp.
  - Local FLUX: 14 placed, from 63 local images drawn (16 assets x 3 in round 1, plus 5 assets x 3 in round 2).
  - Cloudflare: 2 placed (imt-balloon, cts-newsroom), from 4 Cloudflare images drawn.
  - Codex: 1 placed, people-pending (editor-quill), from 1 Codex image drawn.
- Left "needed": none.
- No allowance was hit, for Codex or for Cloudflare.

## What is left

- Cory reviews all 17 placed assets, starting with editor-quill (the one people image).
- Possible redraws once the tools are built: rigid-motion-twins rmt-sandstone (sand more than stone, uneven ripples, 94 KB), packaging-challenge pc-kraft (pale, may seam when tiled), courtroom-statistics courtroom-empty (no clear witness stand), fair-dice-investigation cafe-after-hours (not very noir), computing-team-stories cts-river-lab (monitor shape).
- The image-transformer pictures need a crop to exact 4:3 at build time.
