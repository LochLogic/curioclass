# Egg Carton Factory handoff

## Structure

`src.html` starts from the kit starter. It contains responsive styles, persistent HTML controls,
the 27-line voice inventory, the complete 36-variant Rush card table, state and persistence,
packing and checking logic, then the responsive canvas renderer. It uses the shared kit for speech,
tones, Motion, Sound and Read. There is no family engine. `window.__tool` exposes state and the same
actions used by the controls for reproducible verification.

The panel precedes the stage in DOM order, so its controls come before the long number board in keyboard navigation.
CSS keeps the visual stage at left on laptops and below the controls on phones.
The biggest scene object is the carton, pallet or number board. The canvas draws exact cup counts,
fills by columns, rings empty cups and uses code ovals below 16 pixels. Generated images supply the
setting, materials and characters. The Order Board, Rush choices and handle are keyboard-accessible HTML.

## Tricky behavior

- Pack Station shelves and temporary Rush shelves are separate. Rush never renders the seal or board.
- A turn shares its canonical smaller-side-first pair key. Repacking cannot add a duplicate shelf stamp.
- A Composite placement needs both dimensions at least two, so packing a prime in one column cannot pass as proof.
- Each card's miss count persists across rerolls and reloads. Assistance is persisted before showing the solution.
  A shipped card cannot improve its recorded result by replaying it.
- Rerolls always change the current variant and prefer the least previously sealed set among the alternatives.
- Fill runs use elapsed time and an epoch. New order or size inputs restart immediately.
  Motion off settles the picture immediately and preserves the normal result-tone and speech timing.
- Shipping awaits the result line, then the truck, then the shift line. Mode changes cancel pending continuation.
- Voice welcome lists use nested entries. A flat pair of strings is interpreted by the kit as key plus replacement text.
- The reset confirmation is an HTML dialog panel with focus kept inside and restored without scrolling.
  A real full-viewport blocker and inert background prevent interaction behind it.
- Card buttons are persistent nodes. Opening an order from the board focuses its handle; automatic shipping focuses the next task.

## Decisions and specification tensions

There are no Open questions in the spec. No owner response was needed or assumed.

1. The Art list names 15 assets, despite its stated total of 14. All 15 were generated and placed.
2. There are 36 Rush variants, not the 27 stated in Sources: 12 cards with three variants each.
3. Some correct carton counts equal a shown size, contrary to the Sources and cheat discussion:
   48 divided by 6 is 8; 48 divided by 8 is 6; 54 divided by 6 is 9; 54 divided by 9 is 6.
   Exact quotients remain the rule. Correct answers were not altered to preserve the incorrect general claim.
4. Sources mentions a 91 to 99 decade, but playable Content lists only 41, 61 and 81 decades.
   The extra decade was recomputed but not added as a feature.
5. Ten rows of 36-pixel board cells cannot fit inside the 680 by 425 preview after its header.
   The compact board keeps all 100 numbers in a ten-by-ten grid with smaller cells. This conflicts with the
   universal 44-pixel target rule; it is an explicit remaining limitation for the cold review.
6. The instructions to bundle reference tools conflict with writing only in the two authorized folders.
   Reference sources and assets were read, then bundled into Scratch and opened there. No other tool was written.
7. The instruction to create codex-report.md after the first bundle conflicts with the user's stop condition.
   The early report draft is in Scratch. The final report is written last.
8. Older BUILD and ART wording says not to draw art or people. The user's request, current CODEX-BUILD and
   BASELINE rule 11 authorize generated art and people. Gus's four assets each carry people true.
9. The spec asks for an instant Fill end picture with Motion off, while standing rules preserve timing.
   The final picture and caption appear immediately; the result tone and narration retain the original run duration.

## Sensitivity

Gus is a fictional older farmer with warm brown skin, gray stubble, a canvas cap, plaid shirt and denim apron.
All four people assets are marked people true. The set shows one character consistently across four expressions.
The build contact sheet is `_scratch/egg-carton-factory/art-contact.jpg`. A fresh cold reviewer should inspect
the people set for respectful representation, consistent identity, natural hands, friendly expression and clean edges.
No personal questions, body instruction, religion, hard history or Indigenous cultural content is included.
This build does not authorize publishing or deployment.

## Art and voice

All 15 final WebPs were generated with the built-in OpenAI image tool and processed through art.py --rekey.
Prompts and people flags are in art/prompts.json; raw originals are in art/raw. The flat pulp and empty pallet
were redrawn once each after their first versions contained unwanted cup geometry and boxes respectively.
Generated images remain full silhouettes and are hidden where the compact layout requires it.
The hen is hidden in compact Sort and Decade scenes because their number tags otherwise cover its head.

The voice bank selection is friendly-dad, Achird. All 27 fixed lines are in voice/lines.json.
No audio was recorded, as requested. The built file falls back to browser speech through Curio.voice.
The bank voice itself is still a production recording step, not a claimed listening review in this Build run.

## Evidence

Scratch holds `numbers.json`, the independent arithmetic script, browser assertions and held-input student walks,
responsive and phone screenshots, the art contact sheet, reference frames and the one bounded audit.
Read codex-report.md for final results and unresolved audit leads. No git operations or polish round were performed.

## Cold review repairs

The independent one-pass review puts the current Rush task's how-to before its generic welcome, so the
Every shape instructions survive the ordinary two-second Pack and Ship path. Queued fit and turn lines
now require the same order to still fit; the proof prompt names both nontrivial dimensions.
The proof speech changed in voice/lines.json as well as src.html.
Carton labels have opaque paper plaques. Multiples cards now carry shaded, exact-layout empty-carton
drawings and pinned paper details, preserving the shed artwork and concealing the result.
Assisted solutions receive text-length reading time. The final banner retains the student's own/helped
counts. Saved sealed orders restore their complete matching shelf on reload.
Six-shape help now uses a three-column SVG proof grid, so every carton stays inside compact and phone overlays.
Singular egg, cup and full-column captions are corrected at the small-order extremes.
Audit-confirmed follow-ups keep complete seals, all factors and primary controls in view at 680 pixels and
on phones. A compact single-row header reclaims scene height; Next/Reset share a row only in compact sealed states.
The original full seal text remains on wide screens; concise text repeats the same facts beside all factor labels on small screens.
Result regions receive focus while Ship is disabled, and the next card keeps its existing focus transfer.
The bench readout hides behind the help overlay. Selecting the current mode/card preserves unfinished work and narration.
Fit/turn narration stops when a changed row arrangement makes it false; the factor-search goal remains in the hint.
The order field uses the adjacent steppers instead of native spin buttons, so all three digits of 100 remain visible.
First-miss feedback receives focus, then returns focus to the retry action. Checked choices and counts lock while
shipping, and the Multiples hint names the visible size/count controls instead of Rows. Obsolete task speech stops
before first-miss feedback; the correct main-path welcome and result sequence remains intact.
These changes supersede the build's secondary-seal scrolling limitation; the compact Order Board target conflict remains.
The review audit hit its single forty-minute cap during resize stress; its old bundle and partial leads are archived in Scratch.
Independent review evidence uses review-* and voice-* files in Scratch. See codex-review.md for the
review's final audit disposition and the unresolved compact-board target/specification conflict.

## Engine changes wanted

No family engine change. Shared kit files and engines were not edited.
Audit harness suggestion: scripts/audit_tool.py, PAGE_JS keep-region hit testing, should recognize visible passive
pointer-events-none captions rather than treating the canvas returned by hit testing as a visual obstruction.
