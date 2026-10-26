# Decision Tree navigation plan

Cory's review: "needs better navigation and graphics". This file is the navigation half; `art-plan.md` is the
graphics half. Both are meant to be built in one pass (the art wiring in art-plan.md assumes the sign and story card
below).

Looked at frames from `scripts/drive.py` (muted headless Chrome, real layout) at 1366x768, 1280x720, 1920x1080,
680x425, 800x500 and 760x900, in Grow (empty, planted, graft mode, Next month with graft, choose card) and Side by side.
Positions below are measured `getBoundingClientRect` values with Double Booking, one goal on, A to D planted.

## What is confusing today

1. **The story is off screen where most students sit.** The setup paragraph (`#setup`, the only place the dilemma is
   told) sits at y 773-833 at 1366x768 (below the 768 fold, after the keys tip) and at y 456-504 in the 680x425 and
   800x500 boxes. In those layouts the picker cards show only "Dev / Kai / Nia / Theo". A 7th grader sees four names,
   four goal chips about "the team" and "Ana", and a wooden sign saying "Practice or the party?", and has to guess
   what the decision is. Only the 1920x1080 frame shows the setup without scrolling.
2. **The first screen has no "start here".** On open the stage is an empty hillside with three faint bands and tiny
   rotated labels; the only instruction is one line of small text at the top of the panel ("Tap an option to plant it
   as a branch."). The panel shows picker, chips, options, slider and six tool buttons with equal weight, so nothing
   says which to touch first, and nothing says to pick goals at all (the hint only asks for goals after something is
   planted).
3. **No sense of where you are in the activity.** The intended path is: read the dilemma, pick what matters, plant
   options, slide time, then make a call or choose a branch. Nothing on screen shows those steps or which are done.
   The hint line changes silently (`hintParts`), in muted 14 px text, and is easy to miss.
4. **Buttons go grey with no reason.** `Make a call` is disabled until two branches are planted, a goal is on and time
   is before Next month; `Choose a branch` is disabled until Next month (`updatePanel`, lines 812-814). A student who
   slides to Next month first then finds `Make a call` grey and never learns it had to come earlier. Pressing a grey
   button does nothing, so there is no message either. (`Graft` already handles this well: with fewer than two planted
   it flashes "Plant at least two branches first.")
5. **Sub-modes are easy to get lost in.** In graft, call and choose modes the only signs are the pressed button in the
   panel, dashed outlines, and the hint line. On the stage, where the student is tapping, nothing says "you are
   grafting, tap two branches" or offers a way out. Escape works but is only listed in the keys tip, which is hidden
   in compact.
6. **The tool row is a flat grid of six.** One-shot challenges (`Graft`, `Make a call`), a view toggle
   (`Who it touches`), the ending (`Choose a branch`) and utilities (`Print tree`, `Clear tree`) look identical. In the
   680x425 and 800x500 boxes the whole row sits at y 509-603, fully below the fold, so Graft, Make a call and Choose
   cannot be reached without scrolling the panel (panel content 553 px in a 369 px box).
7. **Time is in the panel, its meaning is on the stage, and the two are not linked.** The slider ticks say "Right
   away / Next week / Next month"; the stage bands say the same in 13 px rotated text at the far left edge
   (`buildStatic`, lines 588-595). The current band is not highlighted, so students do not see that the slider is
   "how far up the tree you are". `Play` at Next month silently jumps back to Right away (`play`, line 955).
8. **The ending is a dead end.** The choose card offers `Back to the tree` and `Next dilemma` only. Side by side (the
   second half of the lesson: same choices, different goals) is never suggested, and the card does not show the path
   the student took (goals on, branches planted, their call) so the look-back question has nothing to look back at.
9. **Side by side opens with no next step on the stage.** Two full trees appear with "Pick a goal" badges; the
   instruction is in the panel hint, and the panel heading "Goals A" does not say it means the left tree.

## Fix list

Each fix names the src.html functions and lines it touches (line numbers from today's file). No new modes, no new
state beyond what is listed.

### N1. Step strip (the main fix)

A row of four numbered steps at the top of the panel, replacing the plain hint position: `1 What matters`,
`2 Plant`, `3 Slide time`, `4 Choose`. Each step is a button (44 px tall, numbers in circles) showing one of three
states: done (check), current (brand fill), not yet (outline). Under it, the existing hint text becomes the "do this
now" line, in 15 px ink (not muted), so the hint and the strip read as one guide.

- Done rules: 1 when `state.goals.size > 0`; 2 when `state.planted.size >= 2`; 3 when the slider has reached Next
  month this dilemma (new `state.reached`, set in `setT`, cleared in `pickDilemma`/`clearTree`); 4 when a branch has
  been chosen (new `state.chosen`, set in `branchPick`). Current = the first step not done.
- Tapping a step moves focus to that section: 1 the first goal chip, 2 the first unplanted option card, 3 the slider,
  4 runs `chooseBtn()` if enabled, else shows the N4 reason. Nothing is locked: students can still do steps in any
  order (the class may plant before picking goals).
- Side by side gets its own three steps: `1 Goals A`, `2 Goals B`, `3 Slide time`, done when `gA`/`gB` are non-empty
  and when time has moved.
- Make a call and Graft are not steps (they are optional challenges); they live in the N5 "Try" row.
- New: `buildSteps()`, `stepState()`; HTML at line 282 (a `<nav class="steps" aria-label="Steps">` before `#hint`);
  CSS near line 69. Touches `updatePanel` (render the strip each update), `setT`, `branchPick`, `pickDilemma`,
  `clearTree`, `setMode` (swap step sets). `window.__tool` gains `stepState` for verify.
- Compact (680x425 to 1000x625): the strip is four 44 px number circles with the hint text beside them in one row
  (no step words), so it costs one row, not two. Stack: the full strip above the time box.

### N2. Story card on the stage, and the sign as its button

The dilemma is told on the stage, where the eyes are.

- Empty state (nothing planted): a card in the middle of the stage with the kid's portrait (art-plan `kid-*`), the
  title, the setup text and two short lines: "1. Pick what matters to {name}." "2. Tap an option to plant it." In
  compact it also holds the four dilemma cards (see below). It is not a dialog: no focus trap, the panel stays live,
  and it fades out on the first plant.
- The wooden sign on the trunk becomes a real button in `#lay` (today an SVG rect plus text in `buildStatic`, lines
  601-605), labelled "{name}: {sign}" with a small "story" mark, painted with the `sign-plank` art. Tapping it reopens
  the story card at any time (Escape or tapping it again closes it).
- Picker placement: wide and stack keep the picker cards in the panel (now with portraits). Compact moves the picker
  into the story card, which frees about 53 px of panel height (see N6). In the short wide layout the setup paragraph
  `#setup` leaves the panel (the story card replaces it); in the tall wide layout (900 px and up) it stays.
- New: `showStory()`, `state.story` (open/closed), `.story` CSS. Touches `buildStatic` (sign out of the SVG),
  `renderTree` (none), `updatePanel` (setup paragraph visibility), `relayout` (move `#picker` between panel and
  story card for compact, the same way it already moves `#detail` and `#swap`), `togglePlant` (close the story on the
  first plant), `pickDilemma` (open the story), keys (Escape closes it).
- Voice: the story card uses the existing `setup-*` lines; no new clips.

### N3. Time on the stage

- The current band is highlighted: its fill goes to a brand tint (`#eef4df` at 0.75) with a 3 px brand left edge;
  bands above the slider stop get a faint dashed top edge ("not grown yet"). These rects move from `buildStatic`
  (lines 588-595, static) to `render` as keyed dynamic elements so they change with `state.t` without a rebuild.
- The rotated band labels become buttons in `#lay` (CSS `writing-mode: vertical-rl; transform: rotate(180deg)`), 26 px
  wide by the band height, that call `setT(j)`. The current one is white on brand. They stay out of the tab order
  (the slider is the keyboard control; tabindex -1) so the panel-first tab order holds.
- `Play` at Next month reads "↺ Replay" (label and aria-label) so the jump back to Right away is expected
  (`updatePanel` line 805).
- Touches `buildStatic`, `render`/`renderTree`, `updatePanel`.

### N4. A reason instead of a dead grey button

`Make a call` and `Choose a branch` stay pressable (`aria-disabled="true"` plus the faded look, not `disabled`). A
press when not ready flashes the reason in the hint line, exactly like Graft's `few` flash:

- Make a call, not ready: "Plant two branches and turn on a goal, then make your call before next month." At Next
  month: "Calls are made before next month. Slide back to make one."
- Choose a branch before Next month: "Slide time to next month first, then choose a branch."
- Touches `callBtn`, `chooseBtn` (flash instead of silent return), `updatePanel` (lines 811-814: `aria-disabled`
  instead of `disabled`), `keepFocus` (no change needed, the buttons no longer vanish from focus).
- Voice: three new `L` lines (`callWhen`, `callLate`, `chooseWhen`), so `voice/lines.json` changes and
  `scripts/voice.py decision-tree` records three clips (bank voice `casual-peer`, about 15 KB each).

### N5. Tool row in groups, a mode bar on the stage

- The tool row splits into a labelled group "Try" (`Graft`, `Make a call`, `Who it touches`) and a smaller utility
  row (`Print tree`, `Clear tree`, as 40 px text buttons). `Choose a branch` moves out of the row: it is step 4 in the
  strip, and at Next month it also appears as a full-width primary button under the time box (brand fill, white text)
  so the ending is unmissable.
- While `state.sub` is `graft`, `call` or `choose`, the step strip row turns into a mode bar in the same place (top
  of the panel, so it is on screen in every layout without moving the tree): a tinted bar with the mode's icon,
  "Grafting", "Making a call" or "Choosing", the existing hint line, and a `Cancel` button (Escape still works). The
  targets on the stage keep their dashed outlines. It uses the existing `graft`, `call`, `choose` lines, so no new
  clips. Cancel returns focus to the tool button that opened the mode.
- New: `showModeBar()` (or a branch inside `buildSteps()`); touches `updatePanel`, the tools HTML (lines 313-320),
  CSS for `.tools` (line 159).

### N6. Compact fit (680x425, 800x500, 1000x625)

Budget for the 369 px compact panel with A to D planted (today 553 px):

| Row | Today | After |
|---|---|---|
| Picker | 48 | 0 (moved to the story card) |
| Steps + hint | hint 33, off screen | 44 (one row) |
| Goal chips (2 rows) | 92 | 92 |
| Time box | 50 | 50 |
| Options (2 rows) | about 130 | about 130 |
| Try row | 94 (2 rows of 3) | 44 (one row: Graft, Call, Who; Print and Clear move to a `⋯` button at the row end that opens a two-item popover) |
| Setup paragraph | 48 | 0 (story card) |
| Gaps | about 30 | about 20 (4 px) |
| **Total** | **about 553** | **about 380** |

About 11 px over with four options; the builder takes it from the compact gaps and option padding and must check
680x425 and 800x500 with real frames. With the graft found (a fifth card) the options grow a row: then the Try row
may scroll, but the chips, options and slider (Done 9's main controls) stay on screen. `Choose a branch` at Next
month replaces the Try row in compact (call is closed by then, graft and who are optional).

### N7. A path trail and a way on from the ending

- The choose card gets a short "Your path" line above the leaves: "Goals on: Keep my word, Have fun. Planted: A, C,
  D, G. Your call: C." (the call only if one was made), so the look-back question has something to look back at.
  Print adds the same line.
- A third card button, `Compare goals side by side`, calls `setMode('sbs')` and carries the Grow goal set into
  `Goals A` (Goals B starts empty, so the Side by side "pick at least one goal" line still applies).
- `Next dilemma` keeps its place. Touches `showCard` (lines 840-862) and `buildPrint` (lines 1020-1037).

### N8. Side by side labels

- The stage labels read "Goals A (left)" / "Goals B (right)" when side by side, "(top)" / "(bottom)" when stacked
  (`trees()`, line 556-557), and the panel headings match ("Goals A, left tree").
- The step strip (N1) carries "1 Goals A, 2 Goals B, 3 Slide time".

### Not changing

- Mode tabs, Motion, Sound and Read in the header; keyboard shortcuts (1 to 5, G, W, P, arrows, Escape); the voice
  queue; all content and math.
- The keys tip moves into a small `Keys` disclosure (`<details>`) at the panel foot, closed by default, in every
  layout (today it takes 104 px at 1366x768 above the fold line).

## Checks for verify

- Every Done-when item in spec.md still holds; Done 9 re-measured at 1366x768, 1280x720, 800x500 and 680x425 with the
  new rows.
- The setup text (story card) is on screen without scrolling at every size on open and after tapping the sign.
- Step states match the rules above after each action, including Clear tree and dilemma changes.
- Pressing a not-ready Make a call or Choose shows its reason and speaks it once.
- Focus: tapping a step moves focus as listed; the story card's buttons are in the tab order after the panel; Cancel on
  the mode bar returns focus to the tool that opened it.
- Spec.md needs updates for N1 to N8 (Screens and modes, Voice for the three new lines) before the build.
