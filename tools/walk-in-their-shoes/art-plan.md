# Walk in Their Shoes: art plan

Cory's review (2026-10-26): "Everything seems good here, the personified animals are a good choice. lets just improve
the graphics." Today every character, face, shoe, setting and cover is drawn in code (`drawChar`, `face`, `shoeOne`,
`setting`, `coverArt`, `bookIcon` in src.html). This plan swaps those for painted art and keeps vector only where the
lesson needs it. Prompts are in `art/prompts.json`.

## The key idea: one Codex image per character

The nine characters need 35 different looks (expression plus prop), counted from the spec's beats and endings. Drawing
each look as its own image would take 35 Codex turns; the allowance is about 12. So each character is drawn **once, as
a character sheet**: every look that character needs, side by side in one row, in one gpt-image-2 image. Looks inside
one image match each other by construction (same face, outfit, shoes, light). Sheets after the first use Juniper's as a
style reference (`"ref": "juniper", "ref_mode": "style"`) so the three stories look like one book.

Each sheet is cut out once, then split into cells by its transparent gaps and repacked into a sprite with equal cell
widths and feet on one baseline. The tool shows one cell with an SVG `<image>` inside a nested `<svg viewBox>`. The
`"cells"` list in each asset names the cells left to right; `src.html` maps a beat's expression (and prop) to a cell.

## Assets

Sizes are WebP file bytes (the bundle adds a third for base64). Source: Codex = `scripts/gptart.py` (gpt-image-2),
Cloudflare = `scripts/cfart.py` (FLUX.2 klein, free tier). No asset shows a person; characters are marked
`"skip_local": true` so Cloudflare and local FLUX never draw them.

| Asset | Source | Cells (left to right) | Size budget | Replaces | Where in src.html |
|---|---|---|---|---|---|
| juniper (fox) | Codex | happy, calm, upset-muddy, calm-clean | 18 KB | `drawChar` fox + `face()`, `o.hold` jacket | `drawChar`, `drawScene`, `coverArt` |
| pip (rabbit) | Codex | happy-jacket, worried-jacket (muddy sleeve), worried, sad, happy | 22 KB | `drawChar` rabbit, `o.jacket`, `o.mud` | same |
| otto (bear) | Codex | calm, surprised, worried, happy, sad | 22 KB | `drawChar` bear | same |
| tamsin (heron) | Codex | worried, sad, happy (tray in all) | 14 KB | `drawChar` heron, `o.tray` | same |
| rory (badger) | Codex | happy, surprised, worried | 13 KB | `drawChar` badger | same |
| wren (owl) | Codex | calm, worried, surprised, happy | 18 KB | `drawChar` owl | same |
| bea (turtle) | Codex | calm, worried (glove loose), sad (glove loose), calm-glove (showing it) | 18 KB | `drawChar` turtle, `o.loose` | same |
| max (goat) | Codex | happy, surprised, upset, calm, sad | 22 KB | `drawChar` goat | same |
| dot (hedgehog) | Codex | happy, worried | 9 KB | `drawChar` hedgehog | same |
| bg-playground | Cloudflare | | 17 KB | `setting('playground')` (sky, clouds, trees, slide, puddle) | `setting`, `coverArt` |
| bg-lunchroom | Cloudflare | | 17 KB | `setting('lunchroom')` (walls, windows, band room door, floor) plus the two `table()` calls | `setting`, `drawScene`, `coverArt` |
| bg-field | Cloudflare | | 17 KB | `setting('field')` (sky, tree line, stripes, lines, goal) | `setting`, `coverArt` |
| duckling | Cloudflare | | 3 KB | the vector duckling in beat 2 of The Muddy Sleeve | `drawScene` (`st.id === 'mud' && beat 2`) |
| stool | Cloudflare | | 1.5 KB | the red saved-seat stool (beats 1 to 3) | `drawScene` (`st.id === 'seat'`) |
| book | Cloudflare | | 1.5 KB | `bookIcon` (Narrator button) | `buildRack` |
| shoes-juniper ... shoes-dot (9) | Cloudflare | | 9 x 1.6 = 14 KB | `shoeOne` / `shoes()` on the rack | `buildRack` |
| **Total** | | 35 cells | **about 227 KB** | | |

Character cells are sized to 240 px tall at quality 70 (a front character shows about 175 px tall at 1366x768 and about
240 px on a 1080p projector), about 4.5 KB a cell. Backgrounds are 720 px wide at quality 55: they sit behind the
characters, are painted soft, and compress well.

Bundle check: the limit is 2,097,152 bytes and the bundle is 1,737,353 now, so 359,799 bytes of headroom. 227 KB of
WebP is about 310 KB as base64; removing `drawChar`, `face`, `shoeOne` and most of `setting` gives back roughly 12 KB of
code. Expected bundle about 2.03 MB of 2.10 MB, a margin of about 45 KB.

**Reference each `art:` token exactly once in src.html** (for example in one `const ART = {...}` map) and reuse the
variable: `bundle_tool.py` inlines a data URI at every occurrence, so a sprite named twice (scene and cover) would be
paid twice.

## Codex count

9 character sheets, plus up to 3 redraws held back for a sheet that comes back with a bad cell (odd hands, a figure
touching its neighbor, a missing prop, a wrong shoe color). Total at most **12**.

## Order to draw

1. `juniper` (Codex, no ref). Look at it closely: it sets the style for the whole cast. Pick it
   (`localart.py --pick juniper:20`) so `art/raw/juniper.png` exists for the others' ref.
2. `pip`, `otto` (finish Story 1, so its three can be checked side by side).
3. `tamsin`, `rory`, `wren`.
4. `bea`, `max`, `dot`. Max and Dot wear the same sky-blue team jersey; if they differ, redraw one with the other as a
   style ref.
5. Cloudflare, any time and in any order (free, about 95 a day): `bg-playground`, `bg-lunchroom`, `bg-field`
   (`--n 3` each, pick the one whose horizon sits at half height and whose middle ground is open), then `duckling`,
   `stool`, `book` and the nine `shoes-*` (`--n 2`). Compare each shoe pair with the shoes on its painted character
   before picking; the rack must match the feet.

## Wiring notes (phase 2)

- **gptart.py ignores `ref_mode`.** It always adds "Match the character design ... exactly" when a ref is attached,
  which would turn every animal into a fox. Before drawing step 2, make `gptart.prompt_for` mirror art.py: with
  `ref_mode: "style"`, ask to match only the drawing style, line quality, proportions and lighting. (Or draw without a
  ref and lean on the shared tool style.)
- **Splitting sheets.** Add a `"cells"` step to the rekey path (art.py, used by `--pick`): after the cutout, find the
  figures as alpha blobs left to right, check there are exactly `len(cells)` of them, align their feet, center each in
  an equal-width cell, size to `height`, and save one sprite. Also write each cell's head-top offset (alpha bounding
  box) so `drawBubble` can anchor the thought bubble; it replaces `ANIMAL[an].top`.
- **Keys.** Pip (green sneakers) and Bea (green skin, green laces) use the magenta key; everyone else uses green. The
  jacket is light blue (it was purple in code) so it survives either key and the mud reads on it.
- **Expression map.** Each beat's `ex` stays as it is; a small table picks the cell from expression plus state: Pip
  wears the jacket on beats 1 and 2 (`happy-jacket`, `worried-jacket`); Juniper holds the jacket from beat 3 on
  (`upset-muddy`, and `calm-clean` in ending B); Bea shows `calm-glove` in ending B, `worried`/`sad` cells already show
  the loose glove. `sceneLabel` keeps reading the expression word.
- **Backgrounds.** Draw them with `preserveAspectRatio="xMidYMid slice"` so the painted horizon stays at `hz = H * .5`.
  Narrow stages crop the sides: check that the slide and puddle (playground), the band room door (lunchroom, where
  Wren stands at x .91) and the goal (field, ball at x .1) still show at 375 and 760 wide; if not, nudge `POS` and the
  ball positions toward the center.
- **Covers.** `coverArt` reuses the scene background and each character's first-beat cell (Tamsin uses `happy`).
  No extra cover art.
- **Credits.** tool.json sources and the src.html header: "Illustrations generated with OpenAI gpt-image, edited for
  Curio Class" and the Cloudflare FLUX.2 klein credit; drop "drawn in code". notes.md's last bullet changes the same
  way.
- `preview.svg` (catalog card) is drawn from the old vector cast; refresh it from the new art after wiring.

## Stays vector

- The thought bubble, its tail dots and the "?" bubble (HTML, they wrap text and follow the head).
- The spotlight glow and the brand ring under the selected character, the ground shadows, and the 85 percent dimming
  of the other two (they respond to the shoe rack and must stay brand-colored and outlined, not color alone).
- The soccer ball and its dashed flight path (it moves between beats).
- Beat dots, buttons, focus rings and the Motion fades.

## If it does not fit

In order: re-encode backgrounds at quality 50 (about 6 KB back); keep the vector shoes on the rack instead of the nine
painted pairs (14 KB back); merge rarely used cells (Otto surprised into worried, Max surprised into upset; about 9 KB).
Voice is already 16 kbps (1.23 MB of MP3); dropping to 12 kbps would free about 300 KB but costs clarity in a
read-aloud tool, so it is the last resort, not the plan.

## As built (2026-10-26)

- The real budget was the bundle, not the 227 KB plan: base64 adds a third, so the art had to stay near 165 KB for
  a bundle under 1.95 MB. Final: 165.0 KB of WebP, bundle 1,945,373 bytes.
- Cells: `scripts/split_sheet.py` keys each raw sheet, splits it at its empty columns (Otto's sheet had two shoes
  touching, so it cut at the emptiest column there), scales the whole sheet so its tallest figure is 170 px (a slumped
  pose stays shorter), and saves `art/<name>-<n>.webp` at quality 24 with alpha quality 10, plus `cells.json`.
  35 cells, 93.5 KB (2.7 KB each on average): Juniper 9.9, Pip 12.1, Otto 11.7, Tamsin 8.6, Rory 8.1, Wren 12.3,
  Bea 11.1, Max 13.6, Dot 6.1. The nine whole-sheet WebPs were deleted; the raws stay in art/raw/.
- Settings 41.4 KB (720x411; the field is trimmed 3.5 percent for its painted frame), shoes 21.0 KB (100 px wide,
  quality 50), duckling, stool and book 9.1 KB.
- Horizons measured from the paintings: playground .56, lunchroom .68, field .54. Wren waits by the band room door
  at x .94; the ball ends inside the painted goal at x .26.
- Covers reuse each setting and the characters' cells; no extra cover art.
