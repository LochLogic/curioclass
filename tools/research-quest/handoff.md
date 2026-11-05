# Research Quest build handoff

## Structure

src.html starts from the kit starter. CSS lays out the illustrated parchment map, chapter card and research pack at actual viewport size. The JavaScript contains exact story data, voice lines, serializable run state, a pure council evaluator, chapter renderers and delegated input handlers. Artwork is referenced through one art table and art tokens. Curio.voice owns the narration queue; the tool owns the hint immediately on each state change.

## Tricky parts

- Council questions use the spec's exact presence, heading, source and plan-step tests. Question 4 selects the first note in visit order under What monarchs need, then the first outlined note elsewhere. Question 6 checks only outlined notes. Not needed never counts as outline evidence.
- A correct source quotation is allowed. Copying without quote marks fails question 4, including when it has a source.
- Rewind retains the reopened stop's choices and clears later choices. Revisiting Gather offers Redo note. No network calls or personal data.
- Choice order for paraphrases is shuffled once per run and persisted. The words, not answer labels, appear on screen.
- The chapter dominates the map; a short landscape view uses a dot strip and pack chip. Phones use a full-width card.
- Trail back buttons correspond to code-drawn paths and open read-only choice cards. Question 1 returns to Ask if the question is unsuitable, or Organize if the garden heading is the missing condition.

## Open questions and build decisions

The spec contains no explicit open-question section. Its leaning toward one continuous quest, no score, delayed story consequences and the five-stop map was followed. No topics or game modes were added. Three existing paintings were retained, nine missing paintings generated, and the blooming garden repainted to show recognizable milkweed. The source request for local FLUX was superseded by the owner's explicit image-tool instruction and CODEX-BUILD.md.

The source's migration distance is reproduced as a fictional video statement and qualified by the supplied good paraphrase. The planted garden is the story payoff, not a new planting simulator. Extra instructional how lines name enabled controls. Metadata credits both retained art and new art.

Compact organizer cards use deliberate excerpts with the full words in their title, the research pack, and Read. Short council layouts show slide headings; the full outline remains in the pack. At 760 wide the pack collapses below the stage; on phones the hint and pack stay in a fixed bottom bar, with Rewind and Start over available inside the pack. Trail lines recalculate their endpoints after layout and resize rather than relying on illustration coordinates.

The opening uses two large painted panels on laptops: the empty bed and the library desk. At the tightest landscape preview the brief is carried by the picture caption, question cards and reply so the next button stays clear. Phones retain the garden panel and the small desk beside the brief. Only the opening was re-shot at every required size after this art adjustment.

## Verification artifacts

Scratch: S:/CurioClass-codex/_scratch/research-quest. numbers.py and numbers.json contain the independent 200,000-run model and contrast checks. model-checks.json checks the shipped evaluator. student-run.json records a complete held-click run and narration. keyboard.json records a complete keyboard-only run. check_reload.py verifies reload, clear and zero external requests. Frame folders preserve initial size coverage and targeted fixes. The audit folder contains the final mechanical audit. No temporary scripts or screenshots are kept in the tool folder.

## Engine changes wanted

None in the kit. A possible audit-helper improvement, left outside this tool's write scope: in scripts/audit_tool.py, PAGE_JS, distinguish a path-only SVG group's accessible name from painted text, and use painted-path hit geometry instead of its rectangular group bounds for overlap leads. Preserve the HTML button and label checks. The Trail back's visible curves intersect by design; the wide, transparent hit paths are not rectangles drawn over labels.

## Audit dispositions

The one complete audit finished in about 27 minutes with 113 leads. Seven leads represented three concrete layout defects: two Ask overlaps at 680, the same shrinking pack question row in three 1280 states, and two undersized Yes targets. All were fixed and re-shot at the affected sizes. The full audit was not repeated.

The other 106 leads are explained in codex-report.md: four intentional note excerpts, one empty sixth-cell sample in the mobile plan-step grid reserved for Done, 97 SVG-path or nested-label geometry reports, and four expected welcome skips when the first question tap speaks its own reply. The full audit's repeated taps, focus and resize checks were clean. The final welcome guard for open dialogs and the four painted visit badges were verified separately. The pack list can scroll as a collection; the count chip opens the whole pack, and Gather also has four visit buttons on wide screens.

## Next work

The separate cold review is documented in codex-review.md. Narration recordings were intentionally not created. No commits or additional polish round.

## Cold review changes, 2026-10-31

The cold review used ports 9960/9961 and host 8765. Its evidence is under _scratch/research-quest/review-*. The council evaluator and all specified outcomes remain intact. Organize now prioritizes the selected-note instruction over Done, with state-specific queued-line validity. Nested pack cards preserve the original focus anchor. Read uses rendered text boundaries so adjacent headings and answer letters are not joined into words.

Trail back keeps its map and every route. Focusing or hovering a question isolates that route and its stop; wide cards and read-only cards show the actual evidence choice. Compact cards keep the short question labels. traceEvidence supplies these descriptions, and highlightTrace controls only presentation.

The inherited caterpillar was replaced using the built-in image generation tool, then processed with art.py --rekey. The prompt is in art/prompts.json and the raw painting in art/raw/rq-caterpillar.png. Two local FLUX paintings remain. See codex-review.md for the final audit disposition and any limitations.

The review audit completed in 1,797 seconds with 124 leads. Its frames exposed a compact ending image extending under the footer status and populated organizer grids growing into the plan-step label; explicit shrinking grid rows now keep both within their reserved space. Compact heading source names have titled ellipses. The audit also caught focus falling to the page during a nested-card transition; openDialog now focuses the first live control after replacing content. All three endings and three/four-note organizer headings were rechecked at 680, 800 and 1000 widths; nested-card focus and Enter-to-return passed all eight standard sizes. No full audit rerun.
