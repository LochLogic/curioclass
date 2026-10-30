# Review fix: painted pets (2026-10-29)

## Cory's note

"the dogs and cats look weird, its mostly the face. otherwise its a good tool."

## What changed

- All 26 pets are now the painted FLUX portraits in `art/pet-<name>.webp` (360 px tall, cut out, side view). The code
  drawing of the pets (`drawHead`, the parametric body, legs, tail) is gone, along with two color helpers only it used.
- `src.html`, `ART` table: one row per pet with its `art:pet-<name>` picture, width/height ratio, head centre and head
  radius (read off each painting by eye), and a flip flag. Four paintings came back facing left (Marmalade, Inky,
  Pepper, Luna); they are mirrored with `scale(-1 1)` so every pet faces Kip and the way it walks. No pet walks left.
- `petGeom` now describes the painting, so the look-alike line still starts on the head, the Cat/Dog badge still sits
  above the pet (or beside or over the body when there is no room), and the fly to the shelf still works.
- Size trait: picture height is 150 + 100 x size stage units (Pebble and Marmalade about 170, Moose and Bear about
  240), so big pets stand taller. Width follows each painting's own ratio, so nothing is stretched.
- Walking: the leg steps became a gentle 2.5 degree rock on the feet, on top of the existing bob. Both are off when
  Motion is off (`Curio.reduce`: callers pass step 0 and bob 0). Opacity (`o.opacity`, the leaving fade and the fly)
  is unchanged.
- Shelf cards: a head-and-shoulders crop of the same painting, centred just under the head, ear tips in. Bigger pets
  fill a little more of the card (the old size scaling). The fly to the shelf now lands the head exactly where the
  card shows it.
- Accessibility: unchanged. Cards keep their `aria-label` ("Marmalade, on the Cat shelf"), the stage keeps its group
  label, and each pet's group is `aria-hidden` (the SVG equivalent of empty alt, since the card or the spoken line
  already names the pet).
- Pet data rows (ears, snout, whiskers, size, dark, fluffy, plus coat and pattern) are untouched. Kip's guesses are
  identical (checked: Maple still matches Marmalade; Pippin is "cat" with 11 cards, "dog" with 12; Luna is "dog" with
  2 cards; full deck parade 10 of 10).
- `tool.json` sources: the "drawn in code" line now says Kip, the lobby and the chart; added "Illustrations drawn with
  FLUX.1-schnell (Apache 2.0) on a local computer, edited for Curio Class". Same fix in the src.html header comment
  and notes.md ("Everything is drawn in code" was no longer true).
- `preview.svg` regenerated with `scripts/preview.py` (a mystery-pet moment: Maple, Kip thinking, 6 cards on the wall).

## Sizes

- Paintings: 26 files, 12 to 23 KB each, about 440 KB in all.
- Bundle `teach-the-robot.html`: 1207 KB (was 640 KB), under the 2 MB limit.
- `preview.svg`: 22 KB.

## Checks

- `python scripts/check_tools.py`: teach-the-robot ok.
- Test hook (`window.__tool`): `drawPet`, `drawPortrait` and `previewSVG` still exported and working; every one of the
  26 pets resolves to an inlined WebP; step adds the rock, opacity carries through, Luna's portrait is mirrored.
- Browser (scripts/drive.py, ports 9311/9312, host 8831), no console errors (one favicon 404 from the narrow host page
  only).

## Screenshots

`S:/CurioClass-codex-scratch/review/teach-pets/`:
- `shelf-wide-1280.png` all 16 cards, `shelf-names-1024.png` cards with names
- `parade-luna-wide.png` (Luna, the miss with 2 cards), `parade-shadow-wide.png` (dark dog, truth badge on its body)
- `pippin-11-cards-cat.png`, `pippin-12-cards-dog.png`, `luna-mystery-wide.png`, `moose-1024.png`, `fly-to-shelf.png`
- `narrow-380-shelf.png`, `narrow-380-parade.png`
- `preview.png` (the new card art); every frame is in `drive/`

Dark pets (Inky, Luna, Moose, Shadow, Pepper) read clearly against the cream wall, the wood floor and the cream
cards, so no halo was added.

## Unsure / for Cory

- The paintings no longer change with the clue numbers the way the code drawing did (it drew ear angle, snout length
  and whisker length straight from the data). They were prompted to match each pet's clues, but a few are loose:
  Pebble and Noodle read as fluffy white dogs with floppy ears (fine); Bear's ears are half-floppy; Coco is a short
  coat. Worth a glance that each painting still shows the clue the lesson points at (Pippin's pointy ears and
  Waffles' short nose do).
- Head centres were set by eye. The line and crops looked right in every frame checked; Noodle has the oddest pose
  (face toward the viewer).
- At 380 px wide the pets are small (the layout's minimum scale); faces are still readable but small. That is the
  existing layout, not the art.
- Mid-fly, the shrinking full-body pet briefly overlaps its neighbour card before the card appears (as before with
  the drawn pets).
- `art/prompts.json` still marks every pet `"review": "pending"`; left for the reviewer.

## Round 2 (after the Final look, final-art.md)

Art (done before this round, not redrawn here): Shadow, Noodle and Pebble are new paintings with natural faces,
side view facing right; Bear, Biscuit, Bramble, Pepper, Pippin, Noodle and Pebble had the leg-gap tint cleaned.

- **ART rows re-fitted:** Shadow 433/360 (head .82, .18, r .15), Noodle 311/360 (.72, .23, .20), Pebble 328/360
  (.78, .24, .20); none flipped. Re-checked every head on a zoomed sheet of all 26 and nudged ten head centres a
  little toward the face (Coco, Smoky, Rocket, Duchess, Ghost, Nutmeg, Pippin, Juniper, Tiger, Bramble, Ziggy) or up
  (Biscuit, Moose), so the line start never lands on an ear or an eye.
- **Look-alike line:** it now starts on the forehead (`petFace`: half a head radius above the head centre, below the
  ears) and the line runs *under* the pet, so a line coming from a card never crosses an ear. The start dot scales with
  the pet (7 px wide screens, 3.5 px at 380 px), so it no longer covers Luna's ear on a phone.
- **Card crops:** `portraitFrame` keeps the head-and-shoulders crop but moves it up when needed so its top edge sits
  just above the top of the painting: every ear tip stays in. Checked all 26 offline and on the wall at 1920, 1280,
  680 and 380; Rocket, Inky, Ziggy and Duchess are whole. The fly to the shelf uses the same frame.
- **Truth badge:** when it cannot go above the pet it now goes beside the pet, left gap first, then the gap between
  the pet and Kip, shrinking to fit (down to 34 px); only if neither fits does a small 34 px badge go over the pet's
  back end. At 680x425 Shadow and Waffles are fully visible (badge to their right); at 380 px it sits left of Shadow.
- **prompts.json:** `"review": "ok"` on all 26 pets.
- Bundle 1207 KB; `check_tools.py` ok; test hook unchanged and working (Maple still matches Marmalade; Pippin cat with
  11 cards, dog with 12; Luna dog with 2). preview.svg regenerated. No console errors (favicon 404 on the host page
  only).

Frames: `S:/CurioClass-codex-scratch/review/teach-pets/round2/` (zooms: z-shelf-1920.png, z-shelf-680.png,
z-pippin-1920.png, z380-luna.png, z-shadow-1366.png, z-quad-1366.png; full frames parade-shadow-680.png,
waffles-10-680.png, parade-luna-680.png, n380-parade-shadow.png, n380-shelf16.png, shelf16-1920.png and the rest;
offline sheets _dots.png and _check.png for all 26).

Still open: nothing blocking. The new Pebble painting has no collar tag (final-art.md polish item 6 is gone with it).
Moose's start dot sits just above the eye on the forehead; fine at every size looked at.
