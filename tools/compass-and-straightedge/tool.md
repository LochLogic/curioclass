# compass-and-straightedge: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: compass-and-straightedge (Curiosity No. 09)

#### Built

An offline drafting instrument on cream paper, with a swinging brass compass, unmarked steel straightedge,
computed crossing points, ink, erasure, measurements, a chronological record, undo and redo, pan and zoom.
The lower-left maker's plate and Manual, and the separate Motion, Sound and Read lamp panel, carry the family marks.
The Book has 15 independent pages. Four local save slots, given sheets and printing are in the Paper cabinet.
The wide log collapses; narrow screens use a log drawer. Phone Book and log drawers open at the bottom.

Bundle: **83,369 bytes (81.4 KiB)**, below the 500 KB specification budget and the 2 MB goal.
Source: [src.html](src.html). Offline file: [compass-and-straightedge.html](compass-and-straightedge.html).
Build only: no commits, deployment, shared-engine edits or polish round. Required tool files are present.

#### The real material

- Original analytic geometry: double-precision line/line, line/circle and circle/circle intersections;
  segment bounds, isolated tangencies, coincident cases, and a 1e-9 sheet-unit merge tolerance.
  Counts and measurements come from the drawing, not a reference answer. No outside dataset.
- Euclid, *Elements*, T. L. Heath translation, Cambridge 1908: the 14 supplied enunciations and three postulates,
  Books I and IV constructions, and XIII.8's pentagon relationship. Public domain in the US.
  The specification's supplied wording was used; no Perseus transcription markup was copied.
- MacTutor, University of St Andrews: Wantzel, Gauss, Lindemann, Mohr and Mascheroni historical facts,
  paraphrased from the specification's named sources. Facts are not copyrightable; article text retains copyright.
  No article prose or images were reproduced. Links and permission notes are in the Manual and metadata.
- Original code-drawn instruments, paper and Book figures. No painted data, downloaded art or outside library.
  Blank sheets retain the reference unit as u, so new free points named A and B do not falsely redefine AB.

#### Break the instrument

- **29 numerical assertions passed**: intersections, tangencies, disjoint and coincident circles,
  finite-segment bounds, parallels, right and undefined angles, equilateral sides and angles, and six-step closure.
- I.2 transfers a length using made points with the collapsing compass; its opening remains zero.
- The full Book-method pentagon replay uses I.46, II.11, I.2, IV.10, IV.2 via I.23, and I.9 before IV.11.
  Result: **47 objects, 1,115 made points, zero free points**, equal sides, and diagonal/side **1.6180339887498931**.
  This is an actual instrument replay, not just the finished reference figure. See pentagon-method.js and its result JSON.
- An initial rapid pentagon replay timed out while repainting intermediate states. Geometry now updates synchronously
  and SVG painting coalesces into the next frame. The same constructive replay then passed without console errors.
- Jittered, held real drags make the two circles and I.1 sides. Keyboard input measures 60.00 degrees.
  Degenerate or unmade anchors are rejected. Repeated free points do not create false free-point log entries.
- Undo/redo restores geometry and ink; erasing a point removes dependent objects. Empty paper and both zoom bounds work.
  Local save/load restores the drawing; blocked storage reports the problem while preserving the current paper.
- Real phone panning and two-finger pinch passed in a 375x812 iframe; scale changed from 114.2308 to 159.9231 px/unit.
  Two circles and four points remained usable, with no page scroll. A resized running sheet retained its objects.
- Forty rapid circle additions and their undo passed. The tested clean triangle prints on one landscape page with its log,
  with zero visible instrument decorations and zero external network requests. See print-check.json and printed-sheet-final.pdf.
- Final focused checks verify a live circle, log collapse/reopen, a clear point label beside the radius tag,
  u on blank sheets, and five source links at least 44 by 44 pixels. A disconnected Chrome batch passed on its smaller retry.

#### Voice walk

knowing-guide is selected in voice/lines.json; no audio was recorded, as instructed. The shared kit uses browser speech fallback.
The main drag path speaks "Drag from A to B." once. The 606.4-second replay records one welcome and one requested Read,
with no automatic speech on Book pages or repeated drawing actions. Read also speaks with Sound off.
Read includes the current hint, last log sentence and selected readout. Status regions expose point names and measurements.
The first timed automation left the Manual open after an ineffective synthetic Escape. Explicit Escape handling and cursor
reset were added, virtual key codes corrected, and the full timed walkthrough was replayed with all adult-path drawers closed.

#### Short test

The controlled agent exploration lasted **606.4 seconds**, using grade-10 and adult lenses. This is not a child user study.

- Would a kid open it unassigned? Likely: the first drag physically sets and swings the compass; crossings invite another action.
- Would an adult play for fun? Yes by this assessment: collapsing-compass transfers and the full pentagon are real construction problems.
- Is the real thing the interface? Yes: every working circle, segment, crossing and readout comes from the analytic drawing.
- Does it work without a score or finish? Yes. The Book was browsed in all 15 positions in a deliberately mixed order,
  with no prerequisites, ticks, ratings or saved page achievements. Its method steps appear only when requested.

Our instrument beside Elements Inspector, both opened and used during the build:

![Compass and Straightedge beside Elements Inspector](../../_scratch/compass-and-straightedge/targeted/frame-comparison.png)

#### Lesson creep check

The requested word search was run on src.html and the voice lines. No score, level, goal, sticker, badge, correct,
wrong, try again, complete or well done hits remain. "Points" denotes geometric points and their data structures,
never rewards. The log's numbers order construction moves; the zoom percentage is magnification.
There is no kit header, mode-pill row, task ladder, quiz, timer, celebration or finish screen.

#### Done when

| Item | Result and evidence |
|---|---|
| 1. Open and draw two circles | PASS: initial A/B and instruments; real drags produce two circles and two crossings. |
| 2. I.1 lengths and angles | PASS: 1.0000, 1.0000, 1.0000 and three computed 60.00-degree angles. |
| 3. Six-step closure | PASS: six made-point circles return to the original rim point, including with the collapsing compass. |
| 4. Book-method pentagon | PASS: full 47-object construction from A/B alone; measured ratio 1.6180. |
| 5. Collapsing compass and I.2 | PASS: opening returns to zero and the copied length matches numerically. |
| 6. Made points, log, undo/redo | PASS: invalid anchors rejected; chronological log and dependency-aware erasure restore through history. |
| 7. Fifteen independent pages | PASS: every page browsed out of order; ghosts only on request; no completion marks. |
| 8. Keyboard, announcements, Motion off | PASS: drawing, free points, measurement, ink, erasure, history and view keys; named native controls; instant calm circles. |
| 9. Responsive sizes | PASS: all eight STANDARDS sizes, including the real 375x812 iframe, with no page scroll. |
| 10. Print, offline, checker, punctuation | PASS for the tested sheet: one print page plus log; no requests; production checker functions pass; no em dashes. |
| 11. Honest short test | PASS: answered above with the frame comparison and the Book's deliberately nonsequential exploration. |
| 12. No lesson game layer | PASS: source and voice search, visual inspection and timed use. |

The opening's implied switch from compass to straightedge is made explicitly by the student; no automatic tool change.
Join A to B as well to close the drawn outline. Its three-vertex triangle can be measured before that final stroke.
The trisection note distinguishes particular trisectible angles from the impossible general construction.
The user's stop instruction takes precedence over the machinery's early-report instruction, so this report is written last.

#### Audit leads

The mechanical audit ran once and finished: **320 leads, 23 frames**. It reports clean Motion-off and mid-action resize checks,
no errors on 19 held-control paths, and clean recorded repeated/rapid speech paths.

- 201 overlap leads: the focusable full-screen SVG lies under its instruments, maker's plate and measurement tags by design.
- 112 hidden-background leads: modal Book, Manual and Paper drawers intentionally cover the inert paper controls.
- Five small source links: fixed to 44-pixel minimum targets, confirmed by the final DOM measurement and frame.
- One scroll-panel lead: bibliography links are below the first viewport of the long, scrollable Manual; its Close stays available.
- One missing-hint lead: the permitted first-run hint disappears after the first drawing action.
- Sound cutting speech and Read skipping the welcome are the specified kit behaviors, not missing narration.

The full audit was not rerun after the focused source-link, unit-label, redraw and log-control fixes.
Those changes received targeted checks instead. The global check_tools.py entry point would rebundle other tools,
so its actual check() and notes_sections() functions were run on a scoped draft mirror, with all production rules intact.

#### Frames looked at

Beat Lab, Elements Inspector, Span and Spire, Pocket Universe; all early and full-size frames; grayscale and Motion off;
the real-drag triangle; Book and ghost frames; corrected timed student/adult frames; phone circles and Book;
both print previews; ratio and full constructive pentagon frames; final source-link, unit and log-control frames.
All 23 audit PNGs were inspected in four contact sheets, including short and phone Book pages and all drawer states.
Failed-fixture and first-walkthrough evidence is preserved separately rather than presented as passing evidence.
Evidence and hashes: ../../_scratch/compass-and-straightedge/validation-manifest.json.

#### Art made

No raster images. Paper tooth and lamp gradient, brass compass, steel straightedge, cloth Book control, point labels,
pencil and ink strokes, and exact Book figures are drawn in CSS and SVG. No placeholders or art left to paint.

#### Engine changes wanted

None required. Optional: kit/curio.js showMotion() and Curio.init() could accept a power-label formatter,
so an instrument need not replace the shared emoji labels in onMotion/onSound callbacks. The kit was not edited.

#### Left open

- The knowing-guide recording is not produced in Build; browser fallback depends on the device's installed speech voices.
- No physical school-Chromebook frame-rate measurement, screen-reader hardware walk or human child usability study was performed.
- Very dense constructions can have overlapping point labels; pan and zoom inspect them. The 600-object guard and
  numerical limits are disclosed in the Manual. A month of depth is a design assessment, not a month-long observation.
- Print pagination was verified on the documented triangle sheet, not every possible length of construction record.
- The marked-ruler extension remains deferred, following the specification's lean. No plan.md was invented; this remains a second card.
- No test servers or debugging listeners remain on the assigned ports; cleanup-check.json verifies kernel TCP state.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: compass-and-straightedge

#### Played

Grade-10 and adult lenses: jittered held drags, the two-circle triangle, keyboard drawing and measuring, independent Book browsing, retained and collapsing openings, ink, erasure, history, paper, saves and printing. The paper and compass invite experiments; the Book was the weakest response.
Process limitation: the first cold load timed out. I opened the builder's report after the retry's opening frame but before the first active input session. This was not a strictly blind play-first review, and I did not conduct a fresh, timed ten-minute play session. Initial document reads preceded the explicit timeout wrapper; subsequent shell commands were bounded.

#### Findings fixed

- **Blocker, general, `src.html` / `lineShape`:** an infinite line vanished when its two defining points were far outside the viewport. Clip the actual infinite line to the paper, including very short defining segments at minimum zoom.
- **Blocker, general, `refreshSlots`:** malformed saved geometry could replace the current state before rendering failed, contradicting the preservation message. Validate references, geometry, arrays, view and Book state before checkpoint/restore.
- **Should fix, general, voice:** Read repeated "Drag from A to B" on blank paper and with other instruments. Added state-specific, requested instructions, matching voice-bank entries, and cancellation on tool/sheet/Book changes. The opening hint remains the only automatic narration.
- **Should fix, general, Book IV.16:** the purported bisector was drawn at -66 degrees instead of midway between -18 and 30 degrees. It now points at 6 degrees, making the adjacent arc 24 degrees.
- **Should fix, general, trisection page:** the caption described 30 and 15 degrees while only a 30-degree ray existed. Added the requested second halving as a separate ghost stroke.
- **Should fix, general, Manual:** "Equal circles on the ends of AB" was insufficient to guarantee an equilateral triangle. It now specifies that each circle passes through the other endpoint.
- **Should fix, general, sources:** named MacTutor's actual CC BY-SA 4.0 article-text licence and distinguished the factual paraphrases used here. Added separate Heath volume links. Metadata carries named sources and permissions.
- **Polish, general, Book response:** the modal hid the new paper stroke while its own figure stayed static. Its figure now shows the requested construction, fits its extents, and darkens the newest stroke. The finished reference remains available before stepping or after Clear ghosts.
- **Polish, general, capacity:** the 600-object boundary now has a visible readout and a useful requested Read, rather than only an assistive announcement.
- **Should fix, general, audit frames:** close point names no longer share a position when there is room to place them separately; fine leaders retain their anchors. The phone zoom tag clears the idle compass, and the short preview's resting edge clears the lower crossing's label.
- **Should fix, general, counters:** singular nouns now read "1 point", "1 circle" and "1 line". Very small nonzero zoom values use scientific notation rather than rounding to "0%".
- **Should fix, general, rapid voice input:** repeated Compass presses cut the only opening hint. Selecting an already active instrument now preserves valid speech; actual state changes still cancel stale speech.

#### Findings left

- **Polish:** dense constructions still crowd point names. The 47-object pentagon can produce 1,115 intersections; its measurements remain valid, but Fit is a poor inspection view for that density. Pan and zoom remain necessary.
- Review-process limitations are stated under Played and Left open; they are not represented as passing checks.

#### Break it

- No score, check, quiz, achievement, target ladder or finish screen exists. No reward can be earned by a slider sweep or tap rhythm.
- Real A-to-B and B-to-A drags produced two circles and two crossings. Joining the upper crossing to both ends and AB gave 1.0000-unit sides and three 60.00-degree angles.
- Eighteen independent numerical assertions covered coincident/disjoint/contained circles, tangencies, segment bounds, parallels, right/undefined angles and a six-circle made-point walk. It returned to B, with six sides rounding to 1.0000 and zero free points.
- Reviewed and reran the builder's full constructive pentagon fixture, rather than accepting its reported result: 47 objects, 1,115 points, zero free points, collapsing opening zero, equal sides, diagonal/side 1.6180339887498931. This includes I.2 transfers.
- Attempted 605 rapid additions: exactly 600 accepted; undo restored 599 and redo 600. Coincident duplicate circles remained responsive. This is not a maximum-density memory benchmark.
- Both zoom bounds, blank paper, duplicate/degenerate anchors, rapid instrument changes and resize during a circle were exercised. The repaired distant-anchor line spans the viewport; the audit also exercises a 2e-9-unit defining segment at minimum zoom.
- Damaged slot with missing point references: live state remained byte-for-byte unchanged and the failure message appeared. All four valid device slots saved and loaded.
- Keyboard path placed two free points and joined them; another path selected three triangle points and measured 60.00 degrees. Retained opening, Euclid's rule, ink, erase, undo/redo, Log, Manual, Book, Clear ghosts, Motion and Sound were exercised.
- Print control invoked printing. Independent PDF output contained one page with the short construction and log; the print frame contained no instrument controls. Network capture recorded zero external requests.
- Evidence: `../../_scratch/compass-and-straightedge/review-play/`, `review-fixed/`, `review-slots/`, `review-numbers/`, `review-print/`, and their adjacent scripts/JSON results. Phone-host favicon 404s and one incorrectly quoted test selector were fixture faults; the corrected slot batch had zero errors.

#### Voice walk

Held inputs at about two-second pace, Motion and Sound on: Compass, A-to-B, B-to-A, Edge, C-to-A, C-to-B, A-to-B, Read. Then keyboard Measure, Read; Sound off, Point, Read; rapid tool changes, blank paper, Read.

| Line or kind | Expected | Observed |
|---|---:|---:|
| Opening "Drag from A to B" | 1 automatic | 1 |
| Main-path requested Reads | 4 | 4 |
| Extra automatic instructions after five tool-switch pairs | 0 | 0 |
| Repeated blank-paper Read, separate batch | 5 | 5 |

Read order: straightedge instruction plus the last move and triangle values; measurement instruction plus 60.00 degrees; free-point instruction; blank-paper instruction. Sound-off Read worked. The final speech queue was empty; rapid tool/sheet changes did not leave stale narration. All 14 fixed hints match `voice/lines.json` and `allLines()`. Evidence: `review-voice/results.json`. After the audit's same-instrument fix, a final voice batch timed out before loading; its single smaller retry passed the full triangle drag path and Read, with one uninterrupted welcome after two Compass presses 0.7 seconds apart, one requested Read and zero errors (`review-voice-retry/results.json`). No recorded knowing-guide clips exist; this tests browser fallback and its log, not recorded performance.

#### Facts checked

Source checks were made on 2026-11-05. No outside dataset is incorporated. Reference downloads and the retrieval script are under `../../_scratch/compass-and-straightedge/data/review/` and `review_sources.py`.

- **Fourteen enunciations and three postulates:** Heath, *The Thirteen Books of Euclid's Elements*, Cambridge 1908, public domain in the US: [I-II](https://archive.org/details/thirteenbookseu02heibgoog), [III-IX](https://archive.org/details/thirteenbookseu00heibgoog), [X-XIII](https://archive.org/details/thirteenbookseu03heibgoog). Matched the supplied wording to the primary OCR, accounting for four obvious OCR errors, and cross-checked the corresponding [David Joyce / Clark University propositions](https://mathcs.clarku.edu/~djoyce/elements/bookI/bookI.html). Clark text was used for verification, not copied into the tool. Sampling: the 14 specified enunciations and all three specified postulates, not entire books in the bundle.
- **Equilateral triangle, midpoint, angle bisection, perpendiculars, parallels, squares, copied lengths:** corresponding Heath I.1, I.2, I.3, I.9-I.12, I.23, I.31, I.46 and IV.6; Clark's independent presentation; recomputed engine examples. A collapsing compass's equivalence is a construction model, not a claim about a surviving physical compass owned by Euclid.
- **Hexagon side equals radius; pentagon diagonal/side 1.6180:** Heath IV.15, IV.11 and XIII.8; [Clark IV.15](https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV15.html) and [XIII.8](https://mathcs.clarku.edu/~djoyce/elements/bookXIII/propXIII8.html); independently checked geometric outputs and (1+sqrt(5))/2. Original calculations and diagrams, no licensed data copied.
- **General trisection impossible, Wantzel 1837, particular exceptions:** [MacTutor Wantzel](https://mathshistory.st-andrews.ac.uk/Biographies/Wantzel/) and [W. Kahan, Berkeley, *Approximate Trisection of an Angle*](https://people.eecs.berkeley.edu/~wkahan/Trisect.pdf). Only facts are incorporated; source prose is not reproduced. The corrected diagram shows 60, 30 and 15 degrees, never a claimed 20-degree construction.
- **Gauss, 1796, age 18; constructible 17-gon and impossible 7-gon:** [MacTutor Gauss](https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/), [Gauss's diary, March 30, 1796](https://tildesites.geneseo.edu/~johannes/gdiary.pdf), and [Freitas and Tavares, *Dividing the Circle*](https://webpages.ciencias.ulisboa.pt/~pjfreitas/pdfs/DividingTheCircle.pdf). Age follows from April 30, 1777 birth before that year's birthday. Facts only; no diary translation or journal figures incorporated.
- **Lindemann, pi transcendental, 1882; circle squaring impossible:** [MacTutor Lindemann](https://mathshistory.st-andrews.ac.uk/Biographies/Lindemann/) and [Lutzen, *The Algebra of Geometric Impossibility*](https://doi.org/10.1111/j.1600-0498.2009.00160.x). Facts only; no source prose incorporated.
- **Mohr 1672, Mascheroni 1797; compass-only point construction:** [MacTutor Mascheroni](https://mathshistory.st-andrews.ac.uk/Biographies/Mascheroni/) and [Hungerbuhler, *A Short Elementary Proof of the Mohr-Mascheroni Theorem*](https://www.math.ch/norbert.hungerbuehler/publications/A_Short_Elementary_Proof_of_the_Mohr-Mascheroni_Theorem.pdf). Facts only, no article text/figures incorporated. MacTutor's actual article-text terms are [CC BY-SA 4.0](https://mathshistory.st-andrews.ac.uk/Miscellaneous/copyright/), explicitly named in the Manual and metadata.
- **Numerical honesty:** original JavaScript geometry, 1e-9 point merge, four-decimal lengths and two-decimal angles. Floating-point measurements are checks on drawings, not symbolic proofs; the Manual retains that distinction and the finite capacity disclosure.

#### Sensitivity

Historical attribution only: retain Mohr's priority alongside Mascheroni, Wantzel's general-impossibility qualifier, and Heath's translator credit. No people imagery, cultural stand-ins, hard history or body content. No new sensitivity judgment is needed for the mathematical diagrams.

#### Flattest moment left

Advanced Book compound constructions still require patient reading. The repaired moving reference gives each press a material response, but the pentagon's full method remains dense. It stays a browsable reference, without prerequisites or achievement marks.

#### Graphics

Preserved cream paper, brass and steel instruments, graphite/ink contrast, maker's plate and quiet Euclid field note. No raster art, placeholders, people or external graphics. Bundle: **90,431 bytes**, about 88.3 KiB. Inspected initial, drags, triangle, Book, blank, keyboard, extremes, repaired states, grayscale, print and all 32 audit frames. Ten final scoped frames confirm the small-screen and extreme-value repairs.

#### Short test

- Would a kid open it unassigned? **Likely yes:** the first two drags yield a surprising, usable pair of crossings. This is an informed reviewer assessment, not observed child testing.
- Would an adult play for fun? **Yes:** actual retained/collapsing constructions and the pentagon have depth without a game layer.
- Is the real thing the interface? **Yes:** circles, straight lines, computed intersections and measured relationships are the working surface; requested Book strokes now remain visible.
- Does it work without score or finish? **Yes:** no goal, score, level, quiz, kit header or finish screen. The source search found only geometric uses of "points" among the lesson-creep terms.

| Compass and Straightedge | Elements Inspector comparison |
|---|---|
| ![Working triangle](../../_scratch/compass-and-straightedge/review-voice-retry/final-voice-triangle.png) | ![Elements Inspector](../../_scratch/compass-and-straightedge/review-models/review-elements.png) |

The comparison is material confidence, not palette or lesson flow: one works through exact geometry, the other through atomic structure. Beat Lab's frame was also inspected; no lesson features were copied.

#### Audit

Ran once, last, with a 40-minute bound on Chrome 9951 and host 8755. It finished: **371 leads, 32 frames**, all eight required sizes and eight listed states. All 32 frames were opened and inspected.

- 211 overlap leads: 210 are the full-screen SVG beneath its own controls/readouts; one was the real adjacent-point label collision, fixed after confirmation.
- 147 hidden-background leads are inert paper controls beneath modal drawers. The bibliography scroll lead is the Manual's eight source links, not hidden instrument choices; its Close remains available.
- Three missing-hint leads are the deliberately retired first-action hint. Seven missing per-mode welcomes conflict with the Curiosity rule that only the initial appropriate hint speaks automatically; they are not lesson-flow defects to add back.
- The real "1 lines" lead and the quick-Compass interruption were fixed. Five-click stress paths were clean. The audit reported no control-path exceptions/focus loss, no endless reduced-motion animation, and no stuck state or exception during its resize runs.
- Re-shot only the affected point/readout/phone/short-paper states, including the 600-object boundary, and re-walked the main voice path plus the 0.7-second repeated-Compass case. The full audit was not rerun. Final scoped evidence is in `review-final/` and `review-voice-retry/`.
- The actual `check_tools.py` contract and notes checks pass on a scoped draft mirror; its global rebundling entry point was avoided because it would write other tools. No commits or shared-file changes.

#### Left open

- Strict cold-order and fresh timed-ten-minute requirements were not met, as disclosed under Played. No child user study, physical Chromebook frame-rate benchmark or assistive-hardware walk was performed.
- The 600-object test used coincident circles, not the maximum possible number of distinct intersections. Extremely dense sheets remain bounded by browser memory and floating-point conditioning.
- Long-log print pagination remains unverified; the tested short construction prints on one clean page. Bank recordings remain absent; no audio was recorded during this review.
- No shared files or kit engines were edited, no commits were made, and no lesson layer was added. All review work stayed in the two authorized folders.
- Chrome ports 9950-9957 and host 8755 were verified closed; the temporary tool-folder host was removed. See `review-cleanup.json`.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 1 (general 0, family 1), should fix 9 (general 5, family 4), polish accepted 16

### Refine: compass-and-straightedge

Curiosity No. 09. Merged from `refine/teaching.md`, `refine/play.md`, `refine/craft.md` (no sensitivity file; all three
lenses found no cultural, Native or hard-history content). All three lenses pass the short test and the lesson creep
check; the engine's numbers recompute right. Frames: `S:/CurioClass-codex-scratch/compass-and-straightedge/` under
`teaching/frames/`, `play/`, `craft/out/` and the shared `audit-r1/`. Integrator spot-checked src.html:290, 363-366,
406-420, 477, 485, 493, 720-724, 866, 961-964 and 1102-1106: every cited claim below holds.

#### Blocker
1. **Tangent circles and tangent lines make phantom duplicate points.** `src.html:290` (`EPS = 1e-9`), `:406-411`
   (line-circle), `:413-420` (circle-circle), `:372-374` (`addPoint` merge). When two circles just touch, rounding
   leaves `h2` around 2e-16, so `h = sqrt(h2)` is about 1.5e-8, above the 1e-9 cut, and one touching point becomes two
   (the same for `dt` on a tangent line). On the spec's own hexagon walk (Things to do 5, Done when 3) on the Given
   circle sheet, opposite rim circles (centres E and C) touch at the centre A and the sheet grows M and N 1.49e-8 from
   A: three stacked labels "N A M" with leader lines, and the log foot reads "15 points" where 13 exist
   (`play/p04`, `craft/out/h1-hexagon.png`, `craft/out/h2-hexagon-phantoms`: `{"n":"M","d":1.49e-8,"parents":["E","C"]}`).
   The phantoms can be chosen with arrows and anchor new circles, which spawn more near-duplicates, while the Manual
   says tangencies are handled. Fixed: treat `h` and `dt` below a relative tolerance (about 1e-7 times the radius) as
   one touching point, and merge new crossings with a tolerance scaled to the figure; the hexagon walk then shows one
   centre and "13 points". Re-word the Manual honesty note ("Points within 10⁻⁹ sheet units are merged", "Tangencies
   use a small relative numerical tolerance") to state the tolerance actually used. (family:curiosity)

#### Should fix
2. **Book ghost steps are not drawn on the student's A and B.** `src.html:961-964` (Book frame A=(-0.5,0), B=(0.5,0)),
   `:1102-1106` (ghost pushed unchanged under a comment that says it is placed apart, which it is not). On the default
   sheet, Show next step twice on I.1 lays one dashed circle centred half a unit left of the student's A and one
   centred on the midpoint of AB, while the step text says "Set the compass at A through B"; a student who draws
   circle A through B sees it miss the ghost (`teaching/frames/t6-book-ghost-i1.png`, `play/p07`,
   `craft/out/g1-ghosts-on-paper.png`; state dump: ghosts at x=-0.5 and 0.5, r=1, student A=(0,0), B=(1,0)). The same
   holds on every page whose words name A and B, and on the IV pages against the Given circle. Fixed: map each page's
   given points onto the sheet's given points when they exist (A and B for I.1, I.10, I.46 and the like; the given
   circle's centre and radius for the IV pages); when the sheet has no matching givens (blank sheet, given angle),
   draw the ghost well clear of the drawing with its own letters (item 4) so nobody reads it as theirs. Fix or remove
   the misleading comment. (family:curiosity)
3. **The record and announcements use internal ids.** `src.html:477` "Erased p5; dependent objects removed.", `:485`
   "Inked circle o3.", `:866` the `[` and `]` keys announce "circle o3. radius 1.0000 AB", `:493` the tool switch
   announces raw tool keys ("line. Arrows choose...", "erase. ..."). Seen in the teaching t8 log dump, `play/p05`,
   `craft/out/c3-erase-ink-log.png` (rows 5 and 6), `craft/k2-words`, `craft/k3-brackets`. The log is meant to read
   in Euclid's style, prints with the sheet, and Read speaks its last row aloud, so "o7" is spoken. Fixed: describe
   strokes the way the log already does: "Inked the circle with centre A through B.", "Erased point C and the 2 lines
   drawn from it.", brackets announce "Circle with centre A through B. Radius 1.0000 AB.", tool switch says
   "Straightedge.", "Eraser." (general)
4. **Book figures and ghosts carry no letters, but every step names points.** `src.html:1086-1094` (drawBook draws
   only lines and circles; 0 text nodes in `#figure`), step strings at `:966-967` and `:1032-1065`. I.1 says "Call the
   upper crossing C" with no C to find (`play/p06`); I.2 says "Circle B through C. It cuts the extended DB at G."
   (`teaching/frames/t7-book-i2-figure.png`, step 7, no labels); IV.11 uses E, F, H, V and D. I.2 and IV.11 teach the
   hardest ideas and can't be followed. Fixed: pencilled letters on the Book figure for every point a step names, and
   on the ghost points laid on the paper (matching the student's own letters where item 2 maps them onto the sheet).
   (family:curiosity)
5. **Undo also rewinds the instrument settings and the view.** `src.html:363-366`: `checkpoint()` clones the whole
   `state`, so Undo restores `tool`, `euclid`, `extend`, `hold`, `view` and the Book ghosts with the drawing
   (`craft/u1-undo-scope`: draw a circle, pick Edge, switch on Euclid's rule and Extend, pan; Ctrl+Z gives back
   `tool:"compass", euclid:false, extend:false` and the view jumps 0.7 units). A student working under Euclid's rule
   (Done when 5) silently loses it on the first Undo. Fixed: history holds only points, objects, log, serial and
   nextName (and unitLabel if a sheet change is undoable); settings, view and ghosts stay as they are. (general)
6. **The readout live region re-announces on every pointer move.** `src.html:168` (`#readout` is `aria-live=polite`),
   `:736` rewrites it on every `render()`, including each `pointermove` while panning (`:819`). With the I.1 triangle
   readout showing, a 30-step pan made 32 live-region mutations (`craft/p1-pan-triangle-live`), so a screen reader
   repeats "AB 1.0000 AC 1.0000..." through the drag. Fixed: write `#readout` only when its text changes (or drop
   `aria-live` there and keep the one `#status` announcement per move). (general)
7. **Frame time falls under 60 fps at moderate density.** `render()` (`:641`) rebuilds the whole SVG and re-places
   every label on each `pointermove` (`:819`), not once per frame. Measured on a fast desktop: 60 objects and 757
   crossings, during a 60-step pan 61 of 181 frames over 20 ms, p95 31.9 ms, max 40 ms (`craft/out/p2-dense.png`); a
   school Chromebook is several times slower, and a Book pentagon is 30 to 40 objects. Fixed: route pointer-driven
   renders through the existing `requestRender()` so there is at most one per animation frame, and skip label
   placement for points off screen (see polish 13 for density). The 13-object hexagon (0.5 ms) must stay as smooth.
   (family:curiosity)
8. **The resting straightedge covers the drawing and never slides.** `src.html:720-724` draws it on top of the
   construction at a fixed spot (about 575 to 620 px down at 1366x768): across the right I.1 circle beside D
   (`play/p03`, `craft/out/c2-triangle.png`), across the hexagon (`play/p04`) and the lower area at 1920
   (`play/r07`). A straightedge drag shows a grey band instead of the straightedge sliding over, as the spec's first
   two minutes promise. Fixed: draw it under the strokes and rest it on the table edge outside the working area (or
   move it aside when ink lies under it), and let it be the thing that slides into place along a straightedge drag
   (instantly with Motion off). (family:curiosity)
9. **The blank sheet's waiting moment says nothing.** Paper, Blank sheet gives an empty page with Compass still
   selected and the hint hidden (`play/q07`, output `true`); dragging pans and tapping does nothing. Read knows the
   line, the screen does not. Fixed: show `L.blank` as the one quiet pencilled line on the paper until the first
   point, and select the Point tool on a blank sheet. Not spoken on its own (Read reaches it). (general)
10. **The readout tag covers point labels.** `src.html:750-755` keeps the tag inside the edges but not off labels: at
    680x425 "CD 1.7321 AB" hides B's label (`play/p10`); at 375x812 "radius 1.0000 AB" sits on B's label
    (`audit-r1/state-circles-375x812.png`). Fixed: the tag avoids point labels the way labels already avoid each
    other. (general)

#### Polish accepted
11. **Say where crossings come from in the log.** `src.html:432-440`. The record jumps from "Circle with centre B
    through A." to "Line from C to A." with no word that C is where the circles cut (`teaching/frames/t2-i1-triangle.png`).
    After a move that makes crossings, add a sub-line naming them: "They cut at C and D." (family:curiosity)
12. **Point names that clash with segment names.** `src.html:367-371` (pointName), `:607`, `:615` (readouts join
    names with no space). A pentagon makes points A to AN, so one point is named "AB" on a sheet whose unit is AB, and a
    segment from A to it reads "AAB 1.0000 AB" (teaching t5 dump). Skip any generated name equal to the unit label or
    to two existing single letters run together (or switch to primes or subscripts after Z), and separate names in
    multi-letter segment readouts (a space or a bar). (general)
13. **Label clutter at density.** `src.html:695-702`: every crossing gets a label, and a dense sheet becomes a block
    of overlapping two- and three-letter names (`craft/out/p2-dense.png`). Always label given, free, chosen and
    stroke-end points; drop a crossing label that would collide, or below a zoom where it can't be read, and show it on
    hover, choice or the arrow cursor. Names in the log stay the same. (family:curiosity)
14. **The margin note for more Book figures.** `src.html:630-640`. Only I.1 earns "Euclid, Book I, Proposition 1";
    the hexagon walk (`play/p04`), the square in a circle and the 1.6180 pentagon (`play/q12`) find nothing. Add the
    same quiet pencilled note where detection is cheap and sure, at least IV.15 (six equal chords close in the given
    circle) and IV.6 (square in the given circle), and others of the 14 only when equally reliable. Never spoken,
    counted or listed as found. (family:curiosity)
15. **"Things people have found" as separate entries.** `src.html:230-237`: the eight finds run together in three
    paragraphs (`play/q05`). One short entry each, led by its figure or name, so a student who just made the hexagon
    finds theirs at a glance. (family:curiosity)
16. **Triangle readout beside the triangle.** The I.1 readout is pinned top-left, far from the figure, while every
    other tag sits by its object (`play/p03`, `play/q10`). Place it beside the triangle like the other tags.
    (general)
17. **A selected stroke is hard to see.** `src.html:653` adds 0.7 px (1.2 to 1.9 px); in `craft/out/c4-select-weight.png`
    the selected CA is barely different from DB. Give the selection a soft red halo or the crossing red at about
    2.5 px. (general)
18. **Undo and redo glyphs are tiny.** `src.html:191-192`: the arrows render about 8 px in a 48 px button
    (`audit-r1/size-1366x768.png`, `size-680x425.png`). Draw them as about 22 px SVG icons like the toolbelt. (general)
19. **The Manual opens as a centred modal, not the lower-left drawer.** `src.html:65-66, 202`: the handle opens a
    740 px centred dialog (`audit-r1/state-manual-1366x768.png`); the family mark (Span and Spire,
    `span-and-spire/src.html:151`) is a drawer anchored at the lower-left handle. Anchor it there. Keep it a modal
    dialog for focus. (family:curiosity)
20. **Strokes have an 18 px tap band.** `src.html:778` `min=9`. Selecting, inking, erasing or measuring a 1.2 px line
    by touch needs a tap within 9 px; points get 44 px. Use about 22 px either side on coarse pointers. (general)
21. **The keyboard cursor ring shows for mouse users.** `src.html:703-707`, `:796`: any click focuses the sheet, so a
    dashed red ring sits on A after a drag or "Back to paper" and looks like a choice (`craft/out/c2-triangle.png`).
    Show it only after a key press. (general)
22. **Accessible names don't start with the visible word.** `src.html:174, 176`: visible "Edge" and "Erase", names
    "Straightedge, S" and "Eraser, E"; voice control users saying "click Edge" can miss. Start each name with the
    visible word ("Edge, straightedge, S"). (general)
23. **The idle compass sits on the zoom tag at 375 wide.** `src.html:718` (compass at 44,65) over "AB = 1 unit · 62%"
    (`audit-r1/size-375x812 (iframe host).png`, `play/q10`). Move one of them. (family:curiosity)
24. **The first-run hint stays after a non-drawing tool is chosen.** Choosing Measure, Erase or Point before any drag
    leaves "Drag from A to B." on screen, which those tools can't do (`play` finding 10). Show the chosen tool's line
    or hide the hint on that switch; no new speech (the welcome rule stays as BASELINE 16 has it). (general)
25. **Confirm the archive.org volume labels.** `src.html:249-251` labels thirteenbookseu02heibgoog as Books I and II,
    00 as III to IX, 03 as X to XIII; Teaching could not confirm the mapping from the item pages. Check inside each
    scan; if a volume can't be confirmed, give the link without the Book range. (general)
26. **Name proof-tower in notes.md.** notes.md "What it teaches": say plainly that G-CO.C proofs are taught in
    proof-tower and this tool is the second card for G-CO.D, as the spec's Map already says. Do not change the module
    map (see open questions). (family:curiosity)

#### Settled calls
- **Book ghosts tag:** Play tagged general, Teaching and Craft family:curiosity. Settled family:curiosity: the Book's
  own coordinate frame is this tool's format, not a general habit.
- **Book letters are their own item (4), not folded into the ghost item (2):** Play joined them; they are separate
  fixes (placement vs lettering) and Codex should check both.
- **Resting straightedge:** Play said should fix, Craft said nit. Settled should fix: it covers working strokes and
  the spec promises it slides over on a straightedge drag.
- **Readout tag over labels:** Play said should fix (680x425), Craft polish (375). Merged as one should fix at both
  sizes.
- **Tangency tolerance is an engine fix, not a spec change.** The spec's Sources line "points merged within 1e-9" is
  an engine detail; Codex changes the tolerance and updates the Manual honesty note to state what the engine does.
- **Not to change:** the full-bleed `#sheet` overlapping every control and controls covered by open modal dialogs are
  by design (all three lenses; the 368 audit leads are almost all these). The first-run hint is not spoken after a
  first tap on a non-compass control (BASELINE 16); item 24 changes only the visible line. Read joining hint, last log
  row and readout through browser speech is the spec's stated fallback. The measure tool stays (spec lean). The Book
  stays browsed: no numbering of progress, ticks or "done" on pages; the margin note stays quiet, unspoken and
  uncounted. Nothing adds a goal, score, level or finish.
- **Done when 3 and 4:** Teaching passed them on the readouts; the hexagon pass holds only once blocker 1 removes the
  phantom points and the count reads true.

#### To the spec's open questions
- **Reach modules overclaim.** math-10-rigid-motions-and-congruence: only G-CO.A.1 (precise definitions of circle,
  perpendicular, parallel) is exercised; nothing for transformations. math-7-scale-drawings-and-constructions (7.G.A.2,
  triangles from three measures): no sheet with three given lengths and no I.22 page, so a grade 7 student has nothing
  to build from. Choose: narrow the reaches (keep G-CO.A.1 only, drop the math-7 reach), or add a "Given three
  lengths" sheet and an I.22 Book page. (Teaching 6)

#### Not taken
- History memory cap or diff history (Craft 17): fine at today's sizes, and item 5 already shrinks each snapshot;
  revisit if item 7 is reworked.
- Audit tweak (skip overlap rows against a stage-sized element and controls under an open modal dialog, Craft audit
  pilot): a change to `scripts/audit_tool.py`, not to this tool; for the integrator's audit backlog.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: compass-and-straightedge (Curiosity No. 09), round 1

Cold Craft lens, 2026-11-06. Judged against CODEX-CURIOSITY.md, VISION.md "Curiosities: the second shape", STANDARDS,
BASELINE and the spec. Bundle `tools/compass-and-straightedge/compass-and-straightedge.html` as built (not re-bundled).
My frames: `S:/CurioClass-codex-scratch/compass-and-straightedge/craft/out/`. Shared audit:
`S:/CurioClass-codex-scratch/compass-and-straightedge/audit-r1/`.

Counts: blocker 1, should fix 5, polish 6, nit 5.

#### Contract (clean)

- One file, 90,431 bytes bundled (goal 2 MB): clean.
- No network requests: `performance.getEntriesByType('resource')` empty after load and a drag (c1-first-drag). The
  Manual's source links are plain anchors, fetched only if clicked.
- No console errors or exceptions in any of my runs or the audit's (the one exception in my log came from my own
  synthetic KeyboardEvent dispatched on `document`, not from the tool).
- Kit used for voice, tones, Motion and Sound (`Curio.voice`, `Curio.tone`, `Curio.init`); no kit header or lesson frame.
- `scripts/check_tools.py`: listed as `draft compass-and-straightedge`, no failure.
- Words: no em dashes in src.html, lines.json, notes.md; "Curio Class" only; privacy stated in the Paper cabinet and
  Manual ("Saves stay on this device. Nothing leaves the device."). Classroom-safe.
- Lines: all 14 `L` entries match `voice/lines.json` word for word (scripted diff).
- Art: no raster art, `art/prompts.json` has no assets, no people. Nothing to check.
- Lesson creep: no score, goal, level, sticker, finish screen or kit header.
- Look rules: the paper fills the screen; readouts and counts in monospace with units (AB, u, degrees); Manual handle
  and engraved plate lower-left with the middle dot; Motion, Sound and Read on their own lamp plate; toggles carry
  `aria-pressed`; controls 44 to 56 px. Exceptions below.

#### Findings

##### Blocker

1. **Tangent circles and tangent lines make phantom duplicate points.** `src.html:413-420` (circle-circle) and
   `:406-411` (line-circle). When two circles just touch, `h2` comes out a tiny positive number from rounding and
   `h = sqrt(h2)` is about 1.5e-8, larger than the 1e-9 merge distance, so one touching point becomes two points.
   How I saw it: the spec's own hexagon walk (Things to do 5, Done when 3) on the Given circle sheet. Opposite rim
   circles (centres E and C) touch at the centre A, and the sheet grows points M and N at 1.49e-8 from A, both labelled
   beside A with leader lines; the counts read "15 points" where 13 exist (`out/h1-hexagon.png`, numbers from
   `out/h2-hexagon-phantoms` js: `{"n":"M","d":1.49e-8,"parents":["E","C"]}`). Arrow keys cycle through them, they can
   anchor new circles (which then spawn more near-duplicates), and the Manual's honesty note says tangencies are
   handled ("Tangencies use a small relative numerical tolerance"), so the readout lies on the flagship construction.
   Better: treat `h` (and `dt`) below a relative tolerance of the radius, around 1e-7, as one touching point, or merge
   new crossings with a tolerance scaled to the radii. Tag family:curiosity.

##### Should fix

2. **Undo also rewinds the instrument settings and the view.** `src.html:363-366`: `checkpoint()` clones the whole
   `state`, so Undo restores `tool`, `euclid`, `extend`, `hold`, `view` and the Book ghosts along with the drawing.
   Check (`u1-undo-scope`): draw a circle, pick Edge, switch on Euclid's rule and Extend, pan; Ctrl+Z gives back
   `tool:"compass", euclid:false, extend:false` and the view jumps back 0.7 units. A student working under Euclid's rule
   (Done when 5) silently loses it on the first Undo. Better: history holds points, objects, log, serial and names
   only. Tag general.

3. **The record and announcements use internal ids.** `src.html:477` "Erased p6; dependent objects removed.",
   `:485` "Inked line o7.", `:866` `[`/`]` announce "circle o3. radius 1.0000 AB", `:493` tool switch announces
   "line. Arrows choose..." and "erase. ...". Seen in the log card (`out/c3-erase-ink-log.png`: rows 5 and 6) and the
   status region (`k3-brackets`, `k2-words`). The log is meant to read "in Euclid's style" and Read speaks its last row.
   Better: "Erased circle with centre A through B.", "Inked line CA.", "Straightedge." Tag general.

4. **The readout live region re-announces on every pointer move.** `src.html:168` makes `#readout` `aria-live=polite`
   and `render()` rewrites its text on every call (`:736`), including each `pointermove` while panning (`:819`). Check
   (`p1-pan-triangle-live`): with the I.1 triangle readout showing, a 30-step pan caused 32 mutations of the live region,
   so a screen reader repeats "AB 1.0000 AC 1.0000..." through the whole drag. Better: only write when the text changes,
   or drop `aria-live` from `#readout` and keep the one `#status` announcement per move. Tag general.

5. **Frame time falls under 60 fps at moderate density.** `render()` (`:641`) rebuilds the whole SVG and re-places every
   point label on each `pointermove` (`:819`), not once per animation frame. Measured on Cory's desktop (fast CPU,
   headless): 60 objects and 757 crossings, render median 12.9 ms, max 19.8 ms; during a 60-step pan, 61 of 181 frames
   over 20 ms, p95 31.9 ms, max 40 ms (`out/p2-dense.png`). A school Chromebook is several times slower, so a month-of-use
   sheet (a Book pentagon is about 30 to 40 objects) will stutter well below the 60 fps rule. Small sheets are fine (the
   hexagon, 13 objects: 0.5 ms). Better: coalesce pointer renders with the existing `requestRender()`, and skip labels
   for points off screen or below a zoom where they would collide. Tag family:curiosity.

6. **Book ghost steps do not sit on the student's points.** `src.html:964` puts the Book's A and B at (-0.5, 0) and
   (0.5, 0); the sheet's A and B are at (0, 0) and (1, 0), and `:1105-1106` pushes the ghost unchanged. Frame
   `out/g1-ghosts-on-paper.png`: after "Show next step" twice on I.1, the ghost circles are centred half a unit left of
   A and on the midpoint of AB, while the step text says "Set the compass at A through B." A reference laid "on the
   paper" that misses the paper's own A and B reads as wrong. Better: map Book coordinates so its A and B land on the
   sheet's A and B when they exist (or draw the ghosts well clear of the drawing, as the code comment intended).
   Tag family:curiosity.

##### Polish

7. **A selected stroke is hard to see.** `src.html:653` adds 0.7 px to the width (1.2 to 1.9 px pencil). In
   `out/c4-select-weight.png` the selected CA is barely distinguishable from DB; only the readout tag tells you which
   one is selected. Better: a soft red halo or the crossing red at 2.5 px while selected. Tag general.
8. **Undo and redo glyphs are tiny.** `src.html:191-192` with `.bench button` at 12px system-ui: the arrows render about
   8 px in a 48 px button (`audit-r1/size-1366x768.png`, `size-680x425.png`). Better: draw them as 22 px SVG icons like
   the toolbelt. Tag general.
9. **The readout tag covers point labels on a phone.** `src.html:750-755` keeps the tag inside the edges but not off
   labels: at 375x812 "radius 1.0000 AB" sits on B's label (`audit-r1/state-circles-375x812.png`). Tag general.
10. **The Manual opens as a centred modal, not a lower-left drawer.** `src.html:65-66, 202`. Span and Spire's Manual is
    a drawer anchored at the lower-left handle (`span-and-spire/src.html:151`); here the same handle opens a 740 px
    centred dialog (`audit-r1/state-manual-1366x768.png`). Better: anchor it at the handle like the family mark.
    Tag family:curiosity.
11. **Strokes have an 18 px tap band.** `src.html:778` `min=9` px. Selecting, inking, erasing or measuring a 1.2 px
    pencil line by touch (the 375 toolbelt layout) needs a tap within 9 px. Points already get 44 px. Better: 22 px on
    coarse pointers. Tag general.
12. **Every crossing gets a letter label.** `src.html:695-702`. At density the sheet turns into a block of overlapping
    two- and three-letter names (`out/p2-dense.png`). Better: label given, free and chosen points always, crossings on
    hover, choice or above a zoom threshold. Tag family:curiosity.

##### Nit

13. The keyboard cursor ring (`:703-707`) shows for mouse users: any click focuses the sheet (`:796`), so a dashed red
    ring sits on A after a drag or after "Back to paper" (`out/c2-triangle.png`, `out/g1-ghosts-on-paper.png`). It looks
    like A is chosen. Show it only after a key press. Tag general.
14. Visible "Edge" and "Erase" vs accessible names "Straightedge, S" and "Eraser, E" (`:174, :176`): voice-control users
    saying "click Edge" may miss. Tag general.
15. At 375 wide the idle compass drawing (`:718`, at 44,65) lies over the zoom tag "AB = 1 unit · 62%"
    (`audit-r1/size-375x812 (iframe host).png`). Tag family:curiosity.
16. The resting straightedge (`:720-724`) is drawn above the construction and covers the lower circles near D at
    1366x768 (`out/c2-triangle.png`). Draw it under the strokes or let it slide aside. Tag family:curiosity.
17. Each move clones the whole state into history (`:363`) with no cap; a 600-object sheet with thousands of crossings
    keeps hundreds of full copies. Fine for now; worth a cap or diff history if finding 5 is reworked. Tag general.

#### Access (clean rows)

- Keyboard: Tab lands on the paper first; arrows move the point cursor, Enter, Enter draws (`k1-keyboard-circle`: log
  "Circle with centre B through A.", status announces it with the radius; `k1b`: "B. Choose the second point.").
  O, crosshair and Enter place a free point; `[` `]` select strokes; Escape cancels; Ctrl+Z/Y. Focus visible (3 px red
  outline). Audit: Enter twice after each click keeps focus, nothing disabled after resize.
- Color is not the only signal: chosen points get a ring, crossings are red dots plus labels.
- Motion off: circles appear at once; audit "nothing runs forever" clean.

#### Standard voice check

A Curiosity: one first-run hint, then Read only. No how-to or event line is spoken on its own, and none should be.

| line | kind | expected | spoken |
|---|---|---|---|
| "Drag from A to B." (hint) | how-to, first run | once on the first plain tap | once (`v2`: sheet, compass, edge, compass, sheet, 2.2 s apart: one entry) |
| hint on first tap of Edge, Point, Erase, Measure, Paper, Book, Manual | how-to | not required (BASELINE 16) | not spoken; reachable by Read (the hint for that tool) |
| hint on a first real drag A to B | how-to | not required | not spoken; the student already did it |
| Read, five presses 2.5 s apart | read | five | five (`v1`) |
| Read with Sound off | read | speaks | speaks (`v3`) |
| Read on Blank sheet | read | blank-paper hint | "Blank paper. Choose Point to place free points..." (`v4`) |

Stale lines and order: nothing queues behind an action (opening a drawer, changing a Book page or a sheet hushes);
audit's five clicks and two quick taps clean on every control that spoke. Read joins the hint, the last log row and the
readout, so it never matches a recording and always uses browser speech; this is the spec's stated fallback, but it
will speak finding 3's "o7" ids aloud.

#### Not checked

Print output (no print emulation in drive.py); the CSS (`:150-161`) hides the instruments and ghosts and prints the
log in three columns, which reads right.

#### Audit pilot

**Why 368 leads.** Almost all are two quirks of this layout, not defects:
- 210 rows: `#sheet` is a focusable full-bleed `role=application` SVG under every control, so the audit reports an
  overlap between it and each of the ~25 floating controls at each of 8 sizes. The Curiosity look ("the object fills
  the screen") makes this the intended layout.
- 147 rows: the Book, Manual and Paper cabinet are `showModal()` dialogs, which make the page behind them inert; the
  audit reports every covered control as "text hidden under another box" per size and state.
- The remaining handful: "hint out of view" in the circles, blank-paper and infinite-line states (the first-run hint
  is meant to vanish after the first action), "choices cut short" in the Manual (its source links sit in a scrolling
  text, as they should), and "welcome not heard" after a first tap on a non-compass control (by design: the hint is
  compass-specific, BASELINE 16, and Read reaches each tool's hint).
- Audit fix to suggest: skip overlap rows with an element whose box equals the stage, and skip controls under an open
  modal `dialog`.

**Leads confirmed:** none as defects. **Leads wrong:** all of the above, for the reasons given. Its clean rows (no
console errors, Motion off, resize mid-action, five clicks and quick taps) held in my runs.

**What it missed:** the phantom tangency points (1), Undo rewinding settings and view (2), internal ids in the log
and announcements (3), the live region firing on every pointer move (4), frame time at density (5), the misplaced Book
ghosts (6), the faint selection, tiny undo glyphs, the readout over a label at 375 and label clutter (7 to 12).

No cultural, Native or hard-history content; no sensitivity review needed from this lens.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: compass-and-straightedge (Curiosity No. 09), round 1

Cold lens, judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape". Frames are mine in
`S:/CurioClass-codex-scratch/compass-and-straightedge/play/` (p*, q*, r*), driven with real drags, clicks and keys where
the input mattered, plus the shared audit `audit-r1/`.

#### Short test

- Would a kid open it unassigned? Yes, mostly. The first drag from A to B lifts the brass compass, swings a pencil
  circle with a graphite scratch and leaves a line that stays (p02). Two drags and two lines make a triangle that reads
  1.0000, 1.0000, 1.0000 and 60.00 degrees with a pencilled "Euclid, Book I, Proposition 1" (p03). That lands.
- Would an adult play for fun? Yes. Walking the radius round a circle makes the six-petal flower (p04), Keep opening
  works as a modern compass (r02, log "Circle with centre C, retained radius 1.0000 AB"), and measuring a pentagon's
  diagonal against its side gives 1.6180 (q12).
- Is the real thing the interface? Yes: circles, crossings and lines are the whole screen; no lesson frame.
- Does it work with no finish line? Yes. No score, goal, level or finish anywhere I looked; the Book is browsed by a
  select menu, nothing ticks.

Passes all four. The findings below are about the instrument telling the truth and the second-session depth.

#### Findings

1. **blocker** · family:curiosity · geometry engine, `src.html:290` (`EPS = 1e-9`) with `addPoint` merge.
   The hexagon walk, the tool's signature "thing people have found", makes duplicate crossings at the centre. After
   walking six circles round the given circle, points M and N sit 1.49e-8 from A (q01 output: "M crossing 1.490e-8",
   "N crossing 1.490e-8"). The paper shows three stacked labels "N A M" with leader lines at the centre (p04), and the
   log foot reads "15 points" where 13 exist. A readout that lies, on the figure a kid is most likely to make. Better:
   merge with a tolerance scaled to the figure (or merge by shared parent objects), so the flower has one centre and
   the counts are true. Also re-word the Manual's "Points within 10⁻⁹ sheet units are merged" to match.

2. **should fix** · general · The Book's ghost steps, `src.html:964` and `:1106`.
   Book figures use their own coordinates (A at -0.5, B at 0.5) while the student's A and B are at 0 and 1. On I.1,
   "Set the compass at A through B" lays a ghost circle centred half a unit left of the student's A, and the second
   ghost is centred on the middle of AB (p07, Book closed after three steps). A student following the Book on their own
   paper sees a reference that contradicts the step text and their own points. Inside the Book the small figure has no
   point labels, so "Call the upper crossing C" (p06) has no C to find. Better: map each page's figure onto the sheet's
   given points where the page starts from A and B (I.1, I.10, I.46, IV pages on the given circle), or draw ghosts in a
   clearly separate place, and letter the Book figure's points.

3. **should fix** · general · Construction record words, `src.html:477`, `:485`, `:866`.
   The log shows internal ids: "Inked circle o3." and "Erased o4; dependent objects removed." (p05 output); the [ and ]
   keys announce "circle o5". Every other log line speaks in point names ("Circle with centre B through A."). Better:
   "Inked circle with centre A through B." and "Erased the circle with centre B through A, and 2 crossings that
   depended on it."

4. **should fix** · family:curiosity · The decorative straightedge, `src.html:720`.
   It is drawn on top of the working paper at a fixed spot (about 575 to 620 px down at 1366x768). With nothing more
   than the I.1 circles it sits across the bottom of the right circle beside crossing D (p03), and across the hexagon
   (p04) and the default 1920 frame's lower area (r07). Meanwhile drawing a line never moves it: the drag shows a grey
   band, not the straightedge sliding over as the spec promises. Better: rest it on the table edge outside the drawing,
   or hide it when ink lies under it, and let it be the thing that slides in on a straightedge drag.

5. **should fix** · general · Blank sheet waiting moment (q07).
   Paper, Blank sheet gives an empty page with Compass still selected and no visible word (hint hidden, q07 output
   `true`). Dragging pans, tapping does nothing. Read knows the line ("Blank paper. Choose Point to place free points"),
   but the screen says nothing. Better: show that one quiet line on the paper until the first point, and select Point.

6. **should fix** · general · 680x425 measure tag (p10).
   Selecting the line CD at 680x425 puts the tag "CD 1.7321 AB" over the label B, which is hidden under it. Better: the
   tag avoids point labels the way labels already avoid each other.

7. **polish** · family:curiosity · The pencilled margin note, `src.html:637`.
   Only I.1 earns it. The hexagon walk (p04), the square in a circle and the 1.6180 pentagon (q12) find nothing. The
   spec's own lean was the 14 Book figures. These are the moments a month of use would find; a quiet "Euclid, Book IV,
   Proposition 15" when six equal chords close would land the way I.1 does.

8. **polish** · family:curiosity · "Things people have found" in the Manual, `src.html:230-237`.
   The eight finds are run together in three paragraphs (q05). A field guide reads better as short separate entries,
   each with its figure name, so a student who just made the hexagon can find their entry at a glance.

9. **polish** · general · Triangle readout position (p03, q10).
   The I.1 readout is pinned at the top-left corner, far from the triangle, while every other tag sits beside its
   object. Better: put it beside the triangle like the other tags.

10. **nit** · general · First-run hint after a non-drawing tool. Choosing Measure, Erase or Point before any drag leaves
    "Drag from A to B." on screen, which those tools cannot do; the audit also shows the hint unspoken when the first tap
    is Edge, Point, Erase, Measure, Paper, The Book or Manual. The visible line covers it for Edge; for the others the
    words no longer match the state.

11. **nit** · general · 375x812 (audit size-375x812, q10): the zoom tag "AB = 1 unit · 62%" sits under the resting
    compass's legs at the top-left.

#### Checked and clean

- Real first drag A to B: circle drawn, hint gone, log line added (p01, p02). Motion off: audit calm row clean.
- Keyboard: Tab, Enter, Right, Enter draws "Circle with centre A through B." with focus on the sheet (p12).
- Euclid's rule on: radius resets to 0 and Keep opening is disabled after a circle (q03).
- Read speaks the tool line, the last move and the readout (q04).
- Extreme zoom out to 0.02 percent: no freeze, labels still placed (q11).
- No score, goal, level, sticker, badge or finish screen in any frame.

#### Audit pilot

- Leads confirmed: none of the 368 as written. The "hint out of view" rows on circles, blank-paper and
  infinite-line-min-zoom are the hint correctly gone after the first action; the welcome "not heard" rows are real but
  minor (finding 10).
- Leads wrong: every "overlap: #sheet" row (the sheet is the full-screen paper under all controls, by design), every
  "text hidden under" row in the book, manual and paper states (a modal drawer over the instrument is expected), and
  "choices cut short by a scroll panel" in the Manual (source links lower in a long reading drawer).
- Missed: duplicate crossings at the hexagon centre and the false point count (1), Book ghosts offset from the
  student's A and B (2), raw ids in the log (3), the prop straightedge over the drawing (4), the silent blank sheet (5),
  the measure tag over a label at 680x425 (6). The audit draws circles by script but cannot see a stacked label or a
  ghost that disagrees with its words.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: compass-and-straightedge (Curiosity No. 09)

Cold lens, round 1, 2026-11-06. Judged as a Curiosity (CODEX-CURIOSITY.md, VISION "Curiosities: the second shape").
Frames and scripts: `S:/CurioClass-codex-scratch/compass-and-straightedge/teaching/` (shots.json, shots2.json, frames/).
The engine is sound: every number I recomputed matches. The weak spot is the Book. Its step-by-step help can't be
followed against the student's own paper.

Counts: blockers 0, should fix 3, polish 3, nits 2.

#### Findings

##### 1. Book ghost strokes are not drawn on the student's A and B (should fix, family:curiosity)
- Where: src.html:961-970 (Book geometry uses its own frame, A=(-0.5,0), B=(0.5,0)), src.html:1105-1106 (ghost
  pushed unchanged, with the comment "Place the reference slightly apart from the starting A/B pair").
- What: on the default sheet, pressing Show next step on I.1 twice lays two dashed circles. One is centred left of
  the student's A and the other on the midpoint of AB. Neither is centred on the A or B labelled on the paper.
  The step text says "Set the compass at A through B", so a student who draws circle A through B sees their circle
  miss the ghost. The reference then contradicts the paper it's drawn on. The same happens on every page whose
  words name A and B.
- How seen: `frames/t6-book-ghost-i1.png`. The state dump shows ghosts at x=-0.5 and x=0.5 with r=1, and the
  student's A=(0,0) and B=(1,0).
- Better: fit the page's own given points onto the student's given points when they exist. Or draw the ghost
  well clear of the drawing, with its own letters (see 2), so nobody reads it as being on their A and B.

##### 2. Book figures and ghosts have no letters, but the steps name points (should fix, family:curiosity)
- Where: src.html:1086-1094 (drawBook draws only lines and circles), Book step strings at src.html:1032-1036 and
  1046-1065.
- What: the steps say "Circle D through G. It cuts extended DA at L." (I.2) and use E, F, H, V and D for IV.11.
  Neither the figure nor the ghosts carry a single letter (0 text nodes in `#figure`). The only labels on the
  sheet are the student's own A and B, and those are different points from the Book's A and B. I.2 and IV.11 are
  the two pages that teach the hardest ideas (the collapsing-compass transfer and the golden division), and they
  can't be followed.
- How seen: `frames/t7-book-i2-figure.png` (I.2 at step 7, steptext "Circle B through C. It cuts the extended DB
  at G.", no labels).
- Better: put pencilled letters on the figure and the ghost points the steps name.

##### 3. Log and announcements use internal ids (should fix, general)
- Where: src.html:477 (`Erased ${id}; dependent objects removed.`), src.html:485 (`Inked circle o3.`),
  src.html:866 (the [ and ] keys announce `circle o3`).
- What: the construction record is meant to be read back "in Euclid's style" (spec Things to do 12) and printed
  with the sheet. Instead it shows "Inked circle o3." and "Erased p5; dependent objects removed." Students never
  see o3 or p5 anywhere else, and a screen reader user hears "circle o3" when picking strokes.
- How seen: t8 log dump: `["Given points A and B. AB = 1 unit.","Circle with centre A through B.","Circle with
  centre B through A.","Inked circle o3.","Erased p5; dependent objects removed."]`.
- Better: name things as the log already does: "Inked the circle with centre A through B." and "Erased point C
  and the 2 lines drawn from it."

##### 4. The log never says where crossings come from (polish, family:curiosity)
- Where: src.html:432-440.
- What: the record reads "Circle with centre B through A." and then "Line from C to A." with nothing between. C
  first appears as a crossing on the paper, but the log never says so. Euclid's own wording is "the circles cut
  one another at C". Without that line the record can't be read on its own, and a printed log that runs into a
  second column loses the link to the figure.
- How seen: `frames/t2-i1-triangle.png` (log entries 3 and 4).
- Better: after a move, add a sub-line naming the new crossings, for example "They cut at C and D."

##### 5. Point names run into double letters fast, including "AB" (polish, general)
- Where: src.html:367-371 (pointName), 607 and 615 (readouts join names with no space), 633 (the triangle check
  looks up points by name).
- What: every crossing of every pair gets a letter. A pentagon of 11 strokes already makes 40 points, A to AN
  (t5). One of those points is named "AB" on a sheet where "AB = 1 unit" is the unit and "AB" is also a segment.
  A segment from A to point AB would read "AAB  1.0000 AB". That confuses the very idea, segment naming, that
  G-CO.D.12 relies on.
- How seen: t5 dump `names: A B C ... Z AA AB AC ... AN`.
- Better: skip names that clash with the unit (or use primes or subscripts, A1, A2), and put a space or a bar in
  multi-letter segment readouts.

##### 6. Map claims beyond what the instrument exercises (polish, family:curiosity)
- Where: spec.md "Map"; notes.md "What it teaches".
- What: G-CO.D.12 is fully exercised: copying a segment (I.2 tested by hand with Euclid's rule on, AL = 1.0000),
  bisecting a segment, bisecting an angle (t11: 25.45 and 25.45 degrees, halves of 50.91), perpendiculars and
  parallels. G-CO.D.13 is fully exercised too: the triangle (t2), the hexagon (t3) and the square. G-CO.C is
  honestly marked partial, and proof-tower carries it, so as a second card this is fine. But notes.md should name
  proof-tower as the place G-CO.C is taught. Of the "reaches":
  - math-10-rigid-motions-and-congruence: only G-CO.A.1 (precise definitions of circle, perpendicular and
    parallel) is exercised. There is nothing for transformations.
  - math-7-scale-drawings-and-constructions (7.G.A.2, triangles from three measures): there is no starting sheet
    with three given lengths and no I.22 page, so a grade 7 student has nothing to build from.
- Better: keep the reach to G-CO.A.1, or add a "Given three lengths" sheet and an I.22 Book page.

##### 7. The margin note only names I.1 (nit, family:curiosity)
- Where: src.html:630-640.
- What: the spec's lean was to name all 14 Book figures quietly. Only I.1 gets "Euclid, Book I, Proposition 1".
  A hexagon (IV.15) or a bisector (I.10) gets nothing. That's fine as it stands; a few more notes would add
  depth without becoming a target.

##### 8. archive.org volume labels not confirmed (nit, general)
- Where: src.html:249-251.
- What: the Manual labels thirteenbookseu02heibgoog as Books I and II, 00 as III to IX, and 03 as X to XIII. Both
  item pages I opened (00: 456 pp, 02: 449 pp) have the same three-volume description and no volume number, so I
  couldn't confirm the mapping. Worth a look inside each scan before ship.

#### Done when (Teaching checks)
| # | Result | Evidence |
|---|---|---|
| 1 | PASS | t1: a real drag from A to B makes "Circle with centre A through B."; audit size frames clean |
| 2 | PASS | t2: `AB 1.0000 AC 1.0000 BC 1.0000`, angles `60.00° 60.00° 60.00°`, note "Euclid, Book I, Proposition 1" |
| 3 | PASS | t3: circles walked from rim crossings at radius 1 land at -60, -120, -180, 120, 60, then back on B (same point, merged) |
| 4 | PASS (readout) | t5: side/diagonal readout `longer / shorter 1.6180`, line angle 36.00°, diagonal 1.9021 (2 sin 72° = 1.90211). I built a shorter valid pentagon, not the full Book method; I recomputed the Book IV.11 page geometry (II.11 radius 0.618, golden triangle with 36°/72°) and it is right |
| 5 | PASS | t4: Euclid's rule on, Keep opening disabled, I.2 by hand gives AL = 1.0000 = BC |
| 6 | PASS, see 3 | only made points are used (hitPoint); log in order; t8: undoing everything leaves 1 entry, redo restores 5 |
| 7 | PASS | ghosts appear only on Show next step; nothing ticked. But see 1 and 2 |
| 8 | PASS (teaching part) | t9: C, Enter, Arrow, Enter draws a circle; Motion off is clean in the audit. Craft owns the rest |
| 12 | PASS | lesson creep grep: no score, goal, level, sticker, correct or wrong; no em dashes |

#### Facts spot-checked (12)
Gauss and the 17-gon, 1796, aged 18 (born April 1777). Wantzel 1837. Lindemann 1882. Mohr 1672 and Mascheroni 1797
(confirmed on MacTutor's Mascheroni page). Heath died 1940. Golden ratio 1.618034, shown as 1.6180. The pentagon's
diagonal and angle (t5). IV.16 arithmetic: 120 - 72 = 48, half is 24 degrees, 360/24 = 15. The II.11 page geometry:
EB = sqrt(5)/2, AH = 0.618, AH squared = AB x HB = 0.382. The 14 enunciations and 3 postulates in the Book and
Manual match spec.md word for word. The honesty notes match the code (EPS 1e-9, 600-object cap). No errors.
No cultural, Native or hard-history content, so no sensitivity review is needed.

#### Audit pilot
- Leads confirmed: none that bear on teaching. "hint out of view" on circles, blank-paper and infinite-line is
  right: the hint is meant to go after the first action.
- Leads wrong: the 368 leads are almost all `#sheet` overlaps (the sheet fills the screen by design) and controls
  "hidden" under modal drawers that are meant to cover them. The manual's "choices cut short" lead is just source
  links further down a scrolling drawer.
- What it missed: the Book ghosts landing off the student's A and B (1), the figures having no letters (2), internal
  ids in the log (3), and point names clashing with the unit (5). None are mechanical layout faults.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: compass-and-straightedge (Codex fix, round 1)

Curiosity No. 09. Work stayed in the requested checkout and two allowed folders; no commits or refine edits.
Evidence paths below are relative to `_scratch/compass-and-straightedge/` unless named otherwise.
The initial harness run had a test-only `window.Curio` lookup error; it was corrected and all required before cases rerun before source fixes.

#### Blocker

1. FIXED: Tangencies and crossing merges use the disclosed relative tolerances. The real six-circle walk changed from 15 to 13 points, with only A at the centre. `before-01-tangency.json`, `after-01-tangency.json`, `fix-before/01-tangency.png`, `fix-after/01-tangency.png`. `verified-tangent-scales.json`: 1,200 tangent cases, three scales, both argument orders, zero failures; a genuinely secant pair still returns two roots.

#### Should fix

2. FIXED: Book coordinates map by similarities onto matching givens. All five relevant I pages have zero A/B placement error, and all four IV pages have zero centre/rim error (`final-book-map-numbers.json`). Default I.1 centres changed from -0.5/0.5 to 0/1. Unmatched studies have primed letters beyond the drawing; their reference extensions stay in that study (`fix-final-extra/detached-final.png`, `fix-verify/ghost-blank.png`, `ghost-angle.png`, `ghost-circle.png`).
3. FIXED: Ink, erase, brackets and tool changes use geometric names. Before: o9, p5, line. After: Inked the line from A to B; Erased point C and 2 dependent lines; Straightedge. See `before-03-language.json`, `after-03-language.json`, `verified-keyboard-announce.json`, and `fix-voice/evidence.json`.
4. FIXED: Reference points are lettered and their glyph bounds prevent collisions, including D/G/L in I.2 and E/F/H, D and V in the pentagon's separate compound drawings. Book and paper names agree, including the student's actual letters where a point already exists. I.2 changed from zero text nodes to five at step 7; at 680x425 the final letters measure 12 px high (`final-book-short-final.json`). The audit exposed a B′/H′ overlap at 680x425, corrected with measured glyph placement and leaders. Final Book checks at 680, 1366 and phone widths show no overlap; all 15 pages at both 680 and 1366 have zero label overlaps (`edge-after-book-pages-680.json`, `edge-after-book-pages-1366.json`). The pentagon transfer now explicitly names the longer part of the preceding golden division, avoiding an absent H (`fix-edge-after/copy-context-680.png`). Frames: `fix-polish/book-i2.png`, `book-pentagon-division.png`, `book-pentagon-circle.png`, `fix-final-extra/book-matched-letters.png`, `book-short-final.png`.
5. FIXED: Snapshots hold only drawing data. Undo and redo preserve the tool, Euclid switch, Extend, retained-opening switch, view and ghosts. The reproduced 0.7-unit jump is gone (`before-05-undo.json`, `after-05-undo.json`, `verified-undo-scope.json`).
6. FIXED: Readout text updates only when its value changes. Thirty pan steps went from 30 live-region mutations to zero (`before-06-live.json`, `after-06-live.json`, `final-live-final.json`).
7. FIXED: Pointer renders coalesce to one per animation frame, offscreen points skip labels, dense crossing labels suppress, dots share SVG paths, and the record is cached. At 1366x768, 60 circles and 2,101 points: p95 direct render 5.6 ms (before 40.8 ms); native 60-step pan p95 6.3 ms, maximum 7.1 ms. A burst of 100 requests produces one render. The 13-object hexagon p95 is 0.8 ms (`verified-dense-timing.json`, `verified-hexagon-timing.json`, `final-dense-pan.json`). These are desktop measurements, not a Chromebook hardware benchmark.
8. FIXED: The real steel edge rests under the strokes at the paper's bottom edge and aligns with a straightedge drag. The held drag recorded 20 distinct instrument transforms, immediately with Motion off (`polish-ruler-drag.json`). Resting frames: `fix-final-extra/triangle-1366.png`, `triangle-1920.png`, `hexagon-1920.png`; the old fixed strip across the working area is gone.
9. FIXED: Blank paper selects Point and displays L.blank until its first point. It stays silent until Read. `before-09-blank.json`, `after-09-blank.json`, `fix-polish/blank-phone.png`, `fix-voice/blank-silent-read.png`.
10. FIXED: Tags avoid label and point bounds. The original 680x425 and 375x812 overlaps with B are reproduced in `fix-before/10-tag-680.png` and `10-tag-phone.png`. Final frames: `fix-last/tag-680-final.png`, `phone-circles.png`; zero label intersections at 680 (`last-tag-680-final.json`), and the phone tag is below B, at y354.5, while B's label ends at y320.5.

#### Polish accepted

11. FIXED: A crossing note is a new line within its parent move, rather than an extra numbered move. `fix-last/log-sublines.png`, `last-log-sublines.json`: three record rows after the two circles, the third containing "They cut at C and D."
12. FIXED: Names after Z use numeric subscripts, with separators for multi-character endpoints. No AB or AA point names in the dense test. The classical pentagon reads N · M₁₂ and 1.6180 (`polish-density-labels.json`, `final-pentagon-method.json`, `fix-final-extra/pentagon-method.png`).
13. FIXED: Given, free, stroke anchors, selected, hovered and keyboard-cursor points retain labels. At low magnification other crossing labels hide; at higher magnification they require collision-free space. The 2,101-point frame has 12 essential labels (`verified-dense-timing.json`, `fix-verify/dense-timing.png`). Arrow selection was verified to reveal hidden N (`edge-after-density-keyboard-reveal.json`: false before, true after); hover and choice use the same required-label path.
14. FIXED: Exact closed chord cycles on the original circle identify IV.15 and IV.6 quietly. Hexagon: `verified-hexagon-timing.json`; square: `polish-square-note.json`, `fix-polish/square-note.png`. Incomplete cycles and radius alone do not suffice. No speech, tally or found list.
15. FIXED: Eight separate named entries in the Manual (`verified-manual-finds.json`, `fix-verify/manual-finds.png`).
16. FIXED: The triangle tag sits outside its triangle bounds, near the figure. `fix-last/triangle-log-final.png`, `fix-final-extra/triangle-1920.png`.
17. FIXED: Selected strokes use a 2.5 px red line and a soft 7 px halo. `fix-last/triangle-log-final.png`, `phone-circles.png`.
18. FIXED: Undo and redo use 22 px SVG icons. Runtime dimensions: `polish-hint-680.json`; final frame `fix-last/tag-680-final.png`.
19. FIXED: Manual remains modal for focus, anchored at left 24 px, bottom 80 px; phone uses left 12 px, bottom 138 px. `polish-manual-drawer.json`, `fix-final-extra/manual-1366.png`.
20. FIXED: Coarse pointers and touch/pen releases use 22 px on either side of a stroke. At 18 px distance, fine-pointer hit is null and coarse-pointer hit is the line (`polish-touch-band.json`).
21. FIXED: Keyboard rings appear after keys and clear on pointer input, including Book/Back to paper. `cursor-final.json`: 1 before the mouse, 0 after; `fix-cursor/cursor-clears-on-mouse.png`. The first attempted harness placed its key after the mouse clicks and correctly showed a ring; the corrected order proves the transition.
22. FIXED: Names start with Edge, Point and Erase, matching visible words. `polish-hint-680.json`.
23. FIXED: Phone zoom tag is at (19,22), clear of the compass, whose resting position is in the right margin. Initial and radius-retained frames: `fix-last/phone-rest.png`, `phone-circles.png`.
24. FIXED: Choosing a non-compass instrument hides the initial drag hint without adding speech. `polish-hint-680.json`, `fix-polish/hint-680.png`; ten rapid instrument changes added no welcome in `fix-voice/evidence.json`.
25. FIXED: Checked the scans' OCR. Volumes 00 and 03 confirm III-IX and X-XIII. Scan 02 metadata failed once; direct OCR retry succeeded, but its contents span the multi-volume contents list, so its link conservatively says Heath scan 02. Raw evidence: `data/fix/`; scripts: `fix_sources.py`, `fix_source_retry.py`. No unconfirmed range remains.
26. FIXED: `tools/compass-and-straightedge/notes.md` now names proof-tower for G-CO.C proofs and identifies this as the second G-CO.D card. The module map stays unchanged.

#### Settled calls

Applied the Curiosity brief over lesson defaults: no welcome screen, goal, score, quiz, level, finish or kit header. The Book remains freely browsed. Measurement stays, with its honesty note. Margin identifications stay quiet. The full-screen sheet underneath controls and modal coverage are intentional. The original numerical threshold in spec.md stays untouched; the working tolerance is disclosed in the Manual and draft sources.

The source lesson-creep scan found zero score, level, goal, sticker, badge, correct, wrong, try again, complete or well done hits. The 60 points hits refer to geometric points, the point tool or point arrays, never scoring (`fix-static.json`).

#### Cheats tried

There is no score or pass condition. Tested the instrument instead: tangent roots in both orders across three scales; a close secant that must retain two roots; Undo/Redo after switches, pan and Book ghosts; repeated render bursts; 60-circle pan; the 47-object classical pentagon with no free points and a collapsed opening. It returns five equal sides and diagonal/side 1.6180339887498931 (`final-pentagon-method.json`). The Book never adds anchors, and blank and given-angle references leave the student's point count unchanged (`verified-ghost-blank.json`, `verified-ghost-angle.json`).

#### Voice walk

Held real clicks for 120 ms, with two-second action gaps and real, whole-pixel jittered drags. `fix-voice/evidence.json`: initial hint once; Read with named ink row once; Read with named erase row once; Read on blank paper with Sound off once. Ten rapid switches add no automatic welcome. The brackets test announces the circle's centre and through-point. allLines equals all 14 unchanged bank lines; zero exceptions and zero HTTP requests. Existing missing recordings use the stated browser-speech fallback; this run checks its start log in muted Chrome, not recorded audio quality.

| Line | Kind | Expected | Logged |
|---|---|---:|---:|
| Drag from A to B | initial hint | 1 | 1 |
| Ink read, with current instrument and measurement | requested Read | 1 | 1 |
| Erase read, with dependent construction | requested Read | 1 | 1 |
| Blank paper, Sound off | requested Read | 1 | 1 |
| Extra welcomes after instrument switches | automatic | 0 | 0 |

#### The real material

- Euclid, Heath's 1908 translation: public domain in the US. [Scan 02](https://archive.org/details/thirteenbookseu02heibgoog), [scan 00](https://archive.org/details/thirteenbookseu00heibgoog), [scan 03](https://archive.org/details/thirteenbookseu03heibgoog). Fetched 2026-11-06, complete available OCR, no sampling and no new OCR prose incorporated. Existing enunciations and postulates remain the supplied specification's wording. Geometry of the triangle, collapsing-compass copy, golden division and pentagon is independently recomputed in the retained construction replay; IV.6 and IV.15 were also checked against [Joyce's Euclid IV.6](https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV6.html) and [IV.15](https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV15.html), verification only, no text or artwork copied.
- Existing historical facts: [MacTutor biographies](https://mathshistory.st-andrews.ac.uk/Biographies/), [text licence CC BY-SA 4.0](https://mathshistory.st-andrews.ac.uk/Miscellaneous/copyright/). Facts paraphrased, no licensed article prose or imagery incorporated. Rechecked Wantzel, Gauss, Lindemann and Mascheroni on 2026-11-06. Independent verification: [Wantzel's 1837 paper catalogue](https://www.numdam.org/item/JMPA_1837_1_2__366_0/), [Gauss diary research](https://epubs.siam.org/doi/10.1137/25M1806491), [Mohr-Mascheroni proof](https://math.ch/norbert.hungerbuehler/publications/A_Short_Elementary_Proof_of_the_Mohr-Mascheroni_Theorem.pdf), [regular polygon theorem](https://webpages.ciencias.ulisboa.pt/~pjfreitas/pdfs/DividingTheCircle.pdf), and [Lindemann biography](https://www.deutsche-biographie.de/sfz51526.html?language=en). Verification only; no copyrighted text, figures or datasets imported.
- Original calculations, new tolerance and numerical readouts: Curio Class engine, MIT code; original text and diagrams CC BY 4.0, as repository LICENSE and LICENSE-CONTENT.md state. No external dataset or library was added. Named source and licence remain in the Manual and tool.draft.json.

Additional saved-reference probe: malformed placement metadata changed from accepted to rejected, and a legacy save without that metadata now advances from two to three ghosts without an exception (`edge-before-saved-reference-context.json`, `edge-after-saved-reference-context.json`).

#### Engine changes wanted

None needed for these fixes. The existing optional kit power-label formatter request remains in handoff.md; the kit was not edited.

#### Audit

The single full audit finished within its 2,400-second limit: `fix-audit/audit.md`, 381 leads. It includes the new I.2 and golden-division states. No second full audit or three-lens review was run. The final Book-only follow-up was bundled and checked with 12 scoped shots; `fix-validation-manifest.json` records both the audited bundle hash and final bundle hash.

| Leads | Disposition |
|---|---|
| 194 sheet/control overlaps | Intentional full-bleed sheet underneath controls, per the settled call. Frames inspected. |
| 135 controls covered by drawers | Intentional native modal coverage, including drawer headings and bodies. Frames inspected. |
| 39 SVG text-size flags | The audit reports font size in SVG user units. Final actual text bounds are about 12 px high at 680 and phone widths, 16 px at 1366. The opening figure is now measured after its drawer opens too. |
| 7 first-tap welcome omissions | Allowed Curiosity behaviour under BASELINE 16. Instrument hints remain reachable through Read; no new welcome is added. |
| 1 Manual scroll flag | Sources are links after the Manual's prose, not a short set of instrument choices. The Manual scrolls, with Close in its sticky heading. |
| 2 hint visibility flags | The saved default and blank-paper frames visibly show the required hints in the paper. Initial hints intentionally disappear after action; current hints remain on Read. See `fix-audit/state-blank-paper-680x425.png`, `fix-last/phone-rest.png`, and `fix-voice/evidence.json`. |
| 1 B′/H′ overlap | Confirmed at 680x425, fixed by glyph-bound placement, re-shot at 680, 1366 and 375. `fix-edge-after/golden-680.png`, `golden-1366.png`, `golden-phone.png`; all three return zero intersections. |
| 1 iframe-context error and 1 missing-hint flag | Audit harness failed to enter the phone iframe, so that part is not claimed as audited. Independent drive.py host runs at 375x812 cover default, circles, blank paper, I.2 and both pentagon subfigures. Their frames and numbers are preserved. |

Motion off and resize checks were clean; every held-click control row reports no errors and no unintended movement, and the keyboard Enter follow-ups pass. The repeated- and quick-click sections are clean. All 27 audit frames and all four final Book contact sheets were inspected.

Final bundle: 106,696 bytes, with no syntax, external-resource, draft-field or notes-section failures in the scoped check_tools.py checks (`fix-static.json`). Zero source em dashes. Targeted driver batches report zero tool console errors; the initial before host's favicon 404 was a test-host issue, removed in the host harness. Voice capture records no HTTP requests.

#### Frames looked at

All targeted before/after, polish, verification, final size/mode and voice frames were inspected, including the 19 contact sheets in `fix-gallery-checks/` and the six native final frames in `fix-last/`. Final cursor and both permitted model frames were inspected in `fix-cursor/`. Models were actually used (Beat Lab play/stop; Elements Inspector element and zoom controls). No other tool was changed. The 14 edge-case frames were inspected through `fix-gallery-edge/`, including both before frames and all 12 final scoped shots.

#### Curiosity check

The four short-test answers remain yes: open drawing invites unassigned play, the real construction has adult depth, geometry is the working interface, and the instrument needs no score or finish. This fix preserves the three lenses' short-test verdict rather than claiming a new cold review. Compare `fix-last/triangle-log-final.png` beside `fix-cursor/model-elements.png`; Beat Lab was also opened and played.

#### Left open

Cleanup limitation: debug ports 9910, 9911, 9912 and 9913 are closed and tools/compass-and-straightedge/host.html is removed. The detached local Python host on 8715 still responds. Windows returned `ERROR: Access denied` to termination of the verified `python scripts/drive.py compass-and-straightedge --host 8715` processes. Identified PIDs: 16768, 27300, 38720, 41340, 48100, 49672, 59992 and 62032. Exact commands and errors are in `fix-server-cleanup.json`; no permission bypass or unrelated process termination was attempted.


The spec's module-reach question is deliberately unchanged, as refine.md directs. The existing recordings are still absent; the spec's browser-speech fallback remains. No claim of a Chromebook hardware benchmark. Optional recognitions beyond I.1, IV.6 and IV.15 were not added, as only cheap, sure detections were requested.

The report was assembled in Scratch and copied to polish.md only after all checks, honoring the user's explicit stop condition over the early-report instruction. Unattended decisions followed the brief: unmatched studies get their own primed letters; unconfirmed scan ranges are omitted; no confirmation was requested.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Compass and Straightedge handoff

src.html contains independent CSS, semantic controls, the geometric engine, SVG rendering, and the 15-page Book.
The source is bundled with kit:curio for shared voice and power settings. No kit stylesheet is used.
History stores only points, objects, log, serial, nextName and unitLabel. Instrument settings, view and Book ghosts stay put.
Made intersections record parent object IDs; deletion cascades.
Ghost reference geometry is kept outside the student's point set. Book sub-constructions are compound where named.
Scratch contains bounded command runner, numerical/interaction evidence, screenshots, and audit results.
Geometry changes are synchronous; createObject coalesces SVG painting through requestRender. Keep that separation:
the 47-object, 1,115-point classical pentagon replay otherwise spends too long redrawing intermediate states.
The full replay is _scratch/compass-and-straightedge/pentagon-method.js. It adds no free points and never retains a radius.
Blank paper labels its unchanged reference unit u, because its new free points can also be named A and B.

#### Cold review changes
Read uses currentHint() for the active instrument, selected anchors and blank paper. Only the initial hint speaks automatically.
The Book figure renders requested steps too, so the open drawer never hides an action's only visual response.
IV.16's bisector now points midway between the 72-degree and 120-degree vertices; the trisection page draws both halvings.
lineShape clips infinite lines to the paper, including when both defining points are off screen.
validSavedState checks a device slot before checkpoint/restore. Malformed data must leave the live sheet untouched.
MacTutor's CC BY-SA 4.0 text licence is named explicitly; only factual paraphrases are incorporated.
Audit follow-up: nearby point labels try alternate positions with fine dashed leaders; geometry and hit areas stay exact.
The phone zoom tag sits at the upper-left, clear of the idle compass. The resting edge is under the strokes at the table edge.
Counts use singular nouns at one; tiny nonzero magnifications use scientific notation.
Repeated presses of the same instrument retain valid speech; actual tool changes still hush it.

#### Refine fixes
Tangencies collapse roots with half-separation within 1e-7 times the larger radius. Crossings merge within
1e-7 times the largest stroke size (at least one unit); free and given points retain the 1e-9 threshold.
Book guides use similarities onto matching givens. Unmatched studies sit beyond the drawing with primed letters.
IV.11 shows each compound sub-construction separately so its repeated A and B cannot label different points at once.
Point names after Z use numeric subscripts. Dense, unselected crossing labels hide until hovered or selected.
Pointer motion requests one render per animation frame. Point dots share SVG paths, the record is cached, and a
readout's live text changes only when its value does. Its position avoids visible point labels and controls.
The two new margin identifications require a closed square or regular hexagon of actual chords on the given circle.
Book lettering is placed from actual SVG glyph bounds, with short leaders where needed. The drawer opens before
the figure is measured so the first figure is as legible as subsequent steps at 680x425.
Older saves without reference-placement metadata derive it on the next Book step; malformed placement data is rejected.
The IV.10 transfer explicitly refers to the longer part of the preceding golden division, rather than an absent H.

#### Engine changes wanted
kit/curio.js: allow a caller-supplied power-button label formatter instead of replacing button text with emoji.
This tool applies its own plain lamp-panel labels through onMotion and onSound callbacks.

#### Decisions
The report is written last because the user's explicit stop condition overrides the early-report instruction.
Trisection says no construction works for every angle; some angles do trisect.
The first triangle requires selecting Edge after the two compass circles. The spec implicitly changes instruments.
Join A to B to close the drawn outline too; the three-vertex triangle can already be measured before that final stroke.
No marked-ruler extension; the spec defers it. No raster art, because exact drafting material is the interface.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
