# Egg Carton Factory: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: egg-carton-factory

#### Built

Four complete modes: Pack Station, Fill Line, Order Board and Rush Orders. Rush has all 12 cards and 36 variants.
Responsive exact-count cartons, column-first egg packing, real edge dragging, canonical factor shelves,
turned-pair glows, seals and factor chips, timed filling, skip counts, proof crates, exact counts,
prime toggles, two-miss help and truck departures. Progress stays on this device; clearing it asks first.
The source is readable, uses the shared kit and makes no application network requests.
All work stayed in the authorized tool and Scratch folders. No commits, publishing or polish round.

#### Numbers check

`check_numbers.py` independently recomputes all 100 orders, factors, classifications, maxima,
all nine multiples variants, the decade prime sets, empty cups, durations and palette contrast.
`numbers.json` contains the results. Most pairs: six; largest smaller side: ten; 36 in five rows: four empty cups.
The spec has 15 named images, not 14, and 36 Rush variants, not 27.
Its claim that a correct count never equals a shown size is false: 48/6=8, 48/8=6, 54/6=9, 54/9=6.
The listed answers were preserved and exact quotient validation is used. Sources' extra 91 to 99 decade was checked but not added.
Contrast on paper: ink 14.79:1, muted 6.59:1, brand 5.99:1, white on brand 6.40:1.
Gold with ink: 8.32:1; gold outline on paper: 5.97:1; white on composite blue: 6.46:1.
One-gray with ink: 10.53:1; empty rings on pulp: 3.65:1; ink on pulp: 9.69:1.

#### Facts checked

- All factor pairs from 1 to 100, multiples of factors and one-digit tests, prime or composite:
  [CCSS 4.OA.B.4](https://www.thecorestandards.org/Math/Content/4/OA/B/4/), checked live in this run.
- Prime means exactly two positive factors; composite has a nontrivial factor pair; 1 is neither:
  [Math is Fun, Prime and Composite Numbers](https://www.mathsisfun.com/prime-composite-number.html), checked live.
- Two is the only even prime, and odd does not imply prime: the same source and independent enumeration of 1 to 100.
- Turned rectangles repeat the factor pair, and square pairs repeat one factor: integer multiplication,
  independently enumerated in `numbers.json`; the spec cites Math is Fun Factors and Multiples and Trial Division.
- The 36 factor list, five shapes, square's nine factors, all Rush labels, decade sets and carton counts:
  independently computed rather than copied from the answer table.
- The 30-egg flat arranged five by six:
  [Miller Manufacturing Egg Flats](https://miller-mfg.com/products/egg-flats-30-count-5-x-6-package-of-12), checked live.
  Its description explicitly identifies a 30-egg, five-by-six filler flat. Other sizes are labeled this shed's own cartons.
- Gus, his farm and orders are invented, as the Rush footer and notes state.

#### Break it

`functional-results.json`: 2,418 passing browser assertions, including 243 Sort assignments,
72 Fills sets and all 1,536 decade selections. An independent nested-loop factor search checks all 100 orders.

- Shelf: one pair or all but the final pair cannot ship successfully. Repacking and turned copies never duplicate a pair.
  Sweeping rows one through twelve is the standard's systematic search method and remains valid.
- Sort: all Prime, all Composite, odd-means-prime, Neither guesses and every other bin combination were tried.
  Composite refuses an unproved tag. One row or one column cannot supply a proof; a nontrivial rectangle can.
- Multiples: every selected set was tried with exact counts. Wrong sets, copied order counts, zero, 100,
  fractions, exponent notation, whitespace and empty counts fail. DOM probes confirm blank and fractional fields block Ship.
  The real input handlers accept twelve cartons of six and nine cartons of eight for 72.
- Decade: every subset was tried. Only the exact prime set passes. Odd composites, no selection,
  all odds and extra even selections fail. Extra evens use the existing generic miss reason.
- Explore-copy: leaving Rush or switching away from an unfinished card changes its variant.
  The board and seal are hidden in Rush, and there is no answer-bearing empty shelf slot count.
- Score: the first miss resets unmarked work; the second records helped, never own. Misses persist through rerolls.
  Assistance is saved before reveal. Replaying a shipped card cannot improve its own count.
- Persistence and reset: own progress survived a fresh tab; Cancel preserved it; Confirm cleared board and Rush progress.
- `DOM-results.json` adds seven passing input, shipping, persistence and run-restart checks.
  `reload-reset-results.json` adds four passing reload and confirmation checks.

#### Voice walk

The tool uses Curio.voice, 27 fixed lines and the friendly-dad bank selection. Recorded voice is intentionally absent.
Held clicks used a 120 millisecond press and a two-second tap pace, with no change to the default Sound setting on voice paths.
The real jittered edge drag earned four by nine, followed by the remaining shapes for 36.
Main Pack log: fitHow once, then sealComp. The first action's own line can skip wPack under baseline rule 16;
the premise remains in the hint and Read. The keyboard-only run reached the handle and changed five rows to four.
Mode walk logged wFill, wBoard and wRush. Deliberate quick mode changes cut obsolete welcomes and fill results.
Rush main path after the welcome-list repair: wRush, everyHow, shipRight, then the next card.
`voice-every-settled.json` records those starts in order, without a cut on shipRight, and the next card open.
Side paths logged sortHow then proofHow; multHow; decadeHow then shipRight. All four Rush how lines started.
The Sort held-input walk shipped 13, 21 and 27 with the latter two proved by three-row cartons.
Repeated fit instructions spoke once and then stayed silent in the five-fit path. Event repetition is also covered by the final audit.
These are headless start/completion logs, not a listening review of recorded Achird audio.

#### Feel check

I walked all four modes and each kind of Rush activity as a student, including wrong proof placement and shipping.
Best moment: the final missing shape seals 36, the factor chips appear, and a correct order leaves on the truck.
The turned nine-row carton visibly returns to the four-by-nine twin instead of increasing the shelf count.
Flat moment one: a fit originally only added a label. It now sends a copy of the filled carton toward the shelf,
stamps the shape and gives the hen a cluck pose with an immediate chime.
Flat moment two: help originally read like a text answer. It now shows Gus pointing and, for shape cards,
filled mini-cartons for every factor pair before the assisted truck departure.
The first pallet painting hid the demonstration with boxes; the empty pallet redraw and separate skip counter fixed that distraction.
Both bar tools were bundled into Scratch and opened. `feel-comparison.jpg` places the earned seal beside Snowy Mail Route.
The painted shed has stronger material detail and depth than that reference, with a clearly manipulable central carton.
Beat Lab was also inspected for immediate, readable feedback. This tool's depth comes from changing mathematical tasks and proof requirements.

#### Done when

1. PASS for primary controls in inspected laptop and preview states; compact pager, Pack and Run were repaired and re-shot.
   The phone iframe has all seven scenes. Compact board targets remain below 44 pixels; see Left open.
2. PASS: four initial empty cups; real 36-pixel upward drag earns four by nine; nine rows glows the same twin.
3. PASS: 36 seals after rows 1, 2, 3, 4, 6; 13 seals prime; 1 seals neither. Board colors and square marks match.
4. PASS: rows update during re-deal; a new filling setting restarts immediately and settles correctly; mode changes cancel truck continuation.
5. PASS: 72 in sixes has twelve full cartons; 70 in fours has seventeen full cartons and a last carton with two empty cups.
6. PASS: 12 requires three pairs; a partial shelf fails; a second miss records Gus helped and shows the solution.
7. PASS: 21 needs a nontrivial proof; 27 in Prime produces missOdd. All Sort combinations were tested.
8. PASS: only six with twelve and eight with nine pass the first multiples card; wrong set and count reasons are distinct.
9. PASS: only 41, 43, 47 pass the first decade; marking 49 fails with missOdd. All subsets were tested.
10. PASS: Rush hides board and seal; exit and card navigation change the unfinished variant.
11. PARTIAL: PASS in the held-input and settled logs for how-line identity and result-before-next sequencing.
    Final audit repetition findings are qualified in Audit leads; recorded voice is still a production step.

#### Wave lessons

- Hint and voice: PASS. Hints update synchronously, name the next action and are read by the kit. How repetition uses kit heard state.
- Focus and layout: PASS in the keyboard run. Persistent controls are not rebuilt on row changes; boundary steppers retain focus with aria-disabled.
- Sizes: PARTIAL. Every required size was rendered, plus seven phone scenes. Compact board cells remain smaller than 44 pixels.
- No giveaways: PASS. Rush has no seals, colored board or unfilled shelf placeholders; variant changes block copying from exploration.
- Honest numbers: PASS. Exact cups, factors, skip counts, counts and progress come from the current state, with no probabilistic meter.
- Standards: PASS. All four parts of 4.OA.4 have a solo action and a corresponding puzzle check. No family engine applies.
- Motion off: PASS. Immediate settled filling, no travelling carton copy, stationary truck departure and no infinite visual loop.
- Short choice sets: PASS in targeted states. All carton sizes, proof crates, Fills choices and prime toggles remain visible.
- Resize mid-animation: elapsed fill state survives canvas resizing; the audit tests input/resize continuation.
- Late welcome: PASS. No welcomeAfter. Current-card scope drops obsolete narration. The welcome-list tuple ambiguity was repaired.
- Unknown stays unknown: PASS. Rush shows waiting empty cups, not a live fitted preview or a classified board.
- One look, one meaning: PASS. Empty cups are ringed and counted; board color has a matching icon and legend, including grayscale.
- Badge truth: PASS. Own and helped are separate, persistent and mutually exclusive; the judge checks before crediting either.
- Hint returns with state: PASS. Changing mode, order, selected tag or card updates the hint at once; results do not overwrite it asynchronously.
- No answer by copying words: PASS. Bin names do not appear on unsorted tags; exact counts are not supplied by the multiples card.

#### Audit leads

The audit was run once, with a forty-minute limit, on the frozen bundle in `audit-snapshot-egg-carton-factory.html`.
Its exact final/partial status and lead count are recorded below. It was not rerun after repairs.
It stopped at the forty-minute cap with 898 saved leads. Final walked-control resize stress remains incomplete.

- Compact board targets: retained as an explicit limitation. This also appears again behind the reset dialog in the audit snapshot.
  The final modal makes its background inert, so those background cells are not actionable while the dialog is open.
- Carton-size targets at 41 pixels: fixed by removing horizontal grid gaps in the compact panel. Final bounds are at least 44 pixels.
- Readout/shelf-tab overlaps: fixed by placing the tab inside the shelf. Final geometry checks and frames confirm separation.
- Nine-pixel turn note and crate sublabels: raised to ten pixels. Compact board symbols were raised to ten as well.
- Unnamed count field: explicit size-specific aria-labels now supplement the visible associated labels.
- Disabled Ship hint: while a selected count is empty or invalid, the hint now names only the open count boxes.
  The supplied fixed how-to retains its final conditional Ship step; it starts when Ship is initially available.
- Rush card focus loss/rebuilding: the three card buttons persist across card resets and selection.
- Board navigation focus loss: opening an order transfers focus to its carton handle with preventScroll.
  Panel controls now precede the long board in DOM order; automatic card advance restores focus to its first relevant action.
- Readout keep-region leads: visually false. The passive readout uses pointer-events none, so hit testing finds the canvas behind it.
  Its text is present and visible in the inspected frames. Real shelf-tab overlap was fixed separately.
- First-tap welcome warnings on Rows minus, Rows plus and Order minus: permitted by baseline rule 16.
  Their own fit feedback plays first; the packing premise remains in the current hint and Read.
- Five held clicks at a two-second pace were clean for all ten controls in the audit's repetition sample.
  The four quick mode-button welcome cuts are permitted by baseline rule 16. The quick Order minus cut stops
  a fit explanation for the departed order when the next order no longer fits; keeping that old statement would be stale.
- Mode-switch movement is intentional. Silent boundary steppers and selecting an already-current card are intentional no-ops.
- Additional visual/functional repairs found during frame review: fresh Fill entry caption, no nonexistent factor-chip invitation,
  a real modal pointer blocker, transient-copy cancellation, whole identical-run speech and stale changed-setting result cancellation.
  Compact Sort and Decade hide the hen where the number tags would cover it; other scenes retain the full hen.
- Calm Fill shows its final picture immediately while keeping the normal result-speech/tone timing. Epochs cancel obsolete timers.
  Motion off explicitly stops the idle light. These changes reconcile the spec's instant picture with the standing timing rule.

Final targeted evidence is in `post-audit-frames`, `post-*.json`, and `phone-final-frames`.
`post-audit-source.diff` and the frozen hashes identify the exact changes after the mechanical audit.

#### Frames looked at

Opened the two bar frames and every PNG from first-frames, student-frames, both matrix batches,
functional-frames, final-functional-frames, last-frames, settled-voice-frames, phone-frames,
phone-final-frames and pre-audit-frames. Large contact sheets and selected full-size frames are in Scratch.
Also inspected the final post-audit repair frames, the new keyboard path, all seven final phone scenes,
and the three targeted compact character-visibility views. The first attempt at those three views lost its Chrome connection.
The final art contact sheet includes all fifteen images, four of them people. Audit frames are listed in the disposition evidence.

#### Art made

15 final images, including 4 people assets: 460,464 bytes (449.7 KB). Recorded voice: 0 KB.
Final offline bundle: 711,321 bytes (694.6 KB), below the 2 MB goal.
Bundle SHA-256: `bf264f46285a42e87438ed55625661bc7fa5048e4e605ed3125690b8be77a96b`.
All fifteen spec assets were made during this build, processed only with art.py --rekey and placed in the tool.
Pulp and pallet were redrawn once each. All cutouts were viewed against pink as well as in their final scene.
Raw selected PNGs are in art/raw; final WebPs and the complete prompt set are in art/.

#### Art still to paint

None. A fresh people-art review and production recording of the friendly-dad voice remain for the next stage.

#### Engine changes wanted

No family-engine or shared-kit change was needed. No shared files were edited.
Audit harness suggestion: `scripts/audit_tool.py`, the keep-region hit test inside `PAGE_JS`, should account for
passive pointer-events-none captions when distinguishing visual occlusion from pointer targeting.

#### Left open

- Compact Order Board cells cannot simultaneously be ten by ten, all visible in the smallest previews, and 44 pixels each.
  The current version preserves the specified whole board and smaller compact cells. This is a real target-size limitation.
- On compact sealed orders, secondary seal details and factor chips can require panel scrolling; primary controls stay first.
- No recordings were made. Browser speech is the fallback, with a declared 27-line production inventory.
- Cold review, including fresh review of the four Gus portraits, has not been performed in this Build-only session.
- The single audit stopped at forty minutes with 898 saved leads and 105 inspected frames. Its saved report is partial.
  All size/state checks, all four control walks, ten five-click samples and the quick-tap samples were saved.
  The final resize stress of walked controls was interrupted; it is not claimed complete.
- Windows denied the timeout helper's process-tree termination. The owned audit browser was then closed over CDP,
  and the audit exited through its cleanup path. The resulting harness timeout is not an application exception.
- No second audit was run. The final targeted source and frames include repairs after that frozen snapshot.
- Every launched browser/server is closed and host.html is absent. Final deliverable: `egg-carton-factory.html`.

Final targeted checks: 30 passing assertions. Build only; stop for cold review.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: egg-carton-factory

#### Played

Cold Grade 4 solo/projector play covered all modes and four Rush tasks before builder notes/source.
The rich shed, immediate re-packing and turned-pair glow are strong. Later held-input walks shipped each task kind correctly.

#### Findings fixed

- Should fix, general, Rush voice: Every shape how-to was dropped behind the generic welcome on the two-second Pack/Ship path. Task instructions now lead.
- Should fix, general, Pack voice: queued fit/turn teaching now requires the same order to still fit; proof speech names both rows and columns.
- Should fix, general, Pack graphics: green shape labels disappeared into the painting. Added opaque paper plaques with green outlines.
- Should fix, general, assisted answers: six proof cartons overflowed the compact panel. Exact SVG cartons now fit a three-column grid; reading time follows text length.
- Should fix, general, persistence: a saved seal could reload with a partial shelf. All previously earned pairs now restore together.
- Should fix, general, extreme text: corrected singular egg, cup and full-column wording.
- Polish, general, finish: the final recap was overwritten. Banner and feedback now retain the student's own/helped totals.
- Polish, general, weakest art: flat Multiples cards now have shaded exact-layout carton drawings, paper shading and pin details.
- Should fix, general, compact seal: factors and the next action fell below the panel; phone focus could scroll the hint away. Reclaimed header space, paired Next/Reset controls and concise seal text now keep every factor and primary control in view.
- Should fix, general, result focus: disabled Ship dropped focus to the page. Help and shipping regions now receive focus until the next card. First-miss feedback receives focus, then returns it to the retry action. Checked answers lock during shipping; Multiple feedback names only visible controls. The old readout hides behind the help explanation.
- Should fix, general, active selection: re-entering the selected mode/card could reset unfinished work and cut its welcome. Current selections now preserve work and speech; obsolete fit speech stops when the new carton has gaps, with the search instruction retained in the hint.
- Should fix, general, numeric field: native spinner space clipped the largest order on narrow inputs. Adjacent Order buttons now provide stepping while 100 remains fully readable.

#### Findings left

- Should fix, general, compact Order Board: its all-visible 10 by 10 layout has targets under 44 pixels. See Left open for the specification conflict.

#### Break it

Independent drive evidence: `review-break-results.json` and final `post-break-results.json`: 2,323 assertions each, zero failures.

- Every shape: empty/partial shelves cannot earn credit; duplicates and turned copies cannot increase the count. Sweeping rows is the specified systematic search skill.
- Sort: all 27 assignments per variant tested, including all Prime, all Composite and odd-means-prime. One-row/one-column cartons do not prove composite; nontrivial rectangles do.
- Multiples: all eight Fills sets per variant, copied order/size counts, blanks, zero, 100, fractions, exponent notation and spaces tested. Only exact selected sizes and quotients pass.
- Decade: all 512 selections in each decade tested. All odds, all numbers, none, extra evens and omitted primes fail.
- Credit: first miss gives no credit; second miss is helped. Cancelling help or replaying cannot turn helped into own; misses survive rerolls.
- Explore-copy: leaving Rush changes the unfinished variant; seals and board remain hidden in Rush.
- Seal/board: independently enumerated all factor pairs 1 to 100. Reload now restores all five earned pairs for 36, matching its factor list.

#### Voice walk

Held clicks: 120 ms, ordinary actions two seconds apart, default Sound on. Read final `last-voice-main-*.json` and `voice-repeat-*.json`.
Pack edge, row search and turn, Fill size/Run, Board, Rush row search/Ship:
`wPack, fitHow, sealComp, turnHow, wFill, fillYes, wBoard, everyHow, wRush, shipRight` started in that order.
Sort: `everyHow (cut), sortHow, wRush, shipRight`. Multiples: `everyHow, wRush (cut), sortHow (cut), multHow, shipRight`.
Decade: `everyHow (cut), wRush (cut), decadeHow, shipRight`. Cuts follow explicit shift/card navigation.
Count fields were populated through their input handlers. Explicit mode changes stop departed speech; no stale line followed the switch.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| fitHow, five fits | how | 1 | 1 |
| fillYes, five runs | event | 5 | 5 |

Read interrupted speech, worked with Sound off, and released immediately on mode change. Actual Achird recordings are absent; this is browser-speech timing evidence.

#### Facts checked

- All four learning actions match [CCSS 4.OA.B.4](https://www.thecorestandards.org/Math/Content/4/OA/) and [Illustrative Mathematics](https://tasks.illustrativemathematics.org/4.OA-2), checked live.
- Prime has exactly two positive factors; composite has a nontrivial pair; 1 is neither: [Math is Fun](https://www.mathsisfun.com/prime-composite-number.html), checked live.
- Two is the only even prime; odd composites and all three decade prime sets: [Math is Fun prime list](https://www.mathsisfun.com/prime_numbers.html), checked live plus independent enumeration.
- Turned pairs repeat; the search stops when the smaller side passes its partner: [Math is Fun factor search](https://www.mathsisfun.com/numbers/factors-all-tool.html), checked live plus enumeration.
- Every 1-to-100 factor list, all 36 Rush variants, square 36's five shapes/nine factors, maximum six shapes and smaller side at most ten: `review-numbers.json` and independent browser checks.
- 72/6=12, 72/8=9; 70/4=17 remainder 2; all other displayed counts/remainders: independent integer division, under the CCSS factor/multiple definition above.
- The real 30-egg, 5-by-6 flat: [Miller Manufacturing](https://miller-mfg.com/products/egg-flats-30-count-5-x-6-package-of-12), checked live. Other layouts are explicitly fictional shed cartons.
- Gus and the farm orders are fictional, consistently stated in the footer and notes. Notes open with the three required sections.

#### Sensitivity

Four flagged people assets show the same fictional older farmer. Fresh inspection found consistent identity, friendly expressions, natural hands and no stereotype.
No cultural tradition, Indigenous content, religion, hard history or body instruction is claimed. No added cultural review issue identified.

#### Flattest moment left

The middle of a six-shape factor search is methodical. It remains the intended systematic search; the later Sort, Multiples and Decade tasks supply variety.

#### Graphics

All 15 paintings inspected in a contact sheet and scenes, including the full truck, hen poses and Gus poses. All four people flags confirmed.
Kept the coherent warm artwork. Improved the code-drawn cards, label plaques and assisted proof set; no painting was weakened or removed.
Art: 449.7 KiB. Bundle: 700.7 KiB. `review-comparison/sheet-0.png` places this tool beside Snowy Mail Route; Beat Lab was also opened.
All required widths inspected, including 375 in the host; grayscale, Motion off, keyboard input, one/100 eggs, short fills, seals and final recap checked.

#### Audit

Audit not finished: the 40-minute cap interrupted resize stress. The partial `review-audit/audit.md` preserves 429 leads and 120 frames; the exact old bundle is `review-audit-bundle.html`.

- Completed every listed size/state, Motion off, all four mode control walks, ten five-click samples and ten quick-tap samples. Full resize-stress coverage is not claimed.
- Four hundred rows confirm the single compact-board target conflict, left open below.
- Repaired the confirmed compact seal/hint visibility, shipping focus, active-selection welcome interruption and assisted-caption overlap leads. Scoped geometry, real-click frames and cheat replays verify the repairs.
- Passive readout hit-test coverage and hints behind the inert reset dialog are false positives. Conditional Ship wording describes a later enabled step, exactly as specified.
- The three first-tap welcome skips follow baseline rule 16. Rapid Order changes stop obsolete speech; keeping the old fit statement would contradict the new carton.
- No application errors in completed checks. The iframe host's favicon 404 and timeout shutdown stack are harness output. An earlier Chrome connection loss was retried smaller. A duplicate late drive attached to the existing owned browser and disconnected when its original run closed it; all eight final frames, four voice logs and 2,323-check result were saved.
- No second audit. Owned browsers/server closed after checks.

Sealed-order geometry passed at 680 and 375 for 36, 60, 72 and 100: hint, full factor set and all primary controls visible; targets at least 44 pixels. Re-shot each affected compact mode and both result-focus states.
Recomputed contrast: ink/paper 14.79:1, muted/paper 6.59:1, white/brand 6.40:1, new label/paper 9.55:1. [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); `review-palette.json`.

#### Left open

- The review rule prohibits changing a conflicting spec. Kept its whole compact board instead of adding navigation or scrolling; documented the target limitation in notes/handoff.
- Spec totals are inaccurate: 15 assets and 36 variants, not 14/27. Some correct counts equal shown sizes (48/6=8, 54/6=9); exact quotient checking remains correct.
- No audio was recorded, per build rules. Browser speech was exercised; the named bank voice still needs its production recordings.
- Initial read-only commands and two initial shell-parsing failures lacked a full wrapper; all bundle, drive and audit checks had explicit caps.
- Only authorized tool/Scratch paths written; no commits. Host page removed and owned Chrome/server processes closed. Stop after this report.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Egg Carton Factory handoff

#### Structure

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

#### Tricky behavior

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

#### Decisions and specification tensions

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

#### Sensitivity

Gus is a fictional older farmer with warm brown skin, gray stubble, a canvas cap, plaid shirt and denim apron.
All four people assets are marked people true. The set shows one character consistently across four expressions.
The build contact sheet is `_scratch/egg-carton-factory/art-contact.jpg`. A fresh cold reviewer should inspect
the people set for respectful representation, consistent identity, natural hands, friendly expression and clean edges.
No personal questions, body instruction, religion, hard history or Indigenous cultural content is included.
This build does not authorize publishing or deployment.

#### Art and voice

All 15 final WebPs were generated with the built-in OpenAI image tool and processed through art.py --rekey.
Prompts and people flags are in art/prompts.json; raw originals are in art/raw. The flat pulp and empty pallet
were redrawn once each after their first versions contained unwanted cup geometry and boxes respectively.
Generated images remain full silhouettes and are hidden where the compact layout requires it.
The hen is hidden in compact Sort and Decade scenes because their number tags otherwise cover its head.

The voice bank selection is friendly-dad, Achird. All 27 fixed lines are in voice/lines.json.
No audio was recorded, as requested. The built file falls back to browser speech through Curio.voice.
The bank voice itself is still a production recording step, not a claimed listening review in this Build run.

#### Evidence

Scratch holds `numbers.json`, the independent arithmetic script, browser assertions and held-input student walks,
responsive and phone screenshots, the art contact sheet, reference frames and the one bounded audit.
Read codex-report.md for final results and unresolved audit leads. No git operations or polish round were performed.

#### Cold review repairs

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

#### Engine changes wanted

No family engine change. Shared kit files and engines were not edited.
Audit harness suggestion: scripts/audit_tool.py, PAGE_JS keep-region hit testing, should recognize visible passive
pointer-events-none captions rather than treating the canvas returned by hit testing as a visual obstruction.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)
