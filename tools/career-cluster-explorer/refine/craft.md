# Craft lens: career-cluster-explorer

Cold Craft lens (REFINE.md), round 1, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py
career-cluster-explorer`, 175 KB (182,033 bytes). Placeholder art and the browser voice not reported.

Counts: blockers 0, should fix 6 (general 4, family 2), polish 5 (general 5), nits 7 (general 4, family 3)

## Contract (all pass)

- One file, 175 KB, well under 2 MB. No network requests: the only URLs in the bundle are the 83 Handbook profile
  links (`<a target=_blank>`), nothing loads on its own.
- Kit used: `kit:curio` (Curio.voice, tone, Motion, init) and `kit:careers` (the sheet and helpers); nothing
  re-implemented.
- No console errors or exceptions in any run (audit, 28 frames, 15 voice runs, 19 keyboard and save runs, 7 frames
  at 375 through the iframe host; the only log line was the test server's favicon 404).
- Motion off: `document.getAnimations()` empty after Where? and after opening the sheet; pan is instant; lantern pop
  and shimmer skip on `Curio.reduce`; the audit's calm check is clean.
- No em dashes; "Curio Class" only; privacy line shown in Festival; no `art:` tokens and an empty prompts.json, as
  the spec says (drawn in code).

## Engine against the family doc (kit/careers.js vs docs/families/careers.md)

Line by line: `money`, `payText`, `jobsText`, `ZONE`, `ZONE_SHORT`, `LEVELS` (names and `means` as documented),
`EDU_LEVEL`, `level`, `outlook` (`{pct, word, dir, arrow, text}`), `inHandbook`, `corr`, `similar` (+0.15 same
cluster, n = 4), `esc`, `FACTS` (`pay`, `training`, `jobs`, `edu`, `outlook`) all exist and behave as written. Sheet
options `data, facts, payLabel, factCols, blocks{afterDoes, afterFacts, beforeSimilar, end}, source, similarCount
(0 hides), closeLabel, theme, onOpen, onClose, afterDraw(box, c, ctx), root` and returns `open, close, isOpen,
current, el, box` all present; defaults ('Typical pay', `['pay','training','jobs']`, 4 similar, the quiz's source
line) as documented. Section order, the 260 ms rise (none with Motion off), bottom sheet under 560 px, tighter under
520 px tall, the ten `--cr-*` variables and `--cr-target` all match. Parity with career-match-quiz's `openDetail`:
the defaults draw the same facts, Try, Similar and source line in the same order, with the quiz's own parts going in
`afterDoes` and `afterFacts` as the doc says, so the quiz can move with what is written, apart from the gaps in N3.
Exceptions are S3, N1, N2, N3.

Data: careers.json loads through the `"json:careers"` token as a literal (no runtime validation; none needed with
this file). Checked in Python: 83 careers, all 14 cluster keys valid, every career has `edu`, `outlook`, `ooh`,
`oohTitle`, `level`; every `level` agrees with `EDU_LEVEL[edu]` where edu is a category, and the 7 "See How to Become
One" careers carry `eduNote` and a level that fits the note; every outlook parses (28 much faster, 19 faster, 19 as
fast, 5 slower, 7 little or no change, 5 decline; no sign/word mismatch); only musician and actor are hourly-only;
top pay $244,180, under the $250,000 bar scale.

In the page (one scripted pass over all 14 ladders and all 83 sheets, `bad: []`): every career sits in the column of
`Careers.level`, each bar's width is pay / $250,000 within 0.06 points, hourly-only careers get no bar, every column
count matches the cluster, "Ways in at N of 5 levels" on the board and in the panel both match the columns used
(mfg 3, ag 4, arts 3, build 3, digital 2, edu 3, energy 3, fin 1, health 4, hosp 3, mgmt 1, mkt 2, public 5,
trans 3), each cluster card says its count, and every sheet shows "Median pay, 2025", its `edu` wording, its eduNote
where present, "Job outlook, 2025-35" with the right percent and word, and a Handbook link equal to `ooh`.
`__tool.check()`: 37 hotspots, 83 careers, no duplicates or misses, trail counts 4, 3, 2, 2, 3.

## Findings

### Should fix

**S1. Trails: focus is lost when Next or Back disables itself.** general. `src.html` drawPanel trails block
(`$('next').disabled = ...`, `$('back').disabled = ...`). Keyboard: focus Next, press Enter to the last stop, and
`document.activeElement` is `<body>` (k5_trail_next_end); Back to stop 1 does the same (k5b). The voice run v3 also
ended on body. A keyboard student has to Tab from the top again. BR1 lesson "focus is kept when controls rebuild":
move focus to Open career (or Back) when Next disables, and to Next when Back disables, with `preventScroll`.

**S2. Esc on the Start over confirm drops focus.** general. `src.html` window keydown, `if (state.confirm) {...}`.
Focus on No (where Start over puts it), Esc hides the confirm box with focus inside it and focus falls to `<body>`
(k4_confirm_esc). The No button already does it right (`$('startOver').focus(...)`); Esc should do the same.

**S3. The career sheet ignores Esc after a click on its text.** family:careers. `kit/careers.js:179` listens for
keydown on the overlay only. Click any non-focusable text in the sheet (the "what they do" line), focus moves to
`<body>`, and Esc does nothing (k3_esc_after_text_click: sheet still open), while the hint says "Press Close, or
Esc, to go back to the fair" and the doc promises "Esc and the backdrop close it". Fix in the engine for every
sibling: listen on `document` while open (and still stop propagation), or give the box `tabindex="-1"` and keep
focus in it.

**S4. Read speaks "Press the ✕ to close the card."** general. `src.html` hintText, the card branch. Read speaks
the hint, and a voice reads the symbol ("multiplication x" or nothing). STANDARDS: nothing a voice would misread.
Name the control in words that are on it, for example "Tap Close card" with a visible "Close" beside the ✕ as the
sheet has (`closeLabel`), or "the X button".

**S5. lanternHow plays in Trails and Clusters, where it doesn't fit the strip.** general. `src.html` careerOpened,
`V.how('lanternHow', {valid: ...})`. Fresh page, Trails, Kettle corn, Open career: "That lantern is a career
cluster. Find all fourteen." is spoken (v7 log and frame v7_lantern_in_trails.png) while the strip shows this
trail's lanterns and "Trail: 1 of 4", and the sheet covers it. Add `state.mode === 'festival'` to its `valid`
(dropped unmarked, it comes back on the first lantern lit in Festival).

**S6. "People doing it" misleads for mostly self-employed jobs.** family:careers. `kit/careers.js:65-66`
(`FACTS.jobs`). Farmer or Rancher shows "6,500 jobs in the US (wage and salary)" (frame v7_lantern_in_trails.png);
the OEWS wage-and-salary count leaves out the self-employed farmers who are most of the job, and the
"mostly self-employed" note shows only when `jobs` is null. BR1 lesson "honest numbers": a number that misleads
when its assumption doesn't hold. Give the data a self-employed flag (or the Handbook's employment figure) and say
it on the sheet for those careers (farmer at least; check writer, photographer, actor, musician, stylist, realtor).
The live quiz shows the same number, so this belongs in the engine and the builder.

### Polish

**P1. Where? by keyboard leaves the student far from the circled marker.** general. `src.html` where(). After
Enter on a Where? button, focus stays on it (k7); the circled marker can be 30 or more Tabs away (markers come
after the panel). Move focus to the target marker with `preventScroll` (it already pans), so Enter opens it.

**P2. A place opened from List returns focus to the stage, not the list.** general. `src.html` closeCard
(`$('mk-' + id).focus`). List, Tab to a place, Enter, Esc: focus lands on `#mk-ridge` in the stage (k8), so a
keyboard or screen-reader student loses their place in the list that exists for them. Return focus to the list
item when the card was opened from List (the spec's "focus returns to the marker" fits the stage path).

**P3. The card's "✓ met" doesn't update until it is reopened.** general. `src.html` careerOpened doesn't redraw
the open card; meet the Welder, close the sheet, and the Ferris wheel card still shows no "✓ met" beside Welder.
Redraw the card's job buttons (keeping focus on the same one).

**P4. At 375 the ladder scrolls inside a short box.** general. Stack layout: the board lives in the stage height
(about 340 px at 375x812), so the Health ladder shows about one career at a time inside a nested scroller under
the lanterns (h375_ladder.png). In stack mode let the board take its natural height (the page scrolls) or hide the
lantern strip in Clusters.

**P5. The bar scale is below the fold.** general. At 1366x768 the line "Bars show median yearly pay ... $0 to
$250,000" sits under the ladder, below the fold for Health and Arts (s1366_ladder_health.png), so the bars are read
without their scale. Put it above the ladder (under the heading).

### Nits

**N1.** family:careers. `kit/careers.js:183-184`: the Tab-wrap `focus()` calls don't pass `preventScroll`, while
the doc says focus moves "all with preventScroll".

**N2.** family:careers. `kit/careers.js:21`: `jobsText` uses `toLocaleString()` with no locale for counts under
10,000 (farmer 6,500, wind tech 9,980), so a non-US browser shows "6.500"; `money()` pins `'en-US'`.

**N3.** family:careers. docs/families/careers.md doesn't say: the sheet uses fixed ids `cr-title` and `cr-close`
(one sheet per page); the Tab trap only covers `button, a[href]`, so a block with an input or select falls out of
it; facts go to one column under 640 px; careers.json here has a top-level `handbook` object. A sibling moving onto
the engine should know these.

**N4.** general. `src.html` HOT order: `screen` (x 1236) comes before `theater` (x 1190), so Tab goes right then
left there; the spec says left to right.

**N5.** general. The minimap is a pointer target 16 px tall (12 px compact). It is an extra (drag, arrows and keys
pan too) and `aria-hidden`, so not a blocker, but it is under 44 px.

**N6.** general. The privacy line says "Your lanterns are saved"; the key also stores the careers and places
opened. "Your lanterns and the places you opened are saved..." would be exact.

**N7.** general. Clusters, then a cluster tap within 0.3 s: welcomeClusters ("Tap a cluster to see its ways in")
keeps playing over the open ladder (v5g). It started in time, so this is only a nit.

## Access

- Keyboard: Tab order header, panel, then markers left to right (k1); focusing a far marker pans it into view with
  `scrollY` 0 (k1b); Enter opens the card with focus on its first job, Enter opens the sheet with focus on Close, Esc
  closes the sheet back to the job and Esc closes the card back to the marker (k2, k2c); arrow keys pan (k9);
  Clusters: Enter on a cluster focuses its first career, All clusters returns focus to that cluster (k6); See it
  lands on the card's first job in Festival (k6b); sheet close from the ladder returns to the career (k6c); Similar
  careers then Close returns to the card's job (k10); Yes, start over focuses List. Exceptions S1, S2, S3, P1, P2.
- Visible focus from the kit; markers scale on `:focus-visible` and show their name label.
- Targets: every control 44 px or more at every size (audit, plus `--cr-target: 44px` for Similar), except N5.
- Color never alone: lit lanterns carry a ✓, opened markers a ✓, outlook an arrow plus percent plus word, cluster
  dots always beside the cluster name, trail stops numbered.
- Motion, Sound, Read: covered under Contract and the voice check.

## Saving and Clear

Open Welder and Cybersecurity Analyst, new tab: 2 lit, 2 opened, 2 seen, "Lanterns lit: 2 of 14", 2 lit lanterns,
2 ✓ markers (sv1, sv2). Start over, Yes: storage `{"lit":[],"opened":[],"seen":[],"allDone":false}`, 0 lit, focus
on List; a new tab starts at 0 (sv3). Corrupt JSON in the key: loads clean at 0 with the welcome hint (sv4, sv5).
All storage in try/catch.

## Lines

`__tool.allLines()` returns the 9 lines of voice/lines.json, the same strings in the same order (compared exactly in
Python), and both match the spec's Voice section word for word (trailEnd as two, three, four). How lines: the three
welcomes, panHow, lanternHow; event lines: allLit, trailEnd2-4 (the `EVENTS` set). Each spoken line checked against
its frame: all fit except S5 (lanternHow in Trails) and N7.

## Standard voice check

drive.py, held clicks (0.12 s), Sound on, Motion on, 1366x768, gaps 4 to 5 s for repeats and 0.2 to 0.25 s for
stale; logs from `__tool.vlog`.

| line | kind | run | expected | spoken |
|---|---|---|---|---|
| welcomeFestival | welcome | v1: 5 hotspots opened and closed | 1 | 1 |
| panHow | how | v1: 5 card closes | 1 | 1 (4 silent, heard) |
| lanternHow | how | v2: 5 lanterns from 5 clusters | 1 | 1 |
| trailEnd2 | event | v3: Your ticket end reached 5 times (Back, Next) | 5 | 5 |
| allLit | event | v8: all 14 lit, Start over, all 14 again | 2 | 2 |
| welcomeTrails | welcome | v3, v5b | 1 | 1 |
| welcomeClusters | welcome | v4, v5g | 1 | 1 |
| trailEnd2 (stale) | event | v4, v4b: end reached then Back or a new trail at 0.2 s | 0 | 0 (dropped) |

- Stale: v4 (ankle trail to its end, Back, Kettle corn, Clusters, Festival at 0.2 s): trailEnd dropped, each
  welcome starts on its own mode and the previous one is cut by the mode change. v4b: trail end, new trail at 0.25 s:
  trailEnd dropped. No line plays after its moment, apart from N7.
- First tap: a marker gets the welcome about 0.17 s after the tap (v5a); a mode button gets only its own welcome
  (v5b); Read speaks the hint only (v5c); Sound says nothing, and Sound on 2 s later brings the skipped welcome once
  (v5d); a first Tab gets the welcome (v5e); a first Where? gets the Festival welcome while the hint names the
  circled marker (v5f; the welcome still fits).
- Read: Read during the welcome stops it and speaks the hint; Read with Sound off speaks the hint; the mode change
  after it was not held up (v6). The audit's five clicks 2 s apart were clean on every control that speaks.
- Order: spoken lines follow the actions in every log.

## Layout

Frames looked at (scratch `frames/`, `vframes/`, `kframes/`, `audit/`): 680x425 default, card, sheet, trail end,
Clusters, ladder, List; 800x500 card and sheet; 1000x625 default, ladder, trail end; 1280x720 card; 1366x768
default, sheet, sheet scrolled, Health and Arts ladders, Clusters, trail end, Where?, confirm, all lit; 1920x1080
default and ladder; 760 wide default, card, ladder; 375x812 (`drive.py --host`) default, card, sheet, trail end,
Clusters, Health ladder, List, mid-town. No sideways scroll, no clipped hint, no overlapping labels. At 680x425 the
lanterns are dots with "0 of 14 lit", the header fits one row, Where? appears, the trail picker becomes a select.
At 375 the card and sheet are full-width bottom sheets. Findings: P4, P5.

## Audit pilot

`python scripts/audit_tool.py career-cluster-explorer <scratch>/audit --port 9960`: 93 leads.

- Confirmed: Motion off clean; no console errors; no focus taken on load; the Where? buttons below the fold at 760
  and 375 (true, but they are occasional controls, not the main ones, so no finding); a marker under the ▶ pan button
  at some pans (true, panning fixes it); the five-clicks voice pass agrees with my counts.
- Wrong: every overlap between a marker and a panel control or the privacy line, at every size (the markers are
  clipped by `#town`'s `overflow: hidden`; the audit measures unclipped boxes); "focus lost" on restrooms, first aid,
  radio and sponsor (those markers are off-screen under the panel, so its click hit the panel, not the marker; braids
  "ok" was really a Where? button); the 375 marker-on-marker overlaps (44 px round buttons with centres at least
  44.6 px apart, so the hit areas don't meet). The "others moved" counts after Where? and near-edge markers are the
  pan, expected.
- Missed: everything past one click: focus lost when Next and Back disable at trail ends (S1) and on Esc in the
  confirm (S2); Esc not closing the sheet after a click on its text (S3); the ✕ in the hint Read speaks (S4);
  lanternHow in Trails (S5); the self-employed job count (S6); and the keyboard paths (P1, P2), the stale card badge
  (P3), the 375 ladder (P4) and the engine and doc checks. Suggestion: clip each control's box by its overflow
  ancestors and skip controls outside the visible part.
