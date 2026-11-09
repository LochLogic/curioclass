# Linked Feature

## One idea
The student writes a web feature for a school news site, three pages long, typed in one sitting with a page counter and a keyboarding pace bar; they link each claim to a source page from a small offline library and cite it, draw a linked diagram that shows how their ideas connect, answer an editor's margin comments, and keep a routine of short daily quick-writes beside the long piece, so they learn that writing online means linking and citing, showing connections, working with an editor, and writing often.

## Not like
- explainer-studio (7, concept): the content of an explainer. Here publishing, linking and the writing routine.
- explainer-sections (6-8, spec): section structure. Here linking, citing and diagramming online.
- draft-versus-draft (6-8, spec): comparing revisions for a reader. Here an editor's comments on the student's piece.
- research-rover (4, spec): gathering notes. Here linking finished claims to sources.
- fact-fusion (5, spec): combining three sources. Here a published feature with links.

## Who and how
- Grades 6-8, ELA, module "Writing and Publishing Online" (Writing). Standards: W.6.6, W.7.6, W.8.6, W.6.10, W.7.10, W.8.10.
- Driver: one student (tool.json `driver: "student"`). Every card and comment is read on tap; the student's text is read back by the browser's speech voice.
- Three feature topics, each with an offline source library of 5 pages: "Why Do Cities Plant Street Trees?", "How Do Animals Find Their Way Home?", "What Happens to Our Recycling?". tool.json `modes: ["Feature", "Quick-writes"]`, `minutes: "45-60 per sitting; 5 per quick-write"`, `grades_label: "Grades 6-8"`.
- Saving: the feature, quick-writes and the routine log are kept in this browser; footer: "Your writing stays on this device. Nothing is posted." `Clear my writing` removes it. `Save as web page` gives the student an HTML file of the finished feature.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.6.6 (keyboarding) | Type the feature in one sitting; a page counter reaches three pages (about 750 words at 250 words a page) | the page counter and pace bar | 2 |
| W.7.6 (link and cite) | Select a claim, link it to a source page, and cite it in the sources list | linked words and the sources list | 3 |
| W.8.6 (relationships) | Draw a linked diagram: idea boxes and labeled arrows (causes, is part of, is an example of, answers) | the diagram beside the feature | 4 |
| W.6.6 to W.8.6 (collaborate) | Answer each editor's margin comment by changing the text or replying with a reason | comments marked resolved or answered | 5 |
| W.6.10 to W.8.10 | Keep daily quick-writes (5 minutes, prompts) and the long feature; the routine log shows both | the routine log calendar | 6 |

## Screens and modes
Header (kit): title "Linked Feature"; `Feature`, `Sources`, `Diagram`, `Quick-writes`, `Log`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A newsroom desk with a laptop showing a blank feature page, a pinned assignment note ("Three pages by Friday") and Editor Dana Brooks's coffee mug and red pen. First hint: "Tap a topic card to open its sources." The first tap reads the topic's name; the welcome is queued after it (`welcomeAfter: true`).

**Sources.** Five short pages per topic (each 300 to 500 words, written for Curio Class from sourced facts, each with a title, a made-up site name labeled "practice site", an author or group and a date), shown in a mock browser frame. No real web pages load.

**Feature.** A writing page with a headline, a dek and body text; a page counter (words divided by 250) and a pace bar (words per minute this sitting, shown for the student, not scored). The sitting timer starts with the first keystroke and pauses after 5 minutes idle. A "Three pages in one sitting" badge appears when the counter passes three pages within one sitting.

**Link and cite.** Select words, tap `Link`, pick a source page and the paragraph that backs it; the words become a link (underlined, with a source number). The sources list builds itself (title, site, author or group, date). A claim with a number and no link gets a margin dot: "Where is this from?"

**Diagram.** Idea boxes (from the student's headings or typed) and arrows with labels from a list. The diagram must connect every heading. It prints beside the feature and saves into the web page file.

**Editor's comments.** After the student taps `Send to editor`, Dana leaves 5 to 7 margin comments by rules: a number with no link, a heading that doesn't match its section (shares no content words), a paragraph over 150 words, a missing conclusion, a link to a source that doesn't back the claim (the paragraph the student picked is rated 0 for that claim in data), plus one compliment. The student resolves each by changing the text (the rule rechecks) or replies with a reason (at least 8 words), which marks it answered.

**Quick-writes.** A 5-minute timer and a daily prompt (30 prompts, such as "Describe a sound you heard today that nobody else noticed."). Nothing is checked but the minutes.

**Log.** A calendar of the student's sittings and quick-writes: minutes and words per day.

At 1366x768 the feature and sources fit side by side; at 680x425 sources are a tab.

## Content
Written for Curio Class:
- Three topics with five practice-site pages each, from sourced facts (Sources table): street trees (shade lowers surface temperatures; trees take up stormwater); animal homing (homing pigeons, sea turtles using Earth's magnetic field, salmon smelling their home streams); recycling (sorting at a materials recovery facility; contamination).
- Editor rules and comment wording; 30 quick-write prompts.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typing is never interrupted by sound; comments are read only on tap.
- The web page file contains the feature, the diagram as inline SVG and the sources list, and no scripts.
- With Motion off the counter and pace bar update without animation.

## Look
- Accent `--brand` #0f6f5a web green (header, links, the counter); gold #f4c542 (badges, resolved comments); paper #f1f8f6; ink #08251e; muted #4a5e58. Scene: a sunny school newsroom.
- Contrast (WCAG 2.1, computed): white on brand 6.10:1; brand on paper 5.67:1; ink on paper 15.07:1; muted on paper 6.43:1; ink on gold 9.98:1.
- Never color alone: links are underlined with numbers; comments show words.
- Different from this batch (editor's red, blueprint blue, lilac, lamp amber).

## Art
- People art goes to Gemini: Editor Dana Brooks (a Black woman in her thirties with locs, reading glasses on her head, red pen), 4 poses; "illustrated newsroom editor <pose>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): newsroom desk (1); topic pictures (3): "<a shady tree-lined city street / a sea turtle swimming / a recycling sorting line with no people>, realistic illustration, no text"; 4:3.
About 8 images. Drawn in code: browser frame, diagram, log calendar.

## Voice
Bank voice `news-reader` as Editor Dana Brooks (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.item`, `welcomeAfter: true`.
- how `welcome`: "Three pages, linked and cited, by Friday. Read your sources, then start typing."
- event, whole, `para`: the tapped source paragraph.
- event `noLink`: "Where is this from? Link it to a source."
- event `comment`: the editor's comment.
- event `resolved`: "Fixed. Thanks."
- event `pages`: "Three pages in one sitting. Nice work."
- how `quickHow`: "Five minutes. Write without stopping."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: writing page with counter and sitting timer, link picker, sources list, diagram editor, editor rules, quick-write timer, log. (The research family's notes and boards aren't needed; links point at whole paragraphs.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Three pages | Paste text | Pasting is allowed but the page counter counts only typed words in the sitting. |
| Links | Link every claim to page 1 | Links to paragraphs rated 0 for that claim bring an editor comment. |
| Diagram | Draw unlabeled arrows | Arrows need a label from the list, and every heading must connect. |
| Comments | Reply "ok" | Replies need 8 words or a text change the rule rechecks. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a topic card: its name, `welcome` (queued, first time).
2. Sources: `para` (whole). Feature: `noLink` on tap of a margin dot.
3. Send to editor: `comment` on tap; `resolved` as they clear; `pages` at three.
4. Quick-writes: `quickHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.6 to W.8.6 and W.6.10 to W.8.10 wording, including three pages in a single sitting | thecorestandards.org, Writing Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Street trees shade surfaces and lower surface temperatures, and take up stormwater | US EPA, using trees and vegetation to reduce heat islands | USDA Forest Service, urban forests | yes |
| Sea turtles use Earth's magnetic field to find their way, and salmon use smell to find their home streams | NOAA Fisheries, sea turtle navigation | US Fish and Wildlife Service, salmon life cycle | yes |
| Recyclables are sorted at materials recovery facilities, and food and liquids contaminate recycling | US EPA, how do I recycle common recyclables | US EPA, materials recovery facilities | yes |
Backed twice: 4. Cut: 0.

Design choices (not claims): 250 words a page; the editor's rules.

Checks run (Python, scratchpad b17, 2026-11-09): the sample editor rules flag a 160-word paragraph and an unlinked number and pass an 8-word reply; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the feature and sources fit; at 680x425 sources are a tab.
2. The counter and sitting timer show three pages in one sitting from typed words. (W.6.6)
3. Links and the sources list work. (W.7.6)
4. The diagram connects every heading with labeled arrows. (W.8.6)
5. Editor comments fire by rule and resolve by change or reply. (W.6.6 to W.8.6)
6. Quick-writes and the log record minutes and words. (W.6.10 to W.8.10)
7. Writing survives a reload where storage works; `Clear my writing` removes it; `Save as web page` gives an HTML file with no scripts.
8. Print shows the feature, diagram and sources.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: counters update without animation; no network requests.

## Open questions
- None for Cory.
