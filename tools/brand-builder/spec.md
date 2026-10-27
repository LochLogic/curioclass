# Brand Builder

## One idea
A logo is not done until it survives the real world: design a mark, name and colors for a made-up business once, then watch the same brand land on a 16 pixel browser tab, a circle avatar, a one-ink paper bag, a dark shirt and a black-and-white newspaper, with each surface's test telling you exactly what broke.

## Not like
- design-fixer (6-8): fixes where the eye lands on one poster, judged by squinting. Here the brand is judged by how it holds up across many sizes and printing limits; nothing is squinted at.
- virtual-gallery (9-12): presents finished artworks in a room. Here you design the thing, and the "room" is a wall of real-world surfaces.
- gallery-critique (9-12): debates one painting's meaning. Here critique is tied to a client brief's three words.
- storyboard-studio (9-12, same group): time and camera. Here a single still mark under stress.
- flipbook-studio (6-8, same group): loose pencil drawing. Here clean vector shapes and real typefaces.

## Who and how
- Grade 9-12, media arts, module "Graphic Design (Media Arts)".
- Topic line: logos, typography and color for a brand
- Driver: students (laptops, alone, then pairs swap laptops for the critique). 25 to 45 minutes; brands are saved on this device.
- Standards: NCAS Media Arts MA:Cr2.1.HSI (develop and refine a design to a brief), MA:Cr3.1.HSI (refine for intent and audience); also VA:Cr3.1.HSI (critique and revise).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Modes (`.seg`): `Brief` (default on first load), `Design`, `Test`, `Sheet`. A small brand preview (current lockup) stays in the panel top in every mode.

**Brief.** Six client cards (Content "Briefs") plus `My own business` (a name field and three word fields; text stays on this device). Each card: business name, what it does, who it is for, three personality words, where the brand must work (one constraint). `Start this brand` opens Design. Each brief keeps its own saved brand; a tick shows which have one.

**Design.** Stage: the lockup large on a white artboard with a faint 8-unit grid. Panel, in four collapsible sections:
- `Mark`: `Symbol` grid of 24 symbols (Content), each `Filled` or `Line`; `Line weight` (Thin / Regular / Heavy, for Line symbols); `Container` (None / Circle / Rounded square / Shield / Hexagon); `Monogram` (none, or 1 to 2 letters set in the chosen typeface, inside the container instead of or beside the symbol); `Scale` and `Rotate` (15 degree steps) for the symbol.
- `Name`: `Typeface` (8, Content), `Weight` (where the face has two), `Case` (As typed / UPPERCASE / lowercase), `Spacing` (letter spacing, -20 to +200 thousandths of an em, steps of 10), `Tagline` on or off (the brief's tagline, Content).
- `Color`: `Primary`, `Secondary`, `Ink` (for text), each from a 24-swatch palette or `Custom` (hue and lightness sliders); live readouts "Ink on white 12.4:1" and "Primary on white 3.2:1".
- `Lockup`: `Side by side` / `Stacked` / `Mark only` / `Name only`.
`Undo`, `Redo`, `Start over` (this brand only, with a confirm).

**Test.** The surfaces wall: eight tiles (Content "Surfaces"), each showing the current brand applied the way that surface would really print or display, with a test row under it: a tick or a cross icon, a word ("Holds up" / "Breaks"), and the number. Tap a tile to open it large with a `Why` note and a `Fix in Design` button that jumps to the control most likely to fix it (for example Line weight for a small-size break). A `Brief fit` card at the end: the three words, each with `Not yet` / `Some` / `Yes` and a one-line note field ("Which choice says it?"), set by the student; not scored by the tool.

**Sheet.** The brand sheet, printable (black-on-white friendly; colors print as swatches with their hex values): the lockups (side by side, stacked, mark only), clear space (shown as a box around the lockup), minimum size (the smallest width at which the small-size test still passes), the colors with hex and contrast ratios on white and on black, the typeface name, its class and its license line, and the brief fit notes. `Print sheet`. A `Critique swap` card: four prompts for a partner who sits down at this laptop (Content).

## Content
**Briefs** (all businesses made up for this tool):
1. Pocket Moon Bakery. A small bakery that opens before sunrise. For neighbors on the way to work and school. Words: cozy, handmade, early. Must work: stamped on paper bags in one ink color. Tagline: "Warm before the sun."
2. Gearfox Bike Repair. A van that comes to you and fixes bikes. For commuters and kids. Words: quick, tough, trusty. Must work: as a phone app icon. Tagline: "We bring the shop."
3. Willowmere Animal Clinic. A vet clinic in a farm town. For pet owners and farmers. Words: calm, caring, steady. Must work: stitched on scrubs in one thread color. Tagline: "Every paw, hoof and feather."
4. Kitefish Swim School. Swim lessons for kids 3 to 12. For parents and kids. Words: playful, safe, bright. Must work: small, as a circle avatar for the school's posts. Tagline: "Brave in the water."
5. Ember Wall Climbing Gym. An indoor climbing gym. For teens and adults, beginners welcome. Words: bold, strong, welcoming. Must work: printed light on dark shirts. Tagline: "Find your next hold."
6. Quiet Hours Bookshop. A used bookshop with reading chairs. For readers of every age. Words: thoughtful, classic, warm. Must work: in the town's black-and-white newspaper. Tagline: "Stay a chapter."
Each brief's constraint names its surface; that surface's tile is outlined in the accent on the Test wall.

**Symbols** (24, drawn in code on a 100 x 100 grid, each in a filled and a line version): moon, sun, star, leaf, sprout, wheat, wave, drop, mountain, flame, bolt, heart, paw, fish, bird, feather, gear, wheel, book, cup, key, house, kite, three stacked hexagons.

**Typefaces** (all SIL Open Font License 1.1 from Google Fonts, latin subset, bundled as woff2 inside the file; class and convention note shown in the picker):
1. Instrument Sans (Regular, Bold): sans serif. "Plain and modern; gets out of the way."
2. Montserrat (Regular, Bold): geometric sans. "Built from circles and straight lines; clean and confident."
3. Quicksand (Regular, Bold): rounded sans. "Soft ends feel friendly; thin weights fade when small."
4. Fraunces (Regular, Bold): old-style serif. "Bookish and warm."
5. Playfair Display (Regular, Bold): high-contrast serif. "Elegant; its thin strokes vanish at small sizes."
6. Arvo (Regular, Bold): slab serif. "Sturdy and mechanical, like a typewriter or a poster."
7. Bebas Neue (one weight): condensed display, capitals only. "Loud and tall; fits narrow signs."
8. Pacifico (one weight): script. "Personal and handmade; hard to read small or in capitals."
Fraunces and Instrument Sans are the files the site already ships (`site/assets/fonts/`); the other six come from Google Fonts. Their notes are design conventions, not rules, and say so ("Convention, not a rule").

**Palette** (24 swatches): 8 hues (red, orange, gold, green, teal, blue, violet, pink) in light, mid and deep steps; plus black #111111 and white in the Ink choice. Exact hex values are the builder's, checked so each mid step is at least 3:1 on white.

**Surfaces and tests** (thresholds marked "tool's own" are this tool's choices, not standards):
1. Browser tab: the mark at 16 x 16 px beside the name in a tab. Test "Small size": render the mark at 256 px and at 16 px; scale the 16 px back up and compare the shapes (overlap divided by union of the two masks). Holds up at 80% or more (tool's own). Shown as the 16 px pixels enlarged next to the original.
2. Phone home screen: mark only, 60 px rounded square (the app icon). Test "Fills the icon": the mark covers 30% to 80% of the square (tool's own).
3. Circle avatar: 110 px circle crop. Test "Circle crop": no part of the lockup falls outside a circle 92% of the avatar's width (tool's own safe margin).
4. Storefront sign (photo): side-by-side lockup on the sign band. Test "Name reads": ink on the sign color 4.5:1 or more for the name and tagline (WCAG text contrast; 3:1 if the name is 24 px or larger in the photo's scale).
5. Delivery van (photo): stacked lockup, full color. Test "Mark shows": primary and secondary each 3:1 or more against the van white, or the mark has a container (WCAG non-text contrast).
6. Dark shirt (photo): one-color light print (white or the palette's lightest step). Test "One color": draw the mark in one color and count separate shapes; if two shapes that were told apart only by color now merge, it breaks and the merged part is outlined.
7. Paper bag (photo): one-color dark stamp. Same "One color" test, dark on kraft, plus ink on kraft 4.5:1.
8. Newspaper ad (drawn in code, halftone gray): grayscale. Test "Gray print": primary and secondary must differ by a contrast ratio of 1.5:1 or more once turned to gray (tool's own), else "These two colors print as the same gray."
Extra notes (not pass or fail): a script face in UPPERCASE adds "Script letters are made to join; in capitals they get hard to read." Name cap height under 6 px on any surface adds "The name is too small to read here; use Mark only."

**Critique swap prompts:** "What do you notice first?" / "Pick one word for this business. Is it one of the brief's three?" / "Which surface breaks it worst?" / "Name one change you'd try first."

## Interactions in detail
- All rendering is SVG; tests rasterize to an offscreen canvas. Tests rerun when Test opens and after any change while it is open (debounced 150 ms).
- Contrast uses the WCAG 2.1 relative luminance formula; ratios show to one decimal.
- The one-color test: count connected regions of the mark's mask in full color (each color its own mask) and in one color; fewer regions in one color means a merge. Gaps under 1 px at the surface's print size count as merged.
- Minimum size on the sheet: the smallest width, in 8 px steps from 16 px up, at which the small-size test passes.
- Clear space: a margin equal to 25% of the mark's height on every side (tool's own convention, labeled as such).
- Text fields (own business name and words, brief fit notes) stay on this device: saved with the brand in localStorage `brand-builder-brands` (try/catch); `Clear all brands` in Brief empties it after a confirm. No names of people are asked for.
- Sizes: artboard and the open panel section visible without scrolling at every STANDARDS.md size; Test is a 4 x 2 grid at 1366x768, 2 x 4 at 760 wide, one column at 375 wide; in the 680x425 preview the Test wall shows four tiles with arrows.

## Look
- Accent (`--brand`) #047857 studio green; light theme: paper #f7f7f4, panel #ffffff, ink #18181b, muted #57575f, line #e2e2dc; break marks #b42318 with a cross icon; artboard white with an 8-unit grid at 6% black.
- Contrast: accent on paper 5.11:1; white on accent 5.48:1; ink on paper 16.51:1; muted on panel 7.16:1; break red on panel 6.57:1.
- A clean, quiet design-studio look so the student's colors carry the page. Differs from the group's dark film room, pencil-and-paper flipbook, festival night and camp blue, and from virtual-gallery lime, gallery-critique pink and city-skyline cyan.

## Art
Cloudflare FLUX.2 (`scripts/cfart.py`), no people, no lettering, front-on, flat even daylight, webp, long side 1200 px. After generation the builder records each image's logo zone as a rectangle in percent of the image.
- bb-storefront: a small brick shop front seen straight on, a wide blank painted sign band above the window, a plain wooden door, empty sidewalk; 16:9; cutout no; people no; the sign band is the logo zone.
- bb-van: a plain white delivery van in side view on a quiet street, large blank side panel, clean paint; 16:9; cutout no; people no; the side panel is the logo zone.
- bb-shirt: a plain charcoal t-shirt laid flat on a light wood table, seen from above, blank front; 1:1; cutout no; people no; the chest area is the logo zone.
- bb-bag: a plain brown kraft paper shopping bag standing on a counter, seen straight on, blank front; 3:4; cutout no; people no; the bag front is the logo zone.

## Voice
Bank voice: `hs-narrator` (Kore), "Read clearly and naturally, at a moderate pace", here a design studio lead. Changed at the wave check from knowing-guide, which dance-styles-explorer (9-12 arts) also uses; no other arts or media tool in this wave uses hs-narrator (capture-the-flag, 9-12 CS, does). Style: clear, friendly, brief.
- welcomeBrief (how): "Pick a client. Read their three words, then tap Start this brand."
- welcomeDesign (how): "Choose a symbol and a typeface. Then tap Test to see it in the world."
- welcomeTest (how): "Every tile is a real place your brand will live. Tap a tile marked Breaks to see why."
- briefTile (how, first Test visit): "The outlined tile is the one this client cares about most."
- broke (event, when a test newly breaks after a change; stale after the next change): "That change broke the (surface) test. Tap the tile to see why."
- allHold (event, when all eight tests hold): "All eight surfaces hold up. Now check the brief: does it say all three words?"
- welcomeSheet (how): "This is your brand sheet. Print it, then swap laptops for a critique."

## Family engine
none

## Sources
- NCAS Media Arts MA:Cr2.1, MA:Cr3.1 and Visual Arts VA:Cr3.1, high school proficient: https://www.nationalartsstandards.org/
- Contrast ratio formula, 4.5:1 text, 3:1 large text (24 px, or about 18.7 px bold) and 3:1 non-text contrast: W3C, Web Content Accessibility Guidelines (WCAG) 2.1, Success Criteria 1.4.3 and 1.4.11, https://www.w3.org/TR/WCAG21/
- Browser tab icons at 16 x 16 px: MDN Web Docs, "link rel=icon" (sizes), https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#icon
- Type classes (old-style, high-contrast, slab, geometric, script) and the conventions in the picker notes; script in capitals: Ellen Lupton, Thinking with Type, 2nd ed. (Princeton Architectural Press, 2010), "Letter" chapter.
- Logo systems, clear space, minimum size and one-color versions as practice: Alina Wheeler, Designing Brand Identity, 5th ed. (Wiley, 2017), "Process" and "Touchpoints" sections.
- Fonts: SIL Open Font License 1.1, each family's OFL.txt from https://github.com/google/fonts (ofl/instrumentsans, ofl/montserrat, ofl/quicksand, ofl/fraunces, ofl/playfairdisplay, ofl/arvo, ofl/bebasneue, ofl/pacifico); list in tool.json third_party.
- Businesses, taglines, symbols and palette: made up for this tool.

## Done when
1. Every symbol, container, typeface, case, lockup and color control changes the artboard, undo and redo walk back through it, and fonts load from inside the file with no network request.
2. Contrast readouts match the WCAG formula for five color pairs (recompute in Python).
3. Each of the eight tests has one passing and one breaking setup that the verify agent builds and checks (for example: a Line symbol at Thin weight breaks Small size; a two-color heart with touching halves breaks One color).
4. The brief's own surface is outlined; Fix in Design opens the right control for each test.
5. The sheet shows minimum size and clear space consistent with the tests; Print sheet is black-on-white friendly.
6. Each brief keeps its own brand across a reload; Clear all brands empties storage; own-business text never leaves the page.
7. No business name, symbol or typeface is a real brand or a font needing a paid license (check each name with a search before build; rename any match).
8. Artboard, active controls and the Test wall are visible without scrolling at every STANDARDS.md size.
9. How lines once in five design changes in a row; broke spoken each time a test newly breaks, dropped when stale.
