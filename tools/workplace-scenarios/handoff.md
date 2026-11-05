# Workplace Scenarios build handoff

Build only, 2026-10-30. No git commits. Cold review and any later polish belong to the next chat.

## Files and structure
- `src.html` began with the kit starter. It contains responsive scene CSS, stable choice controls, the map renderer and controller.
- `story.json` holds the exact openings, choices, results, arrival variants and ordered note clauses. The bundle inlines it with `json:story`.
- `art/prompts.json` retains the eight existing backdrop prompts and adds six generated object badges plus a revised car backdrop.
  The active car is `wp-car-final`, made after a cleanup edit of `wp-car-v2`. The original car and first revision are retained as unused variants.
  Raw generated PNGs live in `art/raw/`; finished WebPs are bundled with `art:` tokens.
- `voice/lines.json` lists all fixed narration and choice text for Read. Bank voice: casual-peer, Zubenelgenubi. Browser speech is the current fallback. No recordings were made.
- `audit-states.json` describes actual input paths into results, arrivals, both maps, rewinds and the Job card.

## Tricky logic
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

## Open questions settled for this build
1. Keep the spec's 2012 practice tags and explicitly identify their edition in Job card and notes. The current Advance CTE resource uses the modernized 2024 list, so the old codes are not claimed to be current. No new standards or topics were added.
2. Keep the supplied stop-4 group-chat wording, including the unkind message. Its social consequence is the teaching moment. Content is noted in teacher notes.
3. Keep the six object badges rather than portraits. All six were made during this build. No people or body parts appear in generated art.

## Engine changes wanted
None. All changes are inside this tool; shared kit files are untouched.

## Next
See `codex-report.md` for final evidence, audit leads and any limits. The build uses local device storage with try/catch. Keep the draft metadata until the owner promotes it.

## Build evidence
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

## Cold review changes, 2026-11-03
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
