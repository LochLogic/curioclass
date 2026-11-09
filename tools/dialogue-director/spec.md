# Dialogue Director

## One idea
The student directs a four-panel comic (two characters, a setting, poses and speech bubbles), then shoots the "prose take": every bubble becomes a quoted line with the right commas, quotation marks and capitals, and every picture becomes narration with actions, thoughts and time words, and a blindfolded listener hears only the prose and asks "Wait, what happened?" wherever a picture's action was never written, so the student learns what a written story has to say in words that a comic shows in pictures.

## Not like
- my-story-strip (K, spec): draw and tell a strip out loud. Here the strip is the plan, and the job is turning it into written prose.
- two-sides-theater (2, spec): one event from two sides. Here one story told in two media.
- show-don-t-tell (4, concept): feelings through details. Here the basics: dialogue punctuation, narration of actions, time order.
- draft-car-wash (3-5, spec): revising a given draft. Here writing a new one from a comic.
- story-blanks (3, spec): word jobs in a given story. Here the student's own story.

## Who and how
- Grade 3, ELA, module "Narrative Writing" (Writing). Standards: W.3.3 (a to d), L.3.2a (capitals in titles), L.3.2c (commas and quotation marks in dialogue), L.3.2d (possessives). Address commas and spelling go to draft-car-wash's grade 3 Polish station, as the idea card moved them.
- Driver: one student (tool.json `driver: "student"`). Every bubble, narration line and helper note is read on tap; typed text is read back by the browser's speech voice.
- Three story kits (Lost Dog at the Farmers' Market, Science Fair Mix-Up, Snow Day). tool.json `modes: []`, `minutes: "25-40"`, `grades_label: "Grade 3"`.
- Saving: the strip and prose are kept in this browser through the comic-maker Store (IndexedDB), 6 stories at most; the footer says "Your stories stay on this device." `Clear my stories` removes them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.3.3a | Pick characters and a setting, then write an opening line of narration that names who and where | the opening box above panel 1's prose | 2, 5 |
| W.3.3b | Turn each bubble into a quoted line and write narration for each panel's action, thoughts and feelings | prose beside each panel | 3, 4 |
| W.3.3c | Use time words to move between panels (first, then, after that, later, finally) | time-word chips at the start of panel 2 to 4 prose | 4 |
| W.3.3d | Write a closing that wraps up the story | the closing box | 5 |
| L.3.2a | Type the title; the helper checks capitals on the important words | the title bar with a check | 2 |
| L.3.2c | The punctuation helper marks where quotation marks, the comma and the capital go in each dialogue line | small markers in the line | 3 |
| L.3.2d | Possessives on names (Rosa's dog, the judge's table) checked where the kit uses them | the apostrophe marker | 3 |

## Screens and modes
Header (kit): title "Dialogue Director"; `Kits`, `My stories`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A film set with a director's chair, a clapperboard, and Director Wren, a small wren in a beret. A four-panel strip waits on an easel. First hint: "Tap a story kit to pick your characters and setting." The first tap opens the kit with its line; the welcome is queued after it (`welcomeAfter: true`).

**Strip take.** Focus: a 4-grid strip (each panel 360 x 260). From the kit tray: two characters (each with 6 poses), a backdrop per panel, and props. Drag characters into panels, pick poses, add speech bubbles (tap a character, type up to 80 characters). A title bar sits above. Each panel's job is shown as a small card (1: meet them; 2: the problem; 3: try to fix it; 4: how it ends).

**Prose take.** Each panel sits beside a blank page. For each panel:
1. Narration box: "What happened in this picture?" The student types, using the panel as a guide.
2. Bubbles slide in as dialogue lines: the bubble text appears with an empty speaker tag; the student picks a said-word (said, asked, shouted, whispered) and the helper places markers where quotation marks, the comma or question mark, and the capital go. The student taps each marker to place it; the line is checked against the dialogue rule.
3. Panels 2 to 4: a time-word chip goes at the start.
`Check prose` lists notes in order: no opening; a panel with no narration; a dialogue line with missing marks; no time word; no closing.

**Listener test.** Mr. Pip, a turtle wearing a sleep mask, listens to the prose read aloud. For each panel, the kit has 1 or 2 key actions (data: "the dog runs off", "Rosa looks under the table"). If the panel's narration doesn't contain a key-action word group (generous word forms), Mr. Pip says "Wait, what happened?" and the panel lights. The story passes when every panel has its action and there's a closing.

**Print.** Strip and prose side by side.

At 1366x768 the panel and its page fit side by side; at 680x425 they stack.

## Content
Kits (written for Curio Class), each with 2 characters, 4 backdrops, 8 props, panel jobs and key actions:
- Lost Dog at the Farmers' Market: Rosa and her grandpa; Rosa's dog Pepper slips its leash; possessives: Rosa's dog, the baker's stand.
- Science Fair Mix-Up: Theo and Ms. Kim; two volcano models get switched; possessives: Theo's model, the judge's table.
- Snow Day: twins Ada and Ben; the sled goes missing; possessives: Dad's boots, the neighbor's yard.
Dialogue rule (American usage, as taught at grade 3): opening quotation mark before the first spoken word; the spoken words start with a capital; a comma (or question or exclamation mark) inside the closing quotation mark when a said-tag follows; a period after the said-tag. For tag-first lines: a comma after the tag, then the quotation.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Markers are 44 px targets placed in the gaps between characters; a wrong place says "Try the spot right before the first spoken word."
- The title check capitalizes first and last words and other words except short ones (a, an, the, and, but, or, of, in, on, at, to) and suggests, never forces.
- Typed narration is plain text, up to 400 characters per panel.

## Look
- Accent `--brand` #b23a1c film-set red (header, clapperboard, markers); gold #f4c542 (the lit panel, marker hits); paper #fdf6f3; ink #2a120b; muted #66514a. Scene: a warm film set with lights.
- Contrast (WCAG 2.1, computed): white on brand 5.97:1; brand on paper 5.59:1; ink on paper 16.52:1; muted on paper 6.92:1; ink on gold 10.85:1.
- Never color alone: markers show the actual mark (", ,, ?) and a word; the listener lights the panel and speaks.
- Different from this batch (cork brown, curtain plum, notecard green, blueprint blue).

## Art
- People art goes to Gemini: Rosa (a Latina girl about 8) and her grandpa; Theo (a Black boy about 9) and Ms. Kim (a Korean American teacher in her thirties); twins Ada and Ben (white, about 8) and Dad; 6 poses each (wave, point, surprised, worried, laugh, run), "illustrated children's comic character <description> <pose>, clean outlines, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): set (1), Director Wren (4 poses), Mr. Pip (3 poses), backdrops (12, "a farmers' market stall / a school gym science fair / a snowy backyard, flat comic style, no people, no text"; 13:10), props (24, sticker style).
About 85 images. Drawn in code: panels, bubbles, markers, pages.

## Voice
Bank voice `bright-teacher` as Director Wren (unique in this batch); `soft-breath` for Mr. Pip's few lines (unique in this batch). The student's prose is read by the browser speech voice. `Curio.voice` with `scope: () => state.kit + ':' + state.take + ':' + state.panel`, `welcomeAfter: true`.
- event `kit`: "{Lost Dog at the Farmers' Market}. Pick your poses!"
- how `welcome`: "Welcome to the set! First we make the comic. Then the prose take: we tell the same story in words, with no pictures at all."
- how `stripHow`: "Drag a character into the panel, pick a pose, then tap them to add a speech bubble."
- how `proseHow`: "Write what happened in this picture. Then place the marks for each line someone says."
- event `marker`: "Quotation marks hug the words someone says." / "The comma goes inside, before the closing mark."
- event `whatHappened` (Mr. Pip): "Wait, what happened?"
- event `wrap`: "That's a wrap! Your story stands on its own."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
comic-maker (`kit/comic-maker.js`), described in full in tools/my-story-strip/spec.md, exposed as `__tool.cm`. This tool uses: Strip (`4-grid`), Labels (bubble, caption), `cm.script(strip)` to list bubbles in panel order with speakers for the prose take, Jobs, Store, Print. Not Drawing or Audio (characters are posed art, not drawn). Posed-art panels are a small addition the engine description allows: a panel may hold `art:[{src, x, y, scale}]` instead of strokes.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Listener test | Paste the bubbles as narration | Bubbles rarely carry the key action; panels without the action word group still get "Wait, what happened?" |
| Listener test | Type the key words alone ("dog runs") | Passes that panel; the helper still asks for an opening, time words and a closing. The check is a nudge toward complete narration. |
| Dialogue marks | Tap every gap | Only the rule's gaps hold a mark; wrong gaps say where to look. |
| Title | Capitalize everything | Suggests lowercase for short words; not forced. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a kit: `kit`, `welcome` (queued, first time), `stripHow`.
2. Prose take: `proseHow`; marker hints: `marker`.
3. Listener test: prose read aloud, `whatHappened` at gaps, `wrap` at the end.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.3.3 and L.3.2 wording | thecorestandards.org, Writing and Language Grade 3 | CCSS ELA 2010 PDF | yes |
| In American usage, commas and periods go inside closing quotation marks; a comma separates a said-tag from the quote | Purdue OWL, quotation marks | The Chicago Manual of Style Online, quotation marks and punctuation (Q and A pages) | yes |
| Title capitals: first and last words and major words; short articles, conjunctions and prepositions lowercase | Purdue OWL, capitalization in titles | Merriam-Webster, title capitalization guide | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: people characters go to the fresh-agent review.

Checks run (Python, scratchpad b11, 2026-11-09): 3 kits by 4 panels each have 1 or 2 key actions; every possessive in the kits is a singular noun plus 's; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 a panel and its page fit side by side; at 680x425 they stack.
2. The title check suggests capitals. (L.3.2a)
3. Dialogue lines check marks and capitals, including possessives. (L.3.2c, d)
4. Narration and time words are prompted per panel. (W.3.3b, c)
5. Opening and closing are required by `Check prose`. (W.3.3a, d)
6. The listener test lights panels missing their key action.
7. Stories survive a reload where storage works; `Clear my stories` removes them.
8. Print shows strip and prose side by side.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: no clapperboard snap; no network requests.

## Open questions
- None for Cory.
