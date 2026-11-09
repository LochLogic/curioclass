# Summary Scaffold

## One idea
The student summarizes a short informational article for Theo, a classmate who was out sick: they mark the central idea (two at grade 7) and the supporting ideas, link each supporting idea to the lines that develop it on an organizer, then write the summary with citation frames (According to..., The author explains...), while the tool flags opinion words, strings of five or more words copied from the article, and supporting ideas left out, and Theo's reply shows what he now knows, so the student learns to summarize objectively and report what an author says.

## Not like
- research-notebook (9, spec): synthesis across many sources. Here one article, summarized.
- fact-fusion (5, concept): combining three sources into a report. Here one source, made shorter.
- main-idea-pinboard (3-5, spec): pinning details to a main idea. Here central ideas, citation frames and paraphrase for grades 6 to 8.
- cer-builder (6-8, spec, this batch): your own claim from your own data. Here an author's ideas in your words.
- perspective-frames (6-8, spec): comparing several speakers. Here reporting one author faithfully.

## Who and how
- Grades 6 to 8, English Language Development with Reading Informational Text, module "Summarizing and Citing". Standards: WIDA ELD-LA (Standard 2, the language of language arts), Inform key language use (WIDA 2020); RI.6.2, RI.7.2, RI.8.2.
- Driver: one student; class mode is "Which summary?", where the projector shows two summaries of one article and the class finds the opinion word, the copied string or the missing idea (tool.json `driver: "student"`). The article reads aloud on tap, with key words glossed.
- Grade setting: 6 (one central idea, objective summary), 7 (two central ideas and how each develops), 8 (the central idea and how supporting ideas relate to it). Help setting: Lots (candidate sentences highlighted, full frames), Some (frames with word banks), Little (frame starters, then typing). Teacher notes map them to WIDA 1-2, 3-4 and 5-6. tool.json `modes: ["Summarize", "Which summary?"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the organizer and the summary.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.6.2, RI.7.2, RI.8.2 (central ideas) | Mark the central idea (two at grade 7) in the article | the marked lines | 2 |
| RI.6.2 (details convey it), RI.7.2 (development), RI.8.2 (relationship to supporting ideas) | Link each supporting idea to its lines on the organizer and, at grade 8, label the relationship (cause, example, contrast, result) | the organizer branches with threads to the text | 3 |
| RI.6.2, RI.7.2, RI.8.2 (objective summary) | Write the summary; opinion words are flagged | flags on the draft | 4 |
| WIDA ELD-LA (reporting an author's ideas) | Use citation frames and academic reporting verbs (explains, describes, argues, shows) | the frame bank | 4 |
| WIDA Inform (concise and complete) | Fix copied strings and missing ideas | the empty branch; the copied-string flag | 4 |

## Screens and modes
Header (kit): title "Summary Scaffold"; `Mark`, `Organize`, `Write`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school library table with the article on one side and a phone on the other showing a text from Theo: "I missed this one. What's it about?" First hint: "Tap the article title to hear it." The first tap reads the title and first paragraph; the welcome is queued after it (`welcomeAfter: true`).

**The articles.** Three articles written for Curio Class, about 450 to 600 words each, with a source line:
- Grade 6: "House Hunters with Wings": when a honeybee colony swarms, 20 to 50 scout bees search for a new home, report back with a dance, and the swarm chooses.
- Grade 7: "Cooler Streets": cities are often warmer than the land around them (two central ideas: why cities trap heat, and how trees and green space cool them through shade and evaporation).
- Grade 8: "Why Mars Is Red": iron oxide dust covers the surface, and dust storms spread and lift it; supporting ideas relate as cause, evidence and result.

**Mark.** The student marks the central idea and supporting ideas by tapping sentences. At Lots help, candidate sentences glow faintly.

**Organize.** The central idea sits in the middle (two at grade 7), supporting ideas around it, each linked to its lines by a thread to the article. At grade 8 each branch gets a relationship label. A key idea not yet placed shows as an empty branch.

**Write.** The summary is built from frames: "According to ___, ___." "The author explains that ___." "The article also describes ___." "Overall, ___." Checks run as the student writes:
- opinion words (amazing, I think, the best, cool, boring) are flagged "Is that the author's idea or yours?";
- a string of five or more words copied from the article is flagged "Put it in your own words, or use quotation marks.";
- a supporting idea left out keeps its empty branch.
When the summary passes, every sentence threads to its source lines, and Theo replies with what he now knows, in his own words. If an idea is missing, Theo asks about it ("Wait, how do they pick one?").

**Which summary?** On the projector, two summaries for the class to judge.

At 1366x768 article and organizer fit side by side; at 680x425 they are tabs.

## Content
- Three articles, glossaries, keyed central and supporting ideas, frames and Theo's replies written for Curio Class from the Sources table; each article's facts are backed twice.
- The opinion word list and the copied-string rule (five words) are shown to teachers in the notes.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Marks, branches and sentences can be changed any time; checks update at once.
- With Motion off threads appear without drawing and Theo's message appears without sliding in.

## Look
- Accent `--brand` #6b2d5c library plum (header, organizer center, frames); gold #f4c542 (threads, marked lines); paper #f9f1f7; ink #260d20; muted #64525f. Scene: a library table with an article and a phone.
- Contrast (WCAG 2.1, computed): white on brand 9.74:1; brand on paper 8.79:1; ink on paper 16.33:1; muted on paper 6.50:1; ink on gold 11.12:1.
- Never color alone: flags show a symbol and words; threads are listed as text too.
- Different from this batch (plaza green, rally red, lab blue, playroom orange).

## Art
- People art goes to Gemini: Theo (an Ethiopian American boy about twelve, at home on a couch with a blanket and a phone), 4 poses (asking, reading, thinking, thumbs up); "illustrated middle school boy at home sick <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the library table (1); one picture per article (a bee swarm on a branch, a shady tree-lined street, the red surface of Mars) (3).
About 8 images. Drawn in code: organizer, threads, flags.

## Voice
Bank voice `news-reader` as the hint voice and the article reader (unique in this batch); Theo is read by `casual-peer` (unique in this batch). `Curio.voice` with `scope: () => state.article + ':' + state.view`, `welcomeAfter: true`.
- how `welcome`: "Theo missed this article. Find the central idea and the ideas that support it, then tell him what it's about in your own words."
- event, whole, `para`: the tapped paragraph.
- event `opinion`: "Is that the author's idea or yours?"
- event `copied`: "Put it in your own words, or use quotation marks."
- event `missing`: Theo's question about a missing idea.
- event, whole, `summary`: the summary read back, then Theo's reply.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
research (`kit/research.js`, `R`), described in full in tools/question-sharpener/spec.md. This tool uses: Source (one article with segments), Shelf and Reader (`R.reader` for marking sentences), Note and `R.closeness` (copied run of 5 flags), Board as the organizer (`R.board` with an empty-branch readout), Trace (`R.trace` for summary sentences) and Cite (`'simple'`). Not Conflicts, Weight, Matrix, Question or Store. The opinion-word check, grade settings and Theo's replies are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Central idea | Mark the first sentence | Each article's keyed central idea is not its first sentence. |
| Copying | Paste article sentences | `R.closeness` flags any run of five or more words. |
| Complete | Write one sentence | Each keyed supporting idea needs a sentence threaded to its lines. |
| Objective | Add "I think" | Opinion words are flagged until removed. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the title: `para` (whole), `welcome` (queued, first time).
2. Write: `opinion`, `copied` and `missing` as they fire.
3. Pass: `summary` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.2, RI.7.2, RI.8.2 wording | thecorestandards.org, Reading Informational Text grades 6, 7, 8 | CCSS ELA 2010 PDF | yes |
| WIDA 2020: Standard 2 is the language of language arts; Inform covers reporting and summarizing | WIDA ELD Standards Framework, 2020 Edition | WIDA, Key Language Uses: A Closer Look (2020) | yes |
| A swarm sends out 20 to 50 scout bees to find a new home; scouts report sites with a dance and the swarm chooses one | Wikipedia, Swarming (honey bee) (checked 2026-11-09) | Seeley, Honeybee Democracy (Princeton University Press, 2010) | yes |
| US cities are often 1 to 7 °F warmer than nearby areas by day; trees and green space cool through shade and evaporation | Wikipedia, Urban heat island (checked 2026-11-09) | US EPA, Heat Island Effect | yes |
| Mars looks red because its surface is covered in iron(III) oxide dust; dust storms lift and spread it | Wikipedia, Mars (checked 2026-11-09) | NASA Science, Mars facts | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b28, 2026-11-09): the saved pages contain "20 to 50 scout bees", "warmer than the surrounding area by about 1–7", "evaporative" cooling and "iron(III) oxide"; the copied-string check flags a five-word run from a test article and passes a paraphrase; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 article and organizer fit; at 680x425 they are tabs.
2. Central ideas are marked per grade setting. (RI.6.2, RI.7.2, RI.8.2)
3. Supporting ideas link to their lines; grade 8 labels relationships. (RI.6.2, RI.7.2, RI.8.2)
4. Opinion words, copied strings and missing ideas are flagged; frames use reporting verbs. (WIDA ELD-LA, Inform)
5. The passing summary threads every sentence, and Theo replies.
6. Help levels behave as in Who and how.
7. Which summary? and Print work.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: threads and messages appear without motion; no network requests.

## Open questions
- Home-language support: home-language glossaries for ELD frames (Cory's open question in RUNBOOK.md)? (default used: English only, with pictures and read-aloud)
