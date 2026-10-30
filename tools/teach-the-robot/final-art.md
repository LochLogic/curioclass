PASS (round 2 re-check, 2026-10-29: should fix 1 and polish 2, 3, 6, 7 fixed; 4 fixed except a small Pebble leftover; 5 Waffles kept by choice, accepted)

## Round 2 re-check (same agent, 2026-10-29)

Read review-fix.md "Round 2". Bundle rebuilt with `CURIO_DRAFT=1`: 1207 KB, no console errors in 35 shots (favicon
404 on the host page only). Re-shot every frame tied to a finding with the same shot lists; frames in
`S:/CurioClass-codex-scratch/review/teach-final-art/r2/` (frames/, frames-narrow/, art/, work/). Host.html deleted,
nothing listening on 9321, 9322 or 8841. Voice not re-run: no clip or line changed.

1. **Shadow and Noodle: fixed.** Both are new paintings in the set's style: Shadow a natural black Labrador (calm
   brown eye, no blush, no grin; r2/art/c-shadow-face.png), Noodle a white fluffy dog with long floppy ears in side
   view facing Kip (r2/art/c-noodle-dark.png). Both read as dogs at once, on stage and on cards
   (r2/frames/myst5-16-1366.png, myst3-16-1366.png, parade-shadow-1366.png, r2/frames-narrow/n380-shadow-16.png,
   n380-noodle-16.png). Shadow (dark, floppy, long snout, smooth) and Noodle (fluffy, floppy, white) now show their
   clues. The new Pebble is also natural and has no collar.
2. **Line dot on an ear: fixed.** The dot sits on the forehead below the ears and the line runs under the pet: Pippin's
   two pointy ears are both clear (r2/work/z-pippin-1366.png, r2/frames/pippin-11-1920.png), Luna's at 380 px too
   (r2/work/z380-luna.png).
3. **Card crops: fixed.** Rocket, Inky, Ziggy and Duchess keep their ear tips at 1920, 680 and 380
   (r2/work/z-shelf-1920.png, r2/work/z380-shelf.png, r2/frames/shelf16-680.png).
4. **Leg-gap tint: fixed on Bear, Biscuit, Bramble, Pepper, Pippin, Noodle** (0 green or magenta pixels now).
   **Pebble keeps a small leftover:** the gap between its hind legs shows a thin yellow-tan rim
   (r2/art/c-pebble-dark.png; on stage r2/work/z-pebble-legs.png, about 4 x 12 px at 1366x768). Only seen when
   zoomed; polish, known, not done.
5. **Waffles kept:** accepted. A slightly long muzzle for snout .20 is a smaller miss than bat ears against ears .30;
   Kip's guesses do not change.
6. **Pebble's collar tag: gone** with the new painting.
7. **Truth badge at 680: fixed.** It sits beside the pet now; Shadow and Waffles are fully visible
   (r2/frames/parade-shadow-680.png, r2/frames/waffles-10-680.png; at 1366 it sits between Shadow and Kip,
   r2/frames/myst5-16-1366.png).

Lessons still hold: Luna is Dog with 2 cards (line to Bear; r2/frames/luna-2-1366.png, luna-2-680.png), Pippin Cat
with 11 and Dog with 12 (r2/frames/pippin-11-*.png, pippin-12-1366.png), the full deck parade is 10 of 10
(r2/frames/parade-done-1366.png). `art/prompts.json`: all 26 pets "review": "ok".

# Round 1 (FIX: 1 should fix: redraw Shadow and Noodle with natural faces; 6 polish; nothing blocks)

# teach-the-robot: Final look on the painted pets (2026-10-29, fresh cold agent)

Read refine.md, handoff.md, final.md (PASS, round 2) and review-fix.md first. Cory's note: "the dogs and cats look
weird, its mostly the face. otherwise its a good tool." All 26 pets are now painted FLUX portraits.

Tools: `scripts/audit_tool.py` (port 9321, host 8841), then `scripts/drive.py` on 9321 (wide frames) and 9322 (380 px
iframe host on 8841, host.html deleted after). Scratch: `S:/CurioClass-codex-scratch/review/teach-final-art/`
(audit/, frames/, frames-narrow/, art/, work/). Every Chrome and server I started is closed; nothing listens on 9321,
9322 or 8841. Bundle rebuilt with `CURIO_DRAFT=1`: byte-identical to the one on disk (md5 925dfd39...), 1207 KB, under
2 MB; no http(s) src/href, no leftover `art:` tokens; `check_tools.py`: ok. No console errors in 60 shots (one favicon
404 from the host page only). Audit: every size, Motion off, resize, five-click and quick-tap rows clean; the same 4
"welcome not heard" leads final.md already settled (nothing new).

## Should fix

1. **Shadow and Noodle have cartoon faces, unlike the other 24** (should fix, art). Both have a big white-ringed eye,
   a pink cheek blush and a drawn grin (art/c-shadow-130.png, art/c-noodle-0.png; on stage:
   frames/myst5-16-1366.png, frames/myst3-16-1366.png, frames/parade-shadow-1366.png). The house style asks for
   "natural eyes ... not a cartoon mascot", and the rest of the set (Moose, Bear, Biscuit, every cat) follows it, so
   these two read as from a different book. This is the part Cory flagged (the faces). Noodle is also the oddest
   pose: the body points away with the head turned back over the shoulder, so it reads as walking toward the door
   while looking at Kip. Redraw both with the same prompt plus the house style (Shadow: a black Labrador-like dog,
   floppy ears, long snout, smooth coat; Noodle: a white fluffy dog with floppy ears and a medium-long snout, side
   view facing right), keep the clue values. Both are parade pets, so check the head centre in `ART` again after.

## Polish

2. **The look-alike line's end dot sits on an ear** (polish). The dot is drawn at the head top, which on the paintings
   is often an ear: Pippin's near ear tip (frames/pippin-11-1366.png, pippin-11-1920.png, zoom
   work/z-pippin-1920-badge.png) and Luna's right ear at 380 px (frames-narrow/n380-luna-2.png, zoom
   work/z380-luna.png, the dot covers most of the ear). Pippin's pointy ears are the very clue the lesson points at.
   Better: end the line a few px above the head (above the ear tips) instead of on it.
3. **Card crops clip some ear tips** (polish). Rocket, Inky, Ziggy and Duchess touch or lose the tip of an ear at the
   card's top edge (work/z-shelf-1920.png, work/z-shelf-680.png, work/z380-shelf.png). The builder aimed for "ear
   tips in". Better: move the crop down a little for tall-eared pets (or per pet in `ART`).
4. **Two small key leftovers between the legs** (polish). Bear has a keyed hole with a thin green-yellow rim between
   the hind legs, Biscuit a faint green sliver between the front legs (art/c-bear-80.png, art/c-biscuit-220.png on a
   dark ground). On the cream stage at real size neither is visible (work/z-bear-legs-1366.png,
   work/z-biscuit-legs-1366.png). No magenta (key) fringe on any pet: 0 to 9 magenta-ish pixels per painting, and
   the greenish counts in cats are their green eyes. Optional cleanup.
5. **A few paintings show their clue loosely** (polish). Checked all 26 against the data rows (art/sheet-bg0.png,
   art/sheet-bg2.png, work/deckgrid0.png, work/deckgrid1.png). Ears, snout, fluffy and dark read right for every pet
   the lesson leans on. Loose: Waffles (snout .20) has a medium puppy muzzle, not a flat face like Pudding; Noodle
   (fluffy .78) looks mostly smooth; Scout (dark .60) is a white dalmatian; Bear's ears (.50) are floppy. Kip's
   guesses are unchanged, so nothing is wrong on screen; only a teacher asking "why did Kip match these?" would see
   the gap. Fold Noodle into item 1; the rest can stay.
6. **Pebble wears a collar with a gold tag** (polish). The house style says no collar tags. The tag is blank (no
   lettering), so it is harmless; visible on its card at every size.
7. **At 680x425 the truth badge covers most of a pet's body** (polish, known from refine for the name). With the
   paintings, Shadow is nearly hidden behind the Dog badge (frames/parade-shadow-680.png) and so is the back half of
   Waffles (frames/waffles-10-680.png). Faces stay clear. Better: a smaller badge at that size, or beside the pet.

Also for whoever closes this: `art/prompts.json` still marks every pet `"review": "pending"`.

## The pets (extra attention)

- **Faces:** 24 of 26 read as friendly, natural cats and dogs with calm eyes and a small nose, one artist feel (soft
  gouache, dark outline). Every cat reads as a cat and every dog as a dog at a glance, on stage and on the cards,
  including at 380 px (frames-narrow/n380-shelf16.png). Exceptions: item 1.
- **Key surprises still fair and visible:**
  - Luna (black fluffy cat): with Marmalade and Bear on the wall Kip says Dog and draws the line to Bear
    (frames/luna-2-1366.png, luna-2-1920.png, luna-2-680.png, frames-narrow/n380-luna-2.png). Luna is clearly a cat
    (tall pointy ears, cat face) and clearly dark and fluffy like Bear, so the mistake is visible and fair. With 16
    cards she matches Smoky and is right (frames/myst2-16-1366.png).
  - Pippin (clearly a dog, pointy ears): 11 cards, Kip says Cat via Marmalade (frames/pippin-11-1366.png, -1920,
    -680); 12 cards, Ziggy is on the wall and Kip says Dog (frames/pippin-12-*.png). Pippin and Ziggy are painted as
    the same kind of fox-like dog, Pippin's ears are upright and pointy like a cat's: the lesson reads.
  - Maple matches Marmalade, Waffles matches Pudding (frames/myst0-16-1366.png, waffles-10-*.png); full deck parade
    10 of 10 (frames/parade-done-1366.png).
- **Dark pets:** Inky, Luna, Pepper, Moose, Shadow, Coco and Bear all read against the cream wall, the wood floor and
  the cream cards (frames/deck02-1366.png, deck13-1366.png, deck14-1366.png, motionoff-moose-1366.png,
  frames-narrow/n380-deck13.png).
- **Size, stretch, blur:** heights follow the size clue (Pepper and Marmalade small, Moose and Bear tall); width
  follows each painting's ratio, nothing stretched; 360 px sources stay sharp at 1920x1080 (frames/shelf16-1920.png,
  pippin-11-1920.png). No pet is cut off on stage at any size checked.

## Frames looked at

audit/: size-* at all 8 sizes, state-mode-pet-parade-* at all 8, calm-1366x768. frames/: deck00 to deck15 at
1366x768 (every deck pet arrived), myst0 to myst9 with 16 cards (every parade pet at the truth), luna-2, pippin-11,
pippin-12, waffles-10 at 1366, 1920 and 680; shelf16 at 1366, 1920, 680, 1280, 760; parade-shadow at 1366, 1920,
680; parade-done, motionoff-moose, fly, walk-mid at 1366. frames-narrow/ (380 wide host): Bear, Inky, Moose, Pepper
arriving; Luna 2 cards, Pippin 11, Shadow and Noodle with 16; full shelf; parade at Luna. art/: contact sheets of all
26 paintings on cream, white and dark grounds, and zooms.

Known and left (from final.md, still true): the look-alike line can cross a neighbouring card or name (frames/myst4-16-1366.png
crosses Biscuit and Pudding); at 1920 the line passes behind the truth badge (work/z-pippin-1920-badge.png); voice
was not re-run because no clip or line changed.
