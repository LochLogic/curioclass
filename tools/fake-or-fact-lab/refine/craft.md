# Craft lens: fake-or-fact-lab (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/fact-check.js and
docs/families/fact-check.md (line by line against the engine). Bundled with `CURIO_DRAFT=1` (570 KB, 585,781 bytes).
`audit_tool.py` run first (ports 9970-9971). My own drives on ports 9972, 9974 (my own iframe host served from my
scratch folder, so the tool folder was not touched) and 9976. Frames and logs in my scratch folder `lens-fof-craft`
(`audit/`, `f1` focus and keys, `f2` sizes in four states, `f3` voice, `f4` 375 host, `f5` targets). The engine's pure
part was also run in Node (`pure.js`: 40 searches, 16 reserved-name cases, the world check).

Counts: blockers 0, should fix 8, polish 6, nits 4.

## Should fix

1. **Focus is dropped to the page body after the main actions.** (general) Seen with real held clicks and
   `document.activeElement` (`f1`, `f5`): after **Lock my call** in Pass 1 the button turns disabled and focus falls to
   `<body>` (lock1b); after Lock in Pass 2 the button is hidden and focus falls to `<body>` while the Expert check
   opens (lock2); **Retest** hides itself and then focuses `#lock`, which is disabled, so focus is lost (retest,
   src.html:838); **Clear lab > Yes** focuses `#clear`, which is now disabled (clear, src.html:843). A keyboard
   student has to Tab from the top of the page each time. BR1 lesson "focus is kept when controls rebuild".
   Better: after an inside lock focus the first verdict (or the `+` now unlocked), after an outside lock focus
   **Next specimen** in the reveal, after Retest the first verdict, after Clear the Lab mode button or the empty
   table's heading.
2. **Enter on a different verdict button locks the old verdict.** (general) src.html:868. Press 1 (Trust it), Tab to
   **Don't trust it**, press Enter: the keydown handler sees a verdict and a `.verdict` target, prevents the button's
   own click and locks **Trust it** (shot enter-change-verdict: `calls: ["trust1"]`, focus on v-dont). The student
   recorded a call they had just tried to change. Lock on Enter only when the focused verdict is the selected one (or
   let Enter on a verdict pick it, and lock only from `#lock` or the body).
3. **375 wide: the page is a 137 px slot and Lock my call is below the fold.** (general) Done when 7. `f4/h-p2-375`,
   `h-p1-375`, audit `size-375x812`: at 375x812 the header wraps to two rows (135 px), the tray, tab strip and the
   two-row address bar leave the page area at y 359 to 496, which shows only the site's own header band and a sliver
   of text; `#lock` is not in view (document 878 px tall); at 375x667 the verdicts are off screen too. The 3-line
   reserved hint also leaves an empty band. The spec asks for page, verdicts and Lock visible at every size and "375
   wide works". Better: icon-only Motion, Sound and Read in one header row under about 480 px (handoff already says
   so), the address bar on one row, a smaller tray (jars 80 px, kind and state on one line), so the page gets
   about 300 px and Lock sits on screen.
4. **Plain plurals and singulars miss in Wayfind.** (family:fact-check) `FC.pure.words` only drops a trailing 's,
   and `search` needs every term word exactly, so each tool must hand-list plural twins (this one did it for
   flood/floods, sunday/sundays, week/weeks, frog/frogs) and still missed some. Node run of `FC.pure.results` on this
   world: "puzzle game", "video game smarter" (S5's key evidence route), "study app", "sharks", "libraries sunday",
   "center for smart studies", "Ms Parks" and "4-day week" all give no results; case is handled ("CENTER FOR SMART
   STUDY" works). Better: fold a plain plural in the engine (drop a final "s" after a consonant other than s, on
   both the query words and the terms; "ies" to "y"), document it in fact-check.md, and drop the twin index entries.
   Siblings then get it for free.
5. **Tap targets and links inside pages are under 44 px.** (family:fact-check) `f5`, audit "small target": the inside
   tap notes on post parts are inline elements, so `.fc-tap{min-height:44px}` does nothing: "@StormWatchNow · 12,400
   followers" is 219x16 (S2's followers card). Inline links: "J. Carter" 58x20 (S4's only Pass 1 route to the author
   page), "A new study↗" 102x23 (S5's Trace), "our 2025 family survey↗" 164x24 (S1's Trace), "See all posts from
   @StormWatchNow" 266x23 (S2). The family doc says "Every target is at least 44 px". Better: in `noteOn`, make an
   inline tap part `display:inline-block` with padding to 44 px; give `.fc-a` in body text vertical padding (or a
   44 px hit area through a `::before`), keeping the text look.
6. **The family doc and the engine disagree in places.** (family:fact-check) BR1 lesson "the family doc matches the
   engine". (a) Doc: every block "may carry `note`, `style` and `cls`"; engine `block()` returns early for `img` and
   `post`, so `style` and `cls` are ignored on both and a block-level `note` on a `post` is silently dropped
   (fact-check.js:603-604). (b) Doc and engine: `maxTabs` is an option, but the default `tooMany` text says "Eight
   tabs is the most" whatever `maxTabs` is (fact-check.js:408). (c) The tap highlight, the "✓ Noted" pill and the
   Inside tag colour are hard-coded to this tool's violet `#6d28d9` (fact-check.js:334-338, 387), so fact-check-desk
   and ad-agency would carry fake-or-fact-lab's brand inside their pages and notebook; the doc says only the
   `--fc-*` chrome variables recolor. (d) Tools hang voice `needs` and CSS on `.fc-newtab`, `.fc-lookup`,
   `.fc-imgbtn`, `.fc-sbox`; only `.fc-sbox` is named in the doc. Better: apply style/cls/note in one place for every
   block, build the tooMany text from `maxTabs`, add `--fc-note` (default the tool's `--brand`) for the tap and
   Inside colours, and list the stable class hooks in the doc. Everything else in the doc checked out line by line
   (below).
7. **The "outside" how line plays after its moment at a 2 s pace.** (general) `f3` run v-2s (vlogs/v-2s.json): lock
   Pass 1, then press `+` 2 s later. "Now leave the page. Press the plus to open a new tab..." queued behind the Lab
   welcome and started at 9185 ms, after the student had already pressed `+` at 6436 ms and was in Wayfind. Its
   `valid` checks the specimen and pass only. Add "only the specimen tab is open" (`browser.tabs === 1`, or no new tab
   opened yet) to `valid`, so it drops once `+` is pressed (the tools and image lines then cover the next step).
8. **The Expert event line is lost at a 2 s pace.** (general) Same run, both specimens tried: the expert line ("Here
   is what the experts found...") queued behind the outside, tools and image how lines and was dropped as `newer` when
   Next specimen came 2.1 s after the Pass 2 lock. STANDARDS: no line is lost at a 2 s pace, and an event line is the
   result the student just earned. At the Pass 2 lock, drop the still-pending Pass 2 how lines (they no longer apply)
   or speak expert with `now`. At a 3.6 s pace it played 5 of 5 (voice table below).

## Polish

1. **Reveal table cut at the preview size.** (general) `f2/reveal-680x425`: the Experts column is cut at the right
   ("Partly tr") and needs sideways scrolling; it repeats the verdict shown just above. In compact, drop the Experts
   column (or the third row) so the student's own two calls fit.
2. **Jar state "Inside done" truncates to "Inside ..." at 680x425, 800x500 and 375.** (general) `f2/p2-680x425`,
   `f4/h-p2-375`. The state word is the jar's signal. Use "Inside" (or two lines) in compact.
3. **"blog" reads "bloq" in the tray at compact sizes.** (general) audit `size-800x500`, `f2/p2-680x425`: the kind
   line's `overflow:hidden` with line-height 1.15 at 11.5 px clips the descender. Give `.jar span` a line-height of
   1.3 or padding-bottom 1px.
4. **The site's own address is clipped in Pass 1 at 760 to 1000 wide.** (family:fact-check) audit 800x500, 1000x625,
   760x900: "smartstudycenter.examp..." loses ".org"; the locked "Who runs this site? Pass 2" button takes the room.
   The host is a fact the student should read. Let the host win over the button label (icon plus "Pass 2" only when
   narrow).
5. **Reload loses the open pass's seconds and can double a tab.** (general) `save()` runs only on a lock or Clear,
   so a reload in Pass 2 restarts that pass's seconds and tabs from the last save; a specimen begun before another
   specimen's lock is saved with `tabs: 1`, and reopening it after a reload counts its tab again ("2 tabs" for an
   inside read). Save on `visibilitychange` (hidden) and when opening a specimen, and do not recount the specimen tab
   when the slot already has one.
6. **Single words find nothing.** (general) "Gazette", "Vega", "frog", "Bright Path" give no results while
   "Port Alder Gazette", "Marisol Vega", "wood frog", "BrightPath" work. A student who types one name gets the
   no-results line. Add single-word terms for the names ("gazette", "vega", "frog", "bright path").

## Nits

1. The Lab screen says nothing about storage until the first reveal ("saved on this device only"); the inside lock
   already saves. A small line under Lock my call, or in the pass badge's first lock message, would cover rule 7 at
   once.
2. In the locked search form only the `<form>` gets `aria-disabled`; the input (read-only) and the Search button do
   not, so a screen reader hears a working search box. (family:fact-check)
3. At 760x900 the Report's Clear lab is below the fold under a six-row table (stack). It is not a main control.
4. drive.py has no digit keys in its key map, so verdict keys 1 to 3 had to be sent as page events (Enter was a real
   key). Not a tool problem.

## Checked and fine

- **Contract:** one file, 570 KB with the four webp photos; no network requests (`performance` resource list empty;
  the only URLs in the bundle are the SVG namespace and the made-up `.example` templates); no console errors or
  warnings in any of my shots or the audit; kit used for voice, tones, motion (no re-implementation).
- **Engine against fact-check.md, line by line:** `FC.pure` hostOf (also `a@b.example`), isReserved (evil.com false,
  `brand.com.example` false, `example.com`, `a.example.org`, `sub.example.net`, `x.example.` true, `x.examples` and
  `xexample.com` false), parseUrl ("/" default, `+` and `%26` decoded), words (lowercase, `'s` and `’s` dropped, little
  words gone), search (all terms, most terms first, then index order), results (each address once), lab;
  `FC.create` opts `services` and `now`; `fc.report` `{bad: [], missing: []}` for this world; `safeDomain`; resolve
  for all service shapes; lock/unlock/locked/locks; note/notes/allNotes/group with `for`; begin/focus/pause/resume/
  setHidden/countTab/seconds/tabs/ms; call (replaces), callOf, calls, clear(g) and clear(), dump/restore; browser
  options `art, chips, noResults, maxTabs, lockLabel, texts` (all 13 keys exist), `onLocked, onNote(note, added,
  tapped), onOpen, onLink, home, focusSearch` and the handle; notebook `{empty, group}`, `refresh(fresh)`, `count`;
  every block type, rich parts, cite/Trace (highlight and "This source doesn't say that."), note tags and `on: 'tap'`
  defaults; one-shot notebook highlight. Exceptions are should-fix 6 above.
- **Report counts:** six tested rows with known calls (`f2/report-*`): "Inside read matched the experts on 1 of 6",
  "Outside read matched on 6 of 6", recomputed by hand from the calls; ✓/✗ marks right on every cell.
- **Saving:** calls survive a reload (persist-a, persist-b: tray reads Tested / Inside done after reload); Clear
  lab > Yes empties calls and storage (`{"calls":[],"notes":[],"T":{}}`) and sets the empty hint; No keeps it and
  returns focus to Clear lab; the try/catch wraps every storage call.
- **Focus kept where the engine rebuilds:** closing tab 3 by keyboard leaves focus on the next close button; selecting
  a tab keeps focus on it; `+` puts focus in Wayfind's box; Hide/Show keeps focus on the toggle; Next specimen
  focuses the new jar; a chip click leaves focus on the page container; nothing takes focus on load.
- **Keyboard paths:** tab order header, panel (verdicts, Lock), tray, browser chrome, page; Enter and Space take a tap
  note once; Enter on the locked `+` and in the locked search box give the locked hint and open nothing; key 2 then
  Enter locks "Partly true" from the body; Enter on a jar opens it and does not lock; the ninth tab shows the
  "Eight tabs" message and opens nothing.
- **Motion off:** audit clean (nothing runs forever); calm shot: the reveal is in place at once, no running
  animations.
- **Sizes:** at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900, in Pass 1, Pass 2 with tabs,
  the reveal and the Report: no sideways page scroll, verdicts and Lock in view, the hint unclipped, the notebook
  chip and pop-up placed inside the window at 680x425. Only 375 fails (should fix 3).
- **Lines:** the 15 strings in `L` equal `voice/lines.json` word for word and in order; `allLines()` is `V.allLines`.
- **Art:** four `art:` tokens, all in prompts.json, no people. **Words:** no em dashes in src, notes, lines, prompts,
  tool.draft.json, the engine or the family doc; "Curio Class" never "Curio" alone; classroom-safe; storage stated
  in the Report panel and the reveal.

## Voice check

Driven with `scripts/drive.py`, held clicks (`hold` 0.12), Sound on, Motion on, logs saved from `V.log` to
`f3/vlogs/*.json` (`as` = spoken, silent, dropped, read).

| line | kind | expected | spoken |
|---|---|---|---|
| welcome (Lab) | welcome | 1 | 1 |
| welcome (Report) | welcome | 1 over 5 Report entries | 1 (a pending Lab welcome dropped as stale on a tested specimen: right) |
| locked (tap the locked `+` or search, 6 taps) | how | 1, then silent | 1, then silent 5 |
| outside | how | 1 over 3 specimens | 1, then silent |
| tools | how | 1 over 3 specimens | 1, then silent |
| image | how | 1 where a photo exists | 1; dropped as stale on S1, S4, S5 (no photo; `needs: .fc-imgbtn`): right |
| expert | event | 5 over 5 Pass 2 locks | 5 at a 3.6 s pace; 0 of 2 at a 2 s pace (should fix 8) |
| Read | read | 5 | 5, hint only each time |
| verdict picks, tab opens, notes | none | silent | silent (tones only) |

- **Repeats:** how lines once then silent, the event line five times at a reading pace. Pass.
- **Stale lines:** fast taps (gap 0.2 s) through lock, `+`, Wayfind, then a jar change and Clear: the outside chain
  is dropped on the jar change and expert is dropped on the hush; no line played after its moment in those runs. The
  2 s pace run is the exception: should fix 7.
- **First tap:** the stage gets the welcome in about 130 ms; a jar and the Tab key get the welcome; a tap on the
  locked `+` gets only the locked line, then the welcome once it ends (welcomeAfter); Report with no rows says
  nothing; Read speaks the hint only; Sound says nothing; Sound off then on brings the skipped welcome once. Nothing
  speaks before the first tap. Pass.
- **Read:** cuts the welcome and speaks the hint, also with Sound off; nothing cut Read off; queued how lines are
  hushed and re-offered later; a mode change after Read starts the next line at once. Pass.
- **Order:** spoken lines follow the action order in every run; no older line after a newer one (expert is dropped,
  not played late).
- Every spoken line matched the screen at its time except "outside" in the 2 s run (should fix 7).

## Audit pilot

`audit/audit.md`, 43 leads, run first on ports 9970-9971.

- **Confirmed:** the small inline link ("See all posts", should fix 5); the 375 problems (should fix 3; but it named
  overlaps, not the real cause, the 137 px page slot and Lock below the fold); the host clipped in the address bar at
  800, 1000 and 760 wide (polish 4); Motion off clean; no console errors; nothing focused on load.
- **Wrong:** "overlaps" at 375 were the page's own content scrolled inside `.fc-page`'s overflow clip; "below the
  fold" at 680x425 were controls inside the page's own scroll box, not the tool's controls; the "clipped" tab title is
  an ellipsis by design; jar text "past the edge" at 375 is the tray's sideways scroll, as the spec asks.
- **Missed:** focus lost after Lock, Retest and Clear (Lock is disabled on a fresh page, so its one held click never
  ran it); the Enter-on-another-verdict bug; plural search misses; the inline 16 px tap notes past the first screen;
  the stale outside line and the lost expert line (its five-click runs never chained lock, `+`, Next at a 2 s pace);
  the doc and engine mismatches; "bloq" and "Inside ..." truncation; the reveal table cut at 680x425; Lock below the
  fold at 375 (it saw only the first screen of the page box).
- **For later lenses:** the script can be trusted for first-screen targets, console errors, Motion and focus on load.
  It cannot yet replace multi-step flows (focus after rebuilds, chained voice), engine checks or reading a scroll box;
  its overlap and fold leads need a second look whenever a tool has its own scrolling pane.
