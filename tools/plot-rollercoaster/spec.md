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
- Driver: one student; class mode builds a coaster with custom cards (tool.json `driver: "student"`). Role: lesson. Every episode card is read on tap.
- Change note (spec fix, 2026-11-10): the coaster, the twelve episodes and Rikki's faces stay. The core of Remove a scene is new. Before, the tool showed what broke and the student then picked a label, on one scene. Now the student pulls five scenes, one sentence and one stanza, and for each says first what the story would lose and which later piece would fail, in their own words; only then does the track show the break. Heights are no longer set by trial: they are tested as a whole track. Six episode notes and a closing paragraph, written beside a model and a guide, give the "describe" the standard asks for. The announcer works the first piece as the model. Not added: a drama. The standard says "story's or drama's", so one story meets it, and Class coaster takes the scenes of a play.
- Text: "Rikki-Tikki-Tavi" from The Jungle Book by Rudyard Kipling (1894), public domain, in twelve episode cards with the full text a tap away. tool.json `modes: ["Rikki-Tikki-Tavi", "Class coaster"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the coaster and the remove-a-scene answers. A class coaster typed by the teacher stays only while the page is open.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RL.6.3 (episodes) | describe how a story's plot unfolds in a series of episodes | the student | Order the twelve episodes, set each height, and write an episode note on six pieces: what happens and how it raises or lowers the tension | 12 pieces; 6 notes | the track; the student's notes on the pieces | 2, 3 |
| RL.6.3 (characters respond or change) | describe how the characters respond or change | the student | At each piece pick how Rikki responds and tap the line that shows it; say it in the note | 12 | Rikki's face and thought bubble per piece | 4 |
| RL.6.3 (toward a resolution) | as the plot moves toward a resolution | the student | Ride, then write three sentences on how Rikki at the end differs from Rikki at the start and which episode turned him | 1 paragraph | the ride and the before-and-after faces | 5 |
| RL.6.5 | analyze how a sentence, chapter, scene or stanza fits the overall structure and contributes to theme, setting or plot (chapter left out: the story is one chapter) | the student | Pull a part; before anything breaks, pick what the story would lose, tap the later piece that depends on it, and write why; then test | 7 (5 scenes, 1 sentence, 1 stanza) | the track failing only after the student's answer | 6 |

## Screens and modes
Header (kit): title "Plot Rollercoaster"; `Cards`, `Build`, `Ride`, `Remove a scene`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A sunny coaster yard at a fair, an empty track bed, a stack of twelve episode cards and a park announcer's booth. First hint: "Tap the top card to hear the story begin." The first tap reads the first card; the welcome is queued after it (`welcomeAfter: true`).

**Cards.** Twelve episodes: the flood washes Rikki into the garden; the family takes him in; he explores the house; Darzee warns him about Nag; the first face-off with Nag and Nagaina; Rikki kills Karait and saves Teddy; Chuchundra's warning; the fight with Nag in the bathroom; the plan with Darzee's wife; the eggs; Nagaina threatens the family at breakfast; the last chase into the rat-hole and the end. Each card shows a short summary and a `Read the story` link to the full passage.

**The announcer lays the first piece (the model).** The announcer places "the flood", sets it low and says why ("Nothing is after him yet. He is only lost."), picks curious, taps the line that shows it, and writes the note: "A flood washes Rikki out of his burrow and into the garden. He is not afraid. He wants to look at everything." This cannot be skipped and `Announcer's piece` reopens it.

**Build.** The student drags the other eleven cards onto the track bed in order and sets each piece's height with a slider in five steps (flat, low, climb, high, peak). Nothing is judged while the sliders move. `Test the track` checks the whole track against a keyed range: the start is low, the peak is one of the last three cards before the end (the bathroom fight, the breakfast threat or the chase), there is only one peak, and the end drops. A failed test says how many pieces are out of range but not which; a second failed test outlines them with "Does this add more tension than the last piece?" The track must pass before the ride opens.

**Episode notes.** On six pieces (the family takes him in, the first face-off, Karait, the bathroom fight, the breakfast threat, the chase and the end) a note box opens: two sentences in the student's own words. The announcer's note stays in view with a three-box guide: says what happens; says how Rikki meets it; says whether the danger grows or eases. The tool cannot mark the words, so the model and the guide do that job, and the notes print on the coaster.

**Change.** At each piece, the student picks how Rikki responds (curious, scared, bold, careful, proud) and taps a line from the passage that shows it. Each passage has its lines keyed to the responses they support. A line that does not support the pick is turned away once with "What does this line show him doing?"; a second miss marks the piece "look again", and the ride stops there until it is fixed. The keyed arc runs from curious ("Run and find out") through careful to protector; the student may pick another response if a tapped line supports it.

**Ride.** A small coaster car carries Rikki along the track; at each piece his face changes and his thought bubble shows the student's line (Motion off: the car jumps piece to piece). At the end the first and last faces sit side by side with "What changed?" The student writes three sentences, beside a guide: Rikki at the start; Rikki at the end; the episode that turned him and why. A model paragraph about a different, made-up story (a shy dog at a shelter) shows the form without giving the answer.

**Remove a scene.** Seven parts to pull, in any order: five scenes (the flood, Karait, Chuchundra's warning, the plan with Darzee's wife, the eggs), one sentence (the mongoose family motto, "Run and find out", in the opening) and one stanza (the first stanza of Darzee's Chant at the end). For each the student answers before anything moves:
1. What would the story lose? Pick one or more of plot, setting, character, theme.
2. Which later piece depends on it? Tap that piece on the track (for the stanza, tap `nothing later` and say what the ending would lack).
3. Why? One or two sentences in the student's own words.
Only then does `Pull it` run: the tapped piece either sags, because it did rest on the pulled part, or holds, because it did not. A wrong tap can be tried once more; after a second miss the announcer shows the keyed break, that part is marked "shown", and the student's why line is still required. The announcer pulls one scene first as the model (the family takes him in: without it Rikki has no one to guard, so the breakfast threat means nothing to him).

**Class coaster.** The teacher types episode cards for another book; Remove a scene then asks the student's line with no keyed jobs.

At 1366x768 the cards and track fit; at 680x425 the cards are a strip above the track.

## Content
- "Rikki-Tikki-Tavi", Project Gutenberg #236 (The Jungle Book), split into twelve passages with summaries written for Curio Class, keyed heights, keyed responses and lines.
- Keyed breaks for Remove a scene. The flood: setting and plot; the family takes him in has no way to begin. Karait: character; his boldness at the bathroom fight has no first win behind it. Chuchundra's warning: plot; Rikki has no reason to listen at the bathroom sluice, so the bathroom fight does not start. The plan with Darzee's wife: plot; Nagaina is not drawn away, so Rikki cannot reach the eggs. The eggs: plot; at the breakfast threat Rikki has nothing to turn Nagaina away from Teddy. The motto sentence: character and theme; his choice to follow Nagaina down the hole in the chase loses its root. The stanza of Darzee's Chant: theme; nothing later depends on it, and the ending loses the garden's praise of what Rikki did.
- Six note pieces: the family takes him in, the first face-off, Karait, the bathroom fight, the breakfast threat, the chase and the end.

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
- event `collapse`: "{Where did he come from?}" Plays only after the student's answers are in.
- how `test`: "Set every hill, then tap Test the track."
- how `note`: "Write two sentences about this piece. Then check the guide."
- how `pull`: "Pick what the story would lose. Then tap the piece that needs it."
- event, whole, the announcer's first piece and first pull.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: ordered track pieces with keyed height ranges, keyed responses with lines, the ride, keyed scene jobs.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Heights | Make every piece a peak; nudge sliders until the outline goes | Nothing shows while sliders move; the test is of the whole track, the first fail gives only a count, and only one peak is allowed. |
| Responses | Pick at random; tap lines until one sticks | Five responses and many lines; one free miss, then the piece is marked and blocks the ride. |
| Notes and closing paragraph | Tick the guide on an empty box; copy the model | The ticks open only when the box has words; the announcer's note is about the flood, which is not one of the six, and the closing model is about another story. |
| Remove a scene | Wait to see what breaks, then copy it | The break shows only after the three answers are in. Eleven later pieces can be tapped and two misses mark the part "shown" on the printout. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the top card: first card, `welcome` (queued, first time).
2. The announcer's first piece (whole). Build: `test`; `height` after a second failed test. `note`.
3. Change: `face` per piece.
4. Ride: `ride` at each piece (waits, then the car moves on).
5. Remove a scene: the announcer's pull (whole); `pull`; `collapse` after the answers.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.3 and RL.6.5 wording | thecorestandards.org, Reading Literature Grade 6 | CCSS ELA 2010 PDF | yes |
| "Rikki-Tikki-Tavi" is in Kipling's The Jungle Book (1894), public domain | Project Gutenberg eBook #236 (checked 2026-11-09) | Library of Congress catalog record for The Jungle Book (1894) | yes |
| Plot structure: exposition, rising action, climax, falling action, resolution | ReadWriteThink, plot diagram | Purdue OWL, literary terms (plot) | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: the story is set in a British family's home in colonial India and has fights to the death between animals; the art shows only animals and the garden, the fights are told, not shown, and the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b20, 2026-11-09): the Gutenberg file is The Jungle Book and contains the Rikki-Tikki-Tavi story (about 7,600 words with Darzee's Chant); the lines "Run and find out" and the flood are found in it; contrast as in Look.

Spec fix checks (2026-11-10): the seven keyed breaks were checked against the order of the twelve episode cards, and each depends-on piece comes after the pulled part; the earlier key for "the eggs" (why Nagaina comes to the breakfast table) was wrong, since she comes for the family and the egg is what turns her away, and it has been corrected. The Gutenberg text was not reopened in this pass; the motto sentence and Darzee's Chant should be confirmed against it at Build.

## Done when
1. Focus and fold: at 1366x768 cards and track fit; at 680x425 the cards are a strip.
2. Twelve pieces place, and heights pass `Test the track` as a whole; the first failed test gives a count only. (RL.6.3)
3. Six episode notes are written and checked against the guide. (RL.6.3)
4. Each piece takes a response with a supporting line; a twice-missed piece blocks the ride. (RL.6.3)
5. The ride shows faces and lines and ends with the student's three sentences on what changed. (RL.6.3)
6. Seven parts are pulled (five scenes, one sentence, one stanza); each break shows only after the student has picked what is lost, tapped the piece that depends on it and written why. (RL.6.5)
7. The announcer's first piece and first pull play before the student's and can be reopened.
8. Class coaster takes custom cards.
9. Print shows the coaster, the notes and the answers, with "shown" on any part the announcer had to show.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
11. Motion off: nothing slides or drops; no network requests.

## Open questions
- None for Cory.
