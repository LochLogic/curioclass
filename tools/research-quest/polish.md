# Polish: research-quest (Codex fix, round 1)

The explicit Curiosity instruction takes precedence over Refine's older lesson classification and its keep-endings call. The tool is now an open research desk: Question, Sources, Notes, Outline and Evidence can be used in any order. No welcome screen, kit header, numbered ladder, score, level, quiz or finish screen remains. Evidence gaps are document readouts, not an approval grade. All evidence paths below are relative to `_scratch/research-quest/`.

## Blocker

- **1 FIXED.** Routes use the actual cause: unsuitable question = Question; unvisited source = Sources; unsaved, uncredited, unquoted or changed note = Notes; excluded note, wrong heading, missing plan step or empty outline = Outline. Original skipped-library route was 4; now 2. Original empty-outline citation route was 3; now 4. `fix-before/skip-library.png`, `fix-after/skip-library.png`, `fix-before/all-not-needed.png`, `fix-after/all-not-needed.png`; `logic-verified.json` tests all four useful sources. Both failing runs are in `audit-states.json` as real-input states.
- **19 FIXED.** The citation check examines every outlined note, lists every issue and names its note and source. The named exploit now lists county, nature and notebook, routes to Notes and exposes the missing credits and quote marks. The original 32-case probe accepted 15 uncredited variants; the corrected 10,000-combination test has zero false citation passes and 28,020 assertions. `fix-before/unsourced-copies.png`, `fix-after/unsourced-copies.png`, `logic-before.json`, `logic-verified.json`. Approval itself is removed under Curiosity precedence.

## Should fix

- **2 FIXED.** Both save controls use the same plain style. `save-style-before.json` and `save-style-after.json` record their computed backgrounds; `fix-before/save-style.png` and `fix-after/save-style.png` show the same 1366x768 state.
- **3 FIXED.** Pointer state clears on cancel, native drag start, drag end, blur and a new pointer down. Native drag start no longer silently selects a note. Cancel, native-start/cancel and blur probes followed by a heading click all leave heading 0 and selection null: `cancellation-final.json`, `last-proofs/final-cancellation.png`, against `stale-pointer-before.json` and `fix-before/stale-pointer.png`. Real keyboard placement moves the note to heading 2. The native drag fixture emitted no drop; native-drop success is not claimed.
- **4 FIXED.** Card text begins at the top and uses available space; source lines have reserved space. Selecting a note opens its full wording over the note tray, leaving headings available. Back to notes returns to the cards. Before frames: `fix-before/organize-680.png`, `organize-800.png`, `organize-1000.png`, `phone-before/phone-organize.png`. Final evidence: `fixture-recheck/organize-680x425.png` and `fixture-recheck/selected-note-680x425.png`, `selected-note-800x500.png`, `selected-note-1000x625.png`, `selected-note-375x812.png`, with matching JSON. At 680 the selected text measures 56/56 px client/scroll height and the full credit 32/32; every card credit is within its card. Text and credit client/scroll heights also match at 800, 1000 and 375. Main controls remain available; long unselected note bodies can scroll rather than losing words to a two-line clamp or hover-only title.
- **5 FIXED.** Copy explanations name the actual document and add the missing-credit instruction only when needed. The note's wording is shown before its credit. `fix-after/county-copy.png`, `fix-after/notebook-copy.png`, `county-copy-after.json`, `notebook-copy-after.json` at 1366x768; paired wording corrected in spec Content. These are original fictional document titles, not claims that a county page or notebook is a book.
- **20 FIXED.** An all-quote outline retains its evidence links and displays the uncounted aside, "Can you say that in your own words?" `fix-before/all-quote.png`, `fix-after/all-quote.png`, `all-quote-after.json`, `logic-verified.json`. There is no win or approval state.
- **21 FIXED.** Changed meanings cannot support questions 1, 2, 3 or 5. Each routes to Notes, including when a second organizational problem exists. Before: all four were supported. After: all four expose gaps. `fix-before/all-changed.png`, `fix-after/all-changed.png`, `logic-verified.json`; covered across all 10,000 note combinations.
- **22 FIXED BY REMOVAL.** The Not yet ending is removed with all ending bands. Each evidence gap instead names its missing material and its cause, available immediately rather than after a forced finish. `last-layout/evidence.png`; zero ending renderers in `contract-final.json`. No replacement finish was added.
- **23 FIXED.** AASL Collaborate is removed from the claimed standards in source metadata, spec and notes. `notes.md` explicitly records that automatic responses do not teach it and asks the integrator to give the code to a tool with real collaboration. No catalog outside the allowed folders was edited.

## Polish accepted

- **6 FIXED BY REMOVAL.** No ending heading or paragraph remains to repeat. `last-layout/evidence.png`, `contract-final.json` (zero ending renderers). The live empty-outline detail also avoids repeating its status as a second answer card.
- **7 FIXED BY REMOVAL.** No homework list or joined ending sentence remains. Missing material is shown in separate evidence cards and note details; no ambiguous conjunction chain. `last-layout/evidence.png`.
- **8 FIXED.** All six changed variants are fluent and within 15% of the matching good variant: ratios 1.010, 0.930, 1.008, 0.945, 1.141, 1.082. Same strings in spec Content. `logic-verified.json`; original ratios in `logic-before.json`. The shortest-choice shortcut no longer identifies the changed version reliably.
- **9 FIXED.** Credit details show the actual note text before the source, including every problematic note. `fix-after/county-copy.png`, `fix-after/notebook-copy.png`, `fix-after/unsourced-copies.png` at 1366x768.
- **10 FIXED.** Visible routes have a paper halo and sit above the map cards; lower-row routes use the side margins to avoid upper-row text. Card buttons remain the main input route. Final 1366 and 375 evidence: `fixture-recheck/evidence-seven-1366x768.png` and `fixture-recheck/evidence-seven-375x812.png`, both inspected with all seven routes. The accepted transparent-hit-stroke geometry leads are not treated as painted overlap.
- **11 FIXED.** Every evidence detail offers Rewind to the named file through the existing Yes / No confirmation. The real-input sequence opened the skipped-library detail, chose Sources and chose No; work remained intact. `input-final/rewind.png`, `final-rewind.json`; direct inspection of `trace()` and `confirmReset()` confirms the shared path.
- **12 FIXED.** Wide saved-note hint: "Tap the next place below." Compact layouts name the visible Pack control. `extra-final/saved-hint.png`, `hint-final.json` at 1366x768. The final Pack button is on the power rail at every size, including `phone-final/phone-organize.png`.
- **13 FIXED.** Read is assembled from semantic working content, not chapter innerText. It includes note text and credits, choices and evidence, and skips seals, hidden/decorative copies, placement instructions and footer. It also works inside dialogs via their own Read button. `final-read.json`, `voice-walk-final.json`, `input-final/read.png`, `extra-final/initial-voice.png`. The final semantic filter also excludes dialog help and includes the dialog title; the live `read` field in `fixture-recheck/all-not-needed-680x425.json` confirms the title, question and single status without the footer.
- **14 FIXED BY REMOVAL.** Empty stop badges and the numbered stop strip are removed. The defensive `small:empty` rule also exists. `last-layout/default.png`; independent file tabs have no empty pills.
- **15 FIXED BY REMOVAL.** No marker overlaps a compact label because the sequential marker and stop strip are removed. `last-layout/organizer-680.png`, `organizer-800.png`, `organizer-1000.png` and `phone-final/phone-organize.png`.
- **16 FIXED.** SVG route groups have tabindex -1; their cards remain keyboard buttons. No duplicate tab route is added. Source `trailView()`; `input-final/keyboard.png` also verifies keyboard note placement.
- **17 FIXED.** The bundle header credits illustrations to Curio Class without the company name. All 13 prompt entries explicitly declare people false, including the three named entries. `contract-final.json`; no new painting or people image was made.
- **18 FIXED.** L.next and L.endingNext and all forced-route narration are removed from the spoken bank. `allLines()` and `voice/lines.json` both contain one quiet initial hint. `voice-walk-final.json`, `contract-final.json`.
- **24 FIXED.** B asks, "What would you need to find out about the garden first?" Same wording in spec and source; no automatic praise or correctness marker. The four options remain freely revisable. `reply-final/question-b-final.png` and `question-b-final.json` at 1366x768, after held clicks on Question and B.
- **25 FIXED.** Spec Art now matches the prompt records: eleven generated gpt-image paintings, two retained local FLUX paintings. All people flags are false, so no people contact sheet is required. No images were replaced or removed from the asset set.

## Settled calls

The blocker severity, source-credit requirement, meaning checks, standards removal, and permission to quote with a source are applied. Source relevance still allows the county note under any useful outline heading. The pack is a scrollable collection. Transparent route hit geometry is not painted clutter. Existing art remains.

The old keep-ending-bands instruction and sequential seven-question presentation conflict with the explicit Curiosity request. Ending bands and the forced presentation were removed. The seven question texts remain available as evidence prompts, with the original conditional meaning-change and seed-ad prompts. No welcome, score, goal ladder or forced finish was introduced.

Unattended decisions: use an open desk with freely accessible files; retain the supplied six-document scope; keep browser narration; leave the catalog number unassigned because neither spec nor concept catalog assigns Research Quest a number. Do not fabricate a numbered plate or a new observational dataset.

## Cheats tried

The old library-good / three-uncredited-copies pattern now lists all three citation failures. Single missing source, unquoted copy and combinations of those conditions were tested across all four notes in 10,000 combinations. Zero incorrect citation passes.

All changed notes, one changed note at a time, changed notes with organizational problems, skipped useful sources, all Not needed, wrong headings and missing plan steps route to their actual cause. All-source quotations stay valid and invite paraphrasing. Length-only selection is neutralized within 15%. No score, grade or finish can be earned by a tap pattern.

Three independent canceled-pointer patterns followed by a heading click do not move a note. Keyboard placement does. The native drag fixture reached dragstart/pointercancel/dragend without drop, so native drop remains unverified rather than reported as working.

## Voice walk

Held clicks used a 0.12-second press and two-second spacing: choose quotation, save with source, open Outline, open Evidence, inspect the credit card, Read inside it. The optional initial hint became stale on the first action and was correctly dropped. One Read entry was logged at about 12 seconds. There is no automatic council or ending narration. A separate working-board Read entry includes full note wording and sources without repeated placement instructions. Browser narration is used; no recorded clips were generated or listened to audibly in this muted run. Bank equality: 1 = 1.

## Engine changes wanted

None. All changes are tool-local. No shared kit, scripts or catalog file was changed.

## The real material

Fetched/checked 2026-11-06. Raw verification downloads, rights notes and reproducible gathering script are in `data/source-manifest.json` and `gather_sources.py`. Every request had an 18-second timeout; gathering remained within 45 minutes. No observational dataset was sampled, and no outside passages or media were packed into the tool. All six original fictional documents are bundled in full.

| Material | Named source and rights | Independent check |
|---|---|---|
| Caterpillar milkweed dependency; adult nectar; eastern migration up to 3,000 miles | [U.S. Fish and Wildlife Service, Monarch](https://www.fws.gov/species/monarch-danaus-plexippus). Federal-authored facts public domain, 17 USC 105; [FWS rights notice](https://www.fws.gov/disclaimer) acknowledges third-party exceptions. No third-party media copied. | [NPS, Protecting Western Monarchs](https://www.nps.gov/articles/000/protecting-western-monarchs.htm), [NPS migration event](https://www.nps.gov/planyourvisit/event-details.htm?id=0AFA7A72-FFED-E75A-C80160AEB245F91C). |
| Native milkweed, fall nectar and pesticide avoidance | [Xerces, Monarch Butterfly Conservation](https://xerces.org/monarchs), fact checking only; no copyrighted text or images reused. Student text is original Curio Class writing, CC BY 4.0. | [NPS, Monarchs on the Move](https://www.nps.gov/articles/000/monarchs-in-cuyahoga-valley.htm), Protecting Western Monarchs. [NPS rights](https://www.nps.gov/aboutus/disclaimer.htm): federal-authored text generally public domain; outside images excluded. |
| Common milkweed and butterfly weed identities | [USDA PLANTS](https://plants.usda.gov/), federal plant facts public domain. Regional suitability belongs only to the fictional setting. | [University of Connecticut, Milkweed](https://homegarden.cahnr.uconn.edu/factsheets/milkweed/), reference only; copyright UConn, no text or media packed. |
| Six example documents, authors, notebook count of two, ad, dates, candidate notes and evidence rules | Original fictional Curio Class material, CC BY 4.0. Candidate versions can deliberately distort a source; they are not biological assertions endorsed by the instrument. | Verified against each original passage and exact evaluator tests. |
| Standards references | [AASL Framework](https://standards.aasl.org/framework/), copyright AASL. Codes and citation only; no framework text reproduced. Collaborate removed. | Claimed practice checked against the implemented note and evidence interactions. |
| Illustrations and code | Existing generated Curio Class illustrations; two retained FLUX.1-schnell paintings, model Apache 2.0. Original content CC BY 4.0; code MIT. | Existing provenance retained in art/prompts.json; all 13 people flags false. |

## Curiosity short test and lesson creep

These are agent judgments from the solo research and counterfactual comparison paths, not claims from a human user study. The revised desk supports open comparison and revision with no terminal state. A kid may be drawn to the painted sources and evidence routes; unassigned replay appeal is not established. Adult replay and a month of depth remain limited by the six-document corpus. The real working material is the document wording, citations and their links, with real biological facts inside explicitly fictional documents. This is a bounded document instrument, not a general research or gardening system. No claim that it reaches Beat Lab's or Elements Inspector's depth is made.

The four questions, explicitly:

- Would a kid open it unassigned? The painted sources and changing routes offer a low floor; sustained unassigned return is not established.
- Would an adult play for fun? Brief source/note comparison is interesting, but replay is limited by the fixed corpus.
- Is the real thing the interface? Yes for document wording, citations and links; biological facts are real, while the example documents are explicitly fictional.
- Does it work without a score or finish? Yes. Files and evidence stay open to revision without an approval band or terminal state.

All four model frames were opened and inspected in `model-frames/`. Compare `last-layout/default.png` and `model-frames/beat-lab.png`: the desk uses its own material and permanent working controls, but has substantially less depth. No model file was modified.

Lesson-creep scan: no header or ending renderer, and no score/level/goal/quiz/finish flow. `complete` occurs only in the source's biological phrase "life cycle"; `score` appears only in the Manual's honesty statement that there is none. Legacy unused ending CSS is inert, not a reachable screen. Internal result booleans describe evidence support and never accumulate into a grade.

## Audit

The single full audit completed in **1115.9 seconds (18.6 minutes)**, below its 40-minute limit. `fix-audit/audit.md`, `fix-audit-result.json` and all 81 frames were inspected (also collected in `fix-audit-contacts/`). The audit found 233 mechanical leads, not 233 confirmed instrument defects. Every lead has an individual disposition in `audit-dispositions.json`:

- 18 hidden legacy-hint checks: accepted under Curiosity precedence. The old lesson panel is hidden; working controls, Read and Manual carry the instrument.
- 28 state-step, focus and keep-region checks from invalid compact fixtures: corrected. Hidden visit tabs were replaced by the visible Pack path. Later rows in the working scroll collection are reached with Tab and Enter, not a click below its scroll edge. Fixtures begin with the visible confirmed reset. Twelve scoped real-input cases then passed with zero console errors, including all four saved notes, four selected-note sizes, all Not needed, skipped library and seven routes at 1366 and 375. See `fixture-recheck/summary.json` and all twelve corresponding frames.
- 95 SVG/nested-label geometry checks: accepted after inspecting the actual frames. Transparent 44 px hit strokes and group bounding boxes are not painted rectangles; side-routed, haloed visible strokes do not disappear under cards.
- 81 modal occlusion checks: accepted. The active native dialog intentionally covers inactive map/rail content and has its own Read and return controls.
- 11 lesson-welcome checks: accepted under Curiosity precedence and BASELINE 16. The initial cue can be skipped or cut by an action; no lesson welcome is required.

The audit's 20 initial controls reported no errors or lost focus, including Enter twice after each click. Five-repeat checks were clean. The rapid-tap cue cut is included among the 11 voice leads. Resize checks reported no exceptions or stuck disabled controls; Motion off had no endless animations. Invalid compact fixture paths were not claimed as complete state coverage before the scoped recheck.

Inspection of the held-click table found one additional moment mismatch: the optional cue could speak after opening Manual or Pack. A tool-local validity guard now drops it while a dialog is open. `fixture-recheck/manual-first-1366x768.json` and `pack-first-1366x768.json` log a stale drop and no spoken cue. This was the only application change after the full audit; no second full audit was run.

Final bundle: **1,573,716 bytes**, one offline file, zero unresolved art tokens, zero remote resource attributes or fetch functions, no kit stylesheet, header element or ending renderer. Runtime reopening also recorded zero network resources. `contract-final.json` and `final-validation.json` preserve the checks and hashes. All assigned Chrome ports and host 8725 were closed; no host.html was left in the tool folder.

## Left open

The supplied spec/catalog does not assign a Curiosity plate number to Research Quest, so plate is null and no number was invented. The six-document corpus has limited adult replay and month-long depth; the report does not certify the full Curiosity short-test bar. No new dataset or topic was invented to hide that limit.

Native HTML drop remains unverified: the driver fixture emitted native dragstart/pointercancel/dragend without a drop. The silent-move fault is closed across three cancellation patterns, and the keyboard placement path passes. Browser narration remains the fallback; no recorded voice take was generated or audibly reviewed in this muted run.

The complete audit precedes the single dialog-hint guard and the corrected fixture descriptions. Those changes received scoped rechecks rather than a second full audit, as required by the one-audit rule.

No commits. Writes were restricted to tools/research-quest and _scratch/research-quest. refine.md and refine/ were not edited. The resumed session's failed concurrent browser attempts and earlier intermediate clipping frames are preserved; they are not presented as final passing evidence.
