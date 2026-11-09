# Codex review: keyword-fishing

## Played

Cold as a Grade 4 student, then as a projecting teacher: all six levels and both modes before builder notes/source. Held-click solutions, removal, swaps, unknown words, all 30 fish, keyboard, grayscale and all required sizes. Best: big to size turns an empty lake into useful pages. Rich, inviting art retained.

## Findings fixed

- **Blocker, general, src.html lake (both modes):** stacked nonmatches covered fish targets. Responsive distinct targets now retain at least 44 pixels and painted 70/110-pixel fish. All 30 centers pass at every size; all 30 cards opened with real held taps.
- **Should fix, general, src.html positionSwaps (both modes):** choices appeared far away on the lake. Popup anchors to Swap, follows scroll/resize, fits phone and 680 preview, and keeps all choices visible.
- **Should fix, general, src.html syncAnswerFins (Levels):** Motion/resize erased answer fins while the bucket still marked answers. Fins now follow the current completed catch, including answers beyond the first twelve list entries.
- **Should fix, general, src.html changeLine (both modes):** a spoken result could continue after a line edit. Editing stops stale event speech while an active Read retains priority; unchanged voice text/manifest.
- **Should fix, general, notes.md Standards and sources:** full I.A.1 coverage was overstated and the AASL URL was dead. Notes state the limited alignment and link the current framework; no new topic/activity added.
- **Should fix, general, src.html lake caption (both modes):** displayed snippets could contain a word absent from the search index. Lake caption now states that only page-list words count; exact supplied content retained. Compact caption stays clear of fish.
- **Polish, general:** redistributed rejected fish, reserved a bobber window, clamped focused titles, added an empty-cast ripple, redrew the pail and cleaned cutout spill. No visual simplification.
- **Should fix, general, src.html popups and Free fishing:** audit-confirmed blank Add now prompts/focuses the field using the existing how-to. Compact answer labels stay on one line; card text clears Close. Nonmodal popup names and Close/return focus are explicit. Nine scoped follow-up shots pass, including 375, 680 and 800.

## Findings left

- **Blocker, general, spec conflict:** Level 5's cheapest sweep, how/Cast/Clear/cold/Cast, earns a sticker without demonstrating deliberate keyword choice. The spec explicitly accepts cold = M1/M6; Level 6 likewise accepts lava alone. Preventing this needs a changed goal or new assessment gate, both forbidden. Retained the specified exploratory model and documented the limitation instead of claiming mastery.
- **Should fix, general, standards/spec:** I.A.1 requires formulating questions; Levels supplies them. Notes corrected, but full alignment remains unearned. Moving the catalog code or adding a question-formulation activity exceeds the permitted scope.
- **Should fix, general, spec/model:** B1's displayed snippet says find, while find deliberately catches zero. The visible model explanation helps but does not turn this into realistic web search. A content/index change would contradict the specified checks.
- **Should fix, general, spec/layout tradeoff:** compact views disclose title tags on hover/focus beyond the spec's 680-only exception. All titles remain at least 12 pixels and all 30 page cards remain available by tap/keyboard. Simultaneous labels, 30 large fish and 44-pixel targets crowd the 220-pixel phone lake; retained legibility and rich fish rather than pretending strict always-visible tags pass. This needs a specification/layout decision.

## Break it

- **Live count:** all 25 specified catches independently recomputed, then exact IDs checked against the browser. All 22 little words preserve the count; five plural pairs match. No approximate/percentage meter or best score exists.
- **Stickers, Levels 1-6:** complete held-click solutions earned all six. Broad 30-page casts repeated five times award none; sweeping every Level 1 tile alone awards none. Level 3 hatchling catches T4 but awards no sticker because T3 is absent. Zero catches and interrupted casts award none.
- **Cheap later-level path:** physically ran Level 5's sweep and confirmed the spec-level blocker above. Single-word valid answers remain accepted as required. No claim that six stickers prove mastery.
- **Line/swap gates:** duplicate singular/plural blocked, eight distinct slots enforced, ninth rejected, every supplied swap exercised. Real jittered drags add/remove words. Unknown typed words remain tied on with zero fish; typed volcanoes catches four.
- **Free fishing:** no score/sticker, no answer marker, no reflection gate. Casting an unknown word stays empty. Saved level numbers survive a fresh tab; Clear/No preserves and Clear/Yes empties them. Denied storage does not break play.
- 79 focused core checks pass. Default sizes expose every fish center; page-tag overlays intentionally cover some fish until closed. No answer fin appears before a completed catch.

## Voice walk

Default Sound on, Motion on, held clicks at two-second intervals: stage, sea/turtles/eat/Cast; bats/food/Cast; remove lay and Florida/Cast; tortoises/big/Cast, select big/Swap/size/Cast; Mars/cold/Cast; volcano/lava/Cast; Free fishing, Space drawer, mars/cold/Cast.
Final main path log: w-levels, cast, solved, solved, full, swap, remove, solved, select, none, swapPick, solved, solved, solved, w-free, freeCatch. Both mode instructions heard once, all six stickers earned. Dropped intermediate how lines were heard later where still relevant. User actions can cut long result clips; no late mode welcome.

| Line/kind | Expected | Heard |
|---|---:|---:|
| Levels welcome | 1 | 1 |
| Free welcome | 1 | 1 |
| Cast/swap/swapPick how | 1 each | 1 each |
| Solved event, main walk | 6 | 6 |
| Little event, repeat test | 5 | 5 |
| Same how, repeat test | 1 | 1 |

Read with Sound off speaks the current hint/question. Mode changes drop old speech; line edits drop stale results without interrupting Read. Browser speech fallback remains: no Achird recordings were supplied or made.

## Facts checked

- **Model/numbers:** exact 30 fictional titles, sites, snippets and word lists match spec.md; all 25 catches, eight slots, 22 little words, plural approximation and three-fish target are model rules, not external facts. Evidence: review-independent-numbers.json and review-core-checks.json.
- **Standards:** question formulation versus identifying possible sources checked against [AASL's current learner framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf), I.A.1 and IV.A.2. The spec cites the 2018 edition; current framework retains those competencies. Coverage limitation named above.
- **Real search ranks using multiple signals:** [Google Search, ranking results](https://www.google.com/search/howsearchworks/how-search-works/ranking-results/). Notes correctly distinguish the toy every-word filter.
- **Turtle food/nesting topics:** [NOAA green turtle](https://www.fisheries.noaa.gov/species/green-turtle), [NOAA leatherback](https://www.fisheries.noaa.gov/species/leatherback-turtle), [Florida FWC sea-turtle FAQ](https://myfwc.com/research/wildlife/sea-turtles/florida/faq/). Seagrass/jellyfish diets differ by species; beach nesting is real. No husbandry or wildlife-handling advice is given.
- **Giant tortoises on islands:** [American Museum of Natural History, Galapagos giant tortoise](https://www.amnh.org/exhibitions/permanent/reptiles-amphibians/galapagos-giant-tortoise).
- **Bats use sound to hunt; fruit-eating bats exist:** [National Park Service, echolocation](https://www.nps.gov/subjects/bats/echolocation.htm) and [Virginia DWR, bat biology](https://dwr.virginia.gov/wildlife/bats/bat-biology-and-ecology/). No claim that all species hunt or roost alike.
- **Cricket's flat wooden blade:** [MCC, bat specifications](https://www.lords.org/mcc/the-laws/law-appendices). It is a genuine second meaning of bat.
- **Traditional fable identity:** [Library of Congress, The Hare and the Tortoise](https://www.read.gov/aesop/025). The tool only names a fictional retelling page; it makes no authorship or date claim and does not retell the story.
- **Volcano/magma/pressure/eruption:** [USGS, How Do Volcanoes Erupt?](https://www.usgs.gov/faqs/how-do-volcanoes-erupt). Titles/snippets describe topics; the tool provides no experiment or safety instructions.
- **Mars is cold/red, explored by rovers, named for a Roman god of war:** [NASA, Mars facts](https://science.nasa.gov/mars/facts/). Bakery, toys, crafts, menus, coloring pages, sites and the fable page are clearly fictional examples, not source endorsements or historical retellings.
- **Contrast recomputed:** white/brand 4.99, brand/paper 4.54, ink/paper 13.57, muted/white 6.76, focus/white 5.18, ink/tag 13.86. Grayscale retains numbers, words, stickers and visible focus.

## Sensitivity

Flag M3's Roman religious/mythological name and its neutral use as a meaning distractor for cultural review; also check T11's familiar fable title and B5's cricket vocabulary. NASA supports the Mars association. No people, stereotypes, hard history or European-contact dating. First-person dock art does not need a depicted angler.

## Flattest moment left

Once a student understands the fixed pond, repeating a cast adds little depth. The spec prohibits new topics/modes; retained the lake's live word experiments. Empty casts now have a visible ripple and less piled-up scenery.

## Graphics

Seven painted assets inspected separately and in final-size scenes. Redrew kf-bucket with the built-in imagegen tool; prompt and provenance saved in art/prompts.json, raw source in art/raw/kf-bucket.png. Original retained in Scratch. Re-keyed six cutouts with spill removal, no downloads or recordings. Full set remains one warm storybook style, no people, no missing art tokens.
Final bundle: 404450 bytes (395.0 KiB). Viewed all cold, size, functional, targeted, voice and comparison frames; review-feel-comparison.png places the tool beside Snowy Mail Route. Beat Lab also inspected. Scene/art retained or strengthened.

## Audit

Audit not finished: reached the 2400-second limit during per-control resize stress. Saved review-audit/audit.md has 175 leads and 58 frames, all inspected. Size/state, Motion off, both control walks, repeat and quick-tap stages completed; full resize coverage remains uncertified. No second audit was run.
Confirmed/fixed: blank Add feedback, compact answer-label wrapping and Close clearance, with popup semantics/focus improved. Other leads: intentional popup/modal coverage; compact crowded-school/count overlap with distinct tappable centers; pointer-events-none decoration misclassified as hidden text; long tackle-drawer scrolling; first-tap welcome skips permitted by BASELINE rule 16. The audit phone context failed, so separate real 375-pixel iframe checks provide that evidence. Diagnostic-host favicon 404s were separate from the offline bundle; the final nine hosted follow-ups are console-clean. Tree termination was denied; owned Chrome was closed directly and lingering preview servers were stopped. All 58 audit frames and all affected follow-up frames were opened. No blanket PASS claimed.

## Left open

The four spec-level findings above and browser fallback narration. No questions asked in this unattended run: followed the spec where its explicit content/goals conflicted with review demands. No shared source edits, git commits, new modes or topics. Temporary host removed and owned browsers/server closed. Report staged in Scratch until final writing to honor the immediate stop instruction. One cold review/fix pass, followed only by scoped re-checks and the single audit.
