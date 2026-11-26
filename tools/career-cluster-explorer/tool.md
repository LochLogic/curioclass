# Career Cluster Explorer: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 3 (general 2, family 1), should fix 12 (general 8, family 4), polish accepted 16

### career-cluster-explorer: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C), refine/sensitivity.md (SE, CHANGES).
Read them for frames and detail. Facts held: Teaching checked 23 careers against the live Handbook pages (edu, outlook
and pay 23 of 23, all 7 Handbook quotes word for word) and recomputed all 81 bar widths and the 14 cluster counts;
Craft found kit/careers.js matches docs/families/careers.md apart from the items below. "family" = family:careers
(kit/careers.js, scripts/careers_data.py, careers.json).

#### Blockers
1. **"Ways in at N of 5 levels" reads as the whole cluster** (T-B1; general). The count covers only this tool's 83
   careers, so Financial Services and Management read "1 of 5" (Bachelor's only), against the spec's own claim that
   every cluster has ways in at every level, and notes question 3 steers the class to "finance needs a degree". Do both:
   (a) add real Handbook careers so each cluster has ways in at every level the Handbook supports (same edition and
   fields as the rest, each checked on its Handbook page and added in scripts/careers_data.py; sources.md updated), and
   (b) label what is counted ("Careers in this tool: N of 5 levels") wherever a column stays empty, with a line that the
   real cluster has more. Reword notes question 3 so it doesn't lead to a false conclusion.
2. **Two careers in the wrong cluster** (T-B2; family). Advance CTE 2024: Hairstylist belongs in Healthcare and Human
   Services (Personal Care Services), Real Estate Agent in Financial Services (Real Estate). Fix in
   scripts/careers_data.py and rebuild careers.json; update counts, ladders and any line that names them.
3. **A marker tapped near the edge of the view opens nothing** (P-B1; general). src.html:683: the press focuses the
   marker, focus starts a 420 ms pan and the marker slides out from under the pointer before release. In the 680x425
   preview the edge bands cover about half the town. Don't pan on a pointer focus (pan only for keyboard focus, or after
   the card opens); nothing moves under the pointer.

#### Should fix
4. **Fourteen ladder taps light every lantern** (T-S1; general, BR1 cheap solve). Only careers opened from the festival
   (card, List, trail stop) light lanterns; ladder and Similar opens show the sheet without lighting it, and the sheet's
   lantern line says so honestly for each route. Where? stays as a help (T-P2: it may stop listing all 14 from the first
   screen, as the builder judges).
5. **"People doing it" undercounts self-employed jobs** (T-S2, C-S6; family, BR1 honest numbers). Farmer 6,500 vs the
   linked Handbook's 788,700. Use the Handbook's "Number of jobs, 2025" (same edition as edu and outlook), in the engine
   and the data, and say on the sheet where the number comes from.
6. **The psychologist sheet contradicts itself** (T-S3; family). Path: "A master's or doctoral degree in psychology
   (clinical psychologists need a doctorate)." In scripts/careers_data.py.
7. **The 14 clusters are named, never explained** (T-S4; general, rule 2). One plain line per cluster from Advance CTE's
   "The Cluster Defined", under the ladder heading and on the sheet's lit line; add the page to the spec's Sources.
8. **allLit is lost if the 14th lantern lights during the first-tap welcome** (P-S1; general). It never appears in the
   log and allDone is saved, so it never comes back (Done when 3 and 9). Queue it so it plays after the welcome.
9. **Focus drops at a trail's ends** (P-S2, C-S1; general, BR1 lesson). Next at the last stop and Back at the first
   disable themselves with focus; use aria-disabled or move focus to the next sensible control.
10. **Cluster names clipped mid-word in the grid at 375** (P-S3; general). "Educati", "Manufa", "Constru"; wrap or
    shorten, never cut.
11. **The lantern line is dropped or plays in the wrong mode** (P-S4, C-S5; general). lanternHow is dropped as "newer"
    when panHow queues, so a fast student hears it only on the second lantern; and it plays in Trails and Clusters,
    where the strip shows something else. Queue it as a sequence with panHow, and only where the lanterns show.
12. **Esc on the Start over confirm drops focus** (C-S2; general). Return focus as No does.
13. **The career sheet ignores Esc after a click on its text** (C-S3; family). kit/careers.js:179 listens on the
    overlay only; listen on the sheet (or document) while it is open. Document it.
14. **Read says "Press the ✕"** (C-S4; general). Name the control in words ("Press Close").
15. **People emoji gender jobs unevenly** (SE1; family). In scripts/careers_data.py: Family Doctor 🧑‍⚕️, Chef 🧑‍🍳,
    Hairstylist ✂️ (lines 72, 82, 87 per SE), then rebuild careers.json.

#### Polish accepted
16. The sheet's big education fact in plain grade 6-8 words; the Handbook phrase ("See How to Become One",
    "Postsecondary nondegree award") goes underneath (T-P1).
17. Say when the sheet's pay is for a narrower job than the linked Handbook profile (T-P4).
18. ATC and pilot path lines read cleanly beside their Handbook entries (T-N1).
19. The police figure's head uses the scene's lavender (#c9c3ea) as a stylized silhouette (SE2).
20. Fashion Designer 🧵; Musician "places of worship"; Hotel Manager "Plan a pretend weekend trip and compare three
    places to stay online." (SE3-5).
21. The trail result is in view at 375 and 760 (P-P1).
22. The Ways in ladder isn't a small scroll box at 680x425 and 375 (P-P2, C-P4).
23. Lanterns larger for a projector at 1920 (P-P3).
24. At 1000x625 the Still dark list shows (P-P4).
25. The lantern pop and shimmer show after the sheet closes, not under it (P-P5; family).
26. "Stuck? Tap Where?." punctuation (P-P6); the trail stop header doesn't wrap at 1366 (P-P7).
27. Where? by keyboard puts focus on the circled marker (C-P1).
28. A place opened from List returns focus to the list (C-P2).
29. The card's "✓ met" updates without reopening (C-P3).
30. The bar scale line is in view with the bars (C-P5).
31. docs/families/careers.md documents the fixed ids `cr-title` and `cr-close` and the other gaps in C-N3, and the
    Tab-wrap focus passes preventScroll (C-N1).
32. The privacy line says what is saved (lanterns, careers and places met) (C-N6). Other nits as the builder judges.

#### Spec open questions (not for the builder)
- A guess-the-cluster moment before a job's cluster shows (T-P3).

#### Settled calls
- Flight Attendant and PR placements stay; mark them unconfirmed in sources.md (T-N2).
- The braids booth, the crosswalk officer and the help booth wording stay (SE: checked and fine).
- career-match-quiz keeps its own data copy for now; the fixes in items 2, 5, 6 and 15 reach it when it moves onto
  kit/careers.js (a board item, not for this builder).

#### Exit check, round 1

Cold check, 2026-10-28, against REFINE.md (exit check), STANDARDS.md, BASELINE.md and the BR1 lessons in BUILD.md.
Draft bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py career-cluster-explorer`: 196 KB, clean. Driven with
scripts/drive.py, held clicks (0.12 s), Sound and Motion on unless named; frames and logs in the exit agent's scratch
folder (out/sizes, out/n375, out/voice, out/b, out/compat). Every frame named below was looked at.

##### Items
1. PASS. Ladder line "Careers in this tool: ways in at 3 of 5 levels. This tool shows 5 of this cluster's careers; the
   real cluster has many more..." (fin, read from the DOM), empty columns read "None in this tool (the real cluster may
   have some)", the panel says "careers in this tool: ways in at N of 5 levels"; notes question 3 now asks what jobs
   would fill Hospitality's empty columns. Part (a) is partial: 10 careers added, but Hospitality, Management and
   Marketing still show 2 of 5 here (honestly labeled, so not open; see Left open).
2. PASS. stylist in health, realtor in fin (careers.json); n375-sheet shows Hairstylist, Healthcare and Human
   Services; ladder-760x900 lists Hairstylist under Certificate or some college.
3. PASS. Held press on a marker in the edge bands at 680x425 (ferris right, stage left, bank right, clinic left) and
   gate at 1366x768: the card opened every time (e1 to e5); the pan moves only after the card opens.
4. PASS. A ladder tap (i4) and Similar careers (i4b) leave the lanterns unlit and the sheet says "lantern: not lit yet.
   Meet this job at the festival to light it."; List, card, job lights it (i4c).
5. PASS. "People doing it" uses oohJobs: Psychologist 209,000, "counting people who work for themselves. Handbook count
   for all Psychologists"; Farmer's oohJobs 788,700 matches the Handbook.
6. PASS. Path: "A master's or doctoral degree in psychology (clinical psychologists need a doctorate)."; the eduNote
   matches the Handbook's Education sentence word for word.
7. PASS. The DEF line sits under each ladder heading and on the sheet's lantern line; checked against the careertech.org
   cluster pages (health, fin, mgmt, edu, mkt, trans, build, energy); the spec's Sources names the pages.
8. PASS. v6: 13 lit, the first tap opens the ridge, Wind Turbine Technician lights the 14th during the welcome; log:
   welcomeFestival spoken at 1385 ms, allLit spoken at 6514 ms (after the welcome); allDone true.
9. PASS. Held Next to the last stop: focus on Open career (i9); Back at the first stop: focus on Next (i9b); by keyboard
   too (i9c).
10. PASS. n375-grid: Manufacturing, Construction, Education and the rest whole; no clipping found by measure.
11. PASS. v7 (0.6 s gaps): lanternHow spoken at 6549 ms, then panHow at 10685 ms, in order; v7b: first lantern lit at a
    trail stop, no lanternHow in Trails; v3 (0.2 s gaps): nothing stale played.
12. PASS. Start over, then Esc: confirm closed, focus on Start over (i12).
13. PASS. Held click on the sheet's text, then Esc: the sheet closed, focus back on the job (i13).
14. PASS. Hint while a sheet is open: "Press Close, or Esc, to go back to the fair."
15. PASS. Family Doctor 🧑‍⚕️, Chef 🧑‍🍳, Hairstylist ✂️.
16. PASS. "A master's degree or more" in big type, the Handbook phrase and eduNote underneath (sheet-1366x768).
17. PASS. "The Handbook page covers a larger group, Psychologists: $99,110 a year." (Hairstylist: Barbers,
    Hairstylists, and Cosmetologists, $35,880).
18. PASS. The ATC path and the pilot eduNote read cleanly beside their Handbook entries.
19. PASS. Police head fill #c9c3ea (src.html line 693).
20. PASS. Fashion Designer 🧵; Musician "places of worship"; Hotel Manager's Try it now as written.
21. PASS. Trail result in view at 760x900 and 375 (trailend-760x900, n375-trailend).
22. PASS. At 375 the ladder is part of the page scroll (page 1808 px); at 680x425 the board fills the stage height.
23. PASS. 1920x1080: lanterns "big", labels 14.5 px.
24. PASS. 1000x625: the Still dark list shows with 13 Where? buttons (fest-1000x625).
25. PASS. Lantern pop: no pop while the sheet is open, pop on close (i25).
26. FAIL (polish). "Stuck? Tap Where?" is fixed; the trail stop header still wraps at 1366x768 ("BEHIND THE KETTLE
    CORN: / STOP 5 OF 5", trailend-1366x768).
27. PASS. Where? by keyboard puts focus on the circled marker (mk-ferris); Enter opens it (i27, i27b).
28. PASS. A place opened from List, then Esc: focus back on the list item (i28).
29. PASS. "✓ met" appears on the open card without reopening it (i29).
30. PASS. The scale line sits right above the bars at every size (ladder frames).
31. PASS. careers.md documents cr-title and cr-close; the Tab wrap uses preventScroll.
32. PASS. "Your lanterns and the careers and places you opened are saved in this browser on this device only."
Settled calls: Flight Attendant and PR are marked unconfirmed in sources.md (PASS).

##### Facts checked
Live Handbook pages (WebFetch), 14 careers: the 10 added (Administrative Assistant, Retail Sales Worker, Computer
Research Scientist, Childcare Worker, Teacher Assistant, Home Health Aide, Bookkeeper, Warehouse Worker, Drafter,
Environmental Technician) plus Hairstylist, Real Estate Agent, Farmer and Psychologist. Entry-level education, outlook,
number of jobs 2025 and the page's median pay: 14 of 14 match (all the 2025-35 edition). Hairstylist's and Real
Estate Agent's job pay ($35,790, $52,830) match the narrower medians on the Handbook's Pay tab. The psychologist
eduNote is word for word. Clusters (careertech.org, 2024 framework): all 14 placements fit a named sub-cluster
(Personal Care Services; Real Estate; Behavioral and Mental Health; Early Childhood Development; Learner Support;
Retail and Customer Experience; Purchasing and Warehousing; Architecture and Civil Engineering; Environmental
Protection; Accounting; Leadership and Operations, "administrative support"; Agriculture). Advance CTE's pages name no
occupations, so these are judged by sub-cluster.
Recomputed from careers.json: 93 careers, each in exactly one hotspot; cluster counts (4 4 11 8 6 7 7 5 13 5 4 4 7 8)
equal the grid; every ladder column count equals the DOM; all 93 bar widths equal min(100, pay / 2500) percent
(musician and actor hourly, no bar); levels used per cluster equal the ways-in lines; trail counts 4, 3, 2, 2, 3.

Engine: kit/careers.js matches docs/families/careers.md line by line (data fields, helpers, FACTS wording, sheet
options, Esc read on document in the capture phase, Tab wrap, fixed ids, sizes). Backward compatible:
Careers.sheet({data}) on career-match-quiz's own careers.json (scratch copy) draws Typical pay, Training, People doing
it and the quiz's source line for 83 of 83, with the same pay and job text as the quiz's openDetail; on the explorer's
data (83 with Job Zones) it runs with no errors. A scratch copy of career-match-quiz bundles and loads with no console
errors; its own files were not touched.

##### Regressions looked for
Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 (drive.py --host): Festival,
card, sheet, trail end, Clusters grid and ladder. No horizontal scroll, no button under 44 px, markers 44 px or more,
the hint never clipped (at 760x900 the Clusters board is page scroll by design). Motion off: no animations; none
infinite with Motion on either. Saving survives a new tab; Start over clears storage. Focus kept on rebuilds (Where?,
List, trail ends, the card's ✓ met). allLines() equals voice/lines.json word for word (9 of 9). No console errors in any
shot (the only log was the iframe host's favicon 404), no resource requests, no fetch or XHR in the bundle, 196 KB.

Voice (held clicks, each action five times in a row):

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeFestival | how | 1 | 1 |
| lanternHow | how | 1 | 1 |
| panHow | how | 1, then silent | 1 (silent x4) |
| welcomeTrails | how | 1 | 1 |
| trailEnd4 | event | 5 | 5 |
| trailEnd2, trailEnd3 | event | 1 each | 1 each |
| allLit | event | 1 | 1 |
| welcomeClusters | how | 1 | 1 |

First tap: the stage, a marker and a key get the welcome within 25 ms; a mode button gets only its welcome; Read speaks
the hint only; Sound says nothing and Sound on brings the skipped welcome once. Read during the welcome speaks the hint,
also with Sound off; a mode change right after Read starts its welcome at once. Stale: fast taps then a mode switch
drop lanternHow, panHow and trailEnd4 (hush, chain, newer); nothing played after its moment. Order follows the actions.

##### Gate
1. Done when 1 to 9 pass (check(): 93 careers, no duplicate or missing; Handbook spot-checks; lanterns, Where?, trails,
   ladders, keyboard, sizes and voice as above).
2. CTE Career Clusters is taught by what a solo student does: meeting jobs to light all 14 lanterns, each sheet's
   cluster line and definition, the trails and the ladders.
3. The defaults work for a solo student (Festival with its hint, Where?, List).
4. Sensitivity items applied (emoji, police head, Fashion Designer, Musician, Hotel Manager).
5. No blocker or should-fix open.
6. Bundle clean, 196 KB, no console errors, no network requests.
7. Voice counts right.

##### New findings
- polish (general): Where? for Energy never suggests the barn (Solar Installer). where() indexes a pool that changes
  with the last pick, so it cycles ridge, river, weather (dw4). "Never the same twice running" still holds.
- nit (general): on a slow first meeting lanternHow plays while the sheet covers the lantern strip (v1, 6608 ms, sheet
  open); the sheet's own lamp line is in view, so it still reads.
- nit (general): at 680x425 the Ferris wheel card's fourth job runs to the stage edge (card-680x425).

##### Left open (polish, not blocking)
- Item 26, second half: the trail stop header wraps at 1366x768.
- Item 1(a), partial: Hospitality, Management and Marketing have careers at 2 of 5 levels here (labeled as this tool's
  careers only).
- The three new findings above.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: career-cluster-explorer

Cold Craft lens (REFINE.md), round 1, 2026-10-28. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py
career-cluster-explorer`, 175 KB (182,033 bytes). Placeholder art and the browser voice not reported.

Counts: blockers 0, should fix 6 (general 4, family 2), polish 5 (general 5), nits 7 (general 4, family 3)

#### Contract (all pass)

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

#### Engine against the family doc (kit/careers.js vs docs/families/careers.md)

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

#### Findings

##### Should fix

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

##### Polish

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

##### Nits

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

#### Access

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

#### Saving and Clear

Open Welder and Cybersecurity Analyst, new tab: 2 lit, 2 opened, 2 seen, "Lanterns lit: 2 of 14", 2 lit lanterns,
2 ✓ markers (sv1, sv2). Start over, Yes: storage `{"lit":[],"opened":[],"seen":[],"allDone":false}`, 0 lit, focus
on List; a new tab starts at 0 (sv3). Corrupt JSON in the key: loads clean at 0 with the welcome hint (sv4, sv5).
All storage in try/catch.

#### Lines

`__tool.allLines()` returns the 9 lines of voice/lines.json, the same strings in the same order (compared exactly in
Python), and both match the spec's Voice section word for word (trailEnd as two, three, four). How lines: the three
welcomes, panHow, lanternHow; event lines: allLit, trailEnd2-4 (the `EVENTS` set). Each spoken line checked against
its frame: all fit except S5 (lanternHow in Trails) and N7.

#### Standard voice check

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

#### Layout

Frames looked at (scratch `frames/`, `vframes/`, `kframes/`, `audit/`): 680x425 default, card, sheet, trail end,
Clusters, ladder, List; 800x500 card and sheet; 1000x625 default, ladder, trail end; 1280x720 card; 1366x768
default, sheet, sheet scrolled, Health and Arts ladders, Clusters, trail end, Where?, confirm, all lit; 1920x1080
default and ladder; 760 wide default, card, ladder; 375x812 (`drive.py --host`) default, card, sheet, trail end,
Clusters, Health ladder, List, mid-town. No sideways scroll, no clipped hint, no overlapping labels. At 680x425 the
lanterns are dots with "0 of 14 lit", the header fits one row, Where? appears, the trail picker becomes a select.
At 375 the card and sheet are full-width bottom sheets. Findings: P4, P5.

#### Audit pilot

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

<!-- end part -->

<!-- part: refine/final-sensitivity.md -->

PASS

### Final look sensitivity review: career-cluster-explorer

Fresh cold review, 2026-10-29, against BASELINE.md (rules 4, 5, 6), STANDARDS.md and REFINE.md (Sensitivity agent,
Final look). Read refine/sensitivity.md, spec.md, handoff.md, notes.md, src.html, careers.json (all 93 careers, every
does / path / try line), voice/lines.json and voice/local.json. Drove the bundle (career-cluster-explorer.html) with
scripts/drive.py on Chrome port 9251 at 1366x768 and 1920x1080: cards for braids, help, police, kids, clinic, food,
hardware and truck; sheets for doctor, chef, stylist, home-aide, childcare, police, retail, mover, cook and
social-worker; ladders for health, edu, hosp and public; the full town. Frames and text log in
S:/CurioClass-codex-scratch/final/career-cluster-explorer-sens/ (out/, run1.txt). No console errors in 23 shots. Chrome
closed after the run (no process left on the profile).

Counts: blockers 0, should fix 0, polish 0, nit 1.

#### Earlier fixes: all still fixed

Checked in careers.json, src.html and the bundle text (old strings count 0, new strings count 1), and on screen:

1. People emoji: Family Doctor 🧑‍⚕️, Chef 🧑‍🍳, Hairstylist ✂️. The clinic and food truck cards (out/card-clinic.png,
   out/card-food.png) and the health ladder (out/ladder-health.png) draw the gender-neutral figures in default yellow.
   No 👩‍⚕️, 👨‍🍳 or 💇 anywhere in the bundle.
2. Police figure head is `#c9c3ea` (src.html line 693, and the bundle). It reads as a lavender silhouette like the rest
   of the town (out/card-police.png, out/scene-full.png).
3. Fashion Designer 🧵 (no 👗 in the bundle).
4. Musician "places of worship" (no "churches").
5. Hotel Manager "Plan a pretend weekend trip and compare three places to stay online." (no "family trip").

#### New since that review: checked, fine

- **The 10 careers added in polish round 1** (Administrative Assistant, Retail Sales Worker, Computer Research
  Scientist, Childcare Worker, Teacher Assistant, Home Health Aide, Bookkeeper, Warehouse Worker, Drafter,
  Environmental Technician) were not in the first review. Each does line is plain and respectful ("Helps older adults
  and people with disabilities with daily care in their homes"; "Helps customers find what they need..."). Paths say
  what the Handbook says without ranking words ("no diploma is needed to start"). Emoji are all objects (📎 🛍️ 🧮 🧩 ✏️
  🏠 📒 🏷️ 📏 💧). Childcare's try line keeps a grown-up nearby.
- **Low-pay care and service jobs** (home aide, childcare, teacher assistant, hairstylist, cook, retail, warehouse) sit
  in the "No degree needed" or "Certificate or some college" columns at $35k to $37k. That is the BLS fact, shown on the
  same $0 to $250,000 scale as every job, with no "low" or "entry" label and the "many also have other ways in" key. The
  health ladder puts Home Health Aide beside Dental Hygienist ($98,100, associate's) and Paramedic, so a column is not a
  class marker. Rule 5: plain, with the human side. Fine.
- **Which jobs sit together:** Home Health Aide joined the community help booth (counselor, social worker,
  psychologist); it is human services, and the booth line stays non-clinical. Hairstylist moved to Healthcare and Human
  Services (Advance CTE 2024, Personal Care Services, per sources.md); the braids booth itself is unchanged and still
  ties the job to no group. The kids' corner (teacher, preschool, teacher assistant, childcare) and the clinic hold
  gender-neutral titles and object emoji, so no card casts a gender.
- **Words:** no gendered pronouns or nouns (he, she, his, her, man, woman, guy, girl, boy) in src.html or careers.json;
  no em dashes in src.html, careers.json, lines.json or the bundle. Rule 6 passes. No cultural, Native or hard-history
  content anywhere: Maple Bend and its harvest night are made up, and no line names a culture, faith or group.
- **Drawn people:** the town has one person, the crosswalk officer. The kids' corner circles are craft items on a table
  (src.html lines 659-660), the stage and field have no players drawn. No art files.
- **Voice, real clips.** All nine lines are neutral how-to and event lines; none comments on a job, a pay level or a
  choice, and "from no degree to grad school" names the ladder's columns without judging them. The Final look's Whisper
  pass matched every clip to its text. My own liveliness run (scripts/voice_liveliness.py) and a pitch contour of lines
  3, 6 and 8: deliveries are upbeat and moving (semitone SD 2.98 to 7.94). Line 3 ("All fourteen lanterns are lit...")
  has the widest range (29.6), from a celebratory rise on "One night" plus two 60 Hz breath frames that inflate the
  number; that fits a finish line. Line 4 is the flattest (2.98) and is a plain instruction. No take reads as sarcastic
  or dismissive from these readings. I judged delivery from transcript, pitch and rate, not by ear.

#### Finding

1. **nit (general)**, careers.json via scripts/careers_data.py: two try lines assume a home or a car a student may not
   have: solar "Track how much sun your house gets in a day." and auto-tech "Learn to check a car's oil and tire
   pressure." How seen: reading all 93 try lines. Better: "Track how much sun one window or yard spot gets in a day."
   and "Learn how to check a car's oil and tire pressure (a video works too)." The same kind of fix as the first
   review's Hotel Manager line; optional.

Nothing else found. The finished tool keeps every fix the first review asked for, and the recorded voice adds nothing
that reads as mocking or dismissive.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: career-cluster-explorer

Played cold from spec.md, src.html, notes.md, voice/lines.json and kit/careers.js, on the draft bundle
(`CURIO_DRAFT=1`, 175 KB). Played twice: once as a grade 6-8 student alone at home, once as a teacher projecting a
"who made this?" warm-up. All input through `scripts/drive.py` with held clicks (`hold` 0.12 s), real keys and a
jittered real drag; 375 wide through `drive.py --host`. Frames in my scratch folder `lens-cce-play/shots`.

Counts: blockers 1 (general 1, family 0), should fix 4 (general 4, family 0), polish 7, nits 4.

#### Blocker

**B1. Tapping a marker near the edge of the view does nothing (general).** `src.html:683` (marker `focus` runs
`ensureVisible`) and `:740-743`. When you press a marker, the button takes focus. If the marker is within 90 px of
either edge of the town, `ensureVisible` then starts a 420 ms pan, and the marker slides out from under the pointer
before you release, so the click never fires. The scene moves and no card opens; the student has to find the marker
again and tap a second time.
- Seen at 1366x768: `#mk-food` (x about 955 in a 1026 px town). Held click, card null, pan -56 to 385
  (`edge-1366-food.png`).
- Seen at 680x425: `#mk-weather` and `#mk-gate` (`edge-680-weather.png`, `edge-680-gate`). Card null, pan -56 to 62
  and to 102, while `#mk-bridge`, nearer the middle, opened.
- In the 680x425 preview the 90 px bands cover about 180 of the town's 410 px, so close to half the markers you can
  see fail on the first tap. That is the first thing a student does.

This is the BR1 lesson "nothing moves or rebuilds under the pointer". Better: don't pan on a pointer focus (only on
keyboard focus, `:focus-visible`), or pan after the click.

#### Should fix

**S1. allLit is lost when the 14th lantern lights during the first-tap welcome (general).** `src.html:497-501`.
- Repro: reload with 13 lit, tap the Ferris wheel, then tap Welder within about 4 s. The lantern lights and the
  panel says all 14, but the log shows only `welcomeFestival` after an 8 s wait. allLit is not spoken, dropped or
  silent (`all14b`).
- The same steps with the job tapped after the welcome ends do speak allLit (`all14-mid`, spoken at 8.5 s).
- When it happens: a student who comes back the next day with 13 lit hits exactly this.
- Spec "Done when" 3 and 9 (allLit once, event lines every time) fail in this case.
- Also, the line never comes back. `allDone` is saved as true, so no later moment replays it.

**S2. Focus falls to the page at a trail's last stop (general).** `src.html:1004`. Pressing Next onto the last stop
disables Next while it has focus, and focus drops to `body`. Seen in `t-kettle-end`, `t-bridge-end` and
`t-lights-end`, where the active element is `body` each time. A keyboard student loses their place right at the
result, and pressing Enter again does nothing. BR1 lesson "focus is kept when controls rebuild": move focus to Back
or Open career, or to the end row.

**S3. Cluster names are clipped in the Clusters grid at 375 wide (general).** `src.html:189-193` (`.cl`
`overflow:hidden`, 4 columns at 375). In `n375-clusters` (montage `m375b.png`):
- Clipped mid-word: "Manufa" (the soft hyphen is cut off), "Constru", "Educati" (Education has no break point).
- Breaks that read badly: "Hospi-", "Market-" and "Manage" on the next row.

BR1 sizes lesson: unclipped text at 375 through `--host`. Better: 2 columns of clusters when the body is `narrow`.

**S4. The lantern line, the core idea, is often lost on the first lantern, and can play in the wrong mode
(general).** `src.html:502-504`, `:836`.
- Lost: a student who opens a job, closes the sheet and closes the card within about 3 s never hears "That lantern
  is a career cluster. Find all fourteen." The welcome is still playing, and closing the card queues panHow, a newer
  how-to that replaces the queued lanternHow. The log shows `lanternHow dropped (newer)` in `startover`, `calm-card`
  and `keys-enter-esc`. It comes back only when a second lantern lights.
- Wrong mode: opening a career from Trails speaks "That lantern... Find all fourteen" (`t-open`). But in Trails the
  lantern row shows "This trail" (2 of 3), not the student's lanterns, so the line names a different thing from the
  one on screen.

Better: give lanternHow priority over panHow (queue panHow only after lanternHow is heard), and add
`state.mode === 'festival'` to its `valid`.

#### Polish

- **P1. The trail result needs scrolling on narrow screens (general).** At 375x812 the "These stage lights took 3
  clusters" row starts at y 786 (`n375-trails`). At 760x1000 it runs 940 to 1011 (`tr-end-760x1000`). In stack
  layout, put the end row above the stop box at the last stop, or scroll it into view with `preventScroll` kept for
  focus.
- **P2. The Ways in ladder is a small scroll box at 680x425 and 375 (general).**
  - 680x425: the board is 341 px tall with 1461 px of content (`c-health-680`).
  - 375 wide: 317 px with 1889 px of content, inside a page that also scrolls (`n375-ladder`).
  - A student sees one level at a time and can't compare the levels.
  - Better: shorter chips (put "See it" on the name row, not its own 44 px row), or let the page scroll at 375
    instead of the board.
- **P3. The lanterns are small for a projector (general).** At 1920x1080 the lamps are still 18x24 px with 11 px
  names across a 1580 px stage (`first-1920x1080.png`), while the scene scales up. The class can't read which
  clusters are lit. Scale the lantern row with the stage height.
- **P4. At 1000x625 the panel hides the Still dark list behind one cycling Where? button (general).** The panel is
  half empty (`first-1000x625.png`), but a student can't pick the cluster they want: Where? walks through the dark
  clusters in turn. Show the two-column list in compact when it fits, or at least when the panel is 500 px or taller.
- **P5. The lantern moment is hidden under the sheet (family:careers).** A lantern lights while the career sheet's
  backdrop covers the stage, so its pop, and the allLit shimmer, play unseen (`d-sheet.png`, `all14`). The sheet's
  "lantern: lit" line is the only sign. Better: replay the pop (or the shimmer) on the lantern when the sheet closes.
  That is the moment a student looks up.
- **P6. "Stuck? Tap Where?." (general).** `src.html:1029-1030` doubles the punctuation in compact (`compact-card`
  hint). Drop the template's period when the label ends in "?".
- **P7. The trail stop header wraps at 1366 (general).** "BEHIND THE KETTLE CORN: STOP 5 OF / 5" puts the last "5"
  on its own line (`t-kettle-end.png`). Use the short "Stop 5 of 5" form in the wide panel too, or keep "5 of 5"
  together with a non-breaking space.

#### Nits

- A marker's hover label shows cut off at the card edge ("e Ferris wheel", `d-card.png`). Hide labels while a card
  is open.
- The 56 px pan padding at both ends shows as a blank dark bar, and in Trails it is not dimmed with the rest
  (`first-1366x768.png` left edge, `t-kettle-end.png` right edge).
- At 375 wide, neighboring markers' 44 px targets overlap by 4 to 17 px (theater/help, food/first aid,
  clinic/bank). The dots themselves don't touch.
- In compact the count shows twice: "0 of 14 lit" on the stage and "Lanterns lit: 0 of 14" in the panel.

#### What worked (checked, no finding)

- **First screen at every size:** names the action ("Tap anything glowing at the fair...") with glowing markers.
  Nothing takes focus on load, no sideways scroll, no console errors in any shot.
- **Every waiting moment names the next control:** card ("Tap a job... Press the ✕"), sheet ("Press Close, or
  Esc"), confirm, Where? ("Tap its circled marker"; "Still the Ferris wheel: it's the only place..."), List, each
  trail step ("Tap Next for stop 2, or tap Open career to meet the Farmer or Rancher"), Clusters and the ladder.
- **A student who skips the reading:** tapping only markers lights nothing. After the first card the hint switches
  to "tap a job to light its lantern", so the rule teaches itself.
- **Where?:** cycles hotspots and never repeats one twice running (Health x3, Arts x5). Manufacturing, which has a
  single hotspot, says so instead of pretending to move.
- **Start over:** asks first, puts focus on No, Yes clears, and focus goes to List.
- **Saving:** lanterns survive a reload. All 14 lit shows "Every lantern is lit" with a fitting hint
  (`all14-reload.png`). The privacy line is on screen.
- **Trails:** step in order with counts 4, 3, 2, 2, 3. Markers are numbered ("3-5" for a shared hotspot), the path
  is dotted, and the end row lists the clusters. Next with no trail picked starts Kettle corn, which matches the hint.
- **Clusters:** the grid shows counts. The ladder has 5 columns at 1280 and wider and rows below 900 px, pay bars on
  one $0 to $250,000 scale, "None in this tool" for empty levels, and "Ways in at N of 5 levels" in the panel, so
  the result is visible without scrolling. See it jumps to Festival and opens the card. All clusters returns focus
  to the cluster.
- **Keyboard:** Tab goes header, panel, then markers left to right. Enter opens, Esc closes the sheet then the
  card, and focus returns to the marker. Arrow keys pan.
- **Drag pans** (jittered real drag, pan -56 to 406). The minimap follows.
- **Motion off:** no running loops, the Where? ring is static, pans jump (`calm-card`; the audit agrees).
- **Sound off:** uses nothing up. Sound on brings the skipped welcome once (`sound-off`).
- **Read:** during the welcome, stops it and speaks the current hint (`read-mid`).

#### Voice counts (held clicks)

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeFestival | how | once, on the first tap | 1 per page (every run) |
| welcomeTrails / welcomeClusters | how | once per mode entry | 1 (`t-enter`, `c-grid`) |
| panHow | how | once, then silent | 1 spoken, then silent x3 over 5 hotspots (`d-5hot`) |
| lanternHow | how | once, on the first lantern | spoken in slow runs; dropped `newer` in 3 fast runs (S4) |
| trailEnd2 | event | every arrival | 3 of 3 (`t-end-repeat`) |
| trailEnd3 / trailEnd4 | event | every arrival, dropped when stale | spoken (`t-bridge-end`, `t-kettle-end`); dropped `stale` on a trail switch and a mode switch (`t-stale`, `t-stale2`) |
| allLit | event | when the 14th lights | 1 of 2 runs; missing when lit during the welcome (S1) |

#### Frames looked at

- **First screens:** `first-680x425`, `-800x500`, `-1000x625`, `-1280x720`, `-1366x768`, `-1920x1080`,
  `-760x1000`.
- **375 wide:** `n375-first`, `-card`, `-sheet`, `-trails`, `-trails-pick`, `-clusters`, `-ladder`, `-list`
  (montages `m375a`, `m375b`).
- **Festival at 1366:** `d-card`, `d-sheet`, `d-close`, `d-close2`, `d-5hot`.
- **Where?, List and Start over:** `w-mfg1`, `w-mfg2`, `w-health3`, `w-trans`, `w-5x`, `w-then-tap`, `list`,
  `list-new`, `startover`, `startover-yes`.
- **Trails:** `t-enter`, `t-nexttrail`, `t-kettle-end`, `t-end-repeat`, `t-stale`, `t-stale2`, `t-open`,
  `t-bridge-end`, `t-lights-end`, `t-ticket-mid`, `tr-end-*` (5 sizes).
- **Clusters:** `c-grid`, `c-health`, `c-arts`, `c-digital`, `c-see`, `c-open`, `c-back`, `c-health-1280`,
  `c-health-1000`, `c-grid-680`, `c-health-680`, `c-grid-1920`, `c-arts-1920`.
- **All 14 lit:** `lit13`, `all14`, `all14-reload`, `all14b`, `all14-mid`.
- **Motion, Sound, Read, keyboard and drag:** `calm-card`, `sound-off`, `read-mid`, `keys`, `keys-enter-esc`,
  `arrow`, `drag`.
- **Compact and edge taps:** `compact-where`, `compact-card`, `edge-*`.

#### Audit pilot

**Confirmed:** at 760x900 and 375, the Where? buttons are below the fold (polish here, P4 and P1 nearby). At 375,
neighboring markers' targets overlap by a few px (nit). Motion off is clean.

**Wrong:**
- Every marker/panel overlap at 680 to 1920 (about 60 rows). Those markers sit past the town's clipped edge
  (`overflow:hidden`), so they can't be seen or hit.
- "Focus lost" on restrooms, firstaid, radio and sponsor at 1366. Those markers are off-screen behind the panel;
  the click landed on the panel.

**Partly wrong:** it marked help, food and field "ok". My held click on `#mk-food` opened no card. The audit checks
focus and movement, not whether the click did anything.

**Missed:**
- the edge-tap blocker (B1);
- allLit lost during the welcome (S1, past one click);
- focus lost at a trail's end (S2, past one click);
- clipped names in Clusters at 375 (S3, a mode the size pass doesn't open);
- lanternHow dropped as `newer` (S4);
- the ladder and the trail result needing a scroll (P1, P2);
- all feel items.

<!-- end part -->

<!-- part: refine/sensitivity.md -->

CHANGES

### Sensitivity review: career-cluster-explorer

Fresh review, 2026-10-28, done cold against BASELINE.md (rules 4, 5, 6) and STANDARDS.md. I read spec.md, src.html,
careers.json, notes.md, art/prompts.json and voice/lines.json, and checked the bundled draft in headless Chrome at
1366x768 (the crosswalk, the braids booth, the help booth and the clinic cards).

Overall: careful work. Job titles are gender neutral (Power Line Worker, Firefighter, Police Officer, Flight
Attendant). Every trail line and description uses "A ..." or singular "they", and no line says who does a job. Trades
and service work are written about with respect, and the shared pay scale makes the point well (a power line worker
with a high school diploma at $95,320 sits above most bachelor's jobs). There are no blockers. The one thing to fix is
the people emoji.

#### Blocker

None.

#### Should fix

1. **The people emoji give jobs a gender, and not evenly.** Only three careers use a person emoji. Family Doctor is a
   woman (👩‍⚕️). Chef is a man (👨‍🍳), which matches the stereotype (BLS: most head chefs are men). Hairstylist is 💇,
   which Windows (checked in the render), Apple and Google all draw as a woman, and it shows the client instead of the
   worker; that matches the stereotype too. Human Resources Specialist already uses the gender-neutral 🧑‍💼, so the
   set is inconsistent. A student scanning cards sees "the doctor is a woman, the chef is a man, the hair person is a
   woman," which is exactly the casting this tool should avoid.
   **Fix:** in `scripts/careers_data.py`, change the emoji on line 72 (doctor) `👩‍⚕️` to `🧑‍⚕️`, line 82 (chef)
   `👨‍🍳` to `🧑‍🍳`, and line 87 (stylist) `💇` to `✂️`. Rebuild `careers.json` with the builder so both
   career-cluster-explorer and career-match-quiz get the same emoji. That changes career-match-quiz's display too; it
   is the same fix there, so note it in that tool's notes. The gender-neutral person emoji render on Windows 10 1903+
   and 11, ChromeOS, iOS and Android.

#### Polish

2. **The only person drawn in the town has one fixed skin tone.** The police officer at the crosswalk (src.html line
   637) is the only human figure in the scene, and its head is filled `#d9b98a`, a light tan. It is tiny and mostly
   under the marker, but it still gives the one townsperson a race. Everything else in the scene is stylized plum and
   lavender.
   **Fix:** on line 637, change the head circle's fill from `'#d9b98a'` to `'#c9c3ea'` (the scene's lavender), so the
   figure reads as a stylized silhouette like the rest of the town. Keep the blue uniform and cap.

#### Nit

3. **Fashion Designer's 👗 shows only a dress,** while the job (its own "does" line) is "clothing, shoes and
   accessories" for everyone. **Fix:** `scripts/careers_data.py` line 38, `👗` to `🧵`.
4. **Musician names one faith:** "concerts, recordings, churches, schools and games." **Fix:** `scripts/careers_data.py`
   line 36, "churches" to "places of worship".
5. **Hotel Manager's Try it now assumes the family travels:** "Plan a family trip and compare places to stay."
   **Fix:** `scripts/careers_data.py` line 85, to "Plan a pretend weekend trip and compare three places to stay
   online."

#### Checked and fine (no change)

- **Braids booth** ("The braids and face paint booth", Hairstylist). Braid and face paint booths are ordinary at
  county fairs, the scene draws only a tent, and hair braiding is respected work across many cultures. It does not
  link the job to any group. The Try line ("Practice braids or styles with family or friends") is fine. Keep it.
- **Police figure at the crosswalk.** A crosswalk is the gentlest public-safety moment to show, and the second line
  ("someone tests evidence from a stolen bike case") is low-stakes and age-appropriate. No weapons, no arrests, no
  victims. Keep it, with polish 2 for the skin tone.
- **Help booth wording.** "The community help booth. 'Someone to talk to, and help finding help.'" It is warm and
  non-clinical, it does not stigmatize, and it does not imply the student needs help. The three descriptions (school
  counselor, social worker, psychologist) are plain and kind. The tool asks nothing personal, so it needs no crisis
  line. Keep it.
- **Pay and "which jobs need a degree."** The column is called "No degree needed," not "low" or "entry." The ladder
  goes left to right without ranking words, and every cluster uses one pay scale. The key says "many also have other
  ways in." The trades' paths name paid apprenticeships. Cook ("quickly and carefully during busy restaurant shifts")
  and the other service jobs are written about with respect. notes.md's talk question about a bachelor's-heavy cluster
  and the "Decline does not mean disappearing" prompt are balanced. "Ways in at 4 of 5 levels" is a neutral count.
- **Who does which job.** No gendered titles, no pronouns that assign a gender (the farmer "sells what they grow"),
  and no line ties a job to a culture, class or ability. Air Traffic Controller's "most start before age 31" is the
  FAA's real rule.
- **Disability.** Nothing excludes or pities anyone. The physical therapist and athletic trainer are framed around
  recovery and moving better.
- **Every other emoji** is an object, an animal or a vehicle (🔥 ⚙️ 🏭 🤖 🐾 🐕 🧪 🚜 🎨 🎬 🎸 📷 🎮 🎞️ 🛋️ ✍️ 🎭 🎥 💡 🪚 🔧 📐 🌉
  ❄️ 🚧 💻 🔐 📊 🌐 🖥️ 🍎 🧸 🧭 📚 🏅 🌬️ ☀️ 🌿 🦉 ⚡ 🌦️ 🧾 💰 🎲 🩺 💉 🦵 🦷 🚑 💊 🤝 🧠 🏥 🏈 🍳 🎉 🏨 ✈️ 📋 🗂️ 📣 🏡 🎙️ 🔎
  🚒 🚓 ⚖️ 📁 🏙️ 📞 🔬 🛫 🚚 📦 🚗 🛩️ 📡 🚀). ✍️ and 🤝 are hands in default yellow, with no skin tone set. That is fine.
- **Art prompts.** None: `assets` is empty and everything is drawn in code, so no local-model prompt draws people.
- **Voice lines.** All nine are neutral how-to and event lines.
- **Classroom-safe language and privacy** (rules 6 and 7) pass. The privacy line is on screen in the panel.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: career-cluster-explorer

Round 1, 2026-10-28. Cold lens: read spec.md, src.html, notes.md, careers.json, sources.md, handoff.md, art/prompts.json,
voice/lines.json, kit/careers.js and docs/families/careers.md; bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
career-cluster-explorer` (175 KB, clean); ran `scripts/audit_tool.py` (ports 9930-9931) and `scripts/drive.py` (port 9932)
with held clicks for the voice checks. Frames and logs are in my scratch folder (d1 to d5, audit/).

Counts: blockers 2 (general 1, family 1), should fix 4 (general 2, family 2), polish 4 (general 2, family 2), nits 2 (family 2).

#### Blockers

**B1. Clusters: "Ways in at N of 5 levels" describes the 83-career sample as if it were the whole cluster.** (general)
- Where: src.html drawBoard() line ~930 (`Ways in at ${used} of 5 levels`), drawPanel() line ~1010 (`ways in at N of 5
  levels`), notes.md "Talk about it" question 3.
- What: recomputed from careers.json: Financial Services 1 of 5 (accountant, financial advisor, actuary: all Bachelor's),
  Management and Entrepreneurship 1 of 5 (all Bachelor's), Digital Technology 2 of 5, Marketing and Sales 2 of 5; only
  Public Service and Safety reaches 5 of 5. A grade 7 student reads "Financial Services: ways in at 1 of 5 levels" and
  four "None in this tool" columns as "you need a bachelor's degree to work in finance". That is false for the real
  cluster (Advance CTE 2024 Financial Services includes Banking & Credit, Insurance and Real Estate, which have
  high-school entry jobs such as real estate agent, a Handbook "High school diploma or equivalent" career already in this
  tool). Notes question 3 ("Find one where most jobs need a bachelor's degree. What does that mean for someone who wants
  to start working right after high school?") steers the class to that wrong conclusion. The spec's own "Not like" line
  says the Clusters view "shows that every cluster has ways in at every level of training": the data contradicts it for
  13 of 14 clusters (STANDARDS, Facts: trust the computation and say so). A meter that misleads when its assumption (the
  sample covers the cluster) does not hold is a blocker (REFINE, Rounds).
- How seen: frame d1/ladder_fin.png ("Ways in at 1 of 5 levels"); the dw6 run printed all 14 counts.
- Better: either fill the empty columns with real careers from each cluster (the spec's intent; a spec and data change,
  so the integrator decides, possibly with Cory), or say plainly what is counted: "Careers in this tool: 1 of 5 levels.
  The real cluster has more ways in, like (example)." and reword notes question 3. Do not leave the bare count.

**B2. Two careers are in the wrong Advance CTE 2024 cluster.** (family:careers: the data comes from the shared
careers.json that the live career-match-quiz also bundles)
- Where: careers.json `stylist` (cluster `hosp`) and `realtor` (cluster `mkt`); shown on the festival cards, sheets,
  ladders, the lantern-lit line and the cluster counts.
- What: careertech.org (fetched 2026-10-28): Healthcare & Human Services has the sub-cluster "Personal Care Services"
  with Barbering and Cosmetology as its programs, so Hairstylist belongs in Healthcare and Human Services, not
  Hospitality, Events and Tourism (whose sub-clusters are Accommodations, Conferences & Events, Culinary & Food Services,
  Travel & Leisure). Financial Services has the sub-cluster "Real Estate" (buying, selling, leasing property), so Real
  Estate Agent belongs in Financial Services, not Marketing and Sales (Market Research, Marketing & Advertising, Retail &
  Customer Experience, Strategic Sales; real estate not mentioned). Which cluster a job belongs to is the fact this tool
  teaches.
- How seen: d1/sheet_stylist.png ("Hairstylist / Hospitality, Events and Tourism"), d2 sheet_realtor text ("Marketing
  and Sales"); the careertech.org cluster pages.
- Knock-on after the fix: counts become Hospitality 5, Health 12, Marketing 3, Finance 4; the Finance ladder becomes 2
  of 5 (realtor is High school). No trail uses either career, so the trail counts (4, 3, 2, 2, 3) stay. Where? still works
  (the braids booth and the For sale sign keep their careers). The live career-match-quiz shows the same two labels: tell
  whoever owns it.

#### Should fix

**S1. All 14 lanterns can be lit from the Clusters ladder in 14 taps, and allLit then says "One night at the fair took
every cluster."** (general)
- Where: src.html careerOpened() (line ~490) runs on every sheet open (`onOpen`), including `{from: 'ladder'}` and
  Similar careers.
- What: Clusters mode names every cluster and lists its careers, so opening the first chip of each of the 14 clusters
  lights all 14 lanterns with no finding at all. The spec's reason for lanterns ("finding a cluster means reading about a
  job in it") and the allLit line both assume the student found them at the fair. BUILD wave lesson "No meter or puzzle
  can be solved ... trying every option for free": missed.
- How seen: drive shot cheap_clusters: `{"lit":14,"allDone":true}` after one ladder tap per cluster.
- Better: only careers opened from the festival (card, List, trail stop) light lanterns; ladder and Similar opens show the
  sheet without lighting, or light only once that career's festival place has been opened. Keep the sheet's "lantern: lit"
  line honest for each route.

**S2. "People doing it" shows OEWS wage-and-salary counts that badly undercount some jobs, one tap from a Handbook page
with very different numbers.** (family:careers)
- Where: kit/careers.js FACTS.jobs ("jobs in the US (wage and salary)"); this tool's facts include `jobs`.
- What: Farmer or Rancher shows 6,500; the linked Handbook page says 788,700 jobs (67 percent self-employed). Musician
  36,180 vs 170,400 (48 percent self-employed). Real Estate Agent 193,000 vs 530,600. "Wage and salary" means nothing to a
  grade 6 to 8 student; they will read "only 6,500 farmers in the US". BUILD wave lesson "Honest numbers: a meter or
  estimate says on screen what it assumes": the assumption is stated only in jargon.
- How seen: d1/sheet_farmer.png; Handbook Quick Facts fetched for farmers, musicians and real estate.
- Better: show the Handbook's "Number of jobs, 2025" (same edition as edu and outlook; a data change), or keep OEWS and say
  it plainly: "people who work for an employer; most farmers run their own farm, so the real number is much bigger".

**S3. The psychologist sheet contradicts itself.** (family:careers)
- Where: careers.json `psychologist`: eduNote "Psychologists typically need at least a master's degree to enter the
  occupation." (verbatim on the Handbook page) and, a few lines lower, path "A doctoral degree in psychology."
- What: two different answers to "how much school?" on one sheet.
- How seen: d1/sheet_psych.png.
- Better: path "A master's or doctoral degree in psychology (clinical psychologists need a doctorate)." Fix it in
  scripts/careers_data.py so career-match-quiz gets it too.

**S4. The "14 clusters" half of the standard is named but never explained.** (general)
- Where: Clusters grid and ladder heading (drawBoard), the sheet's lantern-lit line; no Advance CTE text is used anywhere.
- What: CTE.Career Clusters is "the 14 clusters and the occupations in them". The occupations side is taught well by what
  a solo student does (meets each job at a place, sees its cluster, follows trails across clusters, compares ways in). But
  nothing says what any cluster is: a student who lights "Management and Entrepreneurship" or "Supply Chain and
  Transportation" learns only the name and 3 to 7 examples, and tool.draft.json's outcome promises "Name the 14 career
  clusters". BASELINE rule 2 asks for taught well, above the minimum.
- How seen: d1/clusters_grid text (names and counts only), d1/ladder_fin.png.
- Better (inside the spec): one plain line per cluster from Advance CTE's "The Cluster Defined" (for example Financial
  Services: "Managing money: banking, insurance, accounting, investing and real estate") under the ladder heading and on
  the sheet's lit line. Add the page to the spec's Sources.

#### Polish

**P1. The sheet's big education fact is jargon for grades 6-8.** (family:careers) Seven sheets show "See How to Become
One" in bold as the entry-level education (it reads like an instruction), and eleven show "Postsecondary nondegree award".
The exact Handbook wording must stay (spec), but add the plain column name beside it ("No degree needed", "Certificate or
some college") as the ladder's key does. Seen: d1/sheet_psych.png, d1/sheet_stylist.png.

**P2. Where? lists all 14 clusters from the first screen.** (general) A solo student can light everything by tapping 14
Where? buttons and the circled marker, never looking at the town. It is a fair scaffold and each lantern still costs a job
read, but the "find" would land better if Still dark appeared after a few lanterns or after a minute. Seen:
audit/size-1366x768.png (14 Where? buttons on load).

**P3. A predict moment (spec open question, not for the builder).** Before a job's cluster shows, let the student guess
which lantern it lights ("Which lantern will a forensic science technician light?"), with the chip's cluster label hidden
until they guess. This would teach the clusters by doing; it changes the format, so it goes to the spec's open questions.

**P4. Pay on the sheet can differ from the linked Handbook page.** (family:careers) The sheet shows the OEWS median for
the one detailed job (right per the spec), but the profile link shows the profile's median: Business Manager $105,770 vs
Top Executives $108,780; Airline Pilot $232,140 vs Airline and Commercial Pilots $210,020; Psychologist $100,580 vs
$99,110; Social Worker $59,550 vs $61,780; IT Support Specialist $61,860 vs $62,890; CNC Machinist $58,750 vs $59,620.
Label the box "Median pay for this job, 2025" or add "(the Handbook page covers a larger group)" to the source line.

#### Nits

**N1. Two paths sit oddly beside the Handbook entry.** (family:careers) Air Traffic Controller sits under Associate's
but its path says only "FAA Academy training; most start before age 31"; Airline Pilot's path says "many airlines want a
degree" beside the Handbook's "Airline pilots typically need a bachelor's degree". Small rewording in careers_data.py.

**N2. Two cluster placements I could not confirm.** (family:careers) Flight Attendant (Hospitality: Travel & Leisure, or
Supply Chain: Air & Space Transportation, "air cargo and passenger services"?) and Public Relations Specialist (Marketing
and Sales, or Arts' "communications"?). The careertech.org cluster pages name neither occupation; check Advance CTE's
occupation crosswalk when B2 is fixed.

#### For the sensitivity agent (rule 5: flagged, not judged)

- Emoji: only two careers use gendered person emoji, Family Doctor (woman health worker) and Chef (man cook); Human
  Resources uses the neutral person. Hairstylist is the haircut emoji and Fashion Designer a dress. They also appear in
  Similar careers. Check whether the set reads as stereotyping who does which job.
- "The braids and face paint booth" (the Hairstylist's place) and the stylist's Try it now ("Practice braids"): check the framing.
- A police officer figure is drawn in code at the crosswalk; check it reads neutral.
- The community help booth (counselor, social worker, psychologist: "Someone to talk to, and help finding help"): mental
  health framing; probably fine, worth one look.
- Pay comparisons can touch students' family incomes; consider a line in notes.md "Good to know". No standard here covers
  a sensitive topic, so rule 8 needs nothing more.

#### Done when (spec)

1. PASS. check(): 37 hotspots, 83 careers, none duplicated or missing; all 83 sheets show "Median pay, 2025", the exact
   `edu`, "2025-35" and a link equal to `ooh` (drive dw1, `bad: []`).
2. PASS. 23 careers checked live (below), including the three larger profiles and all seven "See How to Become One".
3. PASS. Opening two places lit nothing; opening Welder lit Manufacturing; it survived a reload; Start over cleared it and
   localStorage. allLit was spoken once on the real held tap that lit the 14th (d5: `allLit:spoken`); allDone resets on
   Start over, so it plays again on the next run. (See S1: it can be reached without the fair.)
4. PASS. where() called 4 times per cluster: every pick holds an unopened career of that cluster, never the same place
   twice running except Manufacturing (all four careers are at the Ferris wheel, and the hint says so).
5. PASS. Each trail steps in order ("Stop n of m"); end rows 4, 3, 2, 2, 3 with the right cluster chips.
6. PASS. Every ladder chip sits in column `level` (matches the Handbook wording map, and the eduNote for the seven); bar
   widths recomputed as pay / $250,000, all 81 match to 0.1 percent in style and in measured pixels (doctor 97.7 widest,
   pilot 92.9); musician and actor show hourly with no bar. Grid counts recomputed: 4, 4, 11, 7, 5, 5, 6, 3, 11, 6, 3, 4,
   7, 7 = 83, all match the screen.
7. PASS. 50 real Tabs moved through the markers left to right; page scroll stayed 0, the town's scrollLeft stayed 0 and
   the pan followed focus. The List has all 37.
8. Left to Play and Craft (the audit lists no target under 44 px; see Audit pilot).
9. PASS. Five actions in a row: welcomeFestival, lanternHow and panHow each spoken once, panHow then silent; trailEnd3
   spoken on three of three arrivals (held clicks, d4); pickTrail drops a queued trailEnd.

#### Facts checked

Handbook pages fetched live 2026-10-28 (WebFetch); each page uses the 2025-35 projections:
machinist, it-support, social-worker, psychologist, cook, police, pilot (the seven "See How to Become One": Quick Facts
says so on each, and each eduNote is the Handbook sentence verbatim; the psychologist sentence is present word for word);
game-design (Video Game Designers, 15-1255.01, listed under More Information), robotics-tech (Robotics Technicians,
17-3024.01, listed), ops-mgr ("General and operations managers held about 3.6 million jobs in 2025") (the three larger
profiles); graphic-design, athletic-trainer, web-dev, farmer, wind-tech, data-sci, hotel-mgr, atc, realtor, paralegal,
musician, trucker, dispatcher (the Public Safety Telecommunicators title confirmed).
- `edu`: 23 of 23 match. `level`: 23 of 23 right.
- `outlook` percent and word: 23 of 23 match.
- Pay (OEWS May 2025 for the detailed occupation, from the Handbook's Quick Facts or Pay tab): 23 of 23 match (cook: the
  restaurant cooks hourly $17.98 matches; the page gives no annual figure).
- Jobs: not a Handbook field in this tool; 3 of 3 checked differ widely from the Handbook (S2).
- Clusters: the 14 names match careertech.org; about 30 placements checked against the cluster pages, 2 wrong (B2), 2
  unconfirmed (N2).
- notes.md: every claim checked (the Ferris wheel holds all four Manufacturing careers; the kettle corn trail has 5 stops
  and 4 clusters; the larger-profile examples; the privacy line), except question 3 (B1).
- The spec's "every cluster has ways in at every level": false for 13 of 14 (B1).

No giveaways: there is no quiz, predict or hidden mode; the card naming each job's cluster is the explorer format the spec
asks for (P3 is the idea for more). Guardrails: grades 6-8, no hard history, no health topic beyond job descriptions.

#### Audit pilot

- Confirmed: Motion off is clean; the five-click voice runs are clean (they match my held-click counts); the stacked
  layouts (760x900, 375 host) put most Where? buttons below the fold (the panel sits under the stage there; Play to judge).
- Wrong: every marker/panel and marker/privacy-line overlap from 680x425 to 1920x1080 is a marker clipped by the stage
  (#town hides it; audit/size-1366x768.png shows nothing over the panel); the "37 of 60 moved" rows on Where? are the
  intended pan; the four "focus lost" markers I did not confirm and suspect the same clipped-marker cause.
- Missed (as expected, all teaching): both blockers (the misleading ways-in count, two wrong clusters), the 14-tap cheap
  solve from the ladder, the job-count undercount, the self-contradicting psychologist sheet, the unexplained clusters.

Note: a `host.html` (14:08) is in the tool folder; I did not run `--host`, so it belongs to another agent and I left it.

<!-- end part -->

## Fix

<!-- part: review-fix.md -->

### career-cluster-explorer: review fix (Trails jobs on the map)

2026-10-29. Cory's note: "The trail section of the tool should have the jobs and descriptions over the map so they can be more of the focal point."

#### What changed (src.html, notes.md)

- `drawTrailCards()` draws each stop's job on the map, in `#pan` coordinates so it moves with the town:
  - the current stop: a card at its numbered dot (Stop N of M, the job's emoji, title, a lantern in the cluster's color with the cluster name, and the stop's line), joined to the dot by a short yellow pointer;
  - every earlier stop: a compact label at its dot (stop number and job title; one label per dot, one row per stop, so "1-4" at the gate lists four jobs) with a thin pointer;
  - the last stop: the end line ("This bag of kettle corn took 4 clusters", from each trail's own `end`) with the cluster chips, pinned at the top of the town.
- Placement tries spots around the dot (above, below, beside, corners, at three distances, then top or bottom of the town) and scores the whole layout (card plus every label): nothing may overlap a dot, another card or label, or the end line, or leave the town. If no clean layout fits it shrinks the card (lg 340, md 290, sm 240, xs 200, then `flat`, a wide short card that drops the Stop line, which the panel still shows). A last-resort pass may cover an earlier or later dot, never this stop's or the next stop's; in the final runs it was never needed.
- `panToTrail()` pans so the card and its dot are in view and clear of the ◀ ▶ buttons, then takes in the most recent earlier stops while they fit. Motion off: instant pan, no card fade (Motion on: a 0.3 s fade-up of the card only).
- The panel keeps a short card (Stop N of M, emoji, title; cluster and line are screen-reader text). The panel's end row is no longer shown (the map has it). Back, Next, Open career and the trail picker are unchanged. Stack layouts now only scroll the town back into view if it scrolled off.
- At phone widths (under 560 px) the ◀ ▶ buttons hide in Trails only: at 375 they covered the cards. Next and Back pan the town; drag, wheel, arrow keys and the minimap still work. Noted in notes.md.
- Found on the way: the kit's `.calm *{transition-duration:.01ms}` makes every property transition, so a size read straight after a class change was stale in Motion off (wrong card size and overlaps). The trail layers set `transition-property:none`. The kit rule may bite other tools that measure after a class change.
- No line text changed: `allLines()` equals voice/lines.json (9 lines), so every clip still matches. No art touched.

#### Checks

- Bundled: `python scripts/bundle_tool.py career-cluster-explorer`, 343 KB. `check_tools.py`: ok.
- Driven with scripts/drive.py (ports 9301 and 9302, host 8821): every stop of all 5 trails (27 stops) at 1366x768, 1280x720, 1920x1080, 1000x625, 800x500, 680x425, 760x900 and 375x812 (host), Motion on (final-on/) and off (final-off2/): 432 frames. Each frame's script measured the card, the labels, the end line and the dots: 0 overlaps, the card fully inside the town, and not under a ◀ ▶ button, in all 432. No console errors (only the host server's favicon 404).
- Real held clicks: Trails, Kettle corn, Next x4 at 1366 (Motion on and off): trailEnd4 spoken after the welcome, focus lands on Open career. Ankle trail by the select plus Next at 680. A drag in Trails moves the cards with the town.
- Frames in S:/CurioClass-codex-scratch/review/career-trails/ (contact sheets sheet-on-*.png). Best: final-on/1366x768-t0-s5.png, final-on/1920x1080-t1-s6.png, final-on/h375x812-t3-s5.png.

#### Left

- The full chain does not fit on screen at once on any size (the town is 2400 units wide at stage height), so the end view shows the last card, the end line and the stops that fit; the rest are labeled where they are when the student drags. A zoom-out view at the end would be the next step if Cory wants every stop in one look.
- At 680x425 and 375 the card can sit a long way above or below its dot (the flat card) on the twisted-ankle ending, where four stops crowd one corner.
- At 760x900 cards use the small size (the stage is short for its width); readable but smaller than at 1366.

#### Town art

2026-10-29. Cory's note: "the background graphics are not good and need upgraded."

##### What changed (src.html, tool.json, notes.md, preview.svg)

- `drawScene()` keeps the code sky gradient, stars, moon, string lights and poles, fence, power lines (poles moved down 20 to stand on the painted hills), Main Street road with crosswalk and lane lines, the weather board and the big screen. Every old flat place drawing is gone (far hills, ridge, ground, foreground grass, airport hill and all 33 places).
- New: `town-land.webp` across the bottom (y 309 to 900; the barn sprite covers its little lit house), then the 33 sprites as SVG `<image href="art:town-...">` through one helper, `put(href, w, h, left x, ground y, scale)`, drawn back to front (turbine, soccer, Ferris, radio, stage, art row, barn, bridge, gate, kettle, first aid, food trucks, theater, braids, then the front row, then Main Street). Scales 0.6 to 1.3 so a car or truck stays smaller than a stall, a stall smaller than a building, and the hotel and clinic tallest on Main Street.
- The river: the bridge sprite brings its own water; below it the old river is now a soft teal-to-navy gradient with faint ripples, so the river marker still sits on water.
- The road is narrower and lower (y 818 to 890) so the shops stand on the sidewalk above it; the police car, crosswalk and delivery truck are on it.
- Signs stay code text over the art: FAIR on the gate arch, 72° CLEAR on the board, 2 : 1 on the screen, LIBRARY on the library pediment, SALE on a small red board over the house's painted sign, $ above the bank pediment, HARDWARE on the orange awning, HIRING on a card in the shop window, HOTEL on the hotel roof line.
- The plane sprite faces left, so its dashed trail now runs off to the right (it flies left).
- The Ferris wheel sprite first kept a lot of its green key between the spokes. A display-time filter covered it for one pass; the coordinator then re-keyed `town-ferris.webp` (magenta key) and removed the filter, so src.html has no filter now (see Round 2).
- `police` is now "A police car at the crosswalk" (the sprite replaced the drawn officer; careers unchanged; not a voiced line).
- Minimap silhouette redrawn for the new skyline (bigger Ferris, shorter clinic, wider hotel).
- Unused `poly` and `win` helpers removed. Header comment, tool.json sources and notes.md now say the town is painted; tool.json has the FLUX credit line.

##### Moved HOT ids

- `bank` (1960, 520) to (1960, 600): the old spot was sky above the painted bank.
- `upstairs` (1800, 400) to (1790, 500): the old spot was above the painted clinic's roof; it now sits on its upper windows.
- Nothing else moved. `field` stays between the soccer light poles at their height.

##### Checks

- Bundle 772 KB (art about 335 KB as WebP, about 450 KB once inlined). `check_tools.py`: ok.
- Trails layout check (the scoring script from career-trails, every stop of all 5 trails): 1366x768 Motion on 27/27, 1366x768 and 375x812 Motion off 54/54, 375x812 Motion on 27/27: 0 overlaps with dots, card always in the town and never under a ◀ ▶ button. No console errors (only the host server's favicon 404).
- Frames in S:/CurioClass-codex-scratch/review/career-town/: `full/scene.png` and `full/scene-hot.png` (the whole 2400x900 town at 1:1, with and without every marker drawn on), `fest/fest-1366-p0..p4.png` (Festival panned left to right at 1366x768), `fest/fest-1366-calm-p2.png` (Motion off), `fest/fest-1920.png`, `fest/sheet-h375.png` (phone, panned), `sheet-trails-last.png` and `sheet-trails-h375.png` (each trail's last stop), all Trails frames in `trails-on/`, `trails-off/`, `trails-h/`, and `preview.png` (the new card).

##### Open concerns

- (Closed in Round 2: the Ferris wheel was re-keyed and the filter removed.)
- The gate sprite has the word "Ticket" painted on its booth; it reads fine but is the one bit of painted text.
- The Ferris wheel is the biggest thing in town (346 wide) and its legs reach behind the gate and kettle stand; it reads as the centerpiece but crowds that corner.
- The soccer pitch sits on the crest of the hills; at full size it looks like a field up the hill rather than on the fairground.
- The town art is FLUX art with `"review": "pending"` in prompts.json; nobody has signed off each sprite yet.

#### Round 2

2026-10-29, from final-art.md (Final look: FIX, 2 must, 4 should, 7 polish). New art from the coordinator: art row (one grounded group, no people, 195x140), soccer field (flat, 247x75), bank (no lettering, 169x194), gate (re-keyed), Ferris (re-keyed, filter removed). No art redrawn or re-keyed here.

##### What changed (src.html)

- **Art row (must 1, 2):** the new sprite at 0.7 stands on the fairground left of the field (x 1222, ground 692), clear of the pitch.
- **Soccer field (should 3, 5):** the flat field at 0.8 lies on the fairground just behind the fence (x 1368 to 1566, y 639 to 699), below the hill crest, so it reads as a field at the fair, not a slab on the ridge. Two code light towers with a glow (the old idea) stand at its back corners. First aid moved off it, to the right (x 1560, 0.55). Food trucks moved to the front row (0.62) and the braids booth forward (ground 790) to make room.
- **Signs (should 4):** the library marker moved to the doorway, the hardware marker to the shop's left wall; LIBRARY and HARDWARE read whole. $ moved into the new bank's pediment.
- **put() sizes:** artrow 195x140, soccer 247x75, bank 169x194 (0.9), so nothing is stretched.
- **Polish:** Ferris wheel 0.62 (hub still at 1000, 420; base 678), so the gate, kettle stand and stage have air. Fire truck 20 right, off the river. Road gets a soft left end (gradient over its first 64 units, rounded corners). Minimap skyline lighter (#8d82c4 on #0d0a22). The old `#unkey` comment is gone and the Town art note is corrected.
- **375 Trails labels (polish 12):** `clipLabs()` hides an earlier-stop label, and its pointer, while any part of it is outside the stage; it runs after each layout and on every pan, so a label shows again once it is fully in view. No half words at the edge.
- **375 ankle ending (polish 13):** with `field` and `firstaid` moved, the layout now puts the Physical Therapist card beside stop 5 (sm card, not the flat fallback).

##### Moved HOT ids (this round)

`artrow` (1290, 530) to (1290, 640); `field` (1420, 420) to (1467, 670); `firstaid` (1450, 600) to (1603, 655); `food` (1330, 680) to (1316, 745); `braids` (1560, 720) to (1543, 745); `library` (1700, 600) to (1700, 662); `hardware` (2000, 700) to (1958, 728). Earlier round: `bank`, `upstairs`.

##### Checks

- Bundle 835 KB.
- Trails layout check, every stop of all 5 trails: 1366x768 Motion on 27/27, 1366x768 and 375x812 Motion off 54/54, 375x812 Motion on 27/27; 0 overlaps with dots, cards always in the town and never under a ◀ ▶ button. No console errors (only the host's favicon 404).
- Frames in S:/CurioClass-codex-scratch/review/career-town/round2/: `fest/fest-1366-p0..p4.png`, `fest/fest-1366-calm-p2.png`, `fest/fest-1920.png`, `fest/fest-h375-p*.png`, `sheet-trails-last.png`, `sheet-trails-h375.png`, `trails-on/`, `trails-off/`, `trails-h/`, zooms `z-hardware.png`, `z-ferris.png`, `z-roadend.png`. Whole town at 1:1: `../full/scene-hot.png`. preview.svg regenerated.

##### Open

- Ferris spokes: a thin pink edge is visible at 1:1 (z-ferris.png), mostly on the outer rim. At 1366 it is barely there and reads as trim; a tighter re-key would remove it.
- Bank sprite: fine, no lettering. Gate: no green specks seen in the frames.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Handoff: career-cluster-explorer

Built 2026-10-28 (BR wave, build agent). Draft: no recorded voice yet (`python scripts/voice.py career-cluster-explorer`
when the lines are final). No art: everything is drawn in code.

#### Files

- `src.html`: the tool. Uses `kit:curio` and the careers family engine `kit:careers` (docs/families/careers.md).
- `careers.json`: this tool's own 93 careers (career-match-quiz's 83 plus 10 added in polish round 1) with the Handbook fields (`edu`, `eduNote`,
  `level`, `outlook`, `ooh`, `oohTitle`) and `handbook: {edition: '2025-35'}`. Built in the build agent's scratch
  folder from the live Handbook pages (fetched 2026-10-28); `sources.md` lists every profile URL, the exact wording,
  the seven "See How to Become One" quotes and the larger-profile cases. bls.gov blocks curl (403); fetch pages with a
  browser-like fetch. Never guess a value.
- `sources.md`, `notes.md`, `tool.draft.json`, `voice/lines.json` (upbeat-guide, Zephyr), `art/prompts.json` (empty).

#### How src.html is laid out

1. CONTENT: `HOT` (37 hotspots: id, x, y in scene units 2400 x 900, name, line, short name for hints, careers) and
   `TRAILS` (5: id, short, name, end phrase, stops). `HOME` maps career -> hotspot. `__tool.check()` verifies every
   career is in exactly one hotspot, the minimum marker gap in px, and the trail cluster counts (4, 3, 2, 2, 3).
2. LINES and `EVENTS`, then STATE (lanterns, opened careers and opened places are saved in localStorage
   `career-cluster-explorer-lit`, try/catch) and `Curio.voice` with `hint: false` (the tool owns the hint; Read
   speaks `#hint`).
3. The sheet: `Careers.sheet` with theme `night` (colors in the `.cr-sheet.night` rule), facts pay, edu, outlook,
   jobs; `onOpen` -> `careerOpened` lights the lantern (the only place a lantern lights).
4. Lanterns: one row with names when each gets 64 px, two rows of seven in a tall narrow stage, else dots and a
   count (compact). Soft hyphens (`SOFT`) keep long names readable.
5. The scene: `drawScene()` builds the SVG; markers are 44 px buttons in `#marks` inside `#pan`, positioned at
   `x * s, y * s` with `s = town height / 900`. Panning is a translateX on `#pan` (`setPan`, `panTo`), with a 56 px
   pad past both ends so the end markers clear the ◀ ▶ buttons. Drag (inertia only with Motion on), wheel, arrow
   keys, buttons, the minimap. A scroll of the clipped `#town` (scrollIntoView, screen readers) becomes a pan.
   Focusing a marker pans it into view.
6. The card (`openHot`, `placeCard`, `closeCard`): beside the marker, flipping near the edge; a bottom sheet under
   560 px. Esc closes the sheet first (the engine stops the key), then the card, and focus goes back to the marker.
7. Where? (`where(k)`): a hotspot with an unopened career of that cluster, never the last suggestion unless it is
   the only one (Manufacturing: all four are at the Ferris wheel, so the hint says "Still the Ferris wheel: it's the
   only place..."). Compact layouts have one Where? button that walks the dark clusters in turn.
8. Trails: `pickTrail`, `goStop`, `drawTrail` (dim layer, dotted path through the distinct hotspots, numbered
   stops; a hotspot holding several stops shows "3-5"). trailEnd2/3/4 are events with a `valid` that drops them
   when the trail or stop changes; picking a trail drops a queued trailEnd.
9. Clusters: the grid (full names, short names in compact and narrow), the ladder (5 columns from 900 px of board,
   else rows), pay bars on one $0 to $250,000 scale (musician and actor have hourly pay, no bar), outlook arrow,
   percent and word, See it.
10. Panel and hint: `drawPanel` rebuilds the Where? and List buttons only when their set changes and keeps focus.
    `hintText()` is computed from state and set at once on every change.
11. Layout: `relayout()` picks wide / compact / stack (as in fake-or-fact-lab), sets `narrow` under 560 px, sizes the
    stack stage, the lanterns and the scale, and keeps the view centered across resizes. In compact and stack the
    trail controls come before the trail picker; compact and narrow use a select for the picker.

#### Tricky parts

- The audit's overlap leads between markers and panel controls are markers clipped by the stage (their boxes run
  past `#town`, which hides them). They are not visible or clickable there.
- `state.trail` can be 0: always test `!== null`.
- The engine sheet's Esc handler stops propagation; the page's own Esc handler then sees nothing while the sheet
  is open, by design.
- `Careers` is a page global, so frames can draw a default sheet (`Careers.sheet({data: __tool.DATA}).open('welder')`)
  to check parity with career-match-quiz.

#### What I would do next

- Record the voice. Consider a "nice, you found Manufacturing" style event line per new lantern if Refine finds the
  festival too quiet (the spec has none, so I added none).
- The ladder chips are tall in narrow columns; a denser chip would show more careers at 1280 x 720.
- Move career-match-quiz onto `kit/careers.js` when it is next touched, and teach `scripts/careers_data.py` to write
  the Handbook fields (the open question in the spec).

#### Polish round 1

2026-10-28. Checked with scripts/drive.py, using held clicks and real keys, on ports 9950-9954, plus the 375 host on 9951 (host.html deleted). Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812. No console errors. `__tool.check()` shows 93 careers, none missing or duplicated, and a minimum marker gap of 44.6 px at 375. voice/lines.json still matches allLines() (L unchanged). Bundled with CURIO_DRAFT=1.

1. Added 10 Handbook careers through `C_MORE` in scripts/careers_data.py (`--more`; each one checked on its live Handbook page, with O*NET OnLine interests). Edu, Public Service and Health now have ways in at all 5 levels. The ladder line and the panel now say "Careers in this tool: ways in at N of 5 levels" and add that the real cluster has more. Empty columns read "None in this tool (the real cluster may have some)". Notes question 3 is reworded and the spec claim is fixed. Checked: the fin, mgmt, mfg and health ladders at 1366.
2. Hairstylist moved to health and Real Estate Agent to fin in careers_data.py; careers.json rebuilt and counts updated. Checked: the stylist sheet and the fin ladder.
3. Focusing a marker pans only on `:focus-visible`, so a pointer press never pans. Checked: held clicks on a marker 50 px from the right and left edges at 680x425 and 1366, and 30 px from the edge at 375. Each opened the card.
4. Only `ctx.from` 'card' or 'trail' lights a lantern. The sheet's lantern line says "lit" or "not lit yet. Meet this job at the festival to light it." Checked: a held click on a ladder job and on a Similar career (lit 0, line correct) and on a card job (lit 1).
5. "People doing it" now uses the Handbook's number of jobs (`oohJobs`), and the sheet names the profile and says it counts self-employed workers. Checked: Farmer shows 789,000.
6. New psychologist path text. Checked on the sheet.
7. `DEF` holds one plain line per cluster (from careertech.org "The Cluster Defined"). It shows under the ladder heading and on the sheet's lantern line. Spec Sources and sources.md updated. Checked on the ladders and sheets.
8. allLit is queued with `wait`; if it is dropped, allDone is cleared so it comes back. Checked: lit the 14th lantern during the first-tap welcome. Log: welcome spoken, then allLit spoken at 6.5 s.
9. When Next or Back disables itself while focused, focus moves on (Next to Open career, Back to Next). Checked with real Enter (activeElement openCareer / next) and a held click at 375.
10. The clusters grid uses 2 columns at narrow widths and 3 in compact. Checked: no clipped names at 375, 680, 760 or 800.
11. lanternHow plays only in Festival. closeCard queues [lanternHow, panHow] as one sequence. Checked: the log shows lanternHow spoken, then panHow spoken. In Trails, no lanternHow.
12. Esc on the confirm puts focus on Start over. Checked with real Esc.
13. kit/careers.js reads keys on document in the capture phase while the sheet is open (documented). Checked: clicked the sheet text, then Esc, and the sheet closed.
14. The card button reads "✕ Close". New hint: "Tap Close, or press Esc, to close the card." Checked at 680, 800 and 1366.
15. Emoji: doctor 🧑‍⚕️, chef 🧑‍🍳, hairstylist ✂️. Checked on the sheets.
16. The education fact says the level in plain words, with the Handbook phrase and note underneath (`eduPlain`). Checked: machinist, psychologist and farmer.
17. Pay label is now "Median pay for this job, 2025". When the profile's pay differs, the sheet adds "The Handbook page covers a larger group, ...". Checked: machinist, psychologist and stylist.
18. New pilot and ATC path lines in careers_data.py.
19. Police head fill is #c9c3ea. Checked on the SVG.
20. Fashion 🧵, Musician "places of worship" and the new hotel-mgr try line, all in careers_data.py.
21. At the last stop in a stacked layout, the page scrolls so the trail result is in view. Checked: endrow bottom 800 of 812 at 375 and 988 of 1000 at 760.
22. Stacked Clusters let the page scroll (no inner box). Ladder chips are shorter: on rows, See it sits on the name row, and compact uses one-column, two-line chips with no level subtitles. Checked: 375 board 1808/1808, page 2525; 680 Health 369/1365 (was 341/1461).
23. Lanterns use the `big` class when each gets 100 px or more and the screen is 900 px or taller. Checked: 1920x1080.
24. In compact with innerHeight of 600 or more, the Still dark list shows. Checked: 1000x625.
25. The pop and shimmer wait in `state.pops` until the sheet closes (`popLater`). Checked: no pop under the sheet, ln-mfg pops after close.
26. Hint now reads "Stuck? Tap Where?" with no doubled period. Stop header uses non-breaking "Stop N of M". Checked: header is one line (16 px) at 1280 and 1366.
27. Where? by keyboard (detail 0) focuses the circled marker. Checked with real Enter at 680 (Where?) and at 1366 (Still dark): focus lands on mk-ferris. A mouse click leaves focus on the button.
28. A card opened from the List returns focus to its List entry. Checked: Esc gives list:barn.
29. `cardMet()` adds "✓ met" in place. Checked: shows on the welder job while focus stays on it.
30. The scale line now sits above the ladder. Checked at 1366.
31. The family doc covers the fixed ids, the capture-phase Esc and Tab with preventScroll. Also: the sheet header keeps 116 px clear so a long name no longer runs under "✕ Close" (seen at 375).
32. Privacy line: "Your lanterns and the careers and places you opened are saved in this browser on this device only. Nothing leaves it." Notes updated.
Settled calls: Flight Attendant and PR are marked unconfirmed in sources.md. The braids booth, crosswalk officer and help booth are unchanged. career-match-quiz and its careers.json are untouched; the builder still writes to the quiz path by default, and the quiz picks up the fixes when it moves to kit/careers.js.
Not done: the optional nit to hide marker labels while the card is open. Spec open questions are left as they were.

<!-- end part -->

## Art and voice

<!-- part: final-art.md -->

PASS
Re-check counts: must fix 0, should fix 0, polish open 2 (known, not done). Round 1 counts: must 2, should 4, polish 7.

### career-cluster-explorer: Final look after Cory's review (painted town, Trails cards on the map)

#### Re-check (round 2), 2026-10-29

Same agent, ports and scratch. Rebuilt bundle (19:35, 831,384 bytes). I rescanned the sprites, re-rendered the whole
2400x900 town with and without markers, and re-ran all 147 shots. Everything is in
S:/CurioClass-codex-scratch/review/career-final-art/r2/ (scene-m0.png, scene-m1-0/1/2.png, z-*.png, shots/, run.log,
sheet-h375-town.png, sprites-*.png). Chrome and the 8861 server are closed.

| # | Finding | Now | Frame |
|---|---|---|---|
| 1 | Art row floating on the pitch | Closed: one grounded stall with an easel and a flower cart, standing on its own dirt patch on the fairground left of the field | r2/scene-m0.png, r2/z-artrow.png |
| 2 | People in the art row picture | Closed: the easel and the stall hold sunflower paintings only, no figures | r2/z-artrow.png |
| 3 | Soccer pitch as a slab on the hill | Closed: a flat field on the fairground behind the fence, two code light towers, first aid tent beside it, not on it | r2/scene-m0.png, r2/shots/fest-1366x768.png |
| 4 | Markers over LIBRARY and HARDWARE | Closed: both words read whole at 1366 and on the 1:1 town; HIRING and $ also clear | r2/shots/pan-1366-p4.png, r2/scene-m1-2.png |
| 5 | `field` marker in the sky | Closed: on the pitch. All 37 markers sit on the place they name (artrow, field, firstaid, food, braids, library and hardware re-checked after their moves) | r2/scene-m1-1.png, r2/scene-m1-2.png |
| 6 | Green key on the gate posts | Closed: post feet are clean (19 faint green edge pixels left in the file, none visible) | r2/z-gate-scene.png |
| 7 | Ferris crowding and fringe, stale comment | Closed for crowding (0.62: gate, kettle stand and stage have air) and the comment (no `unkey` in src.html). The spoke edge is now a muted purple, not pink; about 5,470 edge pixels still meet my magenta test, but nothing reads as fringe at 1366 or 1920. Left as known polish | r2/z-ferris-file.png, r2/scene-m0.png |
| 8 | Fire truck on the river edge | Closed: on the bank | r2/z-fire-scene.png |
| 9 | Bank door lettering | Closed: the redrawn bank has none | r2/sprites-dark.png |
| 10 | Road end | Closed: soft fade with rounded corners | r2/scene-m0.png |
| 11 | Minimap contrast | Closed: the skyline is now a light lavender shape, clearly visible | r2/z-mini.png |
| 12 | 375 labels cut mid-word | Closed: no half words in any of the 27 phone frames. Side effect: a label whose dot is in view but whose label would cross the edge is hidden, e.g. "Coach / Athletic Trainer" at the 1-2 dot on the ankle ending. Known polish; the label returns once the town is dragged | r2/sheet-h375-town.png, r2/shots/h375-ankle-s5.png |
| 13 | 375 ankle card far from its dot | Closed: the card sits beside stop 5 (xs card, not the flat fallback) | r2/shots/h375-ankle-s5.png |

No regressions:
- **Trails layout:** 121 of 121 measured layouts are clean (no card or label over a dot, no overlaps, card fully in
  the town). The sizes are the same as round 1: every stop of all 5 trails at 1366 Motion on and off and at 375, plus
  stop 2 and the last stop at 1920, 1280, 760x900 and 680x425. No flat fallback cards remain. Titles are 23 px at
  1920, 19 px at 1366 and 14.5 to 15.5 px at 375.
- **Motion off:** reduce is true with 0 animations.
- **Voice:** in the held-click Trails run, welcomeTrails starts at 1.34 s and trailEnd4 at 7.09 s, matching the end
  line.
- **Bundle:** 0 `art:` tokens, all 34 sprites inlined (md5 matched), no network requests, no em dashes. There are no
  console errors other than the local favicon 404.
- **Panned shots:** the check marks on places in r2/shots/pan-*.png come from earlier card shots in the same test
  profile (saved places). This is not a finding.

Sensitivity on the redrawn art (art row, soccer field, bank, gate, Ferris): no people, faces or hands; no lettering
except the gate's "Ticket"; no symbols, brands or stereotypes. The whole set still has no people. careers.json is
unchanged, so the career cards stand as passed.

Cory's two notes now read as clearly answered. The middle of the fair, the one weak patch in round 1, now looks like
part of the same painted town.

Known, not done (Review Desk "changed" note): the Ferris spoke edge (item 7) and the hidden in-view labels at 375
(item 12).

---

Round 1 findings follow, unchanged.

Cold check on 2026-10-29 against REFINE.md (Final look), STANDARDS.md and BASELINE.md, after reading handoff.md,
final.md, refine/final-sensitivity.md and review-fix.md (both sections). This file covers the tool as it is now; final.md
is left as it was.

Bundle checked as built by the builder (career-cluster-explorer.html, 19:10, same time as src.html). Driven with
scripts/drive.py on Chrome ports 9341 and 9342 (own profiles), the 375 host served from the tool folder on 8861 (the
existing host.html, not rewritten). 147 shots, all looked at as frames or contact sheets. Everything is in
S:/CurioClass-codex-scratch/review/career-final-art/ (shots/, run.log, scene-*.png, z-*.png, sprites-*.png,
sheet-h375.png). Chrome and the server were closed after the run.

#### Cory's two notes: do they read as answered?

- **"The trail section should have the jobs and descriptions over the map."** Yes, clearly. The current stop's card
  (Stop N of M, emoji, title, cluster lantern, the stop's line) sits on the map at its numbered dot with a pointer,
  earlier stops carry name labels, and the last stop pins "This bag of kettle corn took 4 clusters" with chips at the
  top of the town (shots/tr-1366-kettle-s5.png, shots/tr-1366-lights-s3.png, shots/tr-1920x1080-ankle-end.png,
  shots/trcalm-1366-bridge-s5.png). The panel now only repeats the title. The jobs are the focal point.
- **"The background graphics are not good and need upgraded."** Mostly yes. The town now reads as one painted
  storybook place at night with one palette and outline style (scene-m0.png, shots/fest-1366x768.png,
  shots/pan-1366-p2.png, shots/pan-1366-p4.png). Main Street, the farm, bridge and river, and the front row of
  tents are a big step up. The one patch that still looks unfinished is the middle hill (soccer pitch, art row, first
  aid tent), which is the must-fix below. Cory will notice it, because it sits in the center of the default view at
  every size.

#### Must fix

1. **Art row is floating clutter on top of the soccer pitch** (scene-m0.png around x 1230 to 1380, y 520 to 600;
   z-soccer.png; shots/fest-1366x768.png right edge; shots/card-1366-artrow.png). `town-artrow.webp` is a scatter
   of loose objects: a window and a wall lantern hanging in the sky, an easel whose picture floats above its leg, a
   sandwich board, and the parade float. Placed at (1214, 606, 0.8) the float and sandwich board stand on the green
   pitch, and the window, lantern and picture hang in the air left of it. It reads as debris on the field, not as
   "art row: the festival poster, a photo booth and the costume parade float". Needs a redrawn sprite of one grounded
   group (a poster board, a photo booth, a float) placed on the fairground in front of the hill, not on the pitch.
2. **The art row picture shows people from the local model** (z-artrow.png: the easel painting is two figures, an
   adult in a pink dress and a child). STANDARDS (Art): never people, faces or hands from a local model. It is small
   in the scene (about 20 px), but it is a person picture nobody reviewed. The redraw in item 1 should give the
   poster a non-figure design (ask for a blank or patterned poster, worded positively).

#### Should fix

3. **The soccer pitch reads as a raised slab on the hilltop** (z-soccer.png, scene-m0.png x 1060 to 1250 at the
   2000-wide view). The sprite has a thick dark edge under it, so at scale 1.3 on the crest it looks like a table top
   or a field up on the ridge, and the first aid tent sits on its front edge. With item 1 this whole middle patch
   looks stacked. Options: a flatter field sprite set lower behind the fence, or smaller and set back, with the first
   aid tent clear of it. The `field` marker (1420, 420) then needs to move onto the pitch (item 5).
4. **Markers cover their own code signs** (z-signs.png, shots/pan-1366-p4.png, shots/fest-760x900.png): the library
   marker sits on the middle of "LIBRARY" (reads "LIB(dot)ARY") and the hardware marker on "HARDWARE" (reads
   "(dot)ARDWARE"). Move either the marker (for example library to the doorway, hardware to the window, as bank and
   upstairs were moved) or the sign text so both read. The other signs (FAIR, 72° CLEAR, 2 : 1, $, SALE, HIRING,
   HOTEL) sit cleanly on the art.
5. **The `field` marker floats in the sky** between the light poles, about 100 scene units above the pitch
   (scene-m1-1.png, shots/pan-1366-p2.png, also the "1-2" dot in shots/tr-1920x1080-ankle-end.png). It names "the
   youth soccer game under the lights"; every other marker sits on its place. Put it on the pitch once item 3 settles
   where the pitch goes. Every other tap marker checks out on its place (scene-m1-0/1/2.png); `weather` sits on the
   board's pole just under the board, which is fine.
6. **Green key leftovers on the gate** (z-gate.png): the two light green bow-tie shapes at the feet of the gate
   posts are key green that survived (95 strongly green pixels in `town-gate.webp`, 21 on the edge). They show as
   bright green specks right beside the FAIR arch at every size. Re-key or crop them.

#### Polish

7. **Ferris wheel crowding and fringe.** The wheel is the biggest thing in town (346 wide) and its legs run behind
   the gate, the kettle stand and the stage (z-gate.png, scene-m0.png). It reads as the centerpiece and the overlaps
   are front-to-back correct, so this is polish, not a blocker; a slightly smaller wheel (about 0.62) would give the
   gate and kettle stand air. The file on disk is now magenta-keyed (6,606 semi-transparent magenta edge pixels, 18
   green): the spokes have a thin pink outline (z-ferris-top.png, z-ferris-scene.png). On the purple sky it reads as
   neon trim, but it is key fringe. review-fix.md describes a green key and an `#unkey` filter; that filter is no
   longer in src.html, and the comment at src.html line 625 still describes it. Update the comment and the note.
8. **Fire truck parked on the river's edge** (z-fire.png): its painted ground strip overhangs the water. Move it a
   little right (about 20 units) onto the bank.
9. **Bank door lettering**: the bank sprite has tiny garbled lettering above the ATM (z-bank.png). Unreadable at
   display size; the code "$" carries the meaning. Note only; the gate's "Ticket" is the one readable painted word
   and is fine.
10. **Main Street road starts abruptly** at its left end behind the sponsor tent (scene-m0.png bottom, x about 1370
    at the 2000-wide view): a hard dark rectangle. A short fade or a curb end would finish it.
11. **Minimap silhouette barely shows** (z-mini.png): the redrawn skyline is a very low-contrast purple shape in a
    strip about 20 px tall; the yellow view box works, the skyline adds little. Raise its contrast a step.
12. **375 Trails: earlier-stop labels cut by the stage edge** (sheet-h375.png; shots/h375-lights-s4.png shows
    "ne Technician / Worker", shots/h375-kettle-s2.png shows "ancher"). They pan in with the town, so nothing is
    lost, but a half word at the edge looks broken. Hide a label whose dot is off the stage, or clamp it in.
13. **375 flat card far from its dot** on the ankle ending (shots/h375-ankle-s5.png: the Physical Therapist card is at
    the bottom, dot 5 at the top right, no visible pointer between them). Known in review-fix.md; still true.

#### Frames (step 1)

- Festival at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900 (shots/fest-*.png), panned
  left to right at 1366 (shots/pan-1366-p0..p4.png), 375 host default and mid-pan (shots/h375-fest*.png). No
  placeholders, no garbled lettering beyond item 9, no text over busy art except items 4 and 12. Lantern and panel
  text unchanged and readable.
- Cards on the moved and art-heavy spots (artrow, field, weather, firstaid, ferris, police, forsale, upstairs,
  bank) at 1366 all open and sit on solid panels (shots/card-1366-*.png).
- Trails layout, measured in each frame (script in mk.py: every card, label and end line against every trail dot,
  each other and the town box): every stop of all 5 trails (27) at 1366 Motion on, 1366 Motion off and 375 (host),
  plus stop 2 and the last stop of each trail at 1920x1080, 1280x720, 760x900 and 680x425. 121 of 121 layouts have
  no card or label over a dot, no overlaps between them, and the card fully in the town. Card title size: 23 px (lg)
  at 1920, 19 px (md) at 1366, 15.5 px (sm) at 375 and the short stages, 14.5 px only on the 3 flat or xs fallbacks.
  Line text 12.5 to 18 px on solid card panels: readable at every size.
- Motion off: shots/fest-1366-calm.png reports Curio.reduce true and 0 running animations; Trails in Motion off uses
  the same md cards with no overlaps (shots/trcalm-*.png).
- Minimap: the view box tracks the pan in every panned frame; see item 11 for the silhouette.

#### Art (step 2)

- 34 sprites, all present in the bundle as WebP (md5 matched per file), 0 `art:` tokens left.
- One artist feel across the set: gouache, dark outline, blue-violet shading, warm windows (sprites-dark.png,
  sprites-white.png). Scale is sensible on Main Street and in the front row; the soccer pitch and art row are the
  exceptions (items 1 and 3).
- Key check per file (strongly green or magenta pixels, and how many are semi-transparent edge pixels): real
  fringe only on the Ferris wheel (item 7) and the gate (item 6). The soccer grass, stage lights, fire truck lights and
  the land strip's green and magenta counts are painted colors, not key (checked on sprites-lime.png and in the scene).
- Grounding: everything stands on ground except the art row pieces (item 1); the fire truck is on the bank edge
  (item 8). The plane is meant to fly.

#### Voice (step 3)

No line or clip changed since final.md (review-fix.md: `allLines()` equals voice/lines.json). One real held-click run
at 1366 (shots/real-trails-1366.png): Trails, Kettle corn, Next x4; welcomeTrails spoken at 1.35 s, trailEnd4 spoken
at 7.06 s after it, hint "That's the end of the trail. Pick another trail, or tap Open career...", matching the
pinned end line "took 4 clusters". Nothing overlapped.

#### Full run (step 4)

Solo student: the painted town is far more inviting than before, and the Trails cards make each trail a story you
read on the map. The thing a student will poke at is the middle hill, where the art row and soccer field look
dropped in. Teacher projecting at 1920: the trail cards and end line read from the back of the room.

#### Contract (step 5)

Bundle 835,040 bytes (under 2 MB), no fetch, XHR or external src/href, no em dashes. No console errors in 147 shots;
the only log is the local server's favicon 404 (host frames only).

#### Sensitivity (pictures changed)

- People in the art: only the small painting on the art row easel (item 2). No other sprite shows a person, face or
  hand: vehicles are empty, the stage has instruments only, the booths and tents are empty, the petting pen has
  goats. The police place is now a police car, no figure.
- Stereotypes or anything off for a K-12 classroom: none found. No religious, political, brand or cultural symbols;
  the town hall's pediment symbol and the clinic's red crosses are generic. Painted text: "Ticket" on the gate booth
  (fine) and the garbled bank door lettering (item 9).
- Career cards: careers.json is unchanged since refine/final-sensitivity.md (its PASS covered all 93 cards, the
  gender-neutral people emoji and the object emoji). The cards checked here (shots/card-1366-*.png) still show the
  same emoji and wording. Fair across kinds of people as before.

<!-- end part -->

## Finish check

<!-- part: final.md -->

PASS
Counts: blockers 0, should fix 0, polish 3, nit 3

### career-cluster-explorer: Final look

Cold check on 2026-10-29 against REFINE.md (Final look), STANDARDS.md and BASELINE.md, after reading refine.md (round 1 PASS)
and handoff.md. Real assets: 9 recorded clips (local Qwen3-TTS clone, upbeat-guide bank, credit in voice/local.json). No art
files: the town is drawn in code and art/prompts.json is empty by design. The sensitivity review is a separate agent's job
and is not repeated here.

Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py career-cluster-explorer`, 330 KB. Driven with scripts/drive.py (held
clicks of 0.12 s, Sound and Motion on unless named) on ports 9201 and 9202, with the 375 host on 8811. Frames and logs are
in S:/CurioClass-codex-scratch/final/career-cluster-explorer/ (f/, v/, v2/). I looked at every frame named here. The audit
(audit_tool.py, audit/audit.md) finished late, with 25 leads; its log has one CDP connection reset, so its rows are leads
only. I confirmed the leads on my frames:
- Marker / Pan right overlaps at 800, 1280, 1366 and 760, and walk rows 39 to 44 "covered or clipped": these are markers
  clipped by the stage edge, which is the known case in handoff.md (Tricky parts). Not a finding.
- "Where?" buttons below the fold at 760x900 and 375, and trail buttons below the fold at 760x900: these are the
  stacked page scroll, with the first rows in view (f/n375-default). Refine passed this. Not a finding.
- Clusters hint out of view at 375: see nit 6.
- Pan left "nothing changed" in Trails: the view is already at its left end. Not a finding.
- Walk, five clicks and quick taps: every welcome was heard, and all rows are clean.

#### 1. Frames
Default, card, sheet, trail middle, trail end, Clusters grid and ladder at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080 and 760x900 (f/default-*, card-*, sheet-*, trailmid-*, trailend-*, grid-*, ladder-*). At 375 through
the iframe host: default, card, sheet, trail end, grid, two ladders (f/n375-*), no sideways scroll (scrollWidth 375). All
14 lit at 1366 and 680 and in the grid (f/alllit-*). Motion off (f/calm-default-1366x768, f/calm-check: Curio.reduce true,
no running animations with a card open). No placeholders anywhere. No text sits over a picture: card and sheet text is on
solid panels. No clipped words and no overlaps, apart from the carried items below. Lanterns are readable at every size,
and labels are large at 1920.

#### 2. Art against the spec
Nothing to check: no `art:` tokens, art/prompts.json has no assets, and the drawn town matches the spec's flat, layered
night look in every frame. There are no people pictures (the careers use emoji).

#### 3. Voice with the real clips
Clip text: I ran each mp3 and raw take through Whisper base.en. All 9 say exactly their line in voice/lines.json (only
punctuation and "14" vs "fourteen" differ). In the bundle, every line text maps to its own clip (base64 matched per file).
Lengths are 2.38 to 5.36 s, and no clip is very short.

Timing (I logged each Audio play, end and pause next to `__tool.vlog`):
- v2/v1-marker-job-esc (fresh): welcomeFestival plays 1.36 to 6.08 s in full. A job tapped at about 2.9 s lights the
  lantern, and lanternHow waits for the welcome to finish. After Esc twice, lanternHow plays 8.10 to 12.40 s, then panHow
  12.93 to 17.22 s. Nothing overlaps and nothing is cut.
- v/v2-trails: welcomeTrails plays 1.35 to 5.20 s, and trailEnd4 waits for it, then plays 6.06 to 8.48 s while the end
  card shows "took 4 clusters". The line matches the screen.
- v2/v3-trailend-x5: trailEnd4 spoken 5 of 5, each clip ending in full; welcomeTrails once.
- v2/v5-alllit: 13 lit, then the first tap is the ridge's job: welcome 1.44 to 6.15 s, then allLit 6.32 to 11.75 s, in
  full and after the welcome.
- v/v6-read: Read 1.1 s into welcomeTrails pauses that clip and plays the hint (it is the same line, so its clip plays). Read
  is not cut off.
- v/v7-fast: fast taps (0.25 s) through a trail, then Festival: welcomeTrails is hushed, the queued trailEnd3 is dropped
  (hush), and welcomeFestival starts at once. No stale line plays.
- v/v8-sound-toggle: the Sound tap says nothing. Sound back on brings the skipped welcome once.

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeFestival | how | 1 | 1 |
| lanternHow | how | 1 | 1 |
| panHow | how | 1 | 1 |
| welcomeTrails | how | 1 | 1 |
| trailEnd4 | event | 5 | 5 |
| allLit | event | 1 (once all 14 are lit) | 1 |
| welcomeClusters | how | 1 | 1 |

Liveliness (`scripts/voice_liveliness.py`): only line 4 is flagged: welcomeTrails, "Pick a trail, then tap Next to
follow it across the fair.", with semitone SD 2.98 against the 3.0 threshold and the narrowest range, 9.3. It is a
how-to line heard once, when Trails opens. Its rate (14.8 c/s) and its transcript are normal, and it sits on the
threshold, not clearly flat. Judged: it can stay (RUNBOOK: a flag or two is normal). See polish item 2.

#### 4. Full run, solo student and teacher projecting
Solo: the first screen and its spoken welcome say what to do. Every waiting moment names its control (card, sheet,
trail, ladder hints read from the DOM in every shot). The real voice keeps up with a fast student, because lines queue
behind the welcome instead of being lost. Projected at 1920x1080: lanterns, the panel and the trail card read from a
distance. Nothing felt slow, except polish item 1.

#### 5. Contract
330 KB with all 9 clips inlined (9 data:audio/mpeg URIs). No fetch or XHR in the bundle and no external src/href
resources. No console errors or exceptions in any shot (0 of about 75). No em dashes in the bundle.

#### Findings

1. **polish (general)**, Clusters: welcomeClusters runs on over the opened ladder. A student who taps a cluster 1 s after
   entering still hears "Tap a cluster to see its ways in..." for about 3 s more while the ladder already shows
   (v2/v4-clusters: the clip plays 1.35 to 5.74 s, the ladder opens at about 2.4 s). The real clip (4.36 s) holds it a little
   longer than the browser read. Better: give the welcome a `valid` of `state.cluster === null`, and let openCluster cut
   the welcome if it is still playing (or hush), so the line stops once its step is done.
2. **polish (general)**, voice line 4 (welcomeTrails): it is on the liveliness threshold (2.98). It is optional and
   low priority. If Cory hears it as bored, run `localvoice.py career-cluster-explorer --redo 4 --takes 5`. Otherwise
   keep it.
3. **polish (general)**, carried from refine.md item 26: at 1366x768 the trail stop header still wraps ("BEHIND THE
   KETTLE CORN: / STOP 5 OF 5", f/trailend-1366x768). At 800x500 it is a single "STOP 5 OF 5" (f/trailend-800x500).
4. **nit (general)**: allLit plays while the career sheet still covers the lantern strip (v2/v5-alllit, sheet open at
   11.75 s). The sheet's own "lantern: lit" line is in view and the shimmer waits for the close, so it still reads.
   Same as the exit check's lanternHow nit.
5. **nit (general)**, carried: at 680x425 the Ferris wheel card's fourth job runs to the stage edge (f/card-680x425).

6. **nit (general)**: at 375 in Clusters, the hint sits below the 14-tile grid, out of view until the student scrolls
   (audit lead, f/n375-grid). The welcome speaks it, and the grid's own "Ways in" tile says the same, so it still reads.

No blockers or should-fix items. The real clips broke nothing that Refine passed.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/final-sensitivity.md folded in (last changed 2026-10-29)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/sensitivity.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: review-fix.md folded in (last changed 2026-10-29)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)
- 2026-11-25: final-art.md folded in (last changed 2026-10-29)
- 2026-11-25: final.md folded in (last changed 2026-10-29)
