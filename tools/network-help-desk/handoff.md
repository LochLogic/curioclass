# Network Help Desk handoff

`src.html` is a kit-starter tool: inline styles, Calls/House controls, SVG scene and content/state logic. `CALLS`, `QUESTIONS`, `CAUSES`, `KIND_TEXT` and `L` hold the teaching content. Caller words stay on screen only. The four revised Q4 answers follow the updated spec.

A claim selects `chosenKind`, then that kind's cause. Three stable kind buttons stay visible beside the chosen causes. `claim` judges evidence first, then kind, then cause. All weak evidence gets the same reply, no cause confirmation or added effort. Call 1 requires both Q4 and Q1. Other calls follow the written any-one-key rule. A third selected clue replaces the oldest. APIs are one-based; optional fourth claim argument supplies a kind for tests. `chooseKind` is exposed too.

The fixed footer keeps eight 44 px phones in view. Solved puts Next call or Shift report beside the stamp, with the fix and proof below in a scroller. Shift report actions stay at the top. Only clue/report bodies scroll; kind/cause buttons do not. Questions/evidence buttons keep stable nodes and focus. No focus is taken on load.

`makeGraph` and `syncGraph` hold connectivity in model coordinates. `renderGraph` projects it into real pixels. Room floors and named tablet spots use the same design-to-pixel transform. Some fixed device icons have responsive positions within their rooms to keep hit areas apart. Room labels have fixed positions per layout. The internet cloud is outside the walls; its route has via points clear of devices. Unknown links are grey dotted; broken links are grey with break marks; Guest is orange with a distinct dash pattern.

`runPing` uses Net.token/send and 300 ms hops, after the fixed 1500 ms fix. A wrong physical connection test inserts a hidden fault point. `state.fault` carries it into redraws during a resize; model synchronization skips drawing-only nodes/links. Call 5 stops at the router. Failed login/guest markers sit beside the router. Every call/mode change stops movers and clears retained tokens. An interrupted fix rolls back. Motion uses the engine's per-tick calm check, no tool-side token observer or Net.place workaround.

House uses Net.path/reach, with `skip: l => l.guest` for printer targets. It exposes only applicable device settings, has kind/pass-fail results and live tablet bar counts. Arrow keys still move 20 model units, described to students as one small step. Bounds remain 0..1000 by 0..600. Returning in range restores the House hint. Reset restores defaults.

Voice is Curio.voice with mode scope, immediate tool-owned hint and Read returning that exact hint. No welcomeAfter on this two-mode tool. A first action's own line skips the welcome; a later mode entry or Sound on can bring it. Solved plus the once-only Next call how line is a kit sequence, so another how line cannot replace it while waiting. Obsolete claim instructions stop when Send fix is pressed; a generic welcome is not included in that cancellation. Every V.allLines string is in voice/lines.json. No recordings.

## Numbers check

Unrounded model distances from (300,330): Living room 108.1665, Kitchen 255.5386, Bedroom 361.3862, Back door 480.8326, Shed 648.4597. Rounded: 108, 256, 361, 481, 648. The spec lists Kitchen 255; its two bars are unchanged. Thresholds use unrounded distance, and the spec was not edited. Nothing on screen displays a distance.

## Engine changes wanted

None. Both approved backward-compatible changes are implemented in kit/network.js: glide reads calm() every tick, and optional skin.linkStyle supplies up-link color/width/dash in draw and update. The skin option is documented. The proposed homeOnly path/reach option was declined; the documented guest skip recipe is used. Recipes and the family table were left intact.

Polish evidence is under the allowed temporary directory, `C:/Users/Cory/AppData/Local/Temp/network-help-desk-polish/`. It includes the full audit, follow-up page checks, real-input voice logs and internet-journey regression. See polish.md for exact results, open issues and browser/server cleanup. The previous codex-report.md is an unchanged historical build report.
