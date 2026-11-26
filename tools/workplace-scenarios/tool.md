# Workplace Scenarios: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: workplace-scenarios

#### Built

Built the eight-stop camp day, delayed arrivals, locked choices, three ordered notes, partial and complete ripple maps,
thread inspection, rewind, New day, Job card, keyboard shortcuts and device-only saving. No scores or win state.
Uses the shared kit for Motion, Sound, Read, speech and tones. Metadata stays `tool.draft.json`, stage `built`.
Final offline bundle: 832,158 bytes, about 812.7 KiB, below 2 MB. No tool HTTP requests or browser exceptions in the checks.
Build only. No commits, branch changes, shared-engine edits, deployment or polish round.
All remaining repository changes are inside this tool. Generated Python bytecode outside it was cleaned up.
Every Chrome and server started here is closed. Ports 9980, 9981, 9982, 9983 and 8785 were verified closed; host.html is absent.

#### Numbers check

Independent Scratch `numbers.py` enumerated 3 to the eighth power: 6,561 days.
Problem pickup: 5,103 days, 77.78 percent, rounding to the spec's 78 percent. Ordinary pickup: 1,458.
Threads range from 10 to 12. All-A has 10; all-C has 12. Every day has eight openings and all three notes.
Verified 15 minutes of lateness, eight Bluebirds, sixteen children across two groups, twelve practices and fourteen active images.
Scratch `validation.js` checked the implementation across all 6,561 paths: zero failures after fixing duplicate thread ids.
Pickup priority, conditional vote result, no phantom stopped_count pickup thread, note presence and unique endpoints were checked.
No numerical discrepancy with the spec remains. Source checking confirmed the current Advance CTE list differs from the old list.
The spec's 2012 tags are retained and explicitly identified as that edition. Official source links are in notes.md.

#### Feel check

Played complete all-A and all-C days with real held clicks, read the outcomes and notes, inspected threads, and replayed from lunch.
Best moment: a decision at craft time reappears at the field, then the vote lets Mia join in. The two distinct landings can be traced.
Flat moment one: the old car backdrop showed mostly ceiling at laptop size. Made a new traffic painting, then cleaned its markings.
Flat moment two: early map curves crossed the object badges and crowded the words. Moved curves into a separate lane with note endpoints.
Also removed oversized blank space in compact story cards and brought selected thread details into view.
Compared the final opening beside Snowy Mail Route in Scratch `feel-comparison.png`; also opened the Beat Lab bar frame.
The scene has comparable visual weight and a clear first action. It is a story-driven replay, with discussion supplying the longer class pace.
Bar tools were bundled in Scratch so their repository folders stayed untouched.

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

Scratch: `S:/CurioClass-codex/_scratch/workplace-scenarios`.
Inspected 131 shot PNGs, including all 76 audit frames, individually or on full contact sheets with detailed follow-up frames.
Complete filename inventory: Scratch `frames-reviewed.txt`.
Collections: bars-frames, early, final-day, final-map, functional, fixed, recheck, pre-audit, audit, targeted, audit-fixes, focus-check.
Includes every required size, both modes, partial and full days, two arriving ripples, results, notes, rewind, Job card, keyboard, Motion off and grayscale.
Also inspected the art sheets, finished car at its 1400-pixel size, final badge sizes and the side-by-side bar comparison.

#### Art made

Fourteen active images: eight backdrops and six badges, about 554.8 KiB of active WebPs.
Made six object badges and a new car painting during this build using the built-in image tool, eight generation/edit calls total.
The car received one cleanup edit for blank markings and softer rendering. Seven existing camp backdrops remain active.
Sixteen WebPs are retained, about 655.9 KiB total, including the original car and unused first car revision. Final bundle is 832,158 bytes.
Full prompt set and provenance: art/prompts.json. Raw new PNGs: art/raw/. No paid art.py generation or audio recording was run.

#### Art still to paint

None. No people assets or placeholders are required.

#### Engine changes wanted

None. Shared kit and family files were not edited.

#### Left open

No known functional blocker. The long map deliberately scrolls on narrow screens; notes can sit below the fold.
Narration uses the browser fallback. Bank voice metadata is casual-peer, Zubenelgenubi; recordings were not made, as instructed.
The three spec questions are settled in handoff.md: labeled 2012 tags, original group-chat wording, and object badges without portraits.
Cold review remains the next workflow step. No polish round was started.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: workplace-scenarios

#### Played

Cold eight-stop mixed-consequence day as a grade 7 student before reading builder notes; then all-A/all-C real held-click days and projector/keyboard checks. Clear choices and convincing delayed social consequences; map note taps were the flattest payoff.

#### Findings fixed

- Should fix, general, Job card/voice: the modal blocked header Read, and the inventory omitted Read-only choice prefixes, hints and Job card copy. Added Read inside the modal and completed the exact fixed-line inventory.
- Should fix, general, Ripple map: note taps changed only speech/border while their text stayed below the fold. Notes now open visibly at the top, Read follows the selected note, hints update immediately, and stale note speech is discarded.
- Should fix, general, Day on phones: two ripple icons floated together and became detached from their sentences. Each changed sentence now keeps its own icon and line.
- Should fix, general, art: gym rain fell indoors; craft omitted the safety-critical glue guns; lunch omitted cartons/towels; staff had fake wall markings. Repainted four scenes and removed two generated panel artifacts with targeted edits.
- Polish, general, Ripple map: crossing threads competed with the selected one. Dimmed unrelated curves/marks, outlined both endpoints, retained patterns/icons and exact source/destination words.
- Should fix, general, craft: note-button focus is restored when a resize rebuilds the map. Added the longest note-open audit state and matched voice lines/notes/handoff to the changes.
- Polish, general, lunch: the laptop story card now uses 62 percent of the stage width, revealing the juice cartons while meeting the 60 percent focus rule.

#### Findings left

- Should fix, general, spec-constrained, Day: A is helpful at all eight stops, so position becomes a shortcut. The spec fixes letters and requires all-A/all-C thread counts. Shuffling needs a spec decision and was not introduced.
- Polish, general: the eight-column map pans on narrow screens and its complete note list scrolls vertically. All Day choices remain visible; tapping a note brings its complete words into view.

#### Flattest moment left

The staff-room reflection offers three preset responses rather than having the student name a real keep/change. Preserved the required content. The map payoff now reveals each person's actual note with sound off too.

#### Graphics

Inspected all 14 active images at finished size and in scenes. Added four reviewed backdrop variants, preserved original assets and six strong object badges. No people or placeholders; explicit spec requires object badges and people-free paintings.
Built-in imagegen edits; full prompt set and saved WebPs/raw PNGs are in art/. Gym and staff each received one cleanup redraw. Bar frames: Snowy Mail Route and Beat Lab; side-by-side comparison in Scratch review-bar-comparison.jpg.
Fourteen active assets total 652.6 KiB; final offline bundle 969,868 bytes (947.1 KiB). No size exception needed.

#### Audit

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

#### Left open

No commits, shared-kit changes or new features. Browser narration is the supplied fallback; recording audio was prohibited. Object-only people treatment and fixed answer lettering remain explicit spec constraints.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Workplace Scenarios build handoff

Build only, 2026-10-30. No git commits. Cold review and any later polish belong to the next chat.

#### Files and structure
- `src.html` began with the kit starter. It contains responsive scene CSS, stable choice controls, the map renderer and controller.
- `story.json` holds the exact openings, choices, results, arrival variants and ordered note clauses. The bundle inlines it with `json:story`.
- `art/prompts.json` retains the eight existing backdrop prompts and adds six generated object badges plus a revised car backdrop.
  The active car is `wp-car-final`, made after a cleanup edit of `wp-car-v2`. The original car and first revision are retained as unused variants.
  Raw generated PNGs live in `art/raw/`; finished WebPs are bundled with `art:` tokens.
- `voice/lines.json` lists all fixed narration and choice text for Read. Bank voice: casual-peer, Zubenelgenubi. Browser speech is the current fallback. No recordings were made.
- `audit-states.json` describes actual input paths into results, arrivals, both maps, rewinds and the Job card.

#### Tricky logic
`flags`, `options`, `incoming`, `opening`, `resultText`, `noteParts` and `threads` are pure computations over a choice prefix. Pickup priority is kept_walking, then split_up, then silent. The current stop's unanswered opening can already receive a thread on a partial map. Notes only arrive after eight decisions.

No thread is inferred from a tag alone. flat_no reaches the field opening, plus the field result only with vote. stopped_count reaches Ms. Ortega's note only. silent reaches pickup only when the pool flags do not take precedence. `noteParts` follows JSON insertion order. Rewind clears the selected decision and every later one, keeps earlier choices and recomputes the story.

The map has an explicit empty lane for curves beneath the decision nodes, with three separate note endpoints. Identical labels may represent distinct destinations, such as opening and result; accessible names distinguish them. Matching HTML thread buttons provide the keyboard route to SVG paths. Motion drawing never locks input.

SVG curves have 44-pixel transparent hit strokes. `tapThread` samples the curves in screen coordinates and selects
the nearest one, so overlapping hit strokes do not simply choose the last path in the SVG. Rewind controls sit above
the SVG. Symbols are painted after every curve. The draw animation clips ink without changing its dash pattern.
Selecting an HTML thread label moves focus to the visible detail panel before scrolling the map to the top.
Repeated taps on the active mode keep the current narration. An empty map's welcome names Day, and no welcome
plays behind the Job card dialog. Sound reserves its width when its label changes.

Choices update stable DOM buttons. Result replacement moves focus to Next only when a choice owned focus. Next and rewind focus A with preventScroll. The native Job card dialog traps focus and returns it to Job card on Close or Escape. Hint updates synchronously. Curio.voice owns speech interruption, Read priority, once-only how lines and event logs.

#### Open questions settled for this build
1. Keep the spec's 2012 practice tags and explicitly identify their edition in Job card and notes. The current Advance CTE resource uses the modernized 2024 list, so the old codes are not claimed to be current. No new standards or topics were added.
2. Keep the supplied stop-4 group-chat wording, including the unkind message. Its social consequence is the teaching moment. Content is noted in teacher notes.
3. Keep the six object badges rather than portraits. All six were made during this build. No people or body parts appear in generated art.

#### Engine changes wanted
None. All changes are inside this tool; shared kit files are untouched.

#### Next
See `codex-report.md` for final evidence, audit leads and any limits. The build uses local device storage with try/catch. Keep the draft metadata until the owner promotes it.

#### Build evidence
Scratch is `S:/CurioClass-codex/_scratch/workplace-scenarios`. `numbers.py` independently enumerates the rules.
`validation.js` checks all 6,561 paths against the implementation. `exhaustive.json` records zero failures after fixing
a duplicate thread id when the same flag reaches two openings. `browser-checks.json` records real numeric keys,
reload, rewind during drawing, dialog Escape, Read priority, blocked storage, zero HTTP requests and zero exceptions.
`all-A-real.json` and `all-C-real.json` record held-click full days. `voice-pause-at-result.json` holds the five-stop,
two-second pace log: five results start, stale lines drop, and choiceHow starts once at the final pause.
`feel-comparison.png` places the final opening beside the Snowy Mail Route bar frame. The audit folder contains the
single mechanical audit and all of its frames. Earlier manual host shots reported an outer-host favicon 404 only;
the offline tool itself makes no network requests.

The single audit completed with 89 historical leads. `codex-report.md` groups every lead by cause and records the
response. The final targeted runs are in `targeted/`, `audit-fixes/` and `focus-check/`. The first focus attempt clicked
a label below the viewport; the corrected check scrolls to the label before its real held click and confirms focus on
`thread-detail`. Do not count the earlier attempt as a tool failure or as a passing focus test.

#### Cold review changes, 2026-11-03
Note endpoints and note cards now call selectNote: the note opens in the shared detail panel, focus stays visible,
and Read uses the selected note. selectedNote and selectedThread are mutually exclusive. Notes have state-valid
speech. Selected threads dim other curves and marks and outline their endpoints; meanings and dash patterns stay intact.
A phone ripple sentence now keeps its own thread icon on its own line. Resize restoration includes note buttons.
Four new backdrop variants are active: wp-craft-review, wp-lunch-review, wp-gym-review, wp-staff-review.
Craft now shows the glue guns, lunch shows cartons and towels, gym rain is outdoors, and staff wall marks are removed.
Prompts and raw PNGs are retained; generated panels in two candidates were removed with one targeted redraw each.
Current review evidence is in Scratch review-* files and directories. No shared kit edits or commits were made.
Browser narration remains the required fallback; no audio was recorded. Portraits and option shuffling would conflict
with the explicit spec. The three preset reflection choices remain as specified.

The audit completed once on the reviewed bundle. Its modal inspection also confirmed that the header Read is inert
behind the Job card, so the existing Read action is now available inside the dialog. jobReadLines normalizes fixed
copy without speaking the Close label; allLines and voice/lines.json include it, the current hint and lettered choices.
This narrow repair received laptop/preview/phone and keyboard checks after the audit, not another full audit.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
