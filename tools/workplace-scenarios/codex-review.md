# Codex review: workplace-scenarios

## Played

Cold eight-stop mixed-consequence day as a grade 7 student before reading builder notes; then all-A/all-C real held-click days and projector/keyboard checks. Clear choices and convincing delayed social consequences; map note taps were the flattest payoff.

## Findings fixed

- Should fix, general, Job card/voice: the modal blocked header Read, and the inventory omitted Read-only choice prefixes, hints and Job card copy. Added Read inside the modal and completed the exact fixed-line inventory.
- Should fix, general, Ripple map: note taps changed only speech/border while their text stayed below the fold. Notes now open visibly at the top, Read follows the selected note, hints update immediately, and stale note speech is discarded.
- Should fix, general, Day on phones: two ripple icons floated together and became detached from their sentences. Each changed sentence now keeps its own icon and line.
- Should fix, general, art: gym rain fell indoors; craft omitted the safety-critical glue guns; lunch omitted cartons/towels; staff had fake wall markings. Repainted four scenes and removed two generated panel artifacts with targeted edits.
- Polish, general, Ripple map: crossing threads competed with the selected one. Dimmed unrelated curves/marks, outlined both endpoints, retained patterns/icons and exact source/destination words.
- Should fix, general, craft: note-button focus is restored when a resize rebuilds the map. Added the longest note-open audit state and matched voice lines/notes/handoff to the changes.
- Polish, general, lunch: the laptop story card now uses 62 percent of the stage width, revealing the juice cartons while meeting the 60 percent focus rule.

## Findings left

- Should fix, general, spec-constrained, Day: A is helpful at all eight stops, so position becomes a shortcut. The spec fixes letters and requires all-A/all-C thread counts. Shuffling needs a spec decision and was not introduced.
- Polish, general: the eight-column map pans on narrow screens and its complete note list scrolls vertically. All Day choices remain visible; tapping a note brings its complete words into view.

## Flattest moment left

The staff-room reflection offers three preset responses rather than having the student name a real keep/change. Preserved the required content. The map payoff now reveals each person's actual note with sound off too.

## Graphics

Inspected all 14 active images at finished size and in scenes. Added four reviewed backdrop variants, preserved original assets and six strong object badges. No people or placeholders; explicit spec requires object badges and people-free paintings.
Built-in imagegen edits; full prompt set and saved WebPs/raw PNGs are in art/. Gym and staff each received one cleanup redraw. Bar frames: Snowy Mail Route and Beat Lab; side-by-side comparison in Scratch review-bar-comparison.jpg.
Fourteen active assets total 652.6 KiB; final offline bundle 969,868 bytes (947.1 KiB). No size exception needed.

## Audit

Completed the single audit within its 40-minute limit: Scratch review-audit/audit.md, 79 frames, 95 mechanical leads. No repeat audit. All audit frames and this review's 135 shot frames were opened, individually or on contact sheets; inventory: Scratch review-frames-looked-at.txt.
Every lead is covered here:

- SVG target bounds omit the 44 px hit stroke. A real held tap about 20 px off a curve selected the expected thread during drawing; rewind during drawing acted immediately.
- Curve crossings are inherent to this causal map. Symbols paint after paths; hit-testing sees the transparent stroke over noninteractive glyphs, but the symbols remain visible. Selected curves and endpoints now stand out.
- Map controls beyond scroll edges are the eight-stop overview, not the Day answer set. Map panning/vertical scrolling is intentional. Day choices stay visible at all eight required sizes.
- Wrapped ripple spans have intersecting inline bounding boxes at 680, 800 and 760 widths; the frames show no overlapping words. Phone ripple sentences now have separate lines.
- Job card deliberately covers/inactivates the underlying hint and Job card button. Its Read and Close controls are visible; Escape returns focus correctly.
- Four missing-welcome leads are intentional: first-choice results take precedence, and no background welcome plays behind Job card, as STANDARDS requires.
Audit repeated/quick clicks, Motion off, keyboard Enter checks and resize stress were clean. No tool console errors in the final targeted checks; restored-page resource check found no HTTP requests.
The narrow Job card Read/inventory repair followed the audit, with 1366, 680, true 375 iframe and keyboard rechecks. The full audit was not repeated.
Independent content check: all 6,561 days, zero differences in openings, pickup priorities, thread endpoints/IDs and ordered notes; 5,103 problem pickups and 1,458 ordinary ones; real all-A/all-C runs gave 10/12 threads. Reload, rewind, New day and blocked storage passed.
Done when 1-6: passed by enumeration and real state checks. 7-10: story-card focus, visible full choices, projector 64 px targets, immediate drawing input and all 14 images checked. 11: five-stop voice log passed.
Read priority and stale-line cancellation passed.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Dev: I saw the group chat. | Event | 5 | 5 |
| Five distinct stop results | Event | 5 | 5 |
| Tap Next to keep the day moving. | How | 1 | 1 |

 All 150 fixed lines match voice/lines.json; longest is 173 characters.
Wave lessons checked: immediate hints/Read, focus, sizes, locked choices, honest counts, six practiced standards, Motion off, resize, welcome timing, unknown stops, distinct thread meanings, true badges, reversible hints and no word-copy shortcut. The fixed-position shortcut remains the named spec exception.
Contrast recomputed: brand/white 4.85:1, brand/paper 4.54:1, muted/white 6.15:1; three thread colors 5.38, 5.48 and 4.83:1. Patterns/icons also work in grayscale.
Official source checks retain explicitly labeled 2012 tags and the supplied general youth-work statement: [Advance CTE](https://careertech.org/resource/career-ready-practices/), [U.S. Department of Labor](https://www.dol.gov/agencies/whd/fact-sheets/43-child-labor-non-agriculture).

## Left open

No commits, shared-kit changes or new features. Browser narration is the supplied fallback; recording audio was prohibited. Object-only people treatment and fixed answer lettering remain explicit spec constraints.
