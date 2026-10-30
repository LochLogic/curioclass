# Art Style Match

## One idea
A style is a recipe of things you can see: play the "tell" cards a painting shows (dots, swirls, gold, flat color) until they point to one style, then deal the same tells onto your own picture and watch it turn into that style.

## Not like
- art-passport (K-2, explorer, same family): travels the world to look and talk about objects. Here every work is a painting card in a game, and the point is naming what you see as a style recipe.
- art-through-time (6-8, timeline, same family and group): why art changed over time, with threads to inventions and history. Here time does not matter; only the visible tells do. No work appears in both.
- paint-mixer (3-5, lab): mixing color. Make mode here repaints a picture with brushwork effects, never mixes paint.
- near-and-far (3-5, puzzle, same group): depth cues in a landscape. Nothing here moves in space.
- melody-maker, song-form-builder (3-5 music): no sound play here beyond chimes.

## Who and how
- Grade 3-5, visual arts, module "Famous Artists and Movements (Visual Arts)".
- Topic line: art styles and the artists who made them
- Driver: students or teacher (pairs on laptops, or the teacher on a projector with the class calling out tells). 15 to 30 minutes.
- Standards: NCAS VA:Re7 (perceive and analyze artistic work), VA:Cn11 (relate artistic ideas and works with societal, cultural and historical context).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound`. Modes (`.seg`): `Look` (explore, the default), `Match` (the card game), `Make` (Style Brush), `Album`.

**Look.** Focus: the opened painting, the biggest thing on the stage. The stage is a card table (painted teal felt, Art). Eighteen painting cards lie in a grid of six columns (one per style, unlabeled at first, order shuffled each load). Tap a card: it flips up big in the art-museum frame (Family engine), filling most of the stage, with its wall label beside it (title, artist, date, what it is made of, the museum). A `Tells` button shows small round pins on the painting, one per tell it has, each with the tell's icon; tapping a pin zooms to that spot (engine zoom) and shows the tell's name and one line ("Tiny dots of color, side by side."). `Whole picture` zooms out. `Next` and `Previous` step through cards; Escape closes. The style name is shown only after the card has been matched in Match or after the student taps `Show style` (so Look stays a fair warm-up).

**Match.** Focus: the painting card in the middle of the table, the largest thing (at least 45% of the stage height at 1366x768). The student's hand of four tell cards runs along the bottom; the six style cards in a row along the top, face down until they light; the draw pile and `Trade` at the right.
- `Deal` starts a round with an unmatched painting (Album order shuffled). The hand is dealt from the deck of ten tells, always holding at least one tell this painting shows (so a grade 3 player is never stuck).
- Play a tell: tap a tell card, then tap the painting (or drag it on). If the painting shows it, the card sticks to the side of the frame and its pin lights on the spot. If not, the card slides back with "No dots here. Look again." (the tell's own name), and no penalty. Then the hand refills from the pile.
- `Trade`: put one tell back under the pile and draw the next. No limit.
- When the played tells fit only one style's recipe, the style cards flip up and the student taps the style. When they still fit two (Bold outlines alone fits Japanese prints and Van Gogh; Flat color alone fits Persian painting and Japanese prints; Outdoor light alone fits Impressionism and Pointillism), the line says "Bold outlines fit two styles. Find one more tell."
- Wrong style card: "Not this one. Check the recipe on the back." The back of each style card lists its recipe with icons.
- Then three artist cards appear (the right artist plus two from other styles): tap one. Right: the painting goes to the Album with a short card line (Content "Card lines"); `Deal` for the next.
- No score, no timer. A round can be skipped with `New painting`.

**Make (Style Brush).** Focus: the student's picture, centered and the biggest thing on the stage. Stage: one of four painted scenes (`Willow by a pond`, `Cat on a windowsill`, `Bowl of fruit`, `Lighthouse by the sea`; scene buttons above the picture), each a painted background with the subject as a separate cutout (Art), repainted live by the effects below. Panel: the ten tell toggles (the same cards as the game, as toggle buttons with icons) and the six style buttons. A style button turns on exactly its recipe. Any mix of tells can be on; the label under the picture names the matching style when the mix is exactly one recipe ("Pointillism recipe") or says "Your own style" when it is not. Buttons: `Save picture` (PNG download, 1600 px wide), `Side by side` (shows the matched painting from Look next to the picture, only for a style matched in the Album), `Reset` (all tells off).

**Album.** Focus: the grid of slots. Eighteen slots in six rows, one per style, with the style name, its recipe icons and the year range. Matched paintings show; empty slots show a dashed outline. Tapping a matched painting opens it in Look. `Clear album` (with a confirm) empties it. Saved on this device only (localStorage `art-style-match-album`).

## Content
**Tells** (id, card name, icon, the one line):
- gold, Gold, a gold leaf: "Real gold you can see shining in the picture."
- tiny, Tiny details, a magnifier: "Small patterns everywhere: on tiles, plants and clothes."
- flat, Flat color, a filled square: "Areas of one color with no shading."
- outline, Bold outlines, a drawn circle: "Dark lines around the shapes."
- smooth, Smooth blending, a soft gradient: "You can't see any brushstrokes."
- shadow, Light and shadow, a half-lit ball: "Strong light from one side and deep dark shadows."
- dabs, Quick dabs, three short strokes: "Short, loose brushstrokes you can see."
- outdoor, Outdoor light, a sun: "Sunlight, sky and bright colors outside."
- dots, Dots, a cluster of dots: "Tiny dots of color, side by side."
- thick, Thick wavy paint, a wave: "Thick paint laid on in curving strokes."

**Styles** (name, years shown, recipe, back-of-card line):
- Persian book painting, 1500s, gold + tiny + flat: "Painted for handmade books of poems and stories in Iran."
- Dutch Golden Age, 1600s, smooth + shadow: "Painted in the Netherlands to look almost real."
- Japanese woodblock prints, 1700s to 1800s, flat + outline: "Carved on wood blocks and printed in many copies in Japan."
- Impressionism, 1870s to 1900s, dabs + outdoor: "Painted quickly to catch light and moments, often outside."
- Pointillism, 1880s to 1890s, dots + outdoor: "Painted with tiny dots that mix in your eye."
- Post-Impressionism: Vincent van Gogh, late 1880s, thick + outline: "Thick paint and strong lines to show feeling."
The recipes are chosen so two tells always point to one style, and one shared tell does not (Interactions).

**Paintings** (id, title on the card, artist, date, made of, museum and id, tells it shows; every tell listed is in its style's recipe):
Persian book painting
- sada: The Feast of Sada (Shahnama of Shah Tahmasp, folio 22v), attributed to Sultan Muhammad, about 1525, opaque watercolor, ink, silver and gold on paper, The Met 452111. gold, tiny, flat.
- khosrow: Kay Khosrow Crosses the Sea of Zareh, artist unknown (Iran), about 1550, watercolor and ink on paper, Art Institute of Chicago 93923. tiny, flat.
- zal: Zal Climbing to Rudaba, artist unknown (Shiraz, Iran), 1580 to 1590, opaque watercolor and gold on paper, Art Institute of Chicago 120662. gold, tiny, flat.
Dutch Golden Age
- pitcher: Young Woman with a Water Pitcher, Johannes Vermeer, about 1662, oil on canvas, The Met 437881. smooth, shadow.
- oysters: Still Life with Oysters, a Silver Tazza, and Glassware, Willem Claesz Heda, 1635, oil on wood, The Met 438376. smooth, shadow.
- margaretha: Margaretha van Haexbergen, Gerard ter Borch the Younger, about 1666 to 1667, oil on canvas, The Met 459084. smooth, shadow.
Japanese woodblock prints
- redfuji: South Wind, Clear Sky (Red Fuji), Katsushika Hokusai, about 1830 to 1832, woodblock print, The Met 36490. flat, outline.
- shower: Sudden Shower over Shin-Ohashi Bridge and Atake, Utagawa Hiroshige, 1857, woodblock print, The Met 55433. flat, outline.
- mimeguri: Sudden Shower at Mimeguri Shrine (left sheet of three), Torii Kiyonaga, about 1787, woodblock print, Art Institute of Chicago 22719. flat, outline.
Impressionism
- lilies: Water Lilies, Claude Monet, 1906, oil on canvas, Art Institute of Chicago 16568. dabs, outdoor.
- garden: Woman in a Garden, Berthe Morisot, 1882 to 1883, oil on canvas, Art Institute of Chicago 153798. dabs, outdoor.
- havre: The Place du Havre, Paris, Camille Pissarro, 1893, oil on canvas, Art Institute of Chicago 81551. dabs, outdoor.
Pointillism
- jatte: A Sunday on La Grande Jatte, 1884, Georges Seurat, 1884 to 1886, oil on canvas, Art Institute of Chicago 27992. dots, outdoor.
- andelys: Les Andelys, Cote d'Aval, Paul Signac, 1886, oil on canvas, Art Institute of Chicago 122130. dots, outdoor.
- pines: Pines Along the Shore, Henri-Edmond Cross, 1896, oil on canvas, The Met 459095. dots, outdoor.
Post-Impressionism: Vincent van Gogh
- bedroom: The Bedroom, 1889, oil on canvas, Art Institute of Chicago 28560. thick, outline.
- irises: Irises, 1890, oil on canvas, The Met 436528. thick, outline.
- selfie: Self-Portrait, 1887, oil on board, Art Institute of Chicago 80607. thick.
The builder places one spot per tell (x, y as fractions) after fetching each image and checks every tell is plainly visible there; if one is not, drop that tell from the card (each card must keep at least one tell only its style has, or two that together point to one style).

**Artist cards:** Sultan Muhammad; Unknown Persian painters; Johannes Vermeer; Willem Claesz Heda; Gerard ter Borch; Katsushika Hokusai; Utagawa Hiroshige; Torii Kiyonaga; Claude Monet; Berthe Morisot; Camille Pissarro; Georges Seurat; Paul Signac; Henri-Edmond Cross; Vincent van Gogh. Khosrow and zal take "Unknown Persian painters" (the card says "Many book painters did not sign their work.").

**Card lines** (shown when a painting joins the Album; one each, from the museum pages and Sources):
- sada: "Made for a Shah's copy of the Book of Kings, a long poem of Iran's legends."
- khosrow: "A king and his army cross a sea in a story from the Book of Kings."
- zal: "In this story, Zal climbs up a rope to visit Rudaba."
- pitcher: "Vermeer painted the soft light from a window again and again."
- oysters: "Heda painted shiny metal and glass so they look real enough to touch."
- margaretha: "Ter Borch was famous for painting shiny satin and silk."
- redfuji: "Fuji turns red in the early morning light in late summer and autumn."
- shower: "Van Gogh liked this print so much he painted his own copy of it."
- mimeguri: "This is one sheet of three that fit together into one wide picture."
- lilies: "Monet painted the water lilies in his own garden pond many times."
- garden: "Morisot showed her paintings at the very first Impressionist show in 1874."
- havre: "Pissarro painted this busy street from a hotel window."
- jatte: "Seurat worked on this painting for about two years."
- andelys: "Signac painted this river town in France."
- pines: "Cross used dots bigger than Seurat's, like little tiles."
- bedroom: "Van Gogh painted his own bedroom in Arles, France."
- irises: "Van Gogh painted these irises in his last year."
- selfie: "Van Gogh painted many pictures of himself because models cost money."

**Make scenes** (painted, Art; each has a light side, left in all four): willow by a pond (meadow and pond background, willow cutout on the left third); cat on a windowsill (window, evening sky and wall background, cat and pot plant cutout on the sill); bowl of fruit (table and wall background, bowl cutout in the center); lighthouse by the sea (sea and sky background, lighthouse on its rocks cutout on the right third).
**Effect per tell in Make** (canvas filters over the painted layers): at load each scene is split once into 8 color regions (k-means on a 320 px wide copy, kept as a label map). gold = the background layer replaced by the gold-leaf texture behind the cutout; tiny = a patterned border and small repeat patterns (drawn in code) on the largest regions; flat = each region filled with its mean color, no shading; outline = 3 px dark lines (#2a1e22) where regions meet and around the cutout edge; smooth = each region blurred inside its own edges with a soft gradient from the light side; shadow = the background darkened, a strong side light on the subject and a cast shadow made from the cutout's shape; dabs = the picture repainted in short strokes along each region (stroke length about 1% of the width), colors sampled from the painting; outdoor = a warm bright grade with shadows shifted to blue-violet; dots = the picture repainted in dots of pure colors (dot about 0.6% of the width, no blending); thick = curving strokes following a flow field, with a raised paint edge highlight. Order when several are on: background (gold), shading (smooth, shadow, outdoor), flat, brushwork (thick, then dabs, then dots on top), tiny, outline last.

## Interactions in detail
- Recipe rule: a style is pointed to when every played tell is in its recipe and no other style's recipe contains them all. One played tell from gold, tiny, smooth, shadow, dabs, dots or thick points to one style already; flat, outline and outdoor each fit two. Two tells from one recipe always point to one style (checked: no two recipes share two tells).
- A tell already played cannot be played twice. A tell the painting does not show bounces back every time with its own "No (tell) here" line.
- The hand never holds two copies; the pile reshuffles when empty. With Motion off, cards move instantly; pacing is unchanged.
- Nothing waits on an animation: a tap during a card flip, a zoom (0.9 s) or a slide finishes that motion at once and acts on the tap; the old line stops.
- Zoom in Match is allowed at any time (tap the painting with no card selected); the pins appear only for played tells.
- Artist step is skipped for Persian cards with no named artist; it shows "Many book painters did not sign their work." and goes to the Album.
- Make renders on a canvas at the stage's real pixel size and re-renders on resize (debounced 150 ms). Rendering must finish under 300 ms at 1920x1080; dots, dabs and thick use a seeded random so the same settings give the same picture. A toggle tapped during a render cancels it and starts the new one.
- Keyboard: in Match, Tab moves through hand cards, then the painting, then style and artist cards; Enter plays the focused card on the painting.
- Sizes: the table lays out at real pixels; in short landscape boxes the hand shrinks to cards 90 px tall in a row beside the painting. At 375 wide the hand is a scrolling row under the painting and the style cards wrap two rows.

## Look
- Accent (`--brand`) #9b2457 deep magenta. Paper (cards) #fbf6ec, ink #2a1e22, muted #6b5a5e; table felt (painted) about #173f45 deep teal, with any text on it in card cream; style card backs in gold #d7a93b with ink text.
- Contrast: white on brand 7.54:1; brand on card 7.0:1; ink on card 14.91:1; card cream on felt #173f45 10.63:1; muted on card 6.0:1; ink on style-card gold 7.36:1.
- Cards have rounded corners and a slight tilt when held; played cards stack beside the frame. Different from art-passport (cream and blue), near-and-far (meadow green), art-through-time (parchment, oxblood and walnut).

## Art
- Eighteen public-domain paintings (Content), from The Met and the Art Institute of Chicago Open Access, long side 900 px, webp, 45 KB or less each. None is used by any other tool in this group or by art-passport. People in the real paintings are fine (not generated).
- Generated with local FLUX (`scripts/localart.py`), one session, no people. The Make scenes share one plain style so the effects show: "a simple clear realistic painting with smooth even colors and soft daylight from the left".
  - felt: "a full-frame texture of deep teal green card-table felt, soft fabric fibers, even light"; 16:9; cutout no; people no; the table in Look and Match, under every card.
  - gold-leaf: "a full-frame texture of hammered gold leaf with fine tooled dot patterns, warm shine"; 1:1; cutout no; people no; the gold tell's background in Make.
  - pond-bg: "a grassy meadow under a clear blue sky with a calm round pond in the lower middle, soft daylight, simple clear realistic painting with smooth even colors"; 16:10; cutout no; people no; Willow scene background.
  - pond-willow: "one weeping willow tree with long hanging green branches and a brown trunk, simple clear realistic painting with smooth even colors, light from the left, plain white background"; 3:4; cutout yes; people no; Willow scene subject, left third, its foot at the pond's edge.
  - window-bg: "a wooden window frame seen from inside a room at dusk, a deep blue evening sky through the glass, a pale yellow wall and a plain cream curtain on the right, a wide wooden sill along the bottom, simple clear realistic painting with smooth even colors"; 16:10; cutout no; people no; Cat scene background.
  - window-cat: "a ginger cat sitting upright beside a small terracotta pot with a green leafy plant, side view, simple clear realistic painting with smooth even colors, light from the left, plain white background"; 4:3; cutout yes; people no; sits on the sill.
  - fruit-bg: "a plain wooden table top in front of a plain warm grey wall, soft daylight from the left, simple clear realistic painting with smooth even colors"; 16:10; cutout no; people no; Fruit scene background.
  - fruit-bowl: "a white ceramic bowl holding an orange, a red apple and a bunch of green grapes, simple clear realistic painting with smooth even colors, light from the left, plain white background"; 4:3; cutout yes; people no; center of the table.
  - sea-bg: "open sea with gentle blue waves under a sunny sky with a few soft white clouds, simple clear realistic painting with smooth even colors"; 16:10; cutout no; people no; Lighthouse scene background.
  - sea-lighthouse: "a white and red striped lighthouse standing on a small point of grey rocks, simple clear realistic painting with smooth even colors, light from the left, plain white background"; 3:4; cutout yes; people no; right third, its rocks at the waterline.
- 10 generated images, none with people. Drawn in code: tell icons, card frames and backs, style card recipe icons, pins, the tiny-tell patterns and every label (controls and symbols).
- The whole bundled file stays under 2 MB (paintings about 1.1 MB after base64, generated images webp at 60 KB or less each).

## Voice
Bank voice: `lively-host` (a game show host at a card table; different from art-passport's knowing-guide and every other tool in this group). Style: bright, quick, friendly; never loud about wrong answers. `Curio.voice` with `scope: () => state.mode`.
- welcomeLook (how; on entering Look; stale when a card is opened): "Tap a painting to see it big. Then tap Tells to find its clues."
- welcomeMatch (how; on entering Match before the first Deal; stale when Deal is tapped): "Tap Deal to get a painting and four tell cards."
- playHow (how; after the first Deal; stale when a card is played): "Tap a tell card you can see in the painting. Then tap the painting."
- miss (event; each bounce; stale on the next card play): "No (tell) here. Look again." (one recorded line per tell, e.g. "No dots here. Look again.")
- twoStyles (event; stale when another tell is played): "(Tell) fits two styles. Tap one more tell card that you can see." (one line each for Flat color, Bold outlines and Outdoor light)
- pickStyle (how; when the style cards first light; stale when a style card is tapped): "Tap the style card that matches your tells."
- wrongStyle (event; stale on the next tap): "Not this one. Check the recipe on the back."
- pickArtist (how; when the artist cards first appear; stale when one is tapped): "Now tap the artist who made it."
- won (event; every match; stale when Deal is tapped): "Into the album!" followed by that painting's card line.
- welcomeMake (how; on entering Make; stale when a toggle or style button is tapped): "Tap a style button, or tap the tell cards on and off, and watch your picture change."
- ownStyle (how; the first time a mix fits no recipe; stale on the next toggle): "That mix is your own style."
- welcomeAlbum (how; on entering Album with at least one painting; stale when a painting is tapped): "Here is every painting you've matched. Tap one to look again."
- albumEmpty (how; on entering Album with none; stale when the mode changes): "Your album is empty. Tap Match, then Deal, to win paintings."
- albumFull (event; when the eighteenth painting joins; stale when Deal or a mode is tapped): "All eighteen! You know six styles by their tells."
- Read speaks the hint, or in Look the open card's wall label.

## Family engine
art-museum. This spec holds the full engine description (art-passport, K-2, was built before it and moves onto it when next touched; art-through-time and gallery-critique feed it).
- `kit/art-museum.js` with a work record: `{id, img, title, artist, date, year, made, museum, museumId, url, kind: 'flat'|'object', alt, spots: [{x, y, key, label}]}` (x, y as fractions of the image).
- `frame(el, work)`: the framed view (gilt frame for flat works, rounded white mount for objects, both drawn in CSS), fitted to its box at real pixels.
- `zoomTo(frame, spot)` and `unzoom(frame)`: the art-passport zoom (2.4 times, clamped so the picture fills the frame, a dimmed ring around the spot, 0.9 s ease; instant with Motion off), Escape unzooms; a new call during a zoom starts from where the old one is.
- `pins(frame, spots, opts)`: tap targets at least 44 px on spots, with an icon or number, keyboard reachable in reading order.
- `label(el, work)`: the museum wall label (title in italics, artist, date, made of, museum with a link to the object page).
- `pair(el, workA, workB)`: two frames side by side (stacked under 760 px).
- Images: webp, long side 900 px, 45 KB or less each, `art:` references, credits in the top comment.
This tool feeds it: 18 works with one spot per tell.

## Sources
- NCAS Visual Arts VA:Re7, VA:Cn11: https://www.nationalartsstandards.org/
- Object pages for every painting (title, artist, date, medium, public domain): https://www.metmuseum.org/art/collection/search/452111 , /437881 , /438376 , /459084 , /36490 , /55433 , /459095 , /436528 ; https://www.artic.edu/artworks/93923 , /120662 , /22719 , /16568 , /153798 , /81551 , /27992 , /122130 , /28560 , /80607
- Van Gogh copied Hiroshige's Sudden Shower and collected Japanese prints: Van Gogh Museum, "Van Gogh and Japan", https://www.vangoghmuseum.nl/en/art-and-stories/stories/van-gogh-and-japan ; and The Met, Heilbrunn Timeline of Art History, "Japonisme", https://www.metmuseum.org/toah/hd/jpon/hd_jpon.htm
- Morisot in the first Impressionist exhibition, 1874: The Met, Heilbrunn Timeline, "Impressionism: Art and Modernity", https://www.metmuseum.org/toah/hd/imml/hd_imml.htm
- Pointillism, dots that mix in the eye, Seurat's two years on La Grande Jatte: Art Institute of Chicago object page 27992.
- Red Fuji in early autumn morning light: The Met object page 36490.
- Pissarro painting from a hotel window: Art Institute of Chicago object page 81551 (builder confirms on the page; if not stated, use "Pissarro painted many views of busy Paris streets.").
- Ter Borch's satin: The Met object page 459084 or Heilbrunn Timeline "Gerard ter Borch"; builder confirms, else use "Ter Borch painted fine clothes in careful detail."
- Van Gogh self-portraits because models cost money: Van Gogh Museum, "Self-portraits", https://www.vangoghmuseum.nl/en/art-and-stories/stories ; builder confirms the page.
- The Book of Kings (Shahnama) and Shah Tahmasp's copy: The Met object page 452111.
- Met essay URLs answered 429 (rate limit) on 2026-10-27; the builder opens each once.
- Make scenes, effects and generated images: this tool's own.
- Checks run (Python, 2026-10-29): recipe rule over the six recipes: gold, tiny, smooth, shadow, dabs, dots and thick each fit one style; flat (Persian, Japanese), outline (Japanese, Van Gogh) and outdoor (Impressionism, Pointillism) each fit two, as the twoStyles lines say; no two recipes share two tells; every pair of tells from one recipe points to one style. All 18 paintings: every listed tell is in its style's recipe, and the full set points to its own style only (selfie with thick alone included). Make labels: of all 1,024 on/off mixes of the ten tells, exactly 6 name a style (the six recipes); every other mix reads "Your own style". Contrast ratios in Look recomputed with the WCAG 2.1 formula (values as stated; the felt changed from wine to teal so it no longer echoes art-through-time's oxblood). No score or tolerance to check.

## Done when
1. All 18 cards open in Look with a correct wall label and working tell pins; each pin's spot visibly shows its tell.
2. In Match on bedroom or irises, playing Bold outlines alone gives the "fits two styles" line; adding Thick wavy paint lights the style cards.
3. Every painting can be matched from a fresh deal without a dead end (the hand always holds one useful tell; Trade works).
4. The Album fills, survives a reload, and `Clear album` empties it; an empty Album says the albumEmpty line, never welcomeAlbum.
5. Make: each style button turns on exactly its recipe and the label names it; an off-recipe mix says "Your own style"; render under 300 ms at 1920x1080; `Save picture` downloads a PNG; all four painted scenes show every effect with the subject's edge intact.
6. Focus: at 1366x768 and 680x425 the open painting (Look), the dealt painting (Match) and the student's picture (Make) are each the largest, central thing on the stage.
7. Tap while it plays: a tap during a card flip, a zoom or a Make render acts at once (the zoom jumps, the render restarts with the new mix) and no stale line plays after.
8. How lines are spoken once in five plays in a row; miss and won are spoken every time and dropped when stale.
9. Hand, painting and Deal are visible without scrolling at every size in STANDARDS.md.
10. The bundled file is under 2 MB.
