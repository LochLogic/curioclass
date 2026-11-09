# Codex report: egg-carton-factory

## Built

Four complete modes: Pack Station, Fill Line, Order Board and Rush Orders. Rush has all 12 cards and 36 variants.
Responsive exact-count cartons, column-first egg packing, real edge dragging, canonical factor shelves,
turned-pair glows, seals and factor chips, timed filling, skip counts, proof crates, exact counts,
prime toggles, two-miss help and truck departures. Progress stays on this device; clearing it asks first.
The source is readable, uses the shared kit and makes no application network requests.
All work stayed in the authorized tool and Scratch folders. No commits, publishing or polish round.

## Numbers check

`check_numbers.py` independently recomputes all 100 orders, factors, classifications, maxima,
all nine multiples variants, the decade prime sets, empty cups, durations and palette contrast.
`numbers.json` contains the results. Most pairs: six; largest smaller side: ten; 36 in five rows: four empty cups.
The spec has 15 named images, not 14, and 36 Rush variants, not 27.
Its claim that a correct count never equals a shown size is false: 48/6=8, 48/8=6, 54/6=9, 54/9=6.
The listed answers were preserved and exact quotient validation is used. Sources' extra 91 to 99 decade was checked but not added.
Contrast on paper: ink 14.79:1, muted 6.59:1, brand 5.99:1, white on brand 6.40:1.
Gold with ink: 8.32:1; gold outline on paper: 5.97:1; white on composite blue: 6.46:1.
One-gray with ink: 10.53:1; empty rings on pulp: 3.65:1; ink on pulp: 9.69:1.

## Facts checked

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

## Break it

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

## Voice walk

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

## Feel check

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

## Done when

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

## Wave lessons

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

## Audit leads

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

## Frames looked at

Opened the two bar frames and every PNG from first-frames, student-frames, both matrix batches,
functional-frames, final-functional-frames, last-frames, settled-voice-frames, phone-frames,
phone-final-frames and pre-audit-frames. Large contact sheets and selected full-size frames are in Scratch.
Also inspected the final post-audit repair frames, the new keyboard path, all seven final phone scenes,
and the three targeted compact character-visibility views. The first attempt at those three views lost its Chrome connection.
The final art contact sheet includes all fifteen images, four of them people. Audit frames are listed in the disposition evidence.

## Art made

15 final images, including 4 people assets: 460,464 bytes (449.7 KB). Recorded voice: 0 KB.
Final offline bundle: 711,321 bytes (694.6 KB), below the 2 MB goal.
Bundle SHA-256: `bf264f46285a42e87438ed55625661bc7fa5048e4e605ed3125690b8be77a96b`.
All fifteen spec assets were made during this build, processed only with art.py --rekey and placed in the tool.
Pulp and pallet were redrawn once each. All cutouts were viewed against pink as well as in their final scene.
Raw selected PNGs are in art/raw; final WebPs and the complete prompt set are in art/.

## Art still to paint

None. A fresh people-art review and production recording of the friendly-dad voice remain for the next stage.

## Engine changes wanted

No family-engine or shared-kit change was needed. No shared files were edited.
Audit harness suggestion: `scripts/audit_tool.py`, the keep-region hit test inside `PAGE_JS`, should account for
passive pointer-events-none captions when distinguishing visual occlusion from pointer targeting.

## Left open

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
