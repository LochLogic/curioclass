# Keyword Fishing build handoff

## Structure

src.html starts from the kit starter. Its style block lays out the painted lake and a tackle panel at actual viewport sizes. POND contains the spec's 30 fictional pages. LEVELS, SWAPS and LITTLE are the instructional data. fishCatch is the pure every-word evaluator exposed as __tool.catch(words), returning page IDs. Rendering, casting, page tags, persistence and pointer gestures follow. There is no family engine.

The kit owns Motion, Sound, Read, speech queuing, tones and chimes. Curio.voice uses mode scope, once-only how lines, repeatable events and validity checks. The tool changes its hint immediately. Read speaks that hint plus the open page tag or the current question. The voice plan is friendly-dad, Achird. No audio was recorded; the kit uses browser speech.

## Tricky parts

- The matching rule is exactly the spec's pairwise equality or suffix s/es comparison. It is deliberately not an English stemmer. All fish have all 22 little words. Unknown typed words are retained on the line.
- Cast snapshots the words, mode, question and results. generation cancels a pending cast on a line or mode change. Re-aiming uses interrupted CSS transitions from current positions. The count changes synchronously. A cancelled cast restores the last catch badge instead of leaving Reeling in on screen.
- The 800 ms cast sends up to 12 painted copies to the actual pail position. The live fish controls and word controls remain available. Calm displays results immediately as explicitly specified. Free fishing never earns answer fins or stickers.
- Selecting a word changes persistent node attributes. Adding/removing rebuilds the eight slots and restores focus with preventScroll. A tied tile passes focus to its new line word; removal and swapping restore a useful enabled control. Native button Enter works throughout. Pointer drags add to the line or remove a line word outside its bounds.
- Swaps use a small popup over the lake, positioned from the stage's current rectangle. It leaves the question, hint, line and Cast uncovered. Resize repositions it. Escape closes swaps or a page tag.
- Only solved level numbers save under kf-levels, guarded and validated. Clear stickers asks Yes/No. Free fishing has no saved work. Privacy is stated in the panel footer.
- Short landscape boxes keep the panel beside the lake. The 760x900 view stacks a 280 px lake above the panel. Phones use the specified 220 px lake. Compact buckets collapse to their count. Long catch captions and typed words deliberately ellipsize with complete title/accessible labels.

## Open questions and build decisions

The spec has no explicit open-question list. Its six independent levels, exact pond, eight slots, three-fish goal and unscored Free fishing mode were followed. No topics or game modes were added.

The supplied catch examples all match. A later exhaustive check of one-to-three-word solution sets found a source-note counting discrepancy: Level 1 has four solutions from its original tiles, but 31 with the listed eat-to-food/diet swaps included. Level 4 has the stated 11 with swaps; the other levels have at least 27 with swaps. No pond, level, swap or spec data was changed. See solution-counts.json in Scratch. The original catch examples were recomputed before building; this broader enumeration was completed during verification.

Matching deliberately uses the Words column, not displayed snippets or titles. B1's snippet includes find even though its supplied keyword list does not. The exact spec makes find a dead word. Teacher notes call out this visible-text/index mismatch; cold review should assess that model limitation. The wording and index were retained as supplied.

The owner and CODEX-BUILD.md request the image tool, superseding the spec's older local FLUX wording. Seven images were generated with the built-in OpenAI image tool, then processed only with art.py --rekey. No people, downloaded media or recordings were made. All seven art tokens are used.

For legibility, fish that swim away show their full 12 px title tags on focus/hover, and crowded schools in narrow lake boxes do likewise. The full tag card remains available by tap or Enter on every fish. This extends the spec's title-hiding exception beyond the 680 preview; cold review should assess it as a deliberate presentation tradeoff.

The spec explicitly makes Motion off casts instant. That specific instruction was followed for this short live-preview action, despite POLISH.md's general equal-timing guidance. No story or narration sequence was sped up.

STANDARDS.md wins where some literal feedback names Take it off or Swap a word before selection has enabled them. Those prompts now ask the student to select a line word first; selection then names the enabled removal/swap controls. A full line never suggests adding a disabled tile. Solved feedback names the next level control. Outcomes, matching, goals and feedback priority are unchanged. EVENT_IDS explicitly identifies repeatable spoken events.

The report was staged in Scratch and is written only after checks finish, following the owner's explicit instruction to stop as soon as codex-report.md is written. Bar tools were copied and bundled inside Scratch so their original folders were never written.

## Evidence

All commands run from S:/CurioClass-codex with a bounded runner. Evidence is under _scratch/keyword-fishing:

- prepare.py and numbers.json independently reproduce the 25 supplied catches and little-word behavior.
- core-results-fixed.json checks exact IDs, plural cases, all little words, every swap, all 30 tags, duplicate/full slots, feedback priority and stale-cast cancellation.
- student-run.json records a complete six-level held-click run earning all stickers. keyboard-solve.json records a keyboard-only solution. drag-on.json and drag-off.json preserve real whole-pixel pointer paths with small timing/position variations.
- storage-resize-results.json verifies earned stickers across reload, both confirmation choices, denied storage, resize during a cast, instant calm re-aiming, no infinite calm loops, and no external requests or exceptions.
- voice-on-two-second.json and voice-two-second.json contain held-click narration logs, repeated cast events, Sound off/on and Read interruption.
- early-frames, functional-frames, late-frames, size-frames and targeted-frames retain the build checks. The single full size sweep was followed by targeted checks only. feel-comparison.png puts Keyword Fishing beside Snowy Mail Route; Beat Lab was also opened and inspected.
- static-results.json records contrast, readable source lines, exact bundle bytes, seven art tokens and no network APIs or external resources.
- audit contains the single final mechanical audit. Final dispositions and limitations are in codex-report.md.

## Audit outcome and final repairs

The one mechanical audit reached its 2400-second limit during the later walk/resize work. The bounded runner stopped its process tree. It saved 58 frames but did not write audit.md. All 58 frames were inspected through eight labeled contact sheets. The audit was not restarted, so the full mechanical walk, repeats and resize suite remain uncertified.

Final targeted repairs widened short tiles and header controls to 44 px, fitted all swap choices within the lake, moved the fixed swap popup out of the scrolling panel, reserved clearance above a selected compact word, and restored the compact bucket count below the actions. Prompt wording follows enabled controls in steps. Fish facing uses current screen positions when retargeted, and turning Motion off removes in-flight painted copies.

post-frames, final-frames and the targeted phone states show the repairs. final-summary.json records zero small targets, clipped UI text, disabled controls named, hidden non-fish labels, unintended non-fish overlaps or missing keep regions in the five measured final states. Fish-school rectangles and a popup covering background fish are explicitly excluded from that UI summary, not treated as clean geometry. Crowded fish and banked nonmatches can overlap, especially in previews; every fish remains in keyboard order, but complete unobstructed pointer access to every fish is not established. The report marks that strict Done when item FAIL.

The final voice test contains one how line, two solved-event starts and Read priority at a two-second held-tap pace. All 19 runtime lines match voice/lines.json. The phone host was removed, and ports 9990, 9991 and 8795 were confirmed closed after testing. No full size sweep or full audit was repeated after these repairs.

## Engine changes wanted

None required. No kit, docs, scripts or other tool sources were edited.

## Cold review repairs (November 7, 2026)

The cold reviewer played all six levels and both modes before reading this handoff or src.html. Responsive fish positions now reserve a distinct target of at least 44 pixels per page, including nonmatches. Painted cutouts remain 110 pixels in roomy scenes and 70 in compact scenes; their overhangs do not intercept neighbouring targets. Focused title tags stay within the lake. The school leaves a clear bobber window, re-aims on resize, and distributes rejected fish instead of stacking them on top of each other.

The swap popup anchors to the Swap button, follows panel scrolling and stays inside the viewport. It can cover bucket contents or part of the word area while open, keeping the question, hint and Cast available. Empty casts have an expanding surface ripple when Motion is on. The pail was redrawn with a clearer handle via the [imagegen skill](C:/Users/Cory/.codex/skills/.system/imagegen/SKILL.md). Its prompt is in art/prompts.json; the original is preserved in Scratch. All six cutouts were reprocessed only with art.py --rekey, with spill removal. No people were added to this first-person dock scene.

Answer fins now survive Motion changes and resize whenever the line still matches the displayed catch, including answers beyond the first twelve bucket entries. A new line clears obsolete fins. Editing a line stops a spoken result that no longer fits while preserving an active Read. Voice text and the once-only how/repeatable-event distinction remain unchanged.

The lake now says that only the words in a page's list count. This makes the supplied find/hunt limitation visible to students. Notes correct the full-I.A.1 teaching claim and use the current AASL framework URL. The fixed supplied questions do not independently teach question formulation; changing the catalog alignment would need an out-of-scope shared edit.

The live count and freely repeatable casts intentionally support exploration. A sticker records a valid query rather than proof of mastery. The spec explicitly accepts cold alone in Level 5 and lava alone in Level 6. Preventing brute-force discovery of those valid answers would require changing the specified goal or adding an assessment mechanic; the review does neither and reports the limitation.

## Sensitivity

M3 names Mars as a Roman god of war and refers to the planet's naming story. NASA's Mars facts support that association. A cultural reviewer should check the neutral treatment of Roman religion/mythology and the use of this title as a meaning distractor, plus the familiar fable title T11 and cricket vocabulary B5. No tradition is dated by European contact, no people appear in art, and there is no hard-history material.

## Cold review audit disposition

The review audit ran once with the 2400-second deadline on Chrome 9941 and host 8745. It reached resize stress checks but did not finish. Its saved audit.md contains 175 leads and 58 frames, all inspected in eight contact sheets. The completed control walks have no console errors or lost focus; repeat and quick-tap rows are clean. Remaining stress coverage is uncertified. No second audit was started.

Confirmed fixes from that audit: empty Add now gives a prompt, focuses the text field without scrolling, and reuses the existing Free fishing how-to; compact answer fins stay on one line; compact page tags reserve more Close clearance. Swap and page-tag popups have nonmodal dialog labels, and opening a page tag focuses Close; closing restores the fish. The voice manifest remains unchanged.

Other leads are expected popup/modal coverage, compact school decoration overlapping the count, pointer-events-none artwork misclassified as hidden text, long tackle-drawer scrolling, and first-tap welcome skips permitted by BASELINE rule 16. The audit could not locate its phone iframe context; separate real 375-pixel iframe frames cover that size and the affected popup states. The diagnostic host's favicon 404 is separate from the offline tool, whose resources are all inline. Process-tree termination was denied at the deadline; the owned Chrome was closed through CDP and lingering preview servers were stopped directly.

## Scope

Build only. No git commits, branch changes, deployments or polish round. The generated offline HTML remains git-ignored. Browser profiles, temporary scripts, reference copies and frames remain in Scratch. The phone host server is stopped after its shots and host.html is removed.
