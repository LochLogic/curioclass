# Art plan: volunteer portraits (Community Project Planner)

Cory's review: "good but needs better graphics for the people." The six volunteers are drawn in code today
(`faceSVG(v, band)` in src.html, a 48x48 vector face in a dark circle). This plan replaces them with painted
head-and-shoulders portraits from gpt-image-2 (Codex). The three FLUX banners stay as they are.

Phase 1 (this file and the new entries in `art/prompts.json`) is planning only. Nothing drawn, src.html untouched.

## Look

Editorial graphic-novel portraits (set per asset as `house_style`, with `skip_style` so the banners' landscape style
is not added): clean ink linework, flat muted color, soft cel shading, realistic teen and adult proportions. Each
portrait keeps the colors the code faces already use (skin, hair, top), so nothing in the spec's Volunteers table
changes. Cut out on a flat key (magenta for Dana's green hoodie and Mei's yellow sweater, green for the rest) and
shown inside the existing dark circle.

Proposed ages (the spec gives none; mixed so a student leader sees peers and grown-ups on the same team):

| Volunteer | Who | Look (from spec) |
|---|---|---|
| Dana Okafor | Black woman, early 40s, neighborhood parent | coily black hair, green hoodie |
| Luis Herrera | Latino, 17, high school junior | wavy dark hair, blue jacket |
| Mei Chen | Chinese American woman, about 27 | black bob with bangs, yellow sweater |
| Tariq Haddad | Arab American, 19, college student | short black hair, glasses, gray shirt |
| Grace Whitehorse | Native American woman, late 50s | long straight black hair with a few silver strands, red flannel; everyday clothes only, no regalia |
| Ben Novak | white, 16, high school sophomore | short red-brown hair, freckles, purple tee |

## Assets

All are `"people": true`, source gpt-image-2 (Codex), 1:1, cutout, exported 192 px wide WebP quality 80
(the largest show size is 54 px, so 192 covers 2x screens and leaves room to grow the meet row to 72 px).

| # | Name | Source | Budget | Replaces (code-drawn) | Where in src.html |
|---|---|---|---|---|---|
| 1 | vol-dana | Codex, no ref (style anchor) | 15 KB | Dana's vector face, Fired up and Steady | `faceSVG` (line ~815), called by the meet row (line ~838) and the volunteer cards (`vc.fwrap`, line ~979) |
| 2 | vol-luis | Codex, ref vol-dana (style mode) | 15 KB | Luis, Fired up and Steady | same |
| 3 | vol-mei | Codex, ref vol-dana (style mode) | 15 KB | Mei, Fired up and Steady | same |
| 4 | vol-tariq | Codex, ref vol-dana (style mode) | 15 KB | Tariq, Fired up and Steady | same |
| 5 | vol-grace | Codex, ref vol-dana (style mode) | 15 KB | Grace, Fired up and Steady | same |
| 6 | vol-ben | Codex, ref vol-dana (style mode) | 15 KB | Ben, Fired up and Steady | same |
| 7 | vol-dana-tired | Codex, ref vol-dana (exact) | 15 KB | Dana, Tired / Running on empty / Stepping back | same, chosen by band |
| 8 | vol-luis-tired | Codex, ref vol-luis | 15 KB | Luis, low bands | same |
| 9 | vol-mei-tired | Codex, ref vol-mei | 15 KB | Mei, low bands | same |
| 10 | vol-tariq-tired | Codex, ref vol-tariq | 15 KB | Tariq, low bands | same |
| 11 | vol-grace-tired | Codex, ref vol-grace | 15 KB | Grace, low bands | same |
| 12 | vol-ben-tired | Codex, ref vol-ben | 15 KB | Ben, low bands | same |

Codex images: 12 (6 bases plus 6 tired variants), one candidate each. Size: about 12 KB expected per portrait at
192 px, budget 15 KB each, 180 KB for the set, well under the 600 KB cap (bundle 0.67 MB now, about 0.85 MB after).

Nothing new from FLUX: there is no non-people art missing. The banners need no change.

## Draw order

1. **vol-dana** alone. Review it (face, hands absent, no text, cutout clean, reads at 19 px). It sets the style for
   everyone, so do not go on until it is right.
2. **vol-luis, vol-mei, vol-tariq, vol-grace, vol-ben**, each with vol-dana as a style reference (`"ref"` plus `"ref_mode": "style"` in prompts.json). Review the six
   side by side as one set (same line weight, same framing, head size within about 10 percent).
3. Pick and cut all six (`localart.py --pick vol-x:20`), wire them in (phase 2) and check the board at every layout.
4. **Tired variants**, only if the bases passed without retakes and the Codex allowance is left. Each refers to its
   own base. If the allowance is short, skip this round: the vector fallback below covers the low bands.

Retakes come out of the same 12. If a base needs a second try, drop the tired round for now rather than go over.

Prerequisite for step 2: `scripts/gptart.py` ignores `ref_mode` today and always adds "Match the character design
... exactly", which would turn all five into copies of Dana. Before drawing step 2 it needs a two-line change: when
`ref_mode` is "style", add "Match only the drawing style, line quality, lighting and framing of the reference image.
Draw a different person, as described." (art.py's own style sentence says "a different child" and "uniform", which
does not fit adults.) Without that change, draw the five with no ref and rely on the shared house_style text.

## How the energy bands map (what stays vector)

The band word, glyph and colored bar already carry the meaning (never color alone); the portrait adds mood.

| Band | Image | Vector on top (CSS / SVG) |
|---|---|---|
| Fired up | base | the existing 3.2 s bob (off under Motion off) |
| Steady | base | none |
| Tired | tired | none |
| Running on empty | tired | tilt 5 degrees and drop 2 px, 30 percent desaturate |
| Stepping back | tired | grayscale, the card's existing .45 opacity on `.fwrap`, the existing "z" moved into a small pause badge |

Without the tired round: Tired = base with 4 degree tilt and 15 percent desaturate, Running on empty = more tilt and
35 percent, Stepping back = grayscale plus the badge.

Stays vector: the dark circle behind each face, the bob, tilts and filters above, the "z" / pause badge, skill icons,
band glyphs, energy bars, task cards, the timeline. `faceSVG` stays as the fallback if an image fails to load
(`onerror` swaps to it) so the tool never shows an empty circle.

## Show sizes to check in phase 2

- Meet row on the picker: 54 px (34 px in short compact). Could grow to 72 px now that the faces carry detail.
- Volunteer cards: 42 px, 32 / 26 px in short compact, **19 px in the tiny 680x425 layout**. At 19 px only skin,
  hair shape and top color read, so the portrait framing keeps the face large (top of hair to mid-chest), and
  phase 2 can set `object-position` toward the face for that size.
- Optional reuse (no new images): the report's "The team at the end" row and the week summary list could show each
  portrait at its final band beside the name.

## Phase 2 checklist

- `<img src="art:vol-<id>">` / `art:vol-<id>-tired` in the meet row and `.fwrap`, circle-clipped, `alt=""` (the card
  already has a full aria-label).
- Update the src.html header comment, spec.md Art and the Volunteers table "Look (drawn in code)" heading, and
  tool.json sources: add "Illustrations generated with OpenAI gpt-image, edited for Curio Class"; drop "faces drawn
  in code".
- Review every portrait (no text, no odd hands, respectful and age-accurate), set `review` in prompts.json, run
  `artstatus.py`, rebundle and check the 2 MB limit.
