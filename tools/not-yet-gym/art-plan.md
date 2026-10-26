# Not Yet Gym art plan

Cory's review: "name is okay but im sure there is a better one. graphics could use a bit for work". Today the one image
is the FLUX backdrop `art/gym-hall.webp` (50 KB); Bix, Dot, the doors, the climbing wall, the room views, the goal board
and the locker are drawn in code. This plan paints Bix and Dot (gpt-image-2 through Codex) and gives every scene a
painted setting (Cloudflare FLUX), while keeping everything that carries text, state or accessibility in code. Prompts
are in `art/prompts.json` (20 new entries after `gym-hall`, which stays as it is). Nothing is drawn or wired yet.

## Bix: six paintings, five colors, gear on top

Bix has six faces (`bix()` face branches, src.html 589-607), five color swatches (`COLORS`, 272-273), four pieces of gear
that drop on by stage (`gearOf`, 553) and a headband that shows the comeback stripe count (573-581). Painting every
combination is out of the question, so:

- **One painting per face, in a pale neutral.** Bix is painted near-white with lavender-grey shading and dark plum limbs.
  The tool tints the image to the chosen swatch with an SVG multiply filter, one per color, defined once in `render()`'s
  `<defs>`: `<filter id="tint-pink" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="r 0 0 0 0 0 g 0 0 0 0 0 b 0 0 0 0 0 1 0"/></filter>`
  with r, g, b = the swatch / 255. Dark plum lines and eyes stay dark; the pale body takes the color with its shading.
  (Pink #f6b3c8 is 0.96, 0.70, 0.78; Mint #9fe3c9 is 0.62, 0.89, 0.79.) The ink-on-swatch contrast ratios in spec.md
  hold, since the body ends up the swatch color or a little darker in shade only.
- **Gear stays separate.** The headband stays code (it shows 0 to 10 stripes or "x12"), drawn as a slightly curved strip
  between two anchor points on the forehead instead of clipped to the old `BLOB` path. Sneakers, gym bag and medal
  become small FLUX cutouts placed at anchors. All four keep the `a-drop` stage-up animation.
- **Anchors.** After each pick, measure and store per painting, as fractions of the image:
  `ANCHOR['bix-cheer'] = {fx, fy, bandL, bandR, bandY, chest, shoulder, handL, handR, bodyH}` (feet center, band line,
  medal point, bag strap start, hands for juggling, and the body height so all six paintings draw the body at one
  scale even though cheer's raised arms make its image taller).

| Face (spec) | When (src.html) | Painting | Notes |
|---|---|---|---|
| happy (idle) | Gym map 1169, Locker 1485, room default | `bix` | also the arms-down frame of jumping jacks |
| focused | room with a puzzle showing (696, 991) | `bix-focused` | |
| thinking | after a not-yet (701) | `bix-thinking` | hand under chin; curious, never sad |
| cheer | comeback (730), goal done (1027) | `bix-cheer` | arms up; also the arms-up jacks frame and the juggling pose |
| proud | first-try solve (731) | `bix-proud` | thumbs up |
| calm | breathing card (973) | `bix-calm` | under the `a-breathe` scale |

### Moves (stage taps, `act` 1535) with paintings

- hop, spin, cartwheel, big jump, breathe: whole-figure CSS transforms on `.bxw`, as now (136-158). No change.
- jumping jacks: today `.armsd` / `.armsu` swap two code arm groups (140-143). With paintings, `.armsd` holds the
  `bix` image and `.armsu` the `bix-cheer` image, same steps(1) keyframes.
- juggling: shows `bix-cheer` while `.a-juggle` runs, code balls (`.balls`, 146-152) re-aimed at the hand anchors.

### Changing faces

Two `<image>` elements in the Bix group (outgoing and incoming); the incoming one fades in over 250 ms and the outgoing
one fades out, driven by the existing `anim()` / `animAttr()` pair so a re-render mid-fade continues instead of
restarting (a new `anims.face = {from, to}`). When Motion is off (`Curio.reduce`), the swap is instant and no move
animations play, exactly as today. The stage-up glow (`#bxglow`, 1115) stays code.

## Assets

Codex = `python scripts/gptart.py not-yet-gym <names>` (gpt-image-2, the only source for characters with faces or hands;
these are `"people": true` so the FLUX scripts skip them). FLUX = `python scripts/cfart.py not-yet-gym <names>`
(Cloudflare FLUX.2 klein, free; it uses the `"sd"` prompt and adds "No people."). Cutouts are on green (none of them is
green; Dot is lilac, the climbing wall's green holds sit inside the panel and survive the key because the cutout keeps
interior pixels, but check them).

| # | Name | Source | Replaces (src.html) | Display size (CSS px) | Output | Budget (WebP) |
|---|---|---|---|---|---|---|
| 1 | bix | Codex | `bix()` 554-617 and `BLOB` 548-552, happy face | Gym 80-260 tall, room 64-190, Locker 90-420 | 1:1, h 480, q 72, cutout | 22-30 KB |
| 2 | bix-focused | Codex, ref bix | same, focused face | same | same | 22-30 KB |
| 3 | bix-thinking | Codex, ref bix | same, thinking face and arm | same | same | 22-30 KB |
| 4 | bix-cheer | Codex, ref bix | same, cheer face and arms up; jacks up frame | same | same | 22-30 KB |
| 5 | bix-proud | Codex, ref bix | same, proud face and thumbs up | same | same | 22-30 KB |
| 6 | bix-calm | Codex, ref bix | same, calm face | same | same | 22-30 KB |
| 7 | dot | Codex, ref bix (style) | `dot()` 618-624 | 32-95 tall | 1:1, h 240, q 72, cutout | 8-12 KB |
| 8 | door | FLUX | door rect, inner panel and knob in `gymScene` 1146-1149 | 56-132 x 84-210 | 9:16, h 360, q 70, cutout; tinted per room | 10-14 KB |
| 9 | padlock | FLUX | code padlock 1154-1156 | 20-40 | 1:1, h 120, q 72, cutout | 3-5 KB |
| 10 | climb-wall | FLUX | Summit wall rect and holds 1139-1143 | 70-165 x 40-120 | 16:10, w 400, q 70, cutout | 12-18 KB |
| 11 | sneaker | FLUX | code shoes in `bix()` 561-563 (one image, mirrored) | 10-90 wide | 4:3, w 128, q 72, cutout | 4-6 KB |
| 12 | gym-bag | FLUX | code bag in `bix()` 565-566 (strap stays a code line) | 25-130 wide | 4:3, w 200, q 72, cutout | 5-9 KB |
| 13 | medal | FLUX | code medal in `bix()` 609 | 15-110 tall | 3:4, h 160, q 72, cutout | 4-7 KB |
| 14 | room-pattern | FLUX | flat `#roomBg` gradient in `roomScene` 1187 | full stage | 16:10, w 1280, q 58 | 22-32 KB |
| 15 | room-memory | FLUX | same | full stage | same | 22-32 KB |
| 16 | room-light | FLUX | same | full stage | same | 22-32 KB |
| 17 | room-lift | FLUX | same | full stage | same | 22-32 KB |
| 18 | room-summit | FLUX | same (Summit rungs) | full stage | same | 22-32 KB |
| 19 | board-cork | FLUX | cork fill and 70 speckles in `goalsScene` 1406-1409 | inner board rect | 16:10, w 1024, q 56, texture | 30-40 KB |
| 20 | locker-room | FLUX | locker row and floor in `lockerScene` 1474-1478 | full stage | 16:10, w 1280, q 58 | 28-40 KB |

Codex images: 7 first draws (bix first, alone; the five variants with plain `"ref": "bix"` so it is the same character;
Dot with `"ref_mode": "style"` so it is a different character drawn the same way). Allow 2-3 redraws, most likely for
the thumbs-up hand or a variant that drifts off the pale body color. FLUX: 13 assets, free, about 3 candidates each.

## Size

Measured 2026-10-26: `python scripts/bundle_tool.py not-yet-gym` gives `not-yet-gym.html` at 1,352,634 bytes
(1,321 KB; the script prints 1319). The limit (`scripts/check_tools.py`) is 2 x 1024 x 1024 = 2,097,152 bytes, so
**headroom today is 744,518 bytes (727 KB of bundle, about 545 KB of WebP after base64)**. Of today's bundle, recorded
speech is 1,145 KB of base64 and the gym-hall image 67 KB.

| | New art as files | In the bundle (x 4/3) | Bundle after | Headroom after |
|---|---|---|---|---|
| Target (middle of each budget) | 419 KB | 559 KB | about 1,880 KB | about 168 KB |
| Every asset at its cap | 491 KB | 655 KB | about 1,976 KB | about 72 KB |

Both are under the 600 KB guide and under 2 MB. Removing the vector Bix, Dot, door, wall and padlock code saves a few
KB more. If it gets tight: drop a painting to quality 66 with `art.py --rekey` (free); drop `board-cork` (keep the code
cork, 35 KB); or set `"kbps": 16` in `voice/lines.json` (speech is most of the bundle; that roughly halves it if the
lines are recorded above 16 kbps today). `gym-hall` stays, so nothing is freed there.

## Draw order

1. `bix` alone (Codex). Pick it (`python scripts/localart.py not-yet-gym --pick bix:20`) so `art/raw/bix.png` exists for
   the refs. Check it tints well: try it under the pink and mint filters before going on (pale, evenly lit body, no
   pink patches, no text).
2. The five variants and Dot:
   `python scripts/gptart.py not-yet-gym bix-focused bix-thinking bix-cheer bix-proud bix-calm dot`
   Look at all six Bix side by side: same body shape, same size of body, all front facing, thinking never sad.
3. FLUX objects and scenes (free, 3 candidates each):
   `python scripts/cfart.py not-yet-gym door padlock climb-wall sneaker gym-bag medal --n 3`
   `python scripts/cfart.py not-yet-gym room-pattern room-memory room-light room-lift room-summit board-cork locker-room --n 3`
   Pick with `localart.py --pick name:<k>` (FLUX candidates are k 9 to 11).
4. Review every image (Bix hands and faces, no lettering anywhere, rooms plain in the middle), set `review` in
   prompts.json.

## Wiring notes (phase 2)

- `bix(o)` keeps its signature `{x, y, h, face}`: it places `art:bix-<face>` (happy uses `art:bix`) by the feet anchor,
  scaled by `bodyH`, with `filter="url(#tint-<color>)"`; then the band strip, sneakers, bag and medal at anchors.
  The `deco`, `.bxw` and animation classes stay where they are.
- `dot()` becomes one `<image href="art:dot">` placed by its feet.
- Doors: the painted door is tinted with a per-room filter (five filters plus a "locked" grey one, built from
  `ROOMS[room].door` and the existing `mix(..., '#c7c2d3', .65)`); the plaque, labels, star and padlock image draw on
  top. The `a-rattle` group wraps the image too.
- Rooms: `roomScene` draws `art:room-<P.room>` full frame (slice) with a `#fbf7ff` rect at about .55 on top, then the
  floor strip, title and puzzle as now. Summit rungs use `room-summit`.
- Gym map: keep `gym-hall`. Optional, free: lower the white overlay (1126) from .4 to about .25 and the code floor
  (1128) from .92 to about .6 so the painted wood shows through.
- Goals: `board-cork` is clipped to the inner board rect (`<clipPath>` with the rx 8 rect), slice.
- Locker: `locker-room` full frame (xMidYMax slice) with a light paper overlay; the code floor band can go if the
  painted floor lines up at 74% height, otherwise keep it at reduced opacity.
- Check every size in STANDARDS.md (680x425 preview, 1366x768, 375 wide): Bix in the room corner at 64 px must still
  show its face; the tinted door must keep the plaque readable.
- Update spec.md (Art, Look, "drawn in code" lines), notes.md (Good to know), the src.html header comment (lines 20-21)
  and tool.json sources: add "Illustrations generated with OpenAI gpt-image, edited for Curio Class" and the
  Cloudflare FLUX.2 klein (Apache 2.0) credit next to the FLUX.1-schnell one. Rebuild preview.svg
  (`scripts/preview.py not-yet-gym`), it shows the vector Bix.

## What stays vector

- The headband and its stripes or "x12" count; the stage-up glow; juggling balls; confetti.
- Every puzzle: pattern items, Memory Mirror pads (shape plus name, never color alone), the Light Mat squares, the Number
  Lift car and buttons, rung labels and brackets. These carry state and must stay crisp and accessible.
- The door name plaques and labels, goal cards, Done column, sticker wall and icons, Coach's corner cards, speech
  bubbles and banners: all text.
- The floor strips and baseboards where a painted floor would not line up across stage shapes.

## Name

Not renaming anything; these are options for Cory. "Brain Gym" is out (registered to Brain Gym International). Also
avoided: "The Power of Yet" (Dweck's talk title and a Sesame Street song), "Brainology" (a Mindset Works product),
"Unstuck" (an existing self-help app) and anything with "Level Up" (crowded in app marks). Checked by web search on
2026-10-26: no trademark or kids app found for the five new names below. That is a quick check, not a clearance; a
USPTO search in class 41 (education) and 9 (software) is the real one before a rename.

| Name | Why |
|---|---|
| Not Yet Gym (keep) | Says the idea in two words ("not yet" means still learning); already live, voiced and in every file. |
| Bix's Comeback Gym | Names the mascot and the core rule: comebacks are worth more than first tries. The verify report suggested it. |
| Comeback Climb | The journey up to Summit Circuit plus the comeback stripes; no "gym" or "brain" baggage at all. |
| Comeback Club | Short, friendly, sounds like something a class joins; a student design project used it, no mark found. |
| Practice Gym | Plainest and most honest about what the tool claims (practice helps); easy for a teacher to search for. |
| Second Try Gym | Kid-readable version of the "not yet" idea; puts the moment after a mistake in the title. |

If Cory picks one with "Comeback", the welcome line ("Welcome to the Not Yet Gym!") and the title need re-recording
(one voice line, `voice.py`).

## Questions for Cory

1. Bix's five color swatches: tinting one pale painting works but each swatch is a tint, not a hand-painted color. OK,
   or cut the swatches to fewer (or none) and paint Bix in one color?
2. Gear (sneakers, bag, medal) from free FLUX next to a Codex Bix may not match in style. Accept and redraw if it
   clashes, or spend 3 more Codex images on gear with `"ref_mode": "style"`?
3. "Dot" is also the hedgehog in walk-in-their-shoes (3-5, a neighbor). Fine, or give the friend another name later
   (no rename now)?
4. Gym hall: keep `gym-hall` with a lighter overlay (free), or also redraw it?
