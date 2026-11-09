# Explainer Sections

## One idea
The student takes apart a short explainer ("How Do Bridge Inspectors Find Cracks?") section by section, putting the shuffled blocks in order and tagging each one's job (hooks, defines, shows steps, compares, explains a cause, answers a worry) while a little reader walks down the page and stops with a question bubble wherever a section arrives too early or is missing; then they build their own explainer by choosing an organizing pattern and writing headings and transitions that fit it, until the reader reaches the end with no questions left, so they learn that structure is how an explainer carries a reader from not knowing to knowing.

## Not like
- explainer-studio (7, concept): the content inside sections (precise words, examples, style). Here the structure between sections.
- blueprint-builder (4, spec): grade 4 text structures from facts. Here grades 6-8 section jobs and a build.
- structure-spotter (3, spec): text features. Here how sections build a whole.
- essay-rope-team (5, spec): essay order and transitions. Here informative sections with jobs and a reader test.
- how-it-works-diagrams (spec): diagrams. Here sections of prose.

## Who and how
- Grades 6-8, ELA, module "Structure in Informative Writing" (Writing and Reading Informational Text). Standards: W.6.2, RI.6.5, RI.7.5, W.7.2, W.8.2.
- Driver: one student, or partners swapping explainers (tool.json `driver: "student"`). Every block is read on tap; the student's sections are read back by the browser's speech voice.
- Grade picker: 6 (take apart, build with headings and transitions), 7 (adds a definition section and a comparison chart), 8 (adds a misunderstanding section and a conclusion that follows from the whole). tool.json `modes: ["Grade 6", "Grade 7", "Grade 8"]`, `minutes: "30-45"`, `grades_label: "Grades 6-8"`.
- Saving: the student's explainer is kept in this browser; footer: "Your explainer stays on this device." `Clear my explainer` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.6.5 | Order the shuffled blocks and tag each block's job | blocks with job tags; the reader's walk | 2 |
| RI.7.5 | Explain how the major sections build the whole in one line per section | the section map | 3 |
| W.6.2 | Build an explainer: pick a pattern, write headings that name the job, add transitions and a conclusion | the student's page and the reader's walk | 4 |
| W.7.2 | Grade 7 build: a definition section and a comparison chart | the chart and the definition tag | 5 |
| W.8.2 | Grade 8 build: a misunderstanding section and a conclusion that follows from the whole | the two extra sections | 6 |

## Screens and modes
Header (kit): title "Explainer Sections"; `Take apart`, `Build`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A tall page on a drafting table, cut into blocks scattered beside it, and Pip, a little reader made of paper with a magnifier, standing at the top of the page. First hint: "Tap a block to hear it." The first tap reads the block's first line; the welcome is queued after it (`welcomeAfter: true`).

**Take apart.** The model explainer, written for Curio Class from sourced facts, in 7 blocks: a hook (a bridge that carries thousands of cars a day), a definition (what a crack in a steel or concrete bridge is and why small ones matter), a cause (what makes cracks: repeated loads, rust, freezing water), steps (how an inspection goes: look, touch, test), a comparison (four ways to find hidden cracks: eyes and hammers, dye that seeps in, magnets and iron powder, sound waves), a worry (Does a crack mean the bridge will fall? Not usually; it means it gets watched and fixed), and a conclusion. Each block's data holds its job and what it depends on (the comparison needs the definition).

**The reader's walk.** `Walk` sends Pip down the page; at a block that uses a word not yet defined, Pip stops with a question bubble ("What's a weld?"); at a missing job, Pip stops with "Wait, why does this happen?" The bubble names the problem, not the fix.

**Tag jobs.** The student tags each block from six job chips; the tag is checked against data.

**Section map (grade 7 and up).** One line per section: "This section ___ so the reader can ___." Read back.

**Build.** A topic shelf: How a seed bank works; How lightning forms; How a bridge inspector's sound-wave tester works (for those who want to go deeper); or the student's own. Each shelf topic comes with a fact pack of 10 to 14 sourced facts. The student picks a pattern (sequence, cause and effect, compare, problem and solution); the pattern suggests section jobs. They write a heading per section that names its job ("Why lightning needs ice"), the section text, and a transition from a tray or their own. Pip walks their draft: Pip stops at any section with no heading, at a fact-pack word that's used before its definition section, and at a missing conclusion.

**Grade 7 and 8 additions.** Grade 7: the build needs a definition section and a two-column comparison chart (drawn in code from rows the student fills). Grade 8: a "common mix-up" section (for lightning: "Lightning never strikes the same place twice" is false) and a conclusion that names the pattern's end point.

**End.** When Pip reaches the end with no bubbles, the student writes one line on why their pattern fit the topic.

At 1366x768 the page and blocks fit side by side; at 680x425 the blocks are a tray under the page.

## Content
Written for Curio Class from sourced facts:
- Model: bridge inspection (federal rules require most highway bridges to be inspected at least every 24 months; methods include visual and hammer checks, dye penetrant, magnetic particle and ultrasonic testing).
- Seed bank pack: the Svalbard Global Seed Vault in Norway stores seed copies from gene banks around the world at about minus 18 degrees Celsius.
- Lightning pack: lightning forms when ice and water particles in a storm cloud collide and separate charge; lightning can and does strike the same place more than once (tall buildings are hit many times a year).
- Transition tray: 16 transitions labeled by pattern.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Blocks and sections can be reordered any time; Walk can run any time.
- With Motion off Pip jumps from block to block.
- The fact-pack words that need a definition are listed in data; the student's own topic skips that check.

## Look
- Accent `--brand` #2d5a8c blueprint blue (header, block edges, the drafting grid); gold #f4c542 (Pip's magnifier, tags); paper #f3f6fb; ink #0e1b2b; muted #4f5868. Scene: a drafting table under a window.
- Contrast (WCAG 2.1, computed): white on brand 7.11:1; brand on paper 6.57:1; ink on paper 16.02:1; muted on paper 6.62:1; ink on gold 10.67:1.
- Never color alone: tags are words; bubbles carry text.
- Different from this batch (editor's red, web green, lilac, lamp amber).

## Art
Local FLUX (`scripts/localart.py`), no people in focus.
- drafting table (1); Pip (4 poses: walk, stop with a question, read, cheer), "A small friendly paper character holding a magnifying glass <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- topic pictures (4): "<a steel bridge underside with rivets / a seed vault entrance in snowy mountains / lightning over a field / an inspector's tablet showing sound waves, no people>, realistic illustration, no text"; 4:3.
About 9 images. Drawn in code: page, blocks, bubbles, chart.

## Voice
Bank voice `science-narrator` as Pip (unique in this batch). `Curio.voice` with `scope: () => state.grade + ':' + state.view + ':' + state.block`, `welcomeAfter: true`.
- how `welcome`: "An explainer carries a reader from not knowing to knowing. Put the sections in order, then I'll walk down the page."
- event, whole, `block`: the tapped block.
- event `stuck`: Pip's question bubble ("What's a {weld}?").
- event `clear`: "Made it to the end. No questions!"
- how `tagHow`: "What job does this section do? Pick a tag."
- how `buildHow`: "Pick a topic and a pattern. Then write a heading that names each section's job."
- event `whyLine`: "Why did your pattern fit? Write one line."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: blocks with jobs and dependencies, the reader walk, section editor with pattern suggestions, comparison chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Try orders until Pip clears | 7 blocks have 5,040 orders; Pip's bubble names the problem, so trying leads to the reasoning, and the tags are checked separately. |
| Tags | Tag everything "explains" | Each block has one job in data. |
| Build | Write one big section | Pip stops at missing headings and a missing conclusion; grade 7 and 8 need their extra sections. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a block: its first line, `welcome` (queued, first time).
2. Blocks: `block` (whole); `tagHow` (first time).
3. Walk: `stuck` at each stop, or `clear`.
4. Build: `buildHow`; at the end, `whyLine`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.2, RI.6.5, RI.7.5, W.7.2, W.8.2 wording | thecorestandards.org, Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Most US highway bridges must be inspected at least every 24 months | Federal Highway Administration, National Bridge Inspection Standards | eCFR, 23 CFR 650 Subpart C | yes |
| Dye penetrant, magnetic particle and ultrasonic testing find surface and hidden cracks in steel | Federal Highway Administration, bridge inspector's reference manual | American Society for Nondestructive Testing, introduction to methods | yes |
| The Svalbard Global Seed Vault stores duplicate seed samples at about minus 18 degrees Celsius | Crop Trust, Svalbard Global Seed Vault | Norwegian Ministry of Agriculture and Food, Svalbard Global Seed Vault | yes |
| Lightning forms as colliding ice and water particles separate charge in a storm cloud; lightning often strikes the same place more than once | NOAA National Severe Storms Laboratory, lightning basics | National Weather Service, lightning myths | yes |
Backed twice: 5. Cut: 1 (a count of how many US bridges are rated in poor condition; the figure changes each year, so the model leaves it out).

Checks run (Python, scratchpad b17, 2026-11-09): in the sample model, the shuffled start triggers at least one stuck bubble and the key order clears the walk; the comparison block depends on the definition block; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page and blocks fit; at 680x425 the blocks are a tray.
2. Blocks order and take job tags; Pip's walk stops at early or missing sections. (RI.6.5)
3. The section map takes a line per section. (RI.7.5)
4. The build takes a pattern, headings, transitions and a conclusion, and Pip walks it. (W.6.2)
5. Grade 7 adds a definition section and a chart. (W.7.2)
6. Grade 8 adds a misunderstanding section and a following conclusion. (W.8.2)
7. The explainer survives a reload where storage works; `Clear my explainer` removes it.
8. Print shows the explainer and the section map.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: Pip jumps; no network requests.

## Open questions
- None for Cory.
