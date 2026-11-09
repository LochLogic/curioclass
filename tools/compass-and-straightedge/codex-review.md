# Codex review: compass-and-straightedge

## Played

Grade-10 and adult lenses: jittered held drags, the two-circle triangle, keyboard drawing and measuring, independent Book browsing, retained and collapsing openings, ink, erasure, history, paper, saves and printing. The paper and compass invite experiments; the Book was the weakest response.
Process limitation: the first cold load timed out. I opened the builder's report after the retry's opening frame but before the first active input session. This was not a strictly blind play-first review, and I did not conduct a fresh, timed ten-minute play session. Initial document reads preceded the explicit timeout wrapper; subsequent shell commands were bounded.

## Findings fixed

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

## Findings left

- **Polish:** dense constructions still crowd point names. The 47-object pentagon can produce 1,115 intersections; its measurements remain valid, but Fit is a poor inspection view for that density. Pan and zoom remain necessary.
- Review-process limitations are stated under Played and Left open; they are not represented as passing checks.

## Break it

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

## Voice walk

Held inputs at about two-second pace, Motion and Sound on: Compass, A-to-B, B-to-A, Edge, C-to-A, C-to-B, A-to-B, Read. Then keyboard Measure, Read; Sound off, Point, Read; rapid tool changes, blank paper, Read.

| Line or kind | Expected | Observed |
|---|---:|---:|
| Opening "Drag from A to B" | 1 automatic | 1 |
| Main-path requested Reads | 4 | 4 |
| Extra automatic instructions after five tool-switch pairs | 0 | 0 |
| Repeated blank-paper Read, separate batch | 5 | 5 |

Read order: straightedge instruction plus the last move and triangle values; measurement instruction plus 60.00 degrees; free-point instruction; blank-paper instruction. Sound-off Read worked. The final speech queue was empty; rapid tool/sheet changes did not leave stale narration. All 14 fixed hints match `voice/lines.json` and `allLines()`. Evidence: `review-voice/results.json`. After the audit's same-instrument fix, a final voice batch timed out before loading; its single smaller retry passed the full triangle drag path and Read, with one uninterrupted welcome after two Compass presses 0.7 seconds apart, one requested Read and zero errors (`review-voice-retry/results.json`). No recorded knowing-guide clips exist; this tests browser fallback and its log, not recorded performance.

## Facts checked

Source checks were made on 2026-11-05. No outside dataset is incorporated. Reference downloads and the retrieval script are under `../../_scratch/compass-and-straightedge/data/review/` and `review_sources.py`.

- **Fourteen enunciations and three postulates:** Heath, *The Thirteen Books of Euclid's Elements*, Cambridge 1908, public domain in the US: [I-II](https://archive.org/details/thirteenbookseu02heibgoog), [III-IX](https://archive.org/details/thirteenbookseu00heibgoog), [X-XIII](https://archive.org/details/thirteenbookseu03heibgoog). Matched the supplied wording to the primary OCR, accounting for four obvious OCR errors, and cross-checked the corresponding [David Joyce / Clark University propositions](https://mathcs.clarku.edu/~djoyce/elements/bookI/bookI.html). Clark text was used for verification, not copied into the tool. Sampling: the 14 specified enunciations and all three specified postulates, not entire books in the bundle.
- **Equilateral triangle, midpoint, angle bisection, perpendiculars, parallels, squares, copied lengths:** corresponding Heath I.1, I.2, I.3, I.9-I.12, I.23, I.31, I.46 and IV.6; Clark's independent presentation; recomputed engine examples. A collapsing compass's equivalence is a construction model, not a claim about a surviving physical compass owned by Euclid.
- **Hexagon side equals radius; pentagon diagonal/side 1.6180:** Heath IV.15, IV.11 and XIII.8; [Clark IV.15](https://mathcs.clarku.edu/~djoyce/elements/bookIV/propIV15.html) and [XIII.8](https://mathcs.clarku.edu/~djoyce/elements/bookXIII/propXIII8.html); independently checked geometric outputs and (1+sqrt(5))/2. Original calculations and diagrams, no licensed data copied.
- **General trisection impossible, Wantzel 1837, particular exceptions:** [MacTutor Wantzel](https://mathshistory.st-andrews.ac.uk/Biographies/Wantzel/) and [W. Kahan, Berkeley, *Approximate Trisection of an Angle*](https://people.eecs.berkeley.edu/~wkahan/Trisect.pdf). Only facts are incorporated; source prose is not reproduced. The corrected diagram shows 60, 30 and 15 degrees, never a claimed 20-degree construction.
- **Gauss, 1796, age 18; constructible 17-gon and impossible 7-gon:** [MacTutor Gauss](https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/), [Gauss's diary, March 30, 1796](https://tildesites.geneseo.edu/~johannes/gdiary.pdf), and [Freitas and Tavares, *Dividing the Circle*](https://webpages.ciencias.ulisboa.pt/~pjfreitas/pdfs/DividingTheCircle.pdf). Age follows from April 30, 1777 birth before that year's birthday. Facts only; no diary translation or journal figures incorporated.
- **Lindemann, pi transcendental, 1882; circle squaring impossible:** [MacTutor Lindemann](https://mathshistory.st-andrews.ac.uk/Biographies/Lindemann/) and [Lutzen, *The Algebra of Geometric Impossibility*](https://doi.org/10.1111/j.1600-0498.2009.00160.x). Facts only; no source prose incorporated.
- **Mohr 1672, Mascheroni 1797; compass-only point construction:** [MacTutor Mascheroni](https://mathshistory.st-andrews.ac.uk/Biographies/Mascheroni/) and [Hungerbuhler, *A Short Elementary Proof of the Mohr-Mascheroni Theorem*](https://www.math.ch/norbert.hungerbuehler/publications/A_Short_Elementary_Proof_of_the_Mohr-Mascheroni_Theorem.pdf). Facts only, no article text/figures incorporated. MacTutor's actual article-text terms are [CC BY-SA 4.0](https://mathshistory.st-andrews.ac.uk/Miscellaneous/copyright/), explicitly named in the Manual and metadata.
- **Numerical honesty:** original JavaScript geometry, 1e-9 point merge, four-decimal lengths and two-decimal angles. Floating-point measurements are checks on drawings, not symbolic proofs; the Manual retains that distinction and the finite capacity disclosure.

## Sensitivity

Historical attribution only: retain Mohr's priority alongside Mascheroni, Wantzel's general-impossibility qualifier, and Heath's translator credit. No people imagery, cultural stand-ins, hard history or body content. No new sensitivity judgment is needed for the mathematical diagrams.

## Flattest moment left

Advanced Book compound constructions still require patient reading. The repaired moving reference gives each press a material response, but the pentagon's full method remains dense. It stays a browsable reference, without prerequisites or achievement marks.

## Graphics

Preserved cream paper, brass and steel instruments, graphite/ink contrast, maker's plate and quiet Euclid field note. No raster art, placeholders, people or external graphics. Bundle: **90,431 bytes**, about 88.3 KiB. Inspected initial, drags, triangle, Book, blank, keyboard, extremes, repaired states, grayscale, print and all 32 audit frames. Ten final scoped frames confirm the small-screen and extreme-value repairs.

## Short test

- Would a kid open it unassigned? **Likely yes:** the first two drags yield a surprising, usable pair of crossings. This is an informed reviewer assessment, not observed child testing.
- Would an adult play for fun? **Yes:** actual retained/collapsing constructions and the pentagon have depth without a game layer.
- Is the real thing the interface? **Yes:** circles, straight lines, computed intersections and measured relationships are the working surface; requested Book strokes now remain visible.
- Does it work without score or finish? **Yes:** no goal, score, level, quiz, kit header or finish screen. The source search found only geometric uses of "points" among the lesson-creep terms.

| Compass and Straightedge | Elements Inspector comparison |
|---|---|
| ![Working triangle](../../_scratch/compass-and-straightedge/review-voice-retry/final-voice-triangle.png) | ![Elements Inspector](../../_scratch/compass-and-straightedge/review-models/review-elements.png) |

The comparison is material confidence, not palette or lesson flow: one works through exact geometry, the other through atomic structure. Beat Lab's frame was also inspected; no lesson features were copied.

## Audit

Ran once, last, with a 40-minute bound on Chrome 9951 and host 8755. It finished: **371 leads, 32 frames**, all eight required sizes and eight listed states. All 32 frames were opened and inspected.

- 211 overlap leads: 210 are the full-screen SVG beneath its own controls/readouts; one was the real adjacent-point label collision, fixed after confirmation.
- 147 hidden-background leads are inert paper controls beneath modal drawers. The bibliography scroll lead is the Manual's eight source links, not hidden instrument choices; its Close remains available.
- Three missing-hint leads are the deliberately retired first-action hint. Seven missing per-mode welcomes conflict with the Curiosity rule that only the initial appropriate hint speaks automatically; they are not lesson-flow defects to add back.
- The real "1 lines" lead and the quick-Compass interruption were fixed. Five-click stress paths were clean. The audit reported no control-path exceptions/focus loss, no endless reduced-motion animation, and no stuck state or exception during its resize runs.
- Re-shot only the affected point/readout/phone/short-paper states, including the 600-object boundary, and re-walked the main voice path plus the 0.7-second repeated-Compass case. The full audit was not rerun. Final scoped evidence is in `review-final/` and `review-voice-retry/`.
- The actual `check_tools.py` contract and notes checks pass on a scoped draft mirror; its global rebundling entry point was avoided because it would write other tools. No commits or shared-file changes.

## Left open

- Strict cold-order and fresh timed-ten-minute requirements were not met, as disclosed under Played. No child user study, physical Chromebook frame-rate benchmark or assistive-hardware walk was performed.
- The 600-object test used coincident circles, not the maximum possible number of distinct intersections. Extremely dense sheets remain bounded by browser memory and floating-point conditioning.
- Long-log print pagination remains unverified; the tested short construction prints on one clean page. Bank recordings remain absent; no audio was recorded during this review.
- No shared files or kit engines were edited, no commits were made, and no lesson layer was added. All review work stayed in the two authorized folders.
- Chrome ports 9950-9957 and host 8755 were verified closed; the temporary tool-folder host was removed. See `review-cleanup.json`.
