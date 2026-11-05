# Codex report: workplace-scenarios

## Built

Built the eight-stop camp day, delayed arrivals, locked choices, three ordered notes, partial and complete ripple maps,
thread inspection, rewind, New day, Job card, keyboard shortcuts and device-only saving. No scores or win state.
Uses the shared kit for Motion, Sound, Read, speech and tones. Metadata stays `tool.draft.json`, stage `built`.
Final offline bundle: 832,158 bytes, about 812.7 KiB, below 2 MB. No tool HTTP requests or browser exceptions in the checks.
Build only. No commits, branch changes, shared-engine edits, deployment or polish round.
All remaining repository changes are inside this tool. Generated Python bytecode outside it was cleaned up.
Every Chrome and server started here is closed. Ports 9980, 9981, 9982, 9983 and 8785 were verified closed; host.html is absent.

## Numbers check

Independent Scratch `numbers.py` enumerated 3 to the eighth power: 6,561 days.
Problem pickup: 5,103 days, 77.78 percent, rounding to the spec's 78 percent. Ordinary pickup: 1,458.
Threads range from 10 to 12. All-A has 10; all-C has 12. Every day has eight openings and all three notes.
Verified 15 minutes of lateness, eight Bluebirds, sixteen children across two groups, twelve practices and fourteen active images.
Scratch `validation.js` checked the implementation across all 6,561 paths: zero failures after fixing duplicate thread ids.
Pickup priority, conditional vote result, no phantom stopped_count pickup thread, note presence and unique endpoints were checked.
No numerical discrepancy with the spec remains. Source checking confirmed the current Advance CTE list differs from the old list.
The spec's 2012 tags are retained and explicitly identified as that edition. Official source links are in notes.md.

## Feel check

Played complete all-A and all-C days with real held clicks, read the outcomes and notes, inspected threads, and replayed from lunch.
Best moment: a decision at craft time reappears at the field, then the vote lets Mia join in. The two distinct landings can be traced.
Flat moment one: the old car backdrop showed mostly ceiling at laptop size. Made a new traffic painting, then cleaned its markings.
Flat moment two: early map curves crossed the object badges and crowded the words. Moved curves into a separate lane with note endpoints.
Also removed oversized blank space in compact story cards and brought selected thread details into view.
Compared the final opening beside Snowy Mail Route in Scratch `feel-comparison.png`; also opened the Beat Lab bar frame.
The scene has comparable visual weight and a clear first action. It is a story-driven replay, with discussion supplying the longer class pace.
Bar tools were bundled in Scratch so their repository folders stayed untouched.

## Done when

1. PASS. All stop-1 craft variants and pickup priorities checked exhaustively; craft and two-arrival field frames inspected.
2. PASS. Problem versus ordinary pickup choices checked for every possible day, including precedence over silent.
3. PASS. Real held-click all-A and all-C runs produce exactly 10 and 12 threads. Words, icons and patterns are present.
4. PASS. Notes follow the stated clause order. Replaying lunch changes Dev's note and the field opening.
5. PASS. Rewind preserves the earlier prefix and clears the selected decision onward. New day clears its key; reload restores choices and position.
6. PASS. No score, meter, stars or winning ending appears. Counts describe stops and consequence threads only.
7. PASS. Story card occupies 76 percent of the laptop stage width and 71.5 percent in compact previews; map curves span its board.
8. PASS. Actual path taps during drawing finish it and open both ends. Rewind during drawing acts immediately. Choice speech interrupts stale openings.
9. PASS. Day choices stay visible at every required size. Preview text is at least 14 px. Projector choices are 64 px tall.
10. PASS. All eight active backdrops and six badges load. Art was inspected; no people or fake lettering in active paintings.
11. PASS. Five-stop, two-second pace log starts five result events; stale openings drop. Next how-to starts once at the final pause.
Read priority, dialog Escape, numeric keys, blocked storage and no focus on load also passed actual browser checks.

## Wave lessons

- PASS, hint and voice: synchronous state hints, Curio.voice, V.heard for how lines, Read priority and valid event sequences.
- PASS, focus and layout: stable choice buttons, preventScroll focus, visible selected-thread detail and dialog focus return.
- PASS, sizes: all eight STANDARDS sizes, including the true 375-wide iframe. Header targets have an explicit 44 px minimum.
- PASS, no giveaways: flag ids and consequence kinds are hidden during decisions; practice tags appear after choosing. Choices lock.
- PASS, honest numbers: no modeled estimate or strength meter. All displayed counts come from the current story state.
- PASS, standards: solo decisions practice responsibility, communication, creativity, problem solving, integrity and teamwork.
- PASS, Motion off: audit found no endless animation; the daylight loop explicitly stops and map drawing becomes instant.
- PASS, short choices: all three full answer texts remain in view, with no answer scroll panel.
- PASS, resize mid-animation: audit stress across every listed state reported no exceptions or controls left disabled.
- PASS, welcome timing: first choices speak their own results and skip the welcome, as STANDARDS requires. No welcomeAfter.
- PASS, unknown as unknown: unanswered stops say Not played yet, with gray badges and dashed nodes. Their text retains the muted contrast color.
- PASS, one look, one meaning: solid plus, dashed minus and dotted dot survive the draw animation and grayscale.
- PASS, truthful badges: named object badges identify the fictional people; no misleading allowed or success status is added.
- PASS, hints change back: mode entry, rewind, reset, result and dialog closure compute their hints from current state.
- PASS, no answer by copying: choices require weighing the scenario; no hidden-answer label is duplicated as a diagnostic clue.
Measured contrast on white: blue 4.85:1, muted 6.15:1, helped 5.38:1, cost 5.48:1, mixed 4.83:1.
Blue on paper is 4.54:1; ink on paper is 14.2:1. Scene titles have a dark backing; curves use full-opacity colors.

## Audit leads

Ran the audit once, with port 9981 and host port 8785, within its 30-minute limit. It completed with 89 historical leads.
Full original report: `S:/CurioClass-codex/_scratch/workplace-scenarios/audit/audit.md`.
Every lead is covered by these groups. The full audit was not repeated; fixes received targeted checks.

- FIXED, narrow Day/header targets: explicit minimum width of 44 px. Final phone measurement confirms every header button is at least 44 by 44.
- EXPLAINED, field inline-span overlaps: multi-line inline bounding rectangles overlap; the painted words do not. Inspected compact, phone and tall frames.
- FIXED, small SVG geometry: hit strokes are now 44 px, with nearest-curve selection. A real tap 20 px off the curve selected the correct thread.
  The old audit measures the thin path's geometry rather than its expanded transparent hit stroke. HTML thread buttons also provide 44 px controls.
- INTENTIONAL, map navigation beyond the scroll edge: this is an eight-column causal map, not a hidden answer set.
  Narrow screens pan horizontally; notes and thread labels scroll vertically. All three Day answers stay visible without scrolling.
- INTENTIONAL, path across path: causal threads cross. Selecting one highlights it and displays its two exact texts.
- FIXED, symbols covered by paths: all symbols now paint after every curve and their positions are staggered.
  Curves sit beneath HTML controls. The reveal animation preserves solid, dashed and dotted meanings throughout.
- FIXED, focused thread label hidden after scrolling: selection now focuses the visible detail panel with preventScroll.
  Corrected real-click check at 680x425 confirms focus on thread-detail, with bounds y=108 to 178.6.
- INTENTIONAL, Job card keep-region coverage: the modal makes the underlying hint and Job card button inactive. Close is visible and Escape returns focus.
- INTENTIONAL, welcome skipped after first choice: the choice's own result takes precedence, exactly as STANDARDS requires.
- FIXED, quick same-mode taps cutting welcomes: active-mode taps preserve current speech. Day and empty-map retap logs show one uncut welcome each.
- FIXED, Sound moving four header controls: reserved its width. Targeted before/after coordinates changed by zero for every header control.
- FIXED additionally: no Day welcome behind Job card; empty-map welcome names Day; singular one-thread caption; full-opacity thread contrast.
Audit Motion off, every resize stress, five held clicks and browser error columns were clean.
Two audit-host connection-reset traces came from closed local test connections, not tool JavaScript exceptions.
Earlier manual host favicon 404s were outer-host noise; the final host checks use a data favicon and report zero errors.

## Frames looked at

Scratch: `S:/CurioClass-codex/_scratch/workplace-scenarios`.
Inspected 131 shot PNGs, including all 76 audit frames, individually or on full contact sheets with detailed follow-up frames.
Complete filename inventory: Scratch `frames-reviewed.txt`.
Collections: bars-frames, early, final-day, final-map, functional, fixed, recheck, pre-audit, audit, targeted, audit-fixes, focus-check.
Includes every required size, both modes, partial and full days, two arriving ripples, results, notes, rewind, Job card, keyboard, Motion off and grayscale.
Also inspected the art sheets, finished car at its 1400-pixel size, final badge sizes and the side-by-side bar comparison.

## Art made

Fourteen active images: eight backdrops and six badges, about 554.8 KiB of active WebPs.
Made six object badges and a new car painting during this build using the built-in image tool, eight generation/edit calls total.
The car received one cleanup edit for blank markings and softer rendering. Seven existing camp backdrops remain active.
Sixteen WebPs are retained, about 655.9 KiB total, including the original car and unused first car revision. Final bundle is 832,158 bytes.
Full prompt set and provenance: art/prompts.json. Raw new PNGs: art/raw/. No paid art.py generation or audio recording was run.

## Art still to paint

None. No people assets or placeholders are required.

## Engine changes wanted

None. Shared kit and family files were not edited.

## Left open

No known functional blocker. The long map deliberately scrolls on narrow screens; notes can sit below the fold.
Narration uses the browser fallback. Bank voice metadata is casual-peer, Zubenelgenubi; recordings were not made, as instructed.
The three spec questions are settled in handoff.md: labeled 2012 tags, original group-chat wording, and object badges without portraits.
Cold review remains the next workflow step. No polish round was started.
