# Traveling Art Show

## One idea
Every material has its own enemies (sun, heat, busy hands, bumps), and the library hides them in plain sight: place six works so none meets its enemy, open the show, and a one-month fast-forward shows exactly what each spot did to each work, so "glass stops hands, not sunlight" is something you watch happen.

## Not like
- virtual-gallery (9-12, builder): orders a portfolio and sends a visitor walking through for flow and labels. Here the order does not matter; what matters is what the room does to each material over a month.
- near-and-far (3-5, puzzle): moves cut-outs to fix depth cues in a picture. Here the pictures never change shape on purpose; the room changes them.
- art-style-match (3-5, cards): reads a painting's style. Here works are read only for the show's theme and their material.
- paint-mixer (3-5, lab): mixes pigment. Here pigment only matters for how fast it fades.
- hallway-art-museum (K-2, A1's band): what a museum is and who works there. Here the class is the curator and conservator of a real, risky venue.

## Who and how
- Grade 3-5, visual arts, module "Caring for and Exhibiting Art (Visual Arts)".
- Topic line: getting art ready for a show
- Driver: students (solo or pairs on laptops) or teacher (projector, class votes on each spot). 15 to 30 minutes.
- Standards: VA:Pr4 (choose works against criteria; materials limit where a work can go), VA:Pr5 (protect, place and label for this venue), VA:Pr6 (library and museum compared), VA:Re9 (one set of criteria across several works).

## Screens and modes
Header: title, topic line, `Read`, `Motion`, `Sound` (kit). Mode buttons (`.seg`): `Look around` (default), `Shows`, `Library and museum`.

**Look around (explore).** Focus: the painted library wall, the biggest thing on the stage, 16:9, with ten numbered spot markers (Content "Spots"). Under it a month strip: `October`, `January`, `June` (segmented). Panel: the crate of eight works as cards (picture, title, material).
- Tap a spot: a 4 second "one day in the library" loop plays on that spot only: the sun patch slides across the wall (code, a soft yellow polygon), heat shimmer rises from the vent (code wavy lines), little hand icons tap the low wall, a cart bumps the door shelf. A card names what that spot meets this month ("S1 Window wall in October: about 4 hours of direct sun a day."). Changing the month changes the loop at once.
- Tap a work card: its "What it fears" card opens: the four enemy icons (sun, heat, hands, bumps), each marked "hurts it" or "fine", with one line why (Content "Works").
- Drag (or tap the card, then tap a spot) to try a work in a spot: a mini 30-day preview plays on it right there (2 s) and the result shows (faded, curled, smudged, cracked, or "fine"). Nothing is scored here.

**Shows (the puzzle).** Focus: the library wall with the placed works; the step panel beside it. Three shows (Content "Shows"), then `Your show` (any theme with any month). Four steps along the top of the panel, always tappable once reached: `1 Choose`, `2 Place`, `3 Label`, `4 Open the show`.
1. Choose: the brief and the theme checklist (two lines), the crate of eight. Tap a card to flip it to "In the show" (gold ribbon) or back. The checklist line under each card shows a tick or a cross for this theme, revealed only after the student taps `Check my six` (so they read the cards first). Exactly six fit each theme; `Check my six` names any wrong pick and why ("River Stripes has no place in our town.").
2. Place: hazards are hidden until the student taps `Look around this month` (plays all ten spot loops at once, 4 s, then leaves small enemy icons on each spot). Drag a chosen work onto a spot (or tap card, tap spot). A spot holds one work; a flat work goes only on a wall spot, a 3D work only on a shelf, sill, pedestal or the case (the case takes either; Content). After placing, the work's protect chips appear under it: flat works `Glass frame`, `Sleeve`, `Nothing`; 3D works `Clear cover`, `Nothing`. Default `Nothing`.
3. Label: a label card per placed work: title and artist are filled in; the student picks the material from three choices and may type one sentence about the idea (optional, 120 characters). Labels show on the wall as small white cards.
4. Open the show: `Open the show` runs the month (Interactions). Results card per work, then `Fix and run again` (keeps placements, puts every work back as new) and, when all six are fine, `Next show`.
- Buttons in the panel: `Start show over`, `Previous show`, `Next show` (shows are never locked).

**Library and museum.** Focus: two painted rooms side by side (the library wall and a museum gallery), each with a column of facts underneath (Content "Compare"). Tap a row to highlight that row in both columns. No score.

## Content
**Works** (eight, made-up student artists; flat or 3D; enemies; what protection stops hands):
| id | title, artist | material | kind | what is in it (for the themes) | hurt by | hands stopped by |
|---|---|---|---|---|---|---|
| W1 | Pumpkin Patch, by Rosa M. | chalk pastel on colored paper | flat | the farm stand on Mill Road, crows on the fence | sun, hands | glass frame (a sleeve rubs it and smudges it) |
| W2 | Rainy Main Street, by Theo K. | watercolor on paper | flat | Main Street shops in the rain, puddles | sun, heat, hands | glass frame or sleeve |
| W3 | Pond Bowl, by Ana P. | fired, glazed clay | 3D | frogs painted around the town pond | hands, bumps | clear cover |
| W4 | Leaf Parade, by Jamal R. | glued paper collage | flat | the fall parade on Main Street, dogs marching | sun, heat, hands | glass frame |
| W5 | Paper Heron, by Mei L. | folded paper sculpture | 3D | a heron standing in a river | heat, hands, bumps | clear cover |
| W6 | Our Bridge, by Sam O. | printed photo (inkjet) | flat | the old bridge over the river, ducks below | sun, heat, hands | glass frame or sleeve |
| W7 | River Stripes, by Lily A. | yarn weaving | flat | blue and green stripes like moving water | sun, hands | glass frame |
| W8 | Library Cat, by Omar D. | marker poster | flat | the library's cat watching the fish tank | sun, hands | glass frame or sleeve |
Why lines (fears card): sun "Light fades dyes and colored paper. Marker and construction paper fade fastest." heat "Warm, dry air from a vent makes paper curl and wave and glue let go." hands "Fingers smudge chalk, pull yarn, and bend paper." bumps "A knock sends a bowl or a paper sculpture to the floor." fine lines: bowl and sun "Fired clay glaze does not fade in a month." weaving and heat "Yarn does not curl in warm air."

**Spots** (kind; hazards by month; effects icons):
| id | name | kind | October | January | June |
|---|---|---|---|---|---|
| S1 | window wall | wall | sun | sun | sun |
| S2 | window sill | shelf | sun | sun | sun |
| S3 | wall over the heater vent | wall | none (heater off) | heat | none |
| S4 | story rug wall, low | wall | hands | hands | hands |
| S5 | story rug wall, high | wall | none | none | none |
| S6 | shelf by the front door | shelf | bumps | bumps | bumps |
| S7 | locked glass case | case (either) | none | none | none |
| S8 | pedestal in the middle | pedestal | none | sun (low winter sun reaches the middle) | hands (summer reading crowd) |
| S9 | quiet nook wall | wall | none | none | sun (long evening sun through the west window) |
| S10 | wall behind the desk | wall | none | none | none |
Rules: the locked case stops hands and bumps and is out of the sun. Glass frame and sleeve stop hands only; clear cover stops hands only. Nothing stops sun or heat except the spot.

**Shows:**
1. "Our Town", October. Brief: "The town library wants six works about places in our town." Checklist: "Shows a place in our town." "Is finished and signed." Fit: W1, W2, W3, W4, W6, W8. Misfits: W5 ("a heron, but no place in town"), W7 ("stripes, no place").
2. "Water All Around", January. Checklist: "Shows water." "Is finished and signed." Fit: W2, W3, W5, W6, W7, W8 (the cat watches the fish tank). Misfits: W1, W4.
3. "Animals We Know", June. Checklist: "Shows an animal." "Is finished and signed." Fit: W1 (crows), W3 (frogs), W4 (dogs), W5, W6 (ducks), W8. Misfits: W2, W7.
4. `Your show`: pick a theme (the three above) and a month.

**Results lines** (one per work and enemy; shown on the result card, spoken as events): sun "faded: the sun hit it about 4 hours a day."; heat "curled: the heater blew warm, dry air on it all month."; hands "smudged" (W1), "pulled threads" (W7), "bent and fingerprinted" (paper works), "picked up and dropped" (W3: cracked), "crushed" (W5); bumps "knocked off the shelf" (W3 cracked, W5 crushed); sleeve on W1 "smudged inside its sleeve: plastic rubs chalk"; fine "Looks just like the day it arrived." Wrong material label: a visitor's sticky note "This label says watercolor, but it's chalk pastel."

**Compare** (Library and museum): rows: Who watches the art? (library: the librarian, now and then; museum: guards and cameras, all day). Light? (library: sunny windows; museum: low light for works on paper, about 50 lux, a tenth of a bright office). Air? (library: heater in winter, open doors; museum: temperature and humidity kept steady all year). Can people touch? (library: kids can reach the low walls; museum: barriers, cases, "please do not touch"). What is it for? (library: lending books and bringing neighbors together; museum: collecting, caring for, studying and showing art). Closing line: "Your library show has to do a museum's job without a museum's tools."

## Interactions in detail
- Month run: `Open the show` plays 30 days in about 8 s (Motion off: the calendar jumps to day 30 after the same 8 s with no sweeping): a calendar counts days, the sun patch sweeps the window side once per day, heat shimmer pulses on S3 when the heater is on, hand icons tap S4 and S8 in June. Damage grows in three visible stages (day 10, 20, 30) so the student sees it coming. Effects are drawn in code over the painted works: fade (CSS filter saturate .3, brightness 1.15, a yellow cast), curl (a corner lifted with a skew and shadow), wave (a ripple mask), smudge (blurred streaks and fingerprint dots), pulled threads (loose yarn loops), crack (a drawn crack line on the bowl) or crush (the heron image tipped and squashed 70%).
- Any tap during the run (a spot, a card, a step) stops it at once and jumps straight to the results; nothing waits on the animation.
- A spot that cannot take a work (a 3D work on a wall) shakes once and the hint says why ("The bowl needs a shelf, a pedestal or the case.").
- Placing a work onto an occupied spot swaps the two (the old one goes back to the tray).
- The case holds one work. Every show has at least 336 safe arrangements (checked), so there is never one hidden answer.
- Keyboard: Tab to a card, Enter to pick it up, Tab to a spot, Enter to place; arrow keys move between spots in number order (panel controls before the spot markers in tab order).
- Saved on this device (localStorage `traveling-art-show`): finished shows and the current placements. `Start show over` clears that show.
- Sizes: the wall is painted at 16:9 and fitted at real pixels; spot markers are 44 px or bigger whatever the scale; at 680x425 the panel goes compact beside the wall (step chips, current card, the step's main button). At 375 wide the panel stacks under the wall with the step's main button first.

## Look
- Accent (`--brand`) #8a2b1f library brick. Paper #f6f1e9, ink #2a201c, muted #665a52, label cards white, "In the show" ribbon gold #f3d36b with ink text, "fine" chip #2e6b3a with white text and a check icon; damage chips use an icon and a word, never color alone.
- Contrast: white on brand 8.59:1; brand on paper 7.64:1; ink on paper 14.13:1; muted on paper 5.93:1; ink on gold 10.85:1; white on fine green 6.40:1; ink on label white 15.89:1.
- Different from neighbors: near-and-far valley green, art-style-match magenta, paint-mixer purple, song-form-builder teal, melody-maker burnt orange (this is a darker, redder brick).

## Art
Local FLUX (`scripts/localart.py`), no people. Style line for the room: "warm painted picture-book look, soft afternoon light, for a grade 4 art lesson". Works are drawn as children's art, each in its own medium.
- library-wall: "inside a small town library, one long cream wall seen straight on, a tall sunny window on the left with a deep window sill, a low wooden heater vent under a blank wall, a round story-time rug with a low bench, a front door with a coat hook and a small shelf beside it, a glass display case, a short white pedestal in the middle of the floor, a cozy reading nook with an armchair, a librarian's desk on the right, empty blank walls ready for art, warm painted picture-book look"; 16:9; cutout no; people no; the stage in Look around and Shows. The builder places the ten spot polygons on it.
- museum-gallery: "a quiet museum gallery with pale gray walls and soft even light, a wooden bench, a rope barrier on posts, a glass case, empty frames on the walls, warm painted picture-book look"; 16:9; people no; Library and museum.
- Eight works (cutouts, each "a child's artwork, <description>, flat front view on a plain white background", 3D ones "<object>, three-quarter view, plain white background"):
  - w1-pastel: a chalk pastel drawing of a farm stand with orange pumpkins and black crows on a fence, on blue paper, soft dusty strokes; 4:3.
  - w2-watercolor: a loose watercolor painting of small-town shops on a rainy street with puddles and umbrellas propped by doors, blank shop signs; 4:3.
  - w3-bowl: a small handmade glazed clay bowl, green glaze with painted frogs around the side; 1:1.
  - w4-collage: a cut and torn paper collage of a fall parade, paper leaves and paper dogs marching down a street, bright construction paper; 4:3.
  - w5-heron: a folded white paper sculpture of a heron standing on one leg on a blue paper base; 3:4.
  - w6-photo: a photo of an old stone bridge over a river with ducks on the water below, printed with a white border; 4:3.
  - w7-weaving: a small hand-woven yarn wall hanging with wavy blue and green stripes and loose fringe, hanging from a stick; 3:4.
  - w8-poster: a marker drawing of a striped orange cat sitting beside a fish tank, bold marker lines, bright flat colors; 3:4.
- 10 generated images, none with people. Drawn in code: spot markers, sun patch, shimmer, hand and cart icons, every damage effect, frames, sleeves, covers, labels, the calendar and all text.

## Voice
Bank voice `curious-librarian` (Aoede), style "Say curiously and warmly, like a friendly school librarian": the town librarian who is lending her walls. Not used by any 3-5 arts neighbor (near-and-far gravel-ranger, art-style-match lively-host, song-form-builder playful-friend, character-voice-booth smooth-narrator, dance-pattern-puzzle clear-teacher) or by another tool in this band. `Curio.voice` with `scope: () => state.mode + ':' + state.show`.
- welcomeLook (how; entering Look around; stale when a spot or card is tapped): "Welcome to the library. Tap a number on the wall to watch one day in that spot."
- fearHow (how; after the first spot loop; stale when a card is tapped): "Now tap an artwork to see what it's afraid of."
- tryHow (how; after the first fears card; stale on the first drag): "Drag an artwork onto a spot to see a month there."
- welcomeShows (how; entering Shows on step 1; stale when a card is flipped): "Read the theme. Tap six artworks to put them in the show, then tap Check my six."
- placeHow (how; first time step 2 opens; stale when Look around this month is tapped): "Tap Look around this month to find the dangers. Then drag each artwork to a safe spot."
- protectHow (how; first placement of a flat work; stale when a protect chip is tapped): "Pick how to protect it: a glass frame, a sleeve, or nothing."
- labelHow (how; first time step 3 opens; stale when a material is picked): "Pick the right material for each label. Then tap Open the show."
- choseWrong (event; after Check my six with a misfit; stale when a card is flipped): the misfit line from Content.
- result lines (event; one per hurt work after the run, in wall order; stale when Fix and run again is tapped): "Rainy Main Street faded: the sun hit it about 4 hours a day." (and the others, built from Content).
- allFine (event; stale when the show changes): "All six look just like the day they arrived. The show was a success."
- compareWelcome (how; entering Library and museum): "Tap a row to compare the library and the museum."

## Family engine
none

## Sources
- Light fades dyes, colored paper and photographs; museum light level about 50 lux for highly sensitive works; high-sensitivity materials show a just-noticeable fade after about 1.5 to 20 years at 50 lux: Canadian Conservation Institute, "Agent of Deterioration: Light, Ultraviolet and Infrared", https://www.canada.ca/en/conservation-institute/services/agents-deterioration/light.html
- Heat and dry air near heaters cause paper to cockle and curl and adhesives to fail; keep works away from vents; steady temperature and humidity in museums: CCI, "Agent of Deterioration: Incorrect Relative Humidity" and "Incorrect Temperature", https://www.canada.ca/en/conservation-institute/services/agents-deterioration.html ; Library of Congress, "Care, Handling and Storage of Works on Paper", https://www.loc.gov/preservation/care/paper.html
- Pastels must not touch glazing or plastic (they smudge and transfer), framed with a mat or spacer: Library of Congress, works on paper page above; Northeast Document Conservation Center, Preservation Leaflet 4.10 "Matting and Framing for Art and Artifacts on Paper", https://www.nedcc.org/free-resources/preservation-leaflets/4.-storage-and-handling/4.10-matting-and-framing-for-art-and-artifacts-on-paper
- Inkjet prints and marker inks are among the fastest-fading media: Image Permanence Institute, "Graphics Atlas: inkjet", http://www.graphicsatlas.org/ ; CCI light page above (felt-tip inks listed as high sensitivity).
- Museum purposes and guarding: American Alliance of Museums, "What is a museum?" https://www.aam-us.org/programs/about-museums/ (purpose line); library purpose: American Library Association, "Libraries Transform", https://www.ala.org/
- Bright office about 500 lux (so 50 lux is a tenth): CCI light page above.
- Checks run (Python, 2026-10-29): brute-force search of every placement of each show's six works into the ten spots with every protection: Show 1 has 1560 safe arrangements, Show 2 has 768, Show 3 has 336, so each show is solvable and has no single hidden answer; each show's aha holds (Show 2: the heron has only S2, S7 and S8 if bumps and heat are avoided, and S8 is sunny in January only for works that fear sun, which the heron does not, so the bowl or heron can take it; Show 3: the pastel's only safe walls are S3, S4 with a glass frame, S5, S7 and S10). Light dose: a just-noticeable fade for high-sensitivity materials is 0.22 to 2.9 million lux hours (CCI numbers, 8 h a day); a window wall in direct sun at about 30,000 lux for 4 h a day gets about 3.6 million lux hours in 30 days, past the top of that range, so a visible fade in one month is fair for marker, colored paper and inkjet; that is about 300 times a museum gallery's daily dose. Contrast ratios computed with the WCAG 2.1 formula.

## Done when
1. Focus: at 1366x768, 680x425 and 375 wide the library wall is the largest thing on screen and all ten spot markers are at least 44 px.
2. In Look around, each spot loop matches the month table (S3 shimmers only in January, S9 gets sun only in June, S8 gets sun in January and hands in June).
3. Choose: Check my six names each misfit with its reason, for all three themes.
4. A pastel in a sleeve on S5 comes out smudged; in a glass frame on S4 it comes out fine; any work that fears sun on S1 fades whatever its protection.
5. The month run shows damage growing at days 10, 20 and 30, and a tap during the run jumps to the results at once, with no line from the old run after it.
6. Each of the three shows can be finished with all six fine, and `Fix and run again` keeps placements.
7. A wrong material label brings the visitor's sticky note.
8. Each how line is spoken once in a run of five placements; result lines are spoken every run.
9. Keyboard alone can finish Show 1.
10. Nothing is stored but the show progress and placements; `Start show over` clears that show.

## Open questions
- None for Cory.
