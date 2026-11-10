# Nerve Signal Relay

## One idea
An illustrated body figure stands beside a big tap pad, with the eye, ear and fingertip marked, and the student races their own reaction time in short rounds against a ghost of their own best: a light round (tap when the circle appears), a sound round (tap at the tone, always shown with a matching visual pulse ring so it works without sound), a choice round (tap only for green, wait on other shapes), and a sequence round where the same four-tap pattern repeats ten times; after each tap the signal's path lights up step by step (receptor, sensory nerve, spinal cord or brain, motor nerve, muscle) with the measured time, and short info cards explain rods and cones in the eye, hair cells in the ear and touch receptors in the skin; at the end a graph of the student's own times shows the choice round slower than the simple round and the practiced sequence speeding up over tries, and the student writes one sentence for "quick reaction" and one for "stored memory" using their data and the cards, so a seventh grader learns to gather and synthesize information that sensory receptors respond to stimuli by sending messages to the brain for immediate behavior or storage as memories.

## Not like
- how-animals-see (3 to 5, live): other animals' eyes. Here a student's own senses, nerves and brain.
- body-thermostat (9, spec): feedback that keeps the body steady. Here messages from senses to brain.
- motion-graph-match (11, live): racing to match graphs. Here racing your own reaction time.
- cell-city (6, spec): cells building body systems. Here signals moving through them.

## Who and how
- Grade 7, Science, module "Senses and the Brain". Standard: MS-LS1-8 (gather and synthesize information that sensory receptors respond to stimuli by sending messages to the brain for immediate behavior or storage as memories).
- Format: race. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more; the tap pad is at least 200 px.
- Four rounds of ten taps each, the ghost of the student's best, the path view, three info cards, the times graph, two sentence cards. Extra: Ruler drop (an off-screen ruler-drop activity with a results sheet). tool.json `modes: ["Relay", "Ruler drop"]`, `minutes: "15-25"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-LS1-8 (receptors to brain) | Tap to light, tone and touch cues and watch the path | the path lighting step by step; the info cards | 2 |
| MS-LS1-8 (immediate behavior) | Compare simple and choice rounds | the times graph | 3 |
| MS-LS1-8 (memory) | Repeat the sequence ten times and write both sentences | the falling sequence times; the sentence cards | 4 |

## Screens and modes
Header (kit): title "Nerve Signal Relay"; `Relay`, `Ruler drop`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The body figure (illustrated, labeled "illustration") with three glowing spots; a big round tap pad below. The welcome is queued (`welcomeAfter: true`): "Your body is sending messages right now. How fast are they? Tap the pad when the circle appears." First hint: "Tap Start, then tap the pad when the circle appears."

**A round (focus: the pad).** At 1366x768 the figure is left and the pad right with the ghost bar above it; at 680x425 the pad fills the lower half and the figure is a small strip. A random wait of one to three seconds, then the cue. The student's time shows beside the ghost's. A tap before the cue says "Too early. Wait for the circle." Then the path view runs once (receptor, nerve, brain, nerve, muscle) with a time on each leg: the nerve legs are tiny (signals travel up to about 100 m a second), most of the time is in the brain deciding.

**Four rounds.** Light (eye), Sound (ear, with the pulse ring always on), Choice (green only; red squares and blue triangles mean wait), Sequence (four spots, same order, ten times). Each round opens one info card: rods and cones; hair cells; touch receptors; practice building memory.

**The graph (the aha).** Bars for each round's median; a line for sequence tries one to ten. Narrator: "A new choice makes your brain stop and think. A pattern you practice gets stored, so your brain can send it faster."

**Sentence cards.** "A quick reaction happens when ___. My data shows ___." "A memory gets stored when ___. My data shows ___."

**The end.** The graph and both sentences. `Print` prints them.

**Ruler drop (extra).** A printable sheet for the classic ruler drop with a distance-to-time table.

## Content
- Four round rules, timing with `performance.now()`, the path view with stated speeds, three info cards plus one on practice, the graph, two sentence cards.
- Flash safety: cues appear and stay until tapped; no flashing; no more than one cue change a second, under the three-flashes-a-second limit.
- Sound round always pairs the tone with a visual pulse ring; with Sound off the ring alone is the cue.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Space or Enter also counts as a tap; voice lines never play during a timed wait.
- Keyboard: Tab to `Start`, the pad, the graph and the cards; Space taps.
- With Motion off the path view lights all at once and the ghost bar is still.

## Look
- Accent `--brand` #7a1f5c signal magenta (header, the path, the ghost bar); gold #f4c542 (the cue circle, the current leg of the path); paper #faf2f7; ink #26091b; muted #5c4f57.
- Contrast (WCAG 2.1, computed): white on brand 9.64:1; brand on paper 8.77:1; ink on paper 16.80:1; muted on paper 7.05:1; ink on gold 11.35:1.
- Never color alone: the choice round uses shape as well as color (green circle, red square, blue triangle).
- Different from this batch (spruce, prairie amber, indigo, factory teal).

## Art
- People (illustrated): the body figure, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Drawn in code: the path, receptors close-ups as simple diagrams, the pad, the ghost bar, the graph.
About 1 image.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the race coach between rounds; `calm-professor` as the info cards and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.try + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `start`: "Tap Start, then tap the pad when the cue shows."
- how `choice`: "Tap only for the green circle."
- how `sequence`: "Tap the four spots in the same order."
- event, whole, each info card (never during a timed wait).
- event, whole, the graph.
- how `write`: "Fill in both sentence cards."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the timer, round rules, the path view, the graph. Speeds and card text sit in a marked block `/* NERVE-RELAY DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rounds | Tap early every time | Early taps don't count and the round repeats that try. |
| Choice | Tap for every shape | Wrong taps are counted and shown on the graph. |
| Sentences | Write without data | Each card asks for a number from the graph. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `start`.
2. Info card (whole) after each round, waits.
3. `choice`; `sequence`.
4. Graph (whole), waits. `write`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-LS1-8 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Rods, cones, hair cells and touch receptors turn stimuli into nerve signals | National Eye Institute, "How the eyes work" | NIH National Institute on Deafness and Other Communication Disorders, "How do we hear?" | yes |
| Fast nerve signals travel up to about 100 meters a second | OpenStax, "Anatomy and Physiology 2e", chapter 12 | University of Washington, "Neuroscience for Kids", speed of nerve impulses | yes |
| Choice reactions are slower than simple reactions | Hick (1952), Quarterly Journal of Experimental Psychology | University of Washington, "Neuroscience for Kids", reaction time | yes |
| Practice speeds up a repeated sequence as it is stored in memory | NIH National Institute of Neurological Disorders and Stroke, "Brain Basics" | OpenStax, "Psychology 2e", chapter 8 | yes |
| Flashes must stay at or under three a second | W3C, WCAG 2.1 Success Criterion 2.3.1 | Epilepsy Foundation, "Photosensitive epilepsy" | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-10): one meter at 100 m a second is 0.01 seconds, 4 percent of a 0.25-second reaction; ten tries per round; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 figure and pad; at 680x425 pad with strip.
2. Light, sound and touch-cue rounds light the full path with info cards. (MS-LS1-8)
3. Simple and choice rounds are compared on the graph. (MS-LS1-8)
4. Ten sequence tries are graphed and both sentences cite data. (MS-LS1-8)
5. No flashing; cues change at most once a second.
6. The sound round works fully with Sound off through the pulse ring.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: path lights at once; no network requests.

## Open questions
- The idea card flags accessibility (default used: the sound round always pairs the tone with a visual pulse ring and works with Sound off; cues never flash and change at most once a second, under the WCAG three-flash limit).
