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

**Look.** The stage is a card table (deep wine felt). Eighteen painting cards lie in a grid of six columns (one per style, unlabeled at first, order shuffled each load). Tap a card: it flips up big in the art-museum frame (Family engine) with its wall label (title, artist, date, what it is made of, the museum). Beside it, a `Tells` button shows small round pins on the painting, one per tell it has, each with the tell's icon; tapping a pin zooms to that spot (engine zoom) and shows the tell's name and one line ("Tiny dots of color, side by side."). `Whole picture` zooms out. `Next` and `Previous` step through cards; Escape closes. The style name is shown only after the card has been matched in Match or after the student taps `Show style` (so Look stays a fair warm-up).

**Match.** The card game. Layout: the painting card in the middle of the table (framed, zoomable); the student's hand of four tell cards along the bottom; the six style cards in a row along the top, face down until they light; the draw pile and `Trade` at the right.
- `Deal` starts a round with an unmatched painting (Album order shuffled). The hand is dealt from the deck of ten tells, always holding at least one tell this painting shows (so a grade 3 player is never stuck).
- Play a tell: tap a tell card, then tap the painting (or drag it on). If the painting shows it, the card sticks to the side of the frame and its pin lights on the spot. If not, the card slides back with "No dots here. Look again." (the tell's own name), and no penalty. Then the hand refills from the pile.
- `Trade`: put one tell back under the pile and draw the next. No limit.
- When the played tells fit only one style's recipe, the style cards flip up and the student taps the style. When they still fit two (Bold outlines alone fits Japanese prints and Van Gogh; Flat color alone fits Persian painting and Japanese prints; Outdoor light alone fits Impressionism and Pointillism), the line says "Bold outlines fit two styles. Find one more tell."
- Wrong style card: "Not this one. Check the recipe on the back." The back of each style card lists its recipe with icons.
- Then three artist cards appear (the right artist plus two from other styles): tap one. Right: the painting goes to the Album with a short card line (Content "Card lines"); `Deal` for the next.
- No score, no timer. A round can be skipped with `New painting`.

**Make (Style Brush).** Stage: the student's picture, drawn in code from one of four scenes (`Tree by a pond`, `Cat on a windowsill`, `Bowl of fruit`, `Boat at sea`). Panel: the ten tell toggles (the same cards as the game, as toggle buttons with icons) and the six style buttons. A style button turns on exactly its recipe. Any mix of tells can be on; the label under the picture names the matching style ("Pointillism recipe") or says "Your own style" when the mix fits none. Buttons: `Save picture` (PNG download, 1600 px wide), `Side by side` (shows the matched painting from Look next to the picture, only for a style matched in the Album), `Reset` (all tells off).

**Album.** Eighteen slots in six rows, one per style, with the style name, its recipe icons and the year range. Matched paintings show; empty slots show a dashed outline. Tapping a matched painting opens it in Look. `Clear album` (with a confirm) empties it. Saved on this device only (localStorage `art-style-match-album`).

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

**Make scenes** (vector shapes in code, each with a light direction and sky): tree by a pond (tree, pond, grass, sky, sun); cat on a windowsill (cat, window frame, curtain, pot plant, night or day sky); bowl of fruit (bowl, three fruits, table, wall); boat at sea (boat, sail, waves, sky, sun).
**Effect per tell in Make:** gold = gold-leaf background with a fine tooled texture; tiny = a patterned border and small repeat patterns on large flat areas; flat = shapes filled with one color, no shading; outline = 3 px dark outlines on every shape; smooth = soft gradient shading from the light side; shadow = background darkened, a strong side light and cast shadows; dabs = the picture repainted in short strokes along each shape (stroke length about 1% of the width); outdoor = warm bright palette and blue-violet shadows; dots = the picture repainted in dots of pure colors (dot about 0.6% of the width, no blending); thick = curving strokes following a flow field, with a raised paint edge highlight.

## Interactions in detail
- Recipe rule: a style is pointed to when every played tell is in its recipe and no other style's recipe contains them all. One played tell from gold, tiny, smooth, shadow, dabs, dots or thick points to one style already; flat, outline and outdoor each fit two. Two tells from one recipe always point to one style (checked: no two recipes share two tells).
- A tell already played cannot be played twice. A tell the painting does not show bounces back every time with its own "No (tell) here" line.
- The hand never holds two copies; the pile reshuffles when empty. With Motion off, cards move instantly; pacing is unchanged.
- Zoom in Match is allowed at any time (tap the painting with no card selected); the pins appear only for played tells.
- Artist step is skipped for Persian cards with no named artist; it shows "Many book painters did not sign their work." and goes to the Album.
- Make renders on a canvas at the stage's real pixel size and re-renders on resize (debounced 150 ms). Rendering must finish under 300 ms at 1920x1080; dots and thick use a seeded random so the same settings give the same picture.
- Keyboard: in Match, Tab moves through hand cards, then the painting, then style and artist cards; Enter plays the focused card on the painting.
- Sizes: the table lays out at real pixels; in short landscape boxes the hand shrinks to cards 90 px tall in a row beside the painting. At 375 wide the hand is a scrolling row under the painting and the style cards wrap two rows.

## Look
- Accent (`--brand`) #9b2457 deep magenta. Paper (cards) #fbf6ec, ink #2a1e22, muted #6b5a5e; table felt #4a1a2b; style card backs in gold #d7a93b with ink text.
- Contrast: white on brand 7.5:1; brand on card 7.0:1; ink on card 14.9:1; card cream on felt 13.2:1; muted on card 6.0:1.
- Cards have rounded corners and a slight tilt when held; played cards stack beside the frame. Different from art-passport (cream and blue), near-and-far (meadow green), art-through-time (parchment and oxblood).

## Art
- Eighteen public-domain paintings (Content), from The Met and the Art Institute of Chicago Open Access, long side 900 px, webp, 45 KB or less each (about 1.1 MB in the file after base64; the whole file must stay under 2 MB). None is used by any other tool in this group or by art-passport.
- Tell icons, card backs and the felt: drawn in code (SVG).
- No generated images. People: none generated (people in the real paintings are fine).

## Voice
Bank voice: `lively-host` (a game show host at a card table; different from art-passport's knowing-guide and every other tool in this group). Style: bright, quick, friendly; never loud about wrong answers.
- welcomeLook (how): "Tap a painting to see it big. Then tap Tells to find its clues."
- welcomeMatch (how): "Tap Deal to get a painting and four tell cards."
- playHow (how, after Deal): "Tap a tell card you can see in the painting. Then tap the painting."
- miss (event, stale on the next card play): "No (tell) here. Look again." (one line per tell, e.g. "No dots here. Look again.")
- twoStyles (event, stale when another tell is played): "(Tell) fits two styles. Find one more tell."
- pickStyle (how): "Tap the style card that matches your tells."
- wrongStyle (event, stale on the next tap): "Not this one. Check the recipe on the back."
- pickArtist (how): "Now tap the artist who made it."
- won (event): "Into the album!" followed by that painting's card line.
- welcomeMake (how): "Tap a style, or turn tells on and off, and watch your picture change."
- ownStyle (event, the first time a mix fits no style in a session): "That mix is your own style."
- welcomeAlbum (how): "Here is every painting you've matched. Tap one to look again."
- albumFull (event): "All eighteen! You know six styles by their tells."

## Family engine
art-museum. This spec holds the full engine description (art-passport, K-2, was built before it and moves onto it when next touched; art-through-time and gallery-critique feed it).
- `kit/art-museum.js` with a work record: `{id, img, title, artist, date, year, made, museum, museumId, url, kind: 'flat'|'object', alt, spots: [{x, y, key, label}]}` (x, y as fractions of the image).
- `frame(el, work)`: the framed view (gilt frame for flat works, rounded white mount for objects, both drawn in CSS), fitted to its box at real pixels.
- `zoomTo(frame, spot)` and `unzoom(frame)`: the art-passport zoom (2.4 times, clamped so the picture fills the frame, a dimmed ring around the spot, 0.9 s ease; instant with Motion off), Escape unzooms.
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

## Done when
1. All 18 cards open in Look with a correct wall label and working tell pins; each pin's spot visibly shows its tell.
2. In Match, playing Bold outlines alone gives the "fits two styles" line; adding Thick wavy paint lights the style cards.
3. Every painting can be matched from a fresh deal without a dead end (the hand always holds one useful tell; Trade works).
4. The Album fills, survives a reload, and `Clear album` empties it.
5. Make: each style button turns on exactly its recipe and the label names it; an off-recipe mix says "Your own style"; render under 300 ms at 1920x1080; `Save picture` downloads a PNG.
6. How lines are spoken once in five plays in a row; miss and won are spoken every time and dropped when stale.
7. Hand, painting and Deal are visible without scrolling at every size in STANDARDS.md.
8. The bundled file is under 2 MB.
