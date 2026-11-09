# Plot Rollercoaster

## One idea
The student builds a rollercoaster track from the episodes of Rudyard Kipling's "Rikki-Tikki-Tavi", setting each piece's height by how much tension it adds, and rides it with Rikki, whose face and thought bubble change at each drop and climb as he grows from a curious young mongoose washed out by a flood into the garden's guardian; pulling out any one scene makes the track collapse where that scene was holding something up, so they learn how episodes build a plot and how one scene can carry a character's change.

## Not like
- story-map-treasure (1, concept): story elements on a treasure map. Here tension and change across episodes, grade 6.
- story-building-blocks (3, concept): ordering story blocks. Here heights, character change and a remove-a-scene test.
- character-face-off (spec): comparing two characters. Here one character changing scene by scene.
- slow-mo-writer (spec): stretching one moment in your own writing. Here the shape of a whole published story.
- theme-evidence-ladder (6-8, spec, this batch): passages proving a theme. Here episodes building a plot.

## Who and how
- Grade 6, ELA, module "Plot and Character Development" (Reading Literature). Standards: RL.6.3, RL.6.5.
- Driver: one student; class mode builds a coaster with custom cards (tool.json `driver: "student"`). Every episode card is read on tap.
- Text: "Rikki-Tikki-Tavi" from The Jungle Book by Rudyard Kipling (1894), public domain, in twelve episode cards with the full text a tap away. tool.json `modes: ["Rikki-Tikki-Tavi", "Class coaster"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the coaster and the remove-a-scene answers. A class coaster typed by the teacher stays only while the page is open.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.6.3 (episodes) | Place the twelve episodes in order as track pieces and set each height | the track with heights | 2 |
| RL.6.3 (character responds and changes) | At each piece, pick how Rikki responds and what changes in him, backed by a line from the story | Rikki's face and thought bubble per piece | 3 |
| RL.6.3 (toward a resolution) | Ride the coaster; the ride stops at the resolution and Rikki's last face is compared with his first | the ride and the before-and-after faces | 4 |
| RL.6.5 | Pull one scene and explain what it did for the plot, the setting, Rikki's change or the theme | the collapsed track and the student's line | 5 |

## Screens and modes
Header (kit): title "Plot Rollercoaster"; `Cards`, `Build`, `Ride`, `Remove a scene`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A sunny coaster yard at a fair, an empty track bed, a stack of twelve episode cards and a park announcer's booth. First hint: "Tap the top card to hear the story begin." The first tap reads the first card; the welcome is queued after it (`welcomeAfter: true`).

**Cards.** Twelve episodes: the flood washes Rikki into the garden; the family takes him in; he explores the house; Darzee warns him about Nag; the first face-off with Nag and Nagaina; Rikki kills Karait and saves Teddy; Chuchundra's warning; the fight with Nag in the bathroom; the plan with Darzee's wife; the eggs; Nagaina threatens the family at breakfast; the last chase into the rat-hole and the end. Each card shows a short summary and a `Read the story` link to the full passage.

**Build.** The student drags cards onto the track bed in order and sets each piece's height with a slider in five steps (flat, low, climb, high, peak). A keyed range checks heights: the start must be low, the peak must be one of the last three cards before the end (the keyed peaks are the bathroom fight, the breakfast threat and the chase), and the end must drop. Out-of-range pieces show a dashed outline and "Does this add more tension than the last piece?"

**Change.** At each piece, the student picks how Rikki responds (curious, scared, bold, careful, proud) from keyed choices and taps a line from the passage that shows it. The keyed arc runs from curious ("Run and find out") through careful to protector; the student may pick another response if they tap a line that supports it.

**Ride.** A small coaster car carries Rikki along the track; at each piece his face changes and his thought bubble shows the student's line (Motion off: the car jumps piece to piece). At the end the first and last faces sit side by side with "What changed?" and a sentence frame.

**Remove a scene.** The student pulls any one piece. The track shows what breaks using keyed jobs: pulling "the flood" removes the setting and how Rikki arrives ("Where did he come from?"); pulling "Karait" removes his first win, so his boldness at the bathroom comes from nowhere; pulling "the eggs" removes why Nagaina comes to the breakfast table. The student writes one line on what the scene did, picking plot, setting, character or theme.

**Class coaster.** The teacher types episode cards for another book; Remove a scene then asks the student's line with no keyed jobs.

At 1366x768 the cards and track fit; at 680x425 the cards are a strip above the track.

## Content
- "Rikki-Tikki-Tavi", Project Gutenberg #236 (The Jungle Book), split into twelve passages with summaries written for Curio Class, keyed heights, keyed responses and lines, and keyed jobs for Remove a scene.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pieces can be reordered; checks rerun.
- The ride can be paused at any piece.
- With Motion off nothing slides or drops; labels show heights.

## Look
- Accent `--brand` #a12f6b coaster magenta (header, track, car); gold #f4c542 (the peak, Rikki's thought bubble edge); paper #fbf2f7; ink #2e0a1d; muted #6a5060. Scene: a sunny fair with a coaster yard.
- Contrast (WCAG 2.1, computed): white on brand 6.70:1; brand on paper 6.11:1; ink on paper 16.26:1; muted on paper 6.54:1; ink on gold 10.97:1.
- Never color alone: heights show words (flat to peak); collapsed pieces show a label.
- Different from this batch (ivy green, cart amber, roots blue, rally orange).

## Art
- Local FLUX (`scripts/localart.py`): coaster yard (1); Rikki faces (6: curious, scared, bold, careful, proud, protector), "A young mongoose character, <expression>, children's book illustration, soft gouache, plain white background"; 1:1; cutout yes; garden scenes (3: flooded ditch, a garden with a tall bush, a melon bed), no people.
- No people art: Teddy and his family are named in the text but never drawn, which avoids picturing the colonial household.
About 10 images. Drawn in code: track, car, cards, sliders.

## Voice
Bank voice `lively-host` as the park announcer (unique in this batch); the story is read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.piece`, `welcomeAfter: true`.
- how `welcome`: "Every story is a ride. Lay the track, set the hills, and ride along with Rikki."
- event, whole, `card`: the tapped card or passage.
- event `height`: "Does this add more tension than the last piece?"
- event `face`: "{Bold}. Show me the line."
- event `ride`: the student's line at each piece, read as the car passes.
- event `collapse`: "{Where did he come from?}"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: ordered track pieces with keyed height ranges, keyed responses with lines, the ride, keyed scene jobs.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Heights | Make every piece a peak | Keyed ranges flag the start and end; only one peak is allowed. |
| Responses | Pick at random | Each response needs a line from that passage that supports it. |
| Remove a scene | Write anything | The keyed jobs show what broke; the line must pick plot, setting, character or theme matching one of them. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the top card: first card, `welcome` (queued, first time).
2. Build: `height` as it fires.
3. Change: `face` per piece.
4. Ride: `ride` at each piece (waits, then the car moves on).
5. Remove a scene: `collapse`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.3 and RL.6.5 wording | thecorestandards.org, Reading Literature Grade 6 | CCSS ELA 2010 PDF | yes |
| "Rikki-Tikki-Tavi" is in Kipling's The Jungle Book (1894), public domain | Project Gutenberg eBook #236 (checked 2026-11-09) | Library of Congress catalog record for The Jungle Book (1894) | yes |
| Plot structure: exposition, rising action, climax, falling action, resolution | ReadWriteThink, plot diagram | Purdue OWL, literary terms (plot) | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: the story is set in a British family's home in colonial India and has fights to the death between animals; the art shows only animals and the garden, the fights are told, not shown, and the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b20, 2026-11-09): the Gutenberg file is The Jungle Book and contains the Rikki-Tikki-Tavi story (about 7,600 words with Darzee's Chant); the lines "Run and find out" and the flood are found in it; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 cards and track fit; at 680x425 the cards are a strip.
2. Twelve pieces place with heights checked by keyed ranges. (RL.6.3)
3. Each piece takes a response with a supporting line. (RL.6.3)
4. The ride shows faces and lines and ends with first and last faces. (RL.6.3)
5. Remove a scene shows the keyed break and takes a line. (RL.6.5)
6. Class coaster takes custom cards.
7. Print shows the coaster and answers.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: nothing slides or drops; no network requests.

## Open questions
- None for Cory.
