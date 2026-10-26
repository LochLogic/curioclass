# Decision Tree art plan

Cory's review: "needs better navigation and graphics". Today the only painting is the FLUX hillside backdrop
(`art/bg-hillside.webp`, 46 KB); the trunk, mound, sign, branch tips, graft knot, buds and dilemma icons are all drawn
in code, and kids appear only as names. This plan paints the pieces a student looks at most: the four kids, the tree
base, the sign, the branch tips (where Blooming / Wilting happens) and the graft knot. Prompts are in
`art/prompts.json` (bg-hillside kept as is). The navigation half is `nav-plan.md`; the story card and sign button it
describes are where the portraits and the sign art go.

## Assets

| # | Name | Source | Source size | Budget (WebP) | Shown at (CSS px) | Replaces (src.html today) |
|---|---|---|---|---|---|---|
| 1 | kid-dev | Codex gpt-image-2, people | 3:4 cutout, height 320, q72 | 14-20 KB | picker 40 (head crop circle), story card 140 tall, choose card 72 | dilemma icon `pin` (ICON line 359), used by `buildPicker` (751-754); new story card (nav N2); `showCard` heading (855) |
| 2 | kid-kai | Codex, ref kid-dev, ref_mode style | same | 14-20 KB | same | icon `phone` (360) |
| 3 | kid-nia | Codex, ref kid-dev, ref_mode style | same | 14-20 KB | same | icon `jar` (361) |
| 4 | kid-theo | Codex, ref kid-dev, ref_mode style | same | 14-20 KB | same | icon `cart` (362) |
| 5 | tree-base | Cloudflare FLUX (`cfart.py`) | 4:3 cutout on magenta, width 640, q72 | 28-40 KB | 160-460 wide, bottom center of each tree | mound ellipse and trunk path in `buildStatic` (597-600) |
| 6 | sign-plank | Cloudflare FLUX | 5:1 cutout on green, width 480, q75 | 8-14 KB | 150-330 x 30-40, as a 9-slice | sign rect in `buildStatic` (601-605); becomes the sign button (nav N2) |
| 7 | tip-bloom | Cloudflare FLUX | 1:1 cutout on green, width 128, q75 | 5-9 KB | 44-52 (narrow crowns 34) | bark letter circle `.crown .let` (CSS 196, markup in `renderTree` 715) when Blooming |
| 8 | tip-even | Cloudflare FLUX | 1:1 cutout on magenta, width 128, q75 | 5-9 KB | same | same, when Even (and "Pick a goal") |
| 9 | tip-wilt | Cloudflare FLUX | 1:1 cutout on green, width 128, q75 | 5-9 KB | same | same, when Wilting |
| 10 | graft-knot | Cloudflare FLUX | 1:1 cutout on magenta, width 96, q75 | 3-6 KB | 28-32 | knot circle in `renderTree` (741-742) |

Only if Cory declines portraits (Question 1), draw these four instead of 1-4 (also FLUX, free, no people); they are in
prompts.json marked ALTERNATIVE in `local_note`:

| Name | What | Size | Budget |
|---|---|---|---|
| obj-booking | a bowling pin leaning on a small robot arm kit | 1:1 cutout, width 160, q75 | 6-10 KB |
| obj-quiz | a phone lying face up with a plain glowing screen beside a pencil | same | 6-10 KB |
| obj-tablet | a glass jar half full of coins beside a closed drawing tablet | same | 6-10 KB |
| obj-game | a game controller resting on a rolled-up blank poster | same | 6-10 KB |

Codex images: 4 first draws (plus 2-3 redraws allowed for faces or a mismatched sibling). Cloudflare: 6 assets, draw
3 candidates each (`--n 3`, about 18 images, about 1,900 of the 10,000 free daily neurons).

## Size and headroom

Measured: `python scripts/bundle_tool.py decision-tree` gives **563 KB** (578,654 bytes) today: src 82 KB, the
hillside 46 KB (61 KB as base64), the rest recorded voice.

| | Files | In the bundle (base64, x 4/3) |
|---|---|---|
| Portraits 4 x about 17 KB | 68 KB | 91 KB |
| tree-base | about 34 KB | 45 KB |
| sign-plank | about 11 KB | 15 KB |
| Three tips, about 7 KB each | 21 KB | 28 KB |
| graft-knot | about 4 KB | 6 KB |
| Three new voice clips (nav N4, about 15 KB) | 45 KB | 60 KB |
| Nav code and CSS (estimate) | about 12 KB | 12 KB |
| **Added** | **about 195 KB** | **about 257 KB** |

Bundle after: about **820 KB**. Limit 2 MB (taking 2,000,000 bytes to be safe): headroom today about **1.39 MB**,
after about **1.15 MB**. Even at the top of every range (about 330 KB added) it stays under 0.9 MB.

**Bundle rule that matters:** `bundle_tool.py` inlines a full copy of the image at every `art:<name>` token (no
dedupe). Each asset must appear exactly once in src.html. Put them in one map near the top of the script,
`const ART = {dev: 'art:kid-dev', kai: 'art:kid-kai', ...}`, and set them where used (an `<img src>`, an SVG `href`,
or a CSS custom property set once on `:root` from JS for the 9-slice sign and the crown tips). Three references to
a portrait would triple its weight.

## Wiring

### Portraits (kid-*)

- One `<img>` per use, `alt=""` (the name is in the text next to it), `object-fit: cover`.
- Picker card (`buildPicker`): the 24 px icon becomes a 40 px circle cropped to the head (`object-position` from the
  head-center fraction measured after the pick, kept in a small `HEAD = {dev: [x, y], ...}` table). Compact keeps
  32 px. The `pin/phone/jar/cart` ICON entries go.
- Story card (nav N2): 140 px tall on the left of the card, the setup text to its right; at under 420 px stage width,
  96 px above the text.
- Choose card (`showCard`): 72 px beside "{name} chose: ...".
- Side by side: no portraits on the stage (the two trees stay clean); the picker shows them.
- Print stays text only.
- Draw order: kid-dev first; pick it (`localart.py --pick kid-dev:20`) so `art/raw/kid-dev.png` exists as the style
  reference; then the three siblings with `ref_mode: style`. Look at all four side by side: same framing (head and
  shoulders, same head size), all facing forward, friendly, about twelve, no text on clothes.

### tree-base

- An SVG `<image>` in `gStatic`, one per tree, replacing the ellipse and trunk path. Placement by two measured
  anchors (fractions of the image, recorded after the pick in `BASE = {tx, ty}`): the trunk top center maps to
  `(g.tx, g.ty)` where the branches start; the image bottom sits at `by + 4`. Height = `(by + 4 - g.ty) / (1 - ty)`,
  width from the 4:3 aspect.
- Branch strokes stay vector (they animate and re-lay per box), so their color must match the painted bark: after the
  pick, sample the trunk's mid tone near the top and set `--bark` (and `#sv .bpath` stroke) to it, checking white on
  bark still passes AA for the crown letter (today 7.94:1 with #6b4a2f). Add a 1.5 px darker edge to `.bpath` (a
  second, wider stroke underneath in `#4a321e`) so vector branches read as the same wood.
- Fallback: if the image is missing in a draft build, keep today's ellipse and trunk path (keep the code behind
  `if (!ART.base)`).

### sign-plank

- The sign becomes a `<button class="sign">` in `#lay` (nav N2). CSS `border-image: var(--sign) 30% 12% fill / 10px
  22px stretch` so any width keeps clean plank ends; white 15 px bold text (12 px when `g.trunkH < 70`) with a 1 px dark
  text shadow. Check white on the plank's lightest wood tone is at least 4.5:1 after the pick; if not, darken the
  plank with a `linear-gradient(#0003,#0003)` layer under the border-image.
- Same position as today: centered on the trunk at `by - g.trunkH * .52`.

### Branch tips (tip-bloom, tip-even, tip-wilt)

- The crown's letter circle (`.crown .let`) becomes a 48 px box (36 px slim, 30 px narrow) with the tip painting as its
  background and a smaller 28 px bark circle holding the letter on top, so the big A to D letters stay readable on a
  projector. The badge chip (icon, word, tally) stays exactly as it is: the state is never shown by the painting alone.
- Status changes crossfade the background (300 ms, instant with Motion off) using two stacked layers.
- Set the three images once as CSS custom properties (`--tip-bloom` etc.) from the `ART` map; `.crown.s-bloom .let`
  picks one. `renderTree` (line 725) adds the `s-<status>` class to the crown.
- "Pick a goal" (no goals on) uses tip-even.

### graft-knot

- An SVG `<image>` 30 px square centered where the knot circle is (`kx, ky - 2`); the "Graft" text label and the dashed
  parent links stay.

### Backdrop

- bg-hillside stays. With the painted base and tips the stage carries more color, so drop the paper overlay
  (`buildStatic` line 583) from 0.35 to about 0.28 and re-check the leaf and focus-ring contrasts listed in verify.md
  (they are on the leaf fills, not the backdrop, so they hold).

### What stays vector

Branches and their growth animation, leaves (cards with text and marks), bands and band labels, buds, guide lines,
goal icons and arrows, badge chips, the flag, the Side by side labels, the ghost "Graft not found yet" bud,
preview.svg (rebuild it after: `scripts/preview.py decision-tree`).

## Docs to update when building

- spec.md: Art section (it says "No people or characters are drawn anywhere; kids appear only as names" and that the
  sign and tree are code), Look section if `--bark` changes.
- notes.md "Good to know" credit line; the comment at src.html line 21; tool.json sources: add "Illustrations generated
  with OpenAI gpt-image, edited for Curio Class" (portraits) and the Cloudflare FLUX.2 [klein] credit beside the
  FLUX.1-schnell one.

## Commands (Cory runs them, one at a time)

```
python scripts/gptart.py decision-tree kid-dev
python scripts/localart.py decision-tree --pick kid-dev:20
python scripts/gptart.py decision-tree kid-kai kid-nia kid-theo
python scripts/cfart.py decision-tree tree-base sign-plank tip-bloom tip-even tip-wilt graft-knot --n 3
python scripts/localart.py decision-tree --pick kid-kai:20 kid-nia:20 kid-theo:20 tree-base:9 sign-plank:9 tip-bloom:9 tip-even:9 tip-wilt:9 graft-knot:9
```

(Pick numbers are the first candidate; change them after looking at the contact sheets in `art/raw/`.) Then review
every image and set `review` in prompts.json.

## Questions for Cory

1. The spec chose "no people, kids appear only as names" on purpose for an SEL tool. Add the four Codex portraits
   (warmer, and the story card reads as a person's dilemma), or keep it people-free and use the four FLUX object
   vignettes (obj-*) in the picker and story card instead?
2. Kai and Dev have no pronouns in the content, so they are drawn with a relaxed, gender-neutral look; Nia is "her"
   and Theo is "he". OK?
3. The three new voice lines for the grey-button reasons (nav N4): record them, or show the reasons as text only (no
   clip, Read still speaks them through the hint)?
