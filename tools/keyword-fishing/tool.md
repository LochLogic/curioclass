# Keyword Fishing: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: keyword-fishing

#### Built

Offline Grades 3-5 lake puzzle with the exact 30 fictional pages, six levels, Free fishing, eight line slots, every supplied swap, typed words, live matching, clickable fish tags, pail reel-in and saved level stickers. Seven generated paintings. Kit frame, voice, Motion, Sound and Read. Build only; no commits or polish round.

#### Numbers check

PASS: prepare.py independently reproduced all 25 stated catches, all 22 little words and 30 pages before building. core-results-fixed.json compares exact IDs against the bundled __tool.catch API. The browser also checks five plural pairs and every listed swap.
Source-note discrepancy: later exhaustive enumeration found 31 one-to-three-word Level 1 solutions with the listed swaps, versus its stated four. Four is the original-tiles-only count. Level 4 has the stated 11 with swaps; the other levels have 82, 59, 51 and 38, all above the stated 27 minimum. solution-counts.json records both counts. No spec or content was changed. This broader enumeration happened during verification, not before the first build.
Contrast checks: white/brand 4.99, brand/paper 4.54, ink/paper 13.57, muted/white 6.76, focus/white 5.18, ink/fish-tag 13.86, Cast text/gold 7.37. Header focus is white.

#### Feel check

Best moment: Level 4's zero catch opens back up when big is swapped for size, then a successful cast gives the answer page a gold fin and a saved fish sticker.
Flat moment 1: the first cast only lifted fish inside the lake. Changed it to send painted fish across the scene into the pail, with a small pail landing response. Word controls stay live throughout.
Flat moment 2: broad schools made compact title tags pile up. Changed narrow crowded schools and away fish to reveal tags on focus/hover; tapped cards retain the full title, site and snippet. The empty lake now leaves the bobber and count clear.
Played all six levels through held clicks, then Free fishing, unknown words and keyboard use. Compared feel-comparison.png with Snowy Mail Route and inspected Beat Lab. The painted lake, fish, glints and reel-in meet the visual bar. Depth comes from six distinct search problems; Free fishing remains a small fixed pond.

#### Done when

1. PASS: all 25 supplied catches and exact IDs match __tool.catch; each tested cast bucket matches its snapshot. numbers.json and core-results-fixed.json.
2. PASS: count and CSS targets update synchronously; 550 ms transitions re-aim from current positions. Calm snaps immediately. storage-resize-results.json includes before/after positions.
3. PASS: six real held-click solutions earned all six stickers. Earned numbers survived reload; No retained them and Yes cleared them. student-run.json and storage-resize-results.json.
4. PASS: all little words together catch 30; every little word preserves the two-fish sea/eat catch; adding one shows Same fish. core-results-fixed.json.
5. PASS: Level 3 starts with eight words and zero fish. lay selection enables removal and swap. Every listed replacement was exercised; words without swaps disable Swap. core-results-fixed.json.
6. PASS: typed moonstone remains on the line, empties the lake and shows the required message. Typed volcanoes catches four. unknown.json and core-results-fixed.json.
7. FAIL strictly for unobstructed pointer coverage: all 30 card contents were checked, and real Enter on T1 opens its card. Tags are at least 12 px. Crowded fish and banked nonmatches overlap, so some pointer hit areas are covered in tight views. All remain keyboard buttons. Narrow/away tags reveal on focus/hover beyond the spec's 680-only exception.
8. PASS: lake occupies 60 percent of the main width at 1280, 1366 and 1920; bobber center is 50/50. Size JSONs and inspected frames.
9. PASS: adding a word 80 ms into a cast immediately cancels it, changes the catch and prevents stale completion. Real drags on/off work. core-results-fixed.json, cancelled-cast-label.json, drag-on.json and drag-off.json.
10. PASS for primary controls: one full size sweep covered every specified size in both modes, including the real 375x812 iframe. Targeted checks cover the compact full line, Free fishing, swaps, wrong small catch and phone unknown-word state. Questions, line, tiles and Cast remain visible without page scrolling. final-summary.json and phone state JSONs.
11. PASS for targeted queue checks: voice-final-two-second.json shows one how line, two solved-event starts and Read priority with held taps at 2 s. Sound-off checks use no heard lines. All 19 runtime lines match lines.json. Final prompts ask for selection before naming enabled Remove/Swap controls, following STANDARDS over literal spec wording. No browser console errors in drive batches; no external requests or exceptions in storage/resize checks. The full audit did not complete.

#### Wave lessons

- Hint and voice: PASS, hint updates synchronously; V.heard chooses how lines; result speech takes priority over an unfinished how line; Read retains priority. Literal spec feedback that named disabled controls was replaced by selection-first prompts, with enabled-control instructions after selection. Solved feedback names the next level control.
- Focus and layout: PASS in keyboard solve, swapping and removal; restored focus uses preventScroll. Selection does not rebuild a word under the pointer. Hint has reserved minimum height. Swap choices moved onto the lake to leave the hint uncovered.
- Sizes: FAIL strictly for exposed fish hit areas in crowded scenes; PASS for primary 44 px controls, reserved hints and every required viewport. Final targeted measurements have no small targets or hidden primary controls. Long drawer lists scroll independently; compact buckets collapse to counts.
- No giveaways: PASS within this live-preview design. Answer fins and stickers appear only after a cast. A small wrong catch still fails the question. Fish titles/snippets are intentionally inspectable in the spec.
- Honest numbers: PASS, on-screen fish are explicitly 30 made-up pages; notes explain every-word matching, the plural approximation and the fictional three-fish goal.
- Standards: PASS within the spec's given-question scope. Students select searchable words and identify possible pages. Notes distinguish this from full source reading/evaluation. No family engine is named.
- Motion off: PASS, zero infinite animations; instant re-aiming and immediate cast result. All generated art is present.
- Short choice sets: PASS for level numbers, level tiles and swap words; drawer word lists contain the complete vocabulary and intentionally scroll. All five drawer tabs stay visible.
- Resize mid-animation: PASS, a cast completed after flipping to 760x900; no exceptions or stuck casting flag.
- Delayed welcome: PASS in held-tap logs; first tile's own how line supersedes the now-stale welcome. Mode welcomes use Curio.voice, not welcomeAfter.
- Unknown as unknown: PASS, unknown typed words say no fish know them and stay tied on with a zero catch.
- One look, one meaning: PASS, four painted topic kinds retain their identity; dim edge fish are nonmatches, gold fins explicitly say Answers it.
- Badge truth: PASS, Nibble count is the live exact catch; bucket is the last completed cast. Cancelled casts no longer leave Reeling in.
- Reversible hint: PASS, modes, drawers, line edits, swaps, casts and clearing set the current next-action hint immediately.
- No answer by copying words: PASS with the intended keyword lesson. Tiles are deliberately taken from the given question; dead words, alternate words and wrong small catches prevent blindly copying the whole question from solving it.

#### Audit leads

Audit not finished. It was run once on port 9991, host 8795, and stopped at its 40-minute limit. It saved 58 frames but no audit.md, so there is no completed lead list or certification of its full walk/repeat/resize checks. The process tree was stopped and both ports closed.
Confirmed during frame inspection and targeted PAGE_JS checks: short targets fixed; selected compact word/caption overlap fixed; popup fitting fixed; fixed popup moved out of its scroll-panel ancestor; inactive-control prompts fixed; mid-cast Motion off removes moving copies. Final five measured states have no non-fish UI leads in final-summary.json.
Remaining fish/fish overlaps and covered banked fish are real clustering, not silently dismissed as clean geometry. The popup intentionally covers background fish. Those items remain for cold review; strict all-fish pointer coverage is marked FAIL above. The full audit was not repeated.

#### Frames looked at

58 build/reference PNGs: bar-frames 2, early-frames 4, functional-frames 7, late-frames 8, size-frames 19, targeted-frames 7, post-frames 7 and final-frames 4. Also art-contact.png and feel-comparison.png. All 58 audit PNGs were inspected through audit-contact-008 through audit-contact-058, eight sheets. Older frames preserve repaired defects; final-frames and the targeted JSONs show the final repairs.

#### Art made

Seven new gpt-image paintings: misty lake/dock, orange fish, violet fish, coral fish, blue fish, red/white bobber and tin pail. Each was processed only with art.py --rekey and inspected in contact view and in play. No redraw was needed. Art 232.3 KB; final bundle 398,648 bytes (389.3 KB). Code preview.svg was also made and inspected.

#### Art still to paint

None. No people. Recorded narration was explicitly outside this build.

#### Engine changes wanted

None required.

#### Left open

The full mechanical audit timed out and produced no audit.md. Dense fish/bank overlap leaves some pointer targets covered; keyboard access remains. Fish gather at fixed target positions with gentle swim loops rather than continuous orbital paths. Narrow crowded and away fish expose title tags on focus/hover; full cards remain available. Browser speech is used, not recorded Achird clips. Compact bucket contents are hidden beyond their count as specified. The general equal-time motion guideline conflicts with the spec's explicit instant calm cast; the latter was followed for this brief preview action. No live classroom or listening review.
The report was kept in Scratch until all checks completed because the user required stopping immediately when the report is written. The two reference tools were bundled only in Scratch copies, honoring the write boundary.
The index is the supplied Words column, not displayed snippets. B1's snippet contains find while its index does not, so find correctly catches zero under the spec. Teacher notes explicitly identify this model limitation. Snippet and index data were retained.

Cleanup: owned Chrome/server processes closed; 9990, 9991 and 8795 checked closed. host.html removed. No commits, branch changes, shared-source edits or polish round.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: keyword-fishing

#### Played

Cold as a Grade 4 student, then as a projecting teacher: all six levels and both modes before builder notes/source. Held-click solutions, removal, swaps, unknown words, all 30 fish, keyboard, grayscale and all required sizes. Best: big to size turns an empty lake into useful pages. Rich, inviting art retained.

#### Findings fixed

- **Blocker, general, src.html lake (both modes):** stacked nonmatches covered fish targets. Responsive distinct targets now retain at least 44 pixels and painted 70/110-pixel fish. All 30 centers pass at every size; all 30 cards opened with real held taps.
- **Should fix, general, src.html positionSwaps (both modes):** choices appeared far away on the lake. Popup anchors to Swap, follows scroll/resize, fits phone and 680 preview, and keeps all choices visible.
- **Should fix, general, src.html syncAnswerFins (Levels):** Motion/resize erased answer fins while the bucket still marked answers. Fins now follow the current completed catch, including answers beyond the first twelve list entries.
- **Should fix, general, src.html changeLine (both modes):** a spoken result could continue after a line edit. Editing stops stale event speech while an active Read retains priority; unchanged voice text/manifest.
- **Should fix, general, notes.md Standards and sources:** full I.A.1 coverage was overstated and the AASL URL was dead. Notes state the limited alignment and link the current framework; no new topic/activity added.
- **Should fix, general, src.html lake caption (both modes):** displayed snippets could contain a word absent from the search index. Lake caption now states that only page-list words count; exact supplied content retained. Compact caption stays clear of fish.
- **Polish, general:** redistributed rejected fish, reserved a bobber window, clamped focused titles, added an empty-cast ripple, redrew the pail and cleaned cutout spill. No visual simplification.
- **Should fix, general, src.html popups and Free fishing:** audit-confirmed blank Add now prompts/focuses the field using the existing how-to. Compact answer labels stay on one line; card text clears Close. Nonmodal popup names and Close/return focus are explicit. Nine scoped follow-up shots pass, including 375, 680 and 800.

#### Findings left

- **Blocker, general, spec conflict:** Level 5's cheapest sweep, how/Cast/Clear/cold/Cast, earns a sticker without demonstrating deliberate keyword choice. The spec explicitly accepts cold = M1/M6; Level 6 likewise accepts lava alone. Preventing this needs a changed goal or new assessment gate, both forbidden. Retained the specified exploratory model and documented the limitation instead of claiming mastery.
- **Should fix, general, standards/spec:** I.A.1 requires formulating questions; Levels supplies them. Notes corrected, but full alignment remains unearned. Moving the catalog code or adding a question-formulation activity exceeds the permitted scope.
- **Should fix, general, spec/model:** B1's displayed snippet says find, while find deliberately catches zero. The visible model explanation helps but does not turn this into realistic web search. A content/index change would contradict the specified checks.
- **Should fix, general, spec/layout tradeoff:** compact views disclose title tags on hover/focus beyond the spec's 680-only exception. All titles remain at least 12 pixels and all 30 page cards remain available by tap/keyboard. Simultaneous labels, 30 large fish and 44-pixel targets crowd the 220-pixel phone lake; retained legibility and rich fish rather than pretending strict always-visible tags pass. This needs a specification/layout decision.

#### Break it

- **Live count:** all 25 specified catches independently recomputed, then exact IDs checked against the browser. All 22 little words preserve the count; five plural pairs match. No approximate/percentage meter or best score exists.
- **Stickers, Levels 1-6:** complete held-click solutions earned all six. Broad 30-page casts repeated five times award none; sweeping every Level 1 tile alone awards none. Level 3 hatchling catches T4 but awards no sticker because T3 is absent. Zero catches and interrupted casts award none.
- **Cheap later-level path:** physically ran Level 5's sweep and confirmed the spec-level blocker above. Single-word valid answers remain accepted as required. No claim that six stickers prove mastery.
- **Line/swap gates:** duplicate singular/plural blocked, eight distinct slots enforced, ninth rejected, every supplied swap exercised. Real jittered drags add/remove words. Unknown typed words remain tied on with zero fish; typed volcanoes catches four.
- **Free fishing:** no score/sticker, no answer marker, no reflection gate. Casting an unknown word stays empty. Saved level numbers survive a fresh tab; Clear/No preserves and Clear/Yes empties them. Denied storage does not break play.
- 79 focused core checks pass. Default sizes expose every fish center; page-tag overlays intentionally cover some fish until closed. No answer fin appears before a completed catch.

#### Voice walk

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

#### Facts checked

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

#### Sensitivity

Flag M3's Roman religious/mythological name and its neutral use as a meaning distractor for cultural review; also check T11's familiar fable title and B5's cricket vocabulary. NASA supports the Mars association. No people, stereotypes, hard history or European-contact dating. First-person dock art does not need a depicted angler.

#### Flattest moment left

Once a student understands the fixed pond, repeating a cast adds little depth. The spec prohibits new topics/modes; retained the lake's live word experiments. Empty casts now have a visible ripple and less piled-up scenery.

#### Graphics

Seven painted assets inspected separately and in final-size scenes. Redrew kf-bucket with the built-in imagegen tool; prompt and provenance saved in art/prompts.json, raw source in art/raw/kf-bucket.png. Original retained in Scratch. Re-keyed six cutouts with spill removal, no downloads or recordings. Full set remains one warm storybook style, no people, no missing art tokens.
Final bundle: 404450 bytes (395.0 KiB). Viewed all cold, size, functional, targeted, voice and comparison frames; review-feel-comparison.png places the tool beside Snowy Mail Route. Beat Lab also inspected. Scene/art retained or strengthened.

#### Audit

Audit not finished: reached the 2400-second limit during per-control resize stress. Saved review-audit/audit.md has 175 leads and 58 frames, all inspected. Size/state, Motion off, both control walks, repeat and quick-tap stages completed; full resize coverage remains uncertified. No second audit was run.
Confirmed/fixed: blank Add feedback, compact answer-label wrapping and Close clearance, with popup semantics/focus improved. Other leads: intentional popup/modal coverage; compact crowded-school/count overlap with distinct tappable centers; pointer-events-none decoration misclassified as hidden text; long tackle-drawer scrolling; first-tap welcome skips permitted by BASELINE rule 16. The audit phone context failed, so separate real 375-pixel iframe checks provide that evidence. Diagnostic-host favicon 404s were separate from the offline bundle; the final nine hosted follow-ups are console-clean. Tree termination was denied; owned Chrome was closed directly and lingering preview servers were stopped. All 58 audit frames and all affected follow-up frames were opened. No blanket PASS claimed.

#### Left open

The four spec-level findings above and browser fallback narration. No questions asked in this unattended run: followed the spec where its explicit content/goals conflicted with review demands. No shared source edits, git commits, new modes or topics. Temporary host removed and owned browsers/server closed. Report staged in Scratch until final writing to honor the immediate stop instruction. One cold review/fix pass, followed only by scoped re-checks and the single audit.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Keyword Fishing build handoff

#### Structure

src.html starts from the kit starter. Its style block lays out the painted lake and a tackle panel at actual viewport sizes. POND contains the spec's 30 fictional pages. LEVELS, SWAPS and LITTLE are the instructional data. fishCatch is the pure every-word evaluator exposed as __tool.catch(words), returning page IDs. Rendering, casting, page tags, persistence and pointer gestures follow. There is no family engine.

The kit owns Motion, Sound, Read, speech queuing, tones and chimes. Curio.voice uses mode scope, once-only how lines, repeatable events and validity checks. The tool changes its hint immediately. Read speaks that hint plus the open page tag or the current question. The voice plan is friendly-dad, Achird. No audio was recorded; the kit uses browser speech.

#### Tricky parts

- The matching rule is exactly the spec's pairwise equality or suffix s/es comparison. It is deliberately not an English stemmer. All fish have all 22 little words. Unknown typed words are retained on the line.
- Cast snapshots the words, mode, question and results. generation cancels a pending cast on a line or mode change. Re-aiming uses interrupted CSS transitions from current positions. The count changes synchronously. A cancelled cast restores the last catch badge instead of leaving Reeling in on screen.
- The 800 ms cast sends up to 12 painted copies to the actual pail position. The live fish controls and word controls remain available. Calm displays results immediately as explicitly specified. Free fishing never earns answer fins or stickers.
- Selecting a word changes persistent node attributes. Adding/removing rebuilds the eight slots and restores focus with preventScroll. A tied tile passes focus to its new line word; removal and swapping restore a useful enabled control. Native button Enter works throughout. Pointer drags add to the line or remove a line word outside its bounds.
- Swaps use a small popup over the lake, positioned from the stage's current rectangle. It leaves the question, hint, line and Cast uncovered. Resize repositions it. Escape closes swaps or a page tag.
- Only solved level numbers save under kf-levels, guarded and validated. Clear stickers asks Yes/No. Free fishing has no saved work. Privacy is stated in the panel footer.
- Short landscape boxes keep the panel beside the lake. The 760x900 view stacks a 280 px lake above the panel. Phones use the specified 220 px lake. Compact buckets collapse to their count. Long catch captions and typed words deliberately ellipsize with complete title/accessible labels.

#### Open questions and build decisions

The spec has no explicit open-question list. Its six independent levels, exact pond, eight slots, three-fish goal and unscored Free fishing mode were followed. No topics or game modes were added.

The supplied catch examples all match. A later exhaustive check of one-to-three-word solution sets found a source-note counting discrepancy: Level 1 has four solutions from its original tiles, but 31 with the listed eat-to-food/diet swaps included. Level 4 has the stated 11 with swaps; the other levels have at least 27 with swaps. No pond, level, swap or spec data was changed. See solution-counts.json in Scratch. The original catch examples were recomputed before building; this broader enumeration was completed during verification.

Matching deliberately uses the Words column, not displayed snippets or titles. B1's snippet includes find even though its supplied keyword list does not. The exact spec makes find a dead word. Teacher notes call out this visible-text/index mismatch; cold review should assess that model limitation. The wording and index were retained as supplied.

The owner and CODEX-BUILD.md request the image tool, superseding the spec's older local FLUX wording. Seven images were generated with the built-in OpenAI image tool, then processed only with art.py --rekey. No people, downloaded media or recordings were made. All seven art tokens are used.

For legibility, fish that swim away show their full 12 px title tags on focus/hover, and crowded schools in narrow lake boxes do likewise. The full tag card remains available by tap or Enter on every fish. This extends the spec's title-hiding exception beyond the 680 preview; cold review should assess it as a deliberate presentation tradeoff.

The spec explicitly makes Motion off casts instant. That specific instruction was followed for this short live-preview action, despite POLISH.md's general equal-timing guidance. No story or narration sequence was sped up.

STANDARDS.md wins where some literal feedback names Take it off or Swap a word before selection has enabled them. Those prompts now ask the student to select a line word first; selection then names the enabled removal/swap controls. A full line never suggests adding a disabled tile. Solved feedback names the next level control. Outcomes, matching, goals and feedback priority are unchanged. EVENT_IDS explicitly identifies repeatable spoken events.

The report was staged in Scratch and is written only after checks finish, following the owner's explicit instruction to stop as soon as codex-report.md is written. Bar tools were copied and bundled inside Scratch so their original folders were never written.

#### Evidence

All commands run from S:/CurioClass-codex with a bounded runner. Evidence is under _scratch/keyword-fishing:

- prepare.py and numbers.json independently reproduce the 25 supplied catches and little-word behavior.
- core-results-fixed.json checks exact IDs, plural cases, all little words, every swap, all 30 tags, duplicate/full slots, feedback priority and stale-cast cancellation.
- student-run.json records a complete six-level held-click run earning all stickers. keyboard-solve.json records a keyboard-only solution. drag-on.json and drag-off.json preserve real whole-pixel pointer paths with small timing/position variations.
- storage-resize-results.json verifies earned stickers across reload, both confirmation choices, denied storage, resize during a cast, instant calm re-aiming, no infinite calm loops, and no external requests or exceptions.
- voice-on-two-second.json and voice-two-second.json contain held-click narration logs, repeated cast events, Sound off/on and Read interruption.
- early-frames, functional-frames, late-frames, size-frames and targeted-frames retain the build checks. The single full size sweep was followed by targeted checks only. feel-comparison.png puts Keyword Fishing beside Snowy Mail Route; Beat Lab was also opened and inspected.
- static-results.json records contrast, readable source lines, exact bundle bytes, seven art tokens and no network APIs or external resources.
- audit contains the single final mechanical audit. Final dispositions and limitations are in codex-report.md.

#### Audit outcome and final repairs

The one mechanical audit reached its 2400-second limit during the later walk/resize work. The bounded runner stopped its process tree. It saved 58 frames but did not write audit.md. All 58 frames were inspected through eight labeled contact sheets. The audit was not restarted, so the full mechanical walk, repeats and resize suite remain uncertified.

Final targeted repairs widened short tiles and header controls to 44 px, fitted all swap choices within the lake, moved the fixed swap popup out of the scrolling panel, reserved clearance above a selected compact word, and restored the compact bucket count below the actions. Prompt wording follows enabled controls in steps. Fish facing uses current screen positions when retargeted, and turning Motion off removes in-flight painted copies.

post-frames, final-frames and the targeted phone states show the repairs. final-summary.json records zero small targets, clipped UI text, disabled controls named, hidden non-fish labels, unintended non-fish overlaps or missing keep regions in the five measured final states. Fish-school rectangles and a popup covering background fish are explicitly excluded from that UI summary, not treated as clean geometry. Crowded fish and banked nonmatches can overlap, especially in previews; every fish remains in keyboard order, but complete unobstructed pointer access to every fish is not established. The report marks that strict Done when item FAIL.

The final voice test contains one how line, two solved-event starts and Read priority at a two-second held-tap pace. All 19 runtime lines match voice/lines.json. The phone host was removed, and ports 9990, 9991 and 8795 were confirmed closed after testing. No full size sweep or full audit was repeated after these repairs.

#### Engine changes wanted

None required. No kit, docs, scripts or other tool sources were edited.

#### Cold review repairs (November 7, 2026)

The cold reviewer played all six levels and both modes before reading this handoff or src.html. Responsive fish positions now reserve a distinct target of at least 44 pixels per page, including nonmatches. Painted cutouts remain 110 pixels in roomy scenes and 70 in compact scenes; their overhangs do not intercept neighbouring targets. Focused title tags stay within the lake. The school leaves a clear bobber window, re-aims on resize, and distributes rejected fish instead of stacking them on top of each other.

The swap popup anchors to the Swap button, follows panel scrolling and stays inside the viewport. It can cover bucket contents or part of the word area while open, keeping the question, hint and Cast available. Empty casts have an expanding surface ripple when Motion is on. The pail was redrawn with a clearer handle via the [imagegen skill](C:/Users/Cory/.codex/skills/.system/imagegen/SKILL.md). Its prompt is in art/prompts.json; the original is preserved in Scratch. All six cutouts were reprocessed only with art.py --rekey, with spill removal. No people were added to this first-person dock scene.

Answer fins now survive Motion changes and resize whenever the line still matches the displayed catch, including answers beyond the first twelve bucket entries. A new line clears obsolete fins. Editing a line stops a spoken result that no longer fits while preserving an active Read. Voice text and the once-only how/repeatable-event distinction remain unchanged.

The lake now says that only the words in a page's list count. This makes the supplied find/hunt limitation visible to students. Notes correct the full-I.A.1 teaching claim and use the current AASL framework URL. The fixed supplied questions do not independently teach question formulation; changing the catalog alignment would need an out-of-scope shared edit.

The live count and freely repeatable casts intentionally support exploration. A sticker records a valid query rather than proof of mastery. The spec explicitly accepts cold alone in Level 5 and lava alone in Level 6. Preventing brute-force discovery of those valid answers would require changing the specified goal or adding an assessment mechanic; the review does neither and reports the limitation.

#### Sensitivity

M3 names Mars as a Roman god of war and refers to the planet's naming story. NASA's Mars facts support that association. A cultural reviewer should check the neutral treatment of Roman religion/mythology and the use of this title as a meaning distractor, plus the familiar fable title T11 and cricket vocabulary B5. No tradition is dated by European contact, no people appear in art, and there is no hard-history material.

#### Cold review audit disposition

The review audit ran once with the 2400-second deadline on Chrome 9941 and host 8745. It reached resize stress checks but did not finish. Its saved audit.md contains 175 leads and 58 frames, all inspected in eight contact sheets. The completed control walks have no console errors or lost focus; repeat and quick-tap rows are clean. Remaining stress coverage is uncertified. No second audit was started.

Confirmed fixes from that audit: empty Add now gives a prompt, focuses the text field without scrolling, and reuses the existing Free fishing how-to; compact answer fins stay on one line; compact page tags reserve more Close clearance. Swap and page-tag popups have nonmodal dialog labels, and opening a page tag focuses Close; closing restores the fish. The voice manifest remains unchanged.

Other leads are expected popup/modal coverage, compact school decoration overlapping the count, pointer-events-none artwork misclassified as hidden text, long tackle-drawer scrolling, and first-tap welcome skips permitted by BASELINE rule 16. The audit could not locate its phone iframe context; separate real 375-pixel iframe frames cover that size and the affected popup states. The diagnostic host's favicon 404 is separate from the offline tool, whose resources are all inline. Process-tree termination was denied at the deadline; the owned Chrome was closed through CDP and lingering preview servers were stopped directly.

#### Scope

Build only. No git commits, branch changes, deployments or polish round. The generated offline HTML remains git-ignored. Browser profiles, temporary scripts, reference copies and frames remain in Scratch. The phone host server is stopped after its shots and host.html is removed.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
